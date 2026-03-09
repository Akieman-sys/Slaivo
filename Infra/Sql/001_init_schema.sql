create extension if not exists pgcrypto;

create table if not exists shipments (
    id uuid primary key default gen_random_uuid(),
    tracking_id text not null unique,
    client_name text,
    client_phone text not null,
    origin text,
    destination text,
    cargo_type text not null default 'unknown',
    status text not null,
    last_update_at timestamptz not null,
    eta timestamptz,
    fees_due numeric(12,2),
    fees_paid numeric(12,2),
    balance numeric(12,2),
    currency text,
    notes_internal text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    constraint shipments_cargo_type_check check (cargo_type in ('air', 'sea', 'road', 'unknown')),
    constraint shipments_status_check check (
        status in (
            'RECEIVED',
            'DEPARTED',
            'IN_TRANSIT',
            'ARRIVED',
            'IN_CUSTOMS',
            'CLEARED',
            'ARRIVED_KIN',
            'READY_FOR_PICKUP',
            'DELIVERED',
            'ISSUE'
        )
    )
);

create table if not exists conversations (
    id uuid primary key default gen_random_uuid(),
    customer_phone text not null,
    channel text not null default 'whatsapp',
    status text not null default 'open',
    assigned_to text,
    priority text not null default 'low',
    last_message_at timestamptz,
    related_shipment_id uuid references shipments(id) on delete set null,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    constraint conversations_status_check check (status in ('open', 'pending', 'resolved')),
    constraint conversations_priority_check check (priority in ('low', 'medium', 'high'))
);

create table if not exists messages (
    id uuid primary key default gen_random_uuid(),
    conversation_id uuid not null references conversations(id) on delete cascade,
    provider_message_id text,
    direction text not null,
    message_type text not null default 'text',
    text_body text,
    intent text,
    trigger_type text,
    status text,
    from_phone text not null,
    to_phone text not null,
    related_shipment_id uuid references shipments(id) on delete set null,
    raw_payload jsonb,
    dedupe_key text,
    sent_at timestamptz,
    received_at timestamptz,
    created_at timestamptz not null default now(),
    constraint messages_direction_check check (direction in ('inbound', 'outbound'))
);

create table if not exists escalations (
    id uuid primary key default gen_random_uuid(),
    conversation_id uuid not null references conversations(id) on delete cascade,
    customer_phone text not null,
    reason_code text not null,
    reason_detail text,
    related_shipment_id uuid references shipments(id) on delete set null,
    priority text not null,
    suggested_tag text,
    status text not null default 'open',
    triggered_at timestamptz not null default now(),
    resolved_at timestamptz,
    created_at timestamptz not null default now(),
    constraint escalations_priority_check check (priority in ('low', 'medium', 'high')),
    constraint escalations_status_check check (status in ('open', 'resolved'))
);

create table if not exists event_notifications (
    id uuid primary key default gen_random_uuid(),
    shipment_id uuid not null references shipments(id) on delete cascade,
    conversation_id uuid references conversations(id) on delete set null,
    event_type text not null,
    channel text not null default 'whatsapp',
    status text not null,
    cooldown_key text,
    template_name text,
    message_text text,
    failure_reason text,
    sent_at timestamptz,
    created_at timestamptz not null default now(),
    constraint event_notifications_status_check check (status in ('pending', 'sent', 'blocked', 'failed'))
);

create table if not exists knowledge_items (
    id uuid primary key default gen_random_uuid(),
    item_type text not null,
    title text not null,
    key text not null unique,
    content jsonb not null,
    is_active boolean not null default true,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists idx_shipments_tracking_id on shipments(tracking_id);
create index if not exists idx_shipments_client_phone on shipments(client_phone);
create index if not exists idx_conversations_customer_phone on conversations(customer_phone);
create index if not exists idx_messages_conversation_created_at on messages(conversation_id, created_at desc);
create index if not exists idx_messages_provider_message_id on messages(provider_message_id);
create index if not exists idx_escalations_conversation_id on escalations(conversation_id);
create index if not exists idx_event_notifications_shipment_event on event_notifications(shipment_id, event_type);
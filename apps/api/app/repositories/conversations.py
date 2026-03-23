from app.core.db import get_db_connection


def list_conversations() -> list[dict]:
    query = """
        select
            id,
            customer_phone,
            channel,
            status,
            assigned_to,
            priority,
            last_message_at,
            related_shipment_id,
            created_at,
            updated_at
        from conversations
        order by updated_at desc
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]


def assign_conversation(conversation_id: str, assigned_to: str) -> dict | None:
    query = """
        update conversations
        set assigned_to = %s,
            updated_at = now()
        where id = %s
        returning
            id,
            customer_phone,
            channel,
            status,
            assigned_to,
            priority,
            last_message_at,
            related_shipment_id,
            created_at,
            updated_at
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (assigned_to, conversation_id))
            row = cur.fetchone()

            if not row:
                return None

            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))


def find_conversation_by_customer_phone(customer_phone: str) -> dict | None:
    query = """
        select
            id,
            customer_phone,
            channel,
            status,
            assigned_to,
            priority,
            last_message_at,
            related_shipment_id,
            created_at,
            updated_at
        from conversations
        where customer_phone = %s
          and channel = 'whatsapp'
        order by updated_at desc
        limit 1
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (customer_phone,))
            row = cur.fetchone()
            if not row:
                return None

            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))


def create_conversation(
    customer_phone: str,
    related_shipment_id: str | None = None,
    priority: str = "low",
) -> dict:
    query = """
        insert into conversations (
            customer_phone,
            channel,
            status,
            assigned_to,
            priority,
            last_message_at,
            related_shipment_id
        )
        values (
            %s,
            'whatsapp',
            'open',
            null,
            %s,
            now(),
            %s
        )
        returning
            id,
            customer_phone,
            channel,
            status,
            assigned_to,
            priority,
            last_message_at,
            related_shipment_id,
            created_at,
            updated_at
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (customer_phone, priority, related_shipment_id))
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))


def touch_conversation(conversation_id: str) -> None:
    query = """
        update conversations
        set last_message_at = now(),
            updated_at = now()
        where id = %s
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (conversation_id,))
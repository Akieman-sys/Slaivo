from app.core.db import get_db_connection
from psycopg.types.json import Json




def create_agent_outbound_message(
    conversation_id: str,
    from_phone: str,
    to_phone: str,
    text_body: str,
    related_shipment_id: str | None = None,
) -> dict:
    query = """
        insert into messages (
            conversation_id,
            direction,
            message_type,
            text_body,
            trigger_type,
            status,
            from_phone,
            to_phone,
            related_shipment_id,
            sent_at
        )
        values (
            %s,
            'outbound',
            'text',
            %s,
            'agent_reply',
            'pending',
            %s,
            %s,
            %s,
            now()
        )
        returning
            id,
            conversation_id,
            direction,
            message_type,
            text_body,
            trigger_type,
            status,
            from_phone,
            to_phone,
            related_shipment_id,
            sent_at,
            created_at
    """

    update_conversation_query = """
        update conversations
        set last_message_at = now(),
            updated_at = now()
        where id = %s
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select customer_phone, related_shipment_id
                from conversations
                where id = %s
                limit 1
                """,
                (conversation_id,),
            )
            conversation = cur.fetchone()
            if not conversation:
                raise ValueError("Conversation not found")

            customer_phone, conversation_related_shipment_id = conversation
            final_related_shipment_id = related_shipment_id or conversation_related_shipment_id

            cur.execute(
                query,
                (
                    conversation_id,
                    text_body,
                    from_phone,
                    customer_phone if not to_phone else to_phone,
                    final_related_shipment_id,
                ),
            )
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]

            cur.execute(update_conversation_query, (conversation_id,))

            return dict(zip(columns, row))

def create_system_outbound_message(
    conversation_id: str,
    from_phone: str,
    to_phone: str,
    text_body: str,
    trigger_type: str,
    related_shipment_id: str | None = None,
) -> dict:
    query = """
        insert into messages (
            conversation_id,
            direction,
            message_type,
            text_body,
            trigger_type,
            status,
            from_phone,
            to_phone,
            related_shipment_id,
            sent_at
        )
        values (
            %s,
            'outbound',
            'text',
            %s,
            %s,
            'pending',
            %s,
            %s,
            %s,
            now()
        )
        returning
            id,
            conversation_id,
            direction,
            message_type,
            text_body,
            trigger_type,
            status,
            from_phone,
            to_phone,
            related_shipment_id,
            sent_at,
            created_at
    """

    update_conversation_query = """
        update conversations
        set last_message_at = now(),
            updated_at = now()
        where id = %s
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                query,
                (
                    conversation_id,
                    text_body,
                    trigger_type,
                    from_phone,
                    to_phone,
                    related_shipment_id,
                ),
            )
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]

            cur.execute(update_conversation_query, (conversation_id,))
            return dict(zip(columns, row))
        

def create_inbound_message(
    conversation_id: str,
    provider_message_id: str | None,
    message_type: str,
    text_body: str | None,
    intent: str | None,
    from_phone: str,
    to_phone: str,
    raw_payload: dict | None = None,
    related_shipment_id: str | None = None,
    dedupe_key: str | None = None,
    received_at: str | None = None,
) -> dict:
    query = """
        insert into messages (
            conversation_id,
            provider_message_id,
            direction,
            message_type,
            text_body,
            intent,
            status,
            from_phone,
            to_phone,
            related_shipment_id,
            raw_payload,
            dedupe_key,
            received_at
        )
        values (
            %s,
            %s,
            'inbound',
            %s,
            %s,
            %s,
            'received',
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        returning
            id,
            conversation_id,
            provider_message_id,
            direction,
            message_type,
            text_body,
            intent,
            status,
            from_phone,
            to_phone,
            related_shipment_id,
            raw_payload,
            dedupe_key,
            received_at,
            created_at
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                query,
                (
                    conversation_id,
                    provider_message_id,
                    message_type,
                    text_body,
                    intent,
                    from_phone,
                    to_phone,
                    related_shipment_id,
                    Json(raw_payload) if raw_payload is not None else None,
                    dedupe_key,
                    received_at,
                ),
            )
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))
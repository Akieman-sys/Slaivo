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
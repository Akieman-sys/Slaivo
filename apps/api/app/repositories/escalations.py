from app.core.db import get_db_connection


def list_open_escalations() -> list[dict]:
    query = """
        select
            id,
            conversation_id,
            customer_phone,
            reason_code,
            reason_detail,
            related_shipment_id,
            priority,
            suggested_tag,
            status,
            triggered_at,
            resolved_at,
            created_at
        from escalations
        where status = 'open'
        order by triggered_at desc
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
from app.core.db import get_db_connection


def find_shipment_by_tracking_id(tracking_id: str) -> dict | None:
    query = """
        select
            id,
            tracking_id,
            client_name,
            client_phone,
            origin,
            destination,
            cargo_type,
            status,
            last_update_at,
            eta,
            fees_due,
            fees_paid,
            balance,
            currency
        from shipments
        where tracking_id = %s
        limit 1
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (tracking_id,))
            row = cur.fetchone()

            if not row:
                return None

            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))
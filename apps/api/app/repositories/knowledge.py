from app.core.db import get_db_connection


def find_active_knowledge_item(item_type: str) -> dict | None:
    query = """
        select
            id,
            item_type,
            title,
            key,
            content,
            is_active,
            created_at,
            updated_at
        from knowledge_items
        where item_type = %s
          and is_active = true
        order by created_at desc
        limit 1
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (item_type,))
            row = cur.fetchone()

            if not row:
                return None

            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))
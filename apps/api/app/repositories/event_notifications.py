from app.core.db import get_db_connection


def find_recent_event_notification(shipment_id: str, event_type: str) -> dict | None:
    query = """
        select
            id,
            shipment_id,
            conversation_id,
            event_type,
            channel,
            status,
            cooldown_key,
            template_name,
            message_text,
            failure_reason,
            sent_at,
            created_at
        from event_notifications
        where shipment_id = %s
          and event_type = %s
          and created_at >= now() - interval '24 hours'
        order by created_at desc
        limit 1
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (shipment_id, event_type))
            row = cur.fetchone()
            if not row:
                return None

            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))


def create_event_notification(
    shipment_id: str,
    conversation_id: str | None,
    event_type: str,
    status: str,
    cooldown_key: str | None,
    message_text: str | None,
    failure_reason: str | None = None,
) -> dict:
    query = """
        insert into event_notifications (
            shipment_id,
            conversation_id,
            event_type,
            channel,
            status,
            cooldown_key,
            message_text,
            failure_reason,
            sent_at
        )
        values (
            %s,
            %s,
            %s,
            'whatsapp',
            %s,
            %s,
            %s,
            %s,
            now()
        )
        returning
            id,
            shipment_id,
            conversation_id,
            event_type,
            channel,
            status,
            cooldown_key,
            template_name,
            message_text,
            failure_reason,
            sent_at,
            created_at
    """

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                query,
                (
                    shipment_id,
                    conversation_id,
                    event_type,
                    status,
                    cooldown_key,
                    message_text,
                    failure_reason,
                ),
            )
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            return dict(zip(columns, row))
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.repositories.conversations import list_conversations, assign_conversation
from app.repositories.escalations import list_open_escalations
from app.repositories.messages import create_agent_outbound_message

router = APIRouter()


class AssignConversationRequest(BaseModel):
    assigned_to: str


class AgentReplyRequest(BaseModel):
    from_phone: str
    text_body: str
    to_phone: str | None = None
    related_shipment_id: str | None = None


@router.get("/conversations")
def get_conversations():
    return {"items": list_conversations()}


@router.get("/escalations")
def get_escalations():
    return {"items": list_open_escalations()}


@router.post("/conversations/{conversation_id}/assign")
def assign_conversation_route(conversation_id: str, body: AssignConversationRequest):
    updated = assign_conversation(conversation_id, body.assigned_to)

    if not updated:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {"item": updated}


@router.post("/conversations/{conversation_id}/reply")
def reply_to_conversation(conversation_id: str, body: AgentReplyRequest):
    try:
        message = create_agent_outbound_message(
            conversation_id=conversation_id,
            from_phone=body.from_phone,
            to_phone=body.to_phone,
            text_body=body.text_body,
            related_shipment_id=body.related_shipment_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    return {"item": message}
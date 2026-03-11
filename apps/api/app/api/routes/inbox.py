from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.repositories.conversations import list_conversations, assign_conversation
from app.repositories.escalations import list_open_escalations

router = APIRouter()


class AssignConversationRequest(BaseModel):
    assigned_to: str


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
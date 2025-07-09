from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional,  Union

class Message(BaseModel):   
    content: Optional[str] = None
    image: Optional[Union[str, bytes]] = None
    timestamp: Optional[datetime] = None

class Conversation(BaseModel):
    id: str
    user_id: str
    title: str
    created_at: datetime
    messages: List[Message] = Field(default_factory=list)

class UpdateConversationRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="New title for the conversation")
from microsoft.agents.core.models import AgentsModel, ConversationReference


class AgentConversationReference(AgentsModel):
    conversation_reference: ConversationReference
    oauth_scope: str

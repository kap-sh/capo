"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_configuration
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier
    import capo_bedrock_agent_runtime.types.knowledge_base_query
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.user_context


class RetrieveRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier"
    """<p>The unique identifier of the knowledge base to query.</p>"""
    retrieval_query: (
        "capo_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery"
    )
    """<p>Contains the query to send the knowledge base.</p>"""
    retrieval_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    ]
    """<p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>"""
    guardrail_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Guardrail settings.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>"""
    user_context: NotRequired[
        "capo_bedrock_agent_runtime.types.user_context.UserContext"
    ]
    """<p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.knowledge_base_query

    out["retrievalQuery"] = (
        capo_bedrock_agent_runtime.types.knowledge_base_query.serialize_json(
            value["retrieval_query"]
        )
    )
    if "retrieval_configuration" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrievalConfiguration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.serialize_json(
                value["retrieval_configuration"]
            )
        )
    if "guardrail_configuration" in value:
        import capo_bedrock_agent_runtime.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            capo_bedrock_agent_runtime.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "user_context" in value:
        import capo_bedrock_agent_runtime.types.user_context

        out["userContext"] = (
            capo_bedrock_agent_runtime.types.user_context.serialize_json(
                value["user_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrieveRequest:
    out: RetrieveRequest = {}  # type: ignore[typeddict-item]
    if data.get("retrievalQuery") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_query

        out["retrieval_query"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_query.deserialize_json(
                data["retrievalQuery"]
            )
        )
    else:
        raise DeserializationError("RetrieveRequest.retrieval_query required")
    if data.get("retrievalConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrieval_configuration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    if data.get("guardrailConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_configuration

        out["guardrail_configuration"] = (
            capo_bedrock_agent_runtime.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("userContext") is not None:
        import capo_bedrock_agent_runtime.types.user_context

        out["user_context"] = (
            capo_bedrock_agent_runtime.types.user_context.deserialize_json(
                data["userContext"]
            )
        )
    return out

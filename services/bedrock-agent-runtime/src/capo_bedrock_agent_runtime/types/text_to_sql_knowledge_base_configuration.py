"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextToSqlKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_arn


class TextToSqlKnowledgeBaseConfiguration(TypedDict, closed=True):
    knowledge_base_arn: (
        "capo_bedrock_agent_runtime.types.knowledge_base_arn.KnowledgeBaseArn"
    )
    """<p>The ARN of the knowledge base</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextToSqlKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> TextToSqlKnowledgeBaseConfiguration:
    out: TextToSqlKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    return out

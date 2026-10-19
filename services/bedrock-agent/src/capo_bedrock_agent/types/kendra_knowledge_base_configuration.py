"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KendraKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.kendra_index_arn


class KendraKnowledgeBaseConfiguration(TypedDict, closed=True):
    kendra_index_arn: "capo_bedrock_agent.types.kendra_index_arn.KendraIndexArn"
    """<p>The ARN of the Amazon Kendra index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KendraKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    out["kendraIndexArn"] = value["kendra_index_arn"]
    return out


def deserialize_json(data: dict) -> KendraKnowledgeBaseConfiguration:
    out: KendraKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kendraIndexArn") is not None:
        out["kendra_index_arn"] = data["kendraIndexArn"]
    else:
        out["kendra_index_arn"] = ""
    return out

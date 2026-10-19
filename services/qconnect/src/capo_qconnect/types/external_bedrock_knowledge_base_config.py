"""Generated from Smithy shape ``com.amazonaws.qconnect#ExternalBedrockKnowledgeBaseConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.access_role_arn
    import capo_qconnect.types.bedrock_knowledge_base_arn


class ExternalBedrockKnowledgeBaseConfig(TypedDict, closed=True):
    bedrock_knowledge_base_arn: (
        "capo_qconnect.types.bedrock_knowledge_base_arn.BedrockKnowledgeBaseArn"
    )
    """<p>The Amazon Resource Name (ARN) of the external Bedrock knowledge base.</p>"""
    access_role_arn: "capo_qconnect.types.access_role_arn.AccessRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role used to access the external Bedrock knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalBedrockKnowledgeBaseConfig) -> dict:
    out: dict = {}
    out["bedrockKnowledgeBaseArn"] = value["bedrock_knowledge_base_arn"]
    out["accessRoleArn"] = value["access_role_arn"]
    return out


def deserialize_json(data: dict) -> ExternalBedrockKnowledgeBaseConfig:
    out: ExternalBedrockKnowledgeBaseConfig = {}  # type: ignore[typeddict-item]
    if data.get("bedrockKnowledgeBaseArn") is not None:
        out["bedrock_knowledge_base_arn"] = data["bedrockKnowledgeBaseArn"]
    else:
        out["bedrock_knowledge_base_arn"] = ""
    if data.get("accessRoleArn") is not None:
        out["access_role_arn"] = data["accessRoleArn"]
    else:
        out["access_role_arn"] = ""
    return out

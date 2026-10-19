"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#QConnectIntegrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn


class QConnectIntegrationConfig(TypedDict, closed=True):
    knowledge_base_arn: "capo_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: QConnectIntegrationConfig) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> QConnectIntegrationConfig:
    out: QConnectIntegrationConfig = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    return out

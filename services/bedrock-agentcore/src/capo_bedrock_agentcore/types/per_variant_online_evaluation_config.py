"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PerVariantOnlineEvaluationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.online_evaluation_config_arn
    import capo_bedrock_agentcore.types.variant_name


class PerVariantOnlineEvaluationConfig(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.variant_name.VariantName"
    """<p>The name of the variant this evaluation configuration applies to.</p>"""
    online_evaluation_config_arn: "capo_bedrock_agentcore.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p>The Amazon Resource Name (ARN) of the online evaluation configuration for this variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerVariantOnlineEvaluationConfig) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    return out


def deserialize_json(data: dict) -> PerVariantOnlineEvaluationConfig:
    out: PerVariantOnlineEvaluationConfig = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("onlineEvaluationConfigArn") is not None:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        out["online_evaluation_config_arn"] = ""
    return out

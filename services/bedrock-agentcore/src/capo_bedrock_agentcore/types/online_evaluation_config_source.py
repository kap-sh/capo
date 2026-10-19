"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OnlineEvaluationConfigSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.online_evaluation_config_arn
    import capo_bedrock_agentcore.types.session_filter_config


class OnlineEvaluationConfigSource(TypedDict, closed=True):
    online_evaluation_config_arn: "capo_bedrock_agentcore.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p>The Amazon Resource Name (ARN) of the online evaluation configuration to use as the session source.</p>"""
    time_range: NotRequired[
        "capo_bedrock_agentcore.types.session_filter_config.SessionFilterConfig"
    ]
    """<p>Optional session filter configuration to narrow down which sessions from the online evaluation configuration to include.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnlineEvaluationConfigSource) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    if "time_range" in value:
        import capo_bedrock_agentcore.types.session_filter_config

        out["timeRange"] = (
            capo_bedrock_agentcore.types.session_filter_config.serialize_json(
                value["time_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> OnlineEvaluationConfigSource:
    out: OnlineEvaluationConfigSource = {}  # type: ignore[typeddict-item]
    if data.get("onlineEvaluationConfigArn") is not None:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        out["online_evaluation_config_arn"] = ""
    if data.get("timeRange") is not None:
        import capo_bedrock_agentcore.types.session_filter_config

        out["time_range"] = (
            capo_bedrock_agentcore.types.session_filter_config.deserialize_json(
                data["timeRange"]
            )
        )
    return out

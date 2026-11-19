"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OnlineEvaluationSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.online_evaluation_config_arn


class OnlineEvaluationSourceConfig(TypedDict, closed=True):
    online_evaluation_config_arn: "capo_bedrock_agentcore.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p>The Amazon Resource Name (ARN) of the online evaluation configuration.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start of the time window to read sessions from. The default is 7 days before <code>endTime</code>.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end of the time window to read sessions from. The default is the time the generation starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnlineEvaluationSourceConfig) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    if "start_time" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["startTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["endTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> OnlineEvaluationSourceConfig:
    out: OnlineEvaluationSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("onlineEvaluationConfigArn") is not None:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        out["online_evaluation_config_arn"] = ""
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    return out

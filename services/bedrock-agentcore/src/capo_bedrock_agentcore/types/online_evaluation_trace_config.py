"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OnlineEvaluationTraceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.online_evaluation_config_arn


class OnlineEvaluationTraceConfig(TypedDict, closed=True):
    online_evaluation_config_arn: "capo_bedrock_agentcore.types.online_evaluation_config_arn.OnlineEvaluationConfigArn"
    """<p>The ARN of the online evaluation configuration to reuse sessions from.</p>"""
    start_time: "datetime.datetime"
    """<p>The start time of the time range. Only sessions evaluated at or after this timestamp are included.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time of the time range. Only sessions evaluated before this timestamp are included.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnlineEvaluationTraceConfig) -> dict:
    out: dict = {}
    out["onlineEvaluationConfigArn"] = value["online_evaluation_config_arn"]
    import capo_bedrock_agentcore._protocol.serialize

    out["startTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_bedrock_agentcore._protocol.serialize

    out["endTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> OnlineEvaluationTraceConfig:
    out: OnlineEvaluationTraceConfig = {}  # type: ignore[typeddict-item]
    if data.get("onlineEvaluationConfigArn") is not None:
        out["online_evaluation_config_arn"] = data["onlineEvaluationConfigArn"]
    else:
        out["online_evaluation_config_arn"] = ""
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

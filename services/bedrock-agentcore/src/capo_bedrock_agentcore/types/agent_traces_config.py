"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentTracesConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.batch_evaluation_trace_config
    import capo_bedrock_agentcore.types.cloud_watch_logs_trace_config
    import capo_bedrock_agentcore.types.online_evaluation_trace_config
    import capo_bedrock_agentcore.types.spans


class _AgentTracesConfig_sessionSpans(TypedDict, closed=True):
    sessionSpans: "capo_bedrock_agentcore.types.spans.Spans"


class _AgentTracesConfig_cloudwatchLogs(TypedDict, closed=True):
    cloudwatchLogs: "capo_bedrock_agentcore.types.cloud_watch_logs_trace_config.CloudWatchLogsTraceConfig"


class _AgentTracesConfig_batchEvaluation(TypedDict, closed=True):
    batchEvaluation: "capo_bedrock_agentcore.types.batch_evaluation_trace_config.BatchEvaluationTraceConfig"


class _AgentTracesConfig_onlineEvaluation(TypedDict, closed=True):
    onlineEvaluation: "capo_bedrock_agentcore.types.online_evaluation_trace_config.OnlineEvaluationTraceConfig"


AgentTracesConfig: TypeAlias = (
    _AgentTracesConfig_sessionSpans
    | _AgentTracesConfig_cloudwatchLogs
    | _AgentTracesConfig_batchEvaluation
    | _AgentTracesConfig_onlineEvaluation
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AgentTracesConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgentTracesConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sessionSpans" in value:
        import capo_bedrock_agentcore.types.spans

        return {
            "sessionSpans": capo_bedrock_agentcore.types.spans.serialize_json(
                value["sessionSpans"]
            )
        }
    elif "cloudwatchLogs" in value:
        import capo_bedrock_agentcore.types.cloud_watch_logs_trace_config

        return {
            "cloudwatchLogs": capo_bedrock_agentcore.types.cloud_watch_logs_trace_config.serialize_json(
                value["cloudwatchLogs"]
            )
        }
    elif "batchEvaluation" in value:
        import capo_bedrock_agentcore.types.batch_evaluation_trace_config

        return {
            "batchEvaluation": capo_bedrock_agentcore.types.batch_evaluation_trace_config.serialize_json(
                value["batchEvaluation"]
            )
        }
    elif "onlineEvaluation" in value:
        import capo_bedrock_agentcore.types.online_evaluation_trace_config

        return {
            "onlineEvaluation": capo_bedrock_agentcore.types.online_evaluation_trace_config.serialize_json(
                value["onlineEvaluation"]
            )
        }
    else:
        raise SerializationError("AgentTracesConfig: no variant present")


def deserialize_json(data: dict) -> AgentTracesConfig:
    if data.get("sessionSpans") is not None:
        import capo_bedrock_agentcore.types.spans

        return {
            "sessionSpans": capo_bedrock_agentcore.types.spans.deserialize_json(
                data["sessionSpans"]
            )
        }
    elif data.get("cloudwatchLogs") is not None:
        import capo_bedrock_agentcore.types.cloud_watch_logs_trace_config

        return {
            "cloudwatchLogs": capo_bedrock_agentcore.types.cloud_watch_logs_trace_config.deserialize_json(
                data["cloudwatchLogs"]
            )
        }
    elif data.get("batchEvaluation") is not None:
        import capo_bedrock_agentcore.types.batch_evaluation_trace_config

        return {
            "batchEvaluation": capo_bedrock_agentcore.types.batch_evaluation_trace_config.deserialize_json(
                data["batchEvaluation"]
            )
        }
    elif data.get("onlineEvaluation") is not None:
        import capo_bedrock_agentcore.types.online_evaluation_trace_config

        return {
            "onlineEvaluation": capo_bedrock_agentcore.types.online_evaluation_trace_config.deserialize_json(
                data["onlineEvaluation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AgentTracesConfig: no recognized variant key")


def redact_sensitive(value: AgentTracesConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sessionSpans" in value:
        out["sessionSpans"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TraceSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.batch_evaluation_source_config
    import capo_bedrock_agentcore.types.cloud_watch_logs_source_config
    import capo_bedrock_agentcore.types.online_evaluation_source_config


class TraceSourceConfigCloudWatchLogsMember(TypedDict, closed=True):
    cloudWatchLogs: "capo_bedrock_agentcore.types.cloud_watch_logs_source_config.CloudWatchLogsSourceConfig"


class TraceSourceConfigOnlineEvaluationMember(TypedDict, closed=True):
    onlineEvaluation: "capo_bedrock_agentcore.types.online_evaluation_source_config.OnlineEvaluationSourceConfig"


class TraceSourceConfigBatchEvaluationMember(TypedDict, closed=True):
    batchEvaluation: "capo_bedrock_agentcore.types.batch_evaluation_source_config.BatchEvaluationSourceConfig"


TraceSourceConfig: TypeAlias = (
    TraceSourceConfigCloudWatchLogsMember
    | TraceSourceConfigOnlineEvaluationMember
    | TraceSourceConfigBatchEvaluationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TraceSourceConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TraceSourceConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cloudWatchLogs" in value:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source_config

        return {
            "cloudWatchLogs": capo_bedrock_agentcore.types.cloud_watch_logs_source_config.serialize_json(
                value["cloudWatchLogs"]
            )
        }
    elif "onlineEvaluation" in value:
        import capo_bedrock_agentcore.types.online_evaluation_source_config

        return {
            "onlineEvaluation": capo_bedrock_agentcore.types.online_evaluation_source_config.serialize_json(
                value["onlineEvaluation"]
            )
        }
    elif "batchEvaluation" in value:
        import capo_bedrock_agentcore.types.batch_evaluation_source_config

        return {
            "batchEvaluation": capo_bedrock_agentcore.types.batch_evaluation_source_config.serialize_json(
                value["batchEvaluation"]
            )
        }
    else:
        raise SerializationError("TraceSourceConfig: no variant present")


def deserialize_json(data: dict) -> TraceSourceConfig:
    if data.get("cloudWatchLogs") is not None:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source_config

        return {
            "cloudWatchLogs": capo_bedrock_agentcore.types.cloud_watch_logs_source_config.deserialize_json(
                data["cloudWatchLogs"]
            )
        }
    elif data.get("onlineEvaluation") is not None:
        import capo_bedrock_agentcore.types.online_evaluation_source_config

        return {
            "onlineEvaluation": capo_bedrock_agentcore.types.online_evaluation_source_config.deserialize_json(
                data["onlineEvaluation"]
            )
        }
    elif data.get("batchEvaluation") is not None:
        import capo_bedrock_agentcore.types.batch_evaluation_source_config

        return {
            "batchEvaluation": capo_bedrock_agentcore.types.batch_evaluation_source_config.deserialize_json(
                data["batchEvaluation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TraceSourceConfig: no recognized variant key")

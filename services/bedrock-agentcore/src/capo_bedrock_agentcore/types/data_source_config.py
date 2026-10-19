"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DataSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.cloud_watch_logs_source
    import capo_bedrock_agentcore.types.online_evaluation_config_source


class _DataSourceConfig_cloudWatchLogs(TypedDict, closed=True):
    cloudWatchLogs: (
        "capo_bedrock_agentcore.types.cloud_watch_logs_source.CloudWatchLogsSource"
    )


class _DataSourceConfig_onlineEvaluationConfigSource(TypedDict, closed=True):
    onlineEvaluationConfigSource: "capo_bedrock_agentcore.types.online_evaluation_config_source.OnlineEvaluationConfigSource"


DataSourceConfig: TypeAlias = (
    _DataSourceConfig_cloudWatchLogs
    | _DataSourceConfig_onlineEvaluationConfigSource
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DataSourceConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "cloudWatchLogs" in value:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source

        return {
            "cloudWatchLogs": capo_bedrock_agentcore.types.cloud_watch_logs_source.serialize_json(
                value["cloudWatchLogs"]
            )
        }
    elif "onlineEvaluationConfigSource" in value:
        import capo_bedrock_agentcore.types.online_evaluation_config_source

        return {
            "onlineEvaluationConfigSource": capo_bedrock_agentcore.types.online_evaluation_config_source.serialize_json(
                value["onlineEvaluationConfigSource"]
            )
        }
    else:
        raise SerializationError("DataSourceConfig: no variant present")


def deserialize_json(data: dict) -> DataSourceConfig:
    if data.get("cloudWatchLogs") is not None:
        import capo_bedrock_agentcore.types.cloud_watch_logs_source

        return {
            "cloudWatchLogs": capo_bedrock_agentcore.types.cloud_watch_logs_source.deserialize_json(
                data["cloudWatchLogs"]
            )
        }
    elif data.get("onlineEvaluationConfigSource") is not None:
        import capo_bedrock_agentcore.types.online_evaluation_config_source

        return {
            "onlineEvaluationConfigSource": capo_bedrock_agentcore.types.online_evaluation_config_source.deserialize_json(
                data["onlineEvaluationConfigSource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DataSourceConfig: no recognized variant key")

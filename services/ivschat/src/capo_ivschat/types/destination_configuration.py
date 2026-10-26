"""Generated from Smithy shape ``com.amazonaws.ivschat#DestinationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ivschat.errors import DeserializationError, SerializationError
from capo_ivschat.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ivschat.types.cloud_watch_logs_destination_configuration
    import capo_ivschat.types.firehose_destination_configuration
    import capo_ivschat.types.s3_destination_configuration


class _DestinationConfiguration_s3(TypedDict, closed=True):
    s3: "capo_ivschat.types.s3_destination_configuration.S3DestinationConfiguration"


class _DestinationConfiguration_cloudWatchLogs(TypedDict, closed=True):
    cloudWatchLogs: "capo_ivschat.types.cloud_watch_logs_destination_configuration.CloudWatchLogsDestinationConfiguration"


class _DestinationConfiguration_firehose(TypedDict, closed=True):
    firehose: "capo_ivschat.types.firehose_destination_configuration.FirehoseDestinationConfiguration"


DestinationConfiguration: TypeAlias = (
    _DestinationConfiguration_s3
    | _DestinationConfiguration_cloudWatchLogs
    | _DestinationConfiguration_firehose
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DestinationConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_ivschat.types.s3_destination_configuration

        return {
            "s3": capo_ivschat.types.s3_destination_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "cloudWatchLogs" in value:
        import capo_ivschat.types.cloud_watch_logs_destination_configuration

        return {
            "cloudWatchLogs": capo_ivschat.types.cloud_watch_logs_destination_configuration.serialize_json(
                value["cloudWatchLogs"]
            )
        }
    elif "firehose" in value:
        import capo_ivschat.types.firehose_destination_configuration

        return {
            "firehose": capo_ivschat.types.firehose_destination_configuration.serialize_json(
                value["firehose"]
            )
        }
    else:
        raise SerializationError("DestinationConfiguration: no variant present")


def deserialize_json(data: dict) -> DestinationConfiguration:
    if data.get("s3") is not None:
        import capo_ivschat.types.s3_destination_configuration

        return {
            "s3": capo_ivschat.types.s3_destination_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("cloudWatchLogs") is not None:
        import capo_ivschat.types.cloud_watch_logs_destination_configuration

        return {
            "cloudWatchLogs": capo_ivschat.types.cloud_watch_logs_destination_configuration.deserialize_json(
                data["cloudWatchLogs"]
            )
        }
    elif data.get("firehose") is not None:
        import capo_ivschat.types.firehose_destination_configuration

        return {
            "firehose": capo_ivschat.types.firehose_destination_configuration.deserialize_json(
                data["firehose"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DestinationConfiguration: no recognized variant key"
        )

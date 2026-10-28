"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataDestinationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotfleetwise.types.mqtt_topic_config
    import capo_iotfleetwise.types.s3_config
    import capo_iotfleetwise.types.timestream_config


class DataDestinationConfigS3ConfigMember(TypedDict, closed=True):
    s3Config: "capo_iotfleetwise.types.s3_config.S3Config"


class DataDestinationConfigTimestreamConfigMember(TypedDict, closed=True):
    timestreamConfig: "capo_iotfleetwise.types.timestream_config.TimestreamConfig"


class DataDestinationConfigMqttTopicConfigMember(TypedDict, closed=True):
    mqttTopicConfig: "capo_iotfleetwise.types.mqtt_topic_config.MqttTopicConfig"


DataDestinationConfig: TypeAlias = (
    DataDestinationConfigS3ConfigMember
    | DataDestinationConfigTimestreamConfigMember
    | DataDestinationConfigMqttTopicConfigMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataDestinationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DataDestinationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3Config" in value:
        import capo_iotfleetwise.types.s3_config

        return {
            "s3Config": capo_iotfleetwise.types.s3_config.serialize_aws_json_1_0(
                value["s3Config"]
            )
        }
    elif "timestreamConfig" in value:
        import capo_iotfleetwise.types.timestream_config

        return {
            "timestreamConfig": capo_iotfleetwise.types.timestream_config.serialize_aws_json_1_0(
                value["timestreamConfig"]
            )
        }
    elif "mqttTopicConfig" in value:
        import capo_iotfleetwise.types.mqtt_topic_config

        return {
            "mqttTopicConfig": capo_iotfleetwise.types.mqtt_topic_config.serialize_aws_json_1_0(
                value["mqttTopicConfig"]
            )
        }
    else:
        raise SerializationError("DataDestinationConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> DataDestinationConfig:
    if data.get("s3Config") is not None:
        import capo_iotfleetwise.types.s3_config

        return {
            "s3Config": capo_iotfleetwise.types.s3_config.deserialize_aws_json_1_0(
                data["s3Config"]
            )
        }
    elif data.get("timestreamConfig") is not None:
        import capo_iotfleetwise.types.timestream_config

        return {
            "timestreamConfig": capo_iotfleetwise.types.timestream_config.deserialize_aws_json_1_0(
                data["timestreamConfig"]
            )
        }
    elif data.get("mqttTopicConfig") is not None:
        import capo_iotfleetwise.types.mqtt_topic_config

        return {
            "mqttTopicConfig": capo_iotfleetwise.types.mqtt_topic_config.deserialize_aws_json_1_0(
                data["mqttTopicConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DataDestinationConfig: no recognized variant key")

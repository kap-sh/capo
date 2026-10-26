"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectContainerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_container_log_level


class _ServiceConnectContainerConfiguration_logLevel(TypedDict, closed=True):
    logLevel: "capo_ecs.types.service_connect_container_log_level.ServiceConnectContainerLogLevel"


ServiceConnectContainerConfiguration: TypeAlias = (
    _ServiceConnectContainerConfiguration_logLevel | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectContainerConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ServiceConnectContainerConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "logLevel" in value:
        import capo_ecs.types.service_connect_container_log_level

        return {
            "logLevel": capo_ecs.types.service_connect_container_log_level.serialize_aws_json_1_1(
                value["logLevel"]
            )
        }
    else:
        raise SerializationError(
            "ServiceConnectContainerConfiguration: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectContainerConfiguration:
    if data.get("logLevel") is not None:
        import capo_ecs.types.service_connect_container_log_level

        return {
            "logLevel": capo_ecs.types.service_connect_container_log_level.deserialize_aws_json_1_1(
                data["logLevel"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ServiceConnectContainerConfiguration: no recognized variant key"
        )

"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError, SerializationError
from capo_cloudwatch_logs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.open_search_resource_config


class ResourceConfigOpenSearchResourceConfigMember(TypedDict, closed=True):
    openSearchResourceConfig: "capo_cloudwatch_logs.types.open_search_resource_config.OpenSearchResourceConfig"


ResourceConfig: TypeAlias = (
    ResourceConfigOpenSearchResourceConfigMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "openSearchResourceConfig" in value:
        import capo_cloudwatch_logs.types.open_search_resource_config

        return {
            "openSearchResourceConfig": capo_cloudwatch_logs.types.open_search_resource_config.serialize_aws_json_1_1(
                value["openSearchResourceConfig"]
            )
        }
    else:
        raise SerializationError("ResourceConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ResourceConfig:
    if data.get("openSearchResourceConfig") is not None:
        import capo_cloudwatch_logs.types.open_search_resource_config

        return {
            "openSearchResourceConfig": capo_cloudwatch_logs.types.open_search_resource_config.deserialize_aws_json_1_1(
                data["openSearchResourceConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResourceConfig: no recognized variant key")

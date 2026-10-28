"""Generated from Smithy shape ``com.amazonaws.interconnect#Provider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError, SerializationError
from capo_interconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_interconnect.types.cloud_service_provider
    import capo_interconnect.types.last_mile_provider


class ProviderCloudServiceProviderMember(TypedDict, closed=True):
    cloudServiceProvider: (
        "capo_interconnect.types.cloud_service_provider.CloudServiceProvider"
    )


class ProviderLastMileProviderMember(TypedDict, closed=True):
    lastMileProvider: "capo_interconnect.types.last_mile_provider.LastMileProvider"


Provider: TypeAlias = (
    ProviderCloudServiceProviderMember
    | ProviderLastMileProviderMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Provider) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Provider: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cloudServiceProvider" in value:
        return {"cloudServiceProvider": value["cloudServiceProvider"]}
    elif "lastMileProvider" in value:
        return {"lastMileProvider": value["lastMileProvider"]}
    else:
        raise SerializationError("Provider: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Provider:
    if data.get("cloudServiceProvider") is not None:
        return {"cloudServiceProvider": data["cloudServiceProvider"]}
    elif data.get("lastMileProvider") is not None:
        return {"lastMileProvider": data["lastMileProvider"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Provider: no recognized variant key")

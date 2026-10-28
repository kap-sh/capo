"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_source_endpoint_configuration
    import capo_mediaconnect.types.standard_source_endpoint_configuration


class SourceEndpointConfigurationStandardMember(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_source_endpoint_configuration.StandardSourceEndpointConfiguration"


class SourceEndpointConfigurationRouterOutputMember(TypedDict, closed=True):
    RouterOutput: "capo_mediaconnect.types.router_output_source_endpoint_configuration.RouterOutputSourceEndpointConfiguration"


SourceEndpointConfiguration: TypeAlias = (
    SourceEndpointConfigurationStandardMember
    | SourceEndpointConfigurationRouterOutputMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceEndpointConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_source_endpoint_configuration

        return {
            "standard": capo_mediaconnect.types.standard_source_endpoint_configuration.serialize_json(
                value["Standard"]
            )
        }
    elif "RouterOutput" in value:
        import capo_mediaconnect.types.router_output_source_endpoint_configuration

        return {
            "routerOutput": capo_mediaconnect.types.router_output_source_endpoint_configuration.serialize_json(
                value["RouterOutput"]
            )
        }
    else:
        raise SerializationError("SourceEndpointConfiguration: no variant present")


def deserialize_json(data: dict) -> SourceEndpointConfiguration:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_source_endpoint_configuration

        return {
            "Standard": capo_mediaconnect.types.standard_source_endpoint_configuration.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("routerOutput") is not None:
        import capo_mediaconnect.types.router_output_source_endpoint_configuration

        return {
            "RouterOutput": capo_mediaconnect.types.router_output_source_endpoint_configuration.deserialize_json(
                data["routerOutput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SourceEndpointConfiguration: no recognized variant key"
        )

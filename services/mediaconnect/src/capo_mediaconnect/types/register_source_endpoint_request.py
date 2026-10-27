"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RegisterSourceEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.source_endpoint_configuration


class RegisterSourceEndpointRequest(TypedDict, closed=True):
    region_name: NotRequired["str"]
    """<p>The name of the Amazon Web Services Region in which to register the source endpoint. Defaults to the current region if not specified.</p>"""
    description: NotRequired["str"]
    """<p>A description to help you identify the source endpoint.</p>"""
    configuration: "capo_mediaconnect.types.source_endpoint_configuration.SourceEndpointConfiguration"
    """<p>The configuration settings for the source endpoint.</p>"""
    tags: NotRequired["capo_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p>The tags to apply to the source endpoint. Each tag is a key-value pair.</p>"""
    client_token: NotRequired["capo_mediaconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterSourceEndpointRequest) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["regionName"] = value["region_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_mediaconnect.types.source_endpoint_configuration

    out["configuration"] = (
        capo_mediaconnect.types.source_endpoint_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RegisterSourceEndpointRequest:
    out: RegisterSourceEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.source_endpoint_configuration

        out["configuration"] = (
            capo_mediaconnect.types.source_endpoint_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

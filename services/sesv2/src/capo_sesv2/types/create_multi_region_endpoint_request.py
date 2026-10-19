"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateMultiRegionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.details
    import capo_sesv2.types.endpoint_name
    import capo_sesv2.types.tag_list


class CreateMultiRegionEndpointRequest(TypedDict, closed=True):
    endpoint_name: "capo_sesv2.types.endpoint_name.EndpointName"
    """<p>The name of the multi-region endpoint (global-endpoint).</p>"""
    details: "capo_sesv2.types.details.Details"
    """<p>Contains details of a multi-region endpoint (global-endpoint) being created.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the multi-region endpoint (global-endpoint).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiRegionEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    import capo_sesv2.types.details

    out["Details"] = capo_sesv2.types.details.serialize_json(value["details"])
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMultiRegionEndpointRequest:
    out: CreateMultiRegionEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    else:
        out["endpoint_name"] = ""
    if data.get("Details") is not None:
        import capo_sesv2.types.details

        out["details"] = capo_sesv2.types.details.deserialize_json(data["Details"])
    else:
        raise DeserializationError("CreateMultiRegionEndpointRequest.details required")
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out

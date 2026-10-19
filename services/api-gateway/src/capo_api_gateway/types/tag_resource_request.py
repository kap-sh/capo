"""Generated from Smithy shape ``com.amazonaws.apigateway#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_api_gateway.types.string.String"
    """<p>The ARN of a resource that can be tagged.</p>"""
    tags: "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_api_gateway.types.map_of_string_to_string

    out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out

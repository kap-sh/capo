"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class CreateResourceRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    parent_id: "capo_api_gateway.types.string.String"
    """<p>The parent resource's identifier.</p>"""
    path_part: "capo_api_gateway.types.string.String"
    """<p>The last path segment for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceRequest) -> dict:
    out: dict = {}
    out["pathPart"] = value["path_part"]
    return out


def deserialize_json(data: dict) -> CreateResourceRequest:
    out: CreateResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("pathPart") is not None:
        out["path_part"] = data["pathPart"]
    else:
        out["path_part"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class CreateModelRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The RestApi identifier under which the Model will be created.</p>"""
    name: "capo_api_gateway.types.string.String"
    """<p>The name of the model. Must be alphanumeric.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the model.</p>"""
    schema: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The schema for the model. For <code>application/json</code> models, this should be JSON schema draft 4 model. The maximum size of the model is 400 KB.</p>"""
    content_type: "capo_api_gateway.types.string.String"
    """<p>The content-type for the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "schema" in value:
        out["schema"] = value["schema"]
    out["contentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> CreateModelRequest:
    out: CreateModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        out["content_type"] = ""
    return out

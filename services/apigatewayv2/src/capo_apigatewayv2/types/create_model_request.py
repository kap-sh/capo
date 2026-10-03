"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.string_with_length_between0_and32_k
    import capo_apigatewayv2.types.string_with_length_between0_and1024
    import capo_apigatewayv2.types.string_with_length_between1_and128
    import capo_apigatewayv2.types.string_with_length_between1_and256


class CreateModelRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    content_type: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and256.StringWithLengthBetween1And256"
    ]
    """<p>The content-type for the model, for example, "application/json".</p>"""
    description: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The description of the model.</p>"""
    name: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the model. Must be alphanumeric.</p>"""
    schema: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between0_and32_k.StringWithLengthBetween0And32K"
    ]
    """<p>The schema for the model. For application/json models, this should be JSON schema draft 4 model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelRequest) -> dict:
    out: dict = {}
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    if "schema" in value:
        out["schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> CreateModelRequest:
    out: CreateModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    return out

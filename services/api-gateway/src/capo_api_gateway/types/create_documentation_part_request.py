"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateDocumentationPartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.documentation_part_location
    import capo_api_gateway.types.string


class CreateDocumentationPartRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    location: (
        "capo_api_gateway.types.documentation_part_location.DocumentationPartLocation"
    )
    """<p>The location of the targeted API entity of the to-be-created documentation part.</p>"""
    properties: "capo_api_gateway.types.string.String"
    """<p>The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDocumentationPartRequest) -> dict:
    out: dict = {}
    import capo_api_gateway.types.documentation_part_location

    out["location"] = capo_api_gateway.types.documentation_part_location.serialize_json(
        value["location"]
    )
    out["properties"] = value["properties"]
    return out


def deserialize_json(data: dict) -> CreateDocumentationPartRequest:
    out: CreateDocumentationPartRequest = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        import capo_api_gateway.types.documentation_part_location

        out["location"] = (
            capo_api_gateway.types.documentation_part_location.deserialize_json(
                data["location"]
            )
        )
    else:
        raise DeserializationError("CreateDocumentationPartRequest.location required")
    if data.get("properties") is not None:
        out["properties"] = data["properties"]
    else:
        out["properties"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.apigateway#ImportDocumentationPartsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.blob
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.put_mode
    import capo_api_gateway.types.string


class ImportDocumentationPartsRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    mode: NotRequired["capo_api_gateway.types.put_mode.PutMode"]
    """<p>A query parameter to indicate whether to overwrite (<code>overwrite</code>) any existing DocumentationParts definition or to merge (<code>merge</code>) the new definition into the existing one. The default value is <code>merge</code>.</p>"""
    fail_on_warnings: NotRequired["capo_api_gateway.types.boolean.Boolean"]
    """<p>A query parameter to specify whether to rollback the documentation importation (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.</p>"""
    body: "capo_api_gateway.types.blob.Blob"
    """<p>Raw byte array representing the to-be-imported documentation parts. To import from an OpenAPI file, this is a JSON object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDocumentationPartsRequest) -> dict:
    out: dict = {}
    import capo_api_gateway.types.blob

    out["body"] = capo_api_gateway.types.blob.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> ImportDocumentationPartsRequest:
    out: ImportDocumentationPartsRequest = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_api_gateway.types.blob

        out["body"] = capo_api_gateway.types.blob.deserialize_json(data["body"])
    else:
        raise DeserializationError("ImportDocumentationPartsRequest.body required")
    return out

"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateDocumentationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class CreateDocumentationVersionRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    documentation_version: "capo_api_gateway.types.string.String"
    """<p>The version identifier of the new snapshot.</p>"""
    stage_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The stage name to be associated with the new documentation snapshot.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A description about the new documentation snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDocumentationVersionRequest) -> dict:
    out: dict = {}
    out["documentationVersion"] = value["documentation_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateDocumentationVersionRequest:
    out: CreateDocumentationVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("documentationVersion") is not None:
        out["documentation_version"] = data["documentationVersion"]
    else:
        out["documentation_version"] = ""
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.securityagent#ReportDestination``."""

from typing_extensions import NotRequired, TypedDict


class ReportDestination(TypedDict, closed=True):
    integration_id: "str"
    """<p>The integration identifier for the document provider.</p>"""
    container_id: "str"
    """<p>The container identifier where the report will be published.</p>"""
    parent_id: NotRequired["str"]
    """<p>The parent document identifier under which the report will be created.</p>"""
    document_id: NotRequired["str"]
    """<p>The existing document identifier to update instead of creating a new document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportDestination) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["containerId"] = value["container_id"]
    if "parent_id" in value:
        out["parentId"] = value["parent_id"]
    if "document_id" in value:
        out["documentId"] = value["document_id"]
    return out


def deserialize_json(data: dict) -> ReportDestination:
    out: ReportDestination = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("containerId") is not None:
        out["container_id"] = data["containerId"]
    else:
        out["container_id"] = ""
    if data.get("parentId") is not None:
        out["parent_id"] = data["parentId"]
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    return out

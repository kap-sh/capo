"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetFlowTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.urn
    import capo_iotthingsgraph.types.version


class GetFlowTemplateRequest(TypedDict, closed=True):
    id: "capo_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the workflow.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>"""
    revision_number: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The number of the workflow revision to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFlowTemplateRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "revision_number" in value:
        out["revisionNumber"] = value["revision_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFlowTemplateRequest:
    out: GetFlowTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("revisionNumber") is not None:
        out["revision_number"] = data["revisionNumber"]
    return out

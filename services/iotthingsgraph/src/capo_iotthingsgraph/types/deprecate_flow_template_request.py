"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeprecateFlowTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.urn


class DeprecateFlowTemplateRequest(TypedDict, closed=True):
    id: "capo_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the workflow to be deleted.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeprecateFlowTemplateRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeprecateFlowTemplateRequest:
    out: DeprecateFlowTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out

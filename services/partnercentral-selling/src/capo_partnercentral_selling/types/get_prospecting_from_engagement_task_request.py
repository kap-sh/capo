"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetProspectingFromEngagementTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.prospecting_task_identifier


class GetProspectingFromEngagementTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the task. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes. The value must match the catalog used when the task was created.</p>"""
    task_identifier: "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier"
    """<p>The unique identifier of the prospecting task to retrieve. This value is returned in the <code>TaskId</code> field of the <code>StartProspectingFromEngagementTask</code> response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProspectingFromEngagementTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["TaskIdentifier"] = value["task_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProspectingFromEngagementTaskRequest:
    out: GetProspectingFromEngagementTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("TaskIdentifier") is not None:
        out["task_identifier"] = data["TaskIdentifier"]
    else:
        out["task_identifier"] = ""
    return out

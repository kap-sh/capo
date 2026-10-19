"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartProspectingFromEngagementTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.engagement_identifier_list
    import capo_partnercentral_selling.types.task_name


class StartProspectingFromEngagementTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the task is initiated. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>"""
    identifiers: "capo_partnercentral_selling.types.engagement_identifier_list.EngagementIdentifierList"
    """<p>The list of engagement identifiers to include in this prospecting task. Each identifier must correspond to an existing engagement in the specified catalog. Maximum of 100 identifiers per task.</p>"""
    task_name: "capo_partnercentral_selling.types.task_name.TaskName"
    """<p>A descriptive name for the task. This name helps identify the task in list and get operations. The name must contain 1 to 128 characters.</p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier provided by the client to ensure idempotency. Making the same request with the same <code>ClientToken</code> returns the same response without creating a duplicate task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartProspectingFromEngagementTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    import capo_partnercentral_selling.types.engagement_identifier_list

    out["Identifiers"] = (
        capo_partnercentral_selling.types.engagement_identifier_list.serialize_aws_json_1_0(
            value["identifiers"]
        )
    )
    out["TaskName"] = value["task_name"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartProspectingFromEngagementTaskRequest:
    out: StartProspectingFromEngagementTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifiers") is not None:
        import capo_partnercentral_selling.types.engagement_identifier_list

        out["identifiers"] = (
            capo_partnercentral_selling.types.engagement_identifier_list.deserialize_aws_json_1_0(
                data["Identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    if data.get("TaskName") is not None:
        out["task_name"] = data["TaskName"]
    else:
        out["task_name"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out

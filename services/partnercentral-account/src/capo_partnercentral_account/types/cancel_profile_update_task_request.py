"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CancelProfileUpdateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.partner_identifier
    import capo_partnercentral_account.types.profile_task_id


class CancelProfileUpdateTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>The unique identifier of the partner account.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    task_id: "capo_partnercentral_account.types.profile_task_id.ProfileTaskId"
    """<p>The unique identifier of the profile update task to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelProfileUpdateTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelProfileUpdateTaskRequest:
    out: CancelProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    return out

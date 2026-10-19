"""Generated from Smithy shape ``com.amazonaws.workmail#CancelMailboxExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.mailbox_export_job_id
    import capo_workmail.types.organization_id


class CancelMailboxExportJobRequest(TypedDict, closed=True):
    client_token: "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    """<p>The idempotency token for the client request.</p>"""
    job_id: "capo_workmail.types.mailbox_export_job_id.MailboxExportJobId"
    """<p>The job ID.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMailboxExportJobRequest) -> dict:
    out: dict = {}
    out["ClientToken"] = value["client_token"]
    out["JobId"] = value["job_id"]
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMailboxExportJobRequest:
    out: CancelMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    return out

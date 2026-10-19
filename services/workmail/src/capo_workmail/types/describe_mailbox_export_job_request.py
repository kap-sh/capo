"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeMailboxExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.mailbox_export_job_id
    import capo_workmail.types.organization_id


class DescribeMailboxExportJobRequest(TypedDict, closed=True):
    job_id: "capo_workmail.types.mailbox_export_job_id.MailboxExportJobId"
    """<p>The mailbox export job ID.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMailboxExportJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMailboxExportJobRequest:
    out: DescribeMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    return out

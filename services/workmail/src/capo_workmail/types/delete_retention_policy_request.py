"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteRetentionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.organization_id
    import capo_workmail.types.short_string


class DeleteRetentionPolicyRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""
    id: "capo_workmail.types.short_string.ShortString"
    """<p>The retention policy ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRetentionPolicyRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRetentionPolicyRequest:
    out: DeleteRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out

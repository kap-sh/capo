"""Generated from Smithy shape ``com.amazonaws.workmail#AssumeImpersonationRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role_id
    import capo_workmail.types.organization_id


class AssumeImpersonationRoleRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which the impersonation role will be assumed.</p>"""
    impersonation_role_id: (
        "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
    )
    """<p>The impersonation role ID to assume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssumeImpersonationRoleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ImpersonationRoleId"] = value["impersonation_role_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssumeImpersonationRoleRequest:
    out: AssumeImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("ImpersonationRoleId") is not None:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    else:
        out["impersonation_role_id"] = ""
    return out

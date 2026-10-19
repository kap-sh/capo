"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeregisterOrganizationDelegatedAdminRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id


class DeregisterOrganizationDelegatedAdminRequest(TypedDict, closed=True):
    delegated_admin_account_id: "capo_cloudtrail.types.account_id.AccountId"
    """<p>A delegated administrator account ID. This is a member account in an organization that is currently designated as a delegated administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterOrganizationDelegatedAdminRequest) -> dict:
    out: dict = {}
    out["DelegatedAdminAccountId"] = value["delegated_admin_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterOrganizationDelegatedAdminRequest:
    out: DeregisterOrganizationDelegatedAdminRequest = {}  # type: ignore[typeddict-item]
    if data.get("DelegatedAdminAccountId") is not None:
        out["delegated_admin_account_id"] = data["DelegatedAdminAccountId"]
    else:
        out["delegated_admin_account_id"] = ""
    return out

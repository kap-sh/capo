"""Generated from Smithy shape ``com.amazonaws.fms#PutAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.admin_scope
    import capo_fms.types.aws_account_id


class PutAdminAccountRequest(TypedDict, closed=True):
    admin_account: "capo_fms.types.aws_account_id.AWSAccountId"
    """<p>The Amazon Web Services account ID to add as an Firewall Manager administrator account. The account must be a member of the organization that was onboarded to Firewall Manager by <a>AssociateAdminAccount</a>. For more information about Organizations, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html">Managing the Amazon Web Services Accounts in Your Organization</a>.</p>"""
    admin_scope: NotRequired["capo_fms.types.admin_scope.AdminScope"]
    """<p>Configures the resources that the specified Firewall Manager administrator can manage. As a best practice, set the administrative scope according to the principles of least privilege. Only grant the administrator the specific resources or permissions that they need to perform the duties of their role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAdminAccountRequest) -> dict:
    out: dict = {}
    out["AdminAccount"] = value["admin_account"]
    if "admin_scope" in value:
        import capo_fms.types.admin_scope

        out["AdminScope"] = capo_fms.types.admin_scope.serialize_aws_json_1_1(
            value["admin_scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAdminAccountRequest:
    out: PutAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccount") is not None:
        out["admin_account"] = data["AdminAccount"]
    else:
        raise DeserializationError("PutAdminAccountRequest.admin_account required")
    if data.get("AdminScope") is not None:
        import capo_fms.types.admin_scope

        out["admin_scope"] = capo_fms.types.admin_scope.deserialize_aws_json_1_1(
            data["AdminScope"]
        )
    return out

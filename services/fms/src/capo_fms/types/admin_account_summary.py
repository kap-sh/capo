"""Generated from Smithy shape ``com.amazonaws.fms#AdminAccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.boolean
    import capo_fms.types.organization_status


class AdminAccountSummary(TypedDict, closed=True):
    admin_account: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID of the Firewall Manager administrator's account.</p>"""
    default_admin: "capo_fms.types.boolean.Boolean"
    """<p>A boolean value that indicates if the administrator is the default administrator. If true, then this is the default administrator account. The default administrator can manage third-party firewalls and has full administrative scope. There is only one default administrator account per organization. For information about Firewall Manager default administrator accounts, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-administrators.html">Managing Firewall Manager administrators</a> in the <i>Firewall Manager Developer Guide</i>.</p>"""
    status: NotRequired["capo_fms.types.organization_status.OrganizationStatus"]
    """<p>The current status of the request to onboard a member account as an Firewall Manager administrator.</p> <ul> <li> <p> <code>ONBOARDING</code> - The account is onboarding to Firewall Manager as an administrator.</p> </li> <li> <p> <code>ONBOARDING_COMPLETE</code> - Firewall Manager The account is onboarded to Firewall Manager as an administrator, and can perform actions on the resources defined in their <a>AdminScope</a>.</p> </li> <li> <p> <code>OFFBOARDING</code> - The account is being removed as an Firewall Manager administrator.</p> </li> <li> <p> <code>OFFBOARDING_COMPLETE</code> - The account has been removed as an Firewall Manager administrator.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAccountSummary) -> dict:
    out: dict = {}
    if "admin_account" in value:
        out["AdminAccount"] = value["admin_account"]
    out["DefaultAdmin"] = value.get("default_admin", False)
    if "status" in value:
        import capo_fms.types.organization_status

        out["Status"] = capo_fms.types.organization_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminAccountSummary:
    out: AdminAccountSummary = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccount") is not None:
        out["admin_account"] = data["AdminAccount"]
    if data.get("DefaultAdmin") is not None:
        out["default_admin"] = data["DefaultAdmin"]
    else:
        out["default_admin"] = False
    if data.get("Status") is not None:
        import capo_fms.types.organization_status

        out["status"] = capo_fms.types.organization_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out

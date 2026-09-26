"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminAccountDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id
    import capo_network_security_manager.types.admin_account_status
    import capo_network_security_manager.types.admin_priority
    import capo_network_security_manager.types.admin_scope


class AdminAccountDetails(TypedDict, closed=True):
    admin_account: "capo_network_security_manager.types.account_id.AccountId"
    """<p>The AWS account ID of the administrator account.</p>"""
    priority: "capo_network_security_manager.types.admin_priority.AdminPriority"
    """<p>The priority assigned to the administrator account.</p>"""
    admin_scope: NotRequired[
        "capo_network_security_manager.types.admin_scope.AdminScope"
    ]
    """<p>The administrative scope, which defines the accounts, organizational units, and firewall types that the administrator can manage.</p>"""
    status: NotRequired[
        "capo_network_security_manager.types.admin_account_status.AdminAccountStatus"
    ]
    """<p>The status of the administrator account, either <code>ONBOARDED</code> or <code>OFFBOARDED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccountDetails) -> dict:
    out: dict = {}
    out["adminAccount"] = value["admin_account"]
    out["priority"] = value["priority"]
    if "admin_scope" in value:
        import capo_network_security_manager.types.admin_scope

        out["adminScope"] = (
            capo_network_security_manager.types.admin_scope.serialize_json(
                value["admin_scope"]
            )
        )
    if "status" in value:
        import capo_network_security_manager.types.admin_account_status

        out["status"] = (
            capo_network_security_manager.types.admin_account_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdminAccountDetails:
    out: AdminAccountDetails = {}  # type: ignore[typeddict-item]
    if data.get("adminAccount") is not None:
        out["admin_account"] = data["adminAccount"]
    else:
        raise DeserializationError("AdminAccountDetails.admin_account required")
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("AdminAccountDetails.priority required")
    if data.get("adminScope") is not None:
        import capo_network_security_manager.types.admin_scope

        out["admin_scope"] = (
            capo_network_security_manager.types.admin_scope.deserialize_json(
                data["adminScope"]
            )
        )
    if data.get("status") is not None:
        import capo_network_security_manager.types.admin_account_status

        out["status"] = (
            capo_network_security_manager.types.admin_account_status.deserialize_json(
                data["status"]
            )
        )
    return out

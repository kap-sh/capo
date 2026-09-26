"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PutAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id
    import capo_network_security_manager.types.admin_priority
    import capo_network_security_manager.types.admin_scope_input


class PutAdminAccountRequest(TypedDict, closed=True):
    account_id: "capo_network_security_manager.types.account_id.AccountId"
    """<p>The AWS account ID to set as the AWS Network Security Manager administrator account.</p>"""
    priority: "capo_network_security_manager.types.admin_priority.AdminPriority"
    """<p>The priority to assign to the administrator account.</p>"""
    admin_scope: NotRequired[
        "capo_network_security_manager.types.admin_scope_input.AdminScopeInput"
    ]
    """<p>The scope of accounts, organizational units, and firewall types that the administrator can manage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAdminAccountRequest) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["priority"] = value["priority"]
    if "admin_scope" in value:
        import capo_network_security_manager.types.admin_scope_input

        out["adminScope"] = (
            capo_network_security_manager.types.admin_scope_input.serialize_json(
                value["admin_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAdminAccountRequest:
    out: PutAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("PutAdminAccountRequest.account_id required")
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("PutAdminAccountRequest.priority required")
    if data.get("adminScope") is not None:
        import capo_network_security_manager.types.admin_scope_input

        out["admin_scope"] = (
            capo_network_security_manager.types.admin_scope_input.deserialize_json(
                data["adminScope"]
            )
        )
    return out

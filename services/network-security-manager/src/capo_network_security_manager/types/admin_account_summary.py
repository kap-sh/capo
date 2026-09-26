"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminAccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id
    import capo_network_security_manager.types.admin_priority
    import capo_network_security_manager.types.sensitive_email
    import capo_network_security_manager.types.sensitive_name


class AdminAccountSummary(TypedDict, closed=True):
    account_id: "capo_network_security_manager.types.account_id.AccountId"
    """<p>The AWS account ID.</p>"""
    priority: NotRequired[
        "capo_network_security_manager.types.admin_priority.AdminPriority"
    ]
    """<p>The priority assigned to the administrator account.</p>"""
    name: NotRequired[
        "capo_network_security_manager.types.sensitive_name.SensitiveName"
    ]
    """<p>The name of the administrator account.</p>"""
    email: NotRequired[
        "capo_network_security_manager.types.sensitive_email.SensitiveEmail"
    ]
    """<p>The email address associated with the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccountSummary) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> AdminAccountSummary:
    out: AdminAccountSummary = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("AdminAccountSummary.account_id required")
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    return out

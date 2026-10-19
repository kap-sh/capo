"""Generated from Smithy shape ``com.amazonaws.auditmanager#RegisterOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.account_id


class RegisterOrganizationAdminAccountRequest(TypedDict, closed=True):
    admin_account_id: "capo_auditmanager.types.account_id.AccountId"
    """<p> The identifier for the delegated administrator account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    out["adminAccountId"] = value["admin_account_id"]
    return out


def deserialize_json(data: dict) -> RegisterOrganizationAdminAccountRequest:
    out: RegisterOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("adminAccountId") is not None:
        out["admin_account_id"] = data["adminAccountId"]
    else:
        out["admin_account_id"] = ""
    return out

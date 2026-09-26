"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PutAdminAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.admin_account_details


class PutAdminAccountResponse(TypedDict, closed=True):
    admin_account_details: NotRequired[
        "capo_network_security_manager.types.admin_account_details.AdminAccountDetails"
    ]
    """<p>The details of the administrator account that was set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAdminAccountResponse) -> dict:
    out: dict = {}
    if "admin_account_details" in value:
        import capo_network_security_manager.types.admin_account_details

        out["adminAccountDetails"] = (
            capo_network_security_manager.types.admin_account_details.serialize_json(
                value["admin_account_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAdminAccountResponse:
    out: PutAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("adminAccountDetails") is not None:
        import capo_network_security_manager.types.admin_account_details

        out["admin_account_details"] = (
            capo_network_security_manager.types.admin_account_details.deserialize_json(
                data["adminAccountDetails"]
            )
        )
    return out

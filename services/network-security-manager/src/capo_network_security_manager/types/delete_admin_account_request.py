"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeleteAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id


class DeleteAdminAccountRequest(TypedDict, closed=True):
    account_id: "capo_network_security_manager.types.account_id.AccountId"
    """<p>The AWS account ID of the administrator account to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAdminAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAdminAccountRequest:
    out: DeleteAdminAccountRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GetAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id


class GetAdminAccountRequest(TypedDict, closed=True):
    account_id: "capo_network_security_manager.types.account_id.AccountId"
    """<p>The AWS account ID of the administrator account to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdminAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAdminAccountRequest:
    out: GetAdminAccountRequest = {}  # type: ignore[typeddict-item]
    return out

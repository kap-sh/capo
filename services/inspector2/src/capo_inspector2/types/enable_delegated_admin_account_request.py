"""Generated from Smithy shape ``com.amazonaws.inspector2#EnableDelegatedAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.client_token


class EnableDelegatedAdminAccountRequest(TypedDict, closed=True):
    delegated_admin_account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator.</p>"""
    client_token: NotRequired["capo_inspector2.types.client_token.ClientToken"]
    """<p>The idempotency token for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableDelegatedAdminAccountRequest) -> dict:
    out: dict = {}
    out["delegatedAdminAccountId"] = value["delegated_admin_account_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> EnableDelegatedAdminAccountRequest:
    out: EnableDelegatedAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("delegatedAdminAccountId") is not None:
        out["delegated_admin_account_id"] = data["delegatedAdminAccountId"]
    else:
        out["delegated_admin_account_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

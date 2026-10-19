"""Generated from Smithy shape ``com.amazonaws.inspector2#DisableDelegatedAdminAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id


class DisableDelegatedAdminAccountResponse(TypedDict, closed=True):
    delegated_admin_account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the successfully disabled delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableDelegatedAdminAccountResponse) -> dict:
    out: dict = {}
    out["delegatedAdminAccountId"] = value["delegated_admin_account_id"]
    return out


def deserialize_json(data: dict) -> DisableDelegatedAdminAccountResponse:
    out: DisableDelegatedAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("delegatedAdminAccountId") is not None:
        out["delegated_admin_account_id"] = data["delegatedAdminAccountId"]
    else:
        out["delegated_admin_account_id"] = ""
    return out

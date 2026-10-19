"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryMemberOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id


class ProtectedQueryMemberOutputConfiguration(TypedDict, closed=True):
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The unique identifier for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryMemberOutputConfiguration) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedQueryMemberOutputConfiguration:
    out: ProtectedQueryMemberOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    return out

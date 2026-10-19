"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobSingleMemberOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id


class ProtectedJobSingleMemberOutput(TypedDict, closed=True):
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member in the collaboration who can receive results from analyses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobSingleMemberOutput) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedJobSingleMemberOutput:
    out: ProtectedJobSingleMemberOutput = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    return out

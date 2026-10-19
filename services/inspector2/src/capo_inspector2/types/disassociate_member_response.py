"""Generated from Smithy shape ``com.amazonaws.inspector2#DisassociateMemberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id


class DisassociateMemberResponse(TypedDict, closed=True):
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the successfully disassociated member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberResponse) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DisassociateMemberResponse:
    out: DisassociateMemberResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    return out

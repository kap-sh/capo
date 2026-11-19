"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.string


class AccountSummary(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the Amazon Web Services account.</p>"""
    finding_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of findings in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSummary) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "finding_count" in value:
        out["findingCount"] = value["finding_count"]
    return out


def deserialize_json(data: dict) -> AccountSummary:
    out: AccountSummary = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("findingCount") is not None:
        out["finding_count"] = data["findingCount"]
    return out

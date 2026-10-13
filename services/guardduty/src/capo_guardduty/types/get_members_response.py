"""Generated from Smithy shape ``com.amazonaws.guardduty#GetMembersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.members
    import capo_guardduty.types.unprocessed_accounts


class GetMembersResponse(TypedDict, closed=True):
    members: NotRequired["capo_guardduty.types.members.Members"]
    """<p>A list of members.</p>"""
    unprocessed_accounts: NotRequired[
        "capo_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import capo_guardduty.types.members

        out["members"] = capo_guardduty.types.members.serialize_json(value["members"])
    if "unprocessed_accounts" in value:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            capo_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMembersResponse:
    out: GetMembersResponse = {}  # type: ignore[typeddict-item]
    if data.get("members") is not None:
        import capo_guardduty.types.members

        out["members"] = capo_guardduty.types.members.deserialize_json(data["members"])
    if data.get("unprocessedAccounts") is not None:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            capo_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out


def redact_sensitive(value: GetMembersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "members" in value:
        import capo_guardduty.types.members

        out["members"] = capo_guardduty.types.members.redact_sensitive(value["members"])
    return out

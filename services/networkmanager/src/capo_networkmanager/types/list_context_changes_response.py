"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListContextChangesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.context_change_list
    import capo_networkmanager.types.next_token


class ListContextChangesResponse(TypedDict, closed=True):
    context_changes: NotRequired[
        "capo_networkmanager.types.context_change_list.ContextChangeList"
    ]
    """<p>The context entries that were added or removed.</p>"""
    from_version_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The version that the changes start from.</p>"""
    to_version_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The version that the changes bring the context entries up to. To get later changes, specify this value as <code>FromVersionId</code> in your next request. All pages of the same request return the same version.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContextChangesResponse) -> dict:
    out: dict = {}
    if "context_changes" in value:
        import capo_networkmanager.types.context_change_list

        out["ContextChanges"] = (
            capo_networkmanager.types.context_change_list.serialize_json(
                value["context_changes"]
            )
        )
    if "from_version_id" in value:
        out["FromVersionId"] = value["from_version_id"]
    if "to_version_id" in value:
        out["ToVersionId"] = value["to_version_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContextChangesResponse:
    out: ListContextChangesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContextChanges") is not None:
        import capo_networkmanager.types.context_change_list

        out["context_changes"] = (
            capo_networkmanager.types.context_change_list.deserialize_json(
                data["ContextChanges"]
            )
        )
    if data.get("FromVersionId") is not None:
        out["from_version_id"] = data["FromVersionId"]
    if data.get("ToVersionId") is not None:
        out["to_version_id"] = data["ToVersionId"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

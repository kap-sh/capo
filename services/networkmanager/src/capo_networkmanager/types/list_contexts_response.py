"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListContextsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.context_list
    import capo_networkmanager.types.next_token


class ListContextsResponse(TypedDict, closed=True):
    contexts: NotRequired["capo_networkmanager.types.context_list.ContextList"]
    """<p>The context entries.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    version_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The version of the returned context entries. All pages of the same request return the same version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContextsResponse) -> dict:
    out: dict = {}
    if "contexts" in value:
        import capo_networkmanager.types.context_list

        out["Contexts"] = capo_networkmanager.types.context_list.serialize_json(
            value["contexts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> ListContextsResponse:
    out: ListContextsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Contexts") is not None:
        import capo_networkmanager.types.context_list

        out["contexts"] = capo_networkmanager.types.context_list.deserialize_json(
            data["Contexts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    return out

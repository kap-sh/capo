"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentContextsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.context_summaries
    import capo_wellarchitected.types.next_token


class ListAgentContextsResponse(TypedDict, closed=True):
    items: "capo_wellarchitected.types.context_summaries.ContextSummaries"
    """<p>A list of context summaries associated with the profile.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentContextsResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.context_summaries

    out["items"] = capo_wellarchitected.types.context_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentContextsResponse:
    out: ListAgentContextsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_wellarchitected.types.context_summaries

        out["items"] = capo_wellarchitected.types.context_summaries.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListAgentContextsResponse.items required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAgentContextsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_wellarchitected.types.context_summaries

        out["items"] = capo_wellarchitected.types.context_summaries.redact_sensitive(
            value["items"]
        )
    return out

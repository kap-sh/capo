"""Generated from Smithy shape ``com.amazonaws.pipes#ListPipesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.next_token
    import capo_pipes.types.pipe_list


class ListPipesResponse(TypedDict, closed=True):
    pipes: NotRequired["capo_pipes.types.pipe_list.PipeList"]
    """<p>The pipes returned by the call.</p>"""
    next_token: NotRequired["capo_pipes.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipesResponse) -> dict:
    out: dict = {}
    if "pipes" in value:
        import capo_pipes.types.pipe_list

        out["Pipes"] = capo_pipes.types.pipe_list.serialize_json(value["pipes"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPipesResponse:
    out: ListPipesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Pipes") is not None:
        import capo_pipes.types.pipe_list

        out["pipes"] = capo_pipes.types.pipe_list.deserialize_json(data["Pipes"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListPipesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out

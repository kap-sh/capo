"""Generated from Smithy shape ``com.amazonaws.wickr#ListBotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.bots
    import capo_wickr.types.generic_string


class ListBotsResponse(TypedDict, closed=True):
    bots: "capo_wickr.types.bots.Bots"
    """<p>A list of bot objects matching the specified filters and within the current page.</p>"""
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsResponse) -> dict:
    out: dict = {}
    import capo_wickr.types.bots

    out["bots"] = capo_wickr.types.bots.serialize_json(value["bots"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotsResponse:
    out: ListBotsResponse = {}  # type: ignore[typeddict-item]
    if data.get("bots") is not None:
        import capo_wickr.types.bots

        out["bots"] = capo_wickr.types.bots.deserialize_json(data["bots"])
    else:
        out["bots"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

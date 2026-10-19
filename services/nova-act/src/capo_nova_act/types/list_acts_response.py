"""Generated from Smithy shape ``com.amazonaws.novaact#ListActsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.act_summaries
    import capo_nova_act.types.next_token


class ListActsResponse(TypedDict, closed=True):
    act_summaries: "capo_nova_act.types.act_summaries.ActSummaries"
    """<p>A list of summary information for acts in the session.</p>"""
    next_token: NotRequired["capo_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActsResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.act_summaries

    out["actSummaries"] = capo_nova_act.types.act_summaries.serialize_json(
        value["act_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActsResponse:
    out: ListActsResponse = {}  # type: ignore[typeddict-item]
    if data.get("actSummaries") is not None:
        import capo_nova_act.types.act_summaries

        out["act_summaries"] = capo_nova_act.types.act_summaries.deserialize_json(
            data["actSummaries"]
        )
    else:
        out["act_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

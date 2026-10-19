"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListCompositionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition_summary_list
    import capo_ivs_realtime.types.pagination_token


class ListCompositionsResponse(TypedDict, closed=True):
    compositions: (
        "capo_ivs_realtime.types.composition_summary_list.CompositionSummaryList"
    )
    """<p>List of the matching Compositions (summary information only).</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>If there are more compositions than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCompositionsResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.composition_summary_list

    out["compositions"] = (
        capo_ivs_realtime.types.composition_summary_list.serialize_json(
            value["compositions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCompositionsResponse:
    out: ListCompositionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("compositions") is not None:
        import capo_ivs_realtime.types.composition_summary_list

        out["compositions"] = (
            capo_ivs_realtime.types.composition_summary_list.deserialize_json(
                data["compositions"]
            )
        )
    else:
        out["compositions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListSystemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.system_summary_list


class ListSystemsResponse(TypedDict, closed=True):
    system_summaries: "capo_resiliencehubv2.types.system_summary_list.SystemSummaryList"
    """<p>The list of system summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListSystemsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.system_summary_list

    out["systemSummaries"] = (
        capo_resiliencehubv2.types.system_summary_list.serialize_json(
            value["system_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSystemsResponse:
    out: ListSystemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("systemSummaries") is not None:
        import capo_resiliencehubv2.types.system_summary_list

        out["system_summaries"] = (
            capo_resiliencehubv2.types.system_summary_list.deserialize_json(
                data["systemSummaries"]
            )
        )
    else:
        out["system_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

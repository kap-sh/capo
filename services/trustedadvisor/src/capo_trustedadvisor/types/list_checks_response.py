"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.check_summary_list


class ListChecksResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    check_summaries: "capo_trustedadvisor.types.check_summary_list.CheckSummaryList"
    """<p>The list of Checks</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChecksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_trustedadvisor.types.check_summary_list

    out["checkSummaries"] = capo_trustedadvisor.types.check_summary_list.serialize_json(
        value["check_summaries"]
    )
    return out


def deserialize_json(data: dict) -> ListChecksResponse:
    out: ListChecksResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("checkSummaries") is not None:
        import capo_trustedadvisor.types.check_summary_list

        out["check_summaries"] = (
            capo_trustedadvisor.types.check_summary_list.deserialize_json(
                data["checkSummaries"]
            )
        )
    else:
        out["check_summaries"] = []
    return out

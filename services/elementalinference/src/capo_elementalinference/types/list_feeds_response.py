"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListFeedsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_summary_list


class ListFeedsResponse(TypedDict, closed=True):
    feeds: "capo_elementalinference.types.feed_summary_list.FeedSummaryList"
    """<p>A list of FeedSummary objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the batch of results that you want to see. For example, you submit a list request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the list request a second time and specify the NextToken value. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFeedsResponse) -> dict:
    out: dict = {}
    import capo_elementalinference.types.feed_summary_list

    out["feeds"] = capo_elementalinference.types.feed_summary_list.serialize_json(
        value["feeds"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFeedsResponse:
    out: ListFeedsResponse = {}  # type: ignore[typeddict-item]
    if data.get("feeds") is not None:
        import capo_elementalinference.types.feed_summary_list

        out["feeds"] = capo_elementalinference.types.feed_summary_list.deserialize_json(
            data["feeds"]
        )
    else:
        out["feeds"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

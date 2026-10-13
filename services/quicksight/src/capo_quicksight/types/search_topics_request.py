"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchTopicsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_search_filter_list


class SearchTopicsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic that you want to find.</p>"""
    filters: "capo_quicksight.types.topic_search_filter_list.TopicSearchFilterList"
    """<p>The filters that you want to use to search for the topic.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTopicsRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.topic_search_filter_list

    out["Filters"] = capo_quicksight.types.topic_search_filter_list.serialize_json(
        value["filters"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchTopicsRequest:
    out: SearchTopicsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_quicksight.types.topic_search_filter_list

        out["filters"] = (
            capo_quicksight.types.topic_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchTopicsRequest.filters required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


def redact_sensitive(value: SearchTopicsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_quicksight.types.topic_search_filter_list

        out["filters"] = (
            capo_quicksight.types.topic_search_filter_list.redact_sensitive(
                value["filters"]
            )
        )
    return out

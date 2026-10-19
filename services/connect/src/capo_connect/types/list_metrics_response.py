"""Generated from Smithy shape ``com.amazonaws.connect#ListMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.metric_summary_list
    import capo_connect.types.next_token


class ListMetricsResponse(TypedDict, closed=True):
    metric_summary_list: "capo_connect.types.metric_summary_list.MetricSummaryList"
    """<p>The list of metric summaries.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetricsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.metric_summary_list

    out["MetricSummaryList"] = capo_connect.types.metric_summary_list.serialize_json(
        value["metric_summary_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMetricsResponse:
    out: ListMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("MetricSummaryList") is not None:
        import capo_connect.types.metric_summary_list

        out["metric_summary_list"] = (
            capo_connect.types.metric_summary_list.deserialize_json(
                data["MetricSummaryList"]
            )
        )
    else:
        out["metric_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

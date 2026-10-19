"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFlowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.flow_summary_list
    import capo_quicksight.types.status_code


class SearchFlowsOutput(TypedDict, closed=True):
    flow_summary_list: "capo_quicksight.types.flow_summary_list.FlowSummaryList"
    """<p>The list of flows found against the search.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFlowsOutput) -> dict:
    out: dict = {}
    import capo_quicksight.types.flow_summary_list

    out["FlowSummaryList"] = capo_quicksight.types.flow_summary_list.serialize_json(
        value["flow_summary_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchFlowsOutput:
    out: SearchFlowsOutput = {}  # type: ignore[typeddict-item]
    if data.get("FlowSummaryList") is not None:
        import capo_quicksight.types.flow_summary_list

        out["flow_summary_list"] = (
            capo_quicksight.types.flow_summary_list.deserialize_json(
                data["FlowSummaryList"]
            )
        )
    else:
        out["flow_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out

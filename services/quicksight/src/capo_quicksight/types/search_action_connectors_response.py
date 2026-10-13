"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchActionConnectorsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.action_connector_summary_list
    import capo_quicksight.types.status_code


class SearchActionConnectorsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results. If null, there are no more results to retrieve.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status code of the request.</p>"""
    action_connector_summaries: NotRequired[
        "capo_quicksight.types.action_connector_summary_list.ActionConnectorSummaryList"
    ]
    """<p>A list of action connector summaries that match the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchActionConnectorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "action_connector_summaries" in value:
        import capo_quicksight.types.action_connector_summary_list

        out["ActionConnectorSummaries"] = (
            capo_quicksight.types.action_connector_summary_list.serialize_json(
                value["action_connector_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchActionConnectorsResponse:
    out: SearchActionConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("ActionConnectorSummaries") is not None:
        import capo_quicksight.types.action_connector_summary_list

        out["action_connector_summaries"] = (
            capo_quicksight.types.action_connector_summary_list.deserialize_json(
                data["ActionConnectorSummaries"]
            )
        )
    return out


def redact_sensitive(value: SearchActionConnectorsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action_connector_summaries" in value:
        import capo_quicksight.types.action_connector_summary_list

        out["action_connector_summaries"] = (
            capo_quicksight.types.action_connector_summary_list.redact_sensitive(
                value["action_connector_summaries"]
            )
        )
    return out

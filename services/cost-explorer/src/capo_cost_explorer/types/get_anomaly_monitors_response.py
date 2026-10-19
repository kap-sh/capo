"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetAnomalyMonitorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.anomaly_monitors
    import capo_cost_explorer.types.next_page_token


class GetAnomalyMonitorsResponse(TypedDict, closed=True):
    anomaly_monitors: "capo_cost_explorer.types.anomaly_monitors.AnomalyMonitors"
    """<p>A list of cost anomaly monitors that includes the detailed metadata for each monitor. </p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAnomalyMonitorsResponse) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.anomaly_monitors

    out["AnomalyMonitors"] = (
        capo_cost_explorer.types.anomaly_monitors.serialize_aws_json_1_1(
            value["anomaly_monitors"]
        )
    )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAnomalyMonitorsResponse:
    out: GetAnomalyMonitorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyMonitors") is not None:
        import capo_cost_explorer.types.anomaly_monitors

        out["anomaly_monitors"] = (
            capo_cost_explorer.types.anomaly_monitors.deserialize_aws_json_1_1(
                data["AnomalyMonitors"]
            )
        )
    else:
        out["anomaly_monitors"] = []
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out

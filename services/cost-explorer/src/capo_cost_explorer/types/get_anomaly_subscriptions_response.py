"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetAnomalySubscriptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.anomaly_subscriptions
    import capo_cost_explorer.types.next_page_token


class GetAnomalySubscriptionsResponse(TypedDict, closed=True):
    anomaly_subscriptions: (
        "capo_cost_explorer.types.anomaly_subscriptions.AnomalySubscriptions"
    )
    """<p>A list of cost anomaly subscriptions that includes the detailed metadata for each one. </p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAnomalySubscriptionsResponse) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.anomaly_subscriptions

    out["AnomalySubscriptions"] = (
        capo_cost_explorer.types.anomaly_subscriptions.serialize_aws_json_1_1(
            value["anomaly_subscriptions"]
        )
    )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAnomalySubscriptionsResponse:
    out: GetAnomalySubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnomalySubscriptions") is not None:
        import capo_cost_explorer.types.anomaly_subscriptions

        out["anomaly_subscriptions"] = (
            capo_cost_explorer.types.anomaly_subscriptions.deserialize_aws_json_1_1(
                data["AnomalySubscriptions"]
            )
        )
    else:
        out["anomaly_subscriptions"] = []
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out

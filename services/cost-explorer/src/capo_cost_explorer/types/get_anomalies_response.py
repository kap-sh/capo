"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetAnomaliesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.anomalies
    import capo_cost_explorer.types.next_page_token


class GetAnomaliesResponse(TypedDict, closed=True):
    anomalies: "capo_cost_explorer.types.anomalies.Anomalies"
    """<p>A list of cost anomalies. </p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAnomaliesResponse) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.anomalies

    out["Anomalies"] = capo_cost_explorer.types.anomalies.serialize_aws_json_1_1(
        value["anomalies"]
    )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAnomaliesResponse:
    out: GetAnomaliesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Anomalies") is not None:
        import capo_cost_explorer.types.anomalies

        out["anomalies"] = capo_cost_explorer.types.anomalies.deserialize_aws_json_1_1(
            data["Anomalies"]
        )
    else:
        out["anomalies"] = []
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out

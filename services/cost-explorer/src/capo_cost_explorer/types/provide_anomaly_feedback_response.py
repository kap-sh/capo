"""Generated from Smithy shape ``com.amazonaws.costexplorer#ProvideAnomalyFeedbackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class ProvideAnomalyFeedbackResponse(TypedDict, closed=True):
    anomaly_id: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The ID of the modified cost anomaly. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvideAnomalyFeedbackResponse) -> dict:
    out: dict = {}
    out["AnomalyId"] = value["anomaly_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvideAnomalyFeedbackResponse:
    out: ProvideAnomalyFeedbackResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyId") is not None:
        out["anomaly_id"] = data["AnomalyId"]
    else:
        out["anomaly_id"] = ""
    return out

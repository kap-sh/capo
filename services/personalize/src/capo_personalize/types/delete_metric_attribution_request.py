"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteMetricAttributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DeleteMetricAttributionRequest(TypedDict, closed=True):
    metric_attribution_arn: "capo_personalize.types.arn.Arn"
    """<p>The metric attribution's Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMetricAttributionRequest) -> dict:
    out: dict = {}
    out["metricAttributionArn"] = value["metric_attribution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMetricAttributionRequest:
    out: DeleteMetricAttributionRequest = {}  # type: ignore[typeddict-item]
    if data.get("metricAttributionArn") is not None:
        out["metric_attribution_arn"] = data["metricAttributionArn"]
    else:
        out["metric_attribution_arn"] = ""
    return out

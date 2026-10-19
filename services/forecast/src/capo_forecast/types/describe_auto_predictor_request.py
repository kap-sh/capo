"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeAutoPredictorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DescribeAutoPredictorRequest(TypedDict, closed=True):
    predictor_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutoPredictorRequest) -> dict:
    out: dict = {}
    out["PredictorArn"] = value["predictor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutoPredictorRequest:
    out: DescribeAutoPredictorRequest = {}  # type: ignore[typeddict-item]
    if data.get("PredictorArn") is not None:
        out["predictor_arn"] = data["PredictorArn"]
    else:
        out["predictor_arn"] = ""
    return out

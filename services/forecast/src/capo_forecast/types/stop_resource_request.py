"""Generated from Smithy shape ``com.amazonaws.forecast#StopResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class StopResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource to stop. The supported ARNs are <code>DatasetImportJobArn</code>, <code>PredictorArn</code>, <code>PredictorBacktestExportJobArn</code>, <code>ForecastArn</code>, <code>ForecastExportJobArn</code>, <code>ExplainabilityArn</code>, and <code>ExplainabilityExportArn</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopResourceRequest:
    out: StopResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out

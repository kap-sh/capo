"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteExplainabilityExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DeleteExplainabilityExportRequest(TypedDict, closed=True):
    explainability_export_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Explainability export to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExplainabilityExportRequest) -> dict:
    out: dict = {}
    out["ExplainabilityExportArn"] = value["explainability_export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExplainabilityExportRequest:
    out: DeleteExplainabilityExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExplainabilityExportArn") is not None:
        out["explainability_export_arn"] = data["ExplainabilityExportArn"]
    else:
        out["explainability_export_arn"] = ""
    return out

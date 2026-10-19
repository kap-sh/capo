"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#TransformDataResponse``."""

from typing_extensions import NotRequired, TypedDict


class TransformDataResponse(TypedDict, closed=True):
    transformed_data: "str"
    """<p>The transformed FHIR R4 JSON output.</p>"""
    drift_report: NotRequired["str"]
    """<p>The drift report comparing transformation output against ground truth. HealthLake populates this field only when you enable drift detection and ground truth is available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformDataResponse) -> dict:
    out: dict = {}
    out["TransformedData"] = value["transformed_data"]
    if "drift_report" in value:
        out["DriftReport"] = value["drift_report"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformDataResponse:
    out: TransformDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("TransformedData") is not None:
        out["transformed_data"] = data["TransformedData"]
    else:
        out["transformed_data"] = ""
    if data.get("DriftReport") is not None:
        out["drift_report"] = data["DriftReport"]
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SaveWeightsResult``."""

from typing_extensions import NotRequired, TypedDict


class SaveWeightsResult(TypedDict, closed=True):
    model_package_arn: NotRequired["str"]
    """<p>The ARN of the model package created for the saved weights.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaveWeightsResult) -> dict:
    out: dict = {}
    if "model_package_arn" in value:
        out["modelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_json(data: dict) -> SaveWeightsResult:
    out: SaveWeightsResult = {}  # type: ignore[typeddict-item]
    if data.get("modelPackageArn") is not None:
        out["model_package_arn"] = data["modelPackageArn"]
    return out

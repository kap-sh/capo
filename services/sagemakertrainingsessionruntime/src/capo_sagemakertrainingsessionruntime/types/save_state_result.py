"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SaveStateResult``."""

from typing_extensions import TypedDict


class SaveStateResult(TypedDict, closed=True):
    model_package_arn: "str"
    """<p>The ARN of the model package created for the saved state checkpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaveStateResult) -> dict:
    out: dict = {}
    out["modelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_json(data: dict) -> SaveStateResult:
    out: SaveStateResult = {}  # type: ignore[typeddict-item]
    if data.get("modelPackageArn") is not None:
        out["model_package_arn"] = data["modelPackageArn"]
    else:
        out["model_package_arn"] = ""
    return out

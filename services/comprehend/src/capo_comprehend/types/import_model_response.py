"""Generated from Smithy shape ``com.amazonaws.comprehend#ImportModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_model_arn


class ImportModelResponse(TypedDict, closed=True):
    model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the custom model being imported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportModelResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportModelResponse:
    out: ImportModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportModelResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    return out


def deserialize_cbor(data: dict) -> ImportModelResponse:
    out: ImportModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    return out

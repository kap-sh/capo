"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_dataset_arn


class CreateDatasetResponse(TypedDict, closed=True):
    dataset_arn: NotRequired[
        "capo_comprehend.types.comprehend_dataset_arn.ComprehendDatasetArn"
    ]
    """<p>The ARN of the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetResponse:
    out: CreateDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_cbor(data: dict) -> CreateDatasetResponse:
    out: CreateDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    return out

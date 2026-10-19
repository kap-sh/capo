"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_arn


class DescribeDatasetRequest(TypedDict, closed=True):
    dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset that you want to describe. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        out["dataset_arn"] = ""
    return out

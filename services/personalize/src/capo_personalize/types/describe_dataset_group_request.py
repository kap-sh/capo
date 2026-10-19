"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeDatasetGroupRequest(TypedDict, closed=True):
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetGroupRequest) -> dict:
    out: dict = {}
    out["datasetGroupArn"] = value["dataset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetGroupRequest:
    out: DescribeDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        out["dataset_group_arn"] = ""
    return out

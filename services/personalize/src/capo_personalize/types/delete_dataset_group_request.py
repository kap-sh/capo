"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteDatasetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DeleteDatasetGroupRequest(TypedDict, closed=True):
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the dataset group to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDatasetGroupRequest) -> dict:
    out: dict = {}
    out["datasetGroupArn"] = value["dataset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDatasetGroupRequest:
    out: DeleteDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        out["dataset_group_arn"] = ""
    return out

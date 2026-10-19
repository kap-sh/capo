"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class UpdateDatasetRequest(TypedDict, closed=True):
    dataset_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset that you want to update.</p>"""
    schema_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the new schema you want use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDatasetRequest) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["schemaArn"] = value["schema_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDatasetRequest:
    out: UpdateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("schemaArn") is not None:
        out["schema_arn"] = data["schemaArn"]
    else:
        out["schema_arn"] = ""
    return out

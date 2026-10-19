"""Generated from Smithy shape ``com.amazonaws.rekognition#UpdateDatasetEntriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_arn
    import capo_rekognition.types.dataset_changes


class UpdateDatasetEntriesRequest(TypedDict, closed=True):
    dataset_arn: "capo_rekognition.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset that you want to update. </p>"""
    changes: "capo_rekognition.types.dataset_changes.DatasetChanges"
    """<p> The changes that you want to make to the dataset. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDatasetEntriesRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    import capo_rekognition.types.dataset_changes

    out["Changes"] = capo_rekognition.types.dataset_changes.serialize_aws_json_1_1(
        value["changes"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDatasetEntriesRequest:
    out: UpdateDatasetEntriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("Changes") is not None:
        import capo_rekognition.types.dataset_changes

        out["changes"] = (
            capo_rekognition.types.dataset_changes.deserialize_aws_json_1_1(
                data["Changes"]
            )
        )
    else:
        raise DeserializationError("UpdateDatasetEntriesRequest.changes required")
    return out

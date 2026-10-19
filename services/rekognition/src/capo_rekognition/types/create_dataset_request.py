"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_source
    import capo_rekognition.types.dataset_type
    import capo_rekognition.types.project_arn
    import capo_rekognition.types.tag_map


class CreateDatasetRequest(TypedDict, closed=True):
    dataset_source: NotRequired["capo_rekognition.types.dataset_source.DatasetSource"]
    """<p> The source files for the dataset. You can specify the ARN of an existing dataset or specify the Amazon S3 bucket location of an Amazon Sagemaker format manifest file. If you don't specify <code>datasetSource</code>, an empty dataset is created. To add labeled images to the dataset, You can use the console or call <a>UpdateDatasetEntries</a>. </p>"""
    dataset_type: "capo_rekognition.types.dataset_type.DatasetType"
    """<p> The type of the dataset. Specify <code>TRAIN</code> to create a training dataset. Specify <code>TEST</code> to create a test dataset. </p>"""
    project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p> The ARN of the Amazon Rekognition Custom Labels project to which you want to asssign the dataset. </p>"""
    tags: NotRequired["capo_rekognition.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that you want to attach to the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    if "dataset_source" in value:
        import capo_rekognition.types.dataset_source

        out["DatasetSource"] = (
            capo_rekognition.types.dataset_source.serialize_aws_json_1_1(
                value["dataset_source"]
            )
        )
    import capo_rekognition.types.dataset_type

    out["DatasetType"] = capo_rekognition.types.dataset_type.serialize_aws_json_1_1(
        value["dataset_type"]
    )
    out["ProjectArn"] = value["project_arn"]
    if "tags" in value:
        import capo_rekognition.types.tag_map

        out["Tags"] = capo_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetSource") is not None:
        import capo_rekognition.types.dataset_source

        out["dataset_source"] = (
            capo_rekognition.types.dataset_source.deserialize_aws_json_1_1(
                data["DatasetSource"]
            )
        )
    if data.get("DatasetType") is not None:
        import capo_rekognition.types.dataset_type

        out["dataset_type"] = (
            capo_rekognition.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    else:
        import typing

        out["dataset_type"] = typing.cast(
            "capo_rekognition.types.dataset_type.DatasetType", ""
        )
    if data.get("ProjectArn") is not None:
        out["project_arn"] = data["ProjectArn"]
    else:
        out["project_arn"] = ""
    if data.get("Tags") is not None:
        import capo_rekognition.types.tag_map

        out["tags"] = capo_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDataDeletionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.data_source
    import capo_personalize.types.name
    import capo_personalize.types.role_arn
    import capo_personalize.types.tags


class CreateDataDeletionJobRequest(TypedDict, closed=True):
    job_name: "capo_personalize.types.name.Name"
    """<p>The name for the data deletion job.</p>"""
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group that has the datasets you want to delete records from.</p>"""
    data_source: "capo_personalize.types.data_source.DataSource"
    """<p>The Amazon S3 bucket that contains the list of userIds of the users to delete.</p>"""
    role_arn: "capo_personalize.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3 data source.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the data deletion job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataDeletionJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    import capo_personalize.types.data_source

    out["dataSource"] = capo_personalize.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataDeletionJobRequest:
    out: CreateDataDeletionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateDataDeletionJobRequest.job_name required")
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError(
            "CreateDataDeletionJobRequest.dataset_group_arn required"
        )
    if data.get("dataSource") is not None:
        import capo_personalize.types.data_source

        out["data_source"] = (
            capo_personalize.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    else:
        raise DeserializationError("CreateDataDeletionJobRequest.data_source required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateDataDeletionJobRequest.role_arn required")
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out

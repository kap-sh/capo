"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.boolean
    import capo_personalize.types.data_source
    import capo_personalize.types.import_mode
    import capo_personalize.types.name
    import capo_personalize.types.role_arn
    import capo_personalize.types.tags


class CreateDatasetImportJobRequest(TypedDict, closed=True):
    job_name: "capo_personalize.types.name.Name"
    """<p>The name for the dataset import job.</p>"""
    dataset_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the dataset that receives the imported data.</p>"""
    data_source: "capo_personalize.types.data_source.DataSource"
    """<p>The Amazon S3 bucket that contains the training data to import.</p>"""
    role_arn: NotRequired["capo_personalize.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that has permissions to read from the Amazon S3 data source.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset import job.</p>"""
    import_mode: NotRequired["capo_personalize.types.import_mode.ImportMode"]
    """<p>Specify how to add the new records to an existing dataset. The default import mode is <code>FULL</code>. If you haven't imported bulk records into the dataset previously, you can only specify <code>FULL</code>.</p> <ul> <li> <p>Specify <code>FULL</code> to overwrite all existing bulk data in your dataset. Data you imported individually is not replaced.</p> </li> <li> <p>Specify <code>INCREMENTAL</code> to append the new records to the existing data in your dataset. Amazon Personalize replaces any record with the same ID with the new one.</p> </li> </ul>"""
    publish_attribution_metrics_to_s3: NotRequired[
        "capo_personalize.types.boolean.Boolean"
    ]
    """<p>If you created a metric attribution, specify whether to publish metrics for this import job to Amazon S3</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetImportJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["datasetArn"] = value["dataset_arn"]
    import capo_personalize.types.data_source

    out["dataSource"] = capo_personalize.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    if "import_mode" in value:
        import capo_personalize.types.import_mode

        out["importMode"] = capo_personalize.types.import_mode.serialize_aws_json_1_1(
            value["import_mode"]
        )
    if "publish_attribution_metrics_to_s3" in value:
        out["publishAttributionMetricsToS3"] = value[
            "publish_attribution_metrics_to_s3"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetImportJobRequest:
    out: CreateDatasetImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateDatasetImportJobRequest.job_name required")
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("CreateDatasetImportJobRequest.dataset_arn required")
    if data.get("dataSource") is not None:
        import capo_personalize.types.data_source

        out["data_source"] = (
            capo_personalize.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetImportJobRequest.data_source required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("importMode") is not None:
        import capo_personalize.types.import_mode

        out["import_mode"] = (
            capo_personalize.types.import_mode.deserialize_aws_json_1_1(
                data["importMode"]
            )
        )
    if data.get("publishAttributionMetricsToS3") is not None:
        out["publish_attribution_metrics_to_s3"] = data["publishAttributionMetricsToS3"]
    return out

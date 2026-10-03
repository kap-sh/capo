"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.dataset_type
    import capo_forecast.types.domain
    import capo_forecast.types.encryption_config
    import capo_forecast.types.frequency
    import capo_forecast.types.name
    import capo_forecast.types.schema
    import capo_forecast.types.status
    import capo_forecast.types.timestamp


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the dataset.</p>"""
    domain: NotRequired["capo_forecast.types.domain.Domain"]
    """<p>The domain associated with the dataset.</p>"""
    dataset_type: NotRequired["capo_forecast.types.dataset_type.DatasetType"]
    """<p>The dataset type.</p>"""
    data_frequency: NotRequired["capo_forecast.types.frequency.Frequency"]
    """<p>The frequency of data collection.</p> <p>Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, "M" indicates every month and "30min" indicates every 30 minutes.</p>"""
    schema: NotRequired["capo_forecast.types.schema.Schema"]
    """<p>An array of <code>SchemaAttribute</code> objects that specify the dataset fields. Each <code>SchemaAttribute</code> specifies the name and data type of a field.</p>"""
    encryption_config: NotRequired[
        "capo_forecast.types.encryption_config.EncryptionConfig"
    ]
    """<p>The Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the dataset. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> <li> <p> <code>UPDATE_PENDING</code>, <code>UPDATE_IN_PROGRESS</code>, <code>UPDATE_FAILED</code> </p> </li> </ul> <p>The <code>UPDATE</code> states apply while data is imported to the dataset from a call to the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a> operation and reflect the status of the dataset import job. For example, when the import job status is <code>CREATE_IN_PROGRESS</code>, the status of the dataset is <code>UPDATE_IN_PROGRESS</code>.</p> <note> <p>The <code>Status</code> of the dataset must be <code>ACTIVE</code> before you can import training data.</p> </note>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When you create a dataset, <code>LastModificationTime</code> is the same as <code>CreationTime</code>. While data is being imported to the dataset, <code>LastModificationTime</code> is the current time of the <code>DescribeDataset</code> call. After a <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a> operation has finished, <code>LastModificationTime</code> is when the import job completed or failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "domain" in value:
        import capo_forecast.types.domain

        out["Domain"] = capo_forecast.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    if "dataset_type" in value:
        import capo_forecast.types.dataset_type

        out["DatasetType"] = capo_forecast.types.dataset_type.serialize_aws_json_1_1(
            value["dataset_type"]
        )
    if "data_frequency" in value:
        out["DataFrequency"] = value["data_frequency"]
    if "schema" in value:
        import capo_forecast.types.schema

        out["Schema"] = capo_forecast.types.schema.serialize_aws_json_1_1(
            value["schema"]
        )
    if "encryption_config" in value:
        import capo_forecast.types.encryption_config

        out["EncryptionConfig"] = (
            capo_forecast.types.encryption_config.serialize_aws_json_1_1(
                value["encryption_config"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "creation_time" in value:
        import capo_forecast.types.timestamp

        out["CreationTime"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_forecast.types.timestamp

        out["LastModificationTime"] = (
            capo_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("Domain") is not None:
        import capo_forecast.types.domain

        out["domain"] = capo_forecast.types.domain.deserialize_aws_json_1_1(
            data["Domain"]
        )
    if data.get("DatasetType") is not None:
        import capo_forecast.types.dataset_type

        out["dataset_type"] = capo_forecast.types.dataset_type.deserialize_aws_json_1_1(
            data["DatasetType"]
        )
    if data.get("DataFrequency") is not None:
        out["data_frequency"] = data["DataFrequency"]
    if data.get("Schema") is not None:
        import capo_forecast.types.schema

        out["schema"] = capo_forecast.types.schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    if data.get("EncryptionConfig") is not None:
        import capo_forecast.types.encryption_config

        out["encryption_config"] = (
            capo_forecast.types.encryption_config.deserialize_aws_json_1_1(
                data["EncryptionConfig"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("CreationTime") is not None:
        import capo_forecast.types.timestamp

        out["creation_time"] = capo_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModificationTime") is not None:
        import capo_forecast.types.timestamp

        out["last_modification_time"] = (
            capo_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    return out

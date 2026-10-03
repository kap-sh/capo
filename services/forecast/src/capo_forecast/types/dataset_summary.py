"""Generated from Smithy shape ``com.amazonaws.forecast#DatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.dataset_type
    import capo_forecast.types.domain
    import capo_forecast.types.name
    import capo_forecast.types.timestamp


class DatasetSummary(TypedDict, closed=True):
    dataset_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the dataset.</p>"""
    dataset_type: NotRequired["capo_forecast.types.dataset_type.DatasetType"]
    """<p>The dataset type.</p>"""
    domain: NotRequired["capo_forecast.types.domain.Domain"]
    """<p>The domain associated with the dataset.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When you create a dataset, <code>LastModificationTime</code> is the same as <code>CreationTime</code>. While data is being imported to the dataset, <code>LastModificationTime</code> is the current time of the <code>ListDatasets</code> call. After a <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a> operation has finished, <code>LastModificationTime</code> is when the import job completed or failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetSummary) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_type" in value:
        import capo_forecast.types.dataset_type

        out["DatasetType"] = capo_forecast.types.dataset_type.serialize_aws_json_1_1(
            value["dataset_type"]
        )
    if "domain" in value:
        import capo_forecast.types.domain

        out["Domain"] = capo_forecast.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
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


def deserialize_aws_json_1_1(data: dict) -> DatasetSummary:
    out: DatasetSummary = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("DatasetType") is not None:
        import capo_forecast.types.dataset_type

        out["dataset_type"] = capo_forecast.types.dataset_type.deserialize_aws_json_1_1(
            data["DatasetType"]
        )
    if data.get("Domain") is not None:
        import capo_forecast.types.domain

        out["domain"] = capo_forecast.types.domain.deserialize_aws_json_1_1(
            data["Domain"]
        )
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

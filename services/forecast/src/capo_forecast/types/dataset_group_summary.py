"""Generated from Smithy shape ``com.amazonaws.forecast#DatasetGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.name
    import capo_forecast.types.timestamp


class DatasetGroupSummary(TypedDict, closed=True):
    dataset_group_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""
    dataset_group_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the dataset group.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset group was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset group was created or last updated from a call to the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html">UpdateDatasetGroup</a> operation. While the dataset group is being updated, <code>LastModificationTime</code> is the current time of the <code>ListDatasetGroups</code> call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetGroupSummary) -> dict:
    out: dict = {}
    if "dataset_group_arn" in value:
        out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "dataset_group_name" in value:
        out["DatasetGroupName"] = value["dataset_group_name"]
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


def deserialize_aws_json_1_1(data: dict) -> DatasetGroupSummary:
    out: DatasetGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("DatasetGroupArn") is not None:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    if data.get("DatasetGroupName") is not None:
        out["dataset_group_name"] = data["DatasetGroupName"]
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

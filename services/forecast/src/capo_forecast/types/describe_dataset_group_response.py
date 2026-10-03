"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeDatasetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.arn_list
    import capo_forecast.types.domain
    import capo_forecast.types.name
    import capo_forecast.types.status
    import capo_forecast.types.timestamp


class DescribeDatasetGroupResponse(TypedDict, closed=True):
    dataset_group_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the dataset group.</p>"""
    dataset_group_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The ARN of the dataset group.</p>"""
    dataset_arns: NotRequired["capo_forecast.types.arn_list.ArnList"]
    """<p>An array of Amazon Resource Names (ARNs) of the datasets contained in the dataset group.</p>"""
    domain: NotRequired["capo_forecast.types.domain.Domain"]
    """<p>The domain associated with the dataset group.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the dataset group. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> <li> <p> <code>UPDATE_PENDING</code>, <code>UPDATE_IN_PROGRESS</code>, <code>UPDATE_FAILED</code> </p> </li> </ul> <p>The <code>UPDATE</code> states apply when you call the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html">UpdateDatasetGroup</a> operation.</p> <note> <p>The <code>Status</code> of the dataset group must be <code>ACTIVE</code> before you can use the dataset group to create a predictor.</p> </note>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset group was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the dataset group was created or last updated from a call to the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html">UpdateDatasetGroup</a> operation. While the dataset group is being updated, <code>LastModificationTime</code> is the current time of the <code>DescribeDatasetGroup</code> call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetGroupResponse) -> dict:
    out: dict = {}
    if "dataset_group_name" in value:
        out["DatasetGroupName"] = value["dataset_group_name"]
    if "dataset_group_arn" in value:
        out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "dataset_arns" in value:
        import capo_forecast.types.arn_list

        out["DatasetArns"] = capo_forecast.types.arn_list.serialize_aws_json_1_1(
            value["dataset_arns"]
        )
    if "domain" in value:
        import capo_forecast.types.domain

        out["Domain"] = capo_forecast.types.domain.serialize_aws_json_1_1(
            value["domain"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetGroupResponse:
    out: DescribeDatasetGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetGroupName") is not None:
        out["dataset_group_name"] = data["DatasetGroupName"]
    if data.get("DatasetGroupArn") is not None:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    if data.get("DatasetArns") is not None:
        import capo_forecast.types.arn_list

        out["dataset_arns"] = capo_forecast.types.arn_list.deserialize_aws_json_1_1(
            data["DatasetArns"]
        )
    if data.get("Domain") is not None:
        import capo_forecast.types.domain

        out["domain"] = capo_forecast.types.domain.deserialize_aws_json_1_1(
            data["Domain"]
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

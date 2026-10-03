"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMlflowTrackingServersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.mlflow_version
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.sort_tracking_server_by
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.tracking_server_status


class ListMlflowTrackingServersRequest(TypedDict, closed=True):
    created_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Use the <code>CreatedAfter</code> filter to only list tracking servers created after a specific date and time. Listed tracking servers are shown with a date and time such as <code>"2024-03-16T01:46:56+00:00"</code>. The <code>CreatedAfter</code> parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href="https://www.epochconverter.com/">EpochConverter</a>.</p>"""
    created_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Use the <code>CreatedBefore</code> filter to only list tracking servers created before a specific date and time. Listed tracking servers are shown with a date and time such as <code>"2024-03-16T01:46:56+00:00"</code>. The <code>CreatedBefore</code> parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href="https://www.epochconverter.com/">EpochConverter</a>.</p>"""
    tracking_server_status: NotRequired[
        "capo_sagemaker.types.tracking_server_status.TrackingServerStatus"
    ]
    """<p>Filter for tracking servers with a specified creation status.</p>"""
    mlflow_version: NotRequired["capo_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>Filter for tracking servers using the specified MLflow version.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.sort_tracking_server_by.SortTrackingServerBy"
    ]
    """<p>Filter for trackings servers sorting by name, creation time, or creation status.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>Change the order of the listed tracking servers. By default, tracking servers are listed in <code>Descending</code> order by creation time. To change the list order, you can specify <code>SortOrder</code> to be <code>Ascending</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of tracking servers to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMlflowTrackingServersRequest) -> dict:
    out: dict = {}
    if "created_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "tracking_server_status" in value:
        import capo_sagemaker.types.tracking_server_status

        out["TrackingServerStatus"] = (
            capo_sagemaker.types.tracking_server_status.serialize_aws_json_1_1(
                value["tracking_server_status"]
            )
        )
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    if "sort_by" in value:
        import capo_sagemaker.types.sort_tracking_server_by

        out["SortBy"] = (
            capo_sagemaker.types.sort_tracking_server_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMlflowTrackingServersRequest:
    out: ListMlflowTrackingServersRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreatedAfter") is not None:
        import capo_sagemaker.types.timestamp

        out["created_after"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if data.get("CreatedBefore") is not None:
        import capo_sagemaker.types.timestamp

        out["created_before"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if data.get("TrackingServerStatus") is not None:
        import capo_sagemaker.types.tracking_server_status

        out["tracking_server_status"] = (
            capo_sagemaker.types.tracking_server_status.deserialize_aws_json_1_1(
                data["TrackingServerStatus"]
            )
        )
    if data.get("MlflowVersion") is not None:
        out["mlflow_version"] = data["MlflowVersion"]
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.sort_tracking_server_by

        out["sort_by"] = (
            capo_sagemaker.types.sort_tracking_server_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out

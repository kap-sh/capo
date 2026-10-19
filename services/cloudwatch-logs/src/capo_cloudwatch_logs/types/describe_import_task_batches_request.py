"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeImportTaskBatchesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.import_id
    import capo_cloudwatch_logs.types.import_status_list
    import capo_cloudwatch_logs.types.next_token


class DescribeImportTaskBatchesRequest(TypedDict, closed=True):
    import_id: "capo_cloudwatch_logs.types.import_id.ImportId"
    """<p>The ID of the import task to get batch information for.</p>"""
    batch_import_status: NotRequired[
        "capo_cloudwatch_logs.types.import_status_list.ImportStatusList"
    ]
    """<p>Optional filter to list import batches by their status. Accepts multiple status values: IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>"""
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of import batches to return in the response. Default: 10</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The pagination token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTaskBatchesRequest) -> dict:
    out: dict = {}
    out["importId"] = value["import_id"]
    if "batch_import_status" in value:
        import capo_cloudwatch_logs.types.import_status_list

        out["batchImportStatus"] = (
            capo_cloudwatch_logs.types.import_status_list.serialize_aws_json_1_1(
                value["batch_import_status"]
            )
        )
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImportTaskBatchesRequest:
    out: DescribeImportTaskBatchesRequest = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    else:
        out["import_id"] = ""
    if data.get("batchImportStatus") is not None:
        import capo_cloudwatch_logs.types.import_status_list

        out["batch_import_status"] = (
            capo_cloudwatch_logs.types.import_status_list.deserialize_aws_json_1_1(
                data["batchImportStatus"]
            )
        )
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

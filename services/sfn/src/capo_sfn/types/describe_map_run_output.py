"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeMapRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.long_arn
    import capo_sfn.types.map_run_execution_counts
    import capo_sfn.types.map_run_item_counts
    import capo_sfn.types.map_run_status
    import capo_sfn.types.max_concurrency
    import capo_sfn.types.redrive_count
    import capo_sfn.types.timestamp
    import capo_sfn.types.tolerated_failure_count
    import capo_sfn.types.tolerated_failure_percentage


class DescribeMapRunOutput(TypedDict, closed=True):
    map_run_arn: "capo_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) that identifies a Map Run.</p>"""
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the execution in which the Map Run was started.</p>"""
    status: "capo_sfn.types.map_run_status.MapRunStatus"
    """<p>The current status of the Map Run.</p>"""
    start_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date when the Map Run was started.</p>"""
    stop_date: NotRequired["capo_sfn.types.timestamp.Timestamp"]
    """<p>The date when the Map Run was stopped.</p>"""
    max_concurrency: "capo_sfn.types.max_concurrency.MaxConcurrency"
    """<p>The maximum number of child workflow executions configured to run in parallel for the Map Run at the same time.</p>"""
    tolerated_failure_percentage: (
        "capo_sfn.types.tolerated_failure_percentage.ToleratedFailurePercentage"
    )
    """<p>The maximum percentage of failed child workflow executions before the Map Run fails.</p>"""
    tolerated_failure_count: (
        "capo_sfn.types.tolerated_failure_count.ToleratedFailureCount"
    )
    """<p>The maximum number of failed child workflow executions before the Map Run fails.</p>"""
    item_counts: "capo_sfn.types.map_run_item_counts.MapRunItemCounts"
    """<p>A JSON object that contains information about the total number of items, and the item count for each processing status, such as <code>pending</code> and <code>failed</code>.</p>"""
    execution_counts: "capo_sfn.types.map_run_execution_counts.MapRunExecutionCounts"
    """<p>A JSON object that contains information about the total number of child workflow executions for the Map Run, and the count of child workflow executions for each status, such as <code>failed</code> and <code>succeeded</code>.</p>"""
    redrive_count: NotRequired["capo_sfn.types.redrive_count.RedriveCount"]
    """<p>The number of times you've redriven a Map Run. If you have not yet redriven a Map Run, the <code>redriveCount</code> is 0. This count is only updated if you successfully redrive a Map Run.</p>"""
    redrive_date: NotRequired["capo_sfn.types.timestamp.Timestamp"]
    """<p>The date a Map Run was last redriven. If you have not yet redriven a Map Run, the <code>redriveDate</code> is null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeMapRunOutput) -> dict:
    out: dict = {}
    out["mapRunArn"] = value["map_run_arn"]
    out["executionArn"] = value["execution_arn"]
    import capo_sfn.types.map_run_status

    out["status"] = capo_sfn.types.map_run_status.serialize_aws_json_1_0(
        value["status"]
    )
    import capo_sfn.types.timestamp

    out["startDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "stop_date" in value:
        import capo_sfn.types.timestamp

        out["stopDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
            value["stop_date"]
        )
    out["maxConcurrency"] = value.get("max_concurrency", 0)
    out["toleratedFailurePercentage"] = (
        "NaN"
        if value.get("tolerated_failure_percentage", 0)
        != value.get("tolerated_failure_percentage", 0)
        else "Infinity"
        if value.get("tolerated_failure_percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("tolerated_failure_percentage", 0) == float("-inf")
        else value.get("tolerated_failure_percentage", 0)
    )
    out["toleratedFailureCount"] = value.get("tolerated_failure_count", 0)
    import capo_sfn.types.map_run_item_counts

    out["itemCounts"] = capo_sfn.types.map_run_item_counts.serialize_aws_json_1_0(
        value["item_counts"]
    )
    import capo_sfn.types.map_run_execution_counts

    out["executionCounts"] = (
        capo_sfn.types.map_run_execution_counts.serialize_aws_json_1_0(
            value["execution_counts"]
        )
    )
    if "redrive_count" in value:
        out["redriveCount"] = value["redrive_count"]
    if "redrive_date" in value:
        import capo_sfn.types.timestamp

        out["redriveDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
            value["redrive_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeMapRunOutput:
    out: DescribeMapRunOutput = {}  # type: ignore[typeddict-item]
    if data.get("mapRunArn") is not None:
        out["map_run_arn"] = data["mapRunArn"]
    else:
        out["map_run_arn"] = ""
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        out["execution_arn"] = ""
    if data.get("status") is not None:
        import capo_sfn.types.map_run_status

        out["status"] = capo_sfn.types.map_run_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_sfn.types.map_run_status.MapRunStatus", "")
    if data.get("startDate") is not None:
        import capo_sfn.types.timestamp

        out["start_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("stopDate") is not None:
        import capo_sfn.types.timestamp

        out["stop_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    if data.get("maxConcurrency") is not None:
        out["max_concurrency"] = data["maxConcurrency"]
    else:
        out["max_concurrency"] = 0
    if data.get("toleratedFailurePercentage") is not None:
        out["tolerated_failure_percentage"] = float(data["toleratedFailurePercentage"])
    else:
        out["tolerated_failure_percentage"] = 0
    if data.get("toleratedFailureCount") is not None:
        out["tolerated_failure_count"] = data["toleratedFailureCount"]
    else:
        out["tolerated_failure_count"] = 0
    if data.get("itemCounts") is not None:
        import capo_sfn.types.map_run_item_counts

        out["item_counts"] = (
            capo_sfn.types.map_run_item_counts.deserialize_aws_json_1_0(
                data["itemCounts"]
            )
        )
    else:
        raise DeserializationError("DescribeMapRunOutput.item_counts required")
    if data.get("executionCounts") is not None:
        import capo_sfn.types.map_run_execution_counts

        out["execution_counts"] = (
            capo_sfn.types.map_run_execution_counts.deserialize_aws_json_1_0(
                data["executionCounts"]
            )
        )
    else:
        raise DeserializationError("DescribeMapRunOutput.execution_counts required")
    if data.get("redriveCount") is not None:
        out["redrive_count"] = data["redriveCount"]
    if data.get("redriveDate") is not None:
        import capo_sfn.types.timestamp

        out["redrive_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["redriveDate"]
        )
    return out

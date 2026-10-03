"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecutionStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.dpu_count
    import capo_athena.types.long
    import capo_athena.types.result_reuse_information
    import capo_athena.types.string


class QueryExecutionStatistics(TypedDict, closed=True):
    engine_execution_time_in_millis: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of milliseconds that the query took to execute.</p>"""
    data_scanned_in_bytes: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of bytes in the data that was queried.</p>"""
    data_manifest_location: NotRequired["capo_athena.types.string.String"]
    """<p>The location and file name of a data manifest file. The manifest file is saved to the Athena query results location in Amazon S3. The manifest file tracks files that the query wrote to Amazon S3. If the query fails, the manifest file also tracks files that the query intended to write. The manifest is useful for identifying orphaned files resulting from a failed query. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/querying.html">Working with Query Results, Output Files, and Query History</a> in the <i>Amazon Athena User Guide</i>.</p>"""
    total_execution_time_in_millis: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of milliseconds that Athena took to run the query.</p>"""
    query_queue_time_in_millis: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of milliseconds that the query was in your query queue waiting for resources. Note that if transient errors occur, Athena might automatically add the query back to the queue.</p>"""
    service_pre_processing_time_in_millis: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of milliseconds that Athena took to preprocess the query before submitting the query to the query engine.</p>"""
    query_planning_time_in_millis: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source. Note that because the query engine performs the query planning, query planning time is a subset of engine processing time.</p>"""
    service_processing_time_in_millis: NotRequired["capo_athena.types.long.Long"]
    """<p>The number of milliseconds that Athena took to finalize and publish the query results after the query engine finished running the query.</p>"""
    result_reuse_information: NotRequired[
        "capo_athena.types.result_reuse_information.ResultReuseInformation"
    ]
    """<p>Contains information about whether previous query results were reused for the query.</p>"""
    dpu_count: NotRequired["capo_athena.types.dpu_count.DpuCount"]
    """<p>The number of Data Processing Units (DPUs) that Athena used to run the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryExecutionStatistics) -> dict:
    out: dict = {}
    if "engine_execution_time_in_millis" in value:
        out["EngineExecutionTimeInMillis"] = value["engine_execution_time_in_millis"]
    if "data_scanned_in_bytes" in value:
        out["DataScannedInBytes"] = value["data_scanned_in_bytes"]
    if "data_manifest_location" in value:
        out["DataManifestLocation"] = value["data_manifest_location"]
    if "total_execution_time_in_millis" in value:
        out["TotalExecutionTimeInMillis"] = value["total_execution_time_in_millis"]
    if "query_queue_time_in_millis" in value:
        out["QueryQueueTimeInMillis"] = value["query_queue_time_in_millis"]
    if "service_pre_processing_time_in_millis" in value:
        out["ServicePreProcessingTimeInMillis"] = value[
            "service_pre_processing_time_in_millis"
        ]
    if "query_planning_time_in_millis" in value:
        out["QueryPlanningTimeInMillis"] = value["query_planning_time_in_millis"]
    if "service_processing_time_in_millis" in value:
        out["ServiceProcessingTimeInMillis"] = value[
            "service_processing_time_in_millis"
        ]
    if "result_reuse_information" in value:
        import capo_athena.types.result_reuse_information

        out["ResultReuseInformation"] = (
            capo_athena.types.result_reuse_information.serialize_aws_json_1_1(
                value["result_reuse_information"]
            )
        )
    if "dpu_count" in value:
        out["DpuCount"] = (
            "NaN"
            if value["dpu_count"] != value["dpu_count"]
            else "Infinity"
            if value["dpu_count"] == float("inf")
            else "-Infinity"
            if value["dpu_count"] == float("-inf")
            else value["dpu_count"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryExecutionStatistics:
    out: QueryExecutionStatistics = {}  # type: ignore[typeddict-item]
    if data.get("EngineExecutionTimeInMillis") is not None:
        out["engine_execution_time_in_millis"] = data["EngineExecutionTimeInMillis"]
    if data.get("DataScannedInBytes") is not None:
        out["data_scanned_in_bytes"] = data["DataScannedInBytes"]
    if data.get("DataManifestLocation") is not None:
        out["data_manifest_location"] = data["DataManifestLocation"]
    if data.get("TotalExecutionTimeInMillis") is not None:
        out["total_execution_time_in_millis"] = data["TotalExecutionTimeInMillis"]
    if data.get("QueryQueueTimeInMillis") is not None:
        out["query_queue_time_in_millis"] = data["QueryQueueTimeInMillis"]
    if data.get("ServicePreProcessingTimeInMillis") is not None:
        out["service_pre_processing_time_in_millis"] = data[
            "ServicePreProcessingTimeInMillis"
        ]
    if data.get("QueryPlanningTimeInMillis") is not None:
        out["query_planning_time_in_millis"] = data["QueryPlanningTimeInMillis"]
    if data.get("ServiceProcessingTimeInMillis") is not None:
        out["service_processing_time_in_millis"] = data["ServiceProcessingTimeInMillis"]
    if data.get("ResultReuseInformation") is not None:
        import capo_athena.types.result_reuse_information

        out["result_reuse_information"] = (
            capo_athena.types.result_reuse_information.deserialize_aws_json_1_1(
                data["ResultReuseInformation"]
            )
        )
    if data.get("DpuCount") is not None:
        out["dpu_count"] = float(data["DpuCount"])
    return out

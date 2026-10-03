"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetImportTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptune_graph.types.format
    import capo_neptune_graph.types.graph_id
    import capo_neptune_graph.types.import_options
    import capo_neptune_graph.types.import_task_details
    import capo_neptune_graph.types.import_task_status
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.role_arn
    import capo_neptune_graph.types.task_id


class GetImportTaskOutput(TypedDict, closed=True):
    graph_id: NotRequired["capo_neptune_graph.types.graph_id.GraphId"]
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    task_id: "capo_neptune_graph.types.task_id.TaskId"
    """<p>The unique identifier of the import task.</p>"""
    source: "str"
    """<p>A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot</p>"""
    format: NotRequired["capo_neptune_graph.types.format.Format"]
    """<p>Specifies the format of S3 data to be imported. Valid values are <code>CSV</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a> or <code>OPENCYPHER</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>.</p>"""
    parquet_type: NotRequired["capo_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the import task.</p>"""
    role_arn: "capo_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>"""
    status: "capo_neptune_graph.types.import_task_status.ImportTaskStatus"
    """<p>The status of the import task:</p> <ul> <li> <p> <b>INITIALIZING</b> – The necessary resources needed to create the graph are being prepared.</p> </li> <li> <p> <b>ANALYZING_DATA</b> – The data is being analyzed to determine the optimal infrastructure configuration for the new graph.</p> </li> <li> <p> <b>RE_PROVISIONING</b> – The data did not fit into the provisioned graph, so it is being re-provisioned with more capacity.</p> </li> <li> <p> <b>IMPORTING</b> – The data is being loaded.</p> </li> <li> <p> <b>ERROR_ENCOUNTERED</b> – An error has been encountered while trying to create the graph and import the data.</p> </li> <li> <p> <b>ERROR_ENCOUNTERED_ROLLING_BACK</b> – Because of the error that was encountered, the graph is being rolled back and all its resources released.</p> </li> <li> <p> <b>SUCCEEDED</b> – Graph creation and data loading succeeded.</p> </li> <li> <p> <b>FAILED</b> – Graph creation or data loading failed. When the status is <code>FAILED</code>, you can use <code>get-graphs</code> to get more information about the state of the graph.</p> </li> <li> <p> <b>CANCELLING</b> – Because you cancelled the import task, cancellation is in progress.</p> </li> <li> <p> <b>CANCELLED</b> – You have successfully cancelled the import task.</p> </li> </ul>"""
    import_options: NotRequired["capo_neptune_graph.types.import_options.ImportOptions"]
    """<p>Contains options for controlling the import process. For example, if the <code>failOnError</code> key is set to <code>false</code>, the import skips problem data and attempts to continue (whereas if set to <code>true</code>, the default, or if omitted, the import operation halts immediately when an error is encountered.</p>"""
    import_task_details: NotRequired[
        "capo_neptune_graph.types.import_task_details.ImportTaskDetails"
    ]
    """<p>Contains details about the specified import task.</p>"""
    attempt_number: NotRequired["int"]
    """<p>The number of the current attempts to execute the import task.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason that the import task has this status value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportTaskOutput) -> dict:
    out: dict = {}
    if "graph_id" in value:
        out["graphId"] = value["graph_id"]
    out["taskId"] = value["task_id"]
    out["source"] = value["source"]
    if "format" in value:
        import capo_neptune_graph.types.format

        out["format"] = capo_neptune_graph.types.format.serialize_json(value["format"])
    if "parquet_type" in value:
        import capo_neptune_graph.types.parquet_type

        out["parquetType"] = capo_neptune_graph.types.parquet_type.serialize_json(
            value["parquet_type"]
        )
    out["roleArn"] = value["role_arn"]
    import capo_neptune_graph.types.import_task_status

    out["status"] = capo_neptune_graph.types.import_task_status.serialize_json(
        value["status"]
    )
    if "import_options" in value:
        import capo_neptune_graph.types.import_options

        out["importOptions"] = capo_neptune_graph.types.import_options.serialize_json(
            value["import_options"]
        )
    if "import_task_details" in value:
        import capo_neptune_graph.types.import_task_details

        out["importTaskDetails"] = (
            capo_neptune_graph.types.import_task_details.serialize_json(
                value["import_task_details"]
            )
        )
    if "attempt_number" in value:
        out["attemptNumber"] = value["attempt_number"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> GetImportTaskOutput:
    out: GetImportTaskOutput = {}  # type: ignore[typeddict-item]
    if data.get("graphId") is not None:
        out["graph_id"] = data["graphId"]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("GetImportTaskOutput.task_id required")
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("GetImportTaskOutput.source required")
    if data.get("format") is not None:
        import capo_neptune_graph.types.format

        out["format"] = capo_neptune_graph.types.format.deserialize_json(data["format"])
    if data.get("parquetType") is not None:
        import capo_neptune_graph.types.parquet_type

        out["parquet_type"] = capo_neptune_graph.types.parquet_type.deserialize_json(
            data["parquetType"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetImportTaskOutput.role_arn required")
    if data.get("status") is not None:
        import capo_neptune_graph.types.import_task_status

        out["status"] = capo_neptune_graph.types.import_task_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetImportTaskOutput.status required")
    if data.get("importOptions") is not None:
        import capo_neptune_graph.types.import_options

        out["import_options"] = (
            capo_neptune_graph.types.import_options.deserialize_json(
                data["importOptions"]
            )
        )
    if data.get("importTaskDetails") is not None:
        import capo_neptune_graph.types.import_task_details

        out["import_task_details"] = (
            capo_neptune_graph.types.import_task_details.deserialize_json(
                data["importTaskDetails"]
            )
        )
    if data.get("attemptNumber") is not None:
        out["attempt_number"] = data["attemptNumber"]
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out

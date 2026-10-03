"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptune_graph.types.format
    import capo_neptune_graph.types.graph_id
    import capo_neptune_graph.types.import_task_status
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.role_arn
    import capo_neptune_graph.types.task_id


class ImportTaskSummary(TypedDict, closed=True):
    graph_id: NotRequired["capo_neptune_graph.types.graph_id.GraphId"]
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    task_id: "capo_neptune_graph.types.task_id.TaskId"
    """<p>The unique identifier of the import task.</p>"""
    source: "str"
    """<p>A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot</p>"""
    format: NotRequired["capo_neptune_graph.types.format.Format"]
    """<p>Specifies the format of S3 data to be imported. Valid values are <code>CSV</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a> or <code>OPENCYPHER</code>, which identies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>.</p>"""
    parquet_type: NotRequired["capo_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the import task.</p>"""
    role_arn: "capo_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>"""
    status: "capo_neptune_graph.types.import_task_status.ImportTaskStatus"
    """<p>Status of the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskSummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> ImportTaskSummary:
    out: ImportTaskSummary = {}  # type: ignore[typeddict-item]
    if data.get("graphId") is not None:
        out["graph_id"] = data["graphId"]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("ImportTaskSummary.task_id required")
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("ImportTaskSummary.source required")
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
        raise DeserializationError("ImportTaskSummary.role_arn required")
    if data.get("status") is not None:
        import capo_neptune_graph.types.import_task_status

        out["status"] = capo_neptune_graph.types.import_task_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ImportTaskSummary.status required")
    return out

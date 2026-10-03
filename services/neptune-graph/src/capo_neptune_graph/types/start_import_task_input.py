"""Generated from Smithy shape ``com.amazonaws.neptunegraph#StartImportTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptune_graph.types.blank_node_handling
    import capo_neptune_graph.types.format
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.import_options
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.role_arn


class StartImportTaskInput(TypedDict, closed=True):
    import_options: NotRequired["capo_neptune_graph.types.import_options.ImportOptions"]
    fail_on_error: NotRequired["bool"]
    """<p>If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.</p>"""
    source: "str"
    """<p>A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>"""
    format: NotRequired["capo_neptune_graph.types.format.Format"]
    """<p>Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identifies the openCypher load format.</p>"""
    parquet_type: NotRequired["capo_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the import task.</p>"""
    blank_node_handling: NotRequired[
        "capo_neptune_graph.types.blank_node_handling.BlankNodeHandling"
    ]
    """<p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling">Handling RDF values</a>.</p>"""
    graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    role_arn: "capo_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportTaskInput) -> dict:
    out: dict = {}
    if "import_options" in value:
        import capo_neptune_graph.types.import_options

        out["importOptions"] = capo_neptune_graph.types.import_options.serialize_json(
            value["import_options"]
        )
    if "fail_on_error" in value:
        out["failOnError"] = value["fail_on_error"]
    out["source"] = value["source"]
    if "format" in value:
        import capo_neptune_graph.types.format

        out["format"] = capo_neptune_graph.types.format.serialize_json(value["format"])
    if "parquet_type" in value:
        import capo_neptune_graph.types.parquet_type

        out["parquetType"] = capo_neptune_graph.types.parquet_type.serialize_json(
            value["parquet_type"]
        )
    if "blank_node_handling" in value:
        import capo_neptune_graph.types.blank_node_handling

        out["blankNodeHandling"] = (
            capo_neptune_graph.types.blank_node_handling.serialize_json(
                value["blank_node_handling"]
            )
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StartImportTaskInput:
    out: StartImportTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("importOptions") is not None:
        import capo_neptune_graph.types.import_options

        out["import_options"] = (
            capo_neptune_graph.types.import_options.deserialize_json(
                data["importOptions"]
            )
        )
    if data.get("failOnError") is not None:
        out["fail_on_error"] = data["failOnError"]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("StartImportTaskInput.source required")
    if data.get("format") is not None:
        import capo_neptune_graph.types.format

        out["format"] = capo_neptune_graph.types.format.deserialize_json(data["format"])
    if data.get("parquetType") is not None:
        import capo_neptune_graph.types.parquet_type

        out["parquet_type"] = capo_neptune_graph.types.parquet_type.deserialize_json(
            data["parquetType"]
        )
    if data.get("blankNodeHandling") is not None:
        import capo_neptune_graph.types.blank_node_handling

        out["blank_node_handling"] = (
            capo_neptune_graph.types.blank_node_handling.deserialize_json(
                data["blankNodeHandling"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StartImportTaskInput.role_arn required")
    return out

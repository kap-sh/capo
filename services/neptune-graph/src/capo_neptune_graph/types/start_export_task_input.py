"""Generated from Smithy shape ``com.amazonaws.neptunegraph#StartExportTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.export_filter
    import capo_neptune_graph.types.export_format
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.role_arn
    import capo_neptune_graph.types.tag_map


class StartExportTaskInput(TypedDict, closed=True):
    graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The source graph identifier of the export task.</p>"""
    role_arn: "capo_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow data to be exported to the destination.</p>"""
    format: "capo_neptune_graph.types.export_format.ExportFormat"
    """<p>The format of the export task.</p>"""
    destination: "str"
    """<p>The Amazon S3 URI where data will be exported to.</p>"""
    kms_key_identifier: "capo_neptune_graph.types.kms_key_arn.KmsKeyArn"
    """<p>The KMS key identifier of the export task.</p>"""
    parquet_type: NotRequired["capo_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the export task.</p>"""
    export_filter: NotRequired["capo_neptune_graph.types.export_filter.ExportFilter"]
    """<p>The export filter of the export task.</p>"""
    tags: NotRequired["capo_neptune_graph.types.tag_map.TagMap"]
    """<p>Tags to be applied to the export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExportTaskInput) -> dict:
    out: dict = {}
    out["graphIdentifier"] = value["graph_identifier"]
    out["roleArn"] = value["role_arn"]
    import capo_neptune_graph.types.export_format

    out["format"] = capo_neptune_graph.types.export_format.serialize_json(
        value["format"]
    )
    out["destination"] = value["destination"]
    out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "parquet_type" in value:
        import capo_neptune_graph.types.parquet_type

        out["parquetType"] = capo_neptune_graph.types.parquet_type.serialize_json(
            value["parquet_type"]
        )
    if "export_filter" in value:
        import capo_neptune_graph.types.export_filter

        out["exportFilter"] = capo_neptune_graph.types.export_filter.serialize_json(
            value["export_filter"]
        )
    if "tags" in value:
        import capo_neptune_graph.types.tag_map

        out["tags"] = capo_neptune_graph.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartExportTaskInput:
    out: StartExportTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("graphIdentifier") is not None:
        out["graph_identifier"] = data["graphIdentifier"]
    else:
        out["graph_identifier"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("format") is not None:
        import capo_neptune_graph.types.export_format

        out["format"] = capo_neptune_graph.types.export_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_neptune_graph.types.export_format.ExportFormat", ""
        )
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    else:
        out["destination"] = ""
    if data.get("kmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    else:
        out["kms_key_identifier"] = ""
    if data.get("parquetType") is not None:
        import capo_neptune_graph.types.parquet_type

        out["parquet_type"] = capo_neptune_graph.types.parquet_type.deserialize_json(
            data["parquetType"]
        )
    if data.get("exportFilter") is not None:
        import capo_neptune_graph.types.export_filter

        out["export_filter"] = capo_neptune_graph.types.export_filter.deserialize_json(
            data["exportFilter"]
        )
    if data.get("tags") is not None:
        import capo_neptune_graph.types.tag_map

        out["tags"] = capo_neptune_graph.types.tag_map.deserialize_json(data["tags"])
    return out

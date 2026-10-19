"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetExportTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.export_filter
    import capo_neptune_graph.types.export_format
    import capo_neptune_graph.types.export_task_details
    import capo_neptune_graph.types.export_task_id
    import capo_neptune_graph.types.export_task_status
    import capo_neptune_graph.types.graph_id
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.role_arn


class GetExportTaskOutput(TypedDict, closed=True):
    graph_id: "capo_neptune_graph.types.graph_id.GraphId"
    """<p>The source graph identifier of the export task.</p>"""
    role_arn: "capo_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow data to be exported to the destination.</p>"""
    task_id: "capo_neptune_graph.types.export_task_id.ExportTaskId"
    """<p>The unique identifier of the export task.</p>"""
    status: "capo_neptune_graph.types.export_task_status.ExportTaskStatus"
    """<p>The current status of the export task.</p>"""
    format: "capo_neptune_graph.types.export_format.ExportFormat"
    """<p>The format of the export task.</p>"""
    destination: "str"
    """<p>The Amazon S3 URI of the export task where data will be exported.</p>"""
    kms_key_identifier: "capo_neptune_graph.types.kms_key_arn.KmsKeyArn"
    """<p>The KMS key identifier of the export task.</p>"""
    parquet_type: NotRequired["capo_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the export task.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason that the export task has this status value.</p>"""
    export_task_details: NotRequired[
        "capo_neptune_graph.types.export_task_details.ExportTaskDetails"
    ]
    """<p>The details of the export task.</p>"""
    export_filter: NotRequired["capo_neptune_graph.types.export_filter.ExportFilter"]
    """<p>The export filter of the export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportTaskOutput) -> dict:
    out: dict = {}
    out["graphId"] = value["graph_id"]
    out["roleArn"] = value["role_arn"]
    out["taskId"] = value["task_id"]
    import capo_neptune_graph.types.export_task_status

    out["status"] = capo_neptune_graph.types.export_task_status.serialize_json(
        value["status"]
    )
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
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "export_task_details" in value:
        import capo_neptune_graph.types.export_task_details

        out["exportTaskDetails"] = (
            capo_neptune_graph.types.export_task_details.serialize_json(
                value["export_task_details"]
            )
        )
    if "export_filter" in value:
        import capo_neptune_graph.types.export_filter

        out["exportFilter"] = capo_neptune_graph.types.export_filter.serialize_json(
            value["export_filter"]
        )
    return out


def deserialize_json(data: dict) -> GetExportTaskOutput:
    out: GetExportTaskOutput = {}  # type: ignore[typeddict-item]
    if data.get("graphId") is not None:
        out["graph_id"] = data["graphId"]
    else:
        out["graph_id"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("status") is not None:
        import capo_neptune_graph.types.export_task_status

        out["status"] = capo_neptune_graph.types.export_task_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_neptune_graph.types.export_task_status.ExportTaskStatus", ""
        )
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
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("exportTaskDetails") is not None:
        import capo_neptune_graph.types.export_task_details

        out["export_task_details"] = (
            capo_neptune_graph.types.export_task_details.deserialize_json(
                data["exportTaskDetails"]
            )
        )
    if data.get("exportFilter") is not None:
        import capo_neptune_graph.types.export_filter

        out["export_filter"] = capo_neptune_graph.types.export_filter.deserialize_json(
            data["exportFilter"]
        )
    return out

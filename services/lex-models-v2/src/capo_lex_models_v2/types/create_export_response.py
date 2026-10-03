"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.export_resource_specification
    import capo_lex_models_v2.types.export_status
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_export_file_format
    import capo_lex_models_v2.types.timestamp


class CreateExportResponse(TypedDict, closed=True):
    export_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>An identifier for a specific request to create an export.</p>"""
    resource_specification: NotRequired[
        "capo_lex_models_v2.types.export_resource_specification.ExportResourceSpecification"
    ]
    """<p>A description of the type of resource that was exported, either a bot or a bot locale.</p>"""
    file_format: NotRequired[
        "capo_lex_models_v2.types.import_export_file_format.ImportExportFileFormat"
    ]
    """<p>The file format used for the bot or bot locale definition files.</p>"""
    export_status: NotRequired["capo_lex_models_v2.types.export_status.ExportStatus"]
    """<p>The status of the export. When the status is <code>Completed</code>, you can use the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html">DescribeExport</a> operation to get the pre-signed S3 URL link to your exported bot or bot locale.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the request to export a bot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportId"] = value["export_id"]
    if "resource_specification" in value:
        import capo_lex_models_v2.types.export_resource_specification

        out["resourceSpecification"] = (
            capo_lex_models_v2.types.export_resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    if "file_format" in value:
        import capo_lex_models_v2.types.import_export_file_format

        out["fileFormat"] = (
            capo_lex_models_v2.types.import_export_file_format.serialize_json(
                value["file_format"]
            )
        )
    if "export_status" in value:
        import capo_lex_models_v2.types.export_status

        out["exportStatus"] = capo_lex_models_v2.types.export_status.serialize_json(
            value["export_status"]
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateExportResponse:
    out: CreateExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("exportId") is not None:
        out["export_id"] = data["exportId"]
    if data.get("resourceSpecification") is not None:
        import capo_lex_models_v2.types.export_resource_specification

        out["resource_specification"] = (
            capo_lex_models_v2.types.export_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    if data.get("fileFormat") is not None:
        import capo_lex_models_v2.types.import_export_file_format

        out["file_format"] = (
            capo_lex_models_v2.types.import_export_file_format.deserialize_json(
                data["fileFormat"]
            )
        )
    if data.get("exportStatus") is not None:
        import capo_lex_models_v2.types.export_status

        out["export_status"] = capo_lex_models_v2.types.export_status.deserialize_json(
            data["exportStatus"]
        )
    if data.get("creationDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    return out

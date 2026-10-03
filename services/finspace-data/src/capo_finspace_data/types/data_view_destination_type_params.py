"""Generated from Smithy shape ``com.amazonaws.finspacedata#DataViewDestinationTypeParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_finspace_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace_data.types.data_view_destination_type
    import capo_finspace_data.types.export_file_format
    import capo_finspace_data.types.s3_destination_format_options


class DataViewDestinationTypeParams(TypedDict, closed=True):
    destination_type: (
        "capo_finspace_data.types.data_view_destination_type.DataViewDestinationType"
    )
    """<p>Destination type for a Dataview.</p> <ul> <li> <p> <code>GLUE_TABLE</code> – Glue table destination type.</p> </li> <li> <p> <code>S3</code> – S3 destination type.</p> </li> </ul>"""
    s3_destination_export_file_format: NotRequired[
        "capo_finspace_data.types.export_file_format.ExportFileFormat"
    ]
    """<p>Dataview export file format.</p> <ul> <li> <p> <code>PARQUET</code> – Parquet export file format.</p> </li> <li> <p> <code>DELIMITED_TEXT</code> – Delimited text export file format.</p> </li> </ul>"""
    s3_destination_export_file_format_options: NotRequired[
        "capo_finspace_data.types.s3_destination_format_options.S3DestinationFormatOptions"
    ]
    """<p>Format Options for S3 Destination type.</p> <p>Here is an example of how you could specify the <code>s3DestinationExportFileFormatOptions</code> </p> <p> <code> { "header": "true", "delimiter": ",", "compression": "gzip" }</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataViewDestinationTypeParams) -> dict:
    out: dict = {}
    out["destinationType"] = value["destination_type"]
    if "s3_destination_export_file_format" in value:
        import capo_finspace_data.types.export_file_format

        out["s3DestinationExportFileFormat"] = (
            capo_finspace_data.types.export_file_format.serialize_json(
                value["s3_destination_export_file_format"]
            )
        )
    if "s3_destination_export_file_format_options" in value:
        import capo_finspace_data.types.s3_destination_format_options

        out["s3DestinationExportFileFormatOptions"] = (
            capo_finspace_data.types.s3_destination_format_options.serialize_json(
                value["s3_destination_export_file_format_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataViewDestinationTypeParams:
    out: DataViewDestinationTypeParams = {}  # type: ignore[typeddict-item]
    if data.get("destinationType") is not None:
        out["destination_type"] = data["destinationType"]
    else:
        raise DeserializationError(
            "DataViewDestinationTypeParams.destination_type required"
        )
    if data.get("s3DestinationExportFileFormat") is not None:
        import capo_finspace_data.types.export_file_format

        out["s3_destination_export_file_format"] = (
            capo_finspace_data.types.export_file_format.deserialize_json(
                data["s3DestinationExportFileFormat"]
            )
        )
    if data.get("s3DestinationExportFileFormatOptions") is not None:
        import capo_finspace_data.types.s3_destination_format_options

        out["s3_destination_export_file_format_options"] = (
            capo_finspace_data.types.s3_destination_format_options.deserialize_json(
                data["s3DestinationExportFileFormatOptions"]
            )
        )
    return out

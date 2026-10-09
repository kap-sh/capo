"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.export_data_source
    import capo_sesv2.types.export_destination


class CreateExportJobRequest(TypedDict, closed=True):
    export_data_source: "capo_sesv2.types.export_data_source.ExportDataSource"
    """<p>The data source for the export job.</p>"""
    export_destination: "capo_sesv2.types.export_destination.ExportDestination"
    """<p>The destination for the export job. Specify only <code>DataFormat</code>. Do not include <code>S3Url</code> in this request. SES writes the export file to a location that it manages and returns the download URL in <code>GetExportJob</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExportJobRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.export_data_source

    out["ExportDataSource"] = capo_sesv2.types.export_data_source.serialize_json(
        value["export_data_source"]
    )
    import capo_sesv2.types.export_destination

    out["ExportDestination"] = capo_sesv2.types.export_destination.serialize_json(
        value["export_destination"]
    )
    return out


def deserialize_json(data: dict) -> CreateExportJobRequest:
    out: CreateExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExportDataSource") is not None:
        import capo_sesv2.types.export_data_source

        out["export_data_source"] = (
            capo_sesv2.types.export_data_source.deserialize_json(
                data["ExportDataSource"]
            )
        )
    else:
        raise DeserializationError("CreateExportJobRequest.export_data_source required")
    if data.get("ExportDestination") is not None:
        import capo_sesv2.types.export_destination

        out["export_destination"] = (
            capo_sesv2.types.export_destination.deserialize_json(
                data["ExportDestination"]
            )
        )
    else:
        raise DeserializationError("CreateExportJobRequest.export_destination required")
    return out

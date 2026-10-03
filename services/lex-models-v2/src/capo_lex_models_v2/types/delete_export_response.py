"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.export_status
    import capo_lex_models_v2.types.id


class DeleteExportResponse(TypedDict, closed=True):
    export_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the deleted export.</p>"""
    export_status: NotRequired["capo_lex_models_v2.types.export_status.ExportStatus"]
    """<p>The current status of the deletion. When the deletion is complete, the export will no longer be returned by the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListExports.html">ListExports</a> operation and calls to the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html"> DescribeExport</a> operation with the export identifier will fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportId"] = value["export_id"]
    if "export_status" in value:
        import capo_lex_models_v2.types.export_status

        out["exportStatus"] = capo_lex_models_v2.types.export_status.serialize_json(
            value["export_status"]
        )
    return out


def deserialize_json(data: dict) -> DeleteExportResponse:
    out: DeleteExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("exportId") is not None:
        out["export_id"] = data["exportId"]
    if data.get("exportStatus") is not None:
        import capo_lex_models_v2.types.export_status

        out["export_status"] = capo_lex_models_v2.types.export_status.deserialize_json(
            data["exportStatus"]
        )
    return out

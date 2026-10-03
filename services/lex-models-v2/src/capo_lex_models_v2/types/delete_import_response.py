"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_status


class DeleteImportResponse(TypedDict, closed=True):
    import_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the deleted import.</p>"""
    import_status: NotRequired["capo_lex_models_v2.types.import_status.ImportStatus"]
    """<p>The current status of the deletion. When the deletion is complete, the import will no longer be returned by the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListImports.html">ListImports</a> operation and calls to the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeImport.html">DescribeImport</a> operation with the import identifier will fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImportResponse) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_status" in value:
        import capo_lex_models_v2.types.import_status

        out["importStatus"] = capo_lex_models_v2.types.import_status.serialize_json(
            value["import_status"]
        )
    return out


def deserialize_json(data: dict) -> DeleteImportResponse:
    out: DeleteImportResponse = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    if data.get("importStatus") is not None:
        import capo_lex_models_v2.types.import_status

        out["import_status"] = capo_lex_models_v2.types.import_status.deserialize_json(
            data["importStatus"]
        )
    return out

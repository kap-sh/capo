"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationDocFile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.file_blob
    import capo_taxsettings.types.tax_document_name


class TaxRegistrationDocFile(TypedDict, closed=True):
    file_name: "capo_taxsettings.types.tax_document_name.TaxDocumentName"
    """<p>The tax registration document name. </p>"""
    file_content: "capo_taxsettings.types.file_blob.FileBlob"
    """<p>The tax registration document content. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationDocFile) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    import capo_taxsettings.types.file_blob

    out["fileContent"] = capo_taxsettings.types.file_blob.serialize_json(
        value["file_content"]
    )
    return out


def deserialize_json(data: dict) -> TaxRegistrationDocFile:
    out: TaxRegistrationDocFile = {}  # type: ignore[typeddict-item]
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("fileContent") is not None:
        import capo_taxsettings.types.file_blob

        out["file_content"] = capo_taxsettings.types.file_blob.deserialize_json(
            data["fileContent"]
        )
    else:
        out["file_content"] = b""
    return out

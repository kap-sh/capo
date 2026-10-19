"""Generated from Smithy shape ``com.amazonaws.taxsettings#ExemptionCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.exemption_document_name
    import capo_taxsettings.types.exemption_file_blob


class ExemptionCertificate(TypedDict, closed=True):
    document_name: (
        "capo_taxsettings.types.exemption_document_name.ExemptionDocumentName"
    )
    """<p>The exemption certificate file name. </p>"""
    document_file: "capo_taxsettings.types.exemption_file_blob.ExemptionFileBlob"
    """<p>The exemption certificate file content. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExemptionCertificate) -> dict:
    out: dict = {}
    out["documentName"] = value["document_name"]
    import capo_taxsettings.types.exemption_file_blob

    out["documentFile"] = capo_taxsettings.types.exemption_file_blob.serialize_json(
        value["document_file"]
    )
    return out


def deserialize_json(data: dict) -> ExemptionCertificate:
    out: ExemptionCertificate = {}  # type: ignore[typeddict-item]
    if data.get("documentName") is not None:
        out["document_name"] = data["documentName"]
    else:
        out["document_name"] = ""
    if data.get("documentFile") is not None:
        import capo_taxsettings.types.exemption_file_blob

        out["document_file"] = (
            capo_taxsettings.types.exemption_file_blob.deserialize_json(
                data["documentFile"]
            )
        )
    else:
        out["document_file"] = b""
    return out

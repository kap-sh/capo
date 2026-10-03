"""Generated from Smithy shape ``com.amazonaws.taxsettings#ChileAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.chile_document_type
    import capo_taxsettings.types.generic_string


class ChileAdditionalInfo(TypedDict, closed=True):
    document_type: NotRequired[
        "capo_taxsettings.types.chile_document_type.ChileDocumentType"
    ]
    """<p> The type of tax document. For Chile, this can be <code>Invoice</code> or <code>Receipt</code>.</p>"""
    business_activity: NotRequired[
        "capo_taxsettings.types.generic_string.GenericString"
    ]
    """<p> The business activity code of the taxpayer in Chile. This must be the activity code shown on your SII (Servicio de Impuestos Internos) tax profile. For the list of valid activity codes, see <a href="https://www.sii.cl/ayudas/ayudas_por_servicios/1956-codigos-1959.html">SII activity codes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChileAdditionalInfo) -> dict:
    out: dict = {}
    if "document_type" in value:
        import capo_taxsettings.types.chile_document_type

        out["documentType"] = capo_taxsettings.types.chile_document_type.serialize_json(
            value["document_type"]
        )
    if "business_activity" in value:
        out["businessActivity"] = value["business_activity"]
    return out


def deserialize_json(data: dict) -> ChileAdditionalInfo:
    out: ChileAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("documentType") is not None:
        import capo_taxsettings.types.chile_document_type

        out["document_type"] = (
            capo_taxsettings.types.chile_document_type.deserialize_json(
                data["documentType"]
            )
        )
    if data.get("businessActivity") is not None:
        out["business_activity"] = data["businessActivity"]
    return out

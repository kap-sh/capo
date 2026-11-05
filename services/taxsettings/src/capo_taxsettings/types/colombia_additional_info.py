"""Generated from Smithy shape ``com.amazonaws.taxsettings#ColombiaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.colombia_responsabilidades_list
    import capo_taxsettings.types.colombia_tipo_contribuyente_code
    import capo_taxsettings.types.date_string


class ColombiaAdditionalInfo(TypedDict, closed=True):
    responsibility_codes: NotRequired[
        "capo_taxsettings.types.colombia_responsabilidades_list.ColombiaResponsabilidadesList"
    ]
    """<p>The DIAN fiscal responsibility codes from Box 53 of the RUT document (for example, <code>48</code> for value-added tax (VAT) responsibility).</p>"""
    taxpayer_type_code: NotRequired[
        "capo_taxsettings.types.colombia_tipo_contribuyente_code.ColombiaTipoContribuyenteCode"
    ]
    """<p>The taxpayer category from Box 24 of the RUT document (<code>1</code> for a legal entity, <code>2</code> for a natural person).</p>"""
    issue_date: NotRequired["capo_taxsettings.types.date_string.DateString"]
    """<p>The issue date of the RUT document from Box 61, in <code>YYYY-MM-DD</code> format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColombiaAdditionalInfo) -> dict:
    out: dict = {}
    if "responsibility_codes" in value:
        import capo_taxsettings.types.colombia_responsabilidades_list

        out["responsibilityCodes"] = (
            capo_taxsettings.types.colombia_responsabilidades_list.serialize_json(
                value["responsibility_codes"]
            )
        )
    if "taxpayer_type_code" in value:
        out["taxpayerTypeCode"] = value["taxpayer_type_code"]
    if "issue_date" in value:
        out["issueDate"] = value["issue_date"]
    return out


def deserialize_json(data: dict) -> ColombiaAdditionalInfo:
    out: ColombiaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("responsibilityCodes") is not None:
        import capo_taxsettings.types.colombia_responsabilidades_list

        out["responsibility_codes"] = (
            capo_taxsettings.types.colombia_responsabilidades_list.deserialize_json(
                data["responsibilityCodes"]
            )
        )
    if data.get("taxpayerTypeCode") is not None:
        out["taxpayer_type_code"] = data["taxpayerTypeCode"]
    if data.get("issueDate") is not None:
        out["issue_date"] = data["issueDate"]
    return out

"""Generated from Smithy shape ``com.amazonaws.taxsettings#MexicoAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.mexico_cfdi_usage_code
    import capo_taxsettings.types.mexico_tax_regime_code
    import capo_taxsettings.types.mexico_tax_regime_full_name


class MexicoAdditionalInfo(TypedDict, closed=True):
    tax_regime: NotRequired[
        "capo_taxsettings.types.mexico_tax_regime_code.MexicoTaxRegimeCode"
    ]
    """<p>The SAT-assigned tax regime code for your business in Mexico. Must be a 3-digit number (for example, <code>601</code> for General de Ley Personas Morales).</p>"""
    tax_regime_full_name: NotRequired[
        "capo_taxsettings.types.mexico_tax_regime_full_name.MexicoTaxRegimeFullName"
    ]
    """<p>The full name of the SAT tax regime associated with your business in Mexico.</p>"""
    cfdi_usage_code: NotRequired[
        "capo_taxsettings.types.mexico_cfdi_usage_code.MexicoCfdiUsageCode"
    ]
    """<p>The SAT CFDI usage code that identifies the purpose of the invoice in Mexico (for example, <code>G01</code> for goods acquisition, <code>S01</code> for no tax effects).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MexicoAdditionalInfo) -> dict:
    out: dict = {}
    if "tax_regime" in value:
        out["taxRegime"] = value["tax_regime"]
    if "tax_regime_full_name" in value:
        out["taxRegimeFullName"] = value["tax_regime_full_name"]
    if "cfdi_usage_code" in value:
        out["cfdiUsageCode"] = value["cfdi_usage_code"]
    return out


def deserialize_json(data: dict) -> MexicoAdditionalInfo:
    out: MexicoAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("taxRegime") is not None:
        out["tax_regime"] = data["taxRegime"]
    if data.get("taxRegimeFullName") is not None:
        out["tax_regime_full_name"] = data["taxRegimeFullName"]
    if data.get("cfdiUsageCode") is not None:
        out["cfdi_usage_code"] = data["cfdiUsageCode"]
    return out

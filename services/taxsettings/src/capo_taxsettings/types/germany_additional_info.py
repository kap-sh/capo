"""Generated from Smithy shape ``com.amazonaws.taxsettings#GermanyAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.economic_identification_number
    import capo_taxsettings.types.steuernummer


class GermanyAdditionalInfo(TypedDict, closed=True):
    economic_identification_number: NotRequired[
        "capo_taxsettings.types.economic_identification_number.EconomicIdentificationNumber"
    ]
    """<p>The economic identification number (Wirtschafts-Identifikationsnummer, or W-IdNr) in Germany.</p>"""
    steuernummer: NotRequired["capo_taxsettings.types.steuernummer.Steuernummer"]
    """<p>The Steuernummer (tax number issued by the local tax office) in Germany.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GermanyAdditionalInfo) -> dict:
    out: dict = {}
    if "economic_identification_number" in value:
        out["economicIdentificationNumber"] = value["economic_identification_number"]
    if "steuernummer" in value:
        out["steuernummer"] = value["steuernummer"]
    return out


def deserialize_json(data: dict) -> GermanyAdditionalInfo:
    out: GermanyAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("economicIdentificationNumber") is not None:
        out["economic_identification_number"] = data["economicIdentificationNumber"]
    if data.get("steuernummer") is not None:
        out["steuernummer"] = data["steuernummer"]
    return out

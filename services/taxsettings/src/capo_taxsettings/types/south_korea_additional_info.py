"""Generated from Smithy shape ``com.amazonaws.taxsettings#SouthKoreaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.business_representative_name
    import capo_taxsettings.types.item_of_business
    import capo_taxsettings.types.line_of_business


class SouthKoreaAdditionalInfo(TypedDict, closed=True):
    business_representative_name: (
        "capo_taxsettings.types.business_representative_name.BusinessRepresentativeName"
    )
    """<p>The business legal name based on the most recently uploaded tax registration certificate.</p>"""
    line_of_business: "capo_taxsettings.types.line_of_business.LineOfBusiness"
    """<p>Line of business based on the most recently uploaded tax registration certificate.</p>"""
    item_of_business: "capo_taxsettings.types.item_of_business.ItemOfBusiness"
    """<p>Item of business based on the most recently uploaded tax registration certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SouthKoreaAdditionalInfo) -> dict:
    out: dict = {}
    out["businessRepresentativeName"] = value["business_representative_name"]
    out["lineOfBusiness"] = value["line_of_business"]
    out["itemOfBusiness"] = value["item_of_business"]
    return out


def deserialize_json(data: dict) -> SouthKoreaAdditionalInfo:
    out: SouthKoreaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("businessRepresentativeName") is not None:
        out["business_representative_name"] = data["businessRepresentativeName"]
    else:
        out["business_representative_name"] = ""
    if data.get("lineOfBusiness") is not None:
        out["line_of_business"] = data["lineOfBusiness"]
    else:
        out["line_of_business"] = ""
    if data.get("itemOfBusiness") is not None:
        out["item_of_business"] = data["itemOfBusiness"]
    else:
        out["item_of_business"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.taxsettings#EstoniaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.registry_commercial_code


class EstoniaAdditionalInfo(TypedDict, closed=True):
    registry_commercial_code: (
        "capo_taxsettings.types.registry_commercial_code.RegistryCommercialCode"
    )
    """<p> Registry commercial code (RCC) for your TRN in Estonia. This value is an eight-numeric string, such as <code>12345678</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EstoniaAdditionalInfo) -> dict:
    out: dict = {}
    out["registryCommercialCode"] = value["registry_commercial_code"]
    return out


def deserialize_json(data: dict) -> EstoniaAdditionalInfo:
    out: EstoniaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("registryCommercialCode") is not None:
        out["registry_commercial_code"] = data["registryCommercialCode"]
    else:
        out["registry_commercial_code"] = ""
    return out

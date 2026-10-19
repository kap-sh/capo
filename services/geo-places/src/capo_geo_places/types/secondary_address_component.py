"""Generated from Smithy shape ``com.amazonaws.geoplaces#SecondaryAddressComponent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class SecondaryAddressComponent(TypedDict, closed=True):
    number: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>Number that uniquely identifies a secondary address.</p>"""
    designator: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The designator of the secondary address component.</p> <p>Example: <code>Apt</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryAddressComponent) -> dict:
    out: dict = {}
    out["Number"] = value["number"]
    if "designator" in value:
        out["Designator"] = value["designator"]
    return out


def deserialize_json(data: dict) -> SecondaryAddressComponent:
    out: SecondaryAddressComponent = {}  # type: ignore[typeddict-item]
    if data.get("Number") is not None:
        out["number"] = data["Number"]
    else:
        out["number"] = ""
    if data.get("Designator") is not None:
        out["designator"] = data["Designator"]
    return out


def redact_sensitive(value: SecondaryAddressComponent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "number" in value:
        out["number"] = "*** Sensitive Data Redacted ***"
    if "designator" in value:
        out["designator"] = "*** Sensitive Data Redacted ***"
    return out

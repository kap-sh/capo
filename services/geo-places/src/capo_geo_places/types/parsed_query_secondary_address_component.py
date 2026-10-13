"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQuerySecondaryAddressComponent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class ParsedQuerySecondaryAddressComponent(TypedDict, closed=True):
    start_index: "int"
    """<p>Start index of the parsed secondary address component in the query text.</p>"""
    end_index: "int"
    """<p>End index of the parsed secondary address component in the query text.</p>"""
    value: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>Value of the parsed secondary address component.</p>"""
    number: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>Secondary address number provided in the query.</p>"""
    designator: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>Secondary address designator provided in the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQuerySecondaryAddressComponent) -> dict:
    out: dict = {}
    out["StartIndex"] = value["start_index"]
    out["EndIndex"] = value["end_index"]
    out["Value"] = value["value"]
    out["Number"] = value["number"]
    out["Designator"] = value["designator"]
    return out


def deserialize_json(data: dict) -> ParsedQuerySecondaryAddressComponent:
    out: ParsedQuerySecondaryAddressComponent = {}  # type: ignore[typeddict-item]
    if data.get("StartIndex") is not None:
        out["start_index"] = data["StartIndex"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.start_index required"
        )
    if data.get("EndIndex") is not None:
        out["end_index"] = data["EndIndex"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.end_index required"
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.value required"
        )
    if data.get("Number") is not None:
        out["number"] = data["Number"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.number required"
        )
    if data.get("Designator") is not None:
        out["designator"] = data["Designator"]
    else:
        raise DeserializationError(
            "ParsedQuerySecondaryAddressComponent.designator required"
        )
    return out


def redact_sensitive(value: ParsedQuerySecondaryAddressComponent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    if "number" in value:
        out["number"] = "*** Sensitive Data Redacted ***"
    if "designator" in value:
        out["designator"] = "*** Sensitive Data Redacted ***"
    return out

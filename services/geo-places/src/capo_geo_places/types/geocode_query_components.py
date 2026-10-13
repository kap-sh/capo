"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeQueryComponents``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class GeocodeQueryComponents(TypedDict, closed=True):
    country: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The region or state results should be to be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The city or locality results should be present in. </p> <p>Example: <code>Vancouver</code>.</p>"""
    district: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The district or division of a city the results should be present in.</p>"""
    street: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The name of the street results should be present in.</p>"""
    address_number: NotRequired[
        "capo_geo_places.types.sensitive_string.SensitiveString"
    ]
    """<p>The house number or address results should have. </p>"""
    postal_code: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeQueryComponents) -> dict:
    out: dict = {}
    if "country" in value:
        out["Country"] = value["country"]
    if "region" in value:
        out["Region"] = value["region"]
    if "sub_region" in value:
        out["SubRegion"] = value["sub_region"]
    if "locality" in value:
        out["Locality"] = value["locality"]
    if "district" in value:
        out["District"] = value["district"]
    if "street" in value:
        out["Street"] = value["street"]
    if "address_number" in value:
        out["AddressNumber"] = value["address_number"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    return out


def deserialize_json(data: dict) -> GeocodeQueryComponents:
    out: GeocodeQueryComponents = {}  # type: ignore[typeddict-item]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("SubRegion") is not None:
        out["sub_region"] = data["SubRegion"]
    if data.get("Locality") is not None:
        out["locality"] = data["Locality"]
    if data.get("District") is not None:
        out["district"] = data["District"]
    if data.get("Street") is not None:
        out["street"] = data["Street"]
    if data.get("AddressNumber") is not None:
        out["address_number"] = data["AddressNumber"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    return out


def redact_sensitive(value: GeocodeQueryComponents) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "country" in value:
        out["country"] = "*** Sensitive Data Redacted ***"
    if "region" in value:
        out["region"] = "*** Sensitive Data Redacted ***"
    if "sub_region" in value:
        out["sub_region"] = "*** Sensitive Data Redacted ***"
    if "locality" in value:
        out["locality"] = "*** Sensitive Data Redacted ***"
    if "district" in value:
        out["district"] = "*** Sensitive Data Redacted ***"
    if "street" in value:
        out["street"] = "*** Sensitive Data Redacted ***"
    if "address_number" in value:
        out["address_number"] = "*** Sensitive Data Redacted ***"
    if "postal_code" in value:
        out["postal_code"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#RemoteIpDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.city
    import capo_guardduty.types.country
    import capo_guardduty.types.geo_location
    import capo_guardduty.types.organization
    import capo_guardduty.types.sensitive_string


class RemoteIpDetails(TypedDict, closed=True):
    city: NotRequired["capo_guardduty.types.city.City"]
    """<p>The city information of the remote IP address.</p>"""
    country: NotRequired["capo_guardduty.types.country.Country"]
    """<p>The country code of the remote IP address.</p>"""
    geo_location: NotRequired["capo_guardduty.types.geo_location.GeoLocation"]
    """<p>The location information of the remote IP address.</p>"""
    ip_address_v4: NotRequired["capo_guardduty.types.sensitive_string.SensitiveString"]
    """<p>The IPv4 remote address of the connection.</p>"""
    ip_address_v6: NotRequired["capo_guardduty.types.sensitive_string.SensitiveString"]
    """<p>The IPv6 remote address of the connection.</p>"""
    organization: NotRequired["capo_guardduty.types.organization.Organization"]
    """<p>The ISP organization information of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteIpDetails) -> dict:
    out: dict = {}
    if "city" in value:
        import capo_guardduty.types.city

        out["city"] = capo_guardduty.types.city.serialize_json(value["city"])
    if "country" in value:
        import capo_guardduty.types.country

        out["country"] = capo_guardduty.types.country.serialize_json(value["country"])
    if "geo_location" in value:
        import capo_guardduty.types.geo_location

        out["geoLocation"] = capo_guardduty.types.geo_location.serialize_json(
            value["geo_location"]
        )
    if "ip_address_v4" in value:
        out["ipAddressV4"] = value["ip_address_v4"]
    if "ip_address_v6" in value:
        out["ipAddressV6"] = value["ip_address_v6"]
    if "organization" in value:
        import capo_guardduty.types.organization

        out["organization"] = capo_guardduty.types.organization.serialize_json(
            value["organization"]
        )
    return out


def deserialize_json(data: dict) -> RemoteIpDetails:
    out: RemoteIpDetails = {}  # type: ignore[typeddict-item]
    if data.get("city") is not None:
        import capo_guardduty.types.city

        out["city"] = capo_guardduty.types.city.deserialize_json(data["city"])
    if data.get("country") is not None:
        import capo_guardduty.types.country

        out["country"] = capo_guardduty.types.country.deserialize_json(data["country"])
    if data.get("geoLocation") is not None:
        import capo_guardduty.types.geo_location

        out["geo_location"] = capo_guardduty.types.geo_location.deserialize_json(
            data["geoLocation"]
        )
    if data.get("ipAddressV4") is not None:
        out["ip_address_v4"] = data["ipAddressV4"]
    if data.get("ipAddressV6") is not None:
        out["ip_address_v6"] = data["ipAddressV6"]
    if data.get("organization") is not None:
        import capo_guardduty.types.organization

        out["organization"] = capo_guardduty.types.organization.deserialize_json(
            data["organization"]
        )
    return out


def redact_sensitive(value: RemoteIpDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_address_v4" in value:
        out["ip_address_v4"] = "*** Sensitive Data Redacted ***"
    if "ip_address_v6" in value:
        out["ip_address_v6"] = "*** Sensitive Data Redacted ***"
    return out

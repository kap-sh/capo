"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ImpactedLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.health_event_status
    import capo_internetmonitor.types.internet_health
    import capo_internetmonitor.types.ipv4_prefix_list
    import capo_internetmonitor.types.network_impairment


class ImpactedLocation(TypedDict, closed=True):
    as_name: "str"
    """<p>The name of the internet service provider (ISP) or network (ASN).</p>"""
    as_number: "int"
    """<p>The Autonomous System Number (ASN) of the network at an impacted location.</p>"""
    country: "str"
    """<p>The name of the country where the health event is located.</p>"""
    subdivision: NotRequired["str"]
    """<p>The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).</p>"""
    metro: NotRequired["str"]
    """<p>The metro area where the health event is located.</p> <p>Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.</p>"""
    city: NotRequired["str"]
    """<p>The name of the city where the health event is located.</p>"""
    latitude: NotRequired["float"]
    """<p>The latitude where the health event is located.</p>"""
    longitude: NotRequired["float"]
    """<p>The longitude where the health event is located.</p>"""
    country_code: NotRequired["str"]
    """<p>The country code where the health event is located. The ISO 3166-2 codes for the country is provided, when available. </p>"""
    subdivision_code: NotRequired["str"]
    """<p>The subdivision code where the health event is located. The ISO 3166-2 codes for country subdivisions is provided, when available. </p>"""
    service_location: NotRequired["str"]
    """<p>The service location where the health event is located.</p>"""
    status: "capo_internetmonitor.types.health_event_status.HealthEventStatus"
    """<p>The status of the health event at an impacted location.</p>"""
    caused_by: NotRequired[
        "capo_internetmonitor.types.network_impairment.NetworkImpairment"
    ]
    """<p>The cause of the impairment. There are two types of network impairments: Amazon Web Services network issues or internet issues. Internet issues are typically a problem with a network provider, like an internet service provider (ISP).</p>"""
    internet_health: NotRequired[
        "capo_internetmonitor.types.internet_health.InternetHealth"
    ]
    """<p>The calculated health at a specific location.</p>"""
    ipv4_prefixes: NotRequired[
        "capo_internetmonitor.types.ipv4_prefix_list.Ipv4PrefixList"
    ]
    """<p>The IPv4 prefixes at the client location that was impacted by the health event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedLocation) -> dict:
    out: dict = {}
    out["ASName"] = value["as_name"]
    out["ASNumber"] = value["as_number"]
    out["Country"] = value["country"]
    if "subdivision" in value:
        out["Subdivision"] = value["subdivision"]
    if "metro" in value:
        out["Metro"] = value["metro"]
    if "city" in value:
        out["City"] = value["city"]
    if "latitude" in value:
        out["Latitude"] = (
            "NaN"
            if value["latitude"] != value["latitude"]
            else "Infinity"
            if value["latitude"] == float("inf")
            else "-Infinity"
            if value["latitude"] == float("-inf")
            else value["latitude"]
        )
    if "longitude" in value:
        out["Longitude"] = (
            "NaN"
            if value["longitude"] != value["longitude"]
            else "Infinity"
            if value["longitude"] == float("inf")
            else "-Infinity"
            if value["longitude"] == float("-inf")
            else value["longitude"]
        )
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "subdivision_code" in value:
        out["SubdivisionCode"] = value["subdivision_code"]
    if "service_location" in value:
        out["ServiceLocation"] = value["service_location"]
    out["Status"] = value["status"]
    if "caused_by" in value:
        import capo_internetmonitor.types.network_impairment

        out["CausedBy"] = capo_internetmonitor.types.network_impairment.serialize_json(
            value["caused_by"]
        )
    if "internet_health" in value:
        import capo_internetmonitor.types.internet_health

        out["InternetHealth"] = (
            capo_internetmonitor.types.internet_health.serialize_json(
                value["internet_health"]
            )
        )
    if "ipv4_prefixes" in value:
        import capo_internetmonitor.types.ipv4_prefix_list

        out["Ipv4Prefixes"] = (
            capo_internetmonitor.types.ipv4_prefix_list.serialize_json(
                value["ipv4_prefixes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImpactedLocation:
    out: ImpactedLocation = {}  # type: ignore[typeddict-item]
    if data.get("ASName") is not None:
        out["as_name"] = data["ASName"]
    else:
        out["as_name"] = ""
    if data.get("ASNumber") is not None:
        out["as_number"] = data["ASNumber"]
    else:
        out["as_number"] = 0
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    else:
        out["country"] = ""
    if data.get("Subdivision") is not None:
        out["subdivision"] = data["Subdivision"]
    if data.get("Metro") is not None:
        out["metro"] = data["Metro"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("Latitude") is not None:
        out["latitude"] = float(data["Latitude"])
    if data.get("Longitude") is not None:
        out["longitude"] = float(data["Longitude"])
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    if data.get("SubdivisionCode") is not None:
        out["subdivision_code"] = data["SubdivisionCode"]
    if data.get("ServiceLocation") is not None:
        out["service_location"] = data["ServiceLocation"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("CausedBy") is not None:
        import capo_internetmonitor.types.network_impairment

        out["caused_by"] = (
            capo_internetmonitor.types.network_impairment.deserialize_json(
                data["CausedBy"]
            )
        )
    if data.get("InternetHealth") is not None:
        import capo_internetmonitor.types.internet_health

        out["internet_health"] = (
            capo_internetmonitor.types.internet_health.deserialize_json(
                data["InternetHealth"]
            )
        )
    if data.get("Ipv4Prefixes") is not None:
        import capo_internetmonitor.types.ipv4_prefix_list

        out["ipv4_prefixes"] = (
            capo_internetmonitor.types.ipv4_prefix_list.deserialize_json(
                data["Ipv4Prefixes"]
            )
        )
    return out

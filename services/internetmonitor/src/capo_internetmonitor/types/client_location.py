"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ClientLocation``."""

from typing_extensions import NotRequired, TypedDict


class ClientLocation(TypedDict, closed=True):
    as_name: "str"
    """<p>The name of the internet service provider (ISP) or network (ASN).</p>"""
    as_number: "int"
    """<p>The Autonomous System Number (ASN) of the network at an impacted location.</p>"""
    country: "str"
    """<p>The name of the country where the internet event is located.</p>"""
    subdivision: NotRequired["str"]
    """<p>The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).</p>"""
    metro: NotRequired["str"]
    """<p>The metro area where the health event is located.</p> <p>Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.</p>"""
    city: "str"
    """<p>The name of the city where the internet event is located.</p>"""
    latitude: "float"
    """<p>The latitude where the internet event is located.</p>"""
    longitude: "float"
    """<p>The longitude where the internet event is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientLocation) -> dict:
    out: dict = {}
    out["ASName"] = value["as_name"]
    out["ASNumber"] = value["as_number"]
    out["Country"] = value["country"]
    if "subdivision" in value:
        out["Subdivision"] = value["subdivision"]
    if "metro" in value:
        out["Metro"] = value["metro"]
    out["City"] = value["city"]
    out["Latitude"] = (
        "NaN"
        if value["latitude"] != value["latitude"]
        else "Infinity"
        if value["latitude"] == float("inf")
        else "-Infinity"
        if value["latitude"] == float("-inf")
        else value["latitude"]
    )
    out["Longitude"] = (
        "NaN"
        if value["longitude"] != value["longitude"]
        else "Infinity"
        if value["longitude"] == float("inf")
        else "-Infinity"
        if value["longitude"] == float("-inf")
        else value["longitude"]
    )
    return out


def deserialize_json(data: dict) -> ClientLocation:
    out: ClientLocation = {}  # type: ignore[typeddict-item]
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
    else:
        out["city"] = ""
    if data.get("Latitude") is not None:
        out["latitude"] = float(data["Latitude"])
    else:
        out["latitude"] = 0.0
    if data.get("Longitude") is not None:
        out["longitude"] = float(data["Longitude"])
    else:
        out["longitude"] = 0.0
    return out

"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ClientLocation``."""

from typing_extensions import NotRequired, TypedDict


class ClientLocation(TypedDict, closed=True):
    city: NotRequired["str"]
    """<p>The city where the client is located.</p>"""
    subdivision: NotRequired["str"]
    """<p>The subdivision, such as a state or province, where the client is located.</p>"""
    country: NotRequired["str"]
    """<p>The country where the client is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientLocation) -> dict:
    out: dict = {}
    if "city" in value:
        out["city"] = value["city"]
    if "subdivision" in value:
        out["subdivision"] = value["subdivision"]
    if "country" in value:
        out["country"] = value["country"]
    return out


def deserialize_json(data: dict) -> ClientLocation:
    out: ClientLocation = {}  # type: ignore[typeddict-item]
    if data.get("city") is not None:
        out["city"] = data["city"]
    if data.get("subdivision") is not None:
        out["subdivision"] = data["subdivision"]
    if data.get("country") is not None:
        out["country"] = data["country"]
    return out

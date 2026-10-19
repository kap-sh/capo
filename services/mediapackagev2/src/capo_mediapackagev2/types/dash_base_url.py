"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashBaseUrl``."""

from typing_extensions import NotRequired, TypedDict


class DashBaseUrl(TypedDict, closed=True):
    url: "str"
    """<p>A source location for segments.</p>"""
    service_location: NotRequired["str"]
    """<p>The name of the source location.</p>"""
    dvb_priority: NotRequired["int"]
    """<p>For use with DVB-DASH profiles only. The priority of this location for servings segments. The lower the number, the higher the priority.</p>"""
    dvb_weight: NotRequired["int"]
    """<p>For use with DVB-DASH profiles only. The weighting for source locations that have the same priority. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashBaseUrl) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    if "service_location" in value:
        out["ServiceLocation"] = value["service_location"]
    if "dvb_priority" in value:
        out["DvbPriority"] = value["dvb_priority"]
    if "dvb_weight" in value:
        out["DvbWeight"] = value["dvb_weight"]
    return out


def deserialize_json(data: dict) -> DashBaseUrl:
    out: DashBaseUrl = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    if data.get("ServiceLocation") is not None:
        out["service_location"] = data["ServiceLocation"]
    if data.get("DvbPriority") is not None:
        out["dvb_priority"] = data["DvbPriority"]
    if data.get("DvbWeight") is not None:
        out["dvb_weight"] = data["DvbWeight"]
    return out

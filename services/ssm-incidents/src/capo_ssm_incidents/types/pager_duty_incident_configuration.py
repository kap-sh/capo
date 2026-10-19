"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PagerDutyIncidentConfiguration``."""

from typing_extensions import TypedDict


class PagerDutyIncidentConfiguration(TypedDict, closed=True):
    service_id: "str"
    """<p>The ID of the PagerDuty service that the response plan associates with an incident when it launches.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyIncidentConfiguration) -> dict:
    out: dict = {}
    out["serviceId"] = value["service_id"]
    return out


def deserialize_json(data: dict) -> PagerDutyIncidentConfiguration:
    out: PagerDutyIncidentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("serviceId") is not None:
        out["service_id"] = data["serviceId"]
    else:
        out["service_id"] = ""
    return out

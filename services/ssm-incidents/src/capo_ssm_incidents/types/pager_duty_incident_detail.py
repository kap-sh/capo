"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PagerDutyIncidentDetail``."""

from typing_extensions import NotRequired, TypedDict


class PagerDutyIncidentDetail(TypedDict, closed=True):
    id: "str"
    """<p>The ID of the incident associated with the PagerDuty service for the response plan.</p>"""
    auto_resolve: NotRequired["bool"]
    """<p>Indicates whether to resolve the PagerDuty incident when you resolve the associated Incident Manager incident.</p>"""
    secret_id: NotRequired["str"]
    """<p>The ID of the Amazon Web Services Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyIncidentDetail) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "auto_resolve" in value:
        out["autoResolve"] = value["auto_resolve"]
    if "secret_id" in value:
        out["secretId"] = value["secret_id"]
    return out


def deserialize_json(data: dict) -> PagerDutyIncidentDetail:
    out: PagerDutyIncidentDetail = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("autoResolve") is not None:
        out["auto_resolve"] = data["autoResolve"]
    if data.get("secretId") is not None:
        out["secret_id"] = data["secretId"]
    return out

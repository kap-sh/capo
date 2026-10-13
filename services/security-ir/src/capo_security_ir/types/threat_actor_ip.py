"""Generated from Smithy shape ``com.amazonaws.securityir#ThreatActorIp``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.ip_address
    import capo_security_ir.types.user_agent


class ThreatActorIp(TypedDict, closed=True):
    ip_address: "capo_security_ir.types.ip_address.IPAddress"
    """<p/>"""
    user_agent: NotRequired["capo_security_ir.types.user_agent.UserAgent"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatActorIp) -> dict:
    out: dict = {}
    out["ipAddress"] = value["ip_address"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> ThreatActorIp:
    out: ThreatActorIp = {}  # type: ignore[typeddict-item]
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    else:
        raise DeserializationError("ThreatActorIp.ip_address required")
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    return out


def redact_sensitive(value: ThreatActorIp) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_address" in value:
        out["ip_address"] = "*** Sensitive Data Redacted ***"
    return out

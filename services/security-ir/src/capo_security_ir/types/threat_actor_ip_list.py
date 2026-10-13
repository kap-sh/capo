"""Generated from Smithy shape ``com.amazonaws.securityir#ThreatActorIpList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.threat_actor_ip

ThreatActorIpList: TypeAlias = list[
    "capo_security_ir.types.threat_actor_ip.ThreatActorIp"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatActorIpList) -> list:
    import capo_security_ir.types.threat_actor_ip

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.threat_actor_ip.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatActorIpList:
    import capo_security_ir.types.threat_actor_ip

    out: ThreatActorIpList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_security_ir.types.threat_actor_ip.deserialize_json(item))
    return out


def redact_sensitive(value: ThreatActorIpList) -> list[Any]:
    import capo_security_ir.types.threat_actor_ip

    return [
        capo_security_ir.types.threat_actor_ip.redact_sensitive(item) for item in value
    ]

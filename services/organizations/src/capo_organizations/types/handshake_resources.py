"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeResources``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.handshake_resource

HandshakeResources: TypeAlias = list[
    "capo_organizations.types.handshake_resource.HandshakeResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeResources) -> list:
    import capo_organizations.types.handshake_resource

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.handshake_resource.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HandshakeResources:
    import capo_organizations.types.handshake_resource

    out: HandshakeResources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_organizations.types.handshake_resource.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: HandshakeResources) -> list[Any]:
    import capo_organizations.types.handshake_resource

    return [
        capo_organizations.types.handshake_resource.redact_sensitive(item)
        for item in value
    ]

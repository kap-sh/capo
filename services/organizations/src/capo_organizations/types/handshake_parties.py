"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeParties``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.handshake_party

HandshakeParties: TypeAlias = list[
    "capo_organizations.types.handshake_party.HandshakeParty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeParties) -> list:
    import capo_organizations.types.handshake_party

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.handshake_party.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HandshakeParties:
    import capo_organizations.types.handshake_party

    out: HandshakeParties = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_organizations.types.handshake_party.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: HandshakeParties) -> list[Any]:
    import capo_organizations.types.handshake_party

    return [
        capo_organizations.types.handshake_party.redact_sensitive(item)
        for item in value
    ]

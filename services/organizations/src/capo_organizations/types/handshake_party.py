"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeParty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.handshake_party_id
    import capo_organizations.types.handshake_party_type


class HandshakeParty(TypedDict, closed=True):
    id: "capo_organizations.types.handshake_party_id.HandshakePartyId"
    """<p>ID for the participant: Acccount ID, organization ID, or email address.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for handshake ID string requires "h-" followed by from 8 to 32 lowercase letters or digits.</p>"""
    type: "capo_organizations.types.handshake_party_type.HandshakePartyType"
    """<p>The type of ID for the participant.</p> <note> <p>ORGANIZATION is valid only in the response context (identifying the inviting organization). Valid input values for the Target parameter are ACCOUNT and EMAIL only.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeParty) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_organizations.types.handshake_party_type

    out["Type"] = capo_organizations.types.handshake_party_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> HandshakeParty:
    out: HandshakeParty = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("HandshakeParty.id required")
    if data.get("Type") is not None:
        import capo_organizations.types.handshake_party_type

        out["type"] = (
            capo_organizations.types.handshake_party_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("HandshakeParty.type required")
    return out

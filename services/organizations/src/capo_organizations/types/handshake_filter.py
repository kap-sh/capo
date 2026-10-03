"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.action_type
    import capo_organizations.types.handshake_id


class HandshakeFilter(TypedDict, closed=True):
    action_type: NotRequired["capo_organizations.types.action_type.ActionType"]
    """<p>The type of handshake.</p> <p>If you specify <code>ActionType</code>, you cannot also specify <code>ParentHandshakeId</code>.</p>"""
    parent_handshake_id: NotRequired[
        "capo_organizations.types.handshake_id.HandshakeId"
    ]
    """<p>The parent handshake. Only used for handshake types that are a child of another type.</p> <p>If you specify <code>ParentHandshakeId</code>, you cannot also specify <code>ActionType</code>.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for handshake ID string requires "h-" followed by from 8 to 32 lowercase letters or digits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeFilter) -> dict:
    out: dict = {}
    if "action_type" in value:
        import capo_organizations.types.action_type

        out["ActionType"] = capo_organizations.types.action_type.serialize_aws_json_1_1(
            value["action_type"]
        )
    if "parent_handshake_id" in value:
        out["ParentHandshakeId"] = value["parent_handshake_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HandshakeFilter:
    out: HandshakeFilter = {}  # type: ignore[typeddict-item]
    if data.get("ActionType") is not None:
        import capo_organizations.types.action_type

        out["action_type"] = (
            capo_organizations.types.action_type.deserialize_aws_json_1_1(
                data["ActionType"]
            )
        )
    if data.get("ParentHandshakeId") is not None:
        out["parent_handshake_id"] = data["ParentHandshakeId"]
    return out

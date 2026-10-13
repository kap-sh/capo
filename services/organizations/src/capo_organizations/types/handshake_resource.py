"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeResource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake_resource_type
    import capo_organizations.types.handshake_resource_value
    import capo_organizations.types.handshake_resources


class HandshakeResource(TypedDict, closed=True):
    value: NotRequired[
        "capo_organizations.types.handshake_resource_value.HandshakeResourceValue"
    ]
    """<p>Additional information for the handshake. The format of the value string must match the requirements of the specified type.</p>"""
    type: NotRequired[
        "capo_organizations.types.handshake_resource_type.HandshakeResourceType"
    ]
    """<p>The type of information being passed, specifying how the value is to be interpreted by the other party:</p> <ul> <li> <p> <b>ACCOUNT</b>: ID for an Amazon Web Services account.</p> </li> <li> <p> <b>ORGANIZATION</b>: ID for an organization.</p> </li> <li> <p> <b>EMAIL</b>: Email address for the recipient.</p> </li> <li> <p> <b>OWNER_EMAIL</b>: Email address for the sender.</p> </li> <li> <p> <b>OWNER_NAME</b>: Name of the sender.</p> </li> <li> <p> <b>NOTES</b>: Additional text included by the sender for the recipient.</p> </li> </ul>"""
    resources: NotRequired[
        "capo_organizations.types.handshake_resources.HandshakeResources"
    ]
    """<p>An array of <code>HandshakeResource</code> objects. When needed, contains additional details for a handshake. For example, the email address for the sender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeResource) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        import capo_organizations.types.handshake_resource_type

        out["Type"] = (
            capo_organizations.types.handshake_resource_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "resources" in value:
        import capo_organizations.types.handshake_resources

        out["Resources"] = (
            capo_organizations.types.handshake_resources.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HandshakeResource:
    out: HandshakeResource = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Type") is not None:
        import capo_organizations.types.handshake_resource_type

        out["type"] = (
            capo_organizations.types.handshake_resource_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Resources") is not None:
        import capo_organizations.types.handshake_resources

        out["resources"] = (
            capo_organizations.types.handshake_resources.deserialize_aws_json_1_1(
                data["Resources"]
            )
        )
    return out


def redact_sensitive(value: HandshakeResource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    if "resources" in value:
        import capo_organizations.types.handshake_resources

        out["resources"] = (
            capo_organizations.types.handshake_resources.redact_sensitive(
                value["resources"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateMemberInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain.types.client_request_token_string
    import capo_managedblockchain.types.member_configuration
    import capo_managedblockchain.types.resource_id_string


class CreateMemberInput(TypedDict, closed=True):
    client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>"""
    invitation_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the invitation that is sent to the member to join the network.</p>"""
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network in which the member is created.</p>"""
    member_configuration: (
        "capo_managedblockchain.types.member_configuration.MemberConfiguration"
    )
    """<p>Member configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemberInput) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    out["InvitationId"] = value["invitation_id"]
    import capo_managedblockchain.types.member_configuration

    out["MemberConfiguration"] = (
        capo_managedblockchain.types.member_configuration.serialize_json(
            value["member_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateMemberInput:
    out: CreateMemberInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        out["client_request_token"] = ""
    if data.get("InvitationId") is not None:
        out["invitation_id"] = data["InvitationId"]
    else:
        out["invitation_id"] = ""
    if data.get("MemberConfiguration") is not None:
        import capo_managedblockchain.types.member_configuration

        out["member_configuration"] = (
            capo_managedblockchain.types.member_configuration.deserialize_json(
                data["MemberConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateMemberInput.member_configuration required")
    return out


def redact_sensitive(value: CreateMemberInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member_configuration" in value:
        import capo_managedblockchain.types.member_configuration

        out["member_configuration"] = (
            capo_managedblockchain.types.member_configuration.redact_sensitive(
                value["member_configuration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#CreateParticipantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.participant_details_to_add


class CreateParticipantRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. </p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. Supports contacts in the CHAT channel and VOICE (WebRTC) channels. For WebRTC calls, this should be the initial contact ID that was generated when the contact was first created (from the StartWebRTCContact API) in the VOICE channel</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    participant_details: (
        "capo_connect.types.participant_details_to_add.ParticipantDetailsToAdd"
    )
    """<p>Information identifying the participant.</p> <important> <p>The only valid value for <code>ParticipantRole</code> is <code>CUSTOM_BOT</code> for chat contact and <code>CUSTOMER</code> for voice contact.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import capo_connect.types.participant_details_to_add

    out["ParticipantDetails"] = (
        capo_connect.types.participant_details_to_add.serialize_json(
            value["participant_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateParticipantRequest:
    out: CreateParticipantRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("CreateParticipantRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("CreateParticipantRequest.contact_id required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ParticipantDetails") is not None:
        import capo_connect.types.participant_details_to_add

        out["participant_details"] = (
            capo_connect.types.participant_details_to_add.deserialize_json(
                data["ParticipantDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateParticipantRequest.participant_details required"
        )
    return out

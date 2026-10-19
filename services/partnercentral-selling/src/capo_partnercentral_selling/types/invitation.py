"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Invitation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.invitation_message
    import capo_partnercentral_selling.types.payload
    import capo_partnercentral_selling.types.receiver


class Invitation(TypedDict, closed=True):
    message: "capo_partnercentral_selling.types.invitation_message.InvitationMessage"
    """<p> A message accompanying the invitation. </p>"""
    receiver: "capo_partnercentral_selling.types.receiver.Receiver"
    payload: "capo_partnercentral_selling.types.payload.Payload"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Invitation) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_selling.types.receiver

    out["Receiver"] = capo_partnercentral_selling.types.receiver.serialize_aws_json_1_0(
        value["receiver"]
    )
    import capo_partnercentral_selling.types.payload

    out["Payload"] = capo_partnercentral_selling.types.payload.serialize_aws_json_1_0(
        value["payload"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Invitation:
    out: Invitation = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Receiver") is not None:
        import capo_partnercentral_selling.types.receiver

        out["receiver"] = (
            capo_partnercentral_selling.types.receiver.deserialize_aws_json_1_0(
                data["Receiver"]
            )
        )
    else:
        import capo_partnercentral_selling.types._unknown

        out["receiver"] = capo_partnercentral_selling.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("Payload") is not None:
        import capo_partnercentral_selling.types.payload

        out["payload"] = (
            capo_partnercentral_selling.types.payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    else:
        import capo_partnercentral_selling.types._unknown

        out["payload"] = capo_partnercentral_selling.types._unknown.UnknownUnionMember(
            ""
        )
    return out


def redact_sensitive(value: Invitation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    if "receiver" in value:
        import capo_partnercentral_selling.types.receiver

        out["receiver"] = capo_partnercentral_selling.types.receiver.redact_sensitive(
            value["receiver"]
        )
    if "payload" in value:
        import capo_partnercentral_selling.types.payload

        out["payload"] = capo_partnercentral_selling.types.payload.redact_sensitive(
            value["payload"]
        )
    return out

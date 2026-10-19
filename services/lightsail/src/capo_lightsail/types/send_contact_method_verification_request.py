"""Generated from Smithy shape ``com.amazonaws.lightsail#SendContactMethodVerificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.contact_method_verification_protocol


class SendContactMethodVerificationRequest(TypedDict, closed=True):
    protocol: "capo_lightsail.types.contact_method_verification_protocol.ContactMethodVerificationProtocol"
    """<p>The protocol to verify, such as <code>Email</code> or <code>SMS</code> (text messaging).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendContactMethodVerificationRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.contact_method_verification_protocol

    out["protocol"] = (
        capo_lightsail.types.contact_method_verification_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendContactMethodVerificationRequest:
    out: SendContactMethodVerificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("protocol") is not None:
        import capo_lightsail.types.contact_method_verification_protocol

        out["protocol"] = (
            capo_lightsail.types.contact_method_verification_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_lightsail.types.contact_method_verification_protocol.ContactMethodVerificationProtocol",
            "",
        )
    return out

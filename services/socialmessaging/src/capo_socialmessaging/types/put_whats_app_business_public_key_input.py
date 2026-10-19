"""Generated from Smithy shape ``com.amazonaws.socialmessaging#PutWhatsAppBusinessPublicKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.business_public_key_pem
    import capo_socialmessaging.types.kms_key_arn
    import capo_socialmessaging.types.whats_app_phone_number_id


class PutWhatsAppBusinessPublicKeyInput(TypedDict, closed=True):
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The unique identifier of the phone number to associate with the business public key.</p>"""
    business_public_key: NotRequired[
        "capo_socialmessaging.types.business_public_key_pem.BusinessPublicKeyPem"
    ]
    """<p>The PEM-encoded 2048-bit RSA public key to set. Mutually exclusive with <code>kmsKeyArn</code>.</p>"""
    kms_key_arn: NotRequired["capo_socialmessaging.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of a customer managed asymmetric RSA key in Amazon Web Services KMS. Mutually exclusive with <code>businessPublicKey</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutWhatsAppBusinessPublicKeyInput) -> dict:
    out: dict = {}
    out["originationPhoneNumberId"] = value["origination_phone_number_id"]
    if "business_public_key" in value:
        out["businessPublicKey"] = value["business_public_key"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> PutWhatsAppBusinessPublicKeyInput:
    out: PutWhatsAppBusinessPublicKeyInput = {}  # type: ignore[typeddict-item]
    if data.get("originationPhoneNumberId") is not None:
        out["origination_phone_number_id"] = data["originationPhoneNumberId"]
    else:
        out["origination_phone_number_id"] = ""
    if data.get("businessPublicKey") is not None:
        out["business_public_key"] = data["businessPublicKey"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out

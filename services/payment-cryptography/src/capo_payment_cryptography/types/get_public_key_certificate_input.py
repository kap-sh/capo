"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetPublicKeyCertificateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_arn_or_key_alias_type


class GetPublicKeyCertificateInput(TypedDict, closed=True):
    key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>KeyARN</code> of the asymmetric key pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPublicKeyCertificateInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPublicKeyCertificateInput:
    out: GetPublicKeyCertificateInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        out["key_identifier"] = ""
    return out

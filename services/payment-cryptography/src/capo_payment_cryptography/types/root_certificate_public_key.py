"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#RootCertificatePublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_type
    import capo_payment_cryptography.types.key_attributes


class RootCertificatePublicKey(TypedDict, closed=True):
    key_attributes: "capo_payment_cryptography.types.key_attributes.KeyAttributes"
    """<p>The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the root public key is imported.</p>"""
    public_key_certificate: (
        "capo_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>Parameter information for root public key certificate import.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RootCertificatePublicKey) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.key_attributes

    out["KeyAttributes"] = (
        capo_payment_cryptography.types.key_attributes.serialize_aws_json_1_0(
            value["key_attributes"]
        )
    )
    out["PublicKeyCertificate"] = value["public_key_certificate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RootCertificatePublicKey:
    out: RootCertificatePublicKey = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_payment_cryptography.types.key_attributes

        out["key_attributes"] = (
            capo_payment_cryptography.types.key_attributes.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("RootCertificatePublicKey.key_attributes required")
    if data.get("PublicKeyCertificate") is not None:
        out["public_key_certificate"] = data["PublicKeyCertificate"]
    else:
        out["public_key_certificate"] = ""
    return out

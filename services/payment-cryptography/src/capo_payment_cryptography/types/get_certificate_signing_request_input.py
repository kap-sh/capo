"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetCertificateSigningRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.certificate_subject_type
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.signing_algorithm_type


class GetCertificateSigningRequestInput(TypedDict, closed=True):
    key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>Asymmetric key used for generating the certificate signing request</p>"""
    signing_algorithm: (
        "capo_payment_cryptography.types.signing_algorithm_type.SigningAlgorithmType"
    )
    """<p>The cryptographic algorithm used to sign your CSR.</p>"""
    certificate_subject: "capo_payment_cryptography.types.certificate_subject_type.CertificateSubjectType"
    """<p>The metadata used to create the CSR.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCertificateSigningRequestInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["SigningAlgorithm"] = value["signing_algorithm"]
    import capo_payment_cryptography.types.certificate_subject_type

    out["CertificateSubject"] = (
        capo_payment_cryptography.types.certificate_subject_type.serialize_aws_json_1_0(
            value["certificate_subject"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCertificateSigningRequestInput:
    out: GetCertificateSigningRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        out["key_identifier"] = ""
    if data.get("SigningAlgorithm") is not None:
        out["signing_algorithm"] = data["SigningAlgorithm"]
    else:
        out["signing_algorithm"] = ""
    if data.get("CertificateSubject") is not None:
        import capo_payment_cryptography.types.certificate_subject_type

        out["certificate_subject"] = (
            capo_payment_cryptography.types.certificate_subject_type.deserialize_aws_json_1_0(
                data["CertificateSubject"]
            )
        )
    else:
        raise DeserializationError(
            "GetCertificateSigningRequestInput.certificate_subject required"
        )
    return out

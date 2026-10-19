"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.asn1_subject
    import capo_acm_pca.types.csr_extensions
    import capo_acm_pca.types.key_algorithm
    import capo_acm_pca.types.signing_algorithm


class CertificateAuthorityConfiguration(TypedDict, closed=True):
    key_algorithm: "capo_acm_pca.types.key_algorithm.KeyAlgorithm"
    """<p>Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.</p>"""
    signing_algorithm: "capo_acm_pca.types.signing_algorithm.SigningAlgorithm"
    """<p>Name of the algorithm your private CA uses to sign certificate requests.</p> <p>This parameter should not be confused with the <code>SigningAlgorithm</code> parameter of the <code>IssueCertificate</code> API action, which is used to sign certificates when they are issued.</p>"""
    subject: "capo_acm_pca.types.asn1_subject.ASN1Subject"
    """<p>Structure that contains X.500 distinguished name information for your private CA.</p>"""
    csr_extensions: NotRequired["capo_acm_pca.types.csr_extensions.CsrExtensions"]
    """<p>Specifies information to be added to the extension section of the certificate signing request (CSR).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthorityConfiguration) -> dict:
    out: dict = {}
    import capo_acm_pca.types.key_algorithm

    out["KeyAlgorithm"] = capo_acm_pca.types.key_algorithm.serialize_aws_json_1_1(
        value["key_algorithm"]
    )
    import capo_acm_pca.types.signing_algorithm

    out["SigningAlgorithm"] = (
        capo_acm_pca.types.signing_algorithm.serialize_aws_json_1_1(
            value["signing_algorithm"]
        )
    )
    import capo_acm_pca.types.asn1_subject

    out["Subject"] = capo_acm_pca.types.asn1_subject.serialize_aws_json_1_1(
        value["subject"]
    )
    if "csr_extensions" in value:
        import capo_acm_pca.types.csr_extensions

        out["CsrExtensions"] = capo_acm_pca.types.csr_extensions.serialize_aws_json_1_1(
            value["csr_extensions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateAuthorityConfiguration:
    out: CertificateAuthorityConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KeyAlgorithm") is not None:
        import capo_acm_pca.types.key_algorithm

        out["key_algorithm"] = (
            capo_acm_pca.types.key_algorithm.deserialize_aws_json_1_1(
                data["KeyAlgorithm"]
            )
        )
    else:
        import typing

        out["key_algorithm"] = typing.cast(
            "capo_acm_pca.types.key_algorithm.KeyAlgorithm", ""
        )
    if data.get("SigningAlgorithm") is not None:
        import capo_acm_pca.types.signing_algorithm

        out["signing_algorithm"] = (
            capo_acm_pca.types.signing_algorithm.deserialize_aws_json_1_1(
                data["SigningAlgorithm"]
            )
        )
    else:
        import typing

        out["signing_algorithm"] = typing.cast(
            "capo_acm_pca.types.signing_algorithm.SigningAlgorithm", ""
        )
    if data.get("Subject") is not None:
        import capo_acm_pca.types.asn1_subject

        out["subject"] = capo_acm_pca.types.asn1_subject.deserialize_aws_json_1_1(
            data["Subject"]
        )
    else:
        raise DeserializationError("CertificateAuthorityConfiguration.subject required")
    if data.get("CsrExtensions") is not None:
        import capo_acm_pca.types.csr_extensions

        out["csr_extensions"] = (
            capo_acm_pca.types.csr_extensions.deserialize_aws_json_1_1(
                data["CsrExtensions"]
            )
        )
    return out

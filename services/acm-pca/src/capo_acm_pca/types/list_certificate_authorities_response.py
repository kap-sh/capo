"""Generated from Smithy shape ``com.amazonaws.acmpca#ListCertificateAuthoritiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.certificate_authorities
    import capo_acm_pca.types.next_token


class ListCertificateAuthoritiesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_acm_pca.types.next_token.NextToken"]
    """<p>When the list is truncated, this value is present and should be used for the <code>NextToken</code> parameter in a subsequent pagination request.</p>"""
    certificate_authorities: NotRequired[
        "capo_acm_pca.types.certificate_authorities.CertificateAuthorities"
    ]
    """<p>Summary information about each certificate authority you have created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificateAuthoritiesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "certificate_authorities" in value:
        import capo_acm_pca.types.certificate_authorities

        out["CertificateAuthorities"] = (
            capo_acm_pca.types.certificate_authorities.serialize_aws_json_1_1(
                value["certificate_authorities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificateAuthoritiesResponse:
    out: ListCertificateAuthoritiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("CertificateAuthorities") is not None:
        import capo_acm_pca.types.certificate_authorities

        out["certificate_authorities"] = (
            capo_acm_pca.types.certificate_authorities.deserialize_aws_json_1_1(
                data["CertificateAuthorities"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCertificateAuthoritiesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "certificate_authorities" in value:
        import capo_acm_pca.types.certificate_authorities

        out["CertificateAuthorities"] = (
            capo_acm_pca.types.certificate_authorities.serialize_cbor(
                value["certificate_authorities"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListCertificateAuthoritiesResponse:
    out: ListCertificateAuthoritiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("CertificateAuthorities") is not None:
        import capo_acm_pca.types.certificate_authorities

        out["certificate_authorities"] = (
            capo_acm_pca.types.certificate_authorities.deserialize_cbor(
                data["CertificateAuthorities"]
            )
        )
    return out

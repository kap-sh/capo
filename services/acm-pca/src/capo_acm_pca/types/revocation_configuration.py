"""Generated from Smithy shape ``com.amazonaws.acmpca#RevocationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.crl_configuration
    import capo_acm_pca.types.ocsp_configuration


class RevocationConfiguration(TypedDict, closed=True):
    crl_configuration: NotRequired[
        "capo_acm_pca.types.crl_configuration.CrlConfiguration"
    ]
    """<p>Configuration of the certificate revocation list (CRL), if any, maintained by your private CA. A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason a CRL update fails, Amazon Web Services Private CA makes further attempts every 15 minutes.</p>"""
    ocsp_configuration: NotRequired[
        "capo_acm_pca.types.ocsp_configuration.OcspConfiguration"
    ]
    """<p>Configuration of Online Certificate Status Protocol (OCSP) support, if any, maintained by your private CA. When you revoke a certificate, OCSP responses may take up to 60 minutes to reflect the new status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevocationConfiguration) -> dict:
    out: dict = {}
    if "crl_configuration" in value:
        import capo_acm_pca.types.crl_configuration

        out["CrlConfiguration"] = (
            capo_acm_pca.types.crl_configuration.serialize_aws_json_1_1(
                value["crl_configuration"]
            )
        )
    if "ocsp_configuration" in value:
        import capo_acm_pca.types.ocsp_configuration

        out["OcspConfiguration"] = (
            capo_acm_pca.types.ocsp_configuration.serialize_aws_json_1_1(
                value["ocsp_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevocationConfiguration:
    out: RevocationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CrlConfiguration") is not None:
        import capo_acm_pca.types.crl_configuration

        out["crl_configuration"] = (
            capo_acm_pca.types.crl_configuration.deserialize_aws_json_1_1(
                data["CrlConfiguration"]
            )
        )
    if data.get("OcspConfiguration") is not None:
        import capo_acm_pca.types.ocsp_configuration

        out["ocsp_configuration"] = (
            capo_acm_pca.types.ocsp_configuration.deserialize_aws_json_1_1(
                data["OcspConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevocationConfiguration) -> dict:
    out: dict = {}
    if "crl_configuration" in value:
        import capo_acm_pca.types.crl_configuration

        out["CrlConfiguration"] = capo_acm_pca.types.crl_configuration.serialize_cbor(
            value["crl_configuration"]
        )
    if "ocsp_configuration" in value:
        import capo_acm_pca.types.ocsp_configuration

        out["OcspConfiguration"] = capo_acm_pca.types.ocsp_configuration.serialize_cbor(
            value["ocsp_configuration"]
        )
    return out


def deserialize_cbor(data: dict) -> RevocationConfiguration:
    out: RevocationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CrlConfiguration") is not None:
        import capo_acm_pca.types.crl_configuration

        out["crl_configuration"] = (
            capo_acm_pca.types.crl_configuration.deserialize_cbor(
                data["CrlConfiguration"]
            )
        )
    if data.get("OcspConfiguration") is not None:
        import capo_acm_pca.types.ocsp_configuration

        out["ocsp_configuration"] = (
            capo_acm_pca.types.ocsp_configuration.deserialize_cbor(
                data["OcspConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TlsInterceptProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.tls_intercept_mode


class TlsInterceptProperties(TypedDict, closed=True):
    pca_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>Private Certificate Authority (PCA) used to issue private TLS certificates so that the proxy can present PCA-signed certificates which applications trust through the same root, establishing a secure and consistent trust model for encrypted communication.</p>"""
    tls_intercept_mode: NotRequired[
        "capo_network_firewall.types.tls_intercept_mode.TlsInterceptMode"
    ]
    """<p>Specifies whether to enable or disable TLS Intercept Mode. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TlsInterceptProperties) -> dict:
    out: dict = {}
    if "pca_arn" in value:
        out["PcaArn"] = value["pca_arn"]
    if "tls_intercept_mode" in value:
        import capo_network_firewall.types.tls_intercept_mode

        out["TlsInterceptMode"] = (
            capo_network_firewall.types.tls_intercept_mode.serialize_aws_json_1_0(
                value["tls_intercept_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TlsInterceptProperties:
    out: TlsInterceptProperties = {}  # type: ignore[typeddict-item]
    if data.get("PcaArn") is not None:
        out["pca_arn"] = data["PcaArn"]
    if data.get("TlsInterceptMode") is not None:
        import capo_network_firewall.types.tls_intercept_mode

        out["tls_intercept_mode"] = (
            capo_network_firewall.types.tls_intercept_mode.deserialize_aws_json_1_0(
                data["TlsInterceptMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TlsInterceptProperties) -> dict:
    out: dict = {}
    if "pca_arn" in value:
        out["PcaArn"] = value["pca_arn"]
    if "tls_intercept_mode" in value:
        import capo_network_firewall.types.tls_intercept_mode

        out["TlsInterceptMode"] = (
            capo_network_firewall.types.tls_intercept_mode.serialize_cbor(
                value["tls_intercept_mode"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TlsInterceptProperties:
    out: TlsInterceptProperties = {}  # type: ignore[typeddict-item]
    if data.get("PcaArn") is not None:
        out["pca_arn"] = data["PcaArn"]
    if data.get("TlsInterceptMode") is not None:
        import capo_network_firewall.types.tls_intercept_mode

        out["tls_intercept_mode"] = (
            capo_network_firewall.types.tls_intercept_mode.deserialize_cbor(
                data["TlsInterceptMode"]
            )
        )
    return out

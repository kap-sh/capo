"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Certificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.tls_certificate_data

Certificates: TypeAlias = list[
    "capo_network_firewall.types.tls_certificate_data.TlsCertificateData"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Certificates) -> list:
    import capo_network_firewall.types.tls_certificate_data

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.tls_certificate_data.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Certificates:
    import capo_network_firewall.types.tls_certificate_data

    out: Certificates = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.tls_certificate_data.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Certificates) -> list:
    import capo_network_firewall.types.tls_certificate_data

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.tls_certificate_data.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> Certificates:
    import capo_network_firewall.types.tls_certificate_data

    out: Certificates = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.tls_certificate_data.deserialize_cbor(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ServerCertificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.server_certificate

ServerCertificates: TypeAlias = list[
    "capo_network_firewall.types.server_certificate.ServerCertificate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerCertificates) -> list:
    import capo_network_firewall.types.server_certificate

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.server_certificate.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServerCertificates:
    import capo_network_firewall.types.server_certificate

    out: ServerCertificates = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.server_certificate.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServerCertificates) -> list:
    import capo_network_firewall.types.server_certificate

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.server_certificate.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ServerCertificates:
    import capo_network_firewall.types.server_certificate

    out: ServerCertificates = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.server_certificate.deserialize_cbor(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ServerCertificateConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.server_certificate_configuration

ServerCertificateConfigurations: TypeAlias = list[
    "capo_network_firewall.types.server_certificate_configuration.ServerCertificateConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerCertificateConfigurations) -> list:
    import capo_network_firewall.types.server_certificate_configuration

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.server_certificate_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServerCertificateConfigurations:
    import capo_network_firewall.types.server_certificate_configuration

    out: ServerCertificateConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.server_certificate_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServerCertificateConfigurations) -> list:
    import capo_network_firewall.types.server_certificate_configuration

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.server_certificate_configuration.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ServerCertificateConfigurations:
    import capo_network_firewall.types.server_certificate_configuration

    out: ServerCertificateConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.server_certificate_configuration.deserialize_cbor(
                item
            )
        )
    return out

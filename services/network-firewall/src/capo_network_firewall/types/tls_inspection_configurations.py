"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TLSInspectionConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.tls_inspection_configuration_metadata

TLSInspectionConfigurations: TypeAlias = list[
    "capo_network_firewall.types.tls_inspection_configuration_metadata.TLSInspectionConfigurationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TLSInspectionConfigurations) -> list:
    import capo_network_firewall.types.tls_inspection_configuration_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.tls_inspection_configuration_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TLSInspectionConfigurations:
    import capo_network_firewall.types.tls_inspection_configuration_metadata

    out: TLSInspectionConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.tls_inspection_configuration_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TLSInspectionConfigurations) -> list:
    import capo_network_firewall.types.tls_inspection_configuration_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.tls_inspection_configuration_metadata.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> TLSInspectionConfigurations:
    import capo_network_firewall.types.tls_inspection_configuration_metadata

    out: TLSInspectionConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.tls_inspection_configuration_metadata.deserialize_cbor(
                item
            )
        )
    return out

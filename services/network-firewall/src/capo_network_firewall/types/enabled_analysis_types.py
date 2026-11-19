"""Generated from Smithy shape ``com.amazonaws.networkfirewall#EnabledAnalysisTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.enabled_analysis_type

EnabledAnalysisTypes: TypeAlias = list[
    "capo_network_firewall.types.enabled_analysis_type.EnabledAnalysisType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnabledAnalysisTypes) -> list:
    import capo_network_firewall.types.enabled_analysis_type

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.enabled_analysis_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EnabledAnalysisTypes:
    import capo_network_firewall.types.enabled_analysis_type

    out: EnabledAnalysisTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.enabled_analysis_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnabledAnalysisTypes) -> list:
    import capo_network_firewall.types.enabled_analysis_type

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.enabled_analysis_type.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> EnabledAnalysisTypes:
    import capo_network_firewall.types.enabled_analysis_type

    out: EnabledAnalysisTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.enabled_analysis_type.deserialize_cbor(item)
        )
    return out

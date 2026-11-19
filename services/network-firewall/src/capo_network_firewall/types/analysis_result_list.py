"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AnalysisResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_result

AnalysisResultList: TypeAlias = list[
    "capo_network_firewall.types.analysis_result.AnalysisResult"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalysisResultList) -> list:
    import capo_network_firewall.types.analysis_result

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.analysis_result.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AnalysisResultList:
    import capo_network_firewall.types.analysis_result

    out: AnalysisResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.analysis_result.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalysisResultList) -> list:
    import capo_network_firewall.types.analysis_result

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.analysis_result.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AnalysisResultList:
    import capo_network_firewall.types.analysis_result

    out: AnalysisResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.analysis_result.deserialize_cbor(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AnalysisReports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_report

AnalysisReports: TypeAlias = list[
    "capo_network_firewall.types.analysis_report.AnalysisReport"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalysisReports) -> list:
    import capo_network_firewall.types.analysis_report

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.analysis_report.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AnalysisReports:
    import capo_network_firewall.types.analysis_report

    out: AnalysisReports = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.analysis_report.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalysisReports) -> list:
    import capo_network_firewall.types.analysis_report

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.analysis_report.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AnalysisReports:
    import capo_network_firewall.types.analysis_report

    out: AnalysisReports = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.analysis_report.deserialize_cbor(item))
    return out

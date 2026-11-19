"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.export_summary

ExportSummaryList: TypeAlias = list[
    "capo_mailmanager.types.export_summary.ExportSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportSummaryList) -> list:
    import capo_mailmanager.types.export_summary

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.export_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ExportSummaryList:
    import capo_mailmanager.types.export_summary

    out: ExportSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.export_summary.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportSummaryList) -> list:
    import capo_mailmanager.types.export_summary

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.export_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExportSummaryList:
    import capo_mailmanager.types.export_summary

    out: ExportSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.export_summary.deserialize_cbor(item))
    return out

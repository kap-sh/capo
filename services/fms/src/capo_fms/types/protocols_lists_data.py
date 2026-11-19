"""Generated from Smithy shape ``com.amazonaws.fms#ProtocolsListsData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.protocols_list_data_summary

ProtocolsListsData: TypeAlias = list[
    "capo_fms.types.protocols_list_data_summary.ProtocolsListDataSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolsListsData) -> list:
    import capo_fms.types.protocols_list_data_summary

    out: list = []
    for item in value:
        out.append(
            capo_fms.types.protocols_list_data_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtocolsListsData:
    import capo_fms.types.protocols_list_data_summary

    out: ProtocolsListsData = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_fms.types.protocols_list_data_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtocolsListsData) -> list:
    import capo_fms.types.protocols_list_data_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.protocols_list_data_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProtocolsListsData:
    import capo_fms.types.protocols_list_data_summary

    out: ProtocolsListsData = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.protocols_list_data_summary.deserialize_cbor(item))
    return out

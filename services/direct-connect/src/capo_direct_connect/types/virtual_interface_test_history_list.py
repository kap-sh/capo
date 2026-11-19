"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterfaceTestHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.virtual_interface_test_history

VirtualInterfaceTestHistoryList: TypeAlias = list[
    "capo_direct_connect.types.virtual_interface_test_history.VirtualInterfaceTestHistory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterfaceTestHistoryList) -> list:
    import capo_direct_connect.types.virtual_interface_test_history

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.virtual_interface_test_history.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VirtualInterfaceTestHistoryList:
    import capo_direct_connect.types.virtual_interface_test_history

    out: VirtualInterfaceTestHistoryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.virtual_interface_test_history.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VirtualInterfaceTestHistoryList) -> list:
    import capo_direct_connect.types.virtual_interface_test_history

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.virtual_interface_test_history.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> VirtualInterfaceTestHistoryList:
    import capo_direct_connect.types.virtual_interface_test_history

    out: VirtualInterfaceTestHistoryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.virtual_interface_test_history.deserialize_cbor(
                item
            )
        )
    return out

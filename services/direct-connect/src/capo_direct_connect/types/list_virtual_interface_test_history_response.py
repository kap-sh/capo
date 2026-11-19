"""Generated from Smithy shape ``com.amazonaws.directconnect#ListVirtualInterfaceTestHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.virtual_interface_test_history_list


class ListVirtualInterfaceTestHistoryResponse(TypedDict, closed=True):
    virtual_interface_test_history: NotRequired[
        "capo_direct_connect.types.virtual_interface_test_history_list.VirtualInterfaceTestHistoryList"
    ]
    """<p>The ID of the tested virtual interface.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVirtualInterfaceTestHistoryResponse) -> dict:
    out: dict = {}
    if "virtual_interface_test_history" in value:
        import capo_direct_connect.types.virtual_interface_test_history_list

        out["virtualInterfaceTestHistory"] = (
            capo_direct_connect.types.virtual_interface_test_history_list.serialize_aws_json_1_1(
                value["virtual_interface_test_history"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVirtualInterfaceTestHistoryResponse:
    out: ListVirtualInterfaceTestHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceTestHistory") is not None:
        import capo_direct_connect.types.virtual_interface_test_history_list

        out["virtual_interface_test_history"] = (
            capo_direct_connect.types.virtual_interface_test_history_list.deserialize_aws_json_1_1(
                data["virtualInterfaceTestHistory"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVirtualInterfaceTestHistoryResponse) -> dict:
    out: dict = {}
    if "virtual_interface_test_history" in value:
        import capo_direct_connect.types.virtual_interface_test_history_list

        out["virtualInterfaceTestHistory"] = (
            capo_direct_connect.types.virtual_interface_test_history_list.serialize_cbor(
                value["virtual_interface_test_history"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListVirtualInterfaceTestHistoryResponse:
    out: ListVirtualInterfaceTestHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceTestHistory") is not None:
        import capo_direct_connect.types.virtual_interface_test_history_list

        out["virtual_interface_test_history"] = (
            capo_direct_connect.types.virtual_interface_test_history_list.deserialize_cbor(
                data["virtualInterfaceTestHistory"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

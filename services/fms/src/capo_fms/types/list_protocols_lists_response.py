"""Generated from Smithy shape ``com.amazonaws.fms#ListProtocolsListsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.pagination_token
    import capo_fms.types.protocols_lists_data


class ListProtocolsListsResponse(TypedDict, closed=True):
    protocols_lists: NotRequired[
        "capo_fms.types.protocols_lists_data.ProtocolsListsData"
    ]
    """<p>An array of <code>ProtocolsListDataSummary</code> objects.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If you specify a value for <code>MaxResults</code> in your list request, and you have more objects than the maximum, Firewall Manager returns this token in the response. You can use this token in subsequent requests to retrieve the next batch of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProtocolsListsResponse) -> dict:
    out: dict = {}
    if "protocols_lists" in value:
        import capo_fms.types.protocols_lists_data

        out["ProtocolsLists"] = (
            capo_fms.types.protocols_lists_data.serialize_aws_json_1_1(
                value["protocols_lists"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProtocolsListsResponse:
    out: ListProtocolsListsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProtocolsLists") is not None:
        import capo_fms.types.protocols_lists_data

        out["protocols_lists"] = (
            capo_fms.types.protocols_lists_data.deserialize_aws_json_1_1(
                data["ProtocolsLists"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProtocolsListsResponse) -> dict:
    out: dict = {}
    if "protocols_lists" in value:
        import capo_fms.types.protocols_lists_data

        out["ProtocolsLists"] = capo_fms.types.protocols_lists_data.serialize_cbor(
            value["protocols_lists"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListProtocolsListsResponse:
    out: ListProtocolsListsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProtocolsLists") is not None:
        import capo_fms.types.protocols_lists_data

        out["protocols_lists"] = capo_fms.types.protocols_lists_data.deserialize_cbor(
            data["ProtocolsLists"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

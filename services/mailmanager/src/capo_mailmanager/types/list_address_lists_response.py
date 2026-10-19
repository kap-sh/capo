"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListAddressListsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.address_lists
    import capo_mailmanager.types.pagination_token


class ListAddressListsResponse(TypedDict, closed=True):
    address_lists: "capo_mailmanager.types.address_lists.AddressLists"
    """<p>The list of address lists.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAddressListsResponse) -> dict:
    out: dict = {}
    import capo_mailmanager.types.address_lists

    out["AddressLists"] = capo_mailmanager.types.address_lists.serialize_aws_json_1_0(
        value["address_lists"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAddressListsResponse:
    out: ListAddressListsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddressLists") is not None:
        import capo_mailmanager.types.address_lists

        out["address_lists"] = (
            capo_mailmanager.types.address_lists.deserialize_aws_json_1_0(
                data["AddressLists"]
            )
        )
    else:
        out["address_lists"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

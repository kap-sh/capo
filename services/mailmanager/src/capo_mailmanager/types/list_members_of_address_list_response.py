"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListMembersOfAddressListResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.saved_addresses


class ListMembersOfAddressListResponse(TypedDict, closed=True):
    addresses: "capo_mailmanager.types.saved_addresses.SavedAddresses"
    """<p>The list of addresses.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMembersOfAddressListResponse) -> dict:
    out: dict = {}
    import capo_mailmanager.types.saved_addresses

    out["Addresses"] = capo_mailmanager.types.saved_addresses.serialize_aws_json_1_0(
        value["addresses"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMembersOfAddressListResponse:
    out: ListMembersOfAddressListResponse = {}  # type: ignore[typeddict-item]
    if data.get("Addresses") is not None:
        import capo_mailmanager.types.saved_addresses

        out["addresses"] = (
            capo_mailmanager.types.saved_addresses.deserialize_aws_json_1_0(
                data["Addresses"]
            )
        )
    else:
        raise DeserializationError(
            "ListMembersOfAddressListResponse.addresses required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListMembersOfAddressListResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "addresses" in value:
        import capo_mailmanager.types.saved_addresses

        out["addresses"] = capo_mailmanager.types.saved_addresses.redact_sensitive(
            value["addresses"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeregisterMemberFromAddressListRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.address
    import capo_mailmanager.types.address_list_id


class DeregisterMemberFromAddressListRequest(TypedDict, closed=True):
    address_list_id: "capo_mailmanager.types.address_list_id.AddressListId"
    """<p>The unique identifier of the address list to remove the address from.</p>"""
    address: "capo_mailmanager.types.address.Address"
    """<p>The address to be removed from the address list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeregisterMemberFromAddressListRequest) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    out["Address"] = value["address"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeregisterMemberFromAddressListRequest:
    out: DeregisterMemberFromAddressListRequest = {}  # type: ignore[typeddict-item]
    if data.get("AddressListId") is not None:
        out["address_list_id"] = data["AddressListId"]
    else:
        out["address_list_id"] = ""
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    else:
        out["address"] = ""
    return out


def redact_sensitive(value: DeregisterMemberFromAddressListRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "address" in value:
        out["address"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteAddressOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.address
    import capo_outposts.types.address_type


class UpdateSiteAddressOutput(TypedDict, closed=True):
    address_type: NotRequired["capo_outposts.types.address_type.AddressType"]
    """<p> The type of the address. </p>"""
    address: NotRequired["capo_outposts.types.address.Address"]
    """<p> Information about an address. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteAddressOutput) -> dict:
    out: dict = {}
    if "address_type" in value:
        import capo_outposts.types.address_type

        out["AddressType"] = capo_outposts.types.address_type.serialize_json(
            value["address_type"]
        )
    if "address" in value:
        import capo_outposts.types.address

        out["Address"] = capo_outposts.types.address.serialize_json(value["address"])
    return out


def deserialize_json(data: dict) -> UpdateSiteAddressOutput:
    out: UpdateSiteAddressOutput = {}  # type: ignore[typeddict-item]
    if data.get("AddressType") is not None:
        import capo_outposts.types.address_type

        out["address_type"] = capo_outposts.types.address_type.deserialize_json(
            data["AddressType"]
        )
    if data.get("Address") is not None:
        import capo_outposts.types.address

        out["address"] = capo_outposts.types.address.deserialize_json(data["Address"])
    return out


def redact_sensitive(value: UpdateSiteAddressOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "address" in value:
        out["address"] = "*** Sensitive Data Redacted ***"
    return out

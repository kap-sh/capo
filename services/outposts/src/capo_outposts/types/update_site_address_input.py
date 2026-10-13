"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteAddressInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_outposts.types.address
    import capo_outposts.types.address_type
    import capo_outposts.types.site_id


class UpdateSiteAddressInput(TypedDict, closed=True):
    site_id: "capo_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""
    address_type: "capo_outposts.types.address_type.AddressType"
    """<p> The type of the address. </p>"""
    address: "capo_outposts.types.address.Address"
    """<p> The address for the site. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteAddressInput) -> dict:
    out: dict = {}
    import capo_outposts.types.address_type

    out["AddressType"] = capo_outposts.types.address_type.serialize_json(
        value["address_type"]
    )
    import capo_outposts.types.address

    out["Address"] = capo_outposts.types.address.serialize_json(value["address"])
    return out


def deserialize_json(data: dict) -> UpdateSiteAddressInput:
    out: UpdateSiteAddressInput = {}  # type: ignore[typeddict-item]
    if data.get("AddressType") is not None:
        import capo_outposts.types.address_type

        out["address_type"] = capo_outposts.types.address_type.deserialize_json(
            data["AddressType"]
        )
    else:
        raise DeserializationError("UpdateSiteAddressInput.address_type required")
    if data.get("Address") is not None:
        import capo_outposts.types.address

        out["address"] = capo_outposts.types.address.deserialize_json(data["Address"])
    else:
        raise DeserializationError("UpdateSiteAddressInput.address required")
    return out


def redact_sensitive(value: UpdateSiteAddressInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "address" in value:
        out["address"] = "*** Sensitive Data Redacted ***"
    return out

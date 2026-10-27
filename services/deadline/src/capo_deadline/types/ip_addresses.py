"""Generated from Smithy shape ``com.amazonaws.deadline#IpAddresses``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.ip_v4_addresses
    import capo_deadline.types.ip_v6_addresses


class IpAddresses(TypedDict, closed=True):
    ip_v4_addresses: NotRequired["capo_deadline.types.ip_v4_addresses.IpV4Addresses"]
    """The IpV4 address of the network."""
    ip_v6_addresses: NotRequired["capo_deadline.types.ip_v6_addresses.IpV6Addresses"]
    """The IpV6 address for the network and node component."""


# --- restJson1 ser/de ---
def serialize_json(value: IpAddresses) -> dict:
    out: dict = {}
    if "ip_v4_addresses" in value:
        import capo_deadline.types.ip_v4_addresses

        out["ipV4Addresses"] = capo_deadline.types.ip_v4_addresses.serialize_json(
            value["ip_v4_addresses"]
        )
    if "ip_v6_addresses" in value:
        import capo_deadline.types.ip_v6_addresses

        out["ipV6Addresses"] = capo_deadline.types.ip_v6_addresses.serialize_json(
            value["ip_v6_addresses"]
        )
    return out


def deserialize_json(data: dict) -> IpAddresses:
    out: IpAddresses = {}  # type: ignore[typeddict-item]
    if data.get("ipV4Addresses") is not None:
        import capo_deadline.types.ip_v4_addresses

        out["ip_v4_addresses"] = capo_deadline.types.ip_v4_addresses.deserialize_json(
            data["ipV4Addresses"]
        )
    if data.get("ipV6Addresses") is not None:
        import capo_deadline.types.ip_v6_addresses

        out["ip_v6_addresses"] = capo_deadline.types.ip_v6_addresses.deserialize_json(
            data["ipV6Addresses"]
        )
    return out

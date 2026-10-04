"""Generated from Smithy shape ``com.amazonaws.ec2#IpamInternetRegistryAssociationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The state of an IPAM internet registry association.</p>"""
IpamInternetRegistryAssociationState: TypeAlias = Literal[
    "pending-enable",
    "create-in-progress",
    "create-failed",
    "enable-in-progress",
    "enable-complete",
    "enable-failed",
    "disable-in-progress",
    "disable-complete",
    "disable-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamInternetRegistryAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamInternetRegistryAssociationState:
    return cast(IpamInternetRegistryAssociationState, text)


def serialize_ec2_query(
    value: IpamInternetRegistryAssociationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamInternetRegistryAssociationState:
    return from_ec2_query_text(el.text or "")

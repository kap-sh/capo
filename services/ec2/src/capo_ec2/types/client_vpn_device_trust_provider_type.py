"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnDeviceTrustProviderType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ClientVpnDeviceTrustProviderType: TypeAlias = Literal[
    "crowdstrike",
    "jamf",
    "jumpcloud",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ClientVpnDeviceTrustProviderType) -> str:
    return value


def from_ec2_query_text(text: str) -> ClientVpnDeviceTrustProviderType:
    return cast(ClientVpnDeviceTrustProviderType, text)


def serialize_ec2_query(
    value: ClientVpnDeviceTrustProviderType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ClientVpnDeviceTrustProviderType:
    return from_ec2_query_text(el.text or "")

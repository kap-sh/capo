"""Generated from Smithy shape ``com.amazonaws.ec2#PermissionType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

PermissionType: TypeAlias = Literal[
    "vpc-endpoint",
    "transit-gateway-attachment",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PermissionType) -> str:
    return value


def from_ec2_query_text(text: str) -> PermissionType:
    return cast(PermissionType, text)


def serialize_ec2_query(
    value: PermissionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PermissionType:
    return from_ec2_query_text(el.text or "")

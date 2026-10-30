"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityUnit``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityUnit: TypeAlias = Literal[
    "vcpus",
    "instances",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityUnit) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityUnit:
    return cast(CapacityUnit, text)


def serialize_ec2_query(
    value: CapacityUnit, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityUnit:
    return from_ec2_query_text(el.text or "")

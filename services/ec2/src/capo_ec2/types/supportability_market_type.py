"""Generated from Smithy shape ``com.amazonaws.ec2#SupportabilityMarketType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

SupportabilityMarketType: TypeAlias = Literal[
    "on-demand",
    "spot",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SupportabilityMarketType) -> str:
    return value


def from_ec2_query_text(text: str) -> SupportabilityMarketType:
    return cast(SupportabilityMarketType, text)


def serialize_ec2_query(
    value: SupportabilityMarketType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SupportabilityMarketType:
    return from_ec2_query_text(el.text or "")

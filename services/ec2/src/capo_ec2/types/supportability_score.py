"""Generated from Smithy shape ``com.amazonaws.ec2#SupportabilityScore``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

SupportabilityScore: TypeAlias = Literal[
    "high",
    "medium",
    "low",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SupportabilityScore) -> str:
    return value


def from_ec2_query_text(text: str) -> SupportabilityScore:
    return cast(SupportabilityScore, text)


def serialize_ec2_query(
    value: SupportabilityScore, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SupportabilityScore:
    return from_ec2_query_text(el.text or "")

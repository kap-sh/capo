"""Generated from Smithy shape ``com.amazonaws.ec2#SeverityLabel``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

SeverityLabel: TypeAlias = Literal[
    "informational",
    "low",
    "medium",
    "high",
    "critical",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SeverityLabel) -> str:
    return value


def from_ec2_query_text(text: str) -> SeverityLabel:
    return cast(SeverityLabel, text)


def serialize_ec2_query(
    value: SeverityLabel, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SeverityLabel:
    return from_ec2_query_text(el.text or "")

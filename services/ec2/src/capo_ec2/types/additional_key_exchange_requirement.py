"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalKeyExchangeRequirement``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AdditionalKeyExchangeRequirement: TypeAlias = Literal[
    "required",
    "optional",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AdditionalKeyExchangeRequirement) -> str:
    return value


def from_ec2_query_text(text: str) -> AdditionalKeyExchangeRequirement:
    return cast(AdditionalKeyExchangeRequirement, text)


def serialize_ec2_query(
    value: AdditionalKeyExchangeRequirement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AdditionalKeyExchangeRequirement:
    return from_ec2_query_text(el.text or "")

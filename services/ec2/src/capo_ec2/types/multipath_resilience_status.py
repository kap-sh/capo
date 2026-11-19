"""Generated from Smithy shape ``com.amazonaws.ec2#MultipathResilienceStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

MultipathResilienceStatus: TypeAlias = Literal[
    "pending",
    "enabled",
    "disabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: MultipathResilienceStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> MultipathResilienceStatus:
    return cast(MultipathResilienceStatus, text)


def serialize_ec2_query(
    value: MultipathResilienceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MultipathResilienceStatus:
    return from_ec2_query_text(el.text or "")

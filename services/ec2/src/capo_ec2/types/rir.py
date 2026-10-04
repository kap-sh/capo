"""Generated from Smithy shape ``com.amazonaws.ec2#Rir``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The Regional Internet Registry (RIR).</p>"""
Rir: TypeAlias = Literal[
    "ripe",
    "apnic",
    "arin",
    "lacnic",
    "nicbr",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Rir) -> str:
    return value


def from_ec2_query_text(text: str) -> Rir:
    return cast(Rir, text)


def serialize_ec2_query(value: Rir, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Rir:
    return from_ec2_query_text(el.text or "")

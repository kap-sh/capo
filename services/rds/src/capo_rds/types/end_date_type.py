"""Generated from Smithy shape ``com.amazonaws.rds#EndDateType``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

EndDateType: TypeAlias = Literal[
    "unlimited",
    "limited",
]


# --- awsQuery ser/de ---
def to_query_text(value: EndDateType) -> str:
    return value


def from_query_text(text: str) -> EndDateType:
    return cast(EndDateType, text)


def serialize_query(
    value: EndDateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EndDateType:
    return from_query_text(el.text or "")

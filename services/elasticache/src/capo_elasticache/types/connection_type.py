"""Generated from Smithy shape ``com.amazonaws.elasticache#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

ConnectionType: TypeAlias = Literal[
    "vpc",
    "public",
]


# --- awsQuery ser/de ---
def to_query_text(value: ConnectionType) -> str:
    return value


def from_query_text(text: str) -> ConnectionType:
    return cast(ConnectionType, text)


def serialize_query(
    value: ConnectionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ConnectionType:
    return from_query_text(el.text or "")

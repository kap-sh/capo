"""Generated from Smithy shape ``com.amazonaws.elasticache#TlsMode``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

TlsMode: TypeAlias = Literal[
    "none",
    "verify-ca",
]


# --- awsQuery ser/de ---
def to_query_text(value: TlsMode) -> str:
    return value


def from_query_text(text: str) -> TlsMode:
    return cast(TlsMode, text)


def serialize_query(value: TlsMode, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TlsMode:
    return from_query_text(el.text or "")

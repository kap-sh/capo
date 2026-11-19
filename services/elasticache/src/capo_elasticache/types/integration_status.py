"""Generated from Smithy shape ``com.amazonaws.elasticache#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

IntegrationStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabling",
    "disabling",
    "failed",
]


# --- awsQuery ser/de ---
def to_query_text(value: IntegrationStatus) -> str:
    return value


def from_query_text(text: str) -> IntegrationStatus:
    return cast(IntegrationStatus, text)


def serialize_query(
    value: IntegrationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IntegrationStatus:
    return from_query_text(el.text or "")

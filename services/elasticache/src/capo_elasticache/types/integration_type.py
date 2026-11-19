"""Generated from Smithy shape ``com.amazonaws.elasticache#IntegrationType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

IntegrationType: TypeAlias = Literal["dynamodb",]


# --- awsQuery ser/de ---
def to_query_text(value: IntegrationType) -> str:
    return value


def from_query_text(text: str) -> IntegrationType:
    return cast(IntegrationType, text)


def serialize_query(
    value: IntegrationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IntegrationType:
    return from_query_text(el.text or "")

"""Generated from Smithy shape ``com.amazonaws.cloudwatch#QueryType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

QueryType: TypeAlias = Literal[
    "PROMQL",
    "SQL",
    "METRIC_MATH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QueryType:
    return cast(QueryType, data)


# --- awsQuery ser/de ---
def to_query_text(value: QueryType) -> str:
    return value


def from_query_text(text: str) -> QueryType:
    return cast(QueryType, text)


def serialize_query(
    value: QueryType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> QueryType:
    return from_query_text(el.text or "")

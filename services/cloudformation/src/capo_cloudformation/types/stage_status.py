"""Generated from Smithy shape ``com.amazonaws.cloudformation#StageStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StageStatus: TypeAlias = Literal[
    "PENDING",
    "NOT_APPLICABLE",
    "NOT_STARTED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "PARTIAL_SUCCESS",
    "FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: StageStatus) -> str:
    return value


def from_query_text(text: str) -> StageStatus:
    return cast(StageStatus, text)


def serialize_query(
    value: StageStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StageStatus:
    return from_query_text(el.text or "")

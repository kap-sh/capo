"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AmiArchitecture``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

AmiArchitecture: TypeAlias = Literal[
    "x86_64",
    "arm64",
]


# --- awsQuery ser/de ---
def to_query_text(value: AmiArchitecture) -> str:
    return value


def from_query_text(text: str) -> AmiArchitecture:
    return cast(AmiArchitecture, text)


def serialize_query(
    value: AmiArchitecture, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AmiArchitecture:
    return from_query_text(el.text or "")

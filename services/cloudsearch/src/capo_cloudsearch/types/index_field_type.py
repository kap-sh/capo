"""Generated from Smithy shape ``com.amazonaws.cloudsearch#IndexFieldType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudsearch._protocol.xml import Element

"""<p>The type of field. The valid options for a field depend on the field type. For more information about the supported field types, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html" target="_blank">Configuring Index Fields</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>"""
IndexFieldType: TypeAlias = Literal[
    "int",
    "double",
    "literal",
    "text",
    "date",
    "latlon",
    "int-array",
    "double-array",
    "literal-array",
    "text-array",
    "date-array",
]


# --- awsQuery ser/de ---
def to_query_text(value: IndexFieldType) -> str:
    return value


def from_query_text(text: str) -> IndexFieldType:
    return cast(IndexFieldType, text)


def serialize_query(
    value: IndexFieldType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IndexFieldType:
    return from_query_text(el.text or "")

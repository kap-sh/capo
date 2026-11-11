"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FieldType``."""

from typing import Literal, TypeAlias, cast

"""<p>The data type of a custom metadata field. Valid values:</p> <ul> <li> <p> <code>STRING</code> – The field holds a single string value.</p> </li> <li> <p> <code>STRING_LIST</code> – The field holds a list of string values.</p> </li> </ul>"""
FieldType: TypeAlias = Literal[
    "STRING",
    "STRING_LIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldType) -> str:
    return value


def deserialize_json(data: str) -> FieldType:
    return cast(FieldType, data)

"""Generated from Smithy shape ``com.amazonaws.athena#TableAttributes``."""

from typing import Literal, TypeAlias, cast

"""<p>A table property that can be requested in the <code>AttributesToGet</code> parameter of <code>ListTableMetadata</code>.</p>"""
TableAttributes: TypeAlias = Literal[
    "NAME",
    "TABLE_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableAttributes:
    return cast(TableAttributes, data)

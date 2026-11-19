"""Generated from Smithy shape ``com.amazonaws.athena#TableAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.table_attributes

TableAttributesList: TypeAlias = list[
    "capo_athena.types.table_attributes.TableAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableAttributesList) -> list:
    import capo_athena.types.table_attributes

    out: list = []
    for item in value:
        out.append(capo_athena.types.table_attributes.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableAttributesList:
    import capo_athena.types.table_attributes

    out: TableAttributesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_athena.types.table_attributes.deserialize_aws_json_1_1(item))
    return out

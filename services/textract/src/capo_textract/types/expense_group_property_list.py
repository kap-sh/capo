"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseGroupPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.expense_group_property

ExpenseGroupPropertyList: TypeAlias = list[
    "capo_textract.types.expense_group_property.ExpenseGroupProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseGroupPropertyList) -> list:
    import capo_textract.types.expense_group_property

    out: list = []
    for item in value:
        out.append(
            capo_textract.types.expense_group_property.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExpenseGroupPropertyList:
    import capo_textract.types.expense_group_property

    out: ExpenseGroupPropertyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.expense_group_property.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseGroupPropertyList) -> list:
    import capo_textract.types.expense_group_property

    out: list = []
    for item in value:
        out.append(capo_textract.types.expense_group_property.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExpenseGroupPropertyList:
    import capo_textract.types.expense_group_property

    out: ExpenseGroupPropertyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.expense_group_property.deserialize_cbor(item))
    return out

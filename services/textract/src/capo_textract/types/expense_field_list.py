"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.expense_field

ExpenseFieldList: TypeAlias = list["capo_textract.types.expense_field.ExpenseField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseFieldList) -> list:
    import capo_textract.types.expense_field

    out: list = []
    for item in value:
        out.append(capo_textract.types.expense_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExpenseFieldList:
    import capo_textract.types.expense_field

    out: ExpenseFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.expense_field.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseFieldList) -> list:
    import capo_textract.types.expense_field

    out: list = []
    for item in value:
        out.append(capo_textract.types.expense_field.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExpenseFieldList:
    import capo_textract.types.expense_field

    out: ExpenseFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.expense_field.deserialize_cbor(item))
    return out

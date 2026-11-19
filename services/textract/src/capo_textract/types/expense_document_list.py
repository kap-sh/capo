"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.expense_document

ExpenseDocumentList: TypeAlias = list[
    "capo_textract.types.expense_document.ExpenseDocument"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseDocumentList) -> list:
    import capo_textract.types.expense_document

    out: list = []
    for item in value:
        out.append(capo_textract.types.expense_document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExpenseDocumentList:
    import capo_textract.types.expense_document

    out: ExpenseDocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.expense_document.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseDocumentList) -> list:
    import capo_textract.types.expense_document

    out: list = []
    for item in value:
        out.append(capo_textract.types.expense_document.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExpenseDocumentList:
    import capo_textract.types.expense_document

    out: ExpenseDocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.expense_document.deserialize_cbor(item))
    return out

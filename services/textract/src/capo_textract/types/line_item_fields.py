"""Generated from Smithy shape ``com.amazonaws.textract#LineItemFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.expense_field_list


class LineItemFields(TypedDict, closed=True):
    line_item_expense_fields: NotRequired[
        "capo_textract.types.expense_field_list.ExpenseFieldList"
    ]
    """<p>ExpenseFields used to show information from detected lines on a table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineItemFields) -> dict:
    out: dict = {}
    if "line_item_expense_fields" in value:
        import capo_textract.types.expense_field_list

        out["LineItemExpenseFields"] = (
            capo_textract.types.expense_field_list.serialize_aws_json_1_1(
                value["line_item_expense_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LineItemFields:
    out: LineItemFields = {}  # type: ignore[typeddict-item]
    if data.get("LineItemExpenseFields") is not None:
        import capo_textract.types.expense_field_list

        out["line_item_expense_fields"] = (
            capo_textract.types.expense_field_list.deserialize_aws_json_1_1(
                data["LineItemExpenseFields"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LineItemFields) -> dict:
    out: dict = {}
    if "line_item_expense_fields" in value:
        import capo_textract.types.expense_field_list

        out["LineItemExpenseFields"] = (
            capo_textract.types.expense_field_list.serialize_cbor(
                value["line_item_expense_fields"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LineItemFields:
    out: LineItemFields = {}  # type: ignore[typeddict-item]
    if data.get("LineItemExpenseFields") is not None:
        import capo_textract.types.expense_field_list

        out["line_item_expense_fields"] = (
            capo_textract.types.expense_field_list.deserialize_cbor(
                data["LineItemExpenseFields"]
            )
        )
    return out

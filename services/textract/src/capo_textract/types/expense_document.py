"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.block_list
    import capo_textract.types.expense_field_list
    import capo_textract.types.line_item_group_list
    import capo_textract.types.u_integer


class ExpenseDocument(TypedDict, closed=True):
    expense_index: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>Denotes which invoice or receipt in the document the information is coming from. First document will be 1, the second 2, and so on.</p>"""
    summary_fields: NotRequired[
        "capo_textract.types.expense_field_list.ExpenseFieldList"
    ]
    """<p>Any information found outside of a table by Amazon Textract.</p>"""
    line_item_groups: NotRequired[
        "capo_textract.types.line_item_group_list.LineItemGroupList"
    ]
    """<p>Information detected on each table of a document, seperated into <code>LineItems</code>.</p>"""
    blocks: NotRequired["capo_textract.types.block_list.BlockList"]
    """<p>This is a block object, the same as reported when DetectDocumentText is run on a document. It provides word level recognition of text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseDocument) -> dict:
    out: dict = {}
    if "expense_index" in value:
        out["ExpenseIndex"] = value["expense_index"]
    if "summary_fields" in value:
        import capo_textract.types.expense_field_list

        out["SummaryFields"] = (
            capo_textract.types.expense_field_list.serialize_aws_json_1_1(
                value["summary_fields"]
            )
        )
    if "line_item_groups" in value:
        import capo_textract.types.line_item_group_list

        out["LineItemGroups"] = (
            capo_textract.types.line_item_group_list.serialize_aws_json_1_1(
                value["line_item_groups"]
            )
        )
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_aws_json_1_1(
            value["blocks"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpenseDocument:
    out: ExpenseDocument = {}  # type: ignore[typeddict-item]
    if data.get("ExpenseIndex") is not None:
        out["expense_index"] = data["ExpenseIndex"]
    if data.get("SummaryFields") is not None:
        import capo_textract.types.expense_field_list

        out["summary_fields"] = (
            capo_textract.types.expense_field_list.deserialize_aws_json_1_1(
                data["SummaryFields"]
            )
        )
    if data.get("LineItemGroups") is not None:
        import capo_textract.types.line_item_group_list

        out["line_item_groups"] = (
            capo_textract.types.line_item_group_list.deserialize_aws_json_1_1(
                data["LineItemGroups"]
            )
        )
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_aws_json_1_1(
            data["Blocks"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseDocument) -> dict:
    out: dict = {}
    if "expense_index" in value:
        out["ExpenseIndex"] = value["expense_index"]
    if "summary_fields" in value:
        import capo_textract.types.expense_field_list

        out["SummaryFields"] = capo_textract.types.expense_field_list.serialize_cbor(
            value["summary_fields"]
        )
    if "line_item_groups" in value:
        import capo_textract.types.line_item_group_list

        out["LineItemGroups"] = capo_textract.types.line_item_group_list.serialize_cbor(
            value["line_item_groups"]
        )
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_cbor(value["blocks"])
    return out


def deserialize_cbor(data: dict) -> ExpenseDocument:
    out: ExpenseDocument = {}  # type: ignore[typeddict-item]
    if data.get("ExpenseIndex") is not None:
        out["expense_index"] = data["ExpenseIndex"]
    if data.get("SummaryFields") is not None:
        import capo_textract.types.expense_field_list

        out["summary_fields"] = capo_textract.types.expense_field_list.deserialize_cbor(
            data["SummaryFields"]
        )
    if data.get("LineItemGroups") is not None:
        import capo_textract.types.line_item_group_list

        out["line_item_groups"] = (
            capo_textract.types.line_item_group_list.deserialize_cbor(
                data["LineItemGroups"]
            )
        )
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_cbor(data["Blocks"])
    return out

"""Generated from Smithy shape ``com.amazonaws.textract#ExpenseField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.expense_currency
    import capo_textract.types.expense_detection
    import capo_textract.types.expense_group_property_list
    import capo_textract.types.expense_type
    import capo_textract.types.u_integer


class ExpenseField(TypedDict, closed=True):
    type: NotRequired["capo_textract.types.expense_type.ExpenseType"]
    """<p>The implied label of a detected element. Present alongside LabelDetection for explicit elements.</p>"""
    label_detection: NotRequired[
        "capo_textract.types.expense_detection.ExpenseDetection"
    ]
    """<p>The explicitly stated label of a detected element.</p>"""
    value_detection: NotRequired[
        "capo_textract.types.expense_detection.ExpenseDetection"
    ]
    """<p>The value of a detected element. Present in explicit and implicit elements.</p>"""
    page_number: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The page number the value was detected on.</p>"""
    currency: NotRequired["capo_textract.types.expense_currency.ExpenseCurrency"]
    """<p>Shows the kind of currency, both the code and confidence associated with any monatary value detected.</p>"""
    group_properties: NotRequired[
        "capo_textract.types.expense_group_property_list.ExpenseGroupPropertyList"
    ]
    """<p>Shows which group a response object belongs to, such as whether an address line belongs to the vendor's address or the recipent's address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpenseField) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_textract.types.expense_type

        out["Type"] = capo_textract.types.expense_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "label_detection" in value:
        import capo_textract.types.expense_detection

        out["LabelDetection"] = (
            capo_textract.types.expense_detection.serialize_aws_json_1_1(
                value["label_detection"]
            )
        )
    if "value_detection" in value:
        import capo_textract.types.expense_detection

        out["ValueDetection"] = (
            capo_textract.types.expense_detection.serialize_aws_json_1_1(
                value["value_detection"]
            )
        )
    if "page_number" in value:
        out["PageNumber"] = value["page_number"]
    if "currency" in value:
        import capo_textract.types.expense_currency

        out["Currency"] = capo_textract.types.expense_currency.serialize_aws_json_1_1(
            value["currency"]
        )
    if "group_properties" in value:
        import capo_textract.types.expense_group_property_list

        out["GroupProperties"] = (
            capo_textract.types.expense_group_property_list.serialize_aws_json_1_1(
                value["group_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpenseField:
    out: ExpenseField = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_textract.types.expense_type

        out["type"] = capo_textract.types.expense_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("LabelDetection") is not None:
        import capo_textract.types.expense_detection

        out["label_detection"] = (
            capo_textract.types.expense_detection.deserialize_aws_json_1_1(
                data["LabelDetection"]
            )
        )
    if data.get("ValueDetection") is not None:
        import capo_textract.types.expense_detection

        out["value_detection"] = (
            capo_textract.types.expense_detection.deserialize_aws_json_1_1(
                data["ValueDetection"]
            )
        )
    if data.get("PageNumber") is not None:
        out["page_number"] = data["PageNumber"]
    if data.get("Currency") is not None:
        import capo_textract.types.expense_currency

        out["currency"] = capo_textract.types.expense_currency.deserialize_aws_json_1_1(
            data["Currency"]
        )
    if data.get("GroupProperties") is not None:
        import capo_textract.types.expense_group_property_list

        out["group_properties"] = (
            capo_textract.types.expense_group_property_list.deserialize_aws_json_1_1(
                data["GroupProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpenseField) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_textract.types.expense_type

        out["Type"] = capo_textract.types.expense_type.serialize_cbor(value["type"])
    if "label_detection" in value:
        import capo_textract.types.expense_detection

        out["LabelDetection"] = capo_textract.types.expense_detection.serialize_cbor(
            value["label_detection"]
        )
    if "value_detection" in value:
        import capo_textract.types.expense_detection

        out["ValueDetection"] = capo_textract.types.expense_detection.serialize_cbor(
            value["value_detection"]
        )
    if "page_number" in value:
        out["PageNumber"] = value["page_number"]
    if "currency" in value:
        import capo_textract.types.expense_currency

        out["Currency"] = capo_textract.types.expense_currency.serialize_cbor(
            value["currency"]
        )
    if "group_properties" in value:
        import capo_textract.types.expense_group_property_list

        out["GroupProperties"] = (
            capo_textract.types.expense_group_property_list.serialize_cbor(
                value["group_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ExpenseField:
    out: ExpenseField = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_textract.types.expense_type

        out["type"] = capo_textract.types.expense_type.deserialize_cbor(data["Type"])
    if data.get("LabelDetection") is not None:
        import capo_textract.types.expense_detection

        out["label_detection"] = capo_textract.types.expense_detection.deserialize_cbor(
            data["LabelDetection"]
        )
    if data.get("ValueDetection") is not None:
        import capo_textract.types.expense_detection

        out["value_detection"] = capo_textract.types.expense_detection.deserialize_cbor(
            data["ValueDetection"]
        )
    if data.get("PageNumber") is not None:
        out["page_number"] = data["PageNumber"]
    if data.get("Currency") is not None:
        import capo_textract.types.expense_currency

        out["currency"] = capo_textract.types.expense_currency.deserialize_cbor(
            data["Currency"]
        )
    if data.get("GroupProperties") is not None:
        import capo_textract.types.expense_group_property_list

        out["group_properties"] = (
            capo_textract.types.expense_group_property_list.deserialize_cbor(
                data["GroupProperties"]
            )
        )
    return out

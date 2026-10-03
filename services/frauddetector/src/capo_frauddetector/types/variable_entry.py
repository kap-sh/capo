"""Generated from Smithy shape ``com.amazonaws.frauddetector#VariableEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.string


class VariableEntry(TypedDict, closed=True):
    name: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The name of the variable.</p>"""
    data_type: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The data type of the variable.</p>"""
    data_source: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The data source of the variable.</p>"""
    default_value: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The default value of the variable.</p>"""
    description: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The description of the variable.</p>"""
    variable_type: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The type of the variable. For more information see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>.</p> <p>Valid Values: <code>AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT </code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariableEntry) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "data_type" in value:
        out["dataType"] = value["data_type"]
    if "data_source" in value:
        out["dataSource"] = value["data_source"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VariableEntry:
    out: VariableEntry = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("dataType") is not None:
        out["data_type"] = data["dataType"]
    if data.get("dataSource") is not None:
        out["data_source"] = data["dataSource"]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    return out

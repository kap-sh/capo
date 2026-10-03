"""Generated from Smithy shape ``com.amazonaws.frauddetector#Variable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.data_source
    import capo_frauddetector.types.data_type
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.string
    import capo_frauddetector.types.time


class Variable(TypedDict, closed=True):
    name: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The name of the variable.</p>"""
    data_type: NotRequired["capo_frauddetector.types.data_type.DataType"]
    """<p>The data type of the variable. For more information see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>.</p>"""
    data_source: NotRequired["capo_frauddetector.types.data_source.DataSource"]
    """<p>The data source of the variable.</p>"""
    default_value: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The default value of the variable.</p>"""
    description: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The description of the variable. </p>"""
    variable_type: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The variable type of the variable.</p> <p>Valid Values: <code>AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT </code> </p>"""
    last_updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>The time when variable was last updated.</p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>The time when the variable was created.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The ARN of the variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Variable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "data_type" in value:
        import capo_frauddetector.types.data_type

        out["dataType"] = capo_frauddetector.types.data_type.serialize_aws_json_1_1(
            value["data_type"]
        )
    if "data_source" in value:
        import capo_frauddetector.types.data_source

        out["dataSource"] = capo_frauddetector.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Variable:
    out: Variable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("dataType") is not None:
        import capo_frauddetector.types.data_type

        out["data_type"] = capo_frauddetector.types.data_type.deserialize_aws_json_1_1(
            data["dataType"]
        )
    if data.get("dataSource") is not None:
        import capo_frauddetector.types.data_source

        out["data_source"] = (
            capo_frauddetector.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if data.get("createdTime") is not None:
        out["created_time"] = data["createdTime"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out

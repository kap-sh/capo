"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateVariableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.data_source
    import capo_frauddetector.types.data_type
    import capo_frauddetector.types.string
    import capo_frauddetector.types.tag_list


class CreateVariableRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.string.string"
    """<p>The name of the variable.</p>"""
    data_type: "capo_frauddetector.types.data_type.DataType"
    """<p>The data type of the variable.</p>"""
    data_source: "capo_frauddetector.types.data_source.DataSource"
    """<p>The source of the data.</p>"""
    default_value: "capo_frauddetector.types.string.string"
    """<p>The default value for the variable when no value is received.</p>"""
    description: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The description.</p>"""
    variable_type: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The variable type. For more information see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>. </p> <p>Valid Values: <code>AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT</code> </p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVariableRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_frauddetector.types.data_type

    out["dataType"] = capo_frauddetector.types.data_type.serialize_aws_json_1_1(
        value["data_type"]
    )
    import capo_frauddetector.types.data_source

    out["dataSource"] = capo_frauddetector.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVariableRequest:
    out: CreateVariableRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateVariableRequest.name required")
    if data.get("dataType") is not None:
        import capo_frauddetector.types.data_type

        out["data_type"] = capo_frauddetector.types.data_type.deserialize_aws_json_1_1(
            data["dataType"]
        )
    else:
        raise DeserializationError("CreateVariableRequest.data_type required")
    if data.get("dataSource") is not None:
        import capo_frauddetector.types.data_source

        out["data_source"] = (
            capo_frauddetector.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    else:
        raise DeserializationError("CreateVariableRequest.data_source required")
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    else:
        raise DeserializationError("CreateVariableRequest.default_value required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out

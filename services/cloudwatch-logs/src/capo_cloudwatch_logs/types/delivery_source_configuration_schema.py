"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceConfigurationSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_source_configuration_numeric_value
    import capo_cloudwatch_logs.types.delivery_source_configuration_schema_field
    import capo_cloudwatch_logs.types.delivery_source_configuration_schema_value_type
    import capo_cloudwatch_logs.types.delivery_source_configuration_supported_values


class DeliverySourceConfigurationSchema(TypedDict, closed=True):
    key_name: "capo_cloudwatch_logs.types.delivery_source_configuration_schema_field.DeliverySourceConfigurationSchemaField"
    """<p>The name of the configuration.</p>"""
    value_type: "capo_cloudwatch_logs.types.delivery_source_configuration_schema_value_type.DeliverySourceConfigurationSchemaValueType"
    """<p>The data type of the configuration value. Valid values are <code>string</code>, <code>boolean</code>, <code>int</code>, <code>double</code>, and <code>long</code>.</p>"""
    default_value: "capo_cloudwatch_logs.types.delivery_source_configuration_schema_field.DeliverySourceConfigurationSchemaField"
    """<p>The default value of the configuration that is used when a value is not specified in a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html">PutDeliverySource</a> request.</p>"""
    supported_values: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_configuration_supported_values.DeliverySourceConfigurationSupportedValues"
    ]
    """<p>The list of allowed values for the configuration. Empty for free-form configuration.</p>"""
    min_value: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_configuration_numeric_value.DeliverySourceConfigurationNumericValue"
    ]
    """<p>The minimum numeric value allowed for the configuration. This applies only when the <code>valueType</code> is a numeric type.</p>"""
    max_value: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_configuration_numeric_value.DeliverySourceConfigurationNumericValue"
    ]
    """<p>The maximum numeric value allowed for the configuration. This applies only when the <code>valueType</code> is a numeric type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceConfigurationSchema) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    import capo_cloudwatch_logs.types.delivery_source_configuration_schema_value_type

    out["valueType"] = (
        capo_cloudwatch_logs.types.delivery_source_configuration_schema_value_type.serialize_aws_json_1_1(
            value["value_type"]
        )
    )
    out["defaultValue"] = value["default_value"]
    if "supported_values" in value:
        import capo_cloudwatch_logs.types.delivery_source_configuration_supported_values

        out["supportedValues"] = (
            capo_cloudwatch_logs.types.delivery_source_configuration_supported_values.serialize_aws_json_1_1(
                value["supported_values"]
            )
        )
    if "min_value" in value:
        out["minValue"] = (
            "NaN"
            if value["min_value"] != value["min_value"]
            else "Infinity"
            if value["min_value"] == float("inf")
            else "-Infinity"
            if value["min_value"] == float("-inf")
            else value["min_value"]
        )
    if "max_value" in value:
        out["maxValue"] = (
            "NaN"
            if value["max_value"] != value["max_value"]
            else "Infinity"
            if value["max_value"] == float("inf")
            else "-Infinity"
            if value["max_value"] == float("-inf")
            else value["max_value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliverySourceConfigurationSchema:
    out: DeliverySourceConfigurationSchema = {}  # type: ignore[typeddict-item]
    if data.get("keyName") is not None:
        out["key_name"] = data["keyName"]
    else:
        raise DeserializationError(
            "DeliverySourceConfigurationSchema.key_name required"
        )
    if data.get("valueType") is not None:
        import capo_cloudwatch_logs.types.delivery_source_configuration_schema_value_type

        out["value_type"] = (
            capo_cloudwatch_logs.types.delivery_source_configuration_schema_value_type.deserialize_aws_json_1_1(
                data["valueType"]
            )
        )
    else:
        raise DeserializationError(
            "DeliverySourceConfigurationSchema.value_type required"
        )
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    else:
        raise DeserializationError(
            "DeliverySourceConfigurationSchema.default_value required"
        )
    if data.get("supportedValues") is not None:
        import capo_cloudwatch_logs.types.delivery_source_configuration_supported_values

        out["supported_values"] = (
            capo_cloudwatch_logs.types.delivery_source_configuration_supported_values.deserialize_aws_json_1_1(
                data["supportedValues"]
            )
        )
    if data.get("minValue") is not None:
        out["min_value"] = float(data["minValue"])
    if data.get("maxValue") is not None:
        out["max_value"] = float(data["maxValue"])
    return out

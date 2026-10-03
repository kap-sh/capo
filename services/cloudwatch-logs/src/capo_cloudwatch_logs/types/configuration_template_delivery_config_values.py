"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ConfigurationTemplateDeliveryConfigValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field_delimiter
    import capo_cloudwatch_logs.types.record_fields
    import capo_cloudwatch_logs.types.s3_delivery_configuration


class ConfigurationTemplateDeliveryConfigValues(TypedDict, closed=True):
    record_fields: NotRequired["capo_cloudwatch_logs.types.record_fields.RecordFields"]
    """<p>The default record fields that will be delivered when a list of record fields is not provided in a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a> operation.</p>"""
    field_delimiter: NotRequired[
        "capo_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
    ]
    """<p>The default field delimiter that is used in a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a> operation when the field delimiter is not specified in that operation. The field delimiter is used only when the final output delivery is in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>"""
    s3_delivery_configuration: NotRequired[
        "capo_cloudwatch_logs.types.s3_delivery_configuration.S3DeliveryConfiguration"
    ]
    """<p>The delivery parameters that are used when you create a delivery to a delivery destination that is an S3 Bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTemplateDeliveryConfigValues) -> dict:
    out: dict = {}
    if "record_fields" in value:
        import capo_cloudwatch_logs.types.record_fields

        out["recordFields"] = (
            capo_cloudwatch_logs.types.record_fields.serialize_aws_json_1_1(
                value["record_fields"]
            )
        )
    if "field_delimiter" in value:
        out["fieldDelimiter"] = value["field_delimiter"]
    if "s3_delivery_configuration" in value:
        import capo_cloudwatch_logs.types.s3_delivery_configuration

        out["s3DeliveryConfiguration"] = (
            capo_cloudwatch_logs.types.s3_delivery_configuration.serialize_aws_json_1_1(
                value["s3_delivery_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationTemplateDeliveryConfigValues:
    out: ConfigurationTemplateDeliveryConfigValues = {}  # type: ignore[typeddict-item]
    if data.get("recordFields") is not None:
        import capo_cloudwatch_logs.types.record_fields

        out["record_fields"] = (
            capo_cloudwatch_logs.types.record_fields.deserialize_aws_json_1_1(
                data["recordFields"]
            )
        )
    if data.get("fieldDelimiter") is not None:
        out["field_delimiter"] = data["fieldDelimiter"]
    if data.get("s3DeliveryConfiguration") is not None:
        import capo_cloudwatch_logs.types.s3_delivery_configuration

        out["s3_delivery_configuration"] = (
            capo_cloudwatch_logs.types.s3_delivery_configuration.deserialize_aws_json_1_1(
                data["s3DeliveryConfiguration"]
            )
        )
    return out

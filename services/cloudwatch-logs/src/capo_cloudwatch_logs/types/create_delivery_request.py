"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateDeliveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.delivery_source_name
    import capo_cloudwatch_logs.types.field_delimiter
    import capo_cloudwatch_logs.types.record_fields
    import capo_cloudwatch_logs.types.s3_delivery_configuration
    import capo_cloudwatch_logs.types.tags


class CreateDeliveryRequest(TypedDict, closed=True):
    delivery_source_name: (
        "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
    )
    """<p>The name of the delivery source to use for this delivery.</p>"""
    delivery_destination_arn: "capo_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the delivery destination to use for this delivery.</p>"""
    record_fields: NotRequired["capo_cloudwatch_logs.types.record_fields.RecordFields"]
    """<p>The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.</p>"""
    field_delimiter: NotRequired[
        "capo_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
    ]
    """<p>The field delimiter to use between record fields when the final output format of a delivery is in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>"""
    s3_delivery_configuration: NotRequired[
        "capo_cloudwatch_logs.types.s3_delivery_configuration.S3DeliveryConfiguration"
    ]
    """<p>This structure contains parameters that are valid only when the delivery's delivery destination is an S3 bucket.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeliveryRequest) -> dict:
    out: dict = {}
    out["deliverySourceName"] = value["delivery_source_name"]
    out["deliveryDestinationArn"] = value["delivery_destination_arn"]
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
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeliveryRequest:
    out: CreateDeliveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("deliverySourceName") is not None:
        out["delivery_source_name"] = data["deliverySourceName"]
    else:
        raise DeserializationError(
            "CreateDeliveryRequest.delivery_source_name required"
        )
    if data.get("deliveryDestinationArn") is not None:
        out["delivery_destination_arn"] = data["deliveryDestinationArn"]
    else:
        raise DeserializationError(
            "CreateDeliveryRequest.delivery_destination_arn required"
        )
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
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.firehose#StartDeliveryStreamEncryptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_encryption_configuration_input
    import capo_firehose.types.delivery_stream_name


class StartDeliveryStreamEncryptionInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream for which you want to enable server-side encryption (SSE).</p>"""
    delivery_stream_encryption_configuration_input: NotRequired[
        "capo_firehose.types.delivery_stream_encryption_configuration_input.DeliveryStreamEncryptionConfigurationInput"
    ]
    """<p>Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDeliveryStreamEncryptionInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    if "delivery_stream_encryption_configuration_input" in value:
        import capo_firehose.types.delivery_stream_encryption_configuration_input

        out["DeliveryStreamEncryptionConfigurationInput"] = (
            capo_firehose.types.delivery_stream_encryption_configuration_input.serialize_aws_json_1_1(
                value["delivery_stream_encryption_configuration_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDeliveryStreamEncryptionInput:
    out: StartDeliveryStreamEncryptionInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    if data.get("DeliveryStreamEncryptionConfigurationInput") is not None:
        import capo_firehose.types.delivery_stream_encryption_configuration_input

        out["delivery_stream_encryption_configuration_input"] = (
            capo_firehose.types.delivery_stream_encryption_configuration_input.deserialize_aws_json_1_1(
                data["DeliveryStreamEncryptionConfigurationInput"]
            )
        )
    return out

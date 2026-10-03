"""Generated from Smithy shape ``com.amazonaws.firehose#DeleteDeliveryStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.delivery_stream_name


class DeleteDeliveryStreamInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream.</p>"""
    allow_force_delete: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>Set this to true if you want to delete the Firehose stream even if Firehose is unable to retire the grant for the CMK. Firehose might be unable to retire the grant due to a customer error, such as when the CMK or the grant are in an invalid state. If you force deletion, you can then use the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html">RevokeGrant</a> operation to revoke the grant you gave to Firehose. If a failure to retire the grant happens due to an Amazon Web Services KMS issue, Firehose keeps retrying the delete operation.</p> <p>The default value is false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    if "allow_force_delete" in value:
        out["AllowForceDelete"] = value["allow_force_delete"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliveryStreamInput:
    out: DeleteDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError(
            "DeleteDeliveryStreamInput.delivery_stream_name required"
        )
    if data.get("AllowForceDelete") is not None:
        out["allow_force_delete"] = data["AllowForceDelete"]
    return out

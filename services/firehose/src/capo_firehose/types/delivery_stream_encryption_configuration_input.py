"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamEncryptionConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.awskms_key_arn_for_sse
    import capo_firehose.types.key_type


class DeliveryStreamEncryptionConfigurationInput(TypedDict, closed=True):
    key_arn: NotRequired[
        "capo_firehose.types.awskms_key_arn_for_sse.AWSKMSKeyARNForSSE"
    ]
    """<p>If you set <code>KeyType</code> to <code>CUSTOMER_MANAGED_CMK</code>, you must specify the Amazon Resource Name (ARN) of the CMK. If you set <code>KeyType</code> to <code>Amazon Web Services_OWNED_CMK</code>, Firehose uses a service-account CMK.</p>"""
    key_type: "capo_firehose.types.key_type.KeyType"
    """<p>Indicates the type of customer master key (CMK) to use for encryption. The default setting is <code>Amazon Web Services_OWNED_CMK</code>. For more information about CMKs, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys">Customer Master Keys (CMKs)</a>. When you invoke <a>CreateDeliveryStream</a> or <a>StartDeliveryStreamEncryption</a> with <code>KeyType</code> set to CUSTOMER_MANAGED_CMK, Firehose invokes the Amazon KMS operation <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html">CreateGrant</a> to create a grant that allows the Firehose service to use the customer managed CMK to perform encryption and decryption. Firehose manages that grant. </p> <p>When you invoke <a>StartDeliveryStreamEncryption</a> to change the CMK for a Firehose stream that is encrypted with a customer managed CMK, Firehose schedules the grant it had on the old CMK for retirement.</p> <p>You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 Firehose streams. If a <a>CreateDeliveryStream</a> or <a>StartDeliveryStreamEncryption</a> operation exceeds this limit, Firehose throws a <code>LimitExceededException</code>. </p> <important> <p>To encrypt your Firehose stream, use symmetric CMKs. Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html">About Symmetric and Asymmetric CMKs</a> in the Amazon Web Services Key Management Service developer guide.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamEncryptionConfigurationInput) -> dict:
    out: dict = {}
    if "key_arn" in value:
        out["KeyARN"] = value["key_arn"]
    import capo_firehose.types.key_type

    out["KeyType"] = capo_firehose.types.key_type.serialize_aws_json_1_1(
        value["key_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryStreamEncryptionConfigurationInput:
    out: DeliveryStreamEncryptionConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyARN") is not None:
        out["key_arn"] = data["KeyARN"]
    if data.get("KeyType") is not None:
        import capo_firehose.types.key_type

        out["key_type"] = capo_firehose.types.key_type.deserialize_aws_json_1_1(
            data["KeyType"]
        )
    else:
        raise DeserializationError(
            "DeliveryStreamEncryptionConfigurationInput.key_type required"
        )
    return out

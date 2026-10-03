"""Generated from Smithy shape ``com.amazonaws.kinesis#StopStreamEncryptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.encryption_type
    import capo_kinesis.types.key_id
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class StopStreamEncryptionInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream on which to stop encrypting records.</p>"""
    encryption_type: "capo_kinesis.types.encryption_type.EncryptionType"
    """<p>The encryption type. The only valid value is <code>KMS</code>.</p>"""
    key_id: "capo_kinesis.types.key_id.KeyId"
    """<p>The GUID for the customer-managed Amazon Web Services KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias <code>aws/kinesis</code>.</p> <ul> <li> <p>Key ARN example: <code>arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias ARN example: <code>arn:aws:kms:us-east-1:123456789012:alias/MyAliasName</code> </p> </li> <li> <p>Globally unique key ID example: <code>12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p>Alias name example: <code>alias/MyAliasName</code> </p> </li> <li> <p>Master key owned by Kinesis Data Streams: <code>alias/aws/kinesis</code> </p> </li> </ul>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopStreamEncryptionInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import capo_kinesis.types.encryption_type

    out["EncryptionType"] = capo_kinesis.types.encryption_type.serialize_aws_json_1_1(
        value["encryption_type"]
    )
    out["KeyId"] = value["key_id"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopStreamEncryptionInput:
    out: StopStreamEncryptionInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("EncryptionType") is not None:
        import capo_kinesis.types.encryption_type

        out["encryption_type"] = (
            capo_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    else:
        raise DeserializationError("StopStreamEncryptionInput.encryption_type required")
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("StopStreamEncryptionInput.key_id required")
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out

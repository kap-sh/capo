"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.channel_encryption_type
    import capo_kinesis.types.key_id


class ChannelEncryptionConfiguration(TypedDict, closed=True):
    encryption_type: "capo_kinesis.types.channel_encryption_type.ChannelEncryptionType"
    """<p>The encryption type. The only valid value is <code>KMS</code>.</p>"""
    key_id: "capo_kinesis.types.key_id.KeyId"
    """<p>The identifier of the customer managed Amazon Web Services KMS key. You cannot use the Amazon Kinesis Data Streams service key (<code>aws/kinesis</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelEncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis.types.channel_encryption_type

    out["EncryptionType"] = (
        capo_kinesis.types.channel_encryption_type.serialize_aws_json_1_1(
            value["encryption_type"]
        )
    )
    out["KeyId"] = value["key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelEncryptionConfiguration:
    out: ChannelEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EncryptionType") is not None:
        import capo_kinesis.types.channel_encryption_type

        out["encryption_type"] = (
            capo_kinesis.types.channel_encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    else:
        import typing

        out["encryption_type"] = typing.cast(
            "capo_kinesis.types.channel_encryption_type.ChannelEncryptionType", ""
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    return out

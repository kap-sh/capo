"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationEncryptionConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.key_id
    import capo_kinesis_analytics_v2.types.key_type


class ApplicationEncryptionConfigurationDescription(TypedDict, closed=True):
    key_id: NotRequired["capo_kinesis_analytics_v2.types.key_id.KeyId"]
    """<p>The key ARN, key ID, alias ARN, or alias name of the KMS key used for encryption at rest.</p>"""
    key_type: "capo_kinesis_analytics_v2.types.key_type.KeyType"
    """<p>Specifies the type of key used for encryption at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ApplicationEncryptionConfigurationDescription,
) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    import capo_kinesis_analytics_v2.types.key_type

    out["KeyType"] = capo_kinesis_analytics_v2.types.key_type.serialize_aws_json_1_1(
        value["key_type"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ApplicationEncryptionConfigurationDescription:
    out: ApplicationEncryptionConfigurationDescription = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("KeyType") is not None:
        import capo_kinesis_analytics_v2.types.key_type

        out["key_type"] = (
            capo_kinesis_analytics_v2.types.key_type.deserialize_aws_json_1_1(
                data["KeyType"]
            )
        )
    else:
        import typing

        out["key_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.key_type.KeyType", ""
        )
    return out

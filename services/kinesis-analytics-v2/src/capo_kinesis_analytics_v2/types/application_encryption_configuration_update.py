"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationEncryptionConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.key_id
    import capo_kinesis_analytics_v2.types.key_type


class ApplicationEncryptionConfigurationUpdate(TypedDict, closed=True):
    key_id_update: NotRequired["capo_kinesis_analytics_v2.types.key_id.KeyId"]
    """<p>The key ARN, key ID, alias ARN, or alias name of the KMS key to be used for encryption at rest.</p>"""
    key_type_update: "capo_kinesis_analytics_v2.types.key_type.KeyType"
    """<p>Specifies the type of key to be used for encryption at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationEncryptionConfigurationUpdate) -> dict:
    out: dict = {}
    if "key_id_update" in value:
        out["KeyIdUpdate"] = value["key_id_update"]
    import capo_kinesis_analytics_v2.types.key_type

    out["KeyTypeUpdate"] = (
        capo_kinesis_analytics_v2.types.key_type.serialize_aws_json_1_1(
            value["key_type_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationEncryptionConfigurationUpdate:
    out: ApplicationEncryptionConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdUpdate") is not None:
        out["key_id_update"] = data["KeyIdUpdate"]
    if data.get("KeyTypeUpdate") is not None:
        import capo_kinesis_analytics_v2.types.key_type

        out["key_type_update"] = (
            capo_kinesis_analytics_v2.types.key_type.deserialize_aws_json_1_1(
                data["KeyTypeUpdate"]
            )
        )
    else:
        import typing

        out["key_type_update"] = typing.cast(
            "capo_kinesis_analytics_v2.types.key_type.KeyType", ""
        )
    return out

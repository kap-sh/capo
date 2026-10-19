"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError, SerializationError
from capo_odb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_odb.types.aws_encryption_key_configuration
    import capo_odb.types.oci_encryption_key_configuration
    import capo_odb.types.okv_encryption_key_configuration


class _EncryptionKeyConfiguration_awsEncryptionKey(TypedDict, closed=True):
    awsEncryptionKey: (
        "capo_odb.types.aws_encryption_key_configuration.AwsEncryptionKeyConfiguration"
    )


class _EncryptionKeyConfiguration_ociEncryptionKey(TypedDict, closed=True):
    ociEncryptionKey: (
        "capo_odb.types.oci_encryption_key_configuration.OciEncryptionKeyConfiguration"
    )


class _EncryptionKeyConfiguration_okvEncryptionKey(TypedDict, closed=True):
    okvEncryptionKey: (
        "capo_odb.types.okv_encryption_key_configuration.OkvEncryptionKeyConfiguration"
    )


EncryptionKeyConfiguration: TypeAlias = (
    _EncryptionKeyConfiguration_awsEncryptionKey
    | _EncryptionKeyConfiguration_ociEncryptionKey
    | _EncryptionKeyConfiguration_okvEncryptionKey
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionKeyConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EncryptionKeyConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "awsEncryptionKey" in value:
        import capo_odb.types.aws_encryption_key_configuration

        return {
            "awsEncryptionKey": capo_odb.types.aws_encryption_key_configuration.serialize_aws_json_1_0(
                value["awsEncryptionKey"]
            )
        }
    elif "ociEncryptionKey" in value:
        import capo_odb.types.oci_encryption_key_configuration

        return {
            "ociEncryptionKey": capo_odb.types.oci_encryption_key_configuration.serialize_aws_json_1_0(
                value["ociEncryptionKey"]
            )
        }
    elif "okvEncryptionKey" in value:
        import capo_odb.types.okv_encryption_key_configuration

        return {
            "okvEncryptionKey": capo_odb.types.okv_encryption_key_configuration.serialize_aws_json_1_0(
                value["okvEncryptionKey"]
            )
        }
    else:
        raise SerializationError("EncryptionKeyConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EncryptionKeyConfiguration:
    if data.get("awsEncryptionKey") is not None:
        import capo_odb.types.aws_encryption_key_configuration

        return {
            "awsEncryptionKey": capo_odb.types.aws_encryption_key_configuration.deserialize_aws_json_1_0(
                data["awsEncryptionKey"]
            )
        }
    elif data.get("ociEncryptionKey") is not None:
        import capo_odb.types.oci_encryption_key_configuration

        return {
            "ociEncryptionKey": capo_odb.types.oci_encryption_key_configuration.deserialize_aws_json_1_0(
                data["ociEncryptionKey"]
            )
        }
    elif data.get("okvEncryptionKey") is not None:
        import capo_odb.types.okv_encryption_key_configuration

        return {
            "okvEncryptionKey": capo_odb.types.okv_encryption_key_configuration.deserialize_aws_json_1_0(
                data["okvEncryptionKey"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "EncryptionKeyConfiguration: no recognized variant key"
        )

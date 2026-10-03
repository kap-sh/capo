"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyStoreInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.deletion_protection
    import capo_verifiedpermissions.types.encryption_settings
    import capo_verifiedpermissions.types.idempotency_token
    import capo_verifiedpermissions.types.policy_store_description
    import capo_verifiedpermissions.types.tag_map
    import capo_verifiedpermissions.types.validation_settings


class CreatePolicyStoreInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
    ]
    """<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>"""
    validation_settings: (
        "capo_verifiedpermissions.types.validation_settings.ValidationSettings"
    )
    """<p>Specifies the validation setting for this policy store.</p> <p>Currently, the only valid and required value is <code>Mode</code>.</p> <important> <p>We recommend that you turn on <code>STRICT</code> mode only after you define a schema. If a schema doesn't exist, then <code>STRICT</code> mode causes any policy to fail validation, and Verified Permissions rejects the policy. You can turn off validation by using the <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore">UpdatePolicyStore</a>. Then, when you have a schema defined, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore">UpdatePolicyStore</a> again to turn validation back on.</p> </important>"""
    description: NotRequired[
        "capo_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
    ]
    """<p>Descriptive text that you can provide to help with identification of the current policy store.</p>"""
    deletion_protection: NotRequired[
        "capo_verifiedpermissions.types.deletion_protection.DeletionProtection"
    ]
    """<p>Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.</p> <p>The default state is <code>DISABLED</code>.</p>"""
    encryption_settings: NotRequired[
        "capo_verifiedpermissions.types.encryption_settings.EncryptionSettings"
    ]
    """<p>Specifies the encryption settings used to encrypt the policy store and their child resources. Allows for the ability to use a customer owned KMS key for encryption of data.</p> <p>This is an optional field to be used when providing a customer-managed KMS key for encryption.</p>"""
    tags: NotRequired["capo_verifiedpermissions.types.tag_map.TagMap"]
    """<p>The list of key-value pairs to associate with the policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyStoreInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_verifiedpermissions.types.validation_settings

    out["validationSettings"] = (
        capo_verifiedpermissions.types.validation_settings.serialize_aws_json_1_0(
            value["validation_settings"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "deletion_protection" in value:
        import capo_verifiedpermissions.types.deletion_protection

        out["deletionProtection"] = (
            capo_verifiedpermissions.types.deletion_protection.serialize_aws_json_1_0(
                value["deletion_protection"]
            )
        )
    if "encryption_settings" in value:
        import capo_verifiedpermissions.types.encryption_settings

        out["encryptionSettings"] = (
            capo_verifiedpermissions.types.encryption_settings.serialize_aws_json_1_0(
                value["encryption_settings"]
            )
        )
    if "tags" in value:
        import capo_verifiedpermissions.types.tag_map

        out["tags"] = capo_verifiedpermissions.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyStoreInput:
    out: CreatePolicyStoreInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("validationSettings") is not None:
        import capo_verifiedpermissions.types.validation_settings

        out["validation_settings"] = (
            capo_verifiedpermissions.types.validation_settings.deserialize_aws_json_1_0(
                data["validationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePolicyStoreInput.validation_settings required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("deletionProtection") is not None:
        import capo_verifiedpermissions.types.deletion_protection

        out["deletion_protection"] = (
            capo_verifiedpermissions.types.deletion_protection.deserialize_aws_json_1_0(
                data["deletionProtection"]
            )
        )
    if data.get("encryptionSettings") is not None:
        import capo_verifiedpermissions.types.encryption_settings

        out["encryption_settings"] = (
            capo_verifiedpermissions.types.encryption_settings.deserialize_aws_json_1_0(
                data["encryptionSettings"]
            )
        )
    if data.get("tags") is not None:
        import capo_verifiedpermissions.types.tag_map

        out["tags"] = capo_verifiedpermissions.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdatePolicyStoreInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.deletion_protection
    import capo_verifiedpermissions.types.policy_store_description
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.validation_settings


class UpdatePolicyStoreInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store that you want to update</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    validation_settings: (
        "capo_verifiedpermissions.types.validation_settings.ValidationSettings"
    )
    """<p>A structure that defines the validation settings that want to enable for the policy store.</p>"""
    deletion_protection: NotRequired[
        "capo_verifiedpermissions.types.deletion_protection.DeletionProtection"
    ]
    """<p>Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.</p> <p>When you call <code>UpdatePolicyStore</code>, this parameter is unchanged unless explicitly included in the call.</p>"""
    description: NotRequired[
        "capo_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
    ]
    """<p>Descriptive text that you can provide to help with identification of the current policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePolicyStoreInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    import capo_verifiedpermissions.types.validation_settings

    out["validationSettings"] = (
        capo_verifiedpermissions.types.validation_settings.serialize_aws_json_1_0(
            value["validation_settings"]
        )
    )
    if "deletion_protection" in value:
        import capo_verifiedpermissions.types.deletion_protection

        out["deletionProtection"] = (
            capo_verifiedpermissions.types.deletion_protection.serialize_aws_json_1_0(
                value["deletion_protection"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePolicyStoreInput:
    out: UpdatePolicyStoreInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("UpdatePolicyStoreInput.policy_store_id required")
    if data.get("validationSettings") is not None:
        import capo_verifiedpermissions.types.validation_settings

        out["validation_settings"] = (
            capo_verifiedpermissions.types.validation_settings.deserialize_aws_json_1_0(
                data["validationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePolicyStoreInput.validation_settings required"
        )
    if data.get("deletionProtection") is not None:
        import capo_verifiedpermissions.types.deletion_protection

        out["deletion_protection"] = (
            capo_verifiedpermissions.types.deletion_protection.deserialize_aws_json_1_0(
                data["deletionProtection"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyStoreAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.alias
    import capo_verifiedpermissions.types.policy_store_id


class CreatePolicyStoreAliasInput(TypedDict, closed=True):
    alias_name: "capo_verifiedpermissions.types.alias.Alias"
    """<p>Specifies the name of the policy store alias to create. The name must be unique within your Amazon Web Services account and Amazon Web Services Region.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>"""
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store to associate with the alias.</p> <note> <p>The associated policy store must be specified using its ID. The alias name cannot be used.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyStoreAliasInput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    out["policyStoreId"] = value["policy_store_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyStoreAliasInput:
    out: CreatePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    else:
        out["alias_name"] = ""
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    return out

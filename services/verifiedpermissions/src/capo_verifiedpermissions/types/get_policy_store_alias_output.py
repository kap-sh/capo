"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyStoreAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.alias
    import capo_verifiedpermissions.types.alias_state
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.resource_arn
    import capo_verifiedpermissions.types.timestamp_format


class GetPolicyStoreAliasOutput(TypedDict, closed=True):
    alias_name: "capo_verifiedpermissions.types.alias.Alias"
    """<p>The name of the policy store alias.</p>"""
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store associated with the alias.</p>"""
    alias_arn: "capo_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the policy store alias.</p>"""
    created_at: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy store alias was created.</p>"""
    state: "capo_verifiedpermissions.types.alias_state.AliasState"
    """<p>The state of the policy store alias. Policy Store Aliases in the Active state can be used normally. When a policy store alias is deleted, it enters the PendingDeletion state. Policy Store Aliases in the PendingDeletion cannot be used, and creating a policy store alias with the same alias name will fail.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyStoreAliasOutput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    out["policyStoreId"] = value["policy_store_id"]
    out["aliasArn"] = value["alias_arn"]
    import capo_verifiedpermissions.types.timestamp_format

    out["createdAt"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import capo_verifiedpermissions.types.alias_state

    out["state"] = capo_verifiedpermissions.types.alias_state.serialize_aws_json_1_0(
        value["state"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyStoreAliasOutput:
    out: GetPolicyStoreAliasOutput = {}  # type: ignore[typeddict-item]
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    else:
        out["alias_name"] = ""
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("aliasArn") is not None:
        out["alias_arn"] = data["aliasArn"]
    else:
        out["alias_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_at"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("state") is not None:
        import capo_verifiedpermissions.types.alias_state

        out["state"] = (
            capo_verifiedpermissions.types.alias_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_verifiedpermissions.types.alias_state.AliasState", ""
        )
    return out

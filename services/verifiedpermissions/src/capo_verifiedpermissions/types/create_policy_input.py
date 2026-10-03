"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.idempotency_token
    import capo_verifiedpermissions.types.policy_definition
    import capo_verifiedpermissions.types.policy_name
    import capo_verifiedpermissions.types.policy_store_id


class CreatePolicyInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
    ]
    """<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>"""
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the <code>PolicyStoreId</code> of the policy store you want to store the policy in.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    definition: "capo_verifiedpermissions.types.policy_definition.PolicyDefinition"
    """<p>A structure that specifies the policy type and content to use for the new policy. You must include either a static or a templateLinked element. The policy content must be written in the Cedar policy language.</p>"""
    name: NotRequired["capo_verifiedpermissions.types.policy_name.PolicyName"]
    """<p>Specifies a name for the policy that is unique among all policies within the policy store. You can use the name in place of the policy ID in API operations that reference the policy. The name must be prefixed with <code>name/</code>.</p> <p>If you specify a name that is already associated with another policy in the policy store, you receive a <code>ConflictException</code> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["policyStoreId"] = value["policy_store_id"]
    import capo_verifiedpermissions.types.policy_definition

    out["definition"] = (
        capo_verifiedpermissions.types.policy_definition.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyInput:
    out: CreatePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("CreatePolicyInput.policy_store_id required")
    if data.get("definition") is not None:
        import capo_verifiedpermissions.types.policy_definition

        out["definition"] = (
            capo_verifiedpermissions.types.policy_definition.deserialize_aws_json_1_0(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyInput.definition required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out

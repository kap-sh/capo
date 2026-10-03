"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreateIdentitySourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.configuration
    import capo_verifiedpermissions.types.idempotency_token
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.principal_entity_type


class CreateIdentitySourceInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
    ]
    """<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>"""
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store in which you want to store this identity source. Only policies and requests made using this policy store can reference identities from the identity provider configured in the new identity source.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    configuration: "capo_verifiedpermissions.types.configuration.Configuration"
    """<p>Specifies the details required to communicate with the identity provider (IdP) associated with this identity source.</p>"""
    principal_entity_type: NotRequired[
        "capo_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    ]
    """<p>Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIdentitySourceInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["policyStoreId"] = value["policy_store_id"]
    import capo_verifiedpermissions.types.configuration

    out["configuration"] = (
        capo_verifiedpermissions.types.configuration.serialize_aws_json_1_0(
            value["configuration"]
        )
    )
    if "principal_entity_type" in value:
        out["principalEntityType"] = value["principal_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIdentitySourceInput:
    out: CreateIdentitySourceInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("CreateIdentitySourceInput.policy_store_id required")
    if data.get("configuration") is not None:
        import capo_verifiedpermissions.types.configuration

        out["configuration"] = (
            capo_verifiedpermissions.types.configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateIdentitySourceInput.configuration required")
    if data.get("principalEntityType") is not None:
        out["principal_entity_type"] = data["principalEntityType"]
    return out

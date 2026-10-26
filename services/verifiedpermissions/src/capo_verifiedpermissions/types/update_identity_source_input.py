"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateIdentitySourceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.identity_source_id
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.principal_entity_type
    import capo_verifiedpermissions.types.update_configuration


class UpdateIdentitySourceInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store that contains the identity source that you want to update.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    identity_source_id: (
        "capo_verifiedpermissions.types.identity_source_id.IdentitySourceId"
    )
    """<p>Specifies the ID of the identity source that you want to update.</p>"""
    update_configuration: (
        "capo_verifiedpermissions.types.update_configuration.UpdateConfiguration"
    )
    """<p>Specifies the details required to communicate with the identity provider (IdP) associated with this identity source.</p>"""
    principal_entity_type: NotRequired[
        "capo_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    ]
    """<p>Specifies the data type of principals generated for identities authenticated by the identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateIdentitySourceInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["identitySourceId"] = value["identity_source_id"]
    import capo_verifiedpermissions.types.update_configuration

    out["updateConfiguration"] = (
        capo_verifiedpermissions.types.update_configuration.serialize_aws_json_1_0(
            value["update_configuration"]
        )
    )
    if "principal_entity_type" in value:
        out["principalEntityType"] = value["principal_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateIdentitySourceInput:
    out: UpdateIdentitySourceInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("identitySourceId") is not None:
        out["identity_source_id"] = data["identitySourceId"]
    else:
        out["identity_source_id"] = ""
    if data.get("updateConfiguration") is not None:
        import capo_verifiedpermissions.types.update_configuration

        out["update_configuration"] = (
            capo_verifiedpermissions.types.update_configuration.deserialize_aws_json_1_0(
                data["updateConfiguration"]
            )
        )
    else:
        out["update_configuration"] = {"$unknown": {"name": ""}}
    if data.get("principalEntityType") is not None:
        out["principal_entity_type"] = data["principalEntityType"]
    return out


def redact_sensitive(value: UpdateIdentitySourceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "update_configuration" in value:
        import capo_verifiedpermissions.types.update_configuration

        out["update_configuration"] = (
            capo_verifiedpermissions.types.update_configuration.redact_sensitive(
                value["update_configuration"]
            )
        )
    if "principal_entity_type" in value:
        out["principal_entity_type"] = "*** Sensitive Data Redacted ***"
    return out

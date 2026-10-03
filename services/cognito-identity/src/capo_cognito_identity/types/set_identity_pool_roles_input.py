"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#SetIdentityPoolRolesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.role_mapping_map
    import capo_cognito_identity.types.roles_map


class SetIdentityPoolRolesInput(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    roles: "capo_cognito_identity.types.roles_map.RolesMap"
    """<p>The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.</p>"""
    role_mappings: NotRequired[
        "capo_cognito_identity.types.role_mapping_map.RoleMappingMap"
    ]
    """<p>How users for a specific identity provider are to mapped to roles. This is a string to <a>RoleMapping</a> object map. The string identifies the identity provider, for example, <code>graph.facebook.com</code> or <code>cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id</code>.</p> <p>Up to 25 rules can be specified per identity provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetIdentityPoolRolesInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    import capo_cognito_identity.types.roles_map

    out["Roles"] = capo_cognito_identity.types.roles_map.serialize_aws_json_1_1(
        value["roles"]
    )
    if "role_mappings" in value:
        import capo_cognito_identity.types.role_mapping_map

        out["RoleMappings"] = (
            capo_cognito_identity.types.role_mapping_map.serialize_aws_json_1_1(
                value["role_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetIdentityPoolRolesInput:
    out: SetIdentityPoolRolesInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "SetIdentityPoolRolesInput.identity_pool_id required"
        )
    if data.get("Roles") is not None:
        import capo_cognito_identity.types.roles_map

        out["roles"] = capo_cognito_identity.types.roles_map.deserialize_aws_json_1_1(
            data["Roles"]
        )
    else:
        raise DeserializationError("SetIdentityPoolRolesInput.roles required")
    if data.get("RoleMappings") is not None:
        import capo_cognito_identity.types.role_mapping_map

        out["role_mappings"] = (
            capo_cognito_identity.types.role_mapping_map.deserialize_aws_json_1_1(
                data["RoleMappings"]
            )
        )
    return out

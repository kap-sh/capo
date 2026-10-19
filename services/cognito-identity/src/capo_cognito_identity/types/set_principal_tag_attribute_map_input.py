"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#SetPrincipalTagAttributeMapInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.identity_provider_name
    import capo_cognito_identity.types.principal_tags
    import capo_cognito_identity.types.use_defaults


class SetPrincipalTagAttributeMapInput(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>The ID of the Identity Pool you want to set attribute mappings for.</p>"""
    identity_provider_name: (
        "capo_cognito_identity.types.identity_provider_name.IdentityProviderName"
    )
    """<p>The provider name you want to use for attribute mappings.</p>"""
    use_defaults: NotRequired["capo_cognito_identity.types.use_defaults.UseDefaults"]
    """<p>You can use this operation to use default (username and clientID) attribute mappings.</p>"""
    principal_tags: NotRequired[
        "capo_cognito_identity.types.principal_tags.PrincipalTags"
    ]
    """<p>You can use this operation to add principal tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetPrincipalTagAttributeMapInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    out["IdentityProviderName"] = value["identity_provider_name"]
    if "use_defaults" in value:
        out["UseDefaults"] = value["use_defaults"]
    if "principal_tags" in value:
        import capo_cognito_identity.types.principal_tags

        out["PrincipalTags"] = (
            capo_cognito_identity.types.principal_tags.serialize_aws_json_1_1(
                value["principal_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetPrincipalTagAttributeMapInput:
    out: SetPrincipalTagAttributeMapInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        out["identity_pool_id"] = ""
    if data.get("IdentityProviderName") is not None:
        out["identity_provider_name"] = data["IdentityProviderName"]
    else:
        out["identity_provider_name"] = ""
    if data.get("UseDefaults") is not None:
        out["use_defaults"] = data["UseDefaults"]
    if data.get("PrincipalTags") is not None:
        import capo_cognito_identity.types.principal_tags

        out["principal_tags"] = (
            capo_cognito_identity.types.principal_tags.deserialize_aws_json_1_1(
                data["PrincipalTags"]
            )
        )
    return out

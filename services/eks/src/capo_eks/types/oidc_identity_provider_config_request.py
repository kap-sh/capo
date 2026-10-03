"""Generated from Smithy shape ``com.amazonaws.eks#OidcIdentityProviderConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.required_claims_map
    import capo_eks.types.string


class OidcIdentityProviderConfigRequest(TypedDict, closed=True):
    identity_provider_config_name: "capo_eks.types.string.String"
    """<p>The name of the OIDC provider configuration.</p>"""
    issuer_url: "capo_eks.types.string.String"
    """<p>The URL of the OIDC identity provider that allows the API server to discover public signing keys for verifying tokens. The URL must begin with <code>https://</code> and should correspond to the <code>iss</code> claim in the provider's OIDC ID tokens. Based on the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like <code>https://server.example.org</code> or <code>https://example.com</code>. This URL should point to the level below <code>.well-known/openid-configuration</code> and must be publicly accessible over the internet.</p>"""
    client_id: "capo_eks.types.string.String"
    """<p>This is also known as <i>audience</i>. The ID for the client application that makes authentication requests to the OIDC identity provider.</p>"""
    username_claim: NotRequired["capo_eks.types.string.String"]
    """<p>The JSON Web Token (JWT) claim to use as the username. The default is <code>sub</code>, which is expected to be a unique identifier of the end user. You can choose other claims, such as <code>email</code> or <code>name</code>, depending on the OIDC identity provider. Claims other than <code>email</code> are prefixed with the issuer URL to prevent naming clashes with other plug-ins.</p>"""
    username_prefix: NotRequired["capo_eks.types.string.String"]
    """<p>The prefix that is prepended to username claims to prevent clashes with existing names. If you do not provide this field, and <code>username</code> is a value other than <code>email</code>, the prefix defaults to <code>issuerurl#</code>. You can use the value <code>-</code> to disable all prefixing.</p>"""
    groups_claim: NotRequired["capo_eks.types.string.String"]
    """<p>The JWT claim that the provider uses to return your groups.</p>"""
    groups_prefix: NotRequired["capo_eks.types.string.String"]
    """<p>The prefix that is prepended to group claims to prevent clashes with existing names (such as <code>system:</code> groups). For example, the value<code> oidc:</code> will create group names like <code>oidc:engineering</code> and <code>oidc:infra</code>.</p>"""
    required_claims: NotRequired["capo_eks.types.required_claims_map.requiredClaimsMap"]
    """<p>The key value pairs that describe required claims in the identity token. If set, each claim is verified to be present in the token with a matching value. For the maximum number of claims that you can require, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html">Amazon EKS service quotas</a> in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OidcIdentityProviderConfigRequest) -> dict:
    out: dict = {}
    out["identityProviderConfigName"] = value["identity_provider_config_name"]
    out["issuerUrl"] = value["issuer_url"]
    out["clientId"] = value["client_id"]
    if "username_claim" in value:
        out["usernameClaim"] = value["username_claim"]
    if "username_prefix" in value:
        out["usernamePrefix"] = value["username_prefix"]
    if "groups_claim" in value:
        out["groupsClaim"] = value["groups_claim"]
    if "groups_prefix" in value:
        out["groupsPrefix"] = value["groups_prefix"]
    if "required_claims" in value:
        import capo_eks.types.required_claims_map

        out["requiredClaims"] = capo_eks.types.required_claims_map.serialize_json(
            value["required_claims"]
        )
    return out


def deserialize_json(data: dict) -> OidcIdentityProviderConfigRequest:
    out: OidcIdentityProviderConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("identityProviderConfigName") is not None:
        out["identity_provider_config_name"] = data["identityProviderConfigName"]
    else:
        raise DeserializationError(
            "OidcIdentityProviderConfigRequest.identity_provider_config_name required"
        )
    if data.get("issuerUrl") is not None:
        out["issuer_url"] = data["issuerUrl"]
    else:
        raise DeserializationError(
            "OidcIdentityProviderConfigRequest.issuer_url required"
        )
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "OidcIdentityProviderConfigRequest.client_id required"
        )
    if data.get("usernameClaim") is not None:
        out["username_claim"] = data["usernameClaim"]
    if data.get("usernamePrefix") is not None:
        out["username_prefix"] = data["usernamePrefix"]
    if data.get("groupsClaim") is not None:
        out["groups_claim"] = data["groupsClaim"]
    if data.get("groupsPrefix") is not None:
        out["groups_prefix"] = data["groupsPrefix"]
    if data.get("requiredClaims") is not None:
        import capo_eks.types.required_claims_map

        out["required_claims"] = capo_eks.types.required_claims_map.deserialize_json(
            data["requiredClaims"]
        )
    return out

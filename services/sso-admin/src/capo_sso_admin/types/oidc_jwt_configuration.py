"""Generated from Smithy shape ``com.amazonaws.ssoadmin#OidcJwtConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.claim_attribute_path
    import capo_sso_admin.types.jmes_path
    import capo_sso_admin.types.jwks_retrieval_option
    import capo_sso_admin.types.trusted_token_issuer_url


class OidcJwtConfiguration(TypedDict, closed=True):
    issuer_url: "capo_sso_admin.types.trusted_token_issuer_url.TrustedTokenIssuerUrl"
    """<p>The URL that IAM Identity Center uses for OpenID Discovery. OpenID Discovery is used to obtain the information required to verify the tokens that the trusted token issuer generates.</p>"""
    claim_attribute_path: "capo_sso_admin.types.claim_attribute_path.ClaimAttributePath"
    """<p>The path of the source attribute in the JWT from the trusted token issuer. The attribute mapped by this JMESPath expression is compared against the attribute mapped by <code>IdentityStoreAttributePath</code> when a trusted token issuer token is exchanged for an IAM Identity Center token.</p>"""
    identity_store_attribute_path: "capo_sso_admin.types.jmes_path.JMESPath"
    """<p>The path of the destination attribute in a JWT from IAM Identity Center. The attribute mapped by this JMESPath expression is compared against the attribute mapped by <code>ClaimAttributePath</code> when a trusted token issuer token is exchanged for an IAM Identity Center token. </p>"""
    jwks_retrieval_option: (
        "capo_sso_admin.types.jwks_retrieval_option.JwksRetrievalOption"
    )
    """<p>The method that the trusted token issuer can use to retrieve the JSON Web Key Set used to verify a JWT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OidcJwtConfiguration) -> dict:
    out: dict = {}
    out["IssuerUrl"] = value["issuer_url"]
    out["ClaimAttributePath"] = value["claim_attribute_path"]
    out["IdentityStoreAttributePath"] = value["identity_store_attribute_path"]
    import capo_sso_admin.types.jwks_retrieval_option

    out["JwksRetrievalOption"] = (
        capo_sso_admin.types.jwks_retrieval_option.serialize_aws_json_1_1(
            value["jwks_retrieval_option"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OidcJwtConfiguration:
    out: OidcJwtConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IssuerUrl") is not None:
        out["issuer_url"] = data["IssuerUrl"]
    else:
        out["issuer_url"] = ""
    if data.get("ClaimAttributePath") is not None:
        out["claim_attribute_path"] = data["ClaimAttributePath"]
    else:
        out["claim_attribute_path"] = ""
    if data.get("IdentityStoreAttributePath") is not None:
        out["identity_store_attribute_path"] = data["IdentityStoreAttributePath"]
    else:
        out["identity_store_attribute_path"] = ""
    if data.get("JwksRetrievalOption") is not None:
        import capo_sso_admin.types.jwks_retrieval_option

        out["jwks_retrieval_option"] = (
            capo_sso_admin.types.jwks_retrieval_option.deserialize_aws_json_1_1(
                data["JwksRetrievalOption"]
            )
        )
    else:
        import typing

        out["jwks_retrieval_option"] = typing.cast(
            "capo_sso_admin.types.jwks_retrieval_option.JwksRetrievalOption", ""
        )
    return out

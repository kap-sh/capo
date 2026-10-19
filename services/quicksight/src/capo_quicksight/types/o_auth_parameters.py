"""Generated from Smithy shape ``com.amazonaws.quicksight#OAuthParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.ca_certificates_bundle_s3_uri
    import capo_quicksight.types.identity_provider_resource_uri
    import capo_quicksight.types.o_auth_scope
    import capo_quicksight.types.token_provider_url
    import capo_quicksight.types.vpc_connection_properties


class OAuthParameters(TypedDict, closed=True):
    token_provider_url: "capo_quicksight.types.token_provider_url.TokenProviderUrl"
    """<p>The token endpoint URL of the identity provider.</p>"""
    o_auth_scope: NotRequired["capo_quicksight.types.o_auth_scope.OAuthScope"]
    """<p>The OAuth scope.</p>"""
    identity_provider_vpc_connection_properties: NotRequired[
        "capo_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    identity_provider_resource_uri: NotRequired[
        "capo_quicksight.types.identity_provider_resource_uri.IdentityProviderResourceUri"
    ]
    """<p>The resource uri of the identity provider.</p>"""
    identity_provider_ca_certificates_bundle_s3_uri: NotRequired[
        "capo_quicksight.types.ca_certificates_bundle_s3_uri.CACertificatesBundleS3Uri"
    ]
    """<p>The S3 URI of the identity provider's CA certificates bundle in PEM format. Use this parameter to provide a custom CA certificate bundle for the identity provider when the default trust store does not include the required certificates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthParameters) -> dict:
    out: dict = {}
    out["TokenProviderUrl"] = value["token_provider_url"]
    if "o_auth_scope" in value:
        out["OAuthScope"] = value["o_auth_scope"]
    if "identity_provider_vpc_connection_properties" in value:
        import capo_quicksight.types.vpc_connection_properties

        out["IdentityProviderVpcConnectionProperties"] = (
            capo_quicksight.types.vpc_connection_properties.serialize_json(
                value["identity_provider_vpc_connection_properties"]
            )
        )
    if "identity_provider_resource_uri" in value:
        out["IdentityProviderResourceUri"] = value["identity_provider_resource_uri"]
    if "identity_provider_ca_certificates_bundle_s3_uri" in value:
        out["IdentityProviderCACertificatesBundleS3Uri"] = value[
            "identity_provider_ca_certificates_bundle_s3_uri"
        ]
    return out


def deserialize_json(data: dict) -> OAuthParameters:
    out: OAuthParameters = {}  # type: ignore[typeddict-item]
    if data.get("TokenProviderUrl") is not None:
        out["token_provider_url"] = data["TokenProviderUrl"]
    else:
        out["token_provider_url"] = ""
    if data.get("OAuthScope") is not None:
        out["o_auth_scope"] = data["OAuthScope"]
    if data.get("IdentityProviderVpcConnectionProperties") is not None:
        import capo_quicksight.types.vpc_connection_properties

        out["identity_provider_vpc_connection_properties"] = (
            capo_quicksight.types.vpc_connection_properties.deserialize_json(
                data["IdentityProviderVpcConnectionProperties"]
            )
        )
    if data.get("IdentityProviderResourceUri") is not None:
        out["identity_provider_resource_uri"] = data["IdentityProviderResourceUri"]
    if data.get("IdentityProviderCACertificatesBundleS3Uri") is not None:
        out["identity_provider_ca_certificates_bundle_s3_uri"] = data[
            "IdentityProviderCACertificatesBundleS3Uri"
        ]
    return out

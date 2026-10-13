"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateOAuthClientApplicationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.data_source_type
    import capo_quicksight.types.o_auth_authorization_endpoint_url
    import capo_quicksight.types.o_auth_client_application_id
    import capo_quicksight.types.o_auth_client_id
    import capo_quicksight.types.o_auth_client_secret
    import capo_quicksight.types.o_auth_scopes_string
    import capo_quicksight.types.o_auth_token_endpoint_url
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.vpc_connection_properties


class UpdateOAuthClientApplicationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    o_auth_client_application_id: (
        "capo_quicksight.types.o_auth_client_application_id.OAuthClientApplicationId"
    )
    """<p>The ID of the OAuthClientApplication that you want to update.</p>"""
    name: "capo_quicksight.types.resource_name.ResourceName"
    """<p>The display name for the OAuthClientApplication.</p>"""
    client_id: NotRequired["capo_quicksight.types.o_auth_client_id.OAuthClientId"]
    """<p>The client ID of the OAuth application that is registered with the identity provider.</p>"""
    client_secret: NotRequired[
        "capo_quicksight.types.o_auth_client_secret.OAuthClientSecret"
    ]
    """<p>The client secret of the OAuth application that is registered with the identity provider.</p>"""
    o_auth_token_endpoint_url: NotRequired[
        "capo_quicksight.types.o_auth_token_endpoint_url.OAuthTokenEndpointUrl"
    ]
    """<p>The token endpoint URL of the identity provider that is used to obtain access tokens.</p>"""
    o_auth_authorization_endpoint_url: NotRequired[
        "capo_quicksight.types.o_auth_authorization_endpoint_url.OAuthAuthorizationEndpointUrl"
    ]
    """<p>The authorization endpoint URL of the identity provider that is used to obtain authorization codes.</p>"""
    o_auth_scopes: NotRequired[
        "capo_quicksight.types.o_auth_scopes_string.OAuthScopesString"
    ]
    """<p>The OAuth scopes that are requested when the OAuthClientApplication obtains an access token from the identity provider.</p>"""
    data_source_type: NotRequired[
        "capo_quicksight.types.data_source_type.DataSourceType"
    ]
    """<p>The type of data source that the OAuthClientApplication is used with. Valid values are <code>SNOWFLAKE</code>.</p>"""
    identity_provider_vpc_connection_properties: NotRequired[
        "capo_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOAuthClientApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    if "o_auth_token_endpoint_url" in value:
        out["OAuthTokenEndpointUrl"] = value["o_auth_token_endpoint_url"]
    if "o_auth_authorization_endpoint_url" in value:
        out["OAuthAuthorizationEndpointUrl"] = value[
            "o_auth_authorization_endpoint_url"
        ]
    if "o_auth_scopes" in value:
        out["OAuthScopes"] = value["o_auth_scopes"]
    if "data_source_type" in value:
        import capo_quicksight.types.data_source_type

        out["DataSourceType"] = capo_quicksight.types.data_source_type.serialize_json(
            value["data_source_type"]
        )
    if "identity_provider_vpc_connection_properties" in value:
        import capo_quicksight.types.vpc_connection_properties

        out["IdentityProviderVpcConnectionProperties"] = (
            capo_quicksight.types.vpc_connection_properties.serialize_json(
                value["identity_provider_vpc_connection_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOAuthClientApplicationRequest:
    out: UpdateOAuthClientApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateOAuthClientApplicationRequest.name required")
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    if data.get("OAuthTokenEndpointUrl") is not None:
        out["o_auth_token_endpoint_url"] = data["OAuthTokenEndpointUrl"]
    if data.get("OAuthAuthorizationEndpointUrl") is not None:
        out["o_auth_authorization_endpoint_url"] = data["OAuthAuthorizationEndpointUrl"]
    if data.get("OAuthScopes") is not None:
        out["o_auth_scopes"] = data["OAuthScopes"]
    if data.get("DataSourceType") is not None:
        import capo_quicksight.types.data_source_type

        out["data_source_type"] = (
            capo_quicksight.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    if data.get("IdentityProviderVpcConnectionProperties") is not None:
        import capo_quicksight.types.vpc_connection_properties

        out["identity_provider_vpc_connection_properties"] = (
            capo_quicksight.types.vpc_connection_properties.deserialize_json(
                data["IdentityProviderVpcConnectionProperties"]
            )
        )
    return out


def redact_sensitive(value: UpdateOAuthClientApplicationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    if "o_auth_token_endpoint_url" in value:
        out["o_auth_token_endpoint_url"] = "*** Sensitive Data Redacted ***"
    if "o_auth_authorization_endpoint_url" in value:
        out["o_auth_authorization_endpoint_url"] = "*** Sensitive Data Redacted ***"
    return out

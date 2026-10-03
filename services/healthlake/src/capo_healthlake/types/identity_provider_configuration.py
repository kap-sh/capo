"""Generated from Smithy shape ``com.amazonaws.healthlake#IdentityProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.authorization_strategy
    import capo_healthlake.types.configuration_metadata
    import capo_healthlake.types.health_lake_boolean
    import capo_healthlake.types.lambda_arn


class IdentityProviderConfiguration(TypedDict, closed=True):
    authorization_strategy: (
        "capo_healthlake.types.authorization_strategy.AuthorizationStrategy"
    )
    """<p>The authorization strategy selected when the HealthLake data store is created.</p> <note> <p>HealthLake provides support for both SMART on FHIR V1 and V2 as described below.</p> <ul> <li> <p> <code>SMART_ON_FHIR_V1</code> – Support for only SMART on FHIR V1, which includes <code>read</code> (read/search) and <code>write</code> (create/update/delete) permissions.</p> </li> <li> <p> <code>SMART_ON_FHIR</code> – Support for both SMART on FHIR V1 and V2, which includes <code>create</code>, <code>read</code>, <code>update</code>, <code>delete</code>, and <code>search</code> permissions.</p> </li> <li> <p> <code>Amazon Web Services_AUTH</code> – The default HealthLake authorization strategy; not affiliated with SMART on FHIR.</p> </li> </ul> </note>"""
    fine_grained_authorization_enabled: (
        "capo_healthlake.types.health_lake_boolean.HealthLakeBoolean"
    )
    """<p>The parameter to enable SMART on FHIR fine-grained authorization for the data store.</p>"""
    metadata: NotRequired[
        "capo_healthlake.types.configuration_metadata.ConfigurationMetadata"
    ]
    """<p>The JSON metadata elements to use in your identity provider configuration. Required elements are listed based on the launch specification of the SMART application. For more information on all possible elements, see <a href="https://build.fhir.org/ig/HL7/smart-app-launch/conformance.html#metadata">Metadata</a> in SMART's App Launch specification.</p> <p> <code>authorization_endpoint</code>: The URL to the OAuth2 authorization endpoint.</p> <p> <code>grant_types_supported</code>: An array of grant types that are supported at the token endpoint. You must provide at least one grant type option. Valid options are <code>authorization_code</code> and <code>client_credentials</code>.</p> <p> <code>token_endpoint</code>: The URL to the OAuth2 token endpoint.</p> <p> <code>capabilities</code>: An array of strings of the SMART capabilities that the authorization server supports.</p> <p> <code>code_challenge_methods_supported</code>: An array of strings of supported PKCE code challenge methods. You must include the <code>S256</code> method in the array of PKCE code challenge methods.</p>"""
    idp_lambda_arn: NotRequired["capo_healthlake.types.lambda_arn.LambdaArn"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function to use to decode the access token created by the authorization server.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentityProviderConfiguration) -> dict:
    out: dict = {}
    import capo_healthlake.types.authorization_strategy

    out["AuthorizationStrategy"] = (
        capo_healthlake.types.authorization_strategy.serialize_aws_json_1_0(
            value["authorization_strategy"]
        )
    )
    out["FineGrainedAuthorizationEnabled"] = value.get(
        "fine_grained_authorization_enabled", False
    )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "idp_lambda_arn" in value:
        out["IdpLambdaArn"] = value["idp_lambda_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IdentityProviderConfiguration:
    out: IdentityProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AuthorizationStrategy") is not None:
        import capo_healthlake.types.authorization_strategy

        out["authorization_strategy"] = (
            capo_healthlake.types.authorization_strategy.deserialize_aws_json_1_0(
                data["AuthorizationStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "IdentityProviderConfiguration.authorization_strategy required"
        )
    if data.get("FineGrainedAuthorizationEnabled") is not None:
        out["fine_grained_authorization_enabled"] = data[
            "FineGrainedAuthorizationEnabled"
        ]
    else:
        out["fine_grained_authorization_enabled"] = False
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("IdpLambdaArn") is not None:
        out["idp_lambda_arn"] = data["IdpLambdaArn"]
    return out

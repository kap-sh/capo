"""Generated from Smithy shape ``com.amazonaws.appsync#CreateGraphqlApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.additional_authentication_providers
    import capo_appsync.types.authentication_type
    import capo_appsync.types.boolean
    import capo_appsync.types.enhanced_metrics_config
    import capo_appsync.types.graph_ql_api_introspection_config
    import capo_appsync.types.graph_ql_api_type
    import capo_appsync.types.graph_ql_api_visibility
    import capo_appsync.types.lambda_authorizer_config
    import capo_appsync.types.log_config
    import capo_appsync.types.open_id_connect_config
    import capo_appsync.types.query_depth_limit
    import capo_appsync.types.resolver_count_limit
    import capo_appsync.types.string
    import capo_appsync.types.tag_map
    import capo_appsync.types.user_pool_config


class CreateGraphqlApiRequest(TypedDict, closed=True):
    name: "capo_appsync.types.string.String"
    """<p>A user-supplied name for the <code>GraphqlApi</code>.</p>"""
    log_config: NotRequired["capo_appsync.types.log_config.LogConfig"]
    """<p>The Amazon CloudWatch Logs configuration.</p>"""
    authentication_type: "capo_appsync.types.authentication_type.AuthenticationType"
    """<p>The authentication type: API key, Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda.</p>"""
    user_pool_config: NotRequired["capo_appsync.types.user_pool_config.UserPoolConfig"]
    """<p>The Amazon Cognito user pool configuration.</p>"""
    open_id_connect_config: NotRequired[
        "capo_appsync.types.open_id_connect_config.OpenIDConnectConfig"
    ]
    """<p>The OIDC configuration.</p>"""
    tags: NotRequired["capo_appsync.types.tag_map.TagMap"]
    """<p>A <code>TagMap</code> object.</p>"""
    additional_authentication_providers: NotRequired[
        "capo_appsync.types.additional_authentication_providers.AdditionalAuthenticationProviders"
    ]
    """<p>A list of additional authentication providers for the <code>GraphqlApi</code> API.</p>"""
    xray_enabled: "capo_appsync.types.boolean.Boolean"
    """<p>A flag indicating whether to use X-Ray tracing for the <code>GraphqlApi</code>.</p>"""
    lambda_authorizer_config: NotRequired[
        "capo_appsync.types.lambda_authorizer_config.LambdaAuthorizerConfig"
    ]
    """<p>Configuration for Lambda function authorization.</p>"""
    api_type: NotRequired["capo_appsync.types.graph_ql_api_type.GraphQLApiType"]
    """<p>The value that indicates whether the GraphQL API is a standard API (<code>GRAPHQL</code>) or merged API (<code>MERGED</code>).</p>"""
    merged_api_execution_role_arn: NotRequired["capo_appsync.types.string.String"]
    """<p>The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the <code>AUTO_MERGE</code> to update the merged API endpoint with the source API changes automatically.</p>"""
    visibility: NotRequired[
        "capo_appsync.types.graph_ql_api_visibility.GraphQLApiVisibility"
    ]
    """<p>Sets the value of the GraphQL API to public (<code>GLOBAL</code>) or private (<code>PRIVATE</code>). If no value is provided, the visibility will be set to <code>GLOBAL</code> by default. This value cannot be changed once the API has been created.</p>"""
    owner_contact: NotRequired["capo_appsync.types.string.String"]
    """<p>The owner contact information for an API resource.</p> <p>This field accepts any string input with a length of 0 - 256 characters.</p>"""
    introspection_config: NotRequired[
        "capo_appsync.types.graph_ql_api_introspection_config.GraphQLApiIntrospectionConfig"
    ]
    """<p>Sets the value of the GraphQL API to enable (<code>ENABLED</code>) or disable (<code>DISABLED</code>) introspection. If no value is provided, the introspection configuration will be set to <code>ENABLED</code> by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.</p> <p>For more information about introspection, see <a href="https://graphql.org/learn/introspection/">GraphQL introspection</a>.</p>"""
    query_depth_limit: "capo_appsync.types.query_depth_limit.QueryDepthLimit"
    """<p>The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query. The default value is <code>0</code> (or unspecified), which indicates there's no depth limit. If you set a limit, it can be between <code>1</code> and <code>75</code> nested levels. This field will produce a limit error if the operation falls out of bounds.</p> <p>Note that fields can still be set to nullable or non-nullable. If a non-nullable field produces an error, the error will be thrown upwards to the first nullable field available.</p>"""
    resolver_count_limit: "capo_appsync.types.resolver_count_limit.ResolverCountLimit"
    """<p>The maximum number of resolvers that can be invoked in a single request. The default value is <code>0</code> (or unspecified), which will set the limit to <code>10000</code>. When specified, the limit value can be between <code>1</code> and <code>10000</code>. This field will produce a limit error if the operation falls out of bounds.</p>"""
    enhanced_metrics_config: NotRequired[
        "capo_appsync.types.enhanced_metrics_config.EnhancedMetricsConfig"
    ]
    """<p>The <code>enhancedMetricsConfig</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphqlApiRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "log_config" in value:
        import capo_appsync.types.log_config

        out["logConfig"] = capo_appsync.types.log_config.serialize_json(
            value["log_config"]
        )
    import capo_appsync.types.authentication_type

    out["authenticationType"] = capo_appsync.types.authentication_type.serialize_json(
        value["authentication_type"]
    )
    if "user_pool_config" in value:
        import capo_appsync.types.user_pool_config

        out["userPoolConfig"] = capo_appsync.types.user_pool_config.serialize_json(
            value["user_pool_config"]
        )
    if "open_id_connect_config" in value:
        import capo_appsync.types.open_id_connect_config

        out["openIDConnectConfig"] = (
            capo_appsync.types.open_id_connect_config.serialize_json(
                value["open_id_connect_config"]
            )
        )
    if "tags" in value:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    if "additional_authentication_providers" in value:
        import capo_appsync.types.additional_authentication_providers

        out["additionalAuthenticationProviders"] = (
            capo_appsync.types.additional_authentication_providers.serialize_json(
                value["additional_authentication_providers"]
            )
        )
    out["xrayEnabled"] = value.get("xray_enabled", False)
    if "lambda_authorizer_config" in value:
        import capo_appsync.types.lambda_authorizer_config

        out["lambdaAuthorizerConfig"] = (
            capo_appsync.types.lambda_authorizer_config.serialize_json(
                value["lambda_authorizer_config"]
            )
        )
    if "api_type" in value:
        import capo_appsync.types.graph_ql_api_type

        out["apiType"] = capo_appsync.types.graph_ql_api_type.serialize_json(
            value["api_type"]
        )
    if "merged_api_execution_role_arn" in value:
        out["mergedApiExecutionRoleArn"] = value["merged_api_execution_role_arn"]
    if "visibility" in value:
        import capo_appsync.types.graph_ql_api_visibility

        out["visibility"] = capo_appsync.types.graph_ql_api_visibility.serialize_json(
            value["visibility"]
        )
    if "owner_contact" in value:
        out["ownerContact"] = value["owner_contact"]
    if "introspection_config" in value:
        import capo_appsync.types.graph_ql_api_introspection_config

        out["introspectionConfig"] = (
            capo_appsync.types.graph_ql_api_introspection_config.serialize_json(
                value["introspection_config"]
            )
        )
    out["queryDepthLimit"] = value.get("query_depth_limit", 0)
    out["resolverCountLimit"] = value.get("resolver_count_limit", 0)
    if "enhanced_metrics_config" in value:
        import capo_appsync.types.enhanced_metrics_config

        out["enhancedMetricsConfig"] = (
            capo_appsync.types.enhanced_metrics_config.serialize_json(
                value["enhanced_metrics_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGraphqlApiRequest:
    out: CreateGraphqlApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGraphqlApiRequest.name required")
    if data.get("logConfig") is not None:
        import capo_appsync.types.log_config

        out["log_config"] = capo_appsync.types.log_config.deserialize_json(
            data["logConfig"]
        )
    if data.get("authenticationType") is not None:
        import capo_appsync.types.authentication_type

        out["authentication_type"] = (
            capo_appsync.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateGraphqlApiRequest.authentication_type required"
        )
    if data.get("userPoolConfig") is not None:
        import capo_appsync.types.user_pool_config

        out["user_pool_config"] = capo_appsync.types.user_pool_config.deserialize_json(
            data["userPoolConfig"]
        )
    if data.get("openIDConnectConfig") is not None:
        import capo_appsync.types.open_id_connect_config

        out["open_id_connect_config"] = (
            capo_appsync.types.open_id_connect_config.deserialize_json(
                data["openIDConnectConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    if data.get("additionalAuthenticationProviders") is not None:
        import capo_appsync.types.additional_authentication_providers

        out["additional_authentication_providers"] = (
            capo_appsync.types.additional_authentication_providers.deserialize_json(
                data["additionalAuthenticationProviders"]
            )
        )
    if data.get("xrayEnabled") is not None:
        out["xray_enabled"] = data["xrayEnabled"]
    else:
        out["xray_enabled"] = False
    if data.get("lambdaAuthorizerConfig") is not None:
        import capo_appsync.types.lambda_authorizer_config

        out["lambda_authorizer_config"] = (
            capo_appsync.types.lambda_authorizer_config.deserialize_json(
                data["lambdaAuthorizerConfig"]
            )
        )
    if data.get("apiType") is not None:
        import capo_appsync.types.graph_ql_api_type

        out["api_type"] = capo_appsync.types.graph_ql_api_type.deserialize_json(
            data["apiType"]
        )
    if data.get("mergedApiExecutionRoleArn") is not None:
        out["merged_api_execution_role_arn"] = data["mergedApiExecutionRoleArn"]
    if data.get("visibility") is not None:
        import capo_appsync.types.graph_ql_api_visibility

        out["visibility"] = capo_appsync.types.graph_ql_api_visibility.deserialize_json(
            data["visibility"]
        )
    if data.get("ownerContact") is not None:
        out["owner_contact"] = data["ownerContact"]
    if data.get("introspectionConfig") is not None:
        import capo_appsync.types.graph_ql_api_introspection_config

        out["introspection_config"] = (
            capo_appsync.types.graph_ql_api_introspection_config.deserialize_json(
                data["introspectionConfig"]
            )
        )
    if data.get("queryDepthLimit") is not None:
        out["query_depth_limit"] = data["queryDepthLimit"]
    else:
        out["query_depth_limit"] = 0
    if data.get("resolverCountLimit") is not None:
        out["resolver_count_limit"] = data["resolverCountLimit"]
    else:
        out["resolver_count_limit"] = 0
    if data.get("enhancedMetricsConfig") is not None:
        import capo_appsync.types.enhanced_metrics_config

        out["enhanced_metrics_config"] = (
            capo_appsync.types.enhanced_metrics_config.deserialize_json(
                data["enhancedMetricsConfig"]
            )
        )
    return out

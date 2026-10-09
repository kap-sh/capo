"""Generated from Smithy shape ``com.amazonaws.appsync#AWSDeepdishControlPlaneService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_appsync._auth._signers
import capo_appsync._auth._sigv4
from capo_appsync._auth._identity import Credentials
from capo_appsync._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_appsync._auth._zapros_handler import AuthMiddleware
from capo_appsync._pagination import resolve_path as _resolve_path
from capo_appsync._services._aws_config import aws_config
from capo_appsync._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_appsync.types.additional_authentication_providers
    import capo_appsync.types.api
    import capo_appsync.types.api_cache_type
    import capo_appsync.types.api_caching_behavior
    import capo_appsync.types.api_key
    import capo_appsync.types.api_name
    import capo_appsync.types.app_sync_runtime
    import capo_appsync.types.associate_api_request
    import capo_appsync.types.associate_api_response
    import capo_appsync.types.associate_merged_graphql_api_request
    import capo_appsync.types.associate_merged_graphql_api_response
    import capo_appsync.types.associate_source_graphql_api_request
    import capo_appsync.types.associate_source_graphql_api_response
    import capo_appsync.types.auth_modes
    import capo_appsync.types.authentication_type
    import capo_appsync.types.blob
    import capo_appsync.types.boolean
    import capo_appsync.types.boolean_value
    import capo_appsync.types.cache_health_metrics_config
    import capo_appsync.types.caching_config
    import capo_appsync.types.certificate_arn
    import capo_appsync.types.channel_namespace
    import capo_appsync.types.code
    import capo_appsync.types.context
    import capo_appsync.types.create_api_cache_request
    import capo_appsync.types.create_api_cache_response
    import capo_appsync.types.create_api_key_request
    import capo_appsync.types.create_api_key_response
    import capo_appsync.types.create_api_request
    import capo_appsync.types.create_api_response
    import capo_appsync.types.create_channel_namespace_request
    import capo_appsync.types.create_channel_namespace_response
    import capo_appsync.types.create_data_source_request
    import capo_appsync.types.create_data_source_response
    import capo_appsync.types.create_domain_name_request
    import capo_appsync.types.create_domain_name_response
    import capo_appsync.types.create_function_request
    import capo_appsync.types.create_function_response
    import capo_appsync.types.create_graphql_api_request
    import capo_appsync.types.create_graphql_api_response
    import capo_appsync.types.create_resolver_request
    import capo_appsync.types.create_resolver_response
    import capo_appsync.types.create_type_request
    import capo_appsync.types.create_type_response
    import capo_appsync.types.data_source
    import capo_appsync.types.data_source_level_metrics_config
    import capo_appsync.types.data_source_type
    import capo_appsync.types.delete_api_cache_request
    import capo_appsync.types.delete_api_cache_response
    import capo_appsync.types.delete_api_key_request
    import capo_appsync.types.delete_api_key_response
    import capo_appsync.types.delete_api_request
    import capo_appsync.types.delete_api_response
    import capo_appsync.types.delete_channel_namespace_request
    import capo_appsync.types.delete_channel_namespace_response
    import capo_appsync.types.delete_data_source_request
    import capo_appsync.types.delete_data_source_response
    import capo_appsync.types.delete_domain_name_request
    import capo_appsync.types.delete_domain_name_response
    import capo_appsync.types.delete_function_request
    import capo_appsync.types.delete_function_response
    import capo_appsync.types.delete_graphql_api_request
    import capo_appsync.types.delete_graphql_api_response
    import capo_appsync.types.delete_resolver_request
    import capo_appsync.types.delete_resolver_response
    import capo_appsync.types.delete_type_request
    import capo_appsync.types.delete_type_response
    import capo_appsync.types.description
    import capo_appsync.types.disassociate_api_request
    import capo_appsync.types.disassociate_api_response
    import capo_appsync.types.disassociate_merged_graphql_api_request
    import capo_appsync.types.disassociate_merged_graphql_api_response
    import capo_appsync.types.disassociate_source_graphql_api_request
    import capo_appsync.types.disassociate_source_graphql_api_response
    import capo_appsync.types.domain_name
    import capo_appsync.types.domain_name_config
    import capo_appsync.types.dynamodb_data_source_config
    import capo_appsync.types.elasticsearch_data_source_config
    import capo_appsync.types.enhanced_metrics_config
    import capo_appsync.types.environment_variable_map
    import capo_appsync.types.evaluate_code_request
    import capo_appsync.types.evaluate_code_response
    import capo_appsync.types.evaluate_mapping_template_request
    import capo_appsync.types.evaluate_mapping_template_response
    import capo_appsync.types.event_bridge_data_source_config
    import capo_appsync.types.event_config
    import capo_appsync.types.flush_api_cache_request
    import capo_appsync.types.flush_api_cache_response
    import capo_appsync.types.function_configuration
    import capo_appsync.types.get_api_association_request
    import capo_appsync.types.get_api_association_response
    import capo_appsync.types.get_api_cache_request
    import capo_appsync.types.get_api_cache_response
    import capo_appsync.types.get_api_request
    import capo_appsync.types.get_api_response
    import capo_appsync.types.get_channel_namespace_request
    import capo_appsync.types.get_channel_namespace_response
    import capo_appsync.types.get_data_source_introspection_request
    import capo_appsync.types.get_data_source_introspection_response
    import capo_appsync.types.get_data_source_request
    import capo_appsync.types.get_data_source_response
    import capo_appsync.types.get_domain_name_request
    import capo_appsync.types.get_domain_name_response
    import capo_appsync.types.get_function_request
    import capo_appsync.types.get_function_response
    import capo_appsync.types.get_graphql_api_environment_variables_request
    import capo_appsync.types.get_graphql_api_environment_variables_response
    import capo_appsync.types.get_graphql_api_request
    import capo_appsync.types.get_graphql_api_response
    import capo_appsync.types.get_introspection_schema_request
    import capo_appsync.types.get_introspection_schema_response
    import capo_appsync.types.get_resolver_request
    import capo_appsync.types.get_resolver_response
    import capo_appsync.types.get_schema_creation_status_request
    import capo_appsync.types.get_schema_creation_status_response
    import capo_appsync.types.get_source_api_association_request
    import capo_appsync.types.get_source_api_association_response
    import capo_appsync.types.get_type_request
    import capo_appsync.types.get_type_response
    import capo_appsync.types.graph_ql_api_introspection_config
    import capo_appsync.types.graph_ql_api_type
    import capo_appsync.types.graph_ql_api_visibility
    import capo_appsync.types.graphql_api
    import capo_appsync.types.handler_configs
    import capo_appsync.types.http_data_source_config
    import capo_appsync.types.lambda_authorizer_config
    import capo_appsync.types.lambda_data_source_config
    import capo_appsync.types.list_api_keys_request
    import capo_appsync.types.list_api_keys_response
    import capo_appsync.types.list_apis_request
    import capo_appsync.types.list_apis_response
    import capo_appsync.types.list_channel_namespaces_request
    import capo_appsync.types.list_channel_namespaces_response
    import capo_appsync.types.list_data_sources_request
    import capo_appsync.types.list_data_sources_response
    import capo_appsync.types.list_domain_names_request
    import capo_appsync.types.list_domain_names_response
    import capo_appsync.types.list_functions_request
    import capo_appsync.types.list_functions_response
    import capo_appsync.types.list_graphql_apis_request
    import capo_appsync.types.list_graphql_apis_response
    import capo_appsync.types.list_resolvers_by_function_request
    import capo_appsync.types.list_resolvers_by_function_response
    import capo_appsync.types.list_resolvers_request
    import capo_appsync.types.list_resolvers_response
    import capo_appsync.types.list_source_api_associations_request
    import capo_appsync.types.list_source_api_associations_response
    import capo_appsync.types.list_tags_for_resource_request
    import capo_appsync.types.list_tags_for_resource_response
    import capo_appsync.types.list_types_by_association_request
    import capo_appsync.types.list_types_by_association_response
    import capo_appsync.types.list_types_request
    import capo_appsync.types.list_types_response
    import capo_appsync.types.log_config
    import capo_appsync.types.long
    import capo_appsync.types.mapping_template
    import capo_appsync.types.max_batch_size
    import capo_appsync.types.max_results
    import capo_appsync.types.namespace
    import capo_appsync.types.open_id_connect_config
    import capo_appsync.types.open_search_service_data_source_config
    import capo_appsync.types.output_type
    import capo_appsync.types.ownership
    import capo_appsync.types.pagination_token
    import capo_appsync.types.pipeline_config
    import capo_appsync.types.put_graphql_api_environment_variables_request
    import capo_appsync.types.put_graphql_api_environment_variables_response
    import capo_appsync.types.query_depth_limit
    import capo_appsync.types.rds_data_api_config
    import capo_appsync.types.relational_database_data_source_config
    import capo_appsync.types.resolver
    import capo_appsync.types.resolver_count_limit
    import capo_appsync.types.resolver_kind
    import capo_appsync.types.resolver_level_metrics_config
    import capo_appsync.types.resource_arn
    import capo_appsync.types.resource_name
    import capo_appsync.types.source_api_association_config
    import capo_appsync.types.source_api_association_summary
    import capo_appsync.types.start_data_source_introspection_request
    import capo_appsync.types.start_data_source_introspection_response
    import capo_appsync.types.start_schema_creation_request
    import capo_appsync.types.start_schema_creation_response
    import capo_appsync.types.start_schema_merge_request
    import capo_appsync.types.start_schema_merge_response
    import capo_appsync.types.string
    import capo_appsync.types.sync_config
    import capo_appsync.types.tag_key_list
    import capo_appsync.types.tag_map
    import capo_appsync.types.tag_resource_request
    import capo_appsync.types.tag_resource_response
    import capo_appsync.types.template
    import capo_appsync.types.type
    import capo_appsync.types.type_definition_format
    import capo_appsync.types.untag_resource_request
    import capo_appsync.types.untag_resource_response
    import capo_appsync.types.update_api_cache_request
    import capo_appsync.types.update_api_cache_response
    import capo_appsync.types.update_api_key_request
    import capo_appsync.types.update_api_key_response
    import capo_appsync.types.update_api_request
    import capo_appsync.types.update_api_response
    import capo_appsync.types.update_channel_namespace_request
    import capo_appsync.types.update_channel_namespace_response
    import capo_appsync.types.update_data_source_request
    import capo_appsync.types.update_data_source_response
    import capo_appsync.types.update_domain_name_request
    import capo_appsync.types.update_domain_name_response
    import capo_appsync.types.update_function_request
    import capo_appsync.types.update_function_response
    import capo_appsync.types.update_graphql_api_request
    import capo_appsync.types.update_graphql_api_response
    import capo_appsync.types.update_resolver_request
    import capo_appsync.types.update_resolver_response
    import capo_appsync.types.update_source_api_association_request
    import capo_appsync.types.update_source_api_association_response
    import capo_appsync.types.update_type_request
    import capo_appsync.types.update_type_response
    import capo_appsync.types.user_pool_config


class AppSyncClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AppSyncClient:
    """A client for the ``AppSync`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = AppSyncClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AppSyncClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AppSyncClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def associate_api(
        self,
        domain_name: "capo_appsync.types.domain_name.DomainName",
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.associate_api_response.AssociateApiResponse":
        """<p>Maps an endpoint to your custom domain.</p>

        Args:
            domain_name: <p>The domain name.</p>
            api_id: <p>The API ID. Private APIs can not be associated with custom domains.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.associate_api_request.AssociateApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.associate_api_response.AssociateApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.associate_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.associate_api.associate_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.associate_api_request.AssociateApiRequest = {
            "domain_name": domain_name,
            "api_id": api_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_merged_graphql_api(
        self,
        source_api_identifier: "capo_appsync.types.string.String",
        merged_api_identifier: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        source_api_association_config: Optional[
            "capo_appsync.types.source_api_association_config.SourceApiAssociationConfig"
        ] = None,
    ) -> "capo_appsync.types.associate_merged_graphql_api_response.AssociateMergedGraphqlApiResponse":
        """<p>Creates an association between a Merged API and source API using the source API's identifier.</p>

        Args:
            source_api_identifier: <p>The identifier of the AppSync Source API. This is generated by the AppSync service. In most cases, source APIs (especially in your account) only require the API ID value or ARN of the source API. However, source APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the source API.</p>
            merged_api_identifier: <p>The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs in other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.</p>
            description: <p>The description field.</p>
            source_api_association_config: <p>The <code>SourceApiAssociationConfig</code> object data.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.associate_merged_graphql_api_request.AssociateMergedGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.associate_merged_graphql_api_response.AssociateMergedGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.associate_merged_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.associate_merged_graphql_api.associate_merged_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.associate_merged_graphql_api_request.AssociateMergedGraphqlApiRequest = {
            "source_api_identifier": source_api_identifier,
            "merged_api_identifier": merged_api_identifier,
        }
        if description is not None:
            input_["description"] = description
        if source_api_association_config is not None:
            input_["source_api_association_config"] = source_api_association_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_source_graphql_api(
        self,
        merged_api_identifier: "capo_appsync.types.string.String",
        source_api_identifier: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        source_api_association_config: Optional[
            "capo_appsync.types.source_api_association_config.SourceApiAssociationConfig"
        ] = None,
    ) -> "capo_appsync.types.associate_source_graphql_api_response.AssociateSourceGraphqlApiResponse":
        """<p>Creates an association between a Merged API and source API using the Merged API's identifier.</p>

        Args:
            merged_api_identifier: <p>The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs in other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.</p>
            source_api_identifier: <p>The identifier of the AppSync Source API. This is generated by the AppSync service. In most cases, source APIs (especially in your account) only require the API ID value or ARN of the source API. However, source APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the source API.</p>
            description: <p>The description field.</p>
            source_api_association_config: <p>The <code>SourceApiAssociationConfig</code> object data.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.associate_source_graphql_api_request.AssociateSourceGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.associate_source_graphql_api_response.AssociateSourceGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.associate_source_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.associate_source_graphql_api.associate_source_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.associate_source_graphql_api_request.AssociateSourceGraphqlApiRequest = {
            "merged_api_identifier": merged_api_identifier,
            "source_api_identifier": source_api_identifier,
        }
        if description is not None:
            input_["description"] = description
        if source_api_association_config is not None:
            input_["source_api_association_config"] = source_api_association_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_api(
        self,
        name: "capo_appsync.types.api_name.ApiName",
        event_config: "capo_appsync.types.event_config.EventConfig",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        owner_contact: Optional["capo_appsync.types.string.String"] = None,
        tags: Optional["capo_appsync.types.tag_map.TagMap"] = None,
    ) -> "capo_appsync.types.create_api_response.CreateApiResponse":
        """<p>Creates an <code>Api</code> object. Use this operation to create an AppSync API with your preferred configuration, such as an Event API that provides real-time message publishing and message subscriptions over WebSockets.</p>

        Args:
            name: <p>The name for the <code>Api</code>.</p>
            owner_contact: <p>The owner contact information for the <code>Api</code>.</p>
            event_config: <p>The Event API configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_api_request.CreateApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_api_response.CreateApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_api.create_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_api_request.CreateApiRequest = {
            "name": name,
            "event_config": event_config,
        }
        if owner_contact is not None:
            input_["owner_contact"] = owner_contact
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_api_cache(
        self,
        api_id: "capo_appsync.types.string.String",
        ttl: "capo_appsync.types.long.Long",
        api_caching_behavior: "capo_appsync.types.api_caching_behavior.ApiCachingBehavior",
        type: "capo_appsync.types.api_cache_type.ApiCacheType",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        transit_encryption_enabled: Optional[
            "capo_appsync.types.boolean.Boolean"
        ] = None,
        at_rest_encryption_enabled: Optional[
            "capo_appsync.types.boolean.Boolean"
        ] = None,
        health_metrics_config: Optional[
            "capo_appsync.types.cache_health_metrics_config.CacheHealthMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.create_api_cache_response.CreateApiCacheResponse":
        """<p>Creates a cache for the GraphQL API.</p>

        Args:
            api_id: <p>The GraphQL API ID.</p>
            ttl: <p>TTL in seconds for cache entries.</p> <p>Valid values are 1–3,600 seconds.</p>
            transit_encryption_enabled: <p>Transit encryption flag when connecting to cache. You cannot update this setting after creation.</p>
            at_rest_encryption_enabled: <p>At-rest encryption flag for cache. You cannot update this setting after creation.</p>
            api_caching_behavior: <p>Caching behavior.</p> <ul> <li> <p> <b>FULL_REQUEST_CACHING</b>: All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.</p> </li> <li> <p> <b>PER_RESOLVER_CACHING</b>: Individual resolvers that you specify are cached.</p> </li> <li> <p> <b>OPERATION_LEVEL_CACHING</b>: Full requests are cached together and returned without executing resolvers.</p> </li> </ul>
            type: <p>The cache instance type. Valid values are </p> <ul> <li> <p> <code>SMALL</code> </p> </li> <li> <p> <code>MEDIUM</code> </p> </li> <li> <p> <code>LARGE</code> </p> </li> <li> <p> <code>XLARGE</code> </p> </li> <li> <p> <code>LARGE_2X</code> </p> </li> <li> <p> <code>LARGE_4X</code> </p> </li> <li> <p> <code>LARGE_8X</code> (not available in all regions)</p> </li> <li> <p> <code>LARGE_12X</code> </p> </li> </ul> <p>Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.</p> <p>The following legacy instance types are available, but their use is discouraged:</p> <ul> <li> <p> <b>T2_SMALL</b>: A t2.small instance type.</p> </li> <li> <p> <b>T2_MEDIUM</b>: A t2.medium instance type.</p> </li> <li> <p> <b>R4_LARGE</b>: A r4.large instance type.</p> </li> <li> <p> <b>R4_XLARGE</b>: A r4.xlarge instance type.</p> </li> <li> <p> <b>R4_2XLARGE</b>: A r4.2xlarge instance type.</p> </li> <li> <p> <b>R4_4XLARGE</b>: A r4.4xlarge instance type.</p> </li> <li> <p> <b>R4_8XLARGE</b>: A r4.8xlarge instance type.</p> </li> </ul>
            health_metrics_config: <p>Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:</p> <ul> <li> <p>NetworkBandwidthOutAllowanceExceeded: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> <li> <p>EngineCPUUtilization: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> </ul> <p>Metrics will be recorded by API ID. You can set the value to <code>ENABLED</code> or <code>DISABLED</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_api_cache_request.CreateApiCacheRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_api_cache_response.CreateApiCacheResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_api_cache

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_api_cache.create_api_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_api_cache_request.CreateApiCacheRequest = {
            "api_id": api_id,
            "ttl": ttl,
            "api_caching_behavior": api_caching_behavior,
            "type": type,
        }
        if transit_encryption_enabled is not None:
            input_["transit_encryption_enabled"] = transit_encryption_enabled
        if at_rest_encryption_enabled is not None:
            input_["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if health_metrics_config is not None:
            input_["health_metrics_config"] = health_metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_api_key(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        expires: Optional["capo_appsync.types.long.Long"] = None,
    ) -> "capo_appsync.types.create_api_key_response.CreateApiKeyResponse":
        """<p>Creates a unique key that you can distribute to clients who invoke your API.</p>

        Args:
            api_id: <p>The ID for your GraphQL API.</p>
            description: <p>A description of the purpose of the API key.</p>
            expires: <p>From the creation time, the time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour. The default value for this parameter is 7 days from creation time. For more information, see .</p>

        Raises:
            capo_appsync.errors.api_key_limit_exceeded_exception.ApiKeyLimitExceededException: <p>The API key exceeded a limit. Try your request again.</p>
            capo_appsync.errors.api_key_validity_out_of_bounds_exception.ApiKeyValidityOutOfBoundsException: <p>The API key expiration must be set to a value between 1 and 365 days from creation (for <code>CreateApiKey</code>) or from update (for <code>UpdateApiKey</code>).</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_api_key_request.CreateApiKeyRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_api_key_response.CreateApiKeyResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_api_key

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_api_key.create_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_api_key_request.CreateApiKeyRequest = {
            "api_id": api_id
        }
        if description is not None:
            input_["description"] = description
        if expires is not None:
            input_["expires"] = expires

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel_namespace(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.namespace.Namespace",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        subscribe_auth_modes: Optional[
            "capo_appsync.types.auth_modes.AuthModes"
        ] = None,
        publish_auth_modes: Optional["capo_appsync.types.auth_modes.AuthModes"] = None,
        code_handlers: Optional["capo_appsync.types.code.Code"] = None,
        tags: Optional["capo_appsync.types.tag_map.TagMap"] = None,
        handler_configs: Optional[
            "capo_appsync.types.handler_configs.HandlerConfigs"
        ] = None,
    ) -> "capo_appsync.types.create_channel_namespace_response.CreateChannelNamespaceResponse":
        """<p>Creates a <code>ChannelNamespace</code> for an <code>Api</code>.</p>

        Args:
            api_id: <p>The <code>Api</code> ID.</p>
            name: <p>The name of the <code>ChannelNamespace</code>. This name must be unique within the <code>Api</code> </p>
            subscribe_auth_modes: <p>The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>
            publish_auth_modes: <p>The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>
            code_handlers: <p>The event handler functions that run custom business logic to process published events and subscribe requests.</p>
            handler_configs: <p>The configuration for the <code>OnPublish</code> and <code>OnSubscribe</code> handlers.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.conflict_exception.ConflictException: <p>A conflict with a previous successful update is detected. This typically occurs when the previous update did not have time to propagate before the next update was made. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation exceeded the service quota for this resource.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_channel_namespace_request.CreateChannelNamespaceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_channel_namespace_response.CreateChannelNamespaceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_channel_namespace

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_channel_namespace.create_channel_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_channel_namespace_request.CreateChannelNamespaceRequest = {
            "api_id": api_id,
            "name": name,
        }
        if subscribe_auth_modes is not None:
            input_["subscribe_auth_modes"] = subscribe_auth_modes
        if publish_auth_modes is not None:
            input_["publish_auth_modes"] = publish_auth_modes
        if code_handlers is not None:
            input_["code_handlers"] = code_handlers
        if tags is not None:
            input_["tags"] = tags
        if handler_configs is not None:
            input_["handler_configs"] = handler_configs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_source(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.resource_name.ResourceName",
        type: "capo_appsync.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        service_role_arn: Optional["capo_appsync.types.string.String"] = None,
        dynamodb_config: Optional[
            "capo_appsync.types.dynamodb_data_source_config.DynamodbDataSourceConfig"
        ] = None,
        lambda_config: Optional[
            "capo_appsync.types.lambda_data_source_config.LambdaDataSourceConfig"
        ] = None,
        elasticsearch_config: Optional[
            "capo_appsync.types.elasticsearch_data_source_config.ElasticsearchDataSourceConfig"
        ] = None,
        open_search_service_config: Optional[
            "capo_appsync.types.open_search_service_data_source_config.OpenSearchServiceDataSourceConfig"
        ] = None,
        http_config: Optional[
            "capo_appsync.types.http_data_source_config.HttpDataSourceConfig"
        ] = None,
        relational_database_config: Optional[
            "capo_appsync.types.relational_database_data_source_config.RelationalDatabaseDataSourceConfig"
        ] = None,
        event_bridge_config: Optional[
            "capo_appsync.types.event_bridge_data_source_config.EventBridgeDataSourceConfig"
        ] = None,
        metrics_config: Optional[
            "capo_appsync.types.data_source_level_metrics_config.DataSourceLevelMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.create_data_source_response.CreateDataSourceResponse":
        """<p>Creates a <code>DataSource</code> object.</p>

        Args:
            api_id: <p>The API ID for the GraphQL API for the <code>DataSource</code>.</p>
            name: <p>A user-supplied name for the <code>DataSource</code>.</p>
            description: <p>A description of the <code>DataSource</code>.</p>
            type: <p>The type of the <code>DataSource</code>.</p>
            service_role_arn: <p>The Identity and Access Management (IAM) service role Amazon Resource Name (ARN) for the data source. The system assumes this role when accessing the data source.</p>
            dynamodb_config: <p>Amazon DynamoDB settings.</p>
            lambda_config: <p>Lambda settings.</p>
            elasticsearch_config: <p>Amazon OpenSearch Service settings.</p> <p>As of September 2021, Amazon Elasticsearch service is Amazon OpenSearch Service. This configuration is deprecated. For new data sources, use <a>CreateDataSourceRequest$openSearchServiceConfig</a> to create an OpenSearch data source.</p>
            open_search_service_config: <p>Amazon OpenSearch Service settings.</p>
            http_config: <p>HTTP endpoint settings.</p>
            relational_database_config: <p>Relational database settings.</p>
            event_bridge_config: <p>Amazon EventBridge settings.</p>
            metrics_config: <p>Enables or disables enhanced data source metrics for specified data sources. Note that <code>metricsConfig</code> won't be used unless the <code>dataSourceLevelMetricsBehavior</code> value is set to <code>PER_DATA_SOURCE_METRICS</code>. If the <code>dataSourceLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_DATA_SOURCE_METRICS</code> instead, <code>metricsConfig</code> will be ignored. However, you can still set its value.</p> <p> <code>metricsConfig</code> can be <code>ENABLED</code> or <code>DISABLED</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_data_source_request.CreateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_data_source_response.CreateDataSourceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_data_source

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_data_source.create_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_data_source_request.CreateDataSourceRequest = {
            "api_id": api_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if service_role_arn is not None:
            input_["service_role_arn"] = service_role_arn
        if dynamodb_config is not None:
            input_["dynamodb_config"] = dynamodb_config
        if lambda_config is not None:
            input_["lambda_config"] = lambda_config
        if elasticsearch_config is not None:
            input_["elasticsearch_config"] = elasticsearch_config
        if open_search_service_config is not None:
            input_["open_search_service_config"] = open_search_service_config
        if http_config is not None:
            input_["http_config"] = http_config
        if relational_database_config is not None:
            input_["relational_database_config"] = relational_database_config
        if event_bridge_config is not None:
            input_["event_bridge_config"] = event_bridge_config
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain_name(
        self,
        domain_name: "capo_appsync.types.domain_name.DomainName",
        certificate_arn: "capo_appsync.types.certificate_arn.CertificateArn",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.description.Description"] = None,
        tags: Optional["capo_appsync.types.tag_map.TagMap"] = None,
    ) -> "capo_appsync.types.create_domain_name_response.CreateDomainNameResponse":
        """<p>Creates a custom <code>DomainName</code> object.</p>

        Args:
            domain_name: <p>The domain name.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate. This can be an Certificate Manager (ACM) certificate or an Identity and Access Management (IAM) server certificate.</p>
            description: <p>A description of the <code>DomainName</code>.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_domain_name_request.CreateDomainNameRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_domain_name_response.CreateDomainNameResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_domain_name

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_domain_name.create_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_domain_name_request.CreateDomainNameRequest = {
            "domain_name": domain_name,
            "certificate_arn": certificate_arn,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_function(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.resource_name.ResourceName",
        data_source_name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        request_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        response_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        function_version: Optional["capo_appsync.types.string.String"] = None,
        sync_config: Optional["capo_appsync.types.sync_config.SyncConfig"] = None,
        max_batch_size: Optional[
            "capo_appsync.types.max_batch_size.MaxBatchSize"
        ] = None,
        runtime: Optional["capo_appsync.types.app_sync_runtime.AppSyncRuntime"] = None,
        code: Optional["capo_appsync.types.code.Code"] = None,
    ) -> "capo_appsync.types.create_function_response.CreateFunctionResponse":
        """<p>Creates a <code>Function</code> object.</p> <p>A function is a reusable entity. You can use multiple functions to compose the resolver logic.</p>

        Args:
            api_id: <p>The GraphQL API ID.</p>
            name: <p>The <code>Function</code> name. The function name does not have to be unique.</p>
            description: <p>The <code>Function</code> description.</p>
            data_source_name: <p>The <code>Function</code> <code>DataSource</code> name.</p>
            request_mapping_template: <p>The <code>Function</code> request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p>
            response_mapping_template: <p>The <code>Function</code> response mapping template.</p>
            function_version: <p>The <code>version</code> of the request mapping template. Currently, the supported value is 2018-05-29. Note that when using VTL and mapping templates, the <code>functionVersion</code> is required.</p>
            max_batch_size: <p>The maximum batching size for a resolver.</p>
            code: <p>The <code>function</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_function_request.CreateFunctionRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_function_response.CreateFunctionResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_function

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_function.create_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_function_request.CreateFunctionRequest = {
            "api_id": api_id,
            "name": name,
            "data_source_name": data_source_name,
        }
        if description is not None:
            input_["description"] = description
        if request_mapping_template is not None:
            input_["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            input_["response_mapping_template"] = response_mapping_template
        if function_version is not None:
            input_["function_version"] = function_version
        if sync_config is not None:
            input_["sync_config"] = sync_config
        if max_batch_size is not None:
            input_["max_batch_size"] = max_batch_size
        if runtime is not None:
            input_["runtime"] = runtime
        if code is not None:
            input_["code"] = code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_graphql_api(
        self,
        name: "capo_appsync.types.string.String",
        authentication_type: "capo_appsync.types.authentication_type.AuthenticationType",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        log_config: Optional["capo_appsync.types.log_config.LogConfig"] = None,
        user_pool_config: Optional[
            "capo_appsync.types.user_pool_config.UserPoolConfig"
        ] = None,
        open_id_connect_config: Optional[
            "capo_appsync.types.open_id_connect_config.OpenIDConnectConfig"
        ] = None,
        tags: Optional["capo_appsync.types.tag_map.TagMap"] = None,
        additional_authentication_providers: Optional[
            "capo_appsync.types.additional_authentication_providers.AdditionalAuthenticationProviders"
        ] = None,
        xray_enabled: Optional["capo_appsync.types.boolean.Boolean"] = None,
        lambda_authorizer_config: Optional[
            "capo_appsync.types.lambda_authorizer_config.LambdaAuthorizerConfig"
        ] = None,
        api_type: Optional[
            "capo_appsync.types.graph_ql_api_type.GraphQLApiType"
        ] = None,
        merged_api_execution_role_arn: Optional[
            "capo_appsync.types.string.String"
        ] = None,
        visibility: Optional[
            "capo_appsync.types.graph_ql_api_visibility.GraphQLApiVisibility"
        ] = None,
        owner_contact: Optional["capo_appsync.types.string.String"] = None,
        introspection_config: Optional[
            "capo_appsync.types.graph_ql_api_introspection_config.GraphQLApiIntrospectionConfig"
        ] = None,
        query_depth_limit: Optional[
            "capo_appsync.types.query_depth_limit.QueryDepthLimit"
        ] = None,
        resolver_count_limit: Optional[
            "capo_appsync.types.resolver_count_limit.ResolverCountLimit"
        ] = None,
        enhanced_metrics_config: Optional[
            "capo_appsync.types.enhanced_metrics_config.EnhancedMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.create_graphql_api_response.CreateGraphqlApiResponse":
        """<p>Creates a <code>GraphqlApi</code> object.</p>

        Args:
            name: <p>A user-supplied name for the <code>GraphqlApi</code>.</p>
            log_config: <p>The Amazon CloudWatch Logs configuration.</p>
            authentication_type: <p>The authentication type: API key, Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda.</p>
            user_pool_config: <p>The Amazon Cognito user pool configuration.</p>
            open_id_connect_config: <p>The OIDC configuration.</p>
            tags: <p>A <code>TagMap</code> object.</p>
            additional_authentication_providers: <p>A list of additional authentication providers for the <code>GraphqlApi</code> API.</p>
            xray_enabled: <p>A flag indicating whether to use X-Ray tracing for the <code>GraphqlApi</code>.</p>
            lambda_authorizer_config: <p>Configuration for Lambda function authorization.</p>
            api_type: <p>The value that indicates whether the GraphQL API is a standard API (<code>GRAPHQL</code>) or merged API (<code>MERGED</code>).</p>
            merged_api_execution_role_arn: <p>The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the <code>AUTO_MERGE</code> to update the merged API endpoint with the source API changes automatically.</p>
            visibility: <p>Sets the value of the GraphQL API to public (<code>GLOBAL</code>) or private (<code>PRIVATE</code>). If no value is provided, the visibility will be set to <code>GLOBAL</code> by default. This value cannot be changed once the API has been created.</p>
            owner_contact: <p>The owner contact information for an API resource.</p> <p>This field accepts any string input with a length of 0 - 256 characters.</p>
            introspection_config: <p>Sets the value of the GraphQL API to enable (<code>ENABLED</code>) or disable (<code>DISABLED</code>) introspection. If no value is provided, the introspection configuration will be set to <code>ENABLED</code> by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.</p> <p>For more information about introspection, see <a href="https://graphql.org/learn/introspection/">GraphQL introspection</a>.</p>
            query_depth_limit: <p>The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query. The default value is <code>0</code> (or unspecified), which indicates there's no depth limit. If you set a limit, it can be between <code>1</code> and <code>75</code> nested levels. This field will produce a limit error if the operation falls out of bounds.</p> <p>Note that fields can still be set to nullable or non-nullable. If a non-nullable field produces an error, the error will be thrown upwards to the first nullable field available.</p>
            resolver_count_limit: <p>The maximum number of resolvers that can be invoked in a single request. The default value is <code>0</code> (or unspecified), which will set the limit to <code>10000</code>. When specified, the limit value can be between <code>1</code> and <code>10000</code>. This field will produce a limit error if the operation falls out of bounds.</p>
            enhanced_metrics_config: <p>The <code>enhancedMetricsConfig</code> object.</p>

        Raises:
            capo_appsync.errors.api_limit_exceeded_exception.ApiLimitExceededException: <p>The GraphQL API exceeded a limit. Try your request again.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_graphql_api_request.CreateGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_graphql_api_response.CreateGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_graphql_api.create_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_graphql_api_request.CreateGraphqlApiRequest = {
            "name": name,
            "authentication_type": authentication_type,
        }
        if log_config is not None:
            input_["log_config"] = log_config
        if user_pool_config is not None:
            input_["user_pool_config"] = user_pool_config
        if open_id_connect_config is not None:
            input_["open_id_connect_config"] = open_id_connect_config
        if tags is not None:
            input_["tags"] = tags
        if additional_authentication_providers is not None:
            input_["additional_authentication_providers"] = (
                additional_authentication_providers
            )
        if xray_enabled is not None:
            input_["xray_enabled"] = xray_enabled
        if lambda_authorizer_config is not None:
            input_["lambda_authorizer_config"] = lambda_authorizer_config
        if api_type is not None:
            input_["api_type"] = api_type
        if merged_api_execution_role_arn is not None:
            input_["merged_api_execution_role_arn"] = merged_api_execution_role_arn
        if visibility is not None:
            input_["visibility"] = visibility
        if owner_contact is not None:
            input_["owner_contact"] = owner_contact
        if introspection_config is not None:
            input_["introspection_config"] = introspection_config
        if query_depth_limit is not None:
            input_["query_depth_limit"] = query_depth_limit
        if resolver_count_limit is not None:
            input_["resolver_count_limit"] = resolver_count_limit
        if enhanced_metrics_config is not None:
            input_["enhanced_metrics_config"] = enhanced_metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_resolver(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.resource_name.ResourceName",
        field_name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        data_source_name: Optional[
            "capo_appsync.types.resource_name.ResourceName"
        ] = None,
        request_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        response_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        kind: Optional["capo_appsync.types.resolver_kind.ResolverKind"] = None,
        pipeline_config: Optional[
            "capo_appsync.types.pipeline_config.PipelineConfig"
        ] = None,
        sync_config: Optional["capo_appsync.types.sync_config.SyncConfig"] = None,
        caching_config: Optional[
            "capo_appsync.types.caching_config.CachingConfig"
        ] = None,
        max_batch_size: Optional[
            "capo_appsync.types.max_batch_size.MaxBatchSize"
        ] = None,
        runtime: Optional["capo_appsync.types.app_sync_runtime.AppSyncRuntime"] = None,
        code: Optional["capo_appsync.types.code.Code"] = None,
        metrics_config: Optional[
            "capo_appsync.types.resolver_level_metrics_config.ResolverLevelMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.create_resolver_response.CreateResolverResponse":
        """<p>Creates a <code>Resolver</code> object.</p> <p>A resolver converts incoming requests into a format that a data source can understand, and converts the data source's responses into GraphQL.</p>

        Args:
            api_id: <p>The ID for the GraphQL API for which the resolver is being created.</p>
            type_name: <p>The name of the <code>Type</code>.</p>
            field_name: <p>The name of the field to attach the resolver to.</p>
            data_source_name: <p>The name of the data source for which the resolver is being created.</p>
            request_mapping_template: <p>The mapping template to use for requests.</p> <p>A resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).</p> <p>VTL request mapping templates are optional when using an Lambda data source. For all other data sources, VTL request and response mapping templates are required.</p>
            response_mapping_template: <p>The mapping template to use for responses from the data source.</p>
            kind: <p>The resolver type.</p> <ul> <li> <p> <b>UNIT</b>: A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.</p> </li> <li> <p> <b>PIPELINE</b>: A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of <code>Function</code> objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.</p> </li> </ul>
            pipeline_config: <p>The <code>PipelineConfig</code>.</p>
            sync_config: <p>The <code>SyncConfig</code> for a resolver attached to a versioned data source.</p>
            caching_config: <p>The caching configuration for the resolver.</p>
            max_batch_size: <p>The maximum batching size for a resolver.</p>
            code: <p>The <code>resolver</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>
            metrics_config: <p>Enables or disables enhanced resolver metrics for specified resolvers. Note that <code>metricsConfig</code> won't be used unless the <code>resolverLevelMetricsBehavior</code> value is set to <code>PER_RESOLVER_METRICS</code>. If the <code>resolverLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_RESOLVER_METRICS</code> instead, <code>metricsConfig</code> will be ignored. However, you can still set its value.</p> <p> <code>metricsConfig</code> can be <code>ENABLED</code> or <code>DISABLED</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_resolver_request.CreateResolverRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_resolver_response.CreateResolverResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_resolver

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_resolver.create_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_resolver_request.CreateResolverRequest = {
            "api_id": api_id,
            "type_name": type_name,
            "field_name": field_name,
        }
        if data_source_name is not None:
            input_["data_source_name"] = data_source_name
        if request_mapping_template is not None:
            input_["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            input_["response_mapping_template"] = response_mapping_template
        if kind is not None:
            input_["kind"] = kind
        if pipeline_config is not None:
            input_["pipeline_config"] = pipeline_config
        if sync_config is not None:
            input_["sync_config"] = sync_config
        if caching_config is not None:
            input_["caching_config"] = caching_config
        if max_batch_size is not None:
            input_["max_batch_size"] = max_batch_size
        if runtime is not None:
            input_["runtime"] = runtime
        if code is not None:
            input_["code"] = code
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_type(
        self,
        api_id: "capo_appsync.types.string.String",
        definition: "capo_appsync.types.string.String",
        format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.create_type_response.CreateTypeResponse":
        """<p>Creates a <code>Type</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            definition: <p>The type definition, in GraphQL Schema Definition Language (SDL) format.</p> <p>For more information, see the <a href="http://graphql.org/learn/schema/">GraphQL SDL documentation</a>.</p>
            format: <p>The type format: SDL or JSON.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.create_type_request.CreateTypeRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.create_type_response.CreateTypeResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.create_type

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.create_type.create_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.create_type_request.CreateTypeRequest = {
            "api_id": api_id,
            "definition": definition,
            "format": format,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_api(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_api_response.DeleteApiResponse":
        """<p>Deletes an <code>Api</code> object</p>

        Args:
            api_id: <p>The <code>Api</code> ID.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_api_request.DeleteApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_api_response.DeleteApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_api.delete_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_api_request.DeleteApiRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_api_cache(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_api_cache_response.DeleteApiCacheResponse":
        """<p>Deletes an <code>ApiCache</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_api_cache_request.DeleteApiCacheRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_api_cache_response.DeleteApiCacheResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_api_cache

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_api_cache.delete_api_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_api_cache_request.DeleteApiCacheRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_api_key(
        self,
        api_id: "capo_appsync.types.string.String",
        id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_api_key_response.DeleteApiKeyResponse":
        """<p>Deletes an API key.</p>

        Args:
            api_id: <p>The API ID.</p>
            id: <p>The ID for the API key.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_api_key_request.DeleteApiKeyRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_api_key_response.DeleteApiKeyResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_api_key

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_api_key.delete_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_api_key_request.DeleteApiKeyRequest = {
            "api_id": api_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_namespace(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.namespace.Namespace",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_channel_namespace_response.DeleteChannelNamespaceResponse":
        """<p>Deletes a <code>ChannelNamespace</code>.</p>

        Args:
            api_id: <p>The ID of the <code>Api</code> associated with the <code>ChannelNamespace</code>.</p>
            name: <p>The name of the <code>ChannelNamespace</code>.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_channel_namespace_request.DeleteChannelNamespaceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_channel_namespace_response.DeleteChannelNamespaceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_channel_namespace

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_channel_namespace.delete_channel_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_channel_namespace_request.DeleteChannelNamespaceRequest = {
            "api_id": api_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_source(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_data_source_response.DeleteDataSourceResponse":
        """<p>Deletes a <code>DataSource</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            name: <p>The name of the data source.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_data_source_response.DeleteDataSourceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_data_source

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_data_source.delete_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_data_source_request.DeleteDataSourceRequest = {
            "api_id": api_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain_name(
        self,
        domain_name: "capo_appsync.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_domain_name_response.DeleteDomainNameResponse":
        """<p>Deletes a custom <code>DomainName</code> object.</p>

        Args:
            domain_name: <p>The domain name.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_domain_name_request.DeleteDomainNameRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_domain_name_response.DeleteDomainNameResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_domain_name

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_domain_name.delete_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_domain_name_request.DeleteDomainNameRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function(
        self,
        api_id: "capo_appsync.types.string.String",
        function_id: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_function_response.DeleteFunctionResponse":
        """<p>Deletes a <code>Function</code>.</p>

        Args:
            api_id: <p>The GraphQL API ID.</p>
            function_id: <p>The <code>Function</code> ID.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_function

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_function_request.DeleteFunctionRequest = {
            "api_id": api_id,
            "function_id": function_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_graphql_api(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_graphql_api_response.DeleteGraphqlApiResponse":
        """<p>Deletes a <code>GraphqlApi</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_graphql_api_request.DeleteGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_graphql_api_response.DeleteGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_graphql_api.delete_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_graphql_api_request.DeleteGraphqlApiRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resolver(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.resource_name.ResourceName",
        field_name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_resolver_response.DeleteResolverResponse":
        """<p>Deletes a <code>Resolver</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            type_name: <p>The name of the resolver type.</p>
            field_name: <p>The resolver field name.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_resolver_request.DeleteResolverRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_resolver_response.DeleteResolverResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_resolver

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_resolver.delete_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_resolver_request.DeleteResolverRequest = {
            "api_id": api_id,
            "type_name": type_name,
            "field_name": field_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_type(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.delete_type_response.DeleteTypeResponse":
        """<p>Deletes a <code>Type</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            type_name: <p>The type name.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.delete_type_request.DeleteTypeRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.delete_type_response.DeleteTypeResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.delete_type

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.delete_type.delete_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.delete_type_request.DeleteTypeRequest = {
            "api_id": api_id,
            "type_name": type_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_api(
        self,
        domain_name: "capo_appsync.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.disassociate_api_response.DisassociateApiResponse":
        """<p>Removes an <code>ApiAssociation</code> object from a custom domain.</p>

        Args:
            domain_name: <p>The domain name.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.disassociate_api_request.DisassociateApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.disassociate_api_response.DisassociateApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.disassociate_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.disassociate_api.disassociate_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.disassociate_api_request.DisassociateApiRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_merged_graphql_api(
        self,
        source_api_identifier: "capo_appsync.types.string.String",
        association_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.disassociate_merged_graphql_api_response.DisassociateMergedGraphqlApiResponse":
        """<p>Deletes an association between a Merged API and source API using the source API's identifier and the association ID.</p>

        Args:
            source_api_identifier: <p>The identifier of the AppSync Source API. This is generated by the AppSync service. In most cases, source APIs (especially in your account) only require the API ID value or ARN of the source API. However, source APIs from other accounts (cross-account use cases) strictly require the full resource ARN of the source API.</p>
            association_id: <p>The ID generated by the AppSync service for the source API association.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.disassociate_merged_graphql_api_request.DisassociateMergedGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.disassociate_merged_graphql_api_response.DisassociateMergedGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.disassociate_merged_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.disassociate_merged_graphql_api.disassociate_merged_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.disassociate_merged_graphql_api_request.DisassociateMergedGraphqlApiRequest = {
            "source_api_identifier": source_api_identifier,
            "association_id": association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_source_graphql_api(
        self,
        merged_api_identifier: "capo_appsync.types.string.String",
        association_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.disassociate_source_graphql_api_response.DisassociateSourceGraphqlApiResponse":
        """<p>Deletes an association between a Merged API and source API using the Merged API's identifier and the association ID.</p>

        Args:
            merged_api_identifier: <p>The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs in other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.</p>
            association_id: <p>The ID generated by the AppSync service for the source API association.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.disassociate_source_graphql_api_request.DisassociateSourceGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.disassociate_source_graphql_api_response.DisassociateSourceGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.disassociate_source_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.disassociate_source_graphql_api.disassociate_source_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.disassociate_source_graphql_api_request.DisassociateSourceGraphqlApiRequest = {
            "merged_api_identifier": merged_api_identifier,
            "association_id": association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def evaluate_code(
        self,
        runtime: "capo_appsync.types.app_sync_runtime.AppSyncRuntime",
        code: "capo_appsync.types.code.Code",
        context: "capo_appsync.types.context.Context",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        function: Optional["capo_appsync.types.string.String"] = None,
    ) -> "capo_appsync.types.evaluate_code_response.EvaluateCodeResponse":
        """<p>Evaluates the given code and returns the response. The code definition requirements depend on the specified runtime. For <code>APPSYNC_JS</code> runtimes, the code defines the request and response functions. The request function takes the incoming request after a GraphQL operation is parsed and converts it into a request configuration for the selected data source operation. The response function interprets responses from the data source and maps it to the shape of the GraphQL field output type. </p>

        Args:
            runtime: <p>The runtime to be used when evaluating the code. Currently, only the <code>APPSYNC_JS</code> runtime is supported.</p>
            code: <p>The code definition to be evaluated. Note that <code>code</code> and <code>runtime</code> are both required for this action. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>
            context: <p>The map that holds all of the contextual information for your resolver invocation. A <code>context</code> is required for this action.</p>
            function: <p>The function within the code to be evaluated. If provided, the valid values are <code>request</code> and <code>response</code>.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.evaluate_code_request.EvaluateCodeRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.evaluate_code_response.EvaluateCodeResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.evaluate_code

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.evaluate_code.evaluate_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.evaluate_code_request.EvaluateCodeRequest = {
            "runtime": runtime,
            "code": code,
            "context": context,
        }
        if function is not None:
            input_["function"] = function

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def evaluate_mapping_template(
        self,
        template: "capo_appsync.types.template.Template",
        context: "capo_appsync.types.context.Context",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.evaluate_mapping_template_response.EvaluateMappingTemplateResponse":
        """<p>Evaluates a given template and returns the response. The mapping template can be a request or response template.</p> <p>Request templates take the incoming request after a GraphQL operation is parsed and convert it into a request configuration for the selected data source operation. Response templates interpret responses from the data source and map it to the shape of the GraphQL field output type.</p> <p>Mapping templates are written in the Apache Velocity Template Language (VTL).</p>

        Args:
            template: <p>The mapping template; this can be a request or response template. A <code>template</code> is required for this action.</p>
            context: <p>The map that holds all of the contextual information for your resolver invocation. A <code>context</code> is required for this action.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.evaluate_mapping_template_request.EvaluateMappingTemplateRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.evaluate_mapping_template_response.EvaluateMappingTemplateResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.evaluate_mapping_template

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.evaluate_mapping_template.evaluate_mapping_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.evaluate_mapping_template_request.EvaluateMappingTemplateRequest = {
            "template": template,
            "context": context,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def flush_api_cache(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.flush_api_cache_response.FlushApiCacheResponse":
        """<p>Flushes an <code>ApiCache</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.flush_api_cache_request.FlushApiCacheRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.flush_api_cache_response.FlushApiCacheResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.flush_api_cache

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.flush_api_cache.flush_api_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.flush_api_cache_request.FlushApiCacheRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_api_response.GetApiResponse":
        """<p>Retrieves an <code>Api</code> object.</p>

        Args:
            api_id: <p>The <code>Api</code> ID.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_api_request.GetApiRequest]",
        ) -> OperationResponse["capo_appsync.types.get_api_response.GetApiResponse"]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_api.get_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_api_request.GetApiRequest = {"api_id": api_id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api_association(
        self,
        domain_name: "capo_appsync.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_api_association_response.GetApiAssociationResponse":
        """<p>Retrieves an <code>ApiAssociation</code> object.</p>

        Args:
            domain_name: <p>The domain name.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_api_association_request.GetApiAssociationRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_api_association_response.GetApiAssociationResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_api_association

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_api_association.get_api_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_api_association_request.GetApiAssociationRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api_cache(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_api_cache_response.GetApiCacheResponse":
        """<p>Retrieves an <code>ApiCache</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_api_cache_request.GetApiCacheRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_api_cache_response.GetApiCacheResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_api_cache

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_api_cache.get_api_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_api_cache_request.GetApiCacheRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_namespace(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.namespace.Namespace",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> (
        "capo_appsync.types.get_channel_namespace_response.GetChannelNamespaceResponse"
    ):
        """<p>Retrieves the channel namespace for a specified <code>Api</code>.</p>

        Args:
            api_id: <p>The <code>Api</code> ID.</p>
            name: <p>The name of the <code>ChannelNamespace</code>.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_channel_namespace_request.GetChannelNamespaceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_channel_namespace_response.GetChannelNamespaceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_channel_namespace

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_channel_namespace.get_channel_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_channel_namespace_request.GetChannelNamespaceRequest = {
            "api_id": api_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_source(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_data_source_response.GetDataSourceResponse":
        """<p>Retrieves a <code>DataSource</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            name: <p>The name of the data source.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_data_source_request.GetDataSourceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_data_source_response.GetDataSourceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_data_source

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_data_source.get_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_data_source_request.GetDataSourceRequest = {
            "api_id": api_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_source_introspection(
        self,
        introspection_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        include_models_sdl: Optional["capo_appsync.types.boolean.Boolean"] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.get_data_source_introspection_response.GetDataSourceIntrospectionResponse":
        """<p>Retrieves the record of an existing introspection. If the retrieval is successful, the result of the instrospection will also be returned. If the retrieval fails the operation, an error message will be returned instead.</p>

        Args:
            introspection_id: <p>The introspection ID. Each introspection contains a unique ID that can be used to reference the instrospection record.</p>
            include_models_sdl: <p>A boolean flag that determines whether SDL should be generated for introspected types. If set to <code>true</code>, each model will contain an <code>sdl</code> property that contains the SDL for that type. The SDL only contains the type data and no additional metadata or directives. </p>
            next_token: <p>Determines the number of types to be returned in a single response before paginating. This value is typically taken from <code>nextToken</code> value from the previous response.</p>
            max_results: <p>The maximum number of introspected types that will be returned in a single response.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_data_source_introspection_request.GetDataSourceIntrospectionRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_data_source_introspection_response.GetDataSourceIntrospectionResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_data_source_introspection

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_data_source_introspection.get_data_source_introspection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_data_source_introspection_request.GetDataSourceIntrospectionRequest = {
            "introspection_id": introspection_id
        }
        if include_models_sdl is not None:
            input_["include_models_sdl"] = include_models_sdl
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_name(
        self,
        domain_name: "capo_appsync.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_domain_name_response.GetDomainNameResponse":
        """<p>Retrieves a custom <code>DomainName</code> object.</p>

        Args:
            domain_name: <p>The domain name.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_domain_name_request.GetDomainNameRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_domain_name_response.GetDomainNameResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_domain_name

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_domain_name.get_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_domain_name_request.GetDomainNameRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function(
        self,
        api_id: "capo_appsync.types.string.String",
        function_id: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_function_response.GetFunctionResponse":
        """<p>Get a <code>Function</code>.</p>

        Args:
            api_id: <p>The GraphQL API ID.</p>
            function_id: <p>The <code>Function</code> ID.</p>

        Raises:
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_function

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_function_request.GetFunctionRequest = {
            "api_id": api_id,
            "function_id": function_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_graphql_api(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_graphql_api_response.GetGraphqlApiResponse":
        """<p>Retrieves a <code>GraphqlApi</code> object.</p>

        Args:
            api_id: <p>The API ID for the GraphQL API.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_graphql_api_request.GetGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_graphql_api_response.GetGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_graphql_api.get_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_graphql_api_request.GetGraphqlApiRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_graphql_api_environment_variables(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_graphql_api_environment_variables_response.GetGraphqlApiEnvironmentVariablesResponse":
        """<p>Retrieves the list of environmental variable key-value pairs associated with an API by its ID value.</p>

        Args:
            api_id: <p>The ID of the API from which the environmental variable list will be retrieved.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_graphql_api_environment_variables_request.GetGraphqlApiEnvironmentVariablesRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_graphql_api_environment_variables_response.GetGraphqlApiEnvironmentVariablesResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_graphql_api_environment_variables

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_graphql_api_environment_variables.get_graphql_api_environment_variables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_graphql_api_environment_variables_request.GetGraphqlApiEnvironmentVariablesRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_introspection_schema(
        self,
        api_id: "capo_appsync.types.string.String",
        format: "capo_appsync.types.output_type.OutputType",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        include_directives: Optional[
            "capo_appsync.types.boolean_value.BooleanValue"
        ] = None,
    ) -> "capo_appsync.types.get_introspection_schema_response.GetIntrospectionSchemaResponse":
        """<p>Retrieves the introspection schema for a GraphQL API.</p>

        Args:
            api_id: <p>The API ID.</p>
            format: <p>The schema format: SDL or JSON.</p>
            include_directives: <p>A flag that specifies whether the schema introspection should contain directives.</p>

        Raises:
            capo_appsync.errors.graph_ql_schema_exception.GraphQLSchemaException: <p>The GraphQL schema is not valid.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_introspection_schema_request.GetIntrospectionSchemaRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_introspection_schema_response.GetIntrospectionSchemaResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_introspection_schema

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_introspection_schema.get_introspection_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_introspection_schema_request.GetIntrospectionSchemaRequest = {
            "api_id": api_id,
            "format": format,
        }
        if include_directives is not None:
            input_["include_directives"] = include_directives

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resolver(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.resource_name.ResourceName",
        field_name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_resolver_response.GetResolverResponse":
        """<p>Retrieves a <code>Resolver</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            type_name: <p>The resolver type name.</p>
            field_name: <p>The resolver field name.</p>

        Raises:
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_resolver_request.GetResolverRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_resolver_response.GetResolverResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_resolver

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_resolver.get_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_resolver_request.GetResolverRequest = {
            "api_id": api_id,
            "type_name": type_name,
            "field_name": field_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_schema_creation_status(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_schema_creation_status_response.GetSchemaCreationStatusResponse":
        """<p>Retrieves the current status of a schema creation operation.</p>

        Args:
            api_id: <p>The API ID.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_schema_creation_status_request.GetSchemaCreationStatusRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_schema_creation_status_response.GetSchemaCreationStatusResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_schema_creation_status

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_schema_creation_status.get_schema_creation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_schema_creation_status_request.GetSchemaCreationStatusRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_source_api_association(
        self,
        merged_api_identifier: "capo_appsync.types.string.String",
        association_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_source_api_association_response.GetSourceApiAssociationResponse":
        """<p>Retrieves a <code>SourceApiAssociation</code> object.</p>

        Args:
            merged_api_identifier: <p>The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs in other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.</p>
            association_id: <p>The ID generated by the AppSync service for the source API association.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_source_api_association_request.GetSourceApiAssociationRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.get_source_api_association_response.GetSourceApiAssociationResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_source_api_association

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_source_api_association.get_source_api_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_source_api_association_request.GetSourceApiAssociationRequest = {
            "merged_api_identifier": merged_api_identifier,
            "association_id": association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_type(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.resource_name.ResourceName",
        format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.get_type_response.GetTypeResponse":
        """<p>Retrieves a <code>Type</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            type_name: <p>The type name.</p>
            format: <p>The type format: SDL or JSON.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.get_type_request.GetTypeRequest]",
        ) -> OperationResponse["capo_appsync.types.get_type_response.GetTypeResponse"]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.get_type

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.get_type.get_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.get_type_request.GetTypeRequest = {
            "api_id": api_id,
            "type_name": type_name,
            "format": format,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_api_keys(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_api_keys_response.ListApiKeysResponse":
        """<p>Lists the API keys for a given API.</p> <note> <p>API keys are deleted automatically 60 days after they expire. However, they may still be included in the response until they have actually been deleted. You can safely call <code>DeleteApiKey</code> to manually delete a key before it's automatically deleted.</p> </note>

        Args:
            api_id: <p>The API ID.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_api_keys_request.ListApiKeysRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_api_keys_response.ListApiKeysResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_api_keys

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_api_keys.list_api_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_api_keys_request.ListApiKeysRequest = {
            "api_id": api_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_api_keys(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.api_key.ApiKey]":
        _token = next_token
        while True:
            _response = self.list_api_keys(
                api_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("api_keys",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_apis(
        self,
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_apis_response.ListApisResponse":
        """<p>Lists the APIs in your AppSync account.</p> <p> <code>ListApis</code> returns only the high level API details. For more detailed information about an API, use <code>GetApi</code>.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_apis_request.ListApisRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_apis_response.ListApisResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_apis

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_apis.list_apis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_apis_request.ListApisRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_apis(
        self,
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.api.Api]":
        _token = next_token
        while True:
            _response = self.list_apis(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("apis",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_namespaces(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_channel_namespaces_response.ListChannelNamespacesResponse":
        """<p>Lists the channel namespaces for a specified <code>Api</code>.</p> <p> <code>ListChannelNamespaces</code> returns only high level details for the channel namespace. To retrieve code handlers, use <code>GetChannelNamespace</code>.</p>

        Args:
            api_id: <p>The <code>Api</code> ID.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_channel_namespaces_request.ListChannelNamespacesRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_channel_namespaces_response.ListChannelNamespacesResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_channel_namespaces

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_channel_namespaces.list_channel_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_channel_namespaces_request.ListChannelNamespacesRequest = {
            "api_id": api_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_channel_namespaces(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.channel_namespace.ChannelNamespace]":
        _token = next_token
        while True:
            _response = self.list_channel_namespaces(
                api_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("channel_namespaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_sources(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_data_sources_response.ListDataSourcesResponse":
        """<p>Lists the data sources for a given API.</p>

        Args:
            api_id: <p>The API ID.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_data_sources

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_data_sources.list_data_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_data_sources_request.ListDataSourcesRequest = {
            "api_id": api_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_sources(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.data_source.DataSource]":
        _token = next_token
        while True:
            _response = self.list_data_sources(
                api_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_domain_names(
        self,
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_domain_names_response.ListDomainNamesResponse":
        """<p>Lists multiple custom domain names.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_domain_names_request.ListDomainNamesRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_domain_names_response.ListDomainNamesResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_domain_names

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_domain_names.list_domain_names(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_domain_names_request.ListDomainNamesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_domain_names(
        self,
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.domain_name_config.DomainNameConfig]":
        _token = next_token
        while True:
            _response = self.list_domain_names(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("domain_name_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_functions(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_functions_response.ListFunctionsResponse":
        """<p>List multiple functions.</p>

        Args:
            api_id: <p>The GraphQL API ID.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_functions

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_functions_request.ListFunctionsRequest = {
            "api_id": api_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_functions(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.function_configuration.FunctionConfiguration]":
        _token = next_token
        while True:
            _response = self.list_functions(
                api_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("functions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_graphql_apis(
        self,
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
        api_type: Optional[
            "capo_appsync.types.graph_ql_api_type.GraphQLApiType"
        ] = None,
        owner: Optional["capo_appsync.types.ownership.Ownership"] = None,
    ) -> "capo_appsync.types.list_graphql_apis_response.ListGraphqlApisResponse":
        """<p>Lists your GraphQL APIs.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>
            api_type: <p>The value that indicates whether the GraphQL API is a standard API (<code>GRAPHQL</code>) or merged API (<code>MERGED</code>).</p>
            owner: <p>The account owner of the GraphQL API.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_graphql_apis_request.ListGraphqlApisRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_graphql_apis_response.ListGraphqlApisResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_graphql_apis

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_graphql_apis.list_graphql_apis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_graphql_apis_request.ListGraphqlApisRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if api_type is not None:
            input_["api_type"] = api_type
        if owner is not None:
            input_["owner"] = owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_graphql_apis(
        self,
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
        api_type: Optional[
            "capo_appsync.types.graph_ql_api_type.GraphQLApiType"
        ] = None,
        owner: Optional["capo_appsync.types.ownership.Ownership"] = None,
    ) -> "Iterator[capo_appsync.types.graphql_api.GraphqlApi]":
        _token = next_token
        while True:
            _response = self.list_graphql_apis(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                api_type=api_type,
                owner=owner,
            )
            _page = _resolve_path(_response, ("graphql_apis",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resolvers(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_resolvers_response.ListResolversResponse":
        """<p>Lists the resolvers for a given API and type.</p>

        Args:
            api_id: <p>The API ID.</p>
            type_name: <p>The type name.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_resolvers_request.ListResolversRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_resolvers_response.ListResolversResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_resolvers

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_resolvers.list_resolvers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_resolvers_request.ListResolversRequest = {
            "api_id": api_id,
            "type_name": type_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_resolvers(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.resolver.Resolver]":
        _token = next_token
        while True:
            _response = self.list_resolvers(
                api_id,
                type_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resolvers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resolvers_by_function(
        self,
        api_id: "capo_appsync.types.string.String",
        function_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_resolvers_by_function_response.ListResolversByFunctionResponse":
        """<p>List the resolvers that are associated with a specific function.</p>

        Args:
            api_id: <p>The API ID.</p>
            function_id: <p>The function ID.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_resolvers_by_function_request.ListResolversByFunctionRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_resolvers_by_function_response.ListResolversByFunctionResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_resolvers_by_function

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_resolvers_by_function.list_resolvers_by_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_resolvers_by_function_request.ListResolversByFunctionRequest = {
            "api_id": api_id,
            "function_id": function_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_resolvers_by_function(
        self,
        api_id: "capo_appsync.types.string.String",
        function_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.resolver.Resolver]":
        _token = next_token
        while True:
            _response = self.list_resolvers_by_function(
                api_id,
                function_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resolvers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_source_api_associations(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_source_api_associations_response.ListSourceApiAssociationsResponse":
        """<p>Lists the <code>SourceApiAssociationSummary</code> data.</p>

        Args:
            api_id: <p>The API ID.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_source_api_associations_request.ListSourceApiAssociationsRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_source_api_associations_response.ListSourceApiAssociationsResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_source_api_associations

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_source_api_associations.list_source_api_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_source_api_associations_request.ListSourceApiAssociationsRequest = {
            "api_id": api_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_source_api_associations(
        self,
        api_id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.source_api_association_summary.SourceApiAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_source_api_associations(
                api_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("source_api_association_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_appsync.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> (
        "capo_appsync.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists the tags for a resource.</p>

        Args:
            resource_arn: <p>The <code>GraphqlApi</code> Amazon Resource Name (ARN).</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_tags_for_resource

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_types(
        self,
        api_id: "capo_appsync.types.string.String",
        format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_types_response.ListTypesResponse":
        """<p>Lists the types for a given API.</p>

        Args:
            api_id: <p>The API ID.</p>
            format: <p>The type format: SDL or JSON.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_types_request.ListTypesRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_types_response.ListTypesResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_types

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_types.list_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_types_request.ListTypesRequest = {
            "api_id": api_id,
            "format": format,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_types(
        self,
        api_id: "capo_appsync.types.string.String",
        format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.type.Type]":
        _token = next_token
        while True:
            _response = self.list_types(
                api_id,
                format,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_types_by_association(
        self,
        merged_api_identifier: "capo_appsync.types.string.String",
        association_id: "capo_appsync.types.string.String",
        format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse":
        """<p>Lists <code>Type</code> objects by the source API association ID.</p>

        Args:
            merged_api_identifier: <p>The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs in other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.</p>
            association_id: <p>The ID generated by the AppSync service for the source API association.</p>
            format: <p>The format type.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>
            max_results: <p>The maximum number of results that you want the request to return.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.list_types_by_association_request.ListTypesByAssociationRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.list_types_by_association_response.ListTypesByAssociationResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.list_types_by_association

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.list_types_by_association.list_types_by_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.list_types_by_association_request.ListTypesByAssociationRequest = {
            "merged_api_identifier": merged_api_identifier,
            "association_id": association_id,
            "format": format,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_types_by_association(
        self,
        merged_api_identifier: "capo_appsync.types.string.String",
        association_id: "capo_appsync.types.string.String",
        format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        next_token: Optional[
            "capo_appsync.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_appsync.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_appsync.types.type.Type]":
        _token = next_token
        while True:
            _response = self.list_types_by_association(
                merged_api_identifier,
                association_id,
                format,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_graphql_api_environment_variables(
        self,
        api_id: "capo_appsync.types.string.String",
        environment_variables: "capo_appsync.types.environment_variable_map.EnvironmentVariableMap",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.put_graphql_api_environment_variables_response.PutGraphqlApiEnvironmentVariablesResponse":
        """<p>Creates a list of environmental variables in an API by its ID value. </p> <p>When creating an environmental variable, it must follow the constraints below:</p> <ul> <li> <p>Both JavaScript and VTL templates support environmental variables.</p> </li> <li> <p>Environmental variables are not evaluated before function invocation.</p> </li> <li> <p>Environmental variables only support string values.</p> </li> <li> <p>Any defined value in an environmental variable is considered a string literal and not expanded.</p> </li> <li> <p>Variable evaluations should ideally be performed in the function code.</p> </li> </ul> <p>When creating an environmental variable key-value pair, it must follow the additional constraints below:</p> <ul> <li> <p>Keys must begin with a letter.</p> </li> <li> <p>Keys must be at least two characters long.</p> </li> <li> <p>Keys can only contain letters, numbers, and the underscore character (_).</p> </li> <li> <p>Values can be up to 512 characters long.</p> </li> <li> <p>You can configure up to 50 key-value pairs in a GraphQL API.</p> </li> </ul> <p>You can create a list of environmental variables by adding it to the <code>environmentVariables</code> payload as a list in the format <code>{"key1":"value1","key2":"value2", …}</code>. Note that each call of the <code>PutGraphqlApiEnvironmentVariables</code> action will result in the overwriting of the existing environmental variable list of that API. This means the existing environmental variables will be lost. To avoid this, you must include all existing and new environmental variables in the list each time you call this action.</p>

        Args:
            api_id: <p>The ID of the API to which the environmental variable list will be written.</p>
            environment_variables: <p>The list of environmental variables to add to the API.</p> <p>When creating an environmental variable key-value pair, it must follow the additional constraints below:</p> <ul> <li> <p>Keys must begin with a letter.</p> </li> <li> <p>Keys must be at least two characters long.</p> </li> <li> <p>Keys can only contain letters, numbers, and the underscore character (_).</p> </li> <li> <p>Values can be up to 512 characters long.</p> </li> <li> <p>You can configure up to 50 key-value pairs in a GraphQL API.</p> </li> </ul> <p>You can create a list of environmental variables by adding it to the <code>environmentVariables</code> payload as a list in the format <code>{"key1":"value1","key2":"value2", …}</code>. Note that each call of the <code>PutGraphqlApiEnvironmentVariables</code> action will result in the overwriting of the existing environmental variable list of that API. This means the existing environmental variables will be lost. To avoid this, you must include all existing and new environmental variables in the list each time you call this action.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.put_graphql_api_environment_variables_request.PutGraphqlApiEnvironmentVariablesRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.put_graphql_api_environment_variables_response.PutGraphqlApiEnvironmentVariablesResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.put_graphql_api_environment_variables

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.put_graphql_api_environment_variables.put_graphql_api_environment_variables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.put_graphql_api_environment_variables_request.PutGraphqlApiEnvironmentVariablesRequest = {
            "api_id": api_id,
            "environment_variables": environment_variables,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_data_source_introspection(
        self,
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        rds_data_api_config: Optional[
            "capo_appsync.types.rds_data_api_config.RdsDataApiConfig"
        ] = None,
    ) -> "capo_appsync.types.start_data_source_introspection_response.StartDataSourceIntrospectionResponse":
        """<p>Creates a new introspection. Returns the <code>introspectionId</code> of the new introspection after its creation. </p>

        Args:
            rds_data_api_config: <p>The <code>rdsDataApiConfig</code> object data.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.start_data_source_introspection_request.StartDataSourceIntrospectionRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.start_data_source_introspection_response.StartDataSourceIntrospectionResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.start_data_source_introspection

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.start_data_source_introspection.start_data_source_introspection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.start_data_source_introspection_request.StartDataSourceIntrospectionRequest = {}
        if rds_data_api_config is not None:
            input_["rds_data_api_config"] = rds_data_api_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_schema_creation(
        self,
        api_id: "capo_appsync.types.string.String",
        definition: "capo_appsync.types.blob.Blob",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> (
        "capo_appsync.types.start_schema_creation_response.StartSchemaCreationResponse"
    ):
        """<p>Adds a new schema to your GraphQL API.</p> <p>This operation is asynchronous. Use to determine when it has completed.</p>

        Args:
            api_id: <p>The API ID.</p>
            definition: <p>The schema definition, in GraphQL schema language format.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.start_schema_creation_request.StartSchemaCreationRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.start_schema_creation_response.StartSchemaCreationResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.start_schema_creation

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.start_schema_creation.start_schema_creation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.start_schema_creation_request.StartSchemaCreationRequest = {
            "api_id": api_id,
            "definition": definition,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_schema_merge(
        self,
        association_id: "capo_appsync.types.string.String",
        merged_api_identifier: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.start_schema_merge_response.StartSchemaMergeResponse":
        """<p>Initiates a merge operation. Returns a status that shows the result of the merge operation.</p>

        Args:
            association_id: <p>The ID generated by the AppSync service for the source API association.</p>
            merged_api_identifier: <p>The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs in other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.start_schema_merge_request.StartSchemaMergeRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.start_schema_merge_response.StartSchemaMergeResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.start_schema_merge

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.start_schema_merge.start_schema_merge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.start_schema_merge_request.StartSchemaMergeRequest = {
            "association_id": association_id,
            "merged_api_identifier": merged_api_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_appsync.types.resource_arn.ResourceArn",
        tags: "capo_appsync.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource with user-supplied tags.</p>

        Args:
            resource_arn: <p>The <code>GraphqlApi</code> Amazon Resource Name (ARN).</p>
            tags: <p>A <code>TagMap</code> object.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.tag_resource

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_appsync.types.resource_arn.ResourceArn",
        tag_keys: "capo_appsync.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
    ) -> "capo_appsync.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags a resource.</p>

        Args:
            resource_arn: <p>The <code>GraphqlApi</code> Amazon Resource Name (ARN).</p>
            tag_keys: <p>A list of <code>TagKey</code> objects.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.untag_resource

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_api(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.api_name.ApiName",
        event_config: "capo_appsync.types.event_config.EventConfig",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        owner_contact: Optional["capo_appsync.types.string.String"] = None,
    ) -> "capo_appsync.types.update_api_response.UpdateApiResponse":
        """<p>Updates an <code>Api</code>.</p>

        Args:
            api_id: <p>The <code>Api</code> ID.</p>
            name: <p>The name of the Api.</p>
            owner_contact: <p>The owner contact information for the <code>Api</code>.</p>
            event_config: <p>The new event configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_api_request.UpdateApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_api_response.UpdateApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_api.update_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_api_request.UpdateApiRequest = {
            "api_id": api_id,
            "name": name,
            "event_config": event_config,
        }
        if owner_contact is not None:
            input_["owner_contact"] = owner_contact

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_api_cache(
        self,
        api_id: "capo_appsync.types.string.String",
        ttl: "capo_appsync.types.long.Long",
        api_caching_behavior: "capo_appsync.types.api_caching_behavior.ApiCachingBehavior",
        type: "capo_appsync.types.api_cache_type.ApiCacheType",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        health_metrics_config: Optional[
            "capo_appsync.types.cache_health_metrics_config.CacheHealthMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.update_api_cache_response.UpdateApiCacheResponse":
        """<p>Updates the cache for the GraphQL API.</p>

        Args:
            api_id: <p>The GraphQL API ID.</p>
            ttl: <p>TTL in seconds for cache entries.</p> <p>Valid values are 1–3,600 seconds.</p>
            api_caching_behavior: <p>Caching behavior.</p> <ul> <li> <p> <b>FULL_REQUEST_CACHING</b>: All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.</p> </li> <li> <p> <b>PER_RESOLVER_CACHING</b>: Individual resolvers that you specify are cached.</p> </li> <li> <p> <b>OPERATION_LEVEL_CACHING</b>: Full requests are cached together and returned without executing resolvers.</p> </li> </ul>
            type: <p>The cache instance type. Valid values are </p> <ul> <li> <p> <code>SMALL</code> </p> </li> <li> <p> <code>MEDIUM</code> </p> </li> <li> <p> <code>LARGE</code> </p> </li> <li> <p> <code>XLARGE</code> </p> </li> <li> <p> <code>LARGE_2X</code> </p> </li> <li> <p> <code>LARGE_4X</code> </p> </li> <li> <p> <code>LARGE_8X</code> (not available in all regions)</p> </li> <li> <p> <code>LARGE_12X</code> </p> </li> </ul> <p>Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.</p> <p>The following legacy instance types are available, but their use is discouraged:</p> <ul> <li> <p> <b>T2_SMALL</b>: A t2.small instance type.</p> </li> <li> <p> <b>T2_MEDIUM</b>: A t2.medium instance type.</p> </li> <li> <p> <b>R4_LARGE</b>: A r4.large instance type.</p> </li> <li> <p> <b>R4_XLARGE</b>: A r4.xlarge instance type.</p> </li> <li> <p> <b>R4_2XLARGE</b>: A r4.2xlarge instance type.</p> </li> <li> <p> <b>R4_4XLARGE</b>: A r4.4xlarge instance type.</p> </li> <li> <p> <b>R4_8XLARGE</b>: A r4.8xlarge instance type.</p> </li> </ul>
            health_metrics_config: <p>Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:</p> <ul> <li> <p>NetworkBandwidthOutAllowanceExceeded: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> <li> <p>EngineCPUUtilization: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> </ul> <p>Metrics will be recorded by API ID. You can set the value to <code>ENABLED</code> or <code>DISABLED</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_api_cache_request.UpdateApiCacheRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_api_cache_response.UpdateApiCacheResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_api_cache

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_api_cache.update_api_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_api_cache_request.UpdateApiCacheRequest = {
            "api_id": api_id,
            "ttl": ttl,
            "api_caching_behavior": api_caching_behavior,
            "type": type,
        }
        if health_metrics_config is not None:
            input_["health_metrics_config"] = health_metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_api_key(
        self,
        api_id: "capo_appsync.types.string.String",
        id: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        expires: Optional["capo_appsync.types.long.Long"] = None,
    ) -> "capo_appsync.types.update_api_key_response.UpdateApiKeyResponse":
        """<p>Updates an API key. You can update the key as long as it's not deleted.</p>

        Args:
            api_id: <p>The ID for the GraphQL API.</p>
            id: <p>The API key ID.</p>
            description: <p>A description of the purpose of the API key.</p>
            expires: <p>From the update time, the time after which the API key expires. The date is represented as seconds since the epoch. For more information, see .</p>

        Raises:
            capo_appsync.errors.api_key_validity_out_of_bounds_exception.ApiKeyValidityOutOfBoundsException: <p>The API key expiration must be set to a value between 1 and 365 days from creation (for <code>CreateApiKey</code>) or from update (for <code>UpdateApiKey</code>).</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a limit. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_api_key_request.UpdateApiKeyRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_api_key_response.UpdateApiKeyResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_api_key

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_api_key.update_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_api_key_request.UpdateApiKeyRequest = {
            "api_id": api_id,
            "id": id,
        }
        if description is not None:
            input_["description"] = description
        if expires is not None:
            input_["expires"] = expires

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel_namespace(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.namespace.Namespace",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        subscribe_auth_modes: Optional[
            "capo_appsync.types.auth_modes.AuthModes"
        ] = None,
        publish_auth_modes: Optional["capo_appsync.types.auth_modes.AuthModes"] = None,
        code_handlers: Optional["capo_appsync.types.code.Code"] = None,
        handler_configs: Optional[
            "capo_appsync.types.handler_configs.HandlerConfigs"
        ] = None,
    ) -> "capo_appsync.types.update_channel_namespace_response.UpdateChannelNamespaceResponse":
        """<p>Updates a <code>ChannelNamespace</code> associated with an <code>Api</code>.</p>

        Args:
            api_id: <p>The <code>Api</code> ID.</p>
            name: <p>The name of the <code>ChannelNamespace</code>.</p>
            subscribe_auth_modes: <p>The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>
            publish_auth_modes: <p>The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>
            code_handlers: <p>The event handler functions that run custom business logic to process published events and subscribe requests.</p>
            handler_configs: <p>The configuration for the <code>OnPublish</code> and <code>OnSubscribe</code> handlers.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_channel_namespace_request.UpdateChannelNamespaceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_channel_namespace_response.UpdateChannelNamespaceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_channel_namespace

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_channel_namespace.update_channel_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_channel_namespace_request.UpdateChannelNamespaceRequest = {
            "api_id": api_id,
            "name": name,
        }
        if subscribe_auth_modes is not None:
            input_["subscribe_auth_modes"] = subscribe_auth_modes
        if publish_auth_modes is not None:
            input_["publish_auth_modes"] = publish_auth_modes
        if code_handlers is not None:
            input_["code_handlers"] = code_handlers
        if handler_configs is not None:
            input_["handler_configs"] = handler_configs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_source(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.resource_name.ResourceName",
        type: "capo_appsync.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        service_role_arn: Optional["capo_appsync.types.string.String"] = None,
        dynamodb_config: Optional[
            "capo_appsync.types.dynamodb_data_source_config.DynamodbDataSourceConfig"
        ] = None,
        lambda_config: Optional[
            "capo_appsync.types.lambda_data_source_config.LambdaDataSourceConfig"
        ] = None,
        elasticsearch_config: Optional[
            "capo_appsync.types.elasticsearch_data_source_config.ElasticsearchDataSourceConfig"
        ] = None,
        open_search_service_config: Optional[
            "capo_appsync.types.open_search_service_data_source_config.OpenSearchServiceDataSourceConfig"
        ] = None,
        http_config: Optional[
            "capo_appsync.types.http_data_source_config.HttpDataSourceConfig"
        ] = None,
        relational_database_config: Optional[
            "capo_appsync.types.relational_database_data_source_config.RelationalDatabaseDataSourceConfig"
        ] = None,
        event_bridge_config: Optional[
            "capo_appsync.types.event_bridge_data_source_config.EventBridgeDataSourceConfig"
        ] = None,
        metrics_config: Optional[
            "capo_appsync.types.data_source_level_metrics_config.DataSourceLevelMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.update_data_source_response.UpdateDataSourceResponse":
        """<p>Updates a <code>DataSource</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            name: <p>The new name for the data source.</p>
            description: <p>The new description for the data source.</p>
            type: <p>The new data source type.</p>
            service_role_arn: <p>The new service role Amazon Resource Name (ARN) for the data source.</p>
            dynamodb_config: <p>The new Amazon DynamoDB configuration.</p>
            lambda_config: <p>The new Lambda configuration.</p>
            elasticsearch_config: <p>The new OpenSearch configuration.</p> <p>As of September 2021, Amazon Elasticsearch service is Amazon OpenSearch Service. This configuration is deprecated. Instead, use <a>UpdateDataSourceRequest$openSearchServiceConfig</a> to update an OpenSearch data source.</p>
            open_search_service_config: <p>The new OpenSearch configuration.</p>
            http_config: <p>The new HTTP endpoint configuration.</p>
            relational_database_config: <p>The new relational database configuration.</p>
            event_bridge_config: <p>The new Amazon EventBridge settings.</p>
            metrics_config: <p>Enables or disables enhanced data source metrics for specified data sources. Note that <code>metricsConfig</code> won't be used unless the <code>dataSourceLevelMetricsBehavior</code> value is set to <code>PER_DATA_SOURCE_METRICS</code>. If the <code>dataSourceLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_DATA_SOURCE_METRICS</code> instead, <code>metricsConfig</code> will be ignored. However, you can still set its value.</p> <p> <code>metricsConfig</code> can be <code>ENABLED</code> or <code>DISABLED</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_data_source_response.UpdateDataSourceResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_data_source

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_data_source.update_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_data_source_request.UpdateDataSourceRequest = {
            "api_id": api_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if service_role_arn is not None:
            input_["service_role_arn"] = service_role_arn
        if dynamodb_config is not None:
            input_["dynamodb_config"] = dynamodb_config
        if lambda_config is not None:
            input_["lambda_config"] = lambda_config
        if elasticsearch_config is not None:
            input_["elasticsearch_config"] = elasticsearch_config
        if open_search_service_config is not None:
            input_["open_search_service_config"] = open_search_service_config
        if http_config is not None:
            input_["http_config"] = http_config
        if relational_database_config is not None:
            input_["relational_database_config"] = relational_database_config
        if event_bridge_config is not None:
            input_["event_bridge_config"] = event_bridge_config
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_domain_name(
        self,
        domain_name: "capo_appsync.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.description.Description"] = None,
    ) -> "capo_appsync.types.update_domain_name_response.UpdateDomainNameResponse":
        """<p>Updates a custom <code>DomainName</code> object.</p>

        Args:
            domain_name: <p>The domain name.</p>
            description: <p>A description of the <code>DomainName</code>.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_domain_name_request.UpdateDomainNameRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_domain_name_response.UpdateDomainNameResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_domain_name

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_domain_name.update_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_domain_name_request.UpdateDomainNameRequest = {
            "domain_name": domain_name
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.resource_name.ResourceName",
        function_id: "capo_appsync.types.resource_name.ResourceName",
        data_source_name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        request_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        response_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        function_version: Optional["capo_appsync.types.string.String"] = None,
        sync_config: Optional["capo_appsync.types.sync_config.SyncConfig"] = None,
        max_batch_size: Optional[
            "capo_appsync.types.max_batch_size.MaxBatchSize"
        ] = None,
        runtime: Optional["capo_appsync.types.app_sync_runtime.AppSyncRuntime"] = None,
        code: Optional["capo_appsync.types.code.Code"] = None,
    ) -> "capo_appsync.types.update_function_response.UpdateFunctionResponse":
        """<p>Updates a <code>Function</code> object.</p>

        Args:
            api_id: <p>The GraphQL API ID.</p>
            name: <p>The <code>Function</code> name.</p>
            description: <p>The <code>Function</code> description.</p>
            function_id: <p>The function ID.</p>
            data_source_name: <p>The <code>Function</code> <code>DataSource</code> name.</p>
            request_mapping_template: <p>The <code>Function</code> request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p>
            response_mapping_template: <p>The <code>Function</code> request mapping template.</p>
            function_version: <p>The <code>version</code> of the request mapping template. Currently, the supported value is 2018-05-29. Note that when using VTL and mapping templates, the <code>functionVersion</code> is required.</p>
            max_batch_size: <p>The maximum batching size for a resolver.</p>
            code: <p>The <code>function</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_function_request.UpdateFunctionRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_function_response.UpdateFunctionResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_function

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_function.update_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_function_request.UpdateFunctionRequest = {
            "api_id": api_id,
            "name": name,
            "function_id": function_id,
            "data_source_name": data_source_name,
        }
        if description is not None:
            input_["description"] = description
        if request_mapping_template is not None:
            input_["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            input_["response_mapping_template"] = response_mapping_template
        if function_version is not None:
            input_["function_version"] = function_version
        if sync_config is not None:
            input_["sync_config"] = sync_config
        if max_batch_size is not None:
            input_["max_batch_size"] = max_batch_size
        if runtime is not None:
            input_["runtime"] = runtime
        if code is not None:
            input_["code"] = code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_graphql_api(
        self,
        api_id: "capo_appsync.types.string.String",
        name: "capo_appsync.types.string.String",
        authentication_type: "capo_appsync.types.authentication_type.AuthenticationType",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        log_config: Optional["capo_appsync.types.log_config.LogConfig"] = None,
        user_pool_config: Optional[
            "capo_appsync.types.user_pool_config.UserPoolConfig"
        ] = None,
        open_id_connect_config: Optional[
            "capo_appsync.types.open_id_connect_config.OpenIDConnectConfig"
        ] = None,
        additional_authentication_providers: Optional[
            "capo_appsync.types.additional_authentication_providers.AdditionalAuthenticationProviders"
        ] = None,
        xray_enabled: Optional["capo_appsync.types.boolean.Boolean"] = None,
        lambda_authorizer_config: Optional[
            "capo_appsync.types.lambda_authorizer_config.LambdaAuthorizerConfig"
        ] = None,
        merged_api_execution_role_arn: Optional[
            "capo_appsync.types.string.String"
        ] = None,
        owner_contact: Optional["capo_appsync.types.string.String"] = None,
        introspection_config: Optional[
            "capo_appsync.types.graph_ql_api_introspection_config.GraphQLApiIntrospectionConfig"
        ] = None,
        query_depth_limit: Optional[
            "capo_appsync.types.query_depth_limit.QueryDepthLimit"
        ] = None,
        resolver_count_limit: Optional[
            "capo_appsync.types.resolver_count_limit.ResolverCountLimit"
        ] = None,
        enhanced_metrics_config: Optional[
            "capo_appsync.types.enhanced_metrics_config.EnhancedMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.update_graphql_api_response.UpdateGraphqlApiResponse":
        """<p>Updates a <code>GraphqlApi</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            name: <p>The new name for the <code>GraphqlApi</code> object.</p>
            log_config: <p>The Amazon CloudWatch Logs configuration for the <code>GraphqlApi</code> object.</p>
            authentication_type: <p>The new authentication type for the <code>GraphqlApi</code> object.</p>
            user_pool_config: <p>The new Amazon Cognito user pool configuration for the <code>~GraphqlApi</code> object.</p>
            open_id_connect_config: <p>The OpenID Connect configuration for the <code>GraphqlApi</code> object.</p>
            additional_authentication_providers: <p>A list of additional authentication providers for the <code>GraphqlApi</code> API.</p>
            xray_enabled: <p>A flag indicating whether to use X-Ray tracing for the <code>GraphqlApi</code>.</p>
            lambda_authorizer_config: <p>Configuration for Lambda function authorization.</p>
            merged_api_execution_role_arn: <p>The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the <code>AUTO_MERGE</code> to update the merged API endpoint with the source API changes automatically.</p>
            owner_contact: <p>The owner contact information for an API resource.</p> <p>This field accepts any string input with a length of 0 - 256 characters.</p>
            introspection_config: <p>Sets the value of the GraphQL API to enable (<code>ENABLED</code>) or disable (<code>DISABLED</code>) introspection. If no value is provided, the introspection configuration will be set to <code>ENABLED</code> by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.</p> <p>For more information about introspection, see <a href="https://graphql.org/learn/introspection/">GraphQL introspection</a>.</p>
            query_depth_limit: <p>The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query. The default value is <code>0</code> (or unspecified), which indicates there's no depth limit. If you set a limit, it can be between <code>1</code> and <code>75</code> nested levels. This field will produce a limit error if the operation falls out of bounds.</p> <p>Note that fields can still be set to nullable or non-nullable. If a non-nullable field produces an error, the error will be thrown upwards to the first nullable field available.</p>
            resolver_count_limit: <p>The maximum number of resolvers that can be invoked in a single request. The default value is <code>0</code> (or unspecified), which will set the limit to <code>10000</code>. When specified, the limit value can be between <code>1</code> and <code>10000</code>. This field will produce a limit error if the operation falls out of bounds.</p>
            enhanced_metrics_config: <p>The <code>enhancedMetricsConfig</code> object.</p>

        Raises:
            capo_appsync.errors.access_denied_exception.AccessDeniedException: <p>You don't have access to perform this operation on this resource.</p>
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_graphql_api_request.UpdateGraphqlApiRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_graphql_api_response.UpdateGraphqlApiResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_graphql_api

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_graphql_api.update_graphql_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_graphql_api_request.UpdateGraphqlApiRequest = {
            "api_id": api_id,
            "name": name,
            "authentication_type": authentication_type,
        }
        if log_config is not None:
            input_["log_config"] = log_config
        if user_pool_config is not None:
            input_["user_pool_config"] = user_pool_config
        if open_id_connect_config is not None:
            input_["open_id_connect_config"] = open_id_connect_config
        if additional_authentication_providers is not None:
            input_["additional_authentication_providers"] = (
                additional_authentication_providers
            )
        if xray_enabled is not None:
            input_["xray_enabled"] = xray_enabled
        if lambda_authorizer_config is not None:
            input_["lambda_authorizer_config"] = lambda_authorizer_config
        if merged_api_execution_role_arn is not None:
            input_["merged_api_execution_role_arn"] = merged_api_execution_role_arn
        if owner_contact is not None:
            input_["owner_contact"] = owner_contact
        if introspection_config is not None:
            input_["introspection_config"] = introspection_config
        if query_depth_limit is not None:
            input_["query_depth_limit"] = query_depth_limit
        if resolver_count_limit is not None:
            input_["resolver_count_limit"] = resolver_count_limit
        if enhanced_metrics_config is not None:
            input_["enhanced_metrics_config"] = enhanced_metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resolver(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.resource_name.ResourceName",
        field_name: "capo_appsync.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        data_source_name: Optional[
            "capo_appsync.types.resource_name.ResourceName"
        ] = None,
        request_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        response_mapping_template: Optional[
            "capo_appsync.types.mapping_template.MappingTemplate"
        ] = None,
        kind: Optional["capo_appsync.types.resolver_kind.ResolverKind"] = None,
        pipeline_config: Optional[
            "capo_appsync.types.pipeline_config.PipelineConfig"
        ] = None,
        sync_config: Optional["capo_appsync.types.sync_config.SyncConfig"] = None,
        caching_config: Optional[
            "capo_appsync.types.caching_config.CachingConfig"
        ] = None,
        max_batch_size: Optional[
            "capo_appsync.types.max_batch_size.MaxBatchSize"
        ] = None,
        runtime: Optional["capo_appsync.types.app_sync_runtime.AppSyncRuntime"] = None,
        code: Optional["capo_appsync.types.code.Code"] = None,
        metrics_config: Optional[
            "capo_appsync.types.resolver_level_metrics_config.ResolverLevelMetricsConfig"
        ] = None,
    ) -> "capo_appsync.types.update_resolver_response.UpdateResolverResponse":
        """<p>Updates a <code>Resolver</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            type_name: <p>The new type name.</p>
            field_name: <p>The new field name.</p>
            data_source_name: <p>The new data source name.</p>
            request_mapping_template: <p>The new request mapping template.</p> <p>A resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).</p> <p>VTL request mapping templates are optional when using an Lambda data source. For all other data sources, VTL request and response mapping templates are required.</p>
            response_mapping_template: <p>The new response mapping template.</p>
            kind: <p>The resolver type.</p> <ul> <li> <p> <b>UNIT</b>: A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.</p> </li> <li> <p> <b>PIPELINE</b>: A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of <code>Function</code> objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.</p> </li> </ul>
            pipeline_config: <p>The <code>PipelineConfig</code>.</p>
            sync_config: <p>The <code>SyncConfig</code> for a resolver attached to a versioned data source.</p>
            caching_config: <p>The caching configuration for the resolver.</p>
            max_batch_size: <p>The maximum batching size for a resolver.</p>
            code: <p>The <code>resolver</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>
            metrics_config: <p>Enables or disables enhanced resolver metrics for specified resolvers. Note that <code>metricsConfig</code> won't be used unless the <code>resolverLevelMetricsBehavior</code> value is set to <code>PER_RESOLVER_METRICS</code>. If the <code>resolverLevelMetricsBehavior</code> is set to <code>FULL_REQUEST_RESOLVER_METRICS</code> instead, <code>metricsConfig</code> will be ignored. However, you can still set its value.</p> <p> <code>metricsConfig</code> can be <code>ENABLED</code> or <code>DISABLED</code>.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_resolver_request.UpdateResolverRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_resolver_response.UpdateResolverResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_resolver

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_resolver.update_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_resolver_request.UpdateResolverRequest = {
            "api_id": api_id,
            "type_name": type_name,
            "field_name": field_name,
        }
        if data_source_name is not None:
            input_["data_source_name"] = data_source_name
        if request_mapping_template is not None:
            input_["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            input_["response_mapping_template"] = response_mapping_template
        if kind is not None:
            input_["kind"] = kind
        if pipeline_config is not None:
            input_["pipeline_config"] = pipeline_config
        if sync_config is not None:
            input_["sync_config"] = sync_config
        if caching_config is not None:
            input_["caching_config"] = caching_config
        if max_batch_size is not None:
            input_["max_batch_size"] = max_batch_size
        if runtime is not None:
            input_["runtime"] = runtime
        if code is not None:
            input_["code"] = code
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_source_api_association(
        self,
        association_id: "capo_appsync.types.string.String",
        merged_api_identifier: "capo_appsync.types.string.String",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        description: Optional["capo_appsync.types.string.String"] = None,
        source_api_association_config: Optional[
            "capo_appsync.types.source_api_association_config.SourceApiAssociationConfig"
        ] = None,
    ) -> "capo_appsync.types.update_source_api_association_response.UpdateSourceApiAssociationResponse":
        """<p>Updates some of the configuration choices of a particular source API association.</p>

        Args:
            association_id: <p>The ID generated by the AppSync service for the source API association.</p>
            merged_api_identifier: <p>The identifier of the AppSync Merged API. This is generated by the AppSync service. In most cases, Merged APIs (especially in your account) only require the API ID value or ARN of the merged API. However, Merged APIs in other accounts (cross-account use cases) strictly require the full resource ARN of the merged API.</p>
            description: <p>The description field.</p>
            source_api_association_config: <p>The <code>SourceApiAssociationConfig</code> object data.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_source_api_association_request.UpdateSourceApiAssociationRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_source_api_association_response.UpdateSourceApiAssociationResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_source_api_association

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_source_api_association.update_source_api_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_source_api_association_request.UpdateSourceApiAssociationRequest = {
            "association_id": association_id,
            "merged_api_identifier": merged_api_identifier,
        }
        if description is not None:
            input_["description"] = description
        if source_api_association_config is not None:
            input_["source_api_association_config"] = source_api_association_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_type(
        self,
        api_id: "capo_appsync.types.string.String",
        type_name: "capo_appsync.types.resource_name.ResourceName",
        format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat",
        *,
        config_overrides: Optional[AppSyncClientConfig] = None,
        definition: Optional["capo_appsync.types.string.String"] = None,
    ) -> "capo_appsync.types.update_type_response.UpdateTypeResponse":
        """<p>Updates a <code>Type</code> object.</p>

        Args:
            api_id: <p>The API ID.</p>
            type_name: <p>The new type name.</p>
            definition: <p>The new definition.</p>
            format: <p>The new type format: SDL or JSON.</p>

        Raises:
            capo_appsync.errors.bad_request_exception.BadRequestException: <p>The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.</p>
            capo_appsync.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Another modification is in progress at this time and it must complete before you can make your change.</p>
            capo_appsync.errors.internal_failure_exception.InternalFailureException: <p>An internal AppSync error occurred. Try your request again.</p>
            capo_appsync.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. Check the resource, and then try again.</p>
            capo_appsync.errors.unauthorized_exception.UnauthorizedException: <p>You aren't authorized to perform this operation.</p>
            capo_appsync.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appsync.types.update_type_request.UpdateTypeRequest]",
        ) -> OperationResponse[
            "capo_appsync.types.update_type_response.UpdateTypeResponse"
        ]:
            import capo_appsync._operations.aws_deepdish_control_plane_service.update_type

            output, http_response = (
                capo_appsync._operations.aws_deepdish_control_plane_service.update_type.update_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appsync.types.update_type_request.UpdateTypeRequest = {
            "api_id": api_id,
            "type_name": type_name,
            "format": format,
        }
        if definition is not None:
            input_["definition"] = definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

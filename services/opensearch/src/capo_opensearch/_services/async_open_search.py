"""Generated from Smithy shape ``com.amazonaws.opensearch#AmazonOpenSearchService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_opensearch._auth._signers
import capo_opensearch._auth._sigv4
from capo_opensearch._auth._identity import Credentials
from capo_opensearch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_opensearch._auth._zapros_handler import AuthMiddleware
from capo_opensearch._pagination import resolve_path as _resolve_path
from capo_opensearch._services._aws_config import aaws_config
from capo_opensearch._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_opensearch.types.accept_inbound_connection_request
    import capo_opensearch.types.accept_inbound_connection_response
    import capo_opensearch.types.accepted_warnings_list
    import capo_opensearch.types.action_type
    import capo_opensearch.types.add_data_source_request
    import capo_opensearch.types.add_data_source_response
    import capo_opensearch.types.add_direct_query_data_source_request
    import capo_opensearch.types.add_direct_query_data_source_response
    import capo_opensearch.types.add_tags_request
    import capo_opensearch.types.advanced_options
    import capo_opensearch.types.advanced_security_options_input
    import capo_opensearch.types.aiml_options_input
    import capo_opensearch.types.app_configs
    import capo_opensearch.types.application_id
    import capo_opensearch.types.application_name
    import capo_opensearch.types.application_statuses
    import capo_opensearch.types.application_summary
    import capo_opensearch.types.arn
    import capo_opensearch.types.associate_package_request
    import capo_opensearch.types.associate_package_response
    import capo_opensearch.types.associate_packages_request
    import capo_opensearch.types.associate_packages_response
    import capo_opensearch.types.attach_data_source_request
    import capo_opensearch.types.attach_data_source_response
    import capo_opensearch.types.authorize_vpc_endpoint_access_request
    import capo_opensearch.types.authorize_vpc_endpoint_access_response
    import capo_opensearch.types.auto_tune_options
    import capo_opensearch.types.auto_tune_options_input
    import capo_opensearch.types.automated_snapshot_pause_request_options
    import capo_opensearch.types.aws_account
    import capo_opensearch.types.aws_service_principal
    import capo_opensearch.types.boolean
    import capo_opensearch.types.cancel_domain_config_change_request
    import capo_opensearch.types.cancel_domain_config_change_response
    import capo_opensearch.types.cancel_service_software_update_request
    import capo_opensearch.types.cancel_service_software_update_response
    import capo_opensearch.types.capability_base_request_config
    import capo_opensearch.types.capability_name
    import capo_opensearch.types.client_token
    import capo_opensearch.types.cluster_config
    import capo_opensearch.types.cognito_options
    import capo_opensearch.types.commit_message
    import capo_opensearch.types.connection_alias
    import capo_opensearch.types.connection_id
    import capo_opensearch.types.connection_mode
    import capo_opensearch.types.connection_properties
    import capo_opensearch.types.create_application_request
    import capo_opensearch.types.create_application_response
    import capo_opensearch.types.create_domain_request
    import capo_opensearch.types.create_domain_response
    import capo_opensearch.types.create_index_request
    import capo_opensearch.types.create_index_response
    import capo_opensearch.types.create_outbound_connection_request
    import capo_opensearch.types.create_outbound_connection_response
    import capo_opensearch.types.create_package_request
    import capo_opensearch.types.create_package_response
    import capo_opensearch.types.create_vpc_endpoint_request
    import capo_opensearch.types.create_vpc_endpoint_response
    import capo_opensearch.types.data_source_description
    import capo_opensearch.types.data_source_name
    import capo_opensearch.types.data_source_status
    import capo_opensearch.types.data_source_type
    import capo_opensearch.types.data_sources
    import capo_opensearch.types.delete_application_request
    import capo_opensearch.types.delete_application_response
    import capo_opensearch.types.delete_data_source_request
    import capo_opensearch.types.delete_data_source_response
    import capo_opensearch.types.delete_direct_query_data_source_request
    import capo_opensearch.types.delete_domain_request
    import capo_opensearch.types.delete_domain_response
    import capo_opensearch.types.delete_inbound_connection_request
    import capo_opensearch.types.delete_inbound_connection_response
    import capo_opensearch.types.delete_index_request
    import capo_opensearch.types.delete_index_response
    import capo_opensearch.types.delete_outbound_connection_request
    import capo_opensearch.types.delete_outbound_connection_response
    import capo_opensearch.types.delete_package_request
    import capo_opensearch.types.delete_package_response
    import capo_opensearch.types.delete_vpc_endpoint_request
    import capo_opensearch.types.delete_vpc_endpoint_response
    import capo_opensearch.types.deployment_strategy_options
    import capo_opensearch.types.deregister_capability_request
    import capo_opensearch.types.deregister_capability_response
    import capo_opensearch.types.describe_data_source_attachment_request
    import capo_opensearch.types.describe_data_source_attachment_response
    import capo_opensearch.types.describe_domain_auto_tunes_request
    import capo_opensearch.types.describe_domain_auto_tunes_response
    import capo_opensearch.types.describe_domain_change_progress_request
    import capo_opensearch.types.describe_domain_change_progress_response
    import capo_opensearch.types.describe_domain_config_request
    import capo_opensearch.types.describe_domain_config_response
    import capo_opensearch.types.describe_domain_health_request
    import capo_opensearch.types.describe_domain_health_response
    import capo_opensearch.types.describe_domain_nodes_request
    import capo_opensearch.types.describe_domain_nodes_response
    import capo_opensearch.types.describe_domain_request
    import capo_opensearch.types.describe_domain_response
    import capo_opensearch.types.describe_domains_request
    import capo_opensearch.types.describe_domains_response
    import capo_opensearch.types.describe_dry_run_progress_request
    import capo_opensearch.types.describe_dry_run_progress_response
    import capo_opensearch.types.describe_inbound_connections_request
    import capo_opensearch.types.describe_inbound_connections_response
    import capo_opensearch.types.describe_insight_details_request
    import capo_opensearch.types.describe_insight_details_response
    import capo_opensearch.types.describe_instance_type_limits_request
    import capo_opensearch.types.describe_instance_type_limits_response
    import capo_opensearch.types.describe_outbound_connections_request
    import capo_opensearch.types.describe_outbound_connections_response
    import capo_opensearch.types.describe_packages_filter_list
    import capo_opensearch.types.describe_packages_request
    import capo_opensearch.types.describe_packages_response
    import capo_opensearch.types.describe_reserved_instance_offerings_request
    import capo_opensearch.types.describe_reserved_instance_offerings_response
    import capo_opensearch.types.describe_reserved_instances_request
    import capo_opensearch.types.describe_reserved_instances_response
    import capo_opensearch.types.describe_vpc_endpoints_request
    import capo_opensearch.types.describe_vpc_endpoints_response
    import capo_opensearch.types.detach_data_source_request
    import capo_opensearch.types.detach_data_source_response
    import capo_opensearch.types.direct_query_data_source_description
    import capo_opensearch.types.direct_query_data_source_name
    import capo_opensearch.types.direct_query_data_source_type
    import capo_opensearch.types.direct_query_open_search_arn_list
    import capo_opensearch.types.dissociate_package_request
    import capo_opensearch.types.dissociate_package_response
    import capo_opensearch.types.dissociate_packages_request
    import capo_opensearch.types.dissociate_packages_response
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.domain_endpoint_options
    import capo_opensearch.types.domain_information_container
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.domain_name_list
    import capo_opensearch.types.domain_use_case
    import capo_opensearch.types.dry_run
    import capo_opensearch.types.dry_run_mode
    import capo_opensearch.types.ebs_options
    import capo_opensearch.types.encryption_at_rest_options
    import capo_opensearch.types.engine_mode
    import capo_opensearch.types.engine_type
    import capo_opensearch.types.engine_version
    import capo_opensearch.types.filter_list
    import capo_opensearch.types.get_application_request
    import capo_opensearch.types.get_application_response
    import capo_opensearch.types.get_capability_request
    import capo_opensearch.types.get_capability_response
    import capo_opensearch.types.get_compatible_versions_request
    import capo_opensearch.types.get_compatible_versions_response
    import capo_opensearch.types.get_data_source_request
    import capo_opensearch.types.get_data_source_response
    import capo_opensearch.types.get_default_application_setting_request
    import capo_opensearch.types.get_default_application_setting_response
    import capo_opensearch.types.get_direct_query_data_source_request
    import capo_opensearch.types.get_direct_query_data_source_response
    import capo_opensearch.types.get_domain_maintenance_status_request
    import capo_opensearch.types.get_domain_maintenance_status_response
    import capo_opensearch.types.get_index_request
    import capo_opensearch.types.get_index_response
    import capo_opensearch.types.get_migration_request
    import capo_opensearch.types.get_migration_response
    import capo_opensearch.types.get_package_version_history_request
    import capo_opensearch.types.get_package_version_history_response
    import capo_opensearch.types.get_upgrade_history_request
    import capo_opensearch.types.get_upgrade_history_response
    import capo_opensearch.types.get_upgrade_status_request
    import capo_opensearch.types.get_upgrade_status_response
    import capo_opensearch.types.guid
    import capo_opensearch.types.iam_identity_center_options_input
    import capo_opensearch.types.id
    import capo_opensearch.types.identity_center_options_input
    import capo_opensearch.types.index_name
    import capo_opensearch.types.index_schema
    import capo_opensearch.types.insight_entity
    import capo_opensearch.types.insight_feedback_entity
    import capo_opensearch.types.insight_feedback_request
    import capo_opensearch.types.insight_feedback_response
    import capo_opensearch.types.insight_feedback_text
    import capo_opensearch.types.insight_feedback_thumbs
    import capo_opensearch.types.insight_page_size
    import capo_opensearch.types.insight_sort_order
    import capo_opensearch.types.insight_time_range
    import capo_opensearch.types.instance_count
    import capo_opensearch.types.instance_type_string
    import capo_opensearch.types.integer
    import capo_opensearch.types.ip_address_type
    import capo_opensearch.types.kms_key_arn
    import capo_opensearch.types.list_applications_request
    import capo_opensearch.types.list_applications_response
    import capo_opensearch.types.list_data_source_attachments_request
    import capo_opensearch.types.list_data_source_attachments_response
    import capo_opensearch.types.list_data_sources_request
    import capo_opensearch.types.list_data_sources_response
    import capo_opensearch.types.list_direct_query_data_sources_request
    import capo_opensearch.types.list_direct_query_data_sources_response
    import capo_opensearch.types.list_domain_maintenances_request
    import capo_opensearch.types.list_domain_maintenances_response
    import capo_opensearch.types.list_domain_names_request
    import capo_opensearch.types.list_domain_names_response
    import capo_opensearch.types.list_domains_for_package_request
    import capo_opensearch.types.list_domains_for_package_response
    import capo_opensearch.types.list_insights_request
    import capo_opensearch.types.list_insights_response
    import capo_opensearch.types.list_instance_type_details_request
    import capo_opensearch.types.list_instance_type_details_response
    import capo_opensearch.types.list_migrations_request
    import capo_opensearch.types.list_migrations_response
    import capo_opensearch.types.list_packages_for_domain_request
    import capo_opensearch.types.list_packages_for_domain_response
    import capo_opensearch.types.list_scheduled_actions_request
    import capo_opensearch.types.list_scheduled_actions_response
    import capo_opensearch.types.list_tags_request
    import capo_opensearch.types.list_tags_response
    import capo_opensearch.types.list_versions_request
    import capo_opensearch.types.list_versions_response
    import capo_opensearch.types.list_vpc_endpoint_access_request
    import capo_opensearch.types.list_vpc_endpoint_access_response
    import capo_opensearch.types.list_vpc_endpoints_for_domain_request
    import capo_opensearch.types.list_vpc_endpoints_for_domain_response
    import capo_opensearch.types.list_vpc_endpoints_request
    import capo_opensearch.types.list_vpc_endpoints_response
    import capo_opensearch.types.log_publishing_options
    import capo_opensearch.types.long
    import capo_opensearch.types.maintenance_status
    import capo_opensearch.types.maintenance_type
    import capo_opensearch.types.max_results
    import capo_opensearch.types.migration_options
    import capo_opensearch.types.next_token
    import capo_opensearch.types.node_id
    import capo_opensearch.types.node_to_node_encryption_options
    import capo_opensearch.types.off_peak_window_options
    import capo_opensearch.types.open_search_partition_instance_type
    import capo_opensearch.types.package_association_configuration
    import capo_opensearch.types.package_configuration
    import capo_opensearch.types.package_description
    import capo_opensearch.types.package_details_for_association_list
    import capo_opensearch.types.package_encryption_options
    import capo_opensearch.types.package_id
    import capo_opensearch.types.package_id_list
    import capo_opensearch.types.package_name
    import capo_opensearch.types.package_scope_operation_enum
    import capo_opensearch.types.package_source
    import capo_opensearch.types.package_type
    import capo_opensearch.types.package_user_list
    import capo_opensearch.types.package_vending_options
    import capo_opensearch.types.policy_document
    import capo_opensearch.types.purchase_reserved_instance_offering_request
    import capo_opensearch.types.purchase_reserved_instance_offering_response
    import capo_opensearch.types.put_default_application_setting_request
    import capo_opensearch.types.put_default_application_setting_response
    import capo_opensearch.types.register_capability_request
    import capo_opensearch.types.register_capability_response
    import capo_opensearch.types.reject_inbound_connection_request
    import capo_opensearch.types.reject_inbound_connection_response
    import capo_opensearch.types.remove_tags_request
    import capo_opensearch.types.request_id
    import capo_opensearch.types.reservation_token
    import capo_opensearch.types.revoke_vpc_endpoint_access_request
    import capo_opensearch.types.revoke_vpc_endpoint_access_response
    import capo_opensearch.types.rollback_service_software_update_request
    import capo_opensearch.types.rollback_service_software_update_response
    import capo_opensearch.types.schedule_at
    import capo_opensearch.types.service_options
    import capo_opensearch.types.snapshot_options
    import capo_opensearch.types.software_update_options
    import capo_opensearch.types.start_domain_maintenance_request
    import capo_opensearch.types.start_domain_maintenance_response
    import capo_opensearch.types.start_migration_request
    import capo_opensearch.types.start_migration_response
    import capo_opensearch.types.start_service_software_update_request
    import capo_opensearch.types.start_service_software_update_response
    import capo_opensearch.types.string
    import capo_opensearch.types.string_list
    import capo_opensearch.types.tag_list
    import capo_opensearch.types.update_application_request
    import capo_opensearch.types.update_application_response
    import capo_opensearch.types.update_data_source_request
    import capo_opensearch.types.update_data_source_response
    import capo_opensearch.types.update_direct_query_data_source_request
    import capo_opensearch.types.update_direct_query_data_source_response
    import capo_opensearch.types.update_domain_config_request
    import capo_opensearch.types.update_domain_config_response
    import capo_opensearch.types.update_index_request
    import capo_opensearch.types.update_index_response
    import capo_opensearch.types.update_package_request
    import capo_opensearch.types.update_package_response
    import capo_opensearch.types.update_package_scope_request
    import capo_opensearch.types.update_package_scope_response
    import capo_opensearch.types.update_scheduled_action_request
    import capo_opensearch.types.update_scheduled_action_response
    import capo_opensearch.types.update_vpc_endpoint_request
    import capo_opensearch.types.update_vpc_endpoint_response
    import capo_opensearch.types.upgrade_domain_request
    import capo_opensearch.types.upgrade_domain_response
    import capo_opensearch.types.version_string
    import capo_opensearch.types.vpc_endpoint_id
    import capo_opensearch.types.vpc_endpoint_id_list
    import capo_opensearch.types.vpc_options
    import capo_opensearch.types.workspace_configuration_input


class AsyncOpenSearchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncOpenSearchClient:
    """A client for the ``OpenSearch`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncOpenSearchClientConfig(
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
        self, config_overrides: Optional[AsyncOpenSearchClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncOpenSearchClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def accept_inbound_connection(
        self,
        connection_id: "capo_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.accept_inbound_connection_response.AcceptInboundConnectionResponse":
        """<p>Allows the destination Amazon OpenSearch Service domain owner to accept an inbound cross-cluster search connection request. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            connection_id: <p>The ID of the inbound connection to accept.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.accept_inbound_connection_request.AcceptInboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.accept_inbound_connection_response.AcceptInboundConnectionResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.accept_inbound_connection

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.accept_inbound_connection.async_accept_inbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.accept_inbound_connection_request.AcceptInboundConnectionRequest = {
            "connection_id": connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_data_source(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        name: "capo_opensearch.types.data_source_name.DataSourceName",
        data_source_type: "capo_opensearch.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "capo_opensearch.types.data_source_description.DataSourceDescription"
        ] = None,
    ) -> "capo_opensearch.types.add_data_source_response.AddDataSourceResponse":
        """<p>Creates a new direct-query data source to the specified domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html">Creating Amazon OpenSearch Service data source integrations with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain to add the data source to.</p>
            name: <p>A name for the data source.</p>
            data_source_type: <p>The type of data source.</p>
            description: <p>A description of the data source.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.add_data_source_request.AddDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.add_data_source_response.AddDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.add_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.add_data_source.async_add_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.add_data_source_request.AddDataSourceRequest = {
            "domain_name": domain_name,
            "name": name,
            "data_source_type": data_source_type,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_direct_query_data_source(
        self,
        data_source_name: "capo_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        data_source_type: "capo_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "capo_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
        ] = None,
        open_search_arns: Optional[
            "capo_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
        ] = None,
        data_source_access_policy: Optional[
            "capo_opensearch.types.policy_document.PolicyDocument"
        ] = None,
        tag_list: Optional["capo_opensearch.types.tag_list.TagList"] = None,
    ) -> "capo_opensearch.types.add_direct_query_data_source_response.AddDirectQueryDataSourceResponse":
        """<p> Adds a new data source in Amazon OpenSearch Service so that you can perform direct queries on external data. </p>

        Args:
            data_source_name: <p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>
            data_source_type: <p> The supported Amazon Web Services service that you want to use as the source for direct queries in OpenSearch Service. </p>
            description: <p> An optional text field for providing additional context and details about the data source. </p>
            open_search_arns: <p> An optional list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. This field is required for CloudWatchLogs and SecurityLake datasource types. </p>
            data_source_access_policy: <p> An optional IAM access policy document that defines the permissions for accessing the data source. The policy document must be in valid JSON format and follow IAM policy syntax.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.add_direct_query_data_source_request.AddDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.add_direct_query_data_source_response.AddDirectQueryDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.add_direct_query_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.add_direct_query_data_source.async_add_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.add_direct_query_data_source_request.AddDirectQueryDataSourceRequest = {
            "data_source_name": data_source_name,
            "data_source_type": data_source_type,
        }
        if description is not None:
            input_["description"] = description
        if open_search_arns is not None:
            input_["open_search_arns"] = open_search_arns
        if data_source_access_policy is not None:
            input_["data_source_access_policy"] = data_source_access_policy
        if tag_list is not None:
            input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_tags(
        self,
        arn: "capo_opensearch.types.arn.ARN",
        tag_list: "capo_opensearch.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> None:
        """<p>Attaches tags to an existing Amazon OpenSearch Service domain, data source, or application. </p> <p>Tags are a set of case-sensitive key-value pairs. A domain, data source, or application can have up to 10 tags. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html">Tagging Amazon OpenSearch Service resources</a>. </p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the OpenSearch Service domain, data source, or application to which you want to attach resource tags.</p>
            tag_list: <p>List of resource tags.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.add_tags_request.AddTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_opensearch._operations.amazon_open_search_service.add_tags

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.add_tags.async_add_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.add_tags_request.AddTagsRequest = {
            "arn": arn,
            "tag_list": tag_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_package(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        prerequisite_package_id_list: Optional[
            "capo_opensearch.types.package_id_list.PackageIDList"
        ] = None,
        association_configuration: Optional[
            "capo_opensearch.types.package_association_configuration.PackageAssociationConfiguration"
        ] = None,
    ) -> "capo_opensearch.types.associate_package_response.AssociatePackageResponse":
        """<p>Associates a package with an Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>Internal ID of the package to associate with a domain. Use <code>DescribePackages</code> to find this value. </p>
            domain_name: <p>Name of the domain to associate the package with.</p>
            prerequisite_package_id_list: <p>A list of package IDs that must be associated with the domain before the package specified in the request can be associated.</p>
            association_configuration: <p>The configuration for associating a package with an Amazon OpenSearch Service domain.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.associate_package_request.AssociatePackageRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.associate_package_response.AssociatePackageResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.associate_package

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.associate_package.async_associate_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.associate_package_request.AssociatePackageRequest = {
            "package_id": package_id,
            "domain_name": domain_name,
        }
        if prerequisite_package_id_list is not None:
            input_["prerequisite_package_id_list"] = prerequisite_package_id_list
        if association_configuration is not None:
            input_["association_configuration"] = association_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_packages(
        self,
        package_list: "capo_opensearch.types.package_details_for_association_list.PackageDetailsForAssociationList",
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.associate_packages_response.AssociatePackagesResponse":
        """<p>Operation in the Amazon OpenSearch Service API for associating multiple packages with a domain simultaneously.</p>

        Args:
            package_list: <p>A list of packages and their prerequisites to be associated with a domain.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.associate_packages_request.AssociatePackagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.associate_packages_response.AssociatePackagesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.associate_packages

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.associate_packages.async_associate_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.associate_packages_request.AssociatePackagesRequest = {
            "package_list": package_list,
            "domain_name": domain_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def attach_data_source(
        self,
        id: "capo_opensearch.types.id.Id",
        data_source_arn: "capo_opensearch.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        workspace_id: Optional["capo_opensearch.types.string.String"] = None,
        workspace_configuration: Optional[
            "capo_opensearch.types.workspace_configuration_input.WorkspaceConfigurationInput"
        ] = None,
        client_token: Optional["capo_opensearch.types.client_token.ClientToken"] = None,
    ) -> "capo_opensearch.types.attach_data_source_response.AttachDataSourceResponse":
        """<p>Attaches a data source to an OpenSearch application. The data source must be an Amazon OpenSearch Service domain. If both the application and the data source are active, the attachment completes immediately with a status of <code>ATTACHED</code>. Otherwise, the operation returns <code>PENDING</code> and completes the attachment automatically once both become active. If the attachment cannot be completed, its status becomes <code>FAILED</code>. This operation is idempotent: If the data source is already attached or pending, the operation returns the existing attachment.</p>

        Args:
            id: <p>The unique identifier or name of the OpenSearch application to attach the data source to. This is the same identifier used with <code>UpdateApplication</code>, <code>GetApplication</code>, and <code>DeleteApplication</code>.</p>
            workspace_id: <p>The identifier of an existing workspace to update with the new data source. Mutually exclusive with <code>workspaceConfiguration</code>.</p>
            workspace_configuration: <p>Configuration for creating a new workspace during the attachment. If specified, a workspace is created and linked to the data source after the attachment completes. Mutually exclusive with <code>workspaceId</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. If you retry a request with the same client token and the same parameters, the retry succeeds without performing any further actions.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.attach_data_source_request.AttachDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.attach_data_source_response.AttachDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.attach_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.attach_data_source.async_attach_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.attach_data_source_request.AttachDataSourceRequest = {
            "id": id,
            "data_source_arn": data_source_arn,
        }
        if workspace_id is not None:
            input_["workspace_id"] = workspace_id
        if workspace_configuration is not None:
            input_["workspace_configuration"] = workspace_configuration
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def authorize_vpc_endpoint_access(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        account: Optional["capo_opensearch.types.aws_account.AWSAccount"] = None,
        service: Optional[
            "capo_opensearch.types.aws_service_principal.AWSServicePrincipal"
        ] = None,
        service_options: Optional[
            "capo_opensearch.types.service_options.ServiceOptions"
        ] = None,
    ) -> "capo_opensearch.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse":
        """<p>Provides access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to provide access to.</p>
            account: <p>The Amazon Web Services account ID to grant access to.</p>
            service: <p>The Amazon Web Services service SP to grant access to.</p>
            service_options: <p>The options for the service, including the supported Regions for the endpoint access.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.authorize_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.authorize_vpc_endpoint_access.async_authorize_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest = {
            "domain_name": domain_name
        }
        if account is not None:
            input_["account"] = account
        if service is not None:
            input_["service"] = service
        if service_options is not None:
            input_["service_options"] = service_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_domain_config_change(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        dry_run: Optional["capo_opensearch.types.dry_run.DryRun"] = None,
    ) -> "capo_opensearch.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse":
        """<p>Cancels a pending configuration change on an Amazon OpenSearch Service domain.</p>

        Args:
            dry_run: <p>When set to <code>True</code>, returns the list of change IDs and properties that will be cancelled without actually cancelling the change.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.cancel_domain_config_change

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.cancel_domain_config_change.async_cancel_domain_config_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest = {
            "domain_name": domain_name
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_service_software_update(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.cancel_service_software_update_response.CancelServiceSoftwareUpdateResponse":
        """<p>Cancels a scheduled service software update for an Amazon OpenSearch Service domain. You can only perform this operation before the <code>AutomatedUpdateDate</code> and when the domain's <code>UpdateStatus</code> is <code>PENDING_UPDATE</code>. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html">Service software updates in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain that you want to cancel the service software update on.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.cancel_service_software_update_request.CancelServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.cancel_service_software_update_response.CancelServiceSoftwareUpdateResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.cancel_service_software_update

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.cancel_service_software_update.async_cancel_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.cancel_service_software_update_request.CancelServiceSoftwareUpdateRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_application(
        self,
        name: "capo_opensearch.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        client_token: Optional["capo_opensearch.types.client_token.ClientToken"] = None,
        data_sources: Optional["capo_opensearch.types.data_sources.DataSources"] = None,
        iam_identity_center_options: Optional[
            "capo_opensearch.types.iam_identity_center_options_input.IamIdentityCenterOptionsInput"
        ] = None,
        app_configs: Optional["capo_opensearch.types.app_configs.AppConfigs"] = None,
        tag_list: Optional["capo_opensearch.types.tag_list.TagList"] = None,
        kms_key_arn: Optional["capo_opensearch.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_opensearch.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an OpenSearch UI application. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html">Using the OpenSearch user interface in Amazon OpenSearch Service</a>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
            name: <p>The unique name of the OpenSearch application. Names must be unique within an Amazon Web Services Region for each account.</p>
            data_sources: <p>The data sources to link to the OpenSearch application.</p>
            iam_identity_center_options: <p>Configuration settings for integrating Amazon Web Services IAM Identity Center with the OpenSearch application.</p>
            app_configs: <p>Configuration settings for the OpenSearch application, including administrative options.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest. If provided, the application uses your customer-managed key for encryption. If omitted, the application uses an AWS-managed key. The KMS key must be in the same region as the application.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.create_application

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.create_application_request.CreateApplicationRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if iam_identity_center_options is not None:
            input_["iam_identity_center_options"] = iam_identity_center_options
        if app_configs is not None:
            input_["app_configs"] = app_configs
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_domain(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        engine_version: Optional[
            "capo_opensearch.types.version_string.VersionString"
        ] = None,
        cluster_config: Optional[
            "capo_opensearch.types.cluster_config.ClusterConfig"
        ] = None,
        ebs_options: Optional["capo_opensearch.types.ebs_options.EBSOptions"] = None,
        access_policies: Optional[
            "capo_opensearch.types.policy_document.PolicyDocument"
        ] = None,
        ip_address_type: Optional[
            "capo_opensearch.types.ip_address_type.IPAddressType"
        ] = None,
        snapshot_options: Optional[
            "capo_opensearch.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional["capo_opensearch.types.vpc_options.VPCOptions"] = None,
        cognito_options: Optional[
            "capo_opensearch.types.cognito_options.CognitoOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "capo_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        node_to_node_encryption_options: Optional[
            "capo_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        advanced_options: Optional[
            "capo_opensearch.types.advanced_options.AdvancedOptions"
        ] = None,
        log_publishing_options: Optional[
            "capo_opensearch.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "capo_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        advanced_security_options: Optional[
            "capo_opensearch.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        identity_center_options: Optional[
            "capo_opensearch.types.identity_center_options_input.IdentityCenterOptionsInput"
        ] = None,
        tag_list: Optional["capo_opensearch.types.tag_list.TagList"] = None,
        auto_tune_options: Optional[
            "capo_opensearch.types.auto_tune_options_input.AutoTuneOptionsInput"
        ] = None,
        off_peak_window_options: Optional[
            "capo_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
        ] = None,
        software_update_options: Optional[
            "capo_opensearch.types.software_update_options.SoftwareUpdateOptions"
        ] = None,
        aiml_options: Optional[
            "capo_opensearch.types.aiml_options_input.AIMLOptionsInput"
        ] = None,
        deployment_strategy_options: Optional[
            "capo_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "capo_opensearch.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
        use_case: Optional[
            "capo_opensearch.types.domain_use_case.DomainUseCase"
        ] = None,
        engine_mode: Optional["capo_opensearch.types.engine_mode.EngineMode"] = None,
    ) -> "capo_opensearch.types.create_domain_response.CreateDomainResponse":
        """<p>Creates an Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html">Creating and managing Amazon OpenSearch Service domains</a>.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain to create. Domain names are unique across the domains owned by an account within an Amazon Web Services Region.</p>
            engine_version: <p>String of format Elasticsearch_X.Y or OpenSearch_X.Y to specify the engine version for the OpenSearch Service domain. For example, <code>OpenSearch_1.0</code> or <code>Elasticsearch_7.9</code>. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains">Creating and managing Amazon OpenSearch Service domains</a>.</p>
            cluster_config: <p>Container for the cluster configuration of a domain.</p>
            ebs_options: <p>Container for the parameters required to enable EBS-based storage for an OpenSearch Service domain.</p>
            access_policies: <p>Identity and Access Management (IAM) policy document specifying the access policies for the new domain.</p>
            ip_address_type: <p>Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.</p>
            snapshot_options: <p>DEPRECATED. Container for the parameters required to configure automated snapshots of domain indexes.</p>
            vpc_options: <p>Container for the values required to configure VPC access domains. If you don't specify these values, OpenSearch Service creates the domain with a public endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html">Launching your Amazon OpenSearch Service domains using a VPC</a>.</p>
            cognito_options: <p>Key-value pairs to configure Amazon Cognito authentication. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html">Configuring Amazon Cognito authentication for OpenSearch Dashboards</a>.</p>
            encryption_at_rest_options: <p>Key-value pairs to enable encryption at rest.</p>
            node_to_node_encryption_options: <p>Enables node-to-node encryption.</p>
            advanced_options: <p>Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:</p> <ul> <li> <p> <code>"rest.action.multi.allow_explicit_index": "true" | "false"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>"indices.fielddata.cache.size": "80" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>"indices.query.bool.max_clause_count": "1024"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> <li> <p> <code>"override_main_response_version": "true" | "false"</code> - Note the use of a string rather than a boolean. Specifies whether the domain reports its version as 7.10 to allow Elasticsearch OSS clients and plugins to continue working with it. Default is false when creating a domain and true when upgrading a domain.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options">Advanced cluster parameters</a>.</p>
            log_publishing_options: <p>Key-value pairs to configure log publishing.</p>
            domain_endpoint_options: <p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>
            advanced_security_options: <p>Options for fine-grained access control.</p>
            identity_center_options: <p>Configuration options for enabling and managing IAM Identity Center integration within a domain.</p>
            tag_list: <p>List of tags to add to the domain upon creation.</p>
            auto_tune_options: <p>Options for Auto-Tune.</p>
            off_peak_window_options: <p>Specifies a daily 10-hour time block during which OpenSearch Service can perform configuration changes on the domain, including service software updates and Auto-Tune enhancements that require a blue/green deployment. If no options are specified, the default start time of 10:00 P.M. local time (for the Region that the domain is created in) is used.</p>
            software_update_options: <p>Software update options for the domain.</p>
            aiml_options: <p>Options for all machine learning features for the specified domain.</p>
            deployment_strategy_options: <p>Specifies the deployment strategy options for the domain.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
            use_case: <p>The primary use case for the domain. For valid values, see <code>DomainUseCase</code>.</p>
            engine_mode: <p>The engine mode for the domain. For valid values and requirements, see <code>EngineMode</code>.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access a sub-resource that's either invalid or not supported.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.create_domain

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.create_domain_request.CreateDomainRequest = {
            "domain_name": domain_name
        }
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if cluster_config is not None:
            input_["cluster_config"] = cluster_config
        if ebs_options is not None:
            input_["ebs_options"] = ebs_options
        if access_policies is not None:
            input_["access_policies"] = access_policies
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if snapshot_options is not None:
            input_["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if cognito_options is not None:
            input_["cognito_options"] = cognito_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if node_to_node_encryption_options is not None:
            input_["node_to_node_encryption_options"] = node_to_node_encryption_options
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if domain_endpoint_options is not None:
            input_["domain_endpoint_options"] = domain_endpoint_options
        if advanced_security_options is not None:
            input_["advanced_security_options"] = advanced_security_options
        if identity_center_options is not None:
            input_["identity_center_options"] = identity_center_options
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if auto_tune_options is not None:
            input_["auto_tune_options"] = auto_tune_options
        if off_peak_window_options is not None:
            input_["off_peak_window_options"] = off_peak_window_options
        if software_update_options is not None:
            input_["software_update_options"] = software_update_options
        if aiml_options is not None:
            input_["aiml_options"] = aiml_options
        if deployment_strategy_options is not None:
            input_["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input_["automated_snapshot_pause_options"] = (
                automated_snapshot_pause_options
            )
        if use_case is not None:
            input_["use_case"] = use_case
        if engine_mode is not None:
            input_["engine_mode"] = engine_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_index(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        index_name: "capo_opensearch.types.index_name.IndexName",
        index_schema: "capo_opensearch.types.index_schema.IndexSchema",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.create_index_response.CreateIndexResponse":
        """<p>Creates an OpenSearch index with optional automatic semantic enrichment for specified text fields. Automatic semantic enrichment enables semantic search capabilities without requiring machine learning expertise, improving search relevance by up to 20% by understanding search intent and contextual meaning beyond keyword matching. The semantic enrichment process has zero impact on search latency as sparse encodings are stored directly within the index during indexing. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-semantic-enrichment.html">Automatic semantic enrichment</a>.</p>

        Args:
            index_name: <p>The name of the index to create. Must be between 1 and 255 characters and follow OpenSearch naming conventions.</p>
            index_schema: <p>The JSON schema defining index mappings, settings, and semantic enrichment configuration. The schema specifies which text fields should be automatically enriched for semantic search capabilities and includes OpenSearch index configuration parameters.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Reduce the frequency of your requests and try again.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.create_index_request.CreateIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.create_index_response.CreateIndexResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.create_index

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.create_index.async_create_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.create_index_request.CreateIndexRequest = {
            "domain_name": domain_name,
            "index_name": index_name,
            "index_schema": index_schema,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_outbound_connection(
        self,
        local_domain_info: "capo_opensearch.types.domain_information_container.DomainInformationContainer",
        remote_domain_info: "capo_opensearch.types.domain_information_container.DomainInformationContainer",
        connection_alias: "capo_opensearch.types.connection_alias.ConnectionAlias",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        connection_mode: Optional[
            "capo_opensearch.types.connection_mode.ConnectionMode"
        ] = None,
        connection_properties: Optional[
            "capo_opensearch.types.connection_properties.ConnectionProperties"
        ] = None,
    ) -> "capo_opensearch.types.create_outbound_connection_response.CreateOutboundConnectionResponse":
        """<p>Creates a new cross-cluster search connection from a source Amazon OpenSearch Service domain to a destination domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            local_domain_info: <p>Name and Region of the source (local) domain.</p>
            remote_domain_info: <p>Name and Region of the destination (remote) domain.</p>
            connection_alias: <p>Name of the connection.</p>
            connection_mode: <p>The connection mode.</p>
            connection_properties: <p>The <code>ConnectionProperties</code> for the outbound connection.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.create_outbound_connection_request.CreateOutboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.create_outbound_connection_response.CreateOutboundConnectionResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.create_outbound_connection

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.create_outbound_connection.async_create_outbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.create_outbound_connection_request.CreateOutboundConnectionRequest = {
            "local_domain_info": local_domain_info,
            "remote_domain_info": remote_domain_info,
            "connection_alias": connection_alias,
        }
        if connection_mode is not None:
            input_["connection_mode"] = connection_mode
        if connection_properties is not None:
            input_["connection_properties"] = connection_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_package(
        self,
        package_name: "capo_opensearch.types.package_name.PackageName",
        package_type: "capo_opensearch.types.package_type.PackageType",
        package_source: "capo_opensearch.types.package_source.PackageSource",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        package_description: Optional[
            "capo_opensearch.types.package_description.PackageDescription"
        ] = None,
        package_configuration: Optional[
            "capo_opensearch.types.package_configuration.PackageConfiguration"
        ] = None,
        engine_version: Optional[
            "capo_opensearch.types.engine_version.EngineVersion"
        ] = None,
        package_vending_options: Optional[
            "capo_opensearch.types.package_vending_options.PackageVendingOptions"
        ] = None,
        package_encryption_options: Optional[
            "capo_opensearch.types.package_encryption_options.PackageEncryptionOptions"
        ] = None,
    ) -> "capo_opensearch.types.create_package_response.CreatePackageResponse":
        """<p>Creates a package for use with Amazon OpenSearch Service domains. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_name: <p>Unique name for the package.</p>
            package_type: <p>The type of package.</p>
            package_description: <p>Description of the package.</p>
            package_source: <p>The Amazon S3 location from which to import the package.</p>
            package_configuration: <p> The configuration parameters for the package being created.</p>
            engine_version: <p>The version of the Amazon OpenSearch Service engine for which is compatible with the package. This can only be specified for package type <code>ZIP-PLUGIN</code> </p>
            package_vending_options: <p> The vending options for the package being created. They determine if the package can be vended to other users.</p>
            package_encryption_options: <p>The encryption parameters for the package being created.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access a sub-resource that's either invalid or not supported.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.create_package_request.CreatePackageRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.create_package_response.CreatePackageResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.create_package

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.create_package.async_create_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.create_package_request.CreatePackageRequest = {
            "package_name": package_name,
            "package_type": package_type,
            "package_source": package_source,
        }
        if package_description is not None:
            input_["package_description"] = package_description
        if package_configuration is not None:
            input_["package_configuration"] = package_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if package_vending_options is not None:
            input_["package_vending_options"] = package_vending_options
        if package_encryption_options is not None:
            input_["package_encryption_options"] = package_encryption_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_vpc_endpoint(
        self,
        domain_arn: "capo_opensearch.types.domain_arn.DomainArn",
        vpc_options: "capo_opensearch.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        client_token: Optional["capo_opensearch.types.client_token.ClientToken"] = None,
    ) -> "capo_opensearch.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an Amazon OpenSearch Service-managed VPC endpoint.</p>

        Args:
            domain_arn: <p>The Amazon Resource Name (ARN) of the domain to create the endpoint for.</p>
            vpc_options: <p>Options to specify the subnets and security groups for the endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.create_vpc_endpoint

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.create_vpc_endpoint.async_create_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {
            "domain_arn": domain_arn,
            "vpc_options": vpc_options,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application(
        self,
        id: "capo_opensearch.types.id.Id",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes a specified OpenSearch application.</p>

        Args:
            id: <p>The unique identifier of the OpenSearch application to delete.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_application

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_application_request.DeleteApplicationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_source(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        name: "capo_opensearch.types.data_source_name.DataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_data_source_response.DeleteDataSourceResponse":
        """<p>Deletes a direct-query data source. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-delete.html">Deleting an Amazon OpenSearch Service data source with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            name: <p>The name of the data source to delete.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_data_source_response.DeleteDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_data_source.async_delete_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_data_source_request.DeleteDataSourceRequest = {
            "domain_name": domain_name,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_direct_query_data_source(
        self,
        data_source_name: "capo_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> None:
        """<p> Deletes a previously configured direct query data source from Amazon OpenSearch Service. </p>

        Args:
            data_source_name: <p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_direct_query_data_source_request.DeleteDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_opensearch._operations.amazon_open_search_service.delete_direct_query_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_direct_query_data_source.async_delete_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_direct_query_data_source_request.DeleteDirectQueryDataSourceRequest = {
            "data_source_name": data_source_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes an Amazon OpenSearch Service domain and all of its data. You can't recover a domain after you delete it.</p>

        Args:
            domain_name: <p>The name of the domain you want to permanently delete.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_domain

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_domain_request.DeleteDomainRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_inbound_connection(
        self,
        connection_id: "capo_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_inbound_connection_response.DeleteInboundConnectionResponse":
        """<p>Allows the destination Amazon OpenSearch Service domain owner to delete an existing inbound cross-cluster search connection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            connection_id: <p>The ID of the inbound connection to permanently delete.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_inbound_connection_request.DeleteInboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_inbound_connection_response.DeleteInboundConnectionResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_inbound_connection

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_inbound_connection.async_delete_inbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_inbound_connection_request.DeleteInboundConnectionRequest = {
            "connection_id": connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_index(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        index_name: "capo_opensearch.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_index_response.DeleteIndexResponse":
        """<p>Deletes an OpenSearch index. This operation permanently removes the index and cannot be undone.</p>

        Args:
            index_name: <p>The name of the index to delete.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Reduce the frequency of your requests and try again.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_index_request.DeleteIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_index_response.DeleteIndexResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_index

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_index.async_delete_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_index_request.DeleteIndexRequest = {
            "domain_name": domain_name,
            "index_name": index_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_outbound_connection(
        self,
        connection_id: "capo_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_outbound_connection_response.DeleteOutboundConnectionResponse":
        """<p>Allows the source Amazon OpenSearch Service domain owner to delete an existing outbound cross-cluster search connection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            connection_id: <p>The ID of the outbound connection you want to permanently delete.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_outbound_connection_request.DeleteOutboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_outbound_connection_response.DeleteOutboundConnectionResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_outbound_connection

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_outbound_connection.async_delete_outbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_outbound_connection_request.DeleteOutboundConnectionRequest = {
            "connection_id": connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_package(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_package_response.DeletePackageResponse":
        """<p>Deletes an Amazon OpenSearch Service package. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The internal ID of the package you want to delete. Use <code>DescribePackages</code> to find this value.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_package_request.DeletePackageRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_package_response.DeletePackageResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_package

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_package.async_delete_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_package_request.DeletePackageRequest = {
            "package_id": package_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vpc_endpoint(
        self,
        vpc_endpoint_id: "capo_opensearch.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>The unique identifier of the endpoint.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.delete_vpc_endpoint

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.delete_vpc_endpoint.async_delete_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {
            "vpc_endpoint_id": vpc_endpoint_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_capability(
        self,
        application_id: "capo_opensearch.types.application_id.ApplicationId",
        capability_name: "capo_opensearch.types.capability_name.CapabilityName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.deregister_capability_response.DeregisterCapabilityResponse":
        """<p>Deregisters a capability from an OpenSearch UI application. This operation removes the capability and its associated configuration.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch UI application to deregister the capability from.</p>
            capability_name: <p>The name of the capability to deregister.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.deregister_capability_request.DeregisterCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.deregister_capability_response.DeregisterCapabilityResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.deregister_capability

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.deregister_capability.async_deregister_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.deregister_capability_request.DeregisterCapabilityRequest = {
            "application_id": application_id,
            "capability_name": capability_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_data_source_attachment(
        self,
        id: "capo_opensearch.types.id.Id",
        data_source_arn: "capo_opensearch.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.describe_data_source_attachment_response.DescribeDataSourceAttachmentResponse":
        """<p>Returns the current status and details of a specific data source attachment for an OpenSearch application. Throws a <code>ResourceNotFoundException</code> if no attachment record exists for the specified application and data source combination.</p>

        Args:
            id: <p>The unique identifier or name of the OpenSearch application.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_data_source_attachment_request.DescribeDataSourceAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_data_source_attachment_response.DescribeDataSourceAttachmentResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_data_source_attachment

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_data_source_attachment.async_describe_data_source_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_data_source_attachment_request.DescribeDataSourceAttachmentRequest = {
            "id": id,
            "data_source_arn": data_source_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domain(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.describe_domain_response.DescribeDomainResponse":
        """<p>Describes the domain configuration for the specified Amazon OpenSearch Service domain, including the domain ID, domain service endpoint, and domain ARN.</p>

        Args:
            domain_name: <p>The name of the domain that you want information about.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_domain_request.DescribeDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_domain_response.DescribeDomainResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_domain

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_domain.async_describe_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_domain_request.DescribeDomainRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domain_auto_tunes(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse":
        """<p>Returns the list of optimizations that Auto-Tune has made to an Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html">Auto-Tune for Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>Name of the domain that you want Auto-Tune details about.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeDomainAutoTunes</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeDomainAutoTunes</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_domain_auto_tunes

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_domain_auto_tunes.async_describe_domain_auto_tunes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_domain_auto_tunes(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse]":
        _token = next_token
        while True:
            _response = await self.describe_domain_auto_tunes(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_domain_change_progress(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        change_id: Optional["capo_opensearch.types.guid.GUID"] = None,
    ) -> "capo_opensearch.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse":
        """<p>Returns information about the current blue/green deployment happening on an Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html">Making configuration changes in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain to get progress information for.</p>
            change_id: <p>The specific change ID for which you want to get progress information. If omitted, the request returns information about the most recent configuration change.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_domain_change_progress

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_domain_change_progress.async_describe_domain_change_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest = {
            "domain_name": domain_name
        }
        if change_id is not None:
            input_["change_id"] = change_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domain_config(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.describe_domain_config_response.DescribeDomainConfigResponse":
        """<p>Returns the configuration of an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain configuration that you want to describe.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_domain_config_request.DescribeDomainConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_domain_config_response.DescribeDomainConfigResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_domain_config

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_domain_config.async_describe_domain_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_domain_config_request.DescribeDomainConfigRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domain_health(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.describe_domain_health_response.DescribeDomainHealthResponse":
        """<p>Returns information about domain and node health, the standby Availability Zone, number of nodes per Availability Zone, and shard count per node.</p>

        Args:
            domain_name: <p>The name of the domain.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_domain_health_request.DescribeDomainHealthRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_domain_health_response.DescribeDomainHealthResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_domain_health

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_domain_health.async_describe_domain_health(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_domain_health_request.DescribeDomainHealthRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domain_nodes(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.describe_domain_nodes_response.DescribeDomainNodesResponse":
        """<p>Returns information about domain and nodes, including data nodes, master nodes, ultrawarm nodes, Availability Zone(s), standby nodes, node configurations, and node states.</p>

        Args:
            domain_name: <p>The name of the domain.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_domain_nodes_request.DescribeDomainNodesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_domain_nodes_response.DescribeDomainNodesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_domain_nodes

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_domain_nodes.async_describe_domain_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_domain_nodes_request.DescribeDomainNodesRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domains(
        self,
        domain_names: "capo_opensearch.types.domain_name_list.DomainNameList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.describe_domains_response.DescribeDomainsResponse":
        """<p>Returns domain configuration information about the specified Amazon OpenSearch Service domains.</p>

        Args:
            domain_names: <p>Array of OpenSearch Service domain names that you want information about. You must specify at least one domain name.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_domains_request.DescribeDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_domains_response.DescribeDomainsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_domains

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_domains.async_describe_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_domains_request.DescribeDomainsRequest = {
            "domain_names": domain_names
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dry_run_progress(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        dry_run_id: Optional["capo_opensearch.types.guid.GUID"] = None,
        load_dry_run_config: Optional["capo_opensearch.types.boolean.Boolean"] = None,
    ) -> "capo_opensearch.types.describe_dry_run_progress_response.DescribeDryRunProgressResponse":
        """<p>Describes the progress of a pre-update dry run analysis on an Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#dryrun">Determining whether a change will cause a blue/green deployment</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            dry_run_id: <p>The unique identifier of the dry run.</p>
            load_dry_run_config: <p>Whether to include the configuration of the dry run in the response. The configuration specifies the updates that you're planning to make on the domain.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_dry_run_progress_request.DescribeDryRunProgressRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_dry_run_progress_response.DescribeDryRunProgressResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_dry_run_progress

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_dry_run_progress.async_describe_dry_run_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_dry_run_progress_request.DescribeDryRunProgressRequest = {
            "domain_name": domain_name
        }
        if dry_run_id is not None:
            input_["dry_run_id"] = dry_run_id
        if load_dry_run_config is not None:
            input_["load_dry_run_config"] = load_dry_run_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_inbound_connections(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional["capo_opensearch.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.describe_inbound_connections_response.DescribeInboundConnectionsResponse":
        """<p>Lists all the inbound cross-cluster search connections for a destination (remote) Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            filters: <p> A list of filters used to match properties for inbound cross-cluster connections.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeInboundConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeInboundConnections</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Request processing failed because you provided an invalid pagination token.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_inbound_connections_request.DescribeInboundConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_inbound_connections_response.DescribeInboundConnectionsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_inbound_connections

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_inbound_connections.async_describe_inbound_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_inbound_connections_request.DescribeInboundConnectionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_inbound_connections(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional["capo_opensearch.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.describe_inbound_connections_response.DescribeInboundConnectionsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_inbound_connections(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_insight_details(
        self,
        entity: "capo_opensearch.types.insight_entity.InsightEntity",
        insight_id: "capo_opensearch.types.guid.GUID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        show_html_content: Optional["capo_opensearch.types.boolean.Boolean"] = None,
    ) -> "capo_opensearch.types.describe_insight_details_response.DescribeInsightDetailsResponse":
        """<p>Describes the details of an existing insight for an Amazon OpenSearch Service domain. Returns detailed fields associated with the specified insight, such as text descriptions and metric data.</p>

        Args:
            entity: <p>The entity for which to retrieve insight details. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.</p>
            insight_id: <p>The unique identifier of the insight to describe.</p>
            show_html_content: <p>Specifies whether to show response with HTML content in response or not.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_insight_details_request.DescribeInsightDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_insight_details_response.DescribeInsightDetailsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_insight_details

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_insight_details.async_describe_insight_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_insight_details_request.DescribeInsightDetailsRequest = {
            "entity": entity,
            "insight_id": insight_id,
        }
        if show_html_content is not None:
            input_["show_html_content"] = show_html_content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_instance_type_limits(
        self,
        instance_type: "capo_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType",
        engine_version: "capo_opensearch.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        domain_name: Optional["capo_opensearch.types.domain_name.DomainName"] = None,
    ) -> "capo_opensearch.types.describe_instance_type_limits_response.DescribeInstanceTypeLimitsResponse":
        """<p>Describes the instance count, storage, and master node limits for a given OpenSearch or Elasticsearch version and instance type.</p>

        Args:
            domain_name: <p>The name of the domain. Only specify if you need the limits for an existing domain.</p>
            instance_type: <p>The OpenSearch Service instance type for which you need limit information.</p>
            engine_version: <p>Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access a sub-resource that's either invalid or not supported.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_instance_type_limits_request.DescribeInstanceTypeLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_instance_type_limits_response.DescribeInstanceTypeLimitsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_instance_type_limits

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_instance_type_limits.async_describe_instance_type_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_instance_type_limits_request.DescribeInstanceTypeLimitsRequest = {
            "instance_type": instance_type,
            "engine_version": engine_version,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_outbound_connections(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional["capo_opensearch.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.describe_outbound_connections_response.DescribeOutboundConnectionsResponse":
        """<p>Lists all the outbound cross-cluster connections for a local (source) Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            filters: <p>List of filter names and values that you can use for requests.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeOutboundConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeOutboundConnections</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Request processing failed because you provided an invalid pagination token.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_outbound_connections_request.DescribeOutboundConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_outbound_connections_response.DescribeOutboundConnectionsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_outbound_connections

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_outbound_connections.async_describe_outbound_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_outbound_connections_request.DescribeOutboundConnectionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_outbound_connections(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional["capo_opensearch.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.describe_outbound_connections_response.DescribeOutboundConnectionsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_outbound_connections(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_packages(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional[
            "capo_opensearch.types.describe_packages_filter_list.DescribePackagesFilterList"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.describe_packages_response.DescribePackagesResponse":
        """<p>Describes all packages available to OpenSearch Service. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            filters: <p>Only returns packages that match the <code>DescribePackagesFilterList</code> values.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribePackageFilters</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribePackageFilters</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_packages_request.DescribePackagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_packages_response.DescribePackagesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_packages

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_packages.async_describe_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_packages_request.DescribePackagesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_packages(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional[
            "capo_opensearch.types.describe_packages_filter_list.DescribePackagesFilterList"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.describe_packages_response.DescribePackagesResponse]":
        _token = next_token
        while True:
            _response = await self.describe_packages(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_reserved_instance_offerings(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        reserved_instance_offering_id: Optional[
            "capo_opensearch.types.guid.GUID"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.describe_reserved_instance_offerings_response.DescribeReservedInstanceOfferingsResponse":
        """<p>Describes the available Amazon OpenSearch Service Reserved Instance offerings for a given Region. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html">Reserved Instances in Amazon OpenSearch Service</a>.</p>

        Args:
            reserved_instance_offering_id: <p>The Reserved Instance identifier filter value. Use this parameter to show only the available instance types that match the specified reservation identifier.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeReservedInstanceOfferings</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeReservedInstanceOfferings</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_reserved_instance_offerings_request.DescribeReservedInstanceOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_reserved_instance_offerings_response.DescribeReservedInstanceOfferingsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_reserved_instance_offerings

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_reserved_instance_offerings.async_describe_reserved_instance_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_reserved_instance_offerings_request.DescribeReservedInstanceOfferingsRequest = {}
        if reserved_instance_offering_id is not None:
            input_["reserved_instance_offering_id"] = reserved_instance_offering_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_reserved_instance_offerings(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        reserved_instance_offering_id: Optional[
            "capo_opensearch.types.guid.GUID"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.describe_reserved_instance_offerings_response.DescribeReservedInstanceOfferingsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_reserved_instance_offerings(
                config_overrides=config_overrides,
                reserved_instance_offering_id=reserved_instance_offering_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_reserved_instances(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        reserved_instance_id: Optional["capo_opensearch.types.guid.GUID"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.describe_reserved_instances_response.DescribeReservedInstancesResponse":
        """<p>Describes the Amazon OpenSearch Service instances that you have reserved in a given Region. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html">Reserved Instances in Amazon OpenSearch Service</a>.</p>

        Args:
            reserved_instance_id: <p>The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved OpenSearch instance ID.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeReservedInstances</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeReservedInstances</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_reserved_instances_request.DescribeReservedInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_reserved_instances_response.DescribeReservedInstancesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_reserved_instances

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_reserved_instances.async_describe_reserved_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_reserved_instances_request.DescribeReservedInstancesRequest = {}
        if reserved_instance_id is not None:
            input_["reserved_instance_id"] = reserved_instance_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_reserved_instances(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        reserved_instance_id: Optional["capo_opensearch.types.guid.GUID"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.describe_reserved_instances_response.DescribeReservedInstancesResponse]":
        _token = next_token
        while True:
            _response = await self.describe_reserved_instances(
                config_overrides=config_overrides,
                reserved_instance_id=reserved_instance_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_vpc_endpoints(
        self,
        vpc_endpoint_ids: "capo_opensearch.types.vpc_endpoint_id_list.VpcEndpointIdList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse":
        """<p>Describes one or more Amazon OpenSearch Service-managed VPC endpoints.</p>

        Args:
            vpc_endpoint_ids: <p>The unique identifiers of the endpoints to get information about.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.describe_vpc_endpoints

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.describe_vpc_endpoints.async_describe_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest = {
            "vpc_endpoint_ids": vpc_endpoint_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detach_data_source(
        self,
        id: "capo_opensearch.types.id.Id",
        data_source_arn: "capo_opensearch.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.detach_data_source_response.DetachDataSourceResponse":
        """<p>Removes a data source from an OpenSearch application. The application must be in the <code>ACTIVE</code> state. This operation removes the data source saved object from the application and deletes the attachment record. Throws a <code>ConflictException</code> if the specified data source has a <code>PENDING</code> attachment, and a <code>ResourceNotFoundException</code> if the data source is not currently attached to the application.</p>

        Args:
            id: <p>The unique identifier or name of the OpenSearch application to detach the data source from.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.detach_data_source_request.DetachDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.detach_data_source_response.DetachDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.detach_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.detach_data_source.async_detach_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.detach_data_source_request.DetachDataSourceRequest = {
            "id": id,
            "data_source_arn": data_source_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def dissociate_package(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.dissociate_package_response.DissociatePackageResponse":
        """<p>Removes a package from the specified Amazon OpenSearch Service domain. The package can't be in use with any OpenSearch index for the dissociation to succeed. The package is still available in OpenSearch Service for association later. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>Internal ID of the package to dissociate from the domain. Use <code>ListPackagesForDomain</code> to find this value.</p>
            domain_name: <p>Name of the domain to dissociate the package from.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.dissociate_package_request.DissociatePackageRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.dissociate_package_response.DissociatePackageResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.dissociate_package

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.dissociate_package.async_dissociate_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.dissociate_package_request.DissociatePackageRequest = {
            "package_id": package_id,
            "domain_name": domain_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def dissociate_packages(
        self,
        package_list: "capo_opensearch.types.package_id_list.PackageIDList",
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "capo_opensearch.types.dissociate_packages_response.DissociatePackagesResponse"
    ):
        """<p>Dissociates multiple packages from a domain simultaneously.</p>

        Args:
            package_list: <p>A list of package IDs to be dissociated from a domain.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.dissociate_packages_request.DissociatePackagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.dissociate_packages_response.DissociatePackagesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.dissociate_packages

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.dissociate_packages.async_dissociate_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.dissociate_packages_request.DissociatePackagesRequest = {
            "package_list": package_list,
            "domain_name": domain_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application(
        self,
        id: "capo_opensearch.types.id.Id",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_application_response.GetApplicationResponse":
        """<p>Retrieves the configuration and status of an existing OpenSearch application.</p>

        Args:
            id: <p>The unique identifier of the OpenSearch application to retrieve.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_application

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_application_request.GetApplicationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_capability(
        self,
        application_id: "capo_opensearch.types.application_id.ApplicationId",
        capability_name: "capo_opensearch.types.capability_name.CapabilityName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_capability_response.GetCapabilityResponse":
        """<p>Retrieves information about a registered capability for an OpenSearch UI application, including its configuration and current status.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch UI application.</p>
            capability_name: <p>The name of the capability to retrieve information about.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_capability_request.GetCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_capability_response.GetCapabilityResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_capability

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_capability.async_get_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_capability_request.GetCapabilityRequest = {
            "application_id": application_id,
            "capability_name": capability_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_compatible_versions(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        domain_name: Optional["capo_opensearch.types.domain_name.DomainName"] = None,
    ) -> "capo_opensearch.types.get_compatible_versions_response.GetCompatibleVersionsResponse":
        """<p>Returns a map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.</p>

        Args:
            domain_name: <p>The name of an existing domain. Provide this parameter to limit the results to a single domain.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_compatible_versions_request.GetCompatibleVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_compatible_versions_response.GetCompatibleVersionsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_compatible_versions

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_compatible_versions.async_get_compatible_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_compatible_versions_request.GetCompatibleVersionsRequest = {}
        if domain_name is not None:
            input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_source(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        name: "capo_opensearch.types.data_source_name.DataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_data_source_response.GetDataSourceResponse":
        """<p>Retrieves information about a direct query data source.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            name: <p>The name of the data source to get information about.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_data_source_request.GetDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_data_source_response.GetDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_data_source.async_get_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_data_source_request.GetDataSourceRequest = {
            "domain_name": domain_name,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_default_application_setting(
        self, *, config_overrides: Optional[AsyncOpenSearchClientConfig] = None
    ) -> "capo_opensearch.types.get_default_application_setting_response.GetDefaultApplicationSettingResponse":
        """<p>Gets the ARN of the current default application.</p> <p> If the default application isn't set, the operation returns a resource not found error.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_default_application_setting_request.GetDefaultApplicationSettingRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_default_application_setting_response.GetDefaultApplicationSettingResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_default_application_setting

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_default_application_setting.async_get_default_application_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_default_application_setting_request.GetDefaultApplicationSettingRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_direct_query_data_source(
        self,
        data_source_name: "capo_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_direct_query_data_source_response.GetDirectQueryDataSourceResponse":
        """<p> Returns detailed configuration information for a specific direct query data source in Amazon OpenSearch Service. </p>

        Args:
            data_source_name: <p> A unique, user-defined label that identifies the data source within your OpenSearch Service environment. </p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_direct_query_data_source_request.GetDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_direct_query_data_source_response.GetDirectQueryDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_direct_query_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_direct_query_data_source.async_get_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_direct_query_data_source_request.GetDirectQueryDataSourceRequest = {
            "data_source_name": data_source_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_maintenance_status(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        maintenance_id: "capo_opensearch.types.request_id.RequestId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_domain_maintenance_status_response.GetDomainMaintenanceStatusResponse":
        """<p>The status of the maintenance action.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            maintenance_id: <p>The request ID of the maintenance action.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_domain_maintenance_status_request.GetDomainMaintenanceStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_domain_maintenance_status_response.GetDomainMaintenanceStatusResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_domain_maintenance_status

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_domain_maintenance_status.async_get_domain_maintenance_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_domain_maintenance_status_request.GetDomainMaintenanceStatusRequest = {
            "domain_name": domain_name,
            "maintenance_id": maintenance_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_index(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        index_name: "capo_opensearch.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_index_response.GetIndexResponse":
        """<p>Retrieves information about an OpenSearch index including its schema and semantic enrichment configuration. Use this operation to view the current index structure and semantic search settings.</p>

        Args:
            index_name: <p>The name of the index to retrieve information about.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Reduce the frequency of your requests and try again.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_index_request.GetIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_index_response.GetIndexResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_index

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_index.async_get_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_index_request.GetIndexRequest = {
            "domain_name": domain_name,
            "index_name": index_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_migration(
        self,
        migration_id: "capo_opensearch.types.string.String",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_migration_response.GetMigrationResponse":
        """<p>Retrieves the current status and progress of a migration job, including the number of exported and imported objects and error details if the migration failed.</p>

        Args:
            migration_id: <p>The unique identifier of the migration job to retrieve.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_migration_request.GetMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_migration_response.GetMigrationResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_migration

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_migration.async_get_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_migration_request.GetMigrationRequest = {
            "migration_id": migration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_package_version_history(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.get_package_version_history_response.GetPackageVersionHistoryResponse":
        """<p>Returns a list of Amazon OpenSearch Service package versions, along with their creation time, commit message, and plugin properties (if the package is a zip plugin package). For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The unique identifier of the package.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>GetPackageVersionHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetPackageVersionHistory</code> operations, which returns results in the next page. </p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_package_version_history_request.GetPackageVersionHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_package_version_history_response.GetPackageVersionHistoryResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_package_version_history

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_package_version_history.async_get_package_version_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_package_version_history_request.GetPackageVersionHistoryRequest = {
            "package_id": package_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_package_version_history(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.get_package_version_history_response.GetPackageVersionHistoryResponse]":
        _token = next_token
        while True:
            _response = await self.get_package_version_history(
                package_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_upgrade_history(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.get_upgrade_history_response.GetUpgradeHistoryResponse":
        """<p>Retrieves the complete history of the last 10 upgrades performed on an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>The name of an existing domain.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>GetUpgradeHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetUpgradeHistory</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_upgrade_history_request.GetUpgradeHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_upgrade_history_response.GetUpgradeHistoryResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_upgrade_history

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_upgrade_history.async_get_upgrade_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_upgrade_history_request.GetUpgradeHistoryRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_upgrade_history(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.get_upgrade_history_response.GetUpgradeHistoryResponse]":
        _token = next_token
        while True:
            _response = await self.get_upgrade_history(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_upgrade_status(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.get_upgrade_status_response.GetUpgradeStatusResponse":
        """<p>Returns the most recent status of the last upgrade or upgrade eligibility check performed on an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>The domain of the domain to get upgrade status information for.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.get_upgrade_status_request.GetUpgradeStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.get_upgrade_status_response.GetUpgradeStatusResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.get_upgrade_status

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.get_upgrade_status.async_get_upgrade_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.get_upgrade_status_request.GetUpgradeStatusRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def insight_feedback(
        self,
        entity: "capo_opensearch.types.insight_feedback_entity.InsightFeedbackEntity",
        insight_id: "capo_opensearch.types.guid.GUID",
        thumbs: "capo_opensearch.types.insight_feedback_thumbs.InsightFeedbackThumbs",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        feedback_text: Optional[
            "capo_opensearch.types.insight_feedback_text.InsightFeedbackText"
        ] = None,
    ) -> "capo_opensearch.types.insight_feedback_response.InsightFeedbackResponse":
        """<p>Submits feedback for an existing insight in an Amazon OpenSearch Service domain. Allows users to provide a thumbs up or thumbs down rating and optional text feedback for a specific insight.</p>

        Args:
            entity: <p>The entity for which to submit insight feedback. Specifies the type and value of the entity, such as a domain name.</p>
            insight_id: <p>The unique identifier of the insight for which to submit feedback.</p>
            thumbs: <p>The thumbs up or thumbs down feedback for the insight. Possible values are <code>Up</code> and <code>Down</code>.</p>
            feedback_text: <p>Optional text feedback providing additional details about the insight. Maximum length is 1000 characters.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.insight_feedback_request.InsightFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.insight_feedback_response.InsightFeedbackResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.insight_feedback

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.insight_feedback.async_insight_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.insight_feedback_request.InsightFeedbackRequest = {
            "entity": entity,
            "insight_id": insight_id,
            "thumbs": thumbs,
        }
        if feedback_text is not None:
            input_["feedback_text"] = feedback_text

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
        statuses: Optional[
            "capo_opensearch.types.application_statuses.ApplicationStatuses"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
    ) -> "capo_opensearch.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists all OpenSearch applications under your account.</p>

        Args:
            statuses: <p>Filters the list of OpenSearch applications by status. Possible values: <code>CREATING</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>FAILED</code>, <code>ACTIVE</code>, and <code>DELETED</code>.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_applications

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if statuses is not None:
            input_["statuses"] = statuses
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
        statuses: Optional[
            "capo_opensearch.types.application_statuses.ApplicationStatuses"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                statuses=statuses,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_source_attachments(
        self,
        id: "capo_opensearch.types.id.Id",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["capo_opensearch.types.string.String"] = None,
        max_results: Optional["capo_opensearch.types.integer.Integer"] = None,
    ) -> "capo_opensearch.types.list_data_source_attachments_response.ListDataSourceAttachmentsResponse":
        """<p>Returns a paginated list of all data source attachments for an OpenSearch application, including attachments in all states (<code>PENDING</code>, <code>ATTACHED</code>, and <code>FAILED</code>).</p>

        Args:
            id: <p>The unique identifier or name of the OpenSearch application to list attachments for.</p>
            next_token: <p>The pagination token from a previous call to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page. The default is 50.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_data_source_attachments_request.ListDataSourceAttachmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_data_source_attachments_response.ListDataSourceAttachmentsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_data_source_attachments

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_data_source_attachments.async_list_data_source_attachments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_data_source_attachments_request.ListDataSourceAttachmentsRequest = {
            "id": id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_sources(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.list_data_sources_response.ListDataSourcesResponse":
        """<p>Lists direct-query data sources for a specific domain. For more information, see For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3.html">Working with Amazon OpenSearch Service direct queries with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_data_sources

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_data_sources.async_list_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_data_sources_request.ListDataSourcesRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_direct_query_data_sources(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_direct_query_data_sources_response.ListDirectQueryDataSourcesResponse":
        """<p> Lists an inventory of all the direct query data sources that you have configured within Amazon OpenSearch Service. </p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_direct_query_data_sources_request.ListDirectQueryDataSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_direct_query_data_sources_response.ListDirectQueryDataSourcesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_direct_query_data_sources

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_direct_query_data_sources.async_list_direct_query_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_direct_query_data_sources_request.ListDirectQueryDataSourcesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_domain_maintenances(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        action: Optional[
            "capo_opensearch.types.maintenance_type.MaintenanceType"
        ] = None,
        status: Optional[
            "capo_opensearch.types.maintenance_status.MaintenanceStatus"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_domain_maintenances_response.ListDomainMaintenancesResponse":
        """<p>A list of maintenance actions for the domain.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            action: <p>The name of the action.</p>
            status: <p>The status of the action.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListDomainMaintenances</code> operation returns a <code>nextToken</code>, include the returned <code>nextToken</code> in subsequent <code>ListDomainMaintenances</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_domain_maintenances_request.ListDomainMaintenancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_domain_maintenances_response.ListDomainMaintenancesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_domain_maintenances

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_domain_maintenances.async_list_domain_maintenances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_domain_maintenances_request.ListDomainMaintenancesRequest = {
            "domain_name": domain_name
        }
        if action is not None:
            input_["action"] = action
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_domain_maintenances(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        action: Optional[
            "capo_opensearch.types.maintenance_type.MaintenanceType"
        ] = None,
        status: Optional[
            "capo_opensearch.types.maintenance_status.MaintenanceStatus"
        ] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.list_domain_maintenances_response.ListDomainMaintenancesResponse]":
        _token = next_token
        while True:
            _response = await self.list_domain_maintenances(
                domain_name,
                config_overrides=config_overrides,
                action=action,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_domain_names(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        engine_type: Optional["capo_opensearch.types.engine_type.EngineType"] = None,
    ) -> "capo_opensearch.types.list_domain_names_response.ListDomainNamesResponse":
        """<p>Returns the names of all Amazon OpenSearch Service domains owned by the current user in the active Region.</p>

        Args:
            engine_type: <p>Filters the output by domain engine type.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_domain_names_request.ListDomainNamesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_domain_names_response.ListDomainNamesResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_domain_names

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_domain_names.async_list_domain_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_domain_names_request.ListDomainNamesRequest = {}
        if engine_type is not None:
            input_["engine_type"] = engine_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_domains_for_package(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_domains_for_package_response.ListDomainsForPackageResponse":
        """<p>Lists all Amazon OpenSearch Service domains associated with a given package. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The unique identifier of the package for which to list associated domains.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListDomainsForPackage</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListDomainsForPackage</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_domains_for_package_request.ListDomainsForPackageRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_domains_for_package_response.ListDomainsForPackageResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_domains_for_package

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_domains_for_package.async_list_domains_for_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_domains_for_package_request.ListDomainsForPackageRequest = {
            "package_id": package_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_domains_for_package(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.list_domains_for_package_response.ListDomainsForPackageResponse]":
        _token = next_token
        while True:
            _response = await self.list_domains_for_package(
                package_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_insights(
        self,
        entity: "capo_opensearch.types.insight_entity.InsightEntity",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        time_range: Optional[
            "capo_opensearch.types.insight_time_range.InsightTimeRange"
        ] = None,
        sort_order: Optional[
            "capo_opensearch.types.insight_sort_order.InsightSortOrder"
        ] = None,
        max_results: Optional[
            "capo_opensearch.types.insight_page_size.InsightPageSize"
        ] = None,
        next_token: Optional["capo_opensearch.types.string.String"] = None,
    ) -> "capo_opensearch.types.list_insights_response.ListInsightsResponse":
        """<p>Lists insights for an Amazon OpenSearch Service domain or Amazon Web Services account. Returns a paginated list of insights based on the specified entity, filters, time range, and sort order.</p>

        Args:
            entity: <p>The entity for which to list insights. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.</p>
            time_range: <p>The time range for filtering insights, specified as epoch millisecond timestamps.</p>
            sort_order: <p>The sort order for the results. Possible values are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>NextToken</code> to get the next page of results. Valid values are 1 to 500.</p>
            next_token: <p>If your initial <code>ListInsights</code> operation returns a <code>NextToken</code>, include the returned <code>NextToken</code> in subsequent <code>ListInsights</code> operations to retrieve the next page of results.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_insights_request.ListInsightsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_insights_response.ListInsightsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_insights

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_insights.async_list_insights(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_insights_request.ListInsightsRequest = {
            "entity": entity
        }
        if time_range is not None:
            input_["time_range"] = time_range
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_instance_type_details(
        self,
        engine_version: "capo_opensearch.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        domain_name: Optional["capo_opensearch.types.domain_name.DomainName"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
        retrieve_a_zs: Optional["capo_opensearch.types.boolean.Boolean"] = None,
        instance_type: Optional[
            "capo_opensearch.types.instance_type_string.InstanceTypeString"
        ] = None,
    ) -> "capo_opensearch.types.list_instance_type_details_response.ListInstanceTypeDetailsResponse":
        """<p>Lists all instance types and available features for a given OpenSearch or Elasticsearch version.</p>

        Args:
            engine_version: <p>The version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>
            domain_name: <p>The name of the domain.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListInstanceTypeDetails</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListInstanceTypeDetails</code> operations, which returns results in the next page.</p>
            retrieve_a_zs: <p>An optional parameter that specifies the Availability Zones for the domain.</p>
            instance_type: <p>An optional parameter that lists information for a given instance type.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_instance_type_details_request.ListInstanceTypeDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_instance_type_details_response.ListInstanceTypeDetailsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_instance_type_details

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_instance_type_details.async_list_instance_type_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_instance_type_details_request.ListInstanceTypeDetailsRequest = {
            "engine_version": engine_version
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if retrieve_a_zs is not None:
            input_["retrieve_a_zs"] = retrieve_a_zs
        if instance_type is not None:
            input_["instance_type"] = instance_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_instance_type_details(
        self,
        engine_version: "capo_opensearch.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        domain_name: Optional["capo_opensearch.types.domain_name.DomainName"] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
        retrieve_a_zs: Optional["capo_opensearch.types.boolean.Boolean"] = None,
        instance_type: Optional[
            "capo_opensearch.types.instance_type_string.InstanceTypeString"
        ] = None,
    ) -> "AsyncIterator[capo_opensearch.types.list_instance_type_details_response.ListInstanceTypeDetailsResponse]":
        _token = next_token
        while True:
            _response = await self.list_instance_type_details(
                engine_version,
                config_overrides=config_overrides,
                domain_name=domain_name,
                max_results=max_results,
                next_token=_token,
                retrieve_a_zs=retrieve_a_zs,
                instance_type=instance_type,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_migrations(
        self,
        application_id: "capo_opensearch.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        status: Optional["capo_opensearch.types.string.String"] = None,
        max_results: Optional["capo_opensearch.types.integer.Integer"] = None,
        next_token: Optional["capo_opensearch.types.string.String"] = None,
    ) -> "capo_opensearch.types.list_migrations_response.ListMigrationsResponse":
        """<p>Lists migration jobs for an Amazon OpenSearch Service application. You can filter results by migration status. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch application to list migrations for.</p>
            status: <p>Filters the results by migration status. Valid values are <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>SUCCEEDED</code>, and <code>FAILED</code>.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call to retrieve the next set of results.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_migrations_request.ListMigrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_migrations_response.ListMigrationsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_migrations

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_migrations.async_list_migrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_migrations_request.ListMigrationsRequest = {
            "application_id": application_id
        }
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_packages_for_domain(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_packages_for_domain_response.ListPackagesForDomainResponse":
        """<p>Lists all packages associated with an Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain for which you want to list associated packages.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListPackagesForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPackagesForDomain</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_packages_for_domain_request.ListPackagesForDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_packages_for_domain_response.ListPackagesForDomainResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_packages_for_domain

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_packages_for_domain.async_list_packages_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_packages_for_domain_request.ListPackagesForDomainRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_packages_for_domain(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.list_packages_for_domain_response.ListPackagesForDomainResponse]":
        _token = next_token
        while True:
            _response = await self.list_packages_for_domain(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_scheduled_actions(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_scheduled_actions_response.ListScheduledActionsResponse":
        """<p>Retrieves a list of configuration changes that are scheduled for a domain. These changes can be <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html">service software updates</a> or <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types">blue/green Auto-Tune enhancements</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListScheduledActions</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListScheduledActions</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Request processing failed because you provided an invalid pagination token.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_scheduled_actions_request.ListScheduledActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_scheduled_actions_response.ListScheduledActionsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_scheduled_actions

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_scheduled_actions.async_list_scheduled_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_scheduled_actions_request.ListScheduledActionsRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_scheduled_actions(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.list_scheduled_actions_response.ListScheduledActionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_scheduled_actions(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags(
        self,
        arn: "capo_opensearch.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.list_tags_response.ListTagsResponse":
        """<p>Returns all resource tags for an Amazon OpenSearch Service domain, data source, or application. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html">Tagging Amazon OpenSearch Service resources</a>.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the domain, data source, or application to view tags for.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_tags_response.ListTagsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_tags

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_tags_request.ListTagsRequest = {"arn": arn}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_versions(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_versions_response.ListVersionsResponse":
        """<p>Lists all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.</p>

        Args:
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListVersions</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVersions</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_versions_request.ListVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_versions_response.ListVersionsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_versions

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_versions.async_list_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_versions_request.ListVersionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_versions(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["capo_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_opensearch.types.list_versions_response.ListVersionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_vpc_endpoint_access(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse":
        """<p>Retrieves information about each Amazon Web Services principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to retrieve access information for.</p>
            next_token: <p>If your initial <code>ListVpcEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpointAccess</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_vpc_endpoint_access.async_list_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest = {
            "domain_name": domain_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_vpc_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current Amazon Web Services account and Region.</p>

        Args:
            next_token: <p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_vpc_endpoints

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_vpc_endpoints.async_list_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_vpc_endpoints_for_domain(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["capo_opensearch.types.next_token.NextToken"] = None,
    ) -> "capo_opensearch.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse":
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain.</p>

        Args:
            domain_name: <p>The name of the domain to list associated VPC endpoints for.</p>
            next_token: <p>If your initial <code>ListEndpointsForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListEndpointsForDomain</code> operations, which returns results in the next page.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.list_vpc_endpoints_for_domain

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.list_vpc_endpoints_for_domain.async_list_vpc_endpoints_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest = {
            "domain_name": domain_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def purchase_reserved_instance_offering(
        self,
        reserved_instance_offering_id: "capo_opensearch.types.guid.GUID",
        reservation_name: "capo_opensearch.types.reservation_token.ReservationToken",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        instance_count: Optional[
            "capo_opensearch.types.instance_count.InstanceCount"
        ] = None,
    ) -> "capo_opensearch.types.purchase_reserved_instance_offering_response.PurchaseReservedInstanceOfferingResponse":
        """<p>Allows you to purchase Amazon OpenSearch Service Reserved Instances.</p>

        Args:
            reserved_instance_offering_id: <p>The ID of the Reserved Instance offering to purchase.</p>
            reservation_name: <p>A customer-specified identifier to track this reservation.</p>
            instance_count: <p>The number of OpenSearch instances to reserve.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.purchase_reserved_instance_offering_request.PurchaseReservedInstanceOfferingRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.purchase_reserved_instance_offering_response.PurchaseReservedInstanceOfferingResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.purchase_reserved_instance_offering

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.purchase_reserved_instance_offering.async_purchase_reserved_instance_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.purchase_reserved_instance_offering_request.PurchaseReservedInstanceOfferingRequest = {
            "reserved_instance_offering_id": reserved_instance_offering_id,
            "reservation_name": reservation_name,
        }
        if instance_count is not None:
            input_["instance_count"] = instance_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_default_application_setting(
        self,
        application_arn: "capo_opensearch.types.arn.ARN",
        set_as_default: "capo_opensearch.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.put_default_application_setting_response.PutDefaultApplicationSettingResponse":
        """<p>Sets the default application to the application with the specified ARN.</p> <p> To remove the default application, use the <code>GetDefaultApplicationSetting</code> operation to get the current default and then call the <code>PutDefaultApplicationSetting</code> with the current applications ARN and the <code>setAsDefault</code> parameter set to <code>false</code>.</p>

        Args:
            set_as_default: <p>Set to true to set the specified ARN as the default application. Set to false to clear the default application.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.put_default_application_setting_request.PutDefaultApplicationSettingRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.put_default_application_setting_response.PutDefaultApplicationSettingResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.put_default_application_setting

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.put_default_application_setting.async_put_default_application_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.put_default_application_setting_request.PutDefaultApplicationSettingRequest = {
            "application_arn": application_arn,
            "set_as_default": set_as_default,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_capability(
        self,
        application_id: "capo_opensearch.types.application_id.ApplicationId",
        capability_name: "capo_opensearch.types.capability_name.CapabilityName",
        capability_config: "capo_opensearch.types.capability_base_request_config.CapabilityBaseRequestConfig",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "capo_opensearch.types.register_capability_response.RegisterCapabilityResponse"
    ):
        """<p>Registers a capability for an OpenSearch UI application. Use this operation to enable specific capabilities, such as AI features, for a given application. The capability configuration defines the type and settings of the capability to register. For more information about the AI features, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-ai-assistant.html">Agentic AI for OpenSearch UI</a>.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch UI application to register the capability for.</p>
            capability_name: <p>The name of the capability to register. Must be between 3 and 30 characters and contain only alphanumeric characters and hyphens. This identifies the type of capability being enabled for the application. For registering AI Assistant capability, use <code>ai-capability</code> </p>
            capability_config: <p>The configuration settings for the capability being registered. This includes capability-specific settings such as AI configuration.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>An exception for when a request would cause a service quota to be exceeded.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.register_capability_request.RegisterCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.register_capability_response.RegisterCapabilityResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.register_capability

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.register_capability.async_register_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.register_capability_request.RegisterCapabilityRequest = {
            "application_id": application_id,
            "capability_name": capability_name,
            "capability_config": capability_config,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_inbound_connection(
        self,
        connection_id: "capo_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.reject_inbound_connection_response.RejectInboundConnectionResponse":
        """<p>Allows the remote Amazon OpenSearch Service domain owner to reject an inbound cross-cluster connection request.</p>

        Args:
            connection_id: <p>The unique identifier of the inbound connection to reject.</p>

        Raises:
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.reject_inbound_connection_request.RejectInboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.reject_inbound_connection_response.RejectInboundConnectionResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.reject_inbound_connection

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.reject_inbound_connection.async_reject_inbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.reject_inbound_connection_request.RejectInboundConnectionRequest = {
            "connection_id": connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags(
        self,
        arn: "capo_opensearch.types.arn.ARN",
        tag_keys: "capo_opensearch.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> None:
        """<p>Removes the specified set of tags from an Amazon OpenSearch Service domain, data source, or application. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains.html#managedomains-awsresorcetagging"> Tagging Amazon OpenSearch Service resources</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the domain, data source, or application from which you want to delete the specified tags.</p>
            tag_keys: <p>The list of tag keys to remove from the domain, data source, or application.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.remove_tags_request.RemoveTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_opensearch._operations.amazon_open_search_service.remove_tags

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.remove_tags.async_remove_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.remove_tags_request.RemoveTagsRequest = {
            "arn": arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_vpc_endpoint_access(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        account: Optional["capo_opensearch.types.aws_account.AWSAccount"] = None,
        service: Optional[
            "capo_opensearch.types.aws_service_principal.AWSServicePrincipal"
        ] = None,
        service_options: Optional[
            "capo_opensearch.types.service_options.ServiceOptions"
        ] = None,
    ) -> "capo_opensearch.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse":
        """<p>Revokes access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain.</p>
            account: <p>The account ID to revoke access from.</p>
            service: <p>The service SP to revoke access from.</p>
            service_options: <p>The options for the service, including the supported Regions for the endpoint access.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.revoke_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.revoke_vpc_endpoint_access.async_revoke_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest = {
            "domain_name": domain_name
        }
        if account is not None:
            input_["account"] = account
        if service is not None:
            input_["service"] = service
        if service_options is not None:
            input_["service_options"] = service_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rollback_service_software_update(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.rollback_service_software_update_response.RollbackServiceSoftwareUpdateResponse":
        """<p>Rolls back a service software update for a domain to the previous version. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html">Service software updates in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain to roll back the service software update on.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.rollback_service_software_update_request.RollbackServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.rollback_service_software_update_response.RollbackServiceSoftwareUpdateResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.rollback_service_software_update

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.rollback_service_software_update.async_rollback_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.rollback_service_software_update_request.RollbackServiceSoftwareUpdateRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_domain_maintenance(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        action: "capo_opensearch.types.maintenance_type.MaintenanceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        node_id: Optional["capo_opensearch.types.node_id.NodeId"] = None,
    ) -> "capo_opensearch.types.start_domain_maintenance_response.StartDomainMaintenanceResponse":
        """<p>Starts the node maintenance process on the data node. These processes can include a node reboot, an Opensearch or Elasticsearch process restart, or a Dashboard or Kibana restart.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            action: <p>The name of the action.</p>
            node_id: <p>The ID of the data node.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.start_domain_maintenance_request.StartDomainMaintenanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.start_domain_maintenance_response.StartDomainMaintenanceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.start_domain_maintenance

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.start_domain_maintenance.async_start_domain_maintenance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.start_domain_maintenance_request.StartDomainMaintenanceRequest = {
            "domain_name": domain_name,
            "action": action,
        }
        if node_id is not None:
            input_["node_id"] = node_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_migration(
        self,
        application_id: "capo_opensearch.types.application_id.ApplicationId",
        migration_options: "capo_opensearch.types.migration_options.MigrationOptions",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        client_token: Optional["capo_opensearch.types.client_token.ClientToken"] = None,
    ) -> "capo_opensearch.types.start_migration_response.StartMigrationResponse":
        """<p>Initiates a migration job to migrate saved objects from a data source to an Amazon OpenSearch Service application workspace. Saved objects include dashboards, visualizations, index patterns, and searches. You can specify export filters to control the scope of the migration and a conflict resolution strategy for handling existing objects in the target workspace.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch application to migrate saved objects into.</p>
            migration_options: <p>The configuration options for the migration, including the source data source, target workspace, export filters, and conflict resolution strategy.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon OpenSearch Service ignores the request but does not return an error.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.start_migration_request.StartMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.start_migration_response.StartMigrationResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.start_migration

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.start_migration.async_start_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.start_migration_request.StartMigrationRequest = {
            "application_id": application_id,
            "migration_options": migration_options,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_service_software_update(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        schedule_at: Optional["capo_opensearch.types.schedule_at.ScheduleAt"] = None,
        desired_start_time: Optional["capo_opensearch.types.long.Long"] = None,
    ) -> "capo_opensearch.types.start_service_software_update_response.StartServiceSoftwareUpdateResponse":
        """<p>Schedules a service software update for an Amazon OpenSearch Service domain. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html">Service software updates in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain that you want to update to the latest service software.</p>
            schedule_at: <p>When to start the service software update.</p> <ul> <li> <p> <code>NOW</code> - Immediately schedules the update to happen in the current hour if there's capacity available.</p> </li> <li> <p> <code>TIMESTAMP</code> - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for <code>DesiredStartTime</code>.</p> </li> <li> <p> <code>OFF_PEAK_WINDOW</code> - Marks the update to be picked up during an upcoming off-peak window. There's no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days.</p> </li> </ul> <p>Default: <code>NOW</code> if you don't specify a value for <code>DesiredStartTime</code>, and <code>TIMESTAMP</code> if you do.</p>
            desired_start_time: <p>The Epoch timestamp when you want the service software update to start. You only need to specify this parameter if you set <code>ScheduleAt</code> to <code>TIMESTAMP</code>.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.start_service_software_update_request.StartServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.start_service_software_update_response.StartServiceSoftwareUpdateResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.start_service_software_update

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.start_service_software_update.async_start_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.start_service_software_update_request.StartServiceSoftwareUpdateRequest = {
            "domain_name": domain_name
        }
        if schedule_at is not None:
            input_["schedule_at"] = schedule_at
        if desired_start_time is not None:
            input_["desired_start_time"] = desired_start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application(
        self,
        id: "capo_opensearch.types.id.Id",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        data_sources: Optional["capo_opensearch.types.data_sources.DataSources"] = None,
        app_configs: Optional["capo_opensearch.types.app_configs.AppConfigs"] = None,
        iam_identity_center_options: Optional[
            "capo_opensearch.types.iam_identity_center_options_input.IamIdentityCenterOptionsInput"
        ] = None,
    ) -> "capo_opensearch.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates the configuration and settings of an existing OpenSearch application.</p>

        Args:
            id: <p>The unique identifier for the OpenSearch application to be updated.</p>
            data_sources: <p>The data sources to associate with the OpenSearch application.</p>
            app_configs: <p>The configuration settings to modify for the OpenSearch application.</p>
            iam_identity_center_options: <p>Configuration settings for integrating IAM Identity Center with the OpenSearch application.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_application

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_application_request.UpdateApplicationRequest = {
            "id": id
        }
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if app_configs is not None:
            input_["app_configs"] = app_configs
        if iam_identity_center_options is not None:
            input_["iam_identity_center_options"] = iam_identity_center_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_source(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        name: "capo_opensearch.types.data_source_name.DataSourceName",
        data_source_type: "capo_opensearch.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "capo_opensearch.types.data_source_description.DataSourceDescription"
        ] = None,
        status: Optional[
            "capo_opensearch.types.data_source_status.DataSourceStatus"
        ] = None,
    ) -> "capo_opensearch.types.update_data_source_response.UpdateDataSourceResponse":
        """<p>Updates a direct-query data source. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html">Working with Amazon OpenSearch Service data source integrations with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            name: <p>The name of the data source to modify.</p>
            data_source_type: <p>The type of data source.</p>
            description: <p>A new description of the data source.</p>
            status: <p>The status of the data source update.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_data_source_response.UpdateDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_data_source.async_update_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_data_source_request.UpdateDataSourceRequest = {
            "domain_name": domain_name,
            "name": name,
            "data_source_type": data_source_type,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_direct_query_data_source(
        self,
        data_source_name: "capo_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        data_source_type: "capo_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "capo_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
        ] = None,
        open_search_arns: Optional[
            "capo_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
        ] = None,
        data_source_access_policy: Optional[
            "capo_opensearch.types.policy_document.PolicyDocument"
        ] = None,
    ) -> "capo_opensearch.types.update_direct_query_data_source_response.UpdateDirectQueryDataSourceResponse":
        """<p> Updates the configuration or properties of an existing direct query data source in Amazon OpenSearch Service. </p>

        Args:
            data_source_name: <p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>
            data_source_type: <p> The supported Amazon Web Services service that you want to use as the source for direct queries in OpenSearch Service. </p>
            description: <p> An optional text field for providing additional context and details about the data source. </p>
            open_search_arns: <p> An optional list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. This field is required for CloudWatchLogs and SecurityLake datasource types. </p>
            data_source_access_policy: <p> An optional IAM access policy document that defines the updated permissions for accessing the direct query data source. The policy document must be in valid JSON format and follow IAM policy syntax. If not specified, the existing access policy if present remains unchanged. </p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_direct_query_data_source_request.UpdateDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_direct_query_data_source_response.UpdateDirectQueryDataSourceResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_direct_query_data_source

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_direct_query_data_source.async_update_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_direct_query_data_source_request.UpdateDirectQueryDataSourceRequest = {
            "data_source_name": data_source_name,
            "data_source_type": data_source_type,
        }
        if description is not None:
            input_["description"] = description
        if open_search_arns is not None:
            input_["open_search_arns"] = open_search_arns
        if data_source_access_policy is not None:
            input_["data_source_access_policy"] = data_source_access_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain_config(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        cluster_config: Optional[
            "capo_opensearch.types.cluster_config.ClusterConfig"
        ] = None,
        ebs_options: Optional["capo_opensearch.types.ebs_options.EBSOptions"] = None,
        snapshot_options: Optional[
            "capo_opensearch.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional["capo_opensearch.types.vpc_options.VPCOptions"] = None,
        cognito_options: Optional[
            "capo_opensearch.types.cognito_options.CognitoOptions"
        ] = None,
        advanced_options: Optional[
            "capo_opensearch.types.advanced_options.AdvancedOptions"
        ] = None,
        access_policies: Optional[
            "capo_opensearch.types.policy_document.PolicyDocument"
        ] = None,
        ip_address_type: Optional[
            "capo_opensearch.types.ip_address_type.IPAddressType"
        ] = None,
        log_publishing_options: Optional[
            "capo_opensearch.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "capo_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "capo_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        node_to_node_encryption_options: Optional[
            "capo_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        advanced_security_options: Optional[
            "capo_opensearch.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        identity_center_options: Optional[
            "capo_opensearch.types.identity_center_options_input.IdentityCenterOptionsInput"
        ] = None,
        auto_tune_options: Optional[
            "capo_opensearch.types.auto_tune_options.AutoTuneOptions"
        ] = None,
        dry_run: Optional["capo_opensearch.types.dry_run.DryRun"] = None,
        dry_run_mode: Optional["capo_opensearch.types.dry_run_mode.DryRunMode"] = None,
        off_peak_window_options: Optional[
            "capo_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
        ] = None,
        software_update_options: Optional[
            "capo_opensearch.types.software_update_options.SoftwareUpdateOptions"
        ] = None,
        aiml_options: Optional[
            "capo_opensearch.types.aiml_options_input.AIMLOptionsInput"
        ] = None,
        deployment_strategy_options: Optional[
            "capo_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "capo_opensearch.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
        use_case: Optional[
            "capo_opensearch.types.domain_use_case.DomainUseCase"
        ] = None,
        engine_mode: Optional["capo_opensearch.types.engine_mode.EngineMode"] = None,
        accepted_warnings: Optional[
            "capo_opensearch.types.accepted_warnings_list.AcceptedWarningsList"
        ] = None,
    ) -> (
        "capo_opensearch.types.update_domain_config_response.UpdateDomainConfigResponse"
    ):
        """<p>Modifies the cluster configuration of the specified Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>The name of the domain that you're updating.</p>
            cluster_config: <p>Changes that you want to make to the cluster configuration, such as the instance type and number of EC2 instances.</p>
            ebs_options: <p>The type and size of the EBS volume to attach to instances in the domain.</p>
            snapshot_options: <p>Option to set the time, in UTC format, for the daily automated snapshot. Default value is <code>0</code> hours. </p>
            vpc_options: <p>Options to specify the subnets and security groups for a VPC endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html">Launching your Amazon OpenSearch Service domains using a VPC</a>.</p>
            cognito_options: <p>Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.</p>
            advanced_options: <p>Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:</p> <ul> <li> <p> <code>"rest.action.multi.allow_explicit_index": "true" | "false"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>"indices.fielddata.cache.size": "80" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>"indices.query.bool.max_clause_count": "1024"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options">Advanced cluster parameters</a>.</p>
            access_policies: <p>Identity and Access Management (IAM) access policy as a JSON-formatted string.</p>
            ip_address_type: <p>Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If your IP address type is currently set to dual stack, you can't change it. </p>
            log_publishing_options: <p>Options to publish OpenSearch logs to Amazon CloudWatch Logs.</p>
            encryption_at_rest_options: <p>Encryption at rest options for the domain.</p>
            domain_endpoint_options: <p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>
            node_to_node_encryption_options: <p>Node-to-node encryption options for the domain.</p>
            advanced_security_options: <p>Options for fine-grained access control.</p>
            auto_tune_options: <p>Options for Auto-Tune.</p>
            dry_run: <p>This flag, when set to True, specifies whether the <code>UpdateDomain</code> request should return the results of a dry run analysis without actually applying the change. A dry run determines what type of deployment the update will cause.</p>
            dry_run_mode: <p>The type of dry run to perform.</p> <ul> <li> <p> <code>Basic</code> only returns the type of deployment (blue/green or dynamic) that the update will cause.</p> </li> <li> <p> <code>Verbose</code> runs an additional check to validate the changes you're making. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#validation-check">Validating a domain update</a>.</p> </li> </ul>
            off_peak_window_options: <p>Off-peak window options for the domain.</p>
            software_update_options: <p>Service software update options for the domain.</p>
            aiml_options: <p>Options for all machine learning features for the specified domain.</p>
            deployment_strategy_options: <p>Specifies the deployment strategy options for the domain.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
            use_case: <p>The primary use case for the domain. For valid values, see <code>DomainUseCase</code>.</p>
            engine_mode: <p>The engine mode for the domain. The engine mode can't be changed after the domain is created. For valid values, see <code>EngineMode</code>.</p>
            accepted_warnings: <p>A list of advisory warning codes to accept for this configuration change. By default, any advisory warning blocks the change. Include the code of each warning you want to accept so the change can proceed. You can find warning codes in the <code>ValidationFailures</code> list returned by <code>DescribeDomainChangeProgress</code> and <code>DescribeDryRunProgress</code>. Critical validation failures cannot be accepted and always block the change. If you omit this parameter or pass an empty list, all warnings block the change. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#validation-check">Validating a domain update</a>.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access a sub-resource that's either invalid or not supported.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_domain_config_request.UpdateDomainConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_domain_config_response.UpdateDomainConfigResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_domain_config

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_domain_config.async_update_domain_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_domain_config_request.UpdateDomainConfigRequest = {
            "domain_name": domain_name
        }
        if cluster_config is not None:
            input_["cluster_config"] = cluster_config
        if ebs_options is not None:
            input_["ebs_options"] = ebs_options
        if snapshot_options is not None:
            input_["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if cognito_options is not None:
            input_["cognito_options"] = cognito_options
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options
        if access_policies is not None:
            input_["access_policies"] = access_policies
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if domain_endpoint_options is not None:
            input_["domain_endpoint_options"] = domain_endpoint_options
        if node_to_node_encryption_options is not None:
            input_["node_to_node_encryption_options"] = node_to_node_encryption_options
        if advanced_security_options is not None:
            input_["advanced_security_options"] = advanced_security_options
        if identity_center_options is not None:
            input_["identity_center_options"] = identity_center_options
        if auto_tune_options is not None:
            input_["auto_tune_options"] = auto_tune_options
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if dry_run_mode is not None:
            input_["dry_run_mode"] = dry_run_mode
        if off_peak_window_options is not None:
            input_["off_peak_window_options"] = off_peak_window_options
        if software_update_options is not None:
            input_["software_update_options"] = software_update_options
        if aiml_options is not None:
            input_["aiml_options"] = aiml_options
        if deployment_strategy_options is not None:
            input_["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input_["automated_snapshot_pause_options"] = (
                automated_snapshot_pause_options
            )
        if use_case is not None:
            input_["use_case"] = use_case
        if engine_mode is not None:
            input_["engine_mode"] = engine_mode
        if accepted_warnings is not None:
            input_["accepted_warnings"] = accepted_warnings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_index(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        index_name: "capo_opensearch.types.index_name.IndexName",
        index_schema: "capo_opensearch.types.index_schema.IndexSchema",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.update_index_response.UpdateIndexResponse":
        """<p>Updates an existing OpenSearch index schema and semantic enrichment configuration. This operation allows modification of field mappings and semantic search settings for text fields. Changes to semantic enrichment configuration will apply to newly ingested documents.</p>

        Args:
            index_name: <p>The name of the index to update.</p>
            index_schema: <p>The updated JSON schema for the index including any changes to mappings, settings, and semantic enrichment configuration.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.dependency_failure_exception.DependencyFailureException: <p>An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Reduce the frequency of your requests and try again.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_index_request.UpdateIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_index_response.UpdateIndexResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_index

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_index.async_update_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_index_request.UpdateIndexRequest = {
            "domain_name": domain_name,
            "index_name": index_name,
            "index_schema": index_schema,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_package(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        package_source: "capo_opensearch.types.package_source.PackageSource",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        package_description: Optional[
            "capo_opensearch.types.package_description.PackageDescription"
        ] = None,
        commit_message: Optional[
            "capo_opensearch.types.commit_message.CommitMessage"
        ] = None,
        package_configuration: Optional[
            "capo_opensearch.types.package_configuration.PackageConfiguration"
        ] = None,
        package_encryption_options: Optional[
            "capo_opensearch.types.package_encryption_options.PackageEncryptionOptions"
        ] = None,
    ) -> "capo_opensearch.types.update_package_response.UpdatePackageResponse":
        """<p>Updates a package for use with Amazon OpenSearch Service domains. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The unique identifier for the package.</p>
            package_source: <p>Amazon S3 bucket and key for the package.</p>
            package_description: <p>A new description of the package.</p>
            commit_message: <p>Commit message for the updated file, which is shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>
            package_configuration: <p>The updated configuration details for a package.</p>
            package_encryption_options: <p>Encryption options for a package.</p>

        Raises:
            capo_opensearch.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because you don't have permissions to access the resource.</p>
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_package_request.UpdatePackageRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_package_response.UpdatePackageResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_package

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_package.async_update_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_package_request.UpdatePackageRequest = {
            "package_id": package_id,
            "package_source": package_source,
        }
        if package_description is not None:
            input_["package_description"] = package_description
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if package_configuration is not None:
            input_["package_configuration"] = package_configuration
        if package_encryption_options is not None:
            input_["package_encryption_options"] = package_encryption_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_package_scope(
        self,
        package_id: "capo_opensearch.types.package_id.PackageID",
        operation: "capo_opensearch.types.package_scope_operation_enum.PackageScopeOperationEnum",
        package_user_list: "capo_opensearch.types.package_user_list.PackageUserList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "capo_opensearch.types.update_package_scope_response.UpdatePackageScopeResponse"
    ):
        """<p>Updates the scope of a package. Scope of the package defines users who can view and associate a package.</p>

        Args:
            package_id: <p>ID of the package whose scope is being updated.</p>
            operation: <p> The operation to perform on the package scope (e.g., add/remove/override users).</p>
            package_user_list: <p> List of users to be added or removed from the package scope.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_package_scope_request.UpdatePackageScopeRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_package_scope_response.UpdatePackageScopeResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_package_scope

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_package_scope.async_update_package_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_package_scope_request.UpdatePackageScopeRequest = {
            "package_id": package_id,
            "operation": operation,
            "package_user_list": package_user_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_scheduled_action(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        action_id: "capo_opensearch.types.string.String",
        action_type: "capo_opensearch.types.action_type.ActionType",
        schedule_at: "capo_opensearch.types.schedule_at.ScheduleAt",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        desired_start_time: Optional["capo_opensearch.types.long.Long"] = None,
    ) -> "capo_opensearch.types.update_scheduled_action_response.UpdateScheduledActionResponse":
        """<p>Reschedules a planned domain configuration change for a later time. This change can be a scheduled <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html">service software update</a> or a <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types">blue/green Auto-Tune enhancement</a>.</p>

        Args:
            domain_name: <p>The name of the domain to reschedule an action for.</p>
            action_id: <p>The unique identifier of the action to reschedule. To retrieve this ID, send a <a href="https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html">ListScheduledActions</a> request.</p>
            action_type: <p>The type of action to reschedule. Can be one of <code>SERVICE_SOFTWARE_UPDATE</code>, <code>JVM_HEAP_SIZE_TUNING</code>, or <code>JVM_YOUNG_GEN_TUNING</code>. To retrieve this value, send a <a href="https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html">ListScheduledActions</a> request.</p>
            schedule_at: <p>When to schedule the action.</p> <ul> <li> <p> <code>NOW</code> - Immediately schedules the update to happen in the current hour if there's capacity available.</p> </li> <li> <p> <code>TIMESTAMP</code> - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for <code>DesiredStartTime</code>.</p> </li> <li> <p> <code>OFF_PEAK_WINDOW</code> - Marks the action to be picked up during an upcoming off-peak window. There's no guarantee that the change will be implemented during the next immediate window. Depending on capacity, it might happen in subsequent days.</p> </li> </ul>
            desired_start_time: <p>The time to implement the change, in Coordinated Universal Time (UTC). Only specify this parameter if you set <code>ScheduleAt</code> to <code>TIMESTAMP</code>.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than the allowed number of resources or sub-resources.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.slot_not_available_exception.SlotNotAvailableException: <p>An exception for attempting to schedule a domain action during an unavailable time slot.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_scheduled_action_request.UpdateScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_scheduled_action_response.UpdateScheduledActionResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_scheduled_action

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_scheduled_action.async_update_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_scheduled_action_request.UpdateScheduledActionRequest = {
            "domain_name": domain_name,
            "action_id": action_id,
            "action_type": action_type,
            "schedule_at": schedule_at,
        }
        if desired_start_time is not None:
            input_["desired_start_time"] = desired_start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_vpc_endpoint(
        self,
        vpc_endpoint_id: "capo_opensearch.types.vpc_endpoint_id.VpcEndpointId",
        vpc_options: "capo_opensearch.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "capo_opensearch.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse":
        """<p>Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>The unique identifier of the endpoint.</p>
            vpc_options: <p>The security groups and/or subnets to add, remove, or modify.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.update_vpc_endpoint

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.update_vpc_endpoint.async_update_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest = {
            "vpc_endpoint_id": vpc_endpoint_id,
            "vpc_options": vpc_options,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def upgrade_domain(
        self,
        domain_name: "capo_opensearch.types.domain_name.DomainName",
        target_version: "capo_opensearch.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        perform_check_only: Optional["capo_opensearch.types.boolean.Boolean"] = None,
        advanced_options: Optional[
            "capo_opensearch.types.advanced_options.AdvancedOptions"
        ] = None,
    ) -> "capo_opensearch.types.upgrade_domain_response.UpgradeDomainResponse":
        """<p>Allows you to either upgrade your Amazon OpenSearch Service domain or perform an upgrade eligibility check to a compatible version of OpenSearch or Elasticsearch.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain that you want to upgrade.</p>
            target_version: <p>OpenSearch or Elasticsearch version to which you want to upgrade, in the format Opensearch_X.Y or Elasticsearch_X.Y.</p>
            perform_check_only: <p>When true, indicates that an upgrade eligibility check needs to be performed. Does not actually perform the upgrade.</p>
            advanced_options: <p>Only supports the <code>override_main_response_version</code> parameter and not other advanced options. You can only include this option when upgrading to an OpenSearch version. Specifies whether the domain reports its version as 7.10 so that it continues to work with Elasticsearch OSS clients and plugins.</p>

        Raises:
            capo_opensearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_opensearch.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access an unsupported operation.</p>
            capo_opensearch.errors.internal_exception.InternalException: <p>Request processing failed because of an unknown error, exception, or internal failure.</p>
            capo_opensearch.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists.</p>
            capo_opensearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.validation_exception.ValidationException: <p>An exception for accessing or deleting a resource that doesn't exist.</p>
            capo_opensearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearch.types.upgrade_domain_request.UpgradeDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearch.types.upgrade_domain_response.UpgradeDomainResponse"
        ]:
            import capo_opensearch._operations.amazon_open_search_service.upgrade_domain

            (
                output,
                http_response,
            ) = await capo_opensearch._operations.amazon_open_search_service.upgrade_domain.async_upgrade_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearch.types.upgrade_domain_request.UpgradeDomainRequest = {
            "domain_name": domain_name,
            "target_version": target_version,
        }
        if perform_check_only is not None:
            input_["perform_check_only"] = perform_check_only
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

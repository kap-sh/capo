"""Generated from Smithy shape ``com.amazonaws.lambda#AWSGirApiService``."""

import time
import uuid
import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._auth._identity import Credentials
from capo_lambda._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lambda._auth._zapros_handler import AuthMiddleware
from capo_lambda._body import Body, closing_bodies
from capo_lambda._iter import ensure_sync_iterator
from capo_lambda._pagination import resolve_path as _resolve_path
from capo_lambda._resources.aws_gir_api_service.capacity_provider_resource import (
    CapacityProviderResource,
)
from capo_lambda._resources.aws_gir_api_service.code_signing_config_resource import (
    CodeSigningConfigResource,
)
from capo_lambda._resources.aws_gir_api_service.durable_execution import (
    DurableExecution,
)
from capo_lambda._resources.aws_gir_api_service.event_source_mapping import (
    EventSourceMapping,
)
from capo_lambda._resources.aws_gir_api_service.function import Function
from capo_lambda._resources.aws_gir_api_service.function_alias import FunctionAlias
from capo_lambda._resources.aws_gir_api_service.function_version_resource import (
    FunctionVersionResource,
)
from capo_lambda._resources.aws_gir_api_service.layer_resource import LayerResource
from capo_lambda._resources.aws_gir_api_service.layer_version import LayerVersion
from capo_lambda._resources.aws_gir_api_service.permission import Permission
from capo_lambda._resources.aws_gir_api_service.provisioned_concurrency_config import (
    ProvisionedConcurrencyConfig,
)
from capo_lambda._services._aws_config import aws_config
from capo_lambda._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)
from capo_lambda.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_lambda.types.action
    import capo_lambda.types.add_layer_version_permission_request
    import capo_lambda.types.add_layer_version_permission_response
    import capo_lambda.types.add_permission_request
    import capo_lambda.types.add_permission_response
    import capo_lambda.types.alias
    import capo_lambda.types.alias_configuration
    import capo_lambda.types.alias_routing_configuration
    import capo_lambda.types.allowed_publishers
    import capo_lambda.types.amazon_managed_kafka_event_source_config
    import capo_lambda.types.architecture
    import capo_lambda.types.architectures_list
    import capo_lambda.types.arn
    import capo_lambda.types.batch_size
    import capo_lambda.types.binary_operation_payload
    import capo_lambda.types.bisect_batch_on_function_error
    import capo_lambda.types.blob
    import capo_lambda.types.blob_stream
    import capo_lambda.types.boolean
    import capo_lambda.types.callback_id
    import capo_lambda.types.capacity_provider
    import capo_lambda.types.capacity_provider_config
    import capo_lambda.types.capacity_provider_name
    import capo_lambda.types.capacity_provider_permissions_config
    import capo_lambda.types.capacity_provider_scaling_config
    import capo_lambda.types.capacity_provider_state
    import capo_lambda.types.capacity_provider_telemetry_config
    import capo_lambda.types.capacity_provider_vpc_config
    import capo_lambda.types.checkpoint_durable_execution_request
    import capo_lambda.types.checkpoint_durable_execution_response
    import capo_lambda.types.checkpoint_token
    import capo_lambda.types.client_token
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.code_signing_policies
    import capo_lambda.types.compatible_architectures
    import capo_lambda.types.compatible_runtimes
    import capo_lambda.types.concurrency
    import capo_lambda.types.cors
    import capo_lambda.types.create_alias_request
    import capo_lambda.types.create_capacity_provider_request
    import capo_lambda.types.create_capacity_provider_response
    import capo_lambda.types.create_code_signing_config_request
    import capo_lambda.types.create_code_signing_config_response
    import capo_lambda.types.create_event_source_mapping_request
    import capo_lambda.types.create_function_request
    import capo_lambda.types.create_function_url_config_request
    import capo_lambda.types.create_function_url_config_response
    import capo_lambda.types.date
    import capo_lambda.types.dead_letter_config
    import capo_lambda.types.delete_alias_request
    import capo_lambda.types.delete_capacity_provider_request
    import capo_lambda.types.delete_capacity_provider_response
    import capo_lambda.types.delete_code_signing_config_request
    import capo_lambda.types.delete_code_signing_config_response
    import capo_lambda.types.delete_event_source_mapping_request
    import capo_lambda.types.delete_function_code_signing_config_request
    import capo_lambda.types.delete_function_concurrency_request
    import capo_lambda.types.delete_function_event_invoke_config_request
    import capo_lambda.types.delete_function_request
    import capo_lambda.types.delete_function_response
    import capo_lambda.types.delete_function_url_config_request
    import capo_lambda.types.delete_layer_version_request
    import capo_lambda.types.delete_provisioned_concurrency_config_request
    import capo_lambda.types.description
    import capo_lambda.types.destination_config
    import capo_lambda.types.document_db_event_source_config
    import capo_lambda.types.durable_config
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.durable_execution_name
    import capo_lambda.types.enabled
    import capo_lambda.types.environment
    import capo_lambda.types.ephemeral_storage
    import capo_lambda.types.error_object
    import capo_lambda.types.event
    import capo_lambda.types.event_source_mapping_configuration
    import capo_lambda.types.event_source_mapping_logging_config
    import capo_lambda.types.event_source_mapping_metrics_config
    import capo_lambda.types.event_source_position
    import capo_lambda.types.event_source_token
    import capo_lambda.types.execution
    import capo_lambda.types.execution_status_list
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.file_system_config_list
    import capo_lambda.types.filter_criteria
    import capo_lambda.types.function_code
    import capo_lambda.types.function_configuration
    import capo_lambda.types.function_event_invoke_config
    import capo_lambda.types.function_name
    import capo_lambda.types.function_response_type_list
    import capo_lambda.types.function_scaling_config
    import capo_lambda.types.function_url_auth_type
    import capo_lambda.types.function_url_function_name
    import capo_lambda.types.function_url_qualifier
    import capo_lambda.types.function_version
    import capo_lambda.types.function_version_latest_published
    import capo_lambda.types.function_versions_by_capacity_provider_list_item
    import capo_lambda.types.get_account_settings_request
    import capo_lambda.types.get_account_settings_response
    import capo_lambda.types.get_alias_request
    import capo_lambda.types.get_capacity_provider_request
    import capo_lambda.types.get_capacity_provider_response
    import capo_lambda.types.get_code_signing_config_request
    import capo_lambda.types.get_code_signing_config_response
    import capo_lambda.types.get_durable_execution_history_request
    import capo_lambda.types.get_durable_execution_history_response
    import capo_lambda.types.get_durable_execution_request
    import capo_lambda.types.get_durable_execution_response
    import capo_lambda.types.get_durable_execution_state_request
    import capo_lambda.types.get_durable_execution_state_response
    import capo_lambda.types.get_event_source_mapping_request
    import capo_lambda.types.get_function_code_signing_config_request
    import capo_lambda.types.get_function_code_signing_config_response
    import capo_lambda.types.get_function_concurrency_request
    import capo_lambda.types.get_function_concurrency_response
    import capo_lambda.types.get_function_configuration_request
    import capo_lambda.types.get_function_event_invoke_config_request
    import capo_lambda.types.get_function_recursion_config_request
    import capo_lambda.types.get_function_recursion_config_response
    import capo_lambda.types.get_function_request
    import capo_lambda.types.get_function_response
    import capo_lambda.types.get_function_scaling_config_request
    import capo_lambda.types.get_function_scaling_config_response
    import capo_lambda.types.get_function_url_config_request
    import capo_lambda.types.get_function_url_config_response
    import capo_lambda.types.get_layer_version_by_arn_request
    import capo_lambda.types.get_layer_version_policy_request
    import capo_lambda.types.get_layer_version_policy_response
    import capo_lambda.types.get_layer_version_request
    import capo_lambda.types.get_layer_version_response
    import capo_lambda.types.get_policy_request
    import capo_lambda.types.get_policy_response
    import capo_lambda.types.get_provisioned_concurrency_config_request
    import capo_lambda.types.get_provisioned_concurrency_config_response
    import capo_lambda.types.get_runtime_management_config_request
    import capo_lambda.types.get_runtime_management_config_response
    import capo_lambda.types.handler
    import capo_lambda.types.image_config
    import capo_lambda.types.include_execution_data
    import capo_lambda.types.instance_requirements
    import capo_lambda.types.invocation_request
    import capo_lambda.types.invocation_response
    import capo_lambda.types.invocation_type
    import capo_lambda.types.invoke_async_request
    import capo_lambda.types.invoke_async_response
    import capo_lambda.types.invoke_mode
    import capo_lambda.types.invoke_with_response_stream_request
    import capo_lambda.types.invoke_with_response_stream_response
    import capo_lambda.types.invoked_via_function_url
    import capo_lambda.types.item_count
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.kms_key_arn_non_empty
    import capo_lambda.types.layer_list
    import capo_lambda.types.layer_name
    import capo_lambda.types.layer_permission_allowed_action
    import capo_lambda.types.layer_permission_allowed_principal
    import capo_lambda.types.layer_version_arn
    import capo_lambda.types.layer_version_content_input
    import capo_lambda.types.layer_version_number
    import capo_lambda.types.license_info
    import capo_lambda.types.list_aliases_request
    import capo_lambda.types.list_aliases_response
    import capo_lambda.types.list_capacity_providers_request
    import capo_lambda.types.list_capacity_providers_response
    import capo_lambda.types.list_code_signing_configs_request
    import capo_lambda.types.list_code_signing_configs_response
    import capo_lambda.types.list_durable_executions_by_function_request
    import capo_lambda.types.list_durable_executions_by_function_response
    import capo_lambda.types.list_event_source_mappings_request
    import capo_lambda.types.list_event_source_mappings_response
    import capo_lambda.types.list_function_event_invoke_configs_request
    import capo_lambda.types.list_function_event_invoke_configs_response
    import capo_lambda.types.list_function_url_configs_request
    import capo_lambda.types.list_function_url_configs_response
    import capo_lambda.types.list_function_versions_by_capacity_provider_request
    import capo_lambda.types.list_function_versions_by_capacity_provider_response
    import capo_lambda.types.list_functions_by_code_signing_config_request
    import capo_lambda.types.list_functions_by_code_signing_config_response
    import capo_lambda.types.list_functions_request
    import capo_lambda.types.list_functions_response
    import capo_lambda.types.list_layer_versions_request
    import capo_lambda.types.list_layer_versions_response
    import capo_lambda.types.list_layers_request
    import capo_lambda.types.list_layers_response
    import capo_lambda.types.list_provisioned_concurrency_configs_request
    import capo_lambda.types.list_provisioned_concurrency_configs_response
    import capo_lambda.types.list_tags_request
    import capo_lambda.types.list_tags_response
    import capo_lambda.types.list_versions_by_function_request
    import capo_lambda.types.list_versions_by_function_response
    import capo_lambda.types.log_type
    import capo_lambda.types.logging_config
    import capo_lambda.types.master_region
    import capo_lambda.types.max_fifty_list_items
    import capo_lambda.types.max_function_event_invoke_config_list_items
    import capo_lambda.types.max_items
    import capo_lambda.types.max_layer_list_items
    import capo_lambda.types.max_list_items
    import capo_lambda.types.max_provisioned_concurrency_config_list_items
    import capo_lambda.types.maximum_batching_window_in_seconds
    import capo_lambda.types.maximum_event_age_in_seconds
    import capo_lambda.types.maximum_record_age_in_seconds
    import capo_lambda.types.maximum_retry_attempts
    import capo_lambda.types.maximum_retry_attempts_event_source_mapping
    import capo_lambda.types.memory_size
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.namespaced_statement_id
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.operation
    import capo_lambda.types.operation_updates
    import capo_lambda.types.organization_id
    import capo_lambda.types.package_type
    import capo_lambda.types.parallelization_factor
    import capo_lambda.types.positive_integer
    import capo_lambda.types.principal
    import capo_lambda.types.principal_org_id
    import capo_lambda.types.propagate_tags
    import capo_lambda.types.provisioned_poller_config
    import capo_lambda.types.publish_layer_version_request
    import capo_lambda.types.publish_layer_version_response
    import capo_lambda.types.publish_version_request
    import capo_lambda.types.published_function_qualifier
    import capo_lambda.types.put_function_code_signing_config_request
    import capo_lambda.types.put_function_code_signing_config_response
    import capo_lambda.types.put_function_concurrency_request
    import capo_lambda.types.put_function_event_invoke_config_request
    import capo_lambda.types.put_function_recursion_config_request
    import capo_lambda.types.put_function_recursion_config_response
    import capo_lambda.types.put_function_scaling_config_request
    import capo_lambda.types.put_function_scaling_config_response
    import capo_lambda.types.put_provisioned_concurrency_config_request
    import capo_lambda.types.put_provisioned_concurrency_config_response
    import capo_lambda.types.put_runtime_management_config_request
    import capo_lambda.types.put_runtime_management_config_response
    import capo_lambda.types.qualifier
    import capo_lambda.types.queues
    import capo_lambda.types.recursive_loop
    import capo_lambda.types.remove_layer_version_permission_request
    import capo_lambda.types.remove_permission_request
    import capo_lambda.types.reserved_concurrent_executions
    import capo_lambda.types.response_streaming_invocation_type
    import capo_lambda.types.reverse_order
    import capo_lambda.types.role_arn
    import capo_lambda.types.runtime
    import capo_lambda.types.runtime_version_arn
    import capo_lambda.types.s3_bucket
    import capo_lambda.types.s3_key
    import capo_lambda.types.s3_object_storage_mode
    import capo_lambda.types.s3_object_version
    import capo_lambda.types.scaling_config
    import capo_lambda.types.self_managed_event_source
    import capo_lambda.types.self_managed_kafka_event_source_config
    import capo_lambda.types.send_durable_execution_callback_failure_request
    import capo_lambda.types.send_durable_execution_callback_failure_response
    import capo_lambda.types.send_durable_execution_callback_heartbeat_request
    import capo_lambda.types.send_durable_execution_callback_heartbeat_response
    import capo_lambda.types.send_durable_execution_callback_success_request
    import capo_lambda.types.send_durable_execution_callback_success_response
    import capo_lambda.types.snap_start
    import capo_lambda.types.source_access_configurations
    import capo_lambda.types.source_owner
    import capo_lambda.types.statement_id
    import capo_lambda.types.stop_durable_execution_request
    import capo_lambda.types.stop_durable_execution_response
    import capo_lambda.types.string
    import capo_lambda.types.tag_key_list
    import capo_lambda.types.tag_resource_request
    import capo_lambda.types.taggable_resource
    import capo_lambda.types.tags
    import capo_lambda.types.tenancy_config
    import capo_lambda.types.tenant_id
    import capo_lambda.types.timeout
    import capo_lambda.types.topics
    import capo_lambda.types.tracing_config
    import capo_lambda.types.tumbling_window_in_seconds
    import capo_lambda.types.unqualified_function_name
    import capo_lambda.types.untag_resource_request
    import capo_lambda.types.update_alias_request
    import capo_lambda.types.update_capacity_provider_request
    import capo_lambda.types.update_capacity_provider_response
    import capo_lambda.types.update_code_signing_config_request
    import capo_lambda.types.update_code_signing_config_response
    import capo_lambda.types.update_event_source_mapping_request
    import capo_lambda.types.update_function_code_request
    import capo_lambda.types.update_function_configuration_request
    import capo_lambda.types.update_function_event_invoke_config_request
    import capo_lambda.types.update_function_url_config_request
    import capo_lambda.types.update_function_url_config_response
    import capo_lambda.types.update_runtime_on
    import capo_lambda.types.uuid_string
    import capo_lambda.types.version_with_latest_published
    import capo_lambda.types.vpc_config


class LambdaClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class LambdaClient:
    """A client for the ``Lambda`` service.

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
        self._config = LambdaClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.capacity_provider_resource = CapacityProviderResource(self)
        self.code_signing_config_resource = CodeSigningConfigResource(self)
        self.durable_execution = DurableExecution(self)
        self.event_source_mapping = EventSourceMapping(self)
        self.function = Function(self)
        self.function_alias = FunctionAlias(self)
        self.function_version_resource = FunctionVersionResource(self)
        self.layer_resource = LayerResource(self)
        self.layer_version = LayerVersion(self)
        self.permission = Permission(self)
        self.provisioned_concurrency_config = ProvisionedConcurrencyConfig(self)

    def operation_options(
        self, config_overrides: Optional[LambdaClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LambdaClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def delete_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.delete_function_response.DeleteFunctionResponse":
        r"""<p>Deletes a Lambda function. To delete a specific function version, use the <code>Qualifier</code> parameter. Otherwise, all versions and aliases are deleted. This doesn't require the user to have explicit permissions for <a>DeleteAlias</a>.</p> <note> <p>A deleted Lambda function cannot be recovered. Ensure that you specify the correct function name and version before deleting.</p> </note> <p>To delete Lambda event source mappings that invoke a function, use <a>DeleteEventSourceMapping</a>. For Amazon Web Services services and resources that invoke your function directly, delete the trigger in the service where you originally configured it.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function or version.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:1</code> (with version).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version to delete. You can't delete a version that an alias references.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a version of a Lambda function
            The following example deletes version 1 of a Lambda function named my-function.

            >>> client.delete_function(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_request.DeleteFunctionRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> None:
        r"""<p>Deletes the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an asynchronous invocation configuration
            The following example deletes the asynchronous invocation configuration for the GREEN alias of a function named my-function.

            >>> client.delete_function_event_invoke_config(function_name='my-function', qualifier='GREEN')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_event_invoke_config_request.DeleteFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_event_invoke_config.delete_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_event_invoke_config_request.DeleteFunctionEventInvokeConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_settings(
        self, *, config_overrides: Optional[LambdaClientConfig] = None
    ) -> "capo_lambda.types.get_account_settings_response.GetAccountSettingsResponse":
        r"""<p>Retrieves details about your account's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/limits.html\">limits</a> and usage in an Amazon Web Services Region.</p>

        Raises:
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get account settings
            This operation takes no parameters and returns details about storage and concurrency quotas in the current Region.

            >>> client.get_account_settings()
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_account_settings

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_account_settings_request.GetAccountSettingsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Retrieves the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get an asynchronous invocation configuration
            The following example returns the asynchronous invocation configuration for the BLUE alias of a function named my-function.

            >>> client.get_function_event_invoke_config(function_name='my-function', qualifier='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_event_invoke_config_request.GetFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_event_invoke_config.get_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_event_invoke_config_request.GetFunctionEventInvokeConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_function_event_invoke_configs(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_function_event_invoke_config_list_items.MaxFunctionEventInvokeConfigListItems"
        ] = None,
    ) -> "capo_lambda.types.list_function_event_invoke_configs_response.ListFunctionEventInvokeConfigsResponse":
        r"""<p>Retrieves a list of configurations for asynchronous invocation for a function.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of configurations to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view a list of asynchronous invocation configurations
            The following example returns a list of asynchronous invocation configurations for a function named my-function.

            >>> client.list_function_event_invoke_configs(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_function_event_invoke_configs_request.ListFunctionEventInvokeConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_function_event_invoke_configs_response.ListFunctionEventInvokeConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_event_invoke_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_function_event_invoke_configs.list_function_event_invoke_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_event_invoke_configs_request.ListFunctionEventInvokeConfigsRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags(
        self,
        resource: "capo_lambda.types.taggable_resource.TaggableResource",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.list_tags_response.ListTagsResponse":
        r"""<p>Returns a function, event source mapping, or code signing configuration's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a>. You can also view function tags with <a>GetFunction</a>.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN). Note: Lambda does not support adding tags to function aliases or versions.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve the list of tags for a Lambda function
            The following example displays the tags attached to the my-function Lambda function.

            >>> client.list_tags(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_tags_request.ListTagsRequest]",
        ) -> OperationResponse["capo_lambda.types.list_tags_response.ListTagsResponse"]:
            import capo_lambda._operations.aws_gir_api_service.list_tags

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_tags.list_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_tags_request.ListTagsRequest = {
            "resource": resource
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
        ] = None,
        maximum_event_age_in_seconds: Optional[
            "capo_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
        ] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Configures options for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html\">asynchronous invocation</a> on a function, version, or alias. If a configuration already exists for a function, version, or alias, this operation overwrites it. If you exclude any settings, they are removed. To set one option without affecting existing settings for other options, use <a>UpdateFunctionEventInvokeConfig</a>.</p> <p>By default, Lambda retries an asynchronous invocation twice if the function returns an error. It retains events in a queue for up to six hours. When an event fails all processing attempts or stays in the asynchronous invocation queue for too long, Lambda discards it. To retain discarded events, configure a dead-letter queue with <a>UpdateFunctionConfiguration</a>.</p> <p>To send an invocation record to a queue, topic, S3 bucket, function, or event bus, specify a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations\">destination</a>. You can configure separate destinations for successful invocations (on-success) and events that fail all processing attempts (on-failure). You can configure destinations in addition to or instead of a dead-letter queue.</p> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>
            maximum_retry_attempts: <p>The maximum number of times to retry when the function returns an error.</p>
            maximum_event_age_in_seconds: <p>The maximum age of a request that Lambda sends to a function for processing.</p>
            destination_config: <p>A destination for events after they have been sent to a function for processing.</p> <p class=\"title\"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure error handling for asynchronous invocation
            The following example sets a maximum event age of one hour and disables retries for the specified function.

            >>> client.put_function_event_invoke_config(function_name='my-function', maximum_event_age_in_seconds=3600, maximum_retry_attempts=0)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_event_invoke_config_request.PutFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_event_invoke_config.put_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_event_invoke_config_request.PutFunctionEventInvokeConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if maximum_event_age_in_seconds is not None:
            input_["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if destination_config is not None:
            input_["destination_config"] = destination_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_durable_execution_callback_failure(
        self,
        callback_id: "capo_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        error: Optional["capo_lambda.types.error_object.ErrorObject"] = None,
    ) -> "capo_lambda.types.send_durable_execution_callback_failure_response.SendDurableExecutionCallbackFailureResponse":
        """<p>Sends a failure response for a callback operation in a durable execution. Use this API when an external system cannot complete a callback operation successfully.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>
            error: <p>Error details describing why the callback operation failed.</p>

        Raises:
            capo_lambda.errors.callback_timeout_exception.CallbackTimeoutException: <p>The callback ID token has either expired or the callback associated with the token has already been closed.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.send_durable_execution_callback_failure_request.SendDurableExecutionCallbackFailureRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.send_durable_execution_callback_failure_response.SendDurableExecutionCallbackFailureResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_failure

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_failure.send_durable_execution_callback_failure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.send_durable_execution_callback_failure_request.SendDurableExecutionCallbackFailureRequest = {
            "callback_id": callback_id
        }
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_durable_execution_callback_heartbeat(
        self,
        callback_id: "capo_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse":
        """<p>Sends a heartbeat signal for a long-running callback operation to prevent timeout. Use this API to extend the callback timeout period while the external operation is still in progress.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>

        Raises:
            capo_lambda.errors.callback_timeout_exception.CallbackTimeoutException: <p>The callback ID token has either expired or the callback associated with the token has already been closed.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.send_durable_execution_callback_heartbeat_response.SendDurableExecutionCallbackHeartbeatResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_heartbeat

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_heartbeat.send_durable_execution_callback_heartbeat(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.send_durable_execution_callback_heartbeat_request.SendDurableExecutionCallbackHeartbeatRequest = {
            "callback_id": callback_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_durable_execution_callback_success(
        self,
        callback_id: "capo_lambda.types.callback_id.CallbackId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        result: Optional[
            "capo_lambda.types.binary_operation_payload.BinaryOperationPayload"
        ] = None,
    ) -> "capo_lambda.types.send_durable_execution_callback_success_response.SendDurableExecutionCallbackSuccessResponse":
        """<p>Sends a successful completion response for a callback operation in a durable execution. Use this API when an external system has successfully completed a callback operation.</p>

        Args:
            callback_id: <p>The unique identifier for the callback operation.</p>
            result: <p>The result data from the successful callback operation. Maximum size is 256 KB.</p>

        Raises:
            capo_lambda.errors.callback_timeout_exception.CallbackTimeoutException: <p>The callback ID token has either expired or the callback associated with the token has already been closed.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.send_durable_execution_callback_success_request.SendDurableExecutionCallbackSuccessRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.send_durable_execution_callback_success_response.SendDurableExecutionCallbackSuccessResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_success

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.send_durable_execution_callback_success.send_durable_execution_callback_success(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.send_durable_execution_callback_success_request.SendDurableExecutionCallbackSuccessRequest = {
            "callback_id": callback_id
        }
        if result is not None:
            input_["result"] = result

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource: "capo_lambda.types.taggable_resource.TaggableResource",
        tags: "capo_lambda.types.tags.Tags",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Adds <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> to a function, event source mapping, or code signing configuration.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN).</p>
            tags: <p>A list of tags to apply to the resource.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to an existing Lambda function
            The following example adds a tag with the key name DEPARTMENT and a value of 'Department A' to the specified Lambda function.

            >>> client.tag_resource(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function', tags={'DEPARTMENT': 'Department A'})
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.tag_resource

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.tag_resource_request.TagResourceRequest = {
            "resource": resource,
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
        resource: "capo_lambda.types.taggable_resource.TaggableResource",
        tag_keys: "capo_lambda.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> from a function, event source mapping, or code signing configuration.</p>

        Args:
            resource: <p>The resource's Amazon Resource Name (ARN).</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from an existing Lambda function
            The following example removes the tag with the key name DEPARTMENT tag from the my-function Lambda function.

            >>> client.untag_resource(resource='arn:aws:lambda:us-west-2:123456789012:function:my-function', tag_keys=['DEPARTMENT'])
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.untag_resource

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.untag_resource_request.UntagResourceRequest = {
            "resource": resource,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_event_invoke_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
        ] = None,
        maximum_event_age_in_seconds: Optional[
            "capo_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
        ] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig":
        r"""<p>Updates the configuration for asynchronous invocation for a function, version, or alias.</p> <p>To configure options for asynchronous invocation, use <a>PutFunctionEventInvokeConfig</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>A version number or alias name.</p>
            maximum_retry_attempts: <p>The maximum number of times to retry when the function returns an error.</p>
            maximum_event_age_in_seconds: <p>The maximum age of a request that Lambda sends to a function for processing.</p>
            destination_config: <p>A destination for events after they have been sent to a function for processing.</p> <p class=\"title\"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an asynchronous invocation configuration
            The following example adds an on-failure destination to the existing asynchronous invocation configuration for a function named my-function.

            >>> client.update_function_event_invoke_config(destination_config={'OnFailure': {'Destination': 'arn:aws:sqs:us-east-2:123456789012:destination'}}, function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_event_invoke_config_request.UpdateFunctionEventInvokeConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_event_invoke_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_event_invoke_config.update_function_event_invoke_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_event_invoke_config_request.UpdateFunctionEventInvokeConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if maximum_event_age_in_seconds is not None:
            input_["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if destination_config is not None:
            input_["destination_config"] = destination_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        vpc_config: "capo_lambda.types.capacity_provider_vpc_config.CapacityProviderVpcConfig",
        permissions_config: "capo_lambda.types.capacity_provider_permissions_config.CapacityProviderPermissionsConfig",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        instance_requirements: Optional[
            "capo_lambda.types.instance_requirements.InstanceRequirements"
        ] = None,
        capacity_provider_scaling_config: Optional[
            "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
        ] = None,
        kms_key_arn: Optional[
            "capo_lambda.types.kms_key_arn_non_empty.KMSKeyArnNonEmpty"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_lambda.types.propagate_tags.PropagateTags"
        ] = None,
        telemetry_config: Optional[
            "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
        ] = None,
    ) -> "capo_lambda.types.create_capacity_provider_response.CreateCapacityProviderResponse":
        """<p>Creates a capacity provider that manages compute resources for Lambda functions</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider. </p>
            vpc_config: <p>The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances will be launched.</p>
            permissions_config: <p>The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources.</p>
            instance_requirements: <p>The instance requirements that specify the compute instance characteristics, including architectures and allowed or excluded instance types.</p>
            capacity_provider_scaling_config: <p>The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count and scaling policies.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt data associated with the capacity provider.</p>
            tags: <p>A list of tags to associate with the capacity provider.</p>
            propagate_tags: <p>The tag propagation configuration for the capacity provider. Specifies tags to apply to managed resources at launch.</p>
            telemetry_config: <p>The telemetry configuration for the capacity provider. Specifies logging settings for managed resources.</p>

        Raises:
            capo_lambda.errors.capacity_provider_limit_exceeded_exception.CapacityProviderLimitExceededException: <p>The maximum number of capacity providers for your account has been exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a> </p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_capacity_provider_request.CreateCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.create_capacity_provider_response.CreateCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_capacity_provider.create_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.create_capacity_provider_request.CreateCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name,
            "vpc_config": vpc_config,
            "permissions_config": permissions_config,
        }
        if instance_requirements is not None:
            input_["instance_requirements"] = instance_requirements
        if capacity_provider_scaling_config is not None:
            input_["capacity_provider_scaling_config"] = (
                capacity_provider_scaling_config
            )
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if telemetry_config is not None:
            input_["telemetry_config"] = telemetry_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_capacity_provider_response.GetCapacityProviderResponse":
        """<p>Retrieves information about a specific capacity provider, including its configuration, state, and associated resources.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to retrieve.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_capacity_provider_request.GetCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_capacity_provider_response.GetCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_capacity_provider.get_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_capacity_provider_request.GetCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        capacity_provider_scaling_config: Optional[
            "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
        ] = None,
        propagate_tags: Optional[
            "capo_lambda.types.propagate_tags.PropagateTags"
        ] = None,
        telemetry_config: Optional[
            "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
        ] = None,
    ) -> "capo_lambda.types.update_capacity_provider_response.UpdateCapacityProviderResponse":
        """<p>Updates the configuration of an existing capacity provider.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to update.</p>
            capacity_provider_scaling_config: <p>The updated scaling configuration for the capacity provider.</p>
            telemetry_config: <p>The updated telemetry configuration for the capacity provider.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_capacity_provider_request.UpdateCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.update_capacity_provider_response.UpdateCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_capacity_provider.update_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_capacity_provider_request.UpdateCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }
        if capacity_provider_scaling_config is not None:
            input_["capacity_provider_scaling_config"] = (
                capacity_provider_scaling_config
            )
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if telemetry_config is not None:
            input_["telemetry_config"] = telemetry_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.delete_capacity_provider_response.DeleteCapacityProviderResponse":
        """<p>Deletes a capacity provider. You cannot delete a capacity provider that is currently being used by Lambda functions.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to delete.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_capacity_provider_request.DeleteCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.delete_capacity_provider_response.DeleteCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_capacity_provider.delete_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_capacity_provider_request.DeleteCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_capacity_providers(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        state: Optional[
            "capo_lambda.types.capacity_provider_state.CapacityProviderState"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "capo_lambda.types.list_capacity_providers_response.ListCapacityProvidersResponse":
        """<p>Returns a list of capacity providers in your account.</p>

        Args:
            state: <p>Filter capacity providers by their current state.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of capacity providers to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_capacity_providers_request.ListCapacityProvidersRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_capacity_providers_response.ListCapacityProvidersResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_capacity_providers

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_capacity_providers.list_capacity_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_capacity_providers_request.ListCapacityProvidersRequest = {}
        if state is not None:
            input_["state"] = state
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_capacity_providers(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        state: Optional[
            "capo_lambda.types.capacity_provider_state.CapacityProviderState"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "Iterator[capo_lambda.types.capacity_provider.CapacityProvider]":
        _token = marker
        while True:
            _response = self.list_capacity_providers(
                config_overrides=config_overrides,
                state=state,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("capacity_providers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_function_versions_by_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "capo_lambda.types.list_function_versions_by_capacity_provider_response.ListFunctionVersionsByCapacityProviderResponse":
        """<p>Returns a list of function versions that are configured to use a specific capacity provider.</p>

        Args:
            capacity_provider_name: <p>The name of the capacity provider to list function versions for.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of function versions to return in the response.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_function_versions_by_capacity_provider_request.ListFunctionVersionsByCapacityProviderRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_function_versions_by_capacity_provider_response.ListFunctionVersionsByCapacityProviderResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_versions_by_capacity_provider

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_function_versions_by_capacity_provider.list_function_versions_by_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_versions_by_capacity_provider_request.ListFunctionVersionsByCapacityProviderRequest = {
            "capacity_provider_name": capacity_provider_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_function_versions_by_capacity_provider(
        self,
        capacity_provider_name: "capo_lambda.types.capacity_provider_name.CapacityProviderName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_fifty_list_items.MaxFiftyListItems"
        ] = None,
    ) -> "Iterator[capo_lambda.types.function_versions_by_capacity_provider_list_item.FunctionVersionsByCapacityProviderListItem]":
        _token = marker
        while True:
            _response = self.list_function_versions_by_capacity_provider(
                capacity_provider_name,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("function_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def create_code_signing_config(
        self,
        allowed_publishers: "capo_lambda.types.allowed_publishers.AllowedPublishers",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        code_signing_policies: Optional[
            "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
    ) -> "capo_lambda.types.create_code_signing_config_response.CreateCodeSigningConfigResponse":
        r"""<p>Creates a code signing configuration. A <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html\">code signing configuration</a> defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail). </p>

        Args:
            description: <p>Descriptive name for this code signing configuration.</p>
            allowed_publishers: <p>Signing profiles for this code signing configuration.</p>
            code_signing_policies: <p>The code signing policies define the actions to take if the validation checks fail. </p>
            tags: <p>A list of tags to add to the code signing configuration.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_code_signing_config_request.CreateCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.create_code_signing_config_response.CreateCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_code_signing_config.create_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.create_code_signing_config_request.CreateCodeSigningConfigRequest = {
            "allowed_publishers": allowed_publishers
        }
        if description is not None:
            input_["description"] = description
        if code_signing_policies is not None:
            input_["code_signing_policies"] = code_signing_policies
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_code_signing_configs(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_code_signing_configs_response.ListCodeSigningConfigsResponse":
        r"""<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuring-codesigning.html\">code signing configurations</a>. A request returns up to 10,000 configurations per call. You can use the <code>MaxItems</code> parameter to return fewer configurations per call. </p>

        Args:
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Maximum number of items to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_code_signing_configs_request.ListCodeSigningConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_code_signing_configs_response.ListCodeSigningConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_code_signing_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_code_signing_configs.list_code_signing_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_code_signing_configs_request.ListCodeSigningConfigsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.delete_code_signing_config_response.DeleteCodeSigningConfigResponse":
        """<p>Deletes the code signing configuration. You can delete the code signing configuration only if no function is using it. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_code_signing_config_request.DeleteCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.delete_code_signing_config_response.DeleteCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_code_signing_config.delete_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_code_signing_config_request.DeleteCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_code_signing_config_response.GetCodeSigningConfigResponse":
        """<p>Returns information about the specified code signing configuration.</p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration. </p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_code_signing_config_request.GetCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_code_signing_config_response.GetCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_code_signing_config.get_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_code_signing_config_request.GetCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_functions_by_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_functions_by_code_signing_config_response.ListFunctionsByCodeSigningConfigResponse":
        """<p>List the functions that use the specified code signing configuration. You can use this method prior to deleting a code signing configuration, to verify that no functions are using it.</p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Maximum number of items to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_functions_by_code_signing_config_request.ListFunctionsByCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_functions_by_code_signing_config_response.ListFunctionsByCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_functions_by_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_functions_by_code_signing_config.list_functions_by_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_functions_by_code_signing_config_request.ListFunctionsByCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        allowed_publishers: Optional[
            "capo_lambda.types.allowed_publishers.AllowedPublishers"
        ] = None,
        code_signing_policies: Optional[
            "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
        ] = None,
    ) -> "capo_lambda.types.update_code_signing_config_response.UpdateCodeSigningConfigResponse":
        """<p>Update the code signing configuration. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            description: <p>Descriptive name for this code signing configuration.</p>
            allowed_publishers: <p>Signing profiles for this code signing configuration.</p>
            code_signing_policies: <p>The code signing policy.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_code_signing_config_request.UpdateCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.update_code_signing_config_response.UpdateCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_code_signing_config.update_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_code_signing_config_request.UpdateCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }
        if description is not None:
            input_["description"] = description
        if allowed_publishers is not None:
            input_["allowed_publishers"] = allowed_publishers
        if code_signing_policies is not None:
            input_["code_signing_policies"] = code_signing_policies

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_durable_execution(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        include_execution_data: Optional[
            "capo_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
    ) -> "capo_lambda.types.get_durable_execution_response.GetDurableExecutionResponse":
        r"""<p>Retrieves detailed information about a specific <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable execution</a>, including its current status, input payload, result or error information, and execution metadata such as start time and usage statistics.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            include_execution_data: <p>Specifies whether to include execution data such as input payload, result, and error information in the response. Set to <code>false</code> for a more compact response that includes only execution metadata. The default value is set to <code>true</code>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_durable_execution_request.GetDurableExecutionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_durable_execution_response.GetDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_durable_execution.get_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_request.GetDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def checkpoint_durable_execution(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        updates: Optional[
            "capo_lambda.types.operation_updates.OperationUpdates"
        ] = None,
        client_token: Optional["capo_lambda.types.client_token.ClientToken"] = None,
    ) -> "capo_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse":
        r"""<p>Saves the progress of a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable function</a> execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typically don't need to call this API directly as the SDK handles checkpointing automatically.</p> <p>Each checkpoint operation consumes the current checkpoint token and returns a new one for the next checkpoint. This ensures that checkpoints are applied in the correct order and prevents duplicate or out-of-order state updates.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be used to ensure checkpoints are applied in the correct order. Each checkpoint operation consumes this token and returns a new one.</p>
            updates: <p>An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such as completing a step, starting a callback, or scheduling a timer. Updates are applied atomically as part of the checkpoint operation.</p>
            client_token: <p>An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda uses this token to detect and handle duplicate requests within a 15-minute window.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.checkpoint_durable_execution

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.checkpoint_durable_execution.checkpoint_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn,
            "checkpoint_token": checkpoint_token,
        }
        if updates is not None:
            input_["updates"] = updates
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_durable_execution_history(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        include_execution_data: Optional[
            "capo_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse":
        r"""<p>Retrieves the execution history for a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable execution</a>, showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progress over time.</p> <p>The history is available while the execution is running and for a retention period after it completes (1-90 days, default 30 days). You can control whether to include execution data such as step results and callback payloads.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            include_execution_data: <p>Specifies whether to include execution data such as step results and callback payloads in the history events. Set to <code>true</code> to include data, or <code>false</code> to exclude it for a more compact response. The default is <code>true</code>.</p>
            max_items: <p>The maximum number of history events to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of results. Each pagination token expires after 24 hours.</p>
            reverse_order: <p>When set to <code>true</code>, returns the history events in reverse chronological order (newest first). By default, events are returned in chronological order (oldest first).</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution_history

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_durable_execution_history.get_durable_execution_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_durable_execution_history(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        include_execution_data: Optional[
            "capo_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
    ) -> "Iterator[capo_lambda.types.event.Event]":
        _token = marker
        while True:
            _response = self.get_durable_execution_history(
                durable_execution_arn,
                config_overrides=config_overrides,
                include_execution_data=include_execution_data,
                max_items=max_items,
                marker=_token,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def get_durable_execution_state(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "capo_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse":
        r"""<p>Retrieves the current execution state required for the replay process during <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable function</a> execution. This API is used by the Lambda durable functions SDK to get state information needed for replay. You typically don't need to call this API directly as the SDK handles state management automatically.</p> <p>The response contains operations ordered by start sequence number in ascending order. Completed operations with children don't include child operation details since they don't need to be replayed.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and ensures that state retrieval is consistent with the current execution context.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of operations. Each pagination token expires after 24 hours.</p>
            max_items: <p>The maximum number of operations to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution_state

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_durable_execution_state.get_durable_execution_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest = {
            "durable_execution_arn": durable_execution_arn,
            "checkpoint_token": checkpoint_token,
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_durable_execution_state(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "Iterator[capo_lambda.types.operation.Operation]":
        _token = marker
        while True:
            _response = self.get_durable_execution_state(
                durable_execution_arn,
                checkpoint_token,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def stop_durable_execution(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        error: Optional["capo_lambda.types.error_object.ErrorObject"] = None,
    ) -> (
        "capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse"
    ):
        r"""<p>Stops a running <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable execution</a>. The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            error: <p>Optional error details explaining why the execution is being stopped.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.stop_durable_execution

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.stop_durable_execution.stop_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event_source_mapping(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        event_source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        enabled: Optional["capo_lambda.types.enabled.Enabled"] = None,
        batch_size: Optional["capo_lambda.types.batch_size.BatchSize"] = None,
        filter_criteria: Optional[
            "capo_lambda.types.filter_criteria.FilterCriteria"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        metrics_config: Optional[
            "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
        ] = None,
        logging_config: Optional[
            "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
        ] = None,
        scaling_config: Optional[
            "capo_lambda.types.scaling_config.ScalingConfig"
        ] = None,
        maximum_batching_window_in_seconds: Optional[
            "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
        ] = None,
        parallelization_factor: Optional[
            "capo_lambda.types.parallelization_factor.ParallelizationFactor"
        ] = None,
        starting_position: Optional[
            "capo_lambda.types.event_source_position.EventSourcePosition"
        ] = None,
        starting_position_timestamp: Optional["capo_lambda.types.date.Date"] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
        maximum_record_age_in_seconds: Optional[
            "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
        ] = None,
        bisect_batch_on_function_error: Optional[
            "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        tumbling_window_in_seconds: Optional[
            "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
        ] = None,
        topics: Optional["capo_lambda.types.topics.Topics"] = None,
        queues: Optional["capo_lambda.types.queues.Queues"] = None,
        source_access_configurations: Optional[
            "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
        ] = None,
        self_managed_event_source: Optional[
            "capo_lambda.types.self_managed_event_source.SelfManagedEventSource"
        ] = None,
        function_response_types: Optional[
            "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
        ] = None,
        amazon_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
        ] = None,
        self_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
        ] = None,
        document_db_event_source_config: Optional[
            "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
        ] = None,
        provisioned_poller_config: Optional[
            "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
        ] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        r"""<p>Creates a mapping between an event source and an Lambda function. Lambda reads items from the event source and invokes the function.</p> <p>For details about how to configure different event sources, see the following topics. </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping\"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping\"> Amazon Kinesis</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource\"> Amazon SQS</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping\"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html\"> Amazon MSK</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html\"> Apache Kafka</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html\"> Amazon DocumentDB</a> </p> </li> </ul> <p>The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka):</p> <ul> <li> <p> <code>BisectBatchOnFunctionError</code> – If the function returns an error, split the batch in two and retry.</p> </li> <li> <p> <code>MaximumRecordAgeInSeconds</code> – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires</p> </li> <li> <p> <code>MaximumRetryAttempts</code> – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p> </li> <li> <p> <code>OnFailure</code> – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations\">Adding a destination</a>.</p> </li> </ul> <p>The following option is available only for DynamoDB and Kinesis event sources:</p> <ul> <li> <p> <code>ParallelizationFactor</code> – Process multiple batches from each shard concurrently.</p> </li> </ul> <p>For information about which configuration parameters apply to each event source, see the following topics.</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params\"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params\"> Amazon Kinesis</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params\"> Amazon SQS</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params\"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms\"> Amazon MSK</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms\"> Apache Kafka</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration\"> Amazon DocumentDB</a> </p> </li> </ul>

        Args:
            event_source_arn: <p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc\">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            enabled: <p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>
            batch_size: <p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>
            filter_criteria: <p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html\">Lambda event filtering</a>.</p>
            kms_key_arn: <p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics\">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>
            metrics_config: <p>The metrics configuration for your event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics\">Event source mapping metrics</a>.</p>
            logging_config: <p>(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html\">Event source mapping logging</a>.</p>
            scaling_config: <p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency\">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>
            maximum_batching_window_in_seconds: <p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>
            parallelization_factor: <p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>
            starting_position: <p>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. <code>AT_TIMESTAMP</code> is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.</p>
            starting_position_timestamp: <p>With <code>StartingPosition</code> set to <code>AT_TIMESTAMP</code>, the time from which to start reading. <code>StartingPositionTimestamp</code> cannot be in the future.</p>
            destination_config: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>
            maximum_record_age_in_seconds: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>
            bisect_batch_on_function_error: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>
            maximum_retry_attempts: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>
            tags: <p>A list of tags to apply to the event source mapping.</p>
            tumbling_window_in_seconds: <p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>
            topics: <p>The name of the Kafka topic.</p>
            queues: <p> (MQ) The name of the Amazon MQ broker destination queue to consume. </p>
            source_access_configurations: <p>An array of authentication protocols or VPC components required to secure your event source.</p>
            self_managed_event_source: <p>The self-managed Apache Kafka cluster to receive records from.</p>
            function_response_types: <p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>
            amazon_managed_kafka_event_source_config: <p>Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.</p>
            self_managed_kafka_event_source_config: <p>Specific configuration settings for a self-managed Apache Kafka event source.</p>
            document_db_event_source_config: <p>Specific configuration settings for a DocumentDB event source.</p>
            provisioned_poller_config: <p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode\">provisioned mode</a>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a mapping between an event source and an AWS Lambda function
            The following example creates a mapping between an SQS queue and the my-function Lambda function.

            >>> client.create_event_source_mapping(batch_size=5, event_source_arn='arn:aws:sqs:us-west-2:123456789012:my-queue', function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_event_source_mapping_request.CreateEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_event_source_mapping.create_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.create_event_source_mapping_request.CreateEventSourceMappingRequest = {
            "function_name": function_name
        }
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if enabled is not None:
            input_["enabled"] = enabled
        if batch_size is not None:
            input_["batch_size"] = batch_size
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if maximum_batching_window_in_seconds is not None:
            input_["maximum_batching_window_in_seconds"] = (
                maximum_batching_window_in_seconds
            )
        if parallelization_factor is not None:
            input_["parallelization_factor"] = parallelization_factor
        if starting_position is not None:
            input_["starting_position"] = starting_position
        if starting_position_timestamp is not None:
            input_["starting_position_timestamp"] = starting_position_timestamp
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if maximum_record_age_in_seconds is not None:
            input_["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if bisect_batch_on_function_error is not None:
            input_["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if tags is not None:
            input_["tags"] = tags
        if tumbling_window_in_seconds is not None:
            input_["tumbling_window_in_seconds"] = tumbling_window_in_seconds
        if topics is not None:
            input_["topics"] = topics
        if queues is not None:
            input_["queues"] = queues
        if source_access_configurations is not None:
            input_["source_access_configurations"] = source_access_configurations
        if self_managed_event_source is not None:
            input_["self_managed_event_source"] = self_managed_event_source
        if function_response_types is not None:
            input_["function_response_types"] = function_response_types
        if amazon_managed_kafka_event_source_config is not None:
            input_["amazon_managed_kafka_event_source_config"] = (
                amazon_managed_kafka_event_source_config
            )
        if self_managed_kafka_event_source_config is not None:
            input_["self_managed_kafka_event_source_config"] = (
                self_managed_kafka_event_source_config
            )
        if document_db_event_source_config is not None:
            input_["document_db_event_source_config"] = document_db_event_source_config
        if provisioned_poller_config is not None:
            input_["provisioned_poller_config"] = provisioned_poller_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_source_mapping(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        """<p>Returns details about an event source mapping. You can get the identifier of a mapping from the output of <a>ListEventSourceMappings</a>.</p>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function's event source mapping
            The following example returns details about an event source mapping. To get a mapping's UUID, use ListEventSourceMappings.

            >>> client.get_event_source_mapping(uuid='14e0db71-xmpl-4eb5-b481-8945cf9d10c2')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_event_source_mapping_request.GetEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_event_source_mapping.get_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_event_source_mapping_request.GetEventSourceMappingRequest = {
            "uuid": uuid
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_event_source_mapping(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_name: Optional[
            "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
        ] = None,
        enabled: Optional["capo_lambda.types.enabled.Enabled"] = None,
        batch_size: Optional["capo_lambda.types.batch_size.BatchSize"] = None,
        filter_criteria: Optional[
            "capo_lambda.types.filter_criteria.FilterCriteria"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        metrics_config: Optional[
            "capo_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
        ] = None,
        logging_config: Optional[
            "capo_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
        ] = None,
        scaling_config: Optional[
            "capo_lambda.types.scaling_config.ScalingConfig"
        ] = None,
        maximum_batching_window_in_seconds: Optional[
            "capo_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
        ] = None,
        parallelization_factor: Optional[
            "capo_lambda.types.parallelization_factor.ParallelizationFactor"
        ] = None,
        destination_config: Optional[
            "capo_lambda.types.destination_config.DestinationConfig"
        ] = None,
        maximum_record_age_in_seconds: Optional[
            "capo_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
        ] = None,
        bisect_batch_on_function_error: Optional[
            "capo_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
        ] = None,
        maximum_retry_attempts: Optional[
            "capo_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
        ] = None,
        tumbling_window_in_seconds: Optional[
            "capo_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
        ] = None,
        source_access_configurations: Optional[
            "capo_lambda.types.source_access_configurations.SourceAccessConfigurations"
        ] = None,
        function_response_types: Optional[
            "capo_lambda.types.function_response_type_list.FunctionResponseTypeList"
        ] = None,
        amazon_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
        ] = None,
        self_managed_kafka_event_source_config: Optional[
            "capo_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
        ] = None,
        document_db_event_source_config: Optional[
            "capo_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
        ] = None,
        provisioned_poller_config: Optional[
            "capo_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
        ] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        r"""<p>Updates an event source mapping. You can change the function that Lambda invokes, or pause invocation and resume later from the same location.</p> <p>For details about how to configure different event sources, see the following topics. </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping\"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping\"> Amazon Kinesis</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource\"> Amazon SQS</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping\"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html\"> Amazon MSK</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html\"> Apache Kafka</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html\"> Amazon DocumentDB</a> </p> </li> </ul> <p>The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka):</p> <ul> <li> <p> <code>BisectBatchOnFunctionError</code> – If the function returns an error, split the batch in two and retry.</p> </li> <li> <p> <code>MaximumRecordAgeInSeconds</code> – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires</p> </li> <li> <p> <code>MaximumRetryAttempts</code> – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p> </li> <li> <p> <code>OnFailure</code> – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations\">Adding a destination</a>.</p> </li> </ul> <p>The following option is available only for DynamoDB and Kinesis event sources:</p> <ul> <li> <p> <code>ParallelizationFactor</code> – Process multiple batches from each shard concurrently.</p> </li> </ul> <p>For information about which configuration parameters apply to each event source, see the following topics.</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params\"> Amazon DynamoDB Streams</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params\"> Amazon Kinesis</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params\"> Amazon SQS</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params\"> Amazon MQ and RabbitMQ</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms\"> Amazon MSK</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms\"> Apache Kafka</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration\"> Amazon DocumentDB</a> </p> </li> </ul>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            enabled: <p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>
            batch_size: <p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>
            filter_criteria: <p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html\">Lambda event filtering</a>.</p>
            kms_key_arn: <p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics\">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>
            metrics_config: <p>The metrics configuration for your event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics\">Event source mapping metrics</a>.</p>
            scaling_config: <p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency\">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>
            maximum_batching_window_in_seconds: <p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>
            parallelization_factor: <p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>
            destination_config: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>
            maximum_record_age_in_seconds: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>
            bisect_batch_on_function_error: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>
            maximum_retry_attempts: <p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>
            tumbling_window_in_seconds: <p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>
            source_access_configurations: <p>An array of authentication protocols or VPC components required to secure your event source.</p>
            function_response_types: <p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>
            document_db_event_source_config: <p>Specific configuration settings for a DocumentDB event source.</p>
            provisioned_poller_config: <p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode\">provisioned mode</a>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDATING.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function event source mapping
            This operation updates a Lambda function event source mapping

            >>> client.update_event_source_mapping(batch_size=123, enabled=True, function_name='myFunction', uuid='a1b2c3d4-5678-90ab-cdef-11111EXAMPLE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_event_source_mapping_request.UpdateEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_event_source_mapping.update_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_event_source_mapping_request.UpdateEventSourceMappingRequest = {
            "uuid": uuid
        }
        if function_name is not None:
            input_["function_name"] = function_name
        if enabled is not None:
            input_["enabled"] = enabled
        if batch_size is not None:
            input_["batch_size"] = batch_size
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if metrics_config is not None:
            input_["metrics_config"] = metrics_config
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if maximum_batching_window_in_seconds is not None:
            input_["maximum_batching_window_in_seconds"] = (
                maximum_batching_window_in_seconds
            )
        if parallelization_factor is not None:
            input_["parallelization_factor"] = parallelization_factor
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if maximum_record_age_in_seconds is not None:
            input_["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
        if bisect_batch_on_function_error is not None:
            input_["bisect_batch_on_function_error"] = bisect_batch_on_function_error
        if maximum_retry_attempts is not None:
            input_["maximum_retry_attempts"] = maximum_retry_attempts
        if tumbling_window_in_seconds is not None:
            input_["tumbling_window_in_seconds"] = tumbling_window_in_seconds
        if source_access_configurations is not None:
            input_["source_access_configurations"] = source_access_configurations
        if function_response_types is not None:
            input_["function_response_types"] = function_response_types
        if amazon_managed_kafka_event_source_config is not None:
            input_["amazon_managed_kafka_event_source_config"] = (
                amazon_managed_kafka_event_source_config
            )
        if self_managed_kafka_event_source_config is not None:
            input_["self_managed_kafka_event_source_config"] = (
                self_managed_kafka_event_source_config
            )
        if document_db_event_source_config is not None:
            input_["document_db_event_source_config"] = document_db_event_source_config
        if provisioned_poller_config is not None:
            input_["provisioned_poller_config"] = provisioned_poller_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_source_mapping(
        self,
        uuid: "capo_lambda.types.uuid_string.UUIDString",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration":
        r"""<p>Deletes an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/intro-invocation-modes.html\">event source mapping</a>. You can get the identifier of a mapping from the output of <a>ListEventSourceMappings</a>.</p> <p>When you delete an event source mapping, it enters a <code>Deleting</code> state and might not be completely deleted for several seconds.</p>

        Args:
            uuid: <p>The identifier of the event source mapping.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDATING.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a Lambda function event source mapping
            The following example deletes an event source mapping. To get a mapping's UUID, use ListEventSourceMappings.

            >>> client.delete_event_source_mapping(uuid='14e0db71-xmpl-4eb5-b481-8945cf9d10c2')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_event_source_mapping_request.DeleteEventSourceMappingRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_event_source_mapping

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_event_source_mapping.delete_event_source_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_event_source_mapping_request.DeleteEventSourceMappingRequest = {
            "uuid": uuid
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_event_source_mappings(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        event_source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        function_name: Optional[
            "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse":
        r"""<p>Lists event source mappings. Specify an <code>EventSourceArn</code> to show only event source mappings for a single event source.</p>

        Args:
            event_source_arn: <p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc\">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of event source mappings to return. Note that ListEventSourceMappings returns a maximum of 100 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the event source mappings for a function
            The following example returns a list of the event source mappings for a function named my-function.

            >>> client.list_event_source_mappings(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_event_source_mappings_response.ListEventSourceMappingsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_event_source_mappings

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_event_source_mappings.list_event_source_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_event_source_mappings_request.ListEventSourceMappingsRequest = {}
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if function_name is not None:
            input_["function_name"] = function_name
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_function(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        role: "capo_lambda.types.role_arn.RoleArn",
        code: "capo_lambda.types.function_code.FunctionCode",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        handler: Optional["capo_lambda.types.handler.Handler"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        timeout: Optional["capo_lambda.types.timeout.Timeout"] = None,
        memory_size: Optional["capo_lambda.types.memory_size.MemorySize"] = None,
        publish: Optional["capo_lambda.types.boolean.Boolean"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
        vpc_config: Optional["capo_lambda.types.vpc_config.VpcConfig"] = None,
        package_type: Optional["capo_lambda.types.package_type.PackageType"] = None,
        dead_letter_config: Optional[
            "capo_lambda.types.dead_letter_config.DeadLetterConfig"
        ] = None,
        environment: Optional["capo_lambda.types.environment.Environment"] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        tracing_config: Optional[
            "capo_lambda.types.tracing_config.TracingConfig"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        layers: Optional["capo_lambda.types.layer_list.LayerList"] = None,
        file_system_configs: Optional[
            "capo_lambda.types.file_system_config_list.FileSystemConfigList"
        ] = None,
        code_signing_config_arn: Optional[
            "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
        ] = None,
        image_config: Optional["capo_lambda.types.image_config.ImageConfig"] = None,
        architectures: Optional[
            "capo_lambda.types.architectures_list.ArchitecturesList"
        ] = None,
        ephemeral_storage: Optional[
            "capo_lambda.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        snap_start: Optional["capo_lambda.types.snap_start.SnapStart"] = None,
        logging_config: Optional[
            "capo_lambda.types.logging_config.LoggingConfig"
        ] = None,
        tenancy_config: Optional[
            "capo_lambda.types.tenancy_config.TenancyConfig"
        ] = None,
        capacity_provider_config: Optional[
            "capo_lambda.types.capacity_provider_config.CapacityProviderConfig"
        ] = None,
        durable_config: Optional[
            "capo_lambda.types.durable_config.DurableConfig"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Creates a Lambda function. To create a function, you need a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html\">deployment package</a> and an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role\">execution role</a>. The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use Amazon Web Services services, such as Amazon CloudWatch Logs for log streaming and X-Ray for request tracing.</p> <p>If the deployment package is a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html\">container image</a>, then you set the package type to <code>Image</code>. For a container image, the code property must include the URI of a container image in the Amazon ECR registry. You do not need to specify the handler and runtime properties.</p> <p>If the deployment package is a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip\">.zip file archive</a>, then you set the package type to <code>Zip</code>. For a .zip file archive, the code property specifies the location of the .zip file. You must also specify the handler and runtime properties. The code in the deployment package must be compatible with the target instruction set architecture of the function (<code>x86-64</code> or <code>arm64</code>). If you do not specify the architecture, then the default value is <code>x86-64</code>.</p> <p>When you create a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute or so. During this time, you can't invoke or modify the function. The <code>State</code>, <code>StateReason</code>, and <code>StateReasonCode</code> fields in the response from <a>GetFunctionConfiguration</a> indicate when the function is ready to invoke. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">Lambda function states</a>.</p> <p>A function has an unpublished version, and can have published versions and aliases. The unpublished version changes when you update your function's code and configuration. A published version is a snapshot of your function code and configuration that can't be changed. An alias is a named resource that maps to a version, and can be changed to map to a different version. Use the <code>Publish</code> parameter to create version <code>1</code> of your function from its initial configuration.</p> <p>The other parameters let you configure version-specific and function-level settings. You can modify version-specific settings later with <a>UpdateFunctionConfiguration</a>. Function-level settings apply to both the unpublished and published versions of the function, and include tags (<a>TagResource</a>) and per-function concurrency limits (<a>PutFunctionConcurrency</a>).</p> <p>You can use code signing if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with <a>UpdateFunctionCode</a>, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes set of signing profiles, which define the trusted publishers for this function.</p> <p>If another Amazon Web Services account or an Amazon Web Services service invokes your function, use <a>AddPermission</a> to grant permission by creating a resource-based Identity and Access Management (IAM) policy. You can grant permissions at the function level, on a version, or on an alias.</p> <p>To invoke your function directly, use <a>Invoke</a>. To invoke your function in response to events in other Amazon Web Services services, create an event source mapping (<a>CreateEventSourceMapping</a>), or configure a function trigger in the other service. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html\">Invoking Lambda functions</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            runtime: <p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            role: <p>The Amazon Resource Name (ARN) of the function's execution role.</p>
            handler: <p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html\">Lambda programming model</a>.</p>
            code: <p>The code for the function.</p>
            description: <p>A description of the function.</p>
            timeout: <p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html\">Lambda execution environment</a>.</p>
            memory_size: <p>The amount of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console\">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>
            publish: <p>Set to true to publish the first version of the function during creation.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>
            vpc_config: <p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            package_type: <p>The type of deployment package. Set to <code>Image</code> for container image and set to <code>Zip</code> for .zip file archive.</p>
            dead_letter_config: <p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">Dead-letter queues</a>.</p>
            environment: <p>Environment variables that are accessible from function code during execution.</p>
            kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>
            tracing_config: <p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\">X-Ray</a>.</p>
            tags: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> to apply to the function.</p>
            layers: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>
            file_system_configs: <p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>
            code_signing_config_arn: <p>To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.</p>
            image_config: <p>Container image <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms\">configuration values</a> that override the values in the container image Dockerfile.</p>
            architectures: <p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>
            ephemeral_storage: <p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>
            snap_start: <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">SnapStart</a> setting.</p>
            logging_config: <p>The function's Amazon CloudWatch Logs configuration settings.</p>
            tenancy_config: <p>Configuration for multi-tenant applications that use Lambda functions. Defines tenant isolation settings and resource allocations. Required for functions supporting multiple tenants.</p>
            capacity_provider_config: <p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>
            durable_config: <p>Configuration settings for durable functions. Enables creating functions with durability that can remember their state and continue execution even after interruptions.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException: <p>The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a function
            The following example creates a function with a deployment package in Amazon S3 and enables X-Ray tracing and environment variable encryption.

            >>> client.create_function(code={'S3Bucket': 'my-bucket-1xpuxmplzrlbh', 'S3Key': 'function.zip'}, description='Process image objects from Amazon S3.', durable_config={'ExecutionTimeout': 31622400, 'RetentionPeriodInDays': 30}, environment={'Variables': {'BUCKET': 'my-bucket-1xpuxmplzrlbh', 'PREFIX': 'inbound'}}, function_name='my-function', handler='index.handler', kms_key_arn='arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966', memory_size=256, publish=True, role='arn:aws:iam::123456789012:role/lambda-role', runtime='nodejs12.x', tags={'DEPARTMENT': 'Assets'}, timeout=15, tracing_config={'Mode': 'Active'})
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_function_request.CreateFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_function.create_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.create_function_request.CreateFunctionRequest = {
            "function_name": function_name,
            "role": role,
            "code": code,
        }
        if runtime is not None:
            input_["runtime"] = runtime
        if handler is not None:
            input_["handler"] = handler
        if description is not None:
            input_["description"] = description
        if timeout is not None:
            input_["timeout"] = timeout
        if memory_size is not None:
            input_["memory_size"] = memory_size
        if publish is not None:
            input_["publish"] = publish
        if publish_to is not None:
            input_["publish_to"] = publish_to
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if package_type is not None:
            input_["package_type"] = package_type
        if dead_letter_config is not None:
            input_["dead_letter_config"] = dead_letter_config
        if environment is not None:
            input_["environment"] = environment
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tracing_config is not None:
            input_["tracing_config"] = tracing_config
        if tags is not None:
            input_["tags"] = tags
        if layers is not None:
            input_["layers"] = layers
        if file_system_configs is not None:
            input_["file_system_configs"] = file_system_configs
        if code_signing_config_arn is not None:
            input_["code_signing_config_arn"] = code_signing_config_arn
        if image_config is not None:
            input_["image_config"] = image_config
        if architectures is not None:
            input_["architectures"] = architectures
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if snap_start is not None:
            input_["snap_start"] = snap_start
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if tenancy_config is not None:
            input_["tenancy_config"] = tenancy_config
        if capacity_provider_config is not None:
            input_["capacity_provider_config"] = capacity_provider_config
        if durable_config is not None:
            input_["durable_config"] = durable_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_functions(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        master_region: Optional["capo_lambda.types.master_region.MasterRegion"] = None,
        function_version: Optional[
            "capo_lambda.types.function_version.FunctionVersion"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_functions_response.ListFunctionsResponse":
        """<p>Returns a list of Lambda functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call.</p> <p>Set <code>FunctionVersion</code> to <code>ALL</code> to include all published versions of each function in addition to the unpublished version.</p> <note> <p>The <code>ListFunctions</code> operation returns a subset of the <a>FunctionConfiguration</a> fields. To get the additional fields (State, StateReasonCode, StateReason, LastUpdateStatus, LastUpdateStatusReason, LastUpdateStatusReasonCode, RuntimeVersionConfig) for a function or version, use <a>GetFunction</a>.</p> </note>

        Args:
            master_region: <p>For Lambda@Edge functions, the Amazon Web Services Region of the master function. For example, <code>us-east-1</code> filters the list of functions to include only Lambda@Edge functions replicated from a master function in US East (N. Virginia). If specified, you must set <code>FunctionVersion</code> to <code>ALL</code>.</p>
            function_version: <p>Set to <code>ALL</code> to include entries for all published versions of each function.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of functions to return in the response. Note that <code>ListFunctions</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of Lambda functions
            This operation returns a list of Lambda functions.

            >>> client.list_functions()
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_functions

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_functions_request.ListFunctionsRequest = {}
        if master_region is not None:
            input_["master_region"] = master_region
        if function_version is not None:
            input_["function_version"] = function_version
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes a concurrent execution limit from a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove the reserved concurrent execution limit from a function
            The following example deletes the reserved concurrent execution limit from a function named my-function.

            >>> client.delete_function_concurrency(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_concurrency_request.DeleteFunctionConcurrencyRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_concurrency

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_concurrency.delete_function_concurrency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_concurrency_request.DeleteFunctionConcurrencyRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_concurrency_response.GetFunctionConcurrencyResponse":
        r"""<p>Returns details about the reserved concurrency configuration for a function. To set a concurrency limit for a function, use <a>PutFunctionConcurrency</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the reserved concurrency setting for a function
            The following example returns the reserved concurrency setting for a function named my-function.

            >>> client.get_function_concurrency(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_concurrency_request.GetFunctionConcurrencyRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_concurrency_response.GetFunctionConcurrencyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_concurrency

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_concurrency.get_function_concurrency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_concurrency_request.GetFunctionConcurrencyRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_provisioned_concurrency_configs(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_provisioned_concurrency_config_list_items.MaxProvisionedConcurrencyConfigListItems"
        ] = None,
    ) -> "capo_lambda.types.list_provisioned_concurrency_configs_response.ListProvisionedConcurrencyConfigsResponse":
        r"""<p>Retrieves a list of provisioned concurrency configurations for a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Specify a number to limit the number of configurations returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of provisioned concurrency configurations
            The following example returns a list of provisioned concurrency configurations for a function named my-function.

            >>> client.list_provisioned_concurrency_configs(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_provisioned_concurrency_configs_request.ListProvisionedConcurrencyConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_provisioned_concurrency_configs_response.ListProvisionedConcurrencyConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_provisioned_concurrency_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_provisioned_concurrency_configs.list_provisioned_concurrency_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_provisioned_concurrency_configs_request.ListProvisionedConcurrencyConfigsRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        reserved_concurrent_executions: "capo_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.concurrency.Concurrency":
        r"""<p>Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level.</p> <p>Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use <a>GetFunction</a> to see the current setting for a function.</p> <p>Use <a>GetAccountSettings</a> to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren't configured with a per-function limit. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html\">Lambda function scaling</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            reserved_concurrent_executions: <p>The number of simultaneous executions to reserve for the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure a reserved concurrency limit for a function
            The following example configures 100 reserved concurrent executions for the my-function function.

            >>> client.put_function_concurrency(function_name='my-function', reserved_concurrent_executions=100)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_concurrency_request.PutFunctionConcurrencyRequest]",
        ) -> OperationResponse["capo_lambda.types.concurrency.Concurrency"]:
            import capo_lambda._operations.aws_gir_api_service.put_function_concurrency

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_concurrency.put_function_concurrency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_concurrency_request.PutFunctionConcurrencyRequest = {
            "function_name": function_name,
            "reserved_concurrent_executions": reserved_concurrent_executions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_code(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        zip_file: Optional["capo_lambda.types.blob.Blob"] = None,
        s3_bucket: Optional["capo_lambda.types.s3_bucket.S3Bucket"] = None,
        s3_key: Optional["capo_lambda.types.s3_key.S3Key"] = None,
        s3_object_version: Optional[
            "capo_lambda.types.s3_object_version.S3ObjectVersion"
        ] = None,
        s3_object_storage_mode: Optional[
            "capo_lambda.types.s3_object_storage_mode.S3ObjectStorageMode"
        ] = None,
        image_uri: Optional["capo_lambda.types.string.String"] = None,
        architectures: Optional[
            "capo_lambda.types.architectures_list.ArchitecturesList"
        ] = None,
        publish: Optional["capo_lambda.types.boolean.Boolean"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
        dry_run: Optional["capo_lambda.types.boolean.Boolean"] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        source_kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Updates a Lambda function's code. If code signing is enabled for the function, the code package must be signed by a trusted publisher. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html\">Configuring code signing for Lambda</a>.</p> <p>If the function's package type is <code>Image</code>, then you must specify the code package in <code>ImageUri</code> as the URI of a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html\">container image</a> in the Amazon ECR registry.</p> <p>If the function's package type is <code>Zip</code>, then you must specify the deployment package as a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip\">.zip file archive</a>. Enter the Amazon S3 bucket and key of the code .zip file location. You can also provide the function code inline using the <code>ZipFile</code> field.</p> <p>The code in the deployment package must be compatible with the target instruction set architecture of the function (<code>x86-64</code> or <code>arm64</code>).</p> <p>The function's code is locked when you publish a version. You can't modify the code of a published version, only the unpublished version.</p> <note> <p>For a function defined as a container image, Lambda resolves the image tag to an image digest. In Amazon ECR, if you update the image tag to a new image, Lambda does not automatically update the function.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            zip_file: <p>The base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for you. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_bucket: <p>An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web Services account. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_key: <p>The Amazon S3 key of the deployment package. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_object_version: <p>For versioned objects, the version of the deployment package object to use.</p>
            s3_object_storage_mode: <p>Specifies how the deployment package is stored. Valid values:</p> <ul> <li> <p> <code>COPY</code> (default) – Uploads a copy of your deployment package to Lambda.</p> </li> <li> <p> <code>REFERENCE</code> – Lambda references the deployment package from the specified Amazon S3 bucket.</p> </li> </ul>
            image_uri: <p>URI of a container image in the Amazon ECR registry. Do not use for a function defined with a .zip file archive.</p>
            architectures: <p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>
            publish: <p>Set to true to publish a new version of the function after updating the code. This has the same effect as calling <a>PublishVersion</a> separately.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>
            dry_run: <p>Set to true to validate the request parameters and access permissions without modifying the function code.</p>
            revision_id: <p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>
            source_kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an Amazon Web Services managed key.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function's code
            The following example replaces the code of the unpublished ($LATEST) version of a function named my-function with the contents of the specified zip file in Amazon S3.

            >>> client.update_function_code(function_name='my-function', s3_bucket='my-bucket-1xpuxmplzrlbh', s3_key='function.zip')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_code_request.UpdateFunctionCodeRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_code

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_code.update_function_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_code_request.UpdateFunctionCodeRequest = {
            "function_name": function_name
        }
        if zip_file is not None:
            input_["zip_file"] = zip_file
        if s3_bucket is not None:
            input_["s3_bucket"] = s3_bucket
        if s3_key is not None:
            input_["s3_key"] = s3_key
        if s3_object_version is not None:
            input_["s3_object_version"] = s3_object_version
        if s3_object_storage_mode is not None:
            input_["s3_object_storage_mode"] = s3_object_storage_mode
        if image_uri is not None:
            input_["image_uri"] = image_uri
        if architectures is not None:
            input_["architectures"] = architectures
        if publish is not None:
            input_["publish"] = publish
        if publish_to is not None:
            input_["publish_to"] = publish_to
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if source_kms_key_arn is not None:
            input_["source_kms_key_arn"] = source_kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_configuration(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        role: Optional["capo_lambda.types.role_arn.RoleArn"] = None,
        handler: Optional["capo_lambda.types.handler.Handler"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        timeout: Optional["capo_lambda.types.timeout.Timeout"] = None,
        memory_size: Optional["capo_lambda.types.memory_size.MemorySize"] = None,
        vpc_config: Optional["capo_lambda.types.vpc_config.VpcConfig"] = None,
        environment: Optional["capo_lambda.types.environment.Environment"] = None,
        runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        dead_letter_config: Optional[
            "capo_lambda.types.dead_letter_config.DeadLetterConfig"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        tracing_config: Optional[
            "capo_lambda.types.tracing_config.TracingConfig"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        layers: Optional["capo_lambda.types.layer_list.LayerList"] = None,
        file_system_configs: Optional[
            "capo_lambda.types.file_system_config_list.FileSystemConfigList"
        ] = None,
        image_config: Optional["capo_lambda.types.image_config.ImageConfig"] = None,
        ephemeral_storage: Optional[
            "capo_lambda.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        snap_start: Optional["capo_lambda.types.snap_start.SnapStart"] = None,
        logging_config: Optional[
            "capo_lambda.types.logging_config.LoggingConfig"
        ] = None,
        capacity_provider_config: Optional[
            "capo_lambda.types.capacity_provider_config.CapacityProviderConfig"
        ] = None,
        durable_config: Optional[
            "capo_lambda.types.durable_config.DurableConfig"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Modify the version-specific settings of a Lambda function.</p> <p>When you update a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute. During this time, you can't modify the function, but you can still invoke it. The <code>LastUpdateStatus</code>, <code>LastUpdateStatusReason</code>, and <code>LastUpdateStatusReasonCode</code> fields in the response from <a>GetFunctionConfiguration</a> indicate when the update is complete and the function is processing events with the new configuration. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">Lambda function states</a>.</p> <p>These settings can vary between versions of a function and are locked when you publish a version. You can't modify the configuration of a published version, only the unpublished version.</p> <p>To configure function concurrency, use <a>PutFunctionConcurrency</a>. To grant invoke permissions to an Amazon Web Services account or Amazon Web Services service, use <a>AddPermission</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            role: <p>The Amazon Resource Name (ARN) of the function's execution role.</p>
            handler: <p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html\">Lambda programming model</a>.</p>
            description: <p>A description of the function.</p>
            timeout: <p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html\">Lambda execution environment</a>.</p>
            memory_size: <p>The amount of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console\">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>
            vpc_config: <p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            environment: <p>Environment variables that are accessible from function code during execution.</p>
            runtime: <p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            dead_letter_config: <p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">Dead-letter queues</a>.</p>
            kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>
            tracing_config: <p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\">X-Ray</a>.</p>
            revision_id: <p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>
            layers: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>
            file_system_configs: <p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>
            image_config: <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms\">Container image configuration values</a> that override the values in the container image Docker file.</p>
            ephemeral_storage: <p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>
            snap_start: <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">SnapStart</a> setting.</p>
            logging_config: <p>The function's Amazon CloudWatch Logs configuration settings.</p>
            capacity_provider_config: <p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>
            durable_config: <p>Configuration settings for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable functions</a>, including execution timeout, retention period for execution history, and an optional ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function's configuration
            The following example modifies the memory size to be 256 MB for the unpublished ($LATEST) version of a function named my-function.

            >>> client.update_function_configuration(durable_config={'ExecutionTimeout': 3600, 'RetentionPeriodInDays': 45}, function_name='my-function', memory_size=256)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_configuration_request.UpdateFunctionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_configuration

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_configuration.update_function_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_configuration_request.UpdateFunctionConfigurationRequest = {
            "function_name": function_name
        }
        if role is not None:
            input_["role"] = role
        if handler is not None:
            input_["handler"] = handler
        if description is not None:
            input_["description"] = description
        if timeout is not None:
            input_["timeout"] = timeout
        if memory_size is not None:
            input_["memory_size"] = memory_size
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if environment is not None:
            input_["environment"] = environment
        if runtime is not None:
            input_["runtime"] = runtime
        if dead_letter_config is not None:
            input_["dead_letter_config"] = dead_letter_config
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tracing_config is not None:
            input_["tracing_config"] = tracing_config
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if layers is not None:
            input_["layers"] = layers
        if file_system_configs is not None:
            input_["file_system_configs"] = file_system_configs
        if image_config is not None:
            input_["image_config"] = image_config
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if snap_start is not None:
            input_["snap_start"] = snap_start
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if capacity_provider_config is not None:
            input_["capacity_provider_config"] = capacity_provider_config
        if durable_config is not None:
            input_["durable_config"] = durable_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        auth_type: "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
        cors: Optional["capo_lambda.types.cors.Cors"] = None,
        invoke_mode: Optional["capo_lambda.types.invoke_mode.InvokeMode"] = None,
    ) -> "capo_lambda.types.create_function_url_config_response.CreateFunctionUrlConfigResponse":
        r"""<p>Creates a Lambda function URL with the specified configuration parameters. A function URL is a dedicated HTTP(S) endpoint that you can use to invoke your function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>
            auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>
            cors: <p>The <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>
            invoke_mode: <p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_function_url_config_request.CreateFunctionUrlConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.create_function_url_config_response.CreateFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_function_url_config.create_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.create_function_url_config_request.CreateFunctionUrlConfigRequest = {
            "function_name": function_name,
            "auth_type": auth_type,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if cors is not None:
            input_["cors"] = cors
        if invoke_mode is not None:
            input_["invoke_mode"] = invoke_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_code_signing_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes the code signing configuration from the function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_code_signing_config_request.DeleteFunctionCodeSigningConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_code_signing_config.delete_function_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_code_signing_config_request.DeleteFunctionCodeSigningConfigRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
    ) -> None:
        r"""<p>Deletes a Lambda function URL. When you delete a function URL, you can't recover it. Creating a new function URL results in a different URL address.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_url_config_request.DeleteFunctionUrlConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_url_config.delete_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_url_config_request.DeleteFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_function_response.GetFunctionResponse":
        r"""<p>Returns information about the function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details that are specific to that version are returned.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get details about a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function
            The following example returns code and configuration details for version 1 of a function named my-function.

            >>> client.get_function(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_request.GetFunctionRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def wait_until_function_exists(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        max_wait_time: float,
        min_delay: float = 1,
        max_delay: float = 20,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_function_response.GetFunctionResponse":
        r"""Wait for function_exists.

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            qualifier: <p>Specify a version or alias to get details about a published version of the function.</p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_lambda.types.get_function_response.GetFunctionResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = self.get_function(  # noqa: F841
                    function_name,
                    config_overrides=config_overrides,
                    qualifier=qualifier,
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                return op_output
            elif op_error is not None and op_error.code == "ResourceNotFoundException":
                pass

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("function_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            time.sleep(delay)
            attempt += 1

    def get_function_code_signing_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_code_signing_config_response.GetFunctionCodeSigningConfigResponse":
        r"""<p>Returns the code signing configuration for the specified function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_code_signing_config_request.GetFunctionCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_code_signing_config_response.GetFunctionCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_code_signing_config.get_function_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_code_signing_config_request.GetFunctionCodeSigningConfigRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_configuration(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Returns the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function. To modify these settings, use <a>UpdateFunctionConfiguration</a>.</p> <p>To get all of a function's details, including function-level settings, use <a>GetFunction</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get details about a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function's event source mapping
            The following example returns and configuration details for version 1 of a function named my-function.

            >>> client.get_function_configuration(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_configuration_request.GetFunctionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_configuration

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_configuration.get_function_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_configuration_request.GetFunctionConfigurationRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_recursion_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_recursion_config_response.GetFunctionRecursionConfigResponse":
        r"""<p>Returns your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html\">recursive loop detection</a> configuration. </p>

        Args:
            function_name: <p>The name of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_recursion_config_request.GetFunctionRecursionConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_recursion_config_response.GetFunctionRecursionConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_recursion_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_recursion_config.get_function_recursion_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_recursion_config_request.GetFunctionRecursionConfigRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_scaling_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        qualifier: "capo_lambda.types.published_function_qualifier.PublishedFunctionQualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_scaling_config_response.GetFunctionScalingConfigResponse":
        """<p>Retrieves the scaling configuration for a Lambda Managed Instances function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p>
            qualifier: <p>Specify a version or alias to get the scaling configuration for a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_scaling_config_request.GetFunctionScalingConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_scaling_config_response.GetFunctionScalingConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_scaling_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_scaling_config.get_function_scaling_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_scaling_config_request.GetFunctionScalingConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_function_url_config_response.GetFunctionUrlConfigResponse":
        r"""<p>Returns details about a Lambda function URL.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_url_config_request.GetFunctionUrlConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_url_config_response.GetFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_url_config.get_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_url_config_request.GetFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_policy_response.GetPolicyResponse":
        r"""<p>Returns the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html\">resource-based IAM policy</a> for a function, version, or alias.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get the policy for that resource.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve a Lambda function policy
            The following example returns the resource-based policy for version 1 of a Lambda function named my-function.

            >>> client.get_policy(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_policy_request.GetPolicyRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_policy

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_policy_request.GetPolicyRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_runtime_management_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_runtime_management_config_response.GetRuntimeManagementConfigResponse":
        r"""<p>Retrieves the runtime management configuration for a function's version. If the runtime update mode is <b>Manual</b>, this includes the ARN of the runtime version and the runtime update mode. If the runtime update mode is <b>Auto</b> or <b>Function update</b>, this includes the runtime update mode and <code>null</code> is returned for the ARN. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html\">Runtime updates</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version of the function. This can be <code>$LATEST</code> or a published version number. If no value is specified, the configuration for the <code>$LATEST</code> version is returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_runtime_management_config_request.GetRuntimeManagementConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_runtime_management_config_response.GetRuntimeManagementConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_runtime_management_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_runtime_management_config.get_runtime_management_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_runtime_management_config_request.GetRuntimeManagementConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        invocation_type: Optional[
            "capo_lambda.types.invocation_type.InvocationType"
        ] = None,
        log_type: Optional["capo_lambda.types.log_type.LogType"] = None,
        client_context: Optional["capo_lambda.types.string.String"] = None,
        durable_execution_name: Optional[
            "capo_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        payload: Optional["capo_lambda.types.blob.Blob"] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        tenant_id: Optional["capo_lambda.types.tenant_id.TenantId"] = None,
    ) -> "capo_lambda.types.invocation_response.InvocationResponse":
        r"""<p>Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the<code>InvocationType</code> is <code>RequestResponse</code>). To invoke a function asynchronously, set <code>InvocationType</code> to <code>Event</code>. Lambda passes the <code>ClientContext</code> object to your function for synchronous invocations only.</p> <p>For synchronous invocations, the maximum payload size is 6 MB. For asynchronous invocations, the maximum payload size is 1 MB.</p> <p>For <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html\">synchronous invocation</a>, details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html\">execution log</a> and <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html\">trace</a>.</p> <p>When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html\">Error handling and automatic retries in Lambda</a>.</p> <p>For <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html\">asynchronous invocation</a>, Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">dead-letter queue</a>.</p> <p>The status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">quota</a> errors, or issues with your function's code and configuration. For example, Lambda returns <code>TooManyRequestsException</code> if running the function would cause you to exceed a concurrency limit at either the account level (<code>ConcurrentInvocationLimitExceeded</code>) or function level (<code>ReservedFunctionConcurrentInvocationLimitExceeded</code>).</p> <p>For functions with a long timeout, your client might disconnect during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.</p> <p>This operation requires permission for the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html\">lambda:InvokeFunction</a> action. For details on how to set up permissions for cross-account invocations, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke\">Granting function access to other accounts</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            invocation_type: <p>Choose from the following options.</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.</p> </li> <li> <p> <code>Event</code> – Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if one is configured). The API response only includes a status code.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the user or role has permission to invoke the function.</p> </li> </ul>
            log_type: <p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>
            client_context: <p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda passes the <code>ClientContext</code> object to your function for synchronous invocations only.</p>
            durable_execution_name: <p>A unique name for the durable execution. If you invoke a durable function using a name that already exists with the same payload, Lambda returns the existing execution instead of creating a duplicate. If the payload differs, Lambda returns a <code>DurableExecutionAlreadyStartedException</code> error.</p> <p>If not specified, Lambda generates a unique identifier automatically. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-idempotency.html#durable-idempotency-execution-names\">Execution names</a>.</p>
            payload: <p>The JSON that you want to provide to your Lambda function as input. The maximum payload size is 6 MB for synchronous invocations and 1 MB for asynchronous invocations.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ \"key\": \"value\" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>
            qualifier: <p>Specify a version or alias to invoke a published version of the function.</p>
            tenant_id: <p>The identifier of the tenant in a multi-tenant Lambda function.</p>

        Raises:
            capo_lambda.errors.code_artifact_user_deleted_exception.CodeArtifactUserDeletedException: <p>The Lambda function couldn't be invoked because its code artifact user has been deleted. Wait for Lambda to provision a new code artifact user, or update the function's code package to recreate it.</p>
            capo_lambda.errors.code_artifact_user_failed_exception.CodeArtifactUserFailedException: <p>The Lambda function couldn't be invoked because provisioning of its code artifact user failed. Update the function's code package or check the Lambda function's <code>State</code> and <code>StateReasonCode</code> for additional context.</p>
            capo_lambda.errors.code_artifact_user_pending_exception.CodeArtifactUserPendingException: <p>The Lambda function couldn't be invoked because its code artifact user is still being provisioned. Wait for the function's <code>State</code> to become <code>Active</code> and try the request again.</p>
            capo_lambda.errors.durable_execution_already_started_exception.DurableExecutionAlreadyStartedException: <p>The durable execution with the specified name has already been started. Each durable execution name must be unique within the function. Use a different name or check the status of the existing execution.</p>
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.eni_not_ready_exception.ENINotReadyException: <p>Lambda couldn't invoke the Lambda function because the elastic network interface (ENI) configured for its VPC connection isn't ready yet. Wait a few moments and try the request again. For more information about VPC configuration, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException: <p>Lambda could not unzip the deployment package.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.mode_not_supported_exception.ModeNotSupportedException: <p>The Lambda function doesn't support the invocation mode requested. For example, calling <code>Invoke</code> with <code>InvocationType=RequestResponse</code> on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html\">Invoking Lambda functions</a>.</p>
            capo_lambda.errors.no_published_version_exception.NoPublishedVersionException: <p>The function has no published versions available.</p>
            capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException: <p>Lambda has detected your function being invoked in a recursive loop with other Amazon Web Services resources and stopped your function's invocation.</p>
            capo_lambda.errors.request_too_large_exception.RequestTooLargeException: <p>The request payload exceeded the <code>Invoke</code> request body JSON input quota. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException: <p>The request payload exceeded the maximum allowed size for serialized request entities.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException: <p>The content type of the <code>Invoke</code> request body is not JSON.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To invoke a Lambda function
            The following example invokes version 1 of a function named my-function with an empty event payload.

            >>> client.invoke(durable_execution_name='myExecution', function_name='my-function', invocation_type='Event', payload='{}', qualifier='1')
            To invoke a Lambda function asynchronously
            The following example invokes version 1 of a function named my-function asynchronously.

            >>> client.invoke(function_name='my-function', invocation_type='Event', payload='{}', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.invocation_request.InvocationRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.invocation_response.InvocationResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.invoke.invoke(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.invocation_request.InvocationRequest = {
            "function_name": function_name
        }
        if invocation_type is not None:
            input_["invocation_type"] = invocation_type
        if log_type is not None:
            input_["log_type"] = log_type
        if client_context is not None:
            input_["client_context"] = client_context
        if durable_execution_name is not None:
            input_["durable_execution_name"] = durable_execution_name
        if payload is not None:
            input_["payload"] = payload
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if tenant_id is not None:
            input_["tenant_id"] = tenant_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke_async(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        invoke_args: Body[Iterator[bytes]] | Iterator[bytes] | bytes,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.invoke_async_response.InvokeAsyncResponse":
        r"""<note> <p>For asynchronous function invocation, use <a>Invoke</a>.</p> </note> <p>Invokes a function asynchronously.</p> <note> <p>The payload limit is 256KB. For larger payloads, for up to 1MB, use <a>Invoke</a>.</p> </note> <note> <p>If you do use the InvokeAsync action, note that it doesn't support the use of X-Ray active tracing. Trace ID is not propagated to the function, even if X-Ray active tracing is turned on.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            invoke_args: <p>The JSON that you want to provide to your Lambda function as input.</p>

        Raises:
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.mode_not_supported_exception.ModeNotSupportedException: <p>The Lambda function doesn't support the invocation mode requested. For example, calling <code>Invoke</code> with <code>InvocationType=RequestResponse</code> on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html\">Invoking Lambda functions</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To invoke a Lambda function asynchronously
            The following example invokes a Lambda function asynchronously

            >>> client.invoke_async(function_name='my-function', invoke_args='{}')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.invoke_async_request.InvokeAsyncRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.invoke_async_response.InvokeAsyncResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke_async

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.invoke_async.invoke_async(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.invoke_async_request.InvokeAsyncRequest = {
            "function_name": function_name,
            "invoke_args": ensure_sync_iterator(invoke_args),
        }

        with closing_bodies(input_):
            response = execute_pipeline(
                OperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            response.response.close()
            return response.output

    @contextmanager
    def invoke_with_response_stream(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        log_type: Optional["capo_lambda.types.log_type.LogType"] = None,
        client_context: Optional["capo_lambda.types.string.String"] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        payload: Optional["capo_lambda.types.blob.Blob"] = None,
        tenant_id: Optional["capo_lambda.types.tenant_id.TenantId"] = None,
        invocation_type: Optional[
            "capo_lambda.types.response_streaming_invocation_type.ResponseStreamingInvocationType"
        ] = None,
    ) -> "Generator[capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse]":
        r"""<p>Configure your Lambda functions to stream response payloads back to clients. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html\">Configuring a Lambda function to stream responses</a>.</p> <p>This operation requires permission for the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html\">lambda:InvokeFunction</a> action. For details on how to set up permissions for cross-account invocations, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke\">Granting function access to other accounts</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            log_type: <p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>
            client_context: <p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.</p>
            qualifier: <p>The alias name.</p>
            payload: <p>The JSON that you want to provide to your Lambda function as input.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ \"key\": \"value\" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>
            tenant_id: <p>The identifier of the tenant in a multi-tenant Lambda function.</p>
            invocation_type: <p>Use one of the following options:</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API operation response includes the function response and additional data.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the IAM user or role has permission to invoke the function.</p> </li> </ul>

        Raises:
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException: <p>Lambda could not unzip the deployment package.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.no_published_version_exception.NoPublishedVersionException: <p>The function has no published versions available.</p>
            capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException: <p>Lambda has detected your function being invoked in a recursive loop with other Amazon Web Services resources and stopped your function's invocation.</p>
            capo_lambda.errors.request_too_large_exception.RequestTooLargeException: <p>The request payload exceeded the <code>Invoke</code> request body JSON input quota. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException: <p>The request payload exceeded the maximum allowed size for serialized request entities.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException: <p>The content type of the <code>Invoke</code> request body is not JSON.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke_with_response_stream

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.invoke_with_response_stream.invoke_with_response_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest = {
            "function_name": function_name
        }
        if log_type is not None:
            input_["log_type"] = log_type
        if client_context is not None:
            input_["client_context"] = client_context
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if payload is not None:
            input_["payload"] = payload
        if tenant_id is not None:
            input_["tenant_id"] = tenant_id
        if invocation_type is not None:
            input_["invocation_type"] = invocation_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def list_durable_executions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        durable_execution_name: Optional[
            "capo_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        statuses: Optional[
            "capo_lambda.types.execution_status_list.ExecutionStatusList"
        ] = None,
        started_after: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        started_before: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "capo_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse":
        r"""<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable executions</a> for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.</p>
            qualifier: <p>The function version or alias. If not specified, lists executions for the $LATEST version.</p>
            durable_execution_name: <p>Filter executions by name. Only executions with names that matches this string are returned.</p>
            statuses: <p>Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED.</p>
            started_after: <p>Filter executions that started after this timestamp (ISO 8601 format).</p>
            started_before: <p>Filter executions that started before this timestamp (ISO 8601 format).</p>
            reverse_order: <p>Set to true to return results in chronological order (oldest first). Default is false.</p>
            marker: <p>Pagination token from a previous request to continue retrieving results.</p>
            max_items: <p>Maximum number of executions to return (1-1000). Default is 100.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_durable_executions_by_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_durable_executions_by_function.list_durable_executions_by_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if durable_execution_name is not None:
            input_["durable_execution_name"] = durable_execution_name
        if statuses is not None:
            input_["statuses"] = statuses
        if started_after is not None:
            input_["started_after"] = started_after
        if started_before is not None:
            input_["started_before"] = started_before
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_durable_executions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        durable_execution_name: Optional[
            "capo_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        statuses: Optional[
            "capo_lambda.types.execution_status_list.ExecutionStatusList"
        ] = None,
        started_after: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        started_before: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "Iterator[capo_lambda.types.execution.Execution]":
        _token = marker
        while True:
            _response = self.list_durable_executions_by_function(
                function_name,
                config_overrides=config_overrides,
                qualifier=qualifier,
                durable_execution_name=durable_execution_name,
                statuses=statuses,
                started_after=started_after,
                started_before=started_before,
                reverse_order=reverse_order,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("durable_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_function_url_configs(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_items.MaxItems"] = None,
    ) -> "capo_lambda.types.list_function_url_configs_response.ListFunctionUrlConfigsResponse":
        r"""<p>Returns a list of Lambda function URLs for the specified function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of function URLs to return in the response. Note that <code>ListFunctionUrlConfigs</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_function_url_configs_request.ListFunctionUrlConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_function_url_configs_response.ListFunctionUrlConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_url_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_function_url_configs.list_function_url_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_url_configs_request.ListFunctionUrlConfigsRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_function_code_signing_config_response.PutFunctionCodeSigningConfigResponse":
        r"""<p>Update the code signing configuration for the function. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_code_signing_config_request.PutFunctionCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_function_code_signing_config_response.PutFunctionCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_code_signing_config.put_function_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_code_signing_config_request.PutFunctionCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn,
            "function_name": function_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_recursion_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        recursive_loop: "capo_lambda.types.recursive_loop.RecursiveLoop",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_function_recursion_config_response.PutFunctionRecursionConfigResponse":
        r"""<p>Sets your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html\">recursive loop detection</a> configuration.</p> <p>When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infinite recursive loop. For example, a Lambda function might write a message to an Amazon Simple Queue Service (Amazon SQS) queue, which then invokes the same function. This invocation causes the function to write another message to the queue, which in turn invokes the function again.</p> <p>Lambda can detect certain types of recursive loops shortly after they occur. When Lambda detects a recursive loop and your function's recursive loop detection configuration is set to <code>Terminate</code>, it stops your function being invoked and notifies you.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            recursive_loop: <p>If you set your function's recursive loop detection configuration to <code>Allow</code>, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop. We recommend that you only use this setting if your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes it.</p> <p>If you set your function's recursive loop detection configuration to <code>Terminate</code>, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.</p> <p>By default, Lambda sets your function's configuration to <code>Terminate</code>.</p> <important> <p>If your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes the function, then use caution and implement suitable guard rails to prevent unexpected charges being billed to your Amazon Web Services account. To learn more about best practices for using recursive invocation patterns, see <a href=\"https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/recursive-runaway\">Recursive patterns that cause run-away Lambda functions</a> in Serverless Land.</p> </important>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_recursion_config_request.PutFunctionRecursionConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_function_recursion_config_response.PutFunctionRecursionConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_recursion_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_recursion_config.put_function_recursion_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_recursion_config_request.PutFunctionRecursionConfigRequest = {
            "function_name": function_name,
            "recursive_loop": recursive_loop,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_scaling_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        qualifier: "capo_lambda.types.published_function_qualifier.PublishedFunctionQualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_scaling_config: Optional[
            "capo_lambda.types.function_scaling_config.FunctionScalingConfig"
        ] = None,
    ) -> "capo_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse":
        """<p>Sets the scaling configuration for a Lambda Managed Instances function. The scaling configuration defines the minimum and maximum number of execution environments that can be provisioned for the function, allowing you to control scaling behavior and resource allocation.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p>
            qualifier: <p>Specify a version or alias to set the scaling configuration for a published version of the function.</p>
            function_scaling_config: <p>The scaling configuration to apply to the function, including minimum and maximum execution environment limits.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_scaling_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_scaling_config.put_function_scaling_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }
        if function_scaling_config is not None:
            input_["function_scaling_config"] = function_scaling_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_runtime_management_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        update_runtime_on: "capo_lambda.types.update_runtime_on.UpdateRuntimeOn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        runtime_version_arn: Optional[
            "capo_lambda.types.runtime_version_arn.RuntimeVersionArn"
        ] = None,
    ) -> "capo_lambda.types.put_runtime_management_config_response.PutRuntimeManagementConfigResponse":
        r"""<p>Sets the runtime management configuration for a function's version. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html\">Runtime updates</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version of the function. This can be <code>$LATEST</code> or a published version number. If no value is specified, the configuration for the <code>$LATEST</code> version is returned.</p>
            update_runtime_on: <p>Specify the runtime update mode.</p> <ul> <li> <p> <b>Auto (default)</b> - Automatically update to the most recent and secure runtime version using a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-two-phase\">Two-phase runtime version rollout</a>. This is the best choice for most customers to ensure they always benefit from runtime updates.</p> </li> <li> <p> <b>Function update</b> - Lambda updates the runtime of your function to the most recent and secure runtime version when you update your function. This approach synchronizes runtime updates with function deployments, giving you control over when runtime updates are applied and allowing you to detect and mitigate rare runtime update incompatibilities early. When using this setting, you need to regularly update your functions to keep their runtime up-to-date.</p> </li> <li> <p> <b>Manual</b> - You specify a runtime version in your function configuration. The function will use this runtime version indefinitely. In the rare case where a new runtime version is incompatible with an existing function, this allows you to roll back your function to an earlier runtime version. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-rollback\">Roll back a runtime version</a>.</p> </li> </ul>
            runtime_version_arn: <p>The ARN of the runtime version you want the function to use.</p> <note> <p>This is only required if you're using the <b>Manual</b> runtime update mode.</p> </note>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_runtime_management_config_request.PutRuntimeManagementConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_runtime_management_config_response.PutRuntimeManagementConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_runtime_management_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_runtime_management_config.put_runtime_management_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_runtime_management_config_request.PutRuntimeManagementConfigRequest = {
            "function_name": function_name,
            "update_runtime_on": update_runtime_on,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if runtime_version_arn is not None:
            input_["runtime_version_arn"] = runtime_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
        auth_type: Optional[
            "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
        ] = None,
        cors: Optional["capo_lambda.types.cors.Cors"] = None,
        invoke_mode: Optional["capo_lambda.types.invoke_mode.InvokeMode"] = None,
    ) -> "capo_lambda.types.update_function_url_config_response.UpdateFunctionUrlConfigResponse":
        r"""<p>Updates the configuration for a Lambda function URL.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>
            auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>
            cors: <p>The <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>
            invoke_mode: <p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_url_config_request.UpdateFunctionUrlConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.update_function_url_config_response.UpdateFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_url_config.update_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_url_config_request.UpdateFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if cors is not None:
            input_["cors"] = cors
        if invoke_mode is not None:
            input_["invoke_mode"] = invoke_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_alias(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        function_version: "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        routing_config: Optional[
            "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
        ] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        r"""<p>Creates an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html\">alias</a> for a Lambda function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version.</p> <p>You can also map an alias to split invocation requests between two versions. Use the <code>RoutingConfig</code> parameter to specify a second version and the percentage of invocation requests that it receives.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>
            function_version: <p>The function version that the alias invokes.</p>
            description: <p>A description of the alias.</p>
            routing_config: <p>The <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing\">routing configuration</a> of the alias.</p>

        Raises:
            capo_lambda.errors.alias_limit_exceeded_exception.AliasLimitExceededException: <p>Lambda couldn't create the alias because your Amazon Web Services account has exceeded the maximum number of aliases allowed per Lambda function. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an alias for a Lambda function
            The following example creates an alias named LIVE that points to version 1 of the my-function Lambda function.

            >>> client.create_alias(description='alias for live version of function', function_name='my-function', function_version='1', name='LIVE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_alias_request.CreateAliasRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_alias.create_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.create_alias_request.CreateAliasRequest = {
            "function_name": function_name,
            "name": name,
            "function_version": function_version,
        }
        if description is not None:
            input_["description"] = description
        if routing_config is not None:
            input_["routing_config"] = routing_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_alias(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        r"""<p>Returns details about a Lambda function <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html\">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function alias
            The following example returns details about an alias named BLUE for a function named my-function

            >>> client.get_alias(function_name='my-function', name='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_alias_request.GetAliasRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_alias.get_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_alias_request.GetAliasRequest = {
            "function_name": function_name,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_alias(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_version: Optional[
            "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
        ] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        routing_config: Optional[
            "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        r"""<p>Updates the configuration of a Lambda function <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html\">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>
            function_version: <p>The function version that the alias invokes.</p>
            description: <p>A description of the alias.</p>
            routing_config: <p>The <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing\">routing configuration</a> of the alias.</p>
            revision_id: <p>Only update the alias if the revision ID matches the ID that's specified. Use this option to avoid modifying an alias that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a function alias
            The following example updates the alias named BLUE to send 30% of traffic to version 2 and 70% to version 1.

            >>> client.update_alias(function_name='my-function', function_version='2', name='BLUE', routing_config={'AdditionalVersionWeights': {'1': 0.7}})
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_alias_request.UpdateAliasRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_alias.update_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.update_alias_request.UpdateAliasRequest = {
            "function_name": function_name,
            "name": name,
        }
        if function_version is not None:
            input_["function_version"] = function_version
        if description is not None:
            input_["description"] = description
        if routing_config is not None:
            input_["routing_config"] = routing_config
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_alias(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Deletes a Lambda function <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html\">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a Lambda function alias
            The following example deletes an alias named BLUE from a function named my-function

            >>> client.delete_alias(function_name='my-function', name='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_alias_request.DeleteAliasRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_alias.delete_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_alias_request.DeleteAliasRequest = {
            "function_name": function_name,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_aliases(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_version: Optional[
            "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_aliases_response.ListAliasesResponse":
        r"""<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html\">aliases</a> for a Lambda function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            function_version: <p>Specify a function version to only list aliases that invoke that version.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Limit the number of aliases returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list a function's aliases
            The following example returns a list of aliases for a function named my-function.

            >>> client.list_aliases(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_aliases_request.ListAliasesRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_aliases_response.ListAliasesResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_aliases

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_aliases.list_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_aliases_request.ListAliasesRequest = {
            "function_name": function_name
        }
        if function_version is not None:
            input_["function_version"] = function_version
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_version(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        code_sha256: Optional["capo_lambda.types.string.String"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Creates a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html\">version</a> from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change.</p> <p>Lambda doesn't publish a version if the function's configuration and code haven't changed since the last version. Use <a>UpdateFunctionCode</a> or <a>UpdateFunctionConfiguration</a> to update the function before publishing a version.</p> <p>Clients can invoke versions directly or with an alias. To create an alias, use <a>CreateAlias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            code_sha256: <p>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of <a>UpdateFunctionCode</a>.</p>
            description: <p>A description for the version to override the description in the function configuration.</p>
            revision_id: <p>Only update the function if the revision ID matches the ID that's specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>

        Raises:
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException: <p>The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To publish a version of a Lambda function
            This operation publishes a version of a Lambda function

            >>> client.publish_version(code_sha256='', description='', function_name='myFunction')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.publish_version_request.PublishVersionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.publish_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.publish_version.publish_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.publish_version_request.PublishVersionRequest = {
            "function_name": function_name
        }
        if code_sha256 is not None:
            input_["code_sha256"] = code_sha256
        if description is not None:
            input_["description"] = description
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if publish_to is not None:
            input_["publish_to"] = publish_to

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_versions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse":
        r"""<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html\">versions</a>, with the version-specific configuration of each. Lambda returns up to 50 versions per call.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of versions to return. Note that <code>ListVersionsByFunction</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list versions of a function
            The following example returns a list of versions of a function named my-function

            >>> client.list_versions_by_function(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_versions_by_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_versions_by_function.list_versions_by_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_versions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "Iterator[capo_lambda.types.function_configuration.FunctionConfiguration]":
        _token = marker
        while True:
            _response = self.list_versions_by_function(
                function_name,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_layers(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        compatible_architecture: Optional[
            "capo_lambda.types.architecture.Architecture"
        ] = None,
        compatible_runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
    ) -> "capo_lambda.types.list_layers_response.ListLayersResponse":
        r"""<p>Lists <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html\">Lambda layers</a> and shows information about the latest version of each. Specify a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\">runtime identifier</a> to list only layers that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layers that are compatible with that <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>

        Args:
            compatible_architecture: <p>The compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of layers to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the layers that are compatible with your function's runtime
            The following example returns information about layers that are compatible with the Python 3.7 runtime.

            >>> client.list_layers(compatible_runtime='python3.7')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_layers_request.ListLayersRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_layers_response.ListLayersResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_layers

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_layers.list_layers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_layers_request.ListLayersRequest = {}
        if compatible_architecture is not None:
            input_["compatible_architecture"] = compatible_architecture
        if compatible_runtime is not None:
            input_["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_layer_versions(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        compatible_architecture: Optional[
            "capo_lambda.types.architecture.Architecture"
        ] = None,
        compatible_runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
    ) -> "capo_lambda.types.list_layer_versions_response.ListLayerVersionsResponse":
        r"""<p>Lists the versions of an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a>. Versions that have been deleted aren't listed. Specify a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\">runtime identifier</a> to list only versions that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layer versions that are compatible with that architecture.</p>

        Args:
            compatible_architecture: <p>The compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architecture</a>.</p>
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of versions to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list versions of a layer
            The following example displays information about the versions for the layer named blank-java-lib

            >>> client.list_layer_versions(layer_name='blank-java-lib')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_layer_versions_request.ListLayerVersionsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_layer_versions_response.ListLayerVersionsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_layer_versions

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_layer_versions.list_layer_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.list_layer_versions_request.ListLayerVersionsRequest = {
            "layer_name": layer_name
        }
        if compatible_architecture is not None:
            input_["compatible_architecture"] = compatible_architecture
        if compatible_runtime is not None:
            input_["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_layer_version_permission(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        action: "capo_lambda.types.layer_permission_allowed_action.LayerPermissionAllowedAction",
        principal: "capo_lambda.types.layer_permission_allowed_principal.LayerPermissionAllowedPrincipal",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        organization_id: Optional[
            "capo_lambda.types.organization_id.OrganizationId"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> "capo_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse":
        r"""<p>Adds permissions to the resource-based policy of a version of an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a>. Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all accounts in an organization, or all Amazon Web Services accounts. </p> <p>To revoke permission, call <a>RemoveLayerVersionPermission</a> with the statement ID that you specified when you added it.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>
            statement_id: <p>An identifier that distinguishes the policy from others on the same layer version.</p>
            action: <p>The API action that grants access to the layer. For example, <code>lambda:GetLayerVersion</code>.</p>
            principal: <p>An account ID, or <code>*</code> to grant layer usage permission to all accounts in an organization, or all Amazon Web Services accounts (if <code>organizationId</code> is not specified). For the last case, make sure that you really do want all Amazon Web Services accounts to have usage permission to this layer. </p>
            organization_id: <p>With the principal set to <code>*</code>, grant permission to all accounts in the specified organization.</p>
            revision_id: <p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.policy_length_exceeded_exception.PolicyLengthExceededException: <p>The permissions policy for the resource is too large. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add permissions to a layer version
            The following example grants permission for the account 223456789012 to use version 1 of a layer named my-layer.

            >>> client.add_layer_version_permission(action='lambda:GetLayerVersion', layer_name='my-layer', principal='223456789012', statement_id='xaccount', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.add_layer_version_permission_response.AddLayerVersionPermissionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.add_layer_version_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.add_layer_version_permission.add_layer_version_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.add_layer_version_permission_request.AddLayerVersionPermissionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
            "statement_id": statement_id,
            "action": action,
            "principal": principal,
        }
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Deletes a version of an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a>. Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to it.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a version of a Lambda layer
            The following example deletes version 2 of a layer named my-layer.

            >>> client.delete_layer_version(layer_name='my-layer', version_number=2)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_layer_version_request.DeleteLayerVersionRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_layer_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_layer_version.delete_layer_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_layer_version_request.DeleteLayerVersionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse":
        r"""<p>Returns information about a version of an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a>, with a link to download the layer archive that's valid for 10 minutes.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a Lambda layer version
            The following example returns information for version 1 of a layer named my-layer.

            >>> client.get_layer_version(layer_name='my-layer', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_layer_version_request.GetLayerVersionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_layer_version.get_layer_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_request.GetLayerVersionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_layer_version_by_arn(
        self,
        arn: "capo_lambda.types.layer_version_arn.LayerVersionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse":
        r"""<p>Returns information about a version of an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a>, with a link to download the layer archive that's valid for 10 minutes.</p>

        Args:
            arn: <p>The ARN of the layer version.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a Lambda layer version
            The following example returns information about the layer version with the specified Amazon Resource Name (ARN).

            >>> client.get_layer_version_by_arn(arn='arn:aws:lambda:ca-central-1:123456789012:layer:blank-python-lib:3')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_layer_version_by_arn_request.GetLayerVersionByArnRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_layer_version_response.GetLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version_by_arn

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_layer_version_by_arn.get_layer_version_by_arn(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_by_arn_request.GetLayerVersionByArnRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_layer_version_policy(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_layer_version_policy_response.GetLayerVersionPolicyResponse":
        r"""<p>Returns the permission policy for a version of an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a>. For more information, see <a>AddLayerVersionPermission</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_layer_version_policy_request.GetLayerVersionPolicyRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_layer_version_policy_response.GetLayerVersionPolicyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_layer_version_policy

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_layer_version_policy.get_layer_version_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_layer_version_policy_request.GetLayerVersionPolicyRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_layer_version(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        content: "capo_lambda.types.layer_version_content_input.LayerVersionContentInput",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        compatible_architectures: Optional[
            "capo_lambda.types.compatible_architectures.CompatibleArchitectures"
        ] = None,
        compatible_runtimes: Optional[
            "capo_lambda.types.compatible_runtimes.CompatibleRuntimes"
        ] = None,
        license_info: Optional["capo_lambda.types.license_info.LicenseInfo"] = None,
    ) -> "capo_lambda.types.publish_layer_version_response.PublishLayerVersionResponse":
        r"""<p>Creates an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a> from a ZIP archive. Each time you call <code>PublishLayerVersion</code> with the same layer name, a new version is created.</p> <p>Add layers to your function with <a>CreateFunction</a> or <a>UpdateFunctionConfiguration</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            description: <p>The description of the version.</p>
            content: <p>The function layer archive.</p>
            compatible_architectures: <p>A list of compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html\">instruction set architectures</a>.</p>
            compatible_runtimes: <p>A list of compatible <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\">function runtimes</a>. Used for filtering with <a>ListLayers</a> and <a>ListLayerVersions</a>.</p> <p>The following list includes deprecated runtimes. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy\">Runtime deprecation policy</a>.</p>
            license_info: <p>The layer's software license. It can be any of the following:</p> <ul> <li> <p>An <a href=\"https://spdx.org/licenses/\">SPDX license identifier</a>. For example, <code>MIT</code>.</p> </li> <li> <p>The URL of a license hosted on the internet. For example, <code>https://opensource.org/licenses/MIT</code>.</p> </li> <li> <p>The full text of the license.</p> </li> </ul>

        Raises:
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a Lambda layer version
            The following example creates a new Python library layer version. The command retrieves the layer content a file named layer.zip in the specified S3 bucket.

            >>> client.publish_layer_version(compatible_runtimes=['python3.6', 'python3.7'], content={'S3Bucket': 'lambda-layers-us-west-2-123456789012', 'S3Key': 'layer.zip'}, description='My Python layer', layer_name='my-layer', license_info='MIT')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.publish_layer_version_request.PublishLayerVersionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.publish_layer_version_response.PublishLayerVersionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.publish_layer_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.publish_layer_version.publish_layer_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.publish_layer_version_request.PublishLayerVersionRequest = {
            "layer_name": layer_name,
            "content": content,
        }
        if description is not None:
            input_["description"] = description
        if compatible_architectures is not None:
            input_["compatible_architectures"] = compatible_architectures
        if compatible_runtimes is not None:
            input_["compatible_runtimes"] = compatible_runtimes
        if license_info is not None:
            input_["license_info"] = license_info

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_layer_version_permission(
        self,
        layer_name: "capo_lambda.types.layer_name.LayerName",
        version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> None:
        r"""<p>Removes a statement from the permissions policy for a version of an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">Lambda layer</a>. For more information, see <a>AddLayerVersionPermission</a>.</p>

        Args:
            layer_name: <p>The name or Amazon Resource Name (ARN) of the layer.</p>
            version_number: <p>The version number.</p>
            statement_id: <p>The identifier that was specified when the statement was added.</p>
            revision_id: <p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete layer-version permissions
            The following example deletes permission for an account to configure a layer version.

            >>> client.remove_layer_version_permission(layer_name='my-layer', statement_id='xaccount', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.remove_layer_version_permission_request.RemoveLayerVersionPermissionRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.remove_layer_version_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.remove_layer_version_permission.remove_layer_version_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.remove_layer_version_permission_request.RemoveLayerVersionPermissionRequest = {
            "layer_name": layer_name,
            "version_number": version_number,
            "statement_id": statement_id,
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_permission(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        statement_id: "capo_lambda.types.statement_id.StatementId",
        action: "capo_lambda.types.action.Action",
        principal: "capo_lambda.types.principal.Principal",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        source_arn: Optional["capo_lambda.types.arn.Arn"] = None,
        function_url_auth_type: Optional[
            "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
        ] = None,
        invoked_via_function_url: Optional[
            "capo_lambda.types.invoked_via_function_url.InvokedViaFunctionUrl"
        ] = None,
        source_account: Optional["capo_lambda.types.source_owner.SourceOwner"] = None,
        event_source_token: Optional[
            "capo_lambda.types.event_source_token.EventSourceToken"
        ] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        principal_org_id: Optional[
            "capo_lambda.types.principal_org_id.PrincipalOrgID"
        ] = None,
    ) -> "capo_lambda.types.add_permission_response.AddPermissionResponse":
        r"""<p>Grants a <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\">principal</a> permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function. Note: Lambda does not support adding policies to version $LATEST.</p> <p>To grant permission to another account, specify the account ID as the <code>Principal</code>. To grant permission to an organization defined in Organizations, specify the organization ID as the <code>PrincipalOrgID</code>. For Amazon Web Services services, the principal is a domain-style identifier that the service defines, such as <code>s3.amazonaws.com</code> or <code>sns.amazonaws.com</code>. For Amazon Web Services services, you can also specify the ARN of the associated resource as the <code>SourceArn</code>. If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.</p> <p>This operation adds a statement to a resource-based permissions policy for the function. For more information about function policies, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html\">Using resource-based policies for Lambda</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            statement_id: <p>A statement identifier that differentiates the statement from others in the same policy.</p>
            action: <p>The action that the principal can use on the function. For example, <code>lambda:InvokeFunction</code> or <code>lambda:GetFunction</code>.</p>
            principal: <p>The Amazon Web Services service, Amazon Web Services account, IAM user, or IAM role that invokes the function. If you specify a service, use <code>SourceArn</code> or <code>SourceAccount</code> to limit who can invoke the function through that service.</p>
            source_arn: <p>For Amazon Web Services services, the ARN of the Amazon Web Services resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.</p> <p>Note that Lambda configures the comparison using the <code>StringLike</code> operator.</p>
            function_url_auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>
            invoked_via_function_url: <p>Indicates whether the permission applies when the function is invoked through a function URL. </p>
            source_account: <p>For Amazon Web Services service, the ID of the Amazon Web Services account that owns the resource. Use this together with <code>SourceArn</code> to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.</p>
            event_source_token: <p>For Alexa Smart Home functions, a token that the invoker must supply.</p>
            qualifier: <p>Specify a version or alias to add permissions to a published version of the function.</p>
            revision_id: <p>Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>
            principal_org_id: <p>The identifier for your organization in Organizations. Use this to grant permissions to all the Amazon Web Services accounts under this organization.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.policy_length_exceeded_exception.PolicyLengthExceededException: <p>The permissions policy for the resource is too large. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.public_policy_exception.PublicPolicyException: <p>The resource-based policy you tried to add to the Lambda function would grant public access to it, and your account's <code>BlockPublicAccess</code> setting prevents public access. For more information about blocking public access to Lambda functions, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#access-control-block-public-access\">Block public access to Lambda resources</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To grant Amazon S3 permission to invoke a function
            The following example adds permission for Amazon S3 to invoke a Lambda function named my-function for notifications from a bucket named my-bucket-1xpuxmplzrlbh in account 123456789012.

            >>> client.add_permission(action='lambda:InvokeFunction', function_name='my-function', principal='s3.amazonaws.com', source_account='123456789012', source_arn='arn:aws:s3:::my-bucket-1xpuxmplzrlbh/*', statement_id='s3')
            To grant another account permission to invoke a function
            The following example adds permission for account 223456789012 invoke a Lambda function named my-function.

            >>> client.add_permission(action='lambda:InvokeFunction', function_name='my-function', principal='223456789012', statement_id='xaccount')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.add_permission_request.AddPermissionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.add_permission_response.AddPermissionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.add_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.add_permission.add_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.add_permission_request.AddPermissionRequest = {
            "function_name": function_name,
            "statement_id": statement_id,
            "action": action,
            "principal": principal,
        }
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if function_url_auth_type is not None:
            input_["function_url_auth_type"] = function_url_auth_type
        if invoked_via_function_url is not None:
            input_["invoked_via_function_url"] = invoked_via_function_url
        if source_account is not None:
            input_["source_account"] = source_account
        if event_source_token is not None:
            input_["event_source_token"] = event_source_token
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if principal_org_id is not None:
            input_["principal_org_id"] = principal_org_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_permission(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        statement_id: "capo_lambda.types.namespaced_statement_id.NamespacedStatementId",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> None:
        r"""<p>Revokes function-use permission from an Amazon Web Services service or another Amazon Web Services account. You can get the ID of the statement from the output of <a>GetPolicy</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            statement_id: <p>Statement ID of the permission to remove.</p>
            qualifier: <p>Specify a version or alias to remove permissions from a published version of the function.</p>
            revision_id: <p>Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.public_policy_exception.PublicPolicyException: <p>The resource-based policy you tried to add to the Lambda function would grant public access to it, and your account's <code>BlockPublicAccess</code> setting prevents public access. For more information about blocking public access to Lambda functions, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#access-control-block-public-access\">Block public access to Lambda resources</a>.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a Lambda function's permissions
            The following example removes a permissions statement named xaccount from the PROD alias of a function named my-function.

            >>> client.remove_permission(function_name='my-function', qualifier='PROD', statement_id='xaccount')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.remove_permission_request.RemovePermissionRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.remove_permission

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.remove_permission.remove_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.remove_permission_request.RemovePermissionRequest = {
            "function_name": function_name,
            "statement_id": statement_id,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_provisioned_concurrency_config(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        provisioned_concurrent_executions: "capo_lambda.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_provisioned_concurrency_config_response.PutProvisionedConcurrencyConfigResponse":
        r"""<p>Adds a provisioned concurrency configuration to a function's alias or version.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>
            provisioned_concurrent_executions: <p>The amount of provisioned concurrency to allocate for the version or alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To allocate provisioned concurrency
            The following example allocates 100 provisioned concurrency for the BLUE alias of the specified function.

            >>> client.put_provisioned_concurrency_config(function_name='my-function', provisioned_concurrent_executions=100, qualifier='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_provisioned_concurrency_config_request.PutProvisionedConcurrencyConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_provisioned_concurrency_config_response.PutProvisionedConcurrencyConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_provisioned_concurrency_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_provisioned_concurrency_config.put_provisioned_concurrency_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.put_provisioned_concurrency_config_request.PutProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
            "provisioned_concurrent_executions": provisioned_concurrent_executions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_provisioned_concurrency_config(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_provisioned_concurrency_config_response.GetProvisionedConcurrencyConfigResponse":
        r"""<p>Retrieves the provisioned concurrency configuration for a function's alias or version.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.provisioned_concurrency_config_not_found_exception.ProvisionedConcurrencyConfigNotFoundException: <p>The specified configuration does not exist.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a provisioned concurrency configuration
            The following example returns details for the provisioned concurrency configuration for the BLUE alias of the specified function.

            >>> client.get_provisioned_concurrency_config(function_name='my-function', qualifier='BLUE')
            To view a provisioned concurrency configuration
            The following example displays details for the provisioned concurrency configuration for the BLUE alias of the specified function.

            >>> client.get_provisioned_concurrency_config(function_name='my-function', qualifier='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_provisioned_concurrency_config_request.GetProvisionedConcurrencyConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_provisioned_concurrency_config_response.GetProvisionedConcurrencyConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_provisioned_concurrency_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_provisioned_concurrency_config.get_provisioned_concurrency_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.get_provisioned_concurrency_config_request.GetProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_provisioned_concurrency_config(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Deletes the provisioned concurrency configuration for a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a provisioned concurrency configuration
            The following example deletes the provisioned concurrency configuration for the GREEN alias of a function named my-function.

            >>> client.delete_provisioned_concurrency_config(function_name='my-function', qualifier='GREEN')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_provisioned_concurrency_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_provisioned_concurrency_config.delete_provisioned_concurrency_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

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

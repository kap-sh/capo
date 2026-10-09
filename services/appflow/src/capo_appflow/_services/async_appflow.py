"""Generated from Smithy shape ``com.amazonaws.appflow#SandstoneConfigurationServiceLambda``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_appflow._auth._signers
import capo_appflow._auth._sigv4
from capo_appflow._auth._identity import Credentials
from capo_appflow._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_appflow._auth._zapros_handler import AuthMiddleware
from capo_appflow._pagination import resolve_path as _resolve_path
from capo_appflow._services._aws_config import aaws_config
from capo_appflow._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_appflow.types.api_version
    import capo_appflow.types.arn
    import capo_appflow.types.boolean
    import capo_appflow.types.cancel_flow_executions_request
    import capo_appflow.types.cancel_flow_executions_response
    import capo_appflow.types.client_token
    import capo_appflow.types.connection_mode
    import capo_appflow.types.connector_label
    import capo_appflow.types.connector_profile_config
    import capo_appflow.types.connector_profile_name
    import capo_appflow.types.connector_profile_name_list
    import capo_appflow.types.connector_provisioning_config
    import capo_appflow.types.connector_provisioning_type
    import capo_appflow.types.connector_type
    import capo_appflow.types.connector_type_list
    import capo_appflow.types.create_connector_profile_request
    import capo_appflow.types.create_connector_profile_response
    import capo_appflow.types.create_flow_request
    import capo_appflow.types.create_flow_response
    import capo_appflow.types.delete_connector_profile_request
    import capo_appflow.types.delete_connector_profile_response
    import capo_appflow.types.delete_flow_request
    import capo_appflow.types.delete_flow_response
    import capo_appflow.types.describe_connector_entity_request
    import capo_appflow.types.describe_connector_entity_response
    import capo_appflow.types.describe_connector_profiles_request
    import capo_appflow.types.describe_connector_profiles_response
    import capo_appflow.types.describe_connector_request
    import capo_appflow.types.describe_connector_response
    import capo_appflow.types.describe_connectors_request
    import capo_appflow.types.describe_connectors_response
    import capo_appflow.types.describe_flow_execution_records_request
    import capo_appflow.types.describe_flow_execution_records_response
    import capo_appflow.types.describe_flow_request
    import capo_appflow.types.describe_flow_response
    import capo_appflow.types.description
    import capo_appflow.types.destination_flow_config_list
    import capo_appflow.types.entities_path
    import capo_appflow.types.entity_name
    import capo_appflow.types.execution_ids
    import capo_appflow.types.flow_description
    import capo_appflow.types.flow_name
    import capo_appflow.types.kms_arn
    import capo_appflow.types.list_connector_entities_request
    import capo_appflow.types.list_connector_entities_response
    import capo_appflow.types.list_connectors_request
    import capo_appflow.types.list_connectors_response
    import capo_appflow.types.list_entities_max_results
    import capo_appflow.types.list_flows_request
    import capo_appflow.types.list_flows_response
    import capo_appflow.types.list_tags_for_resource_request
    import capo_appflow.types.list_tags_for_resource_response
    import capo_appflow.types.max_results
    import capo_appflow.types.metadata_catalog_config
    import capo_appflow.types.next_token
    import capo_appflow.types.register_connector_request
    import capo_appflow.types.register_connector_response
    import capo_appflow.types.reset_connector_metadata_cache_request
    import capo_appflow.types.reset_connector_metadata_cache_response
    import capo_appflow.types.source_flow_config
    import capo_appflow.types.start_flow_request
    import capo_appflow.types.start_flow_response
    import capo_appflow.types.stop_flow_request
    import capo_appflow.types.stop_flow_response
    import capo_appflow.types.tag_key_list
    import capo_appflow.types.tag_map
    import capo_appflow.types.tag_resource_request
    import capo_appflow.types.tag_resource_response
    import capo_appflow.types.tasks
    import capo_appflow.types.trigger_config
    import capo_appflow.types.unregister_connector_request
    import capo_appflow.types.unregister_connector_response
    import capo_appflow.types.untag_resource_request
    import capo_appflow.types.untag_resource_response
    import capo_appflow.types.update_connector_profile_request
    import capo_appflow.types.update_connector_profile_response
    import capo_appflow.types.update_connector_registration_request
    import capo_appflow.types.update_connector_registration_response
    import capo_appflow.types.update_flow_request
    import capo_appflow.types.update_flow_response


class AsyncAppflowClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncAppflowClient:
    """A client for the ``Appflow`` service.

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
        self._config = AsyncAppflowClientConfig(
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
        self, config_overrides: Optional[AsyncAppflowClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAppflowClientConfig = config_overrides or {}
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

    async def cancel_flow_executions(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        execution_ids: Optional["capo_appflow.types.execution_ids.ExecutionIds"] = None,
    ) -> "capo_appflow.types.cancel_flow_executions_response.CancelFlowExecutionsResponse":
        """<p>Cancels active runs for a flow.</p> <p>You can cancel all of the active runs for a flow, or you can cancel specific runs by providing their IDs.</p> <p>You can cancel a flow run only when the run is in progress. You can't cancel a run that has already completed or failed. You also can't cancel a run that's scheduled to occur but hasn't started yet. To prevent a scheduled run, you can deactivate the flow with the <code>StopFlow</code> action.</p> <p>You cannot resume a run after you cancel it.</p> <p>When you send your request, the status for each run becomes <code>CancelStarted</code>. When the cancellation completes, the status becomes <code>Canceled</code>.</p> <note> <p>When you cancel a run, you still incur charges for any data that the run already processed before the cancellation. If the run had already written some data to the flow destination, then that data remains in the destination. If you configured the flow to use a batch API (such as the Salesforce Bulk API 2.0), then the run will finish reading or writing its entire batch of data after the cancellation. For these operations, the data processing charges for Amazon AppFlow apply. For the pricing information, see <a href="http://aws.amazon.com/appflow/pricing/">Amazon AppFlow pricing</a>.</p> </note>

        Args:
            flow_name: <p>The name of a flow with active runs that you want to cancel.</p>
            execution_ids: <p>The ID of each active run to cancel. These runs must belong to the flow you specify in your request.</p> <p>If you omit this parameter, your request ends all active runs that belong to the flow.</p>

        Raises:
            capo_appflow.errors.access_denied_exception.AccessDeniedException: <p>AppFlow/Requester has invalid or missing permissions.</p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.throttling_exception.ThrottlingException: <p>API calls have exceeded the maximum allowed API request rate per account and per Region. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.cancel_flow_executions_request.CancelFlowExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.cancel_flow_executions_response.CancelFlowExecutionsResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.cancel_flow_executions

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.cancel_flow_executions.async_cancel_flow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.cancel_flow_executions_request.CancelFlowExecutionsRequest = {
            "flow_name": flow_name
        }
        if execution_ids is not None:
            input_["execution_ids"] = execution_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_connector_profile(
        self,
        connector_profile_name: "capo_appflow.types.connector_profile_name.ConnectorProfileName",
        connector_type: "capo_appflow.types.connector_type.ConnectorType",
        connection_mode: "capo_appflow.types.connection_mode.ConnectionMode",
        connector_profile_config: "capo_appflow.types.connector_profile_config.ConnectorProfileConfig",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        kms_arn: Optional["capo_appflow.types.kms_arn.KMSArn"] = None,
        connector_label: Optional[
            "capo_appflow.types.connector_label.ConnectorLabel"
        ] = None,
        client_token: Optional["capo_appflow.types.client_token.ClientToken"] = None,
    ) -> "capo_appflow.types.create_connector_profile_response.CreateConnectorProfileResponse":
        """<p> Creates a new connector profile associated with your Amazon Web Services account. There is a soft quota of 100 connector profiles per Amazon Web Services account. If you need more connector profiles than this quota allows, you can submit a request to the Amazon AppFlow team through the Amazon AppFlow support channel. In each connector profile that you create, you can provide the credentials and properties for only one connector.</p>

        Args:
            connector_profile_name: <p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in your Amazon Web Services account. </p>
            kms_arn: <p> The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key. </p>
            connector_type: <p> The type of connector, such as Salesforce, Amplitude, and so on. </p>
            connector_label: <p>The label of the connector. The label is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.</p>
            connection_mode: <p> Indicates the connection mode and specifies whether it is public or private. Private flows use Amazon Web Services PrivateLink to route data over Amazon Web Services infrastructure without exposing it to the public internet. </p>
            connector_profile_config: <p> Defines the connector-specific configuration and credentials. </p>
            client_token: <p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>CreateConnectorProfile</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>CreateConnectorProfile</code>. The token is active for 8 hours.</p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause a service quota (such as the number of flows) to be exceeded. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.create_connector_profile_request.CreateConnectorProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.create_connector_profile_response.CreateConnectorProfileResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.create_connector_profile

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.create_connector_profile.async_create_connector_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.create_connector_profile_request.CreateConnectorProfileRequest = {
            "connector_profile_name": connector_profile_name,
            "connector_type": connector_type,
            "connection_mode": connection_mode,
            "connector_profile_config": connector_profile_config,
        }
        if kms_arn is not None:
            input_["kms_arn"] = kms_arn
        if connector_label is not None:
            input_["connector_label"] = connector_label
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_flow(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        trigger_config: "capo_appflow.types.trigger_config.TriggerConfig",
        source_flow_config: "capo_appflow.types.source_flow_config.SourceFlowConfig",
        destination_flow_config_list: "capo_appflow.types.destination_flow_config_list.DestinationFlowConfigList",
        tasks: "capo_appflow.types.tasks.Tasks",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        description: Optional[
            "capo_appflow.types.flow_description.FlowDescription"
        ] = None,
        kms_arn: Optional["capo_appflow.types.kms_arn.KMSArn"] = None,
        tags: Optional["capo_appflow.types.tag_map.TagMap"] = None,
        metadata_catalog_config: Optional[
            "capo_appflow.types.metadata_catalog_config.MetadataCatalogConfig"
        ] = None,
        client_token: Optional["capo_appflow.types.client_token.ClientToken"] = None,
    ) -> "capo_appflow.types.create_flow_response.CreateFlowResponse":
        """<p> Enables your application to create a new flow using Amazon AppFlow. You must create a connector profile before calling this API. Please note that the Request Syntax below shows syntax for multiple destinations, however, you can only transfer data to one item in this list at a time. Amazon AppFlow does not currently support flows to multiple destinations at once. </p>

        Args:
            flow_name: <p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>
            description: <p> A description of the flow you want to create. </p>
            kms_arn: <p> The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key. </p>
            trigger_config: <p> The trigger settings that determine how and when the flow runs. </p>
            source_flow_config: <p> The configuration that controls how Amazon AppFlow retrieves data from the source connector. </p>
            destination_flow_config_list: <p> The configuration that controls how Amazon AppFlow places data in the destination connector. </p>
            tasks: <p> A list of tasks that Amazon AppFlow performs while transferring the data in the flow run. </p>
            tags: <p> The tags used to organize, track, or control access for your flow. </p>
            metadata_catalog_config: <p>Specifies the configuration that Amazon AppFlow uses when it catalogs the data that's transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.</p>
            client_token: <p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>CreateFlow</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>CreateFlow</code>. The token is active for 8 hours.</p>

        Raises:
            capo_appflow.errors.access_denied_exception.AccessDeniedException: <p>AppFlow/Requester has invalid or missing permissions.</p>
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.connector_server_exception.ConnectorServerException: <p> An error occurred when retrieving data from the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause a service quota (such as the number of flows) to be exceeded. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.create_flow_request.CreateFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.create_flow_response.CreateFlowResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.create_flow

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.create_flow.async_create_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.create_flow_request.CreateFlowRequest = {
            "flow_name": flow_name,
            "trigger_config": trigger_config,
            "source_flow_config": source_flow_config,
            "destination_flow_config_list": destination_flow_config_list,
            "tasks": tasks,
        }
        if description is not None:
            input_["description"] = description
        if kms_arn is not None:
            input_["kms_arn"] = kms_arn
        if tags is not None:
            input_["tags"] = tags
        if metadata_catalog_config is not None:
            input_["metadata_catalog_config"] = metadata_catalog_config
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector_profile(
        self,
        connector_profile_name: "capo_appflow.types.connector_profile_name.ConnectorProfileName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        force_delete: Optional["capo_appflow.types.boolean.Boolean"] = None,
    ) -> "capo_appflow.types.delete_connector_profile_response.DeleteConnectorProfileResponse":
        """<p> Enables you to delete an existing connector profile. </p>

        Args:
            connector_profile_name: <p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in your account. </p>
            force_delete: <p> Indicates whether Amazon AppFlow should delete the profile, even if it is currently in use in one or more flows. </p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.delete_connector_profile_request.DeleteConnectorProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.delete_connector_profile_response.DeleteConnectorProfileResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.delete_connector_profile

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.delete_connector_profile.async_delete_connector_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.delete_connector_profile_request.DeleteConnectorProfileRequest = {
            "connector_profile_name": connector_profile_name
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_flow(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        force_delete: Optional["capo_appflow.types.boolean.Boolean"] = None,
    ) -> "capo_appflow.types.delete_flow_response.DeleteFlowResponse":
        """<p> Enables your application to delete an existing flow. Before deleting the flow, Amazon AppFlow validates the request by checking the flow configuration and status. You can delete flows one at a time. </p>

        Args:
            flow_name: <p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>
            force_delete: <p> Indicates whether Amazon AppFlow should delete the flow, even if it is currently in use. </p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.delete_flow_request.DeleteFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.delete_flow_response.DeleteFlowResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.delete_flow

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.delete_flow.async_delete_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.delete_flow_request.DeleteFlowRequest = {
            "flow_name": flow_name
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connector(
        self,
        connector_type: "capo_appflow.types.connector_type.ConnectorType",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_label: Optional[
            "capo_appflow.types.connector_label.ConnectorLabel"
        ] = None,
    ) -> "capo_appflow.types.describe_connector_response.DescribeConnectorResponse":
        """<p>Describes the given custom connector registered in your Amazon Web Services account. This API can be used for custom connectors that are registered in your account and also for Amazon authored connectors.</p>

        Args:
            connector_type: <p>The connector type, such as CUSTOMCONNECTOR, Saleforce, Marketo. Please choose CUSTOMCONNECTOR for Lambda based custom connectors.</p>
            connector_label: <p>The label of the connector. The label is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.</p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.describe_connector_request.DescribeConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.describe_connector_response.DescribeConnectorResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.describe_connector

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.describe_connector.async_describe_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.describe_connector_request.DescribeConnectorRequest = {
            "connector_type": connector_type
        }
        if connector_label is not None:
            input_["connector_label"] = connector_label

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connector_entity(
        self,
        connector_entity_name: "capo_appflow.types.entity_name.EntityName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_type: Optional[
            "capo_appflow.types.connector_type.ConnectorType"
        ] = None,
        connector_profile_name: Optional[
            "capo_appflow.types.connector_profile_name.ConnectorProfileName"
        ] = None,
        api_version: Optional["capo_appflow.types.api_version.ApiVersion"] = None,
    ) -> "capo_appflow.types.describe_connector_entity_response.DescribeConnectorEntityResponse":
        """<p> Provides details regarding the entity used with the connector, with a description of the data model for each field in that entity. </p>

        Args:
            connector_entity_name: <p> The entity name for that connector. </p>
            connector_type: <p> The type of connector application, such as Salesforce, Amplitude, and so on. </p>
            connector_profile_name: <p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. </p>
            api_version: <p>The version of the API that's used by the connector.</p>

        Raises:
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.connector_server_exception.ConnectorServerException: <p> An error occurred when retrieving data from the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.describe_connector_entity_request.DescribeConnectorEntityRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.describe_connector_entity_response.DescribeConnectorEntityResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.describe_connector_entity

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.describe_connector_entity.async_describe_connector_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.describe_connector_entity_request.DescribeConnectorEntityRequest = {
            "connector_entity_name": connector_entity_name
        }
        if connector_type is not None:
            input_["connector_type"] = connector_type
        if connector_profile_name is not None:
            input_["connector_profile_name"] = connector_profile_name
        if api_version is not None:
            input_["api_version"] = api_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connector_profiles(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_profile_names: Optional[
            "capo_appflow.types.connector_profile_name_list.ConnectorProfileNameList"
        ] = None,
        connector_type: Optional[
            "capo_appflow.types.connector_type.ConnectorType"
        ] = None,
        connector_label: Optional[
            "capo_appflow.types.connector_label.ConnectorLabel"
        ] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "capo_appflow.types.describe_connector_profiles_response.DescribeConnectorProfilesResponse":
        """<p> Returns a list of <code>connector-profile</code> details matching the provided <code>connector-profile</code> names and <code>connector-types</code>. Both input lists are optional, and you can use them to filter the result. </p> <p>If no names or <code>connector-types</code> are provided, returns all connector profiles in a paginated form. If there is no match, this operation returns an empty list.</p>

        Args:
            connector_profile_names: <p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. </p>
            connector_type: <p> The type of connector, such as Salesforce, Amplitude, and so on. </p>
            connector_label: <p>The name of the connector. The name is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.</p>
            max_results: <p> Specifies the maximum number of items that should be returned in the result set. The default for <code>maxResults</code> is 20 (for all paginated API operations). </p>
            next_token: <p> The pagination token for the next page of data. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.describe_connector_profiles_request.DescribeConnectorProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.describe_connector_profiles_response.DescribeConnectorProfilesResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.describe_connector_profiles

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.describe_connector_profiles.async_describe_connector_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.describe_connector_profiles_request.DescribeConnectorProfilesRequest = {}
        if connector_profile_names is not None:
            input_["connector_profile_names"] = connector_profile_names
        if connector_type is not None:
            input_["connector_type"] = connector_type
        if connector_label is not None:
            input_["connector_label"] = connector_label
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

    async def iter_describe_connector_profiles(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_profile_names: Optional[
            "capo_appflow.types.connector_profile_name_list.ConnectorProfileNameList"
        ] = None,
        connector_type: Optional[
            "capo_appflow.types.connector_type.ConnectorType"
        ] = None,
        connector_label: Optional[
            "capo_appflow.types.connector_label.ConnectorLabel"
        ] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_appflow.types.describe_connector_profiles_response.DescribeConnectorProfilesResponse]":
        _token = next_token
        while True:
            _response = await self.describe_connector_profiles(
                config_overrides=config_overrides,
                connector_profile_names=connector_profile_names,
                connector_type=connector_type,
                connector_label=connector_label,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_connectors(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_types: Optional[
            "capo_appflow.types.connector_type_list.ConnectorTypeList"
        ] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "capo_appflow.types.describe_connectors_response.DescribeConnectorsResponse":
        """<p> Describes the connectors vended by Amazon AppFlow for specified connector types. If you don't specify a connector type, this operation describes all connectors vended by Amazon AppFlow. If there are more connectors than can be returned in one page, the response contains a <code>nextToken</code> object, which can be be passed in to the next call to the <code>DescribeConnectors</code> API operation to retrieve the next page. </p>

        Args:
            connector_types: <p> The type of connector, such as Salesforce, Amplitude, and so on. </p>
            max_results: <p>The maximum number of items that should be returned in the result set. The default is 20.</p>
            next_token: <p> The pagination token for the next page of data. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.describe_connectors_request.DescribeConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.describe_connectors_response.DescribeConnectorsResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.describe_connectors

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.describe_connectors.async_describe_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.describe_connectors_request.DescribeConnectorsRequest = {}
        if connector_types is not None:
            input_["connector_types"] = connector_types
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

    async def iter_describe_connectors(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_types: Optional[
            "capo_appflow.types.connector_type_list.ConnectorTypeList"
        ] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_appflow.types.describe_connectors_response.DescribeConnectorsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_connectors(
                config_overrides=config_overrides,
                connector_types=connector_types,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_flow(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
    ) -> "capo_appflow.types.describe_flow_response.DescribeFlowResponse":
        """<p> Provides a description of the specified flow. </p>

        Args:
            flow_name: <p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.describe_flow_request.DescribeFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.describe_flow_response.DescribeFlowResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.describe_flow

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.describe_flow.async_describe_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.describe_flow_request.DescribeFlowRequest = {
            "flow_name": flow_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_flow_execution_records(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "capo_appflow.types.describe_flow_execution_records_response.DescribeFlowExecutionRecordsResponse":
        """<p> Fetches the execution history of the flow. </p>

        Args:
            flow_name: <p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>
            max_results: <p> Specifies the maximum number of items that should be returned in the result set. The default for <code>maxResults</code> is 20 (for all paginated API operations). </p>
            next_token: <p> The pagination token for the next page of data. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.describe_flow_execution_records_request.DescribeFlowExecutionRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.describe_flow_execution_records_response.DescribeFlowExecutionRecordsResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.describe_flow_execution_records

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.describe_flow_execution_records.async_describe_flow_execution_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.describe_flow_execution_records_request.DescribeFlowExecutionRecordsRequest = {
            "flow_name": flow_name
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

    async def iter_describe_flow_execution_records(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_appflow.types.describe_flow_execution_records_response.DescribeFlowExecutionRecordsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_flow_execution_records(
                flow_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_connector_entities(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_profile_name: Optional[
            "capo_appflow.types.connector_profile_name.ConnectorProfileName"
        ] = None,
        connector_type: Optional[
            "capo_appflow.types.connector_type.ConnectorType"
        ] = None,
        entities_path: Optional["capo_appflow.types.entities_path.EntitiesPath"] = None,
        api_version: Optional["capo_appflow.types.api_version.ApiVersion"] = None,
        max_results: Optional[
            "capo_appflow.types.list_entities_max_results.ListEntitiesMaxResults"
        ] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "capo_appflow.types.list_connector_entities_response.ListConnectorEntitiesResponse":
        """<p> Returns the list of available connector entities supported by Amazon AppFlow. For example, you can query Salesforce for <i>Account</i> and <i>Opportunity</i> entities, or query ServiceNow for the <i>Incident</i> entity. </p>

        Args:
            connector_profile_name: <p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account, and is used to query the downstream connector. </p>
            connector_type: <p> The type of connector, such as Salesforce, Amplitude, and so on. </p>
            entities_path: <p> This optional parameter is specific to connector implementation. Some connectors support multiple levels or categories of entities. You can find out the list of roots for such providers by sending a request without the <code>entitiesPath</code> parameter. If the connector supports entities at different roots, this initial request returns the list of roots. Otherwise, this request returns all entities supported by the provider. </p>
            api_version: <p>The version of the API that's used by the connector.</p>
            max_results: <p>The maximum number of items that the operation returns in the response.</p>
            next_token: <p>A token that was provided by your prior <code>ListConnectorEntities</code> operation if the response was too big for the page size. You specify this token to get the next page of results in paginated response.</p>

        Raises:
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.connector_server_exception.ConnectorServerException: <p> An error occurred when retrieving data from the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.list_connector_entities_request.ListConnectorEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.list_connector_entities_response.ListConnectorEntitiesResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.list_connector_entities

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.list_connector_entities.async_list_connector_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.list_connector_entities_request.ListConnectorEntitiesRequest = {}
        if connector_profile_name is not None:
            input_["connector_profile_name"] = connector_profile_name
        if connector_type is not None:
            input_["connector_type"] = connector_type
        if entities_path is not None:
            input_["entities_path"] = entities_path
        if api_version is not None:
            input_["api_version"] = api_version
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

    async def list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "capo_appflow.types.list_connectors_response.ListConnectorsResponse":
        """<p>Returns the list of all registered custom connectors in your Amazon Web Services account. This API lists only custom connectors registered in this account, not the Amazon Web Services authored connectors. </p>

        Args:
            max_results: <p>Specifies the maximum number of items that should be returned in the result set. The default for <code>maxResults</code> is 20 (for all paginated API operations).</p>
            next_token: <p>The pagination token for the next page of data.</p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.list_connectors

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.list_connectors_request.ListConnectorsRequest = {}
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

    async def iter_list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_appflow.types.list_connectors_response.ListConnectorsResponse]":
        _token = next_token
        while True:
            _response = await self.list_connectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_flows(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "capo_appflow.types.list_flows_response.ListFlowsResponse":
        """<p> Lists all of the flows associated with your account. </p>

        Args:
            max_results: <p> Specifies the maximum number of items that should be returned in the result set. </p>
            next_token: <p> The pagination token for next page of data. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.list_flows_request.ListFlowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.list_flows_response.ListFlowsResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.list_flows

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.list_flows.async_list_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.list_flows_request.ListFlowsRequest = {}
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

    async def iter_list_flows(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        max_results: Optional["capo_appflow.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appflow.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_appflow.types.list_flows_response.ListFlowsResponse]":
        _token = next_token
        while True:
            _response = await self.list_flows(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_appflow.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
    ) -> (
        "capo_appflow.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p> Retrieves the tags that are associated with a specified flow. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the specified flow. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_connector(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_label: Optional[
            "capo_appflow.types.connector_label.ConnectorLabel"
        ] = None,
        description: Optional["capo_appflow.types.description.Description"] = None,
        connector_provisioning_type: Optional[
            "capo_appflow.types.connector_provisioning_type.ConnectorProvisioningType"
        ] = None,
        connector_provisioning_config: Optional[
            "capo_appflow.types.connector_provisioning_config.ConnectorProvisioningConfig"
        ] = None,
        client_token: Optional["capo_appflow.types.client_token.ClientToken"] = None,
    ) -> "capo_appflow.types.register_connector_response.RegisterConnectorResponse":
        """<p>Registers a new custom connector with your Amazon Web Services account. Before you can register the connector, you must deploy the associated AWS lambda function in your account.</p>

        Args:
            connector_label: <p> The name of the connector. The name is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account.</p>
            description: <p>A description about the connector that's being registered.</p>
            connector_provisioning_type: <p>The provisioning type of the connector. Currently the only supported value is LAMBDA. </p>
            connector_provisioning_config: <p>The provisioning type of the connector. Currently the only supported value is LAMBDA.</p>
            client_token: <p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>RegisterConnector</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>RegisterConnector</code>. The token is active for 8 hours.</p>

        Raises:
            capo_appflow.errors.access_denied_exception.AccessDeniedException: <p>AppFlow/Requester has invalid or missing permissions.</p>
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.connector_server_exception.ConnectorServerException: <p> An error occurred when retrieving data from the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause a service quota (such as the number of flows) to be exceeded. </p>
            capo_appflow.errors.throttling_exception.ThrottlingException: <p>API calls have exceeded the maximum allowed API request rate per account and per Region. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.register_connector_request.RegisterConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.register_connector_response.RegisterConnectorResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.register_connector

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.register_connector.async_register_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.register_connector_request.RegisterConnectorRequest = {}
        if connector_label is not None:
            input_["connector_label"] = connector_label
        if description is not None:
            input_["description"] = description
        if connector_provisioning_type is not None:
            input_["connector_provisioning_type"] = connector_provisioning_type
        if connector_provisioning_config is not None:
            input_["connector_provisioning_config"] = connector_provisioning_config
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_connector_metadata_cache(
        self,
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        connector_profile_name: Optional[
            "capo_appflow.types.connector_profile_name.ConnectorProfileName"
        ] = None,
        connector_type: Optional[
            "capo_appflow.types.connector_type.ConnectorType"
        ] = None,
        connector_entity_name: Optional[
            "capo_appflow.types.entity_name.EntityName"
        ] = None,
        entities_path: Optional["capo_appflow.types.entities_path.EntitiesPath"] = None,
        api_version: Optional["capo_appflow.types.api_version.ApiVersion"] = None,
    ) -> "capo_appflow.types.reset_connector_metadata_cache_response.ResetConnectorMetadataCacheResponse":
        """<p>Resets metadata about your connector entities that Amazon AppFlow stored in its cache. Use this action when you want Amazon AppFlow to return the latest information about the data that you have in a source application.</p> <p>Amazon AppFlow returns metadata about your entities when you use the ListConnectorEntities or DescribeConnectorEntities actions. Following these actions, Amazon AppFlow caches the metadata to reduce the number of API requests that it must send to the source application. Amazon AppFlow automatically resets the cache once every hour, but you can use this action when you want to get the latest metadata right away.</p>

        Args:
            connector_profile_name: <p>The name of the connector profile that you want to reset cached metadata for.</p> <p>You can omit this parameter if you're resetting the cache for any of the following connectors: Connect Customer, Amazon EventBridge, Amazon Lookout for Metrics, Amazon S3, or Upsolver. If you're resetting the cache for any other connector, you must include this parameter in your request.</p>
            connector_type: <p>The type of connector to reset cached metadata for.</p> <p>You must include this parameter in your request if you're resetting the cache for any of the following connectors: Connect Customer, Amazon EventBridge, Amazon Lookout for Metrics, Amazon S3, or Upsolver. If you're resetting the cache for any other connector, you can omit this parameter from your request. </p>
            connector_entity_name: <p>Use this parameter if you want to reset cached metadata about the details for an individual entity.</p> <p>If you don't include this parameter in your request, Amazon AppFlow only resets cached metadata about entity names, not entity details.</p>
            entities_path: <p>Use this parameter only if you’re resetting the cached metadata about a nested entity. Only some connectors support nested entities. A nested entity is one that has another entity as a parent. To use this parameter, specify the name of the parent entity.</p> <p>To look up the parent-child relationship of entities, you can send a ListConnectorEntities request that omits the entitiesPath parameter. Amazon AppFlow will return a list of top-level entities. For each one, it indicates whether the entity has nested entities. Then, in a subsequent ListConnectorEntities request, you can specify a parent entity name for the entitiesPath parameter. Amazon AppFlow will return a list of the child entities for that parent.</p>
            api_version: <p>The API version that you specified in the connector profile that you’re resetting cached metadata for. You must use this parameter only if the connector supports multiple API versions or if the connector type is CustomConnector.</p> <p>To look up how many versions a connector supports, use the DescribeConnectors action. In the response, find the value that Amazon AppFlow returns for the connectorVersion parameter.</p> <p>To look up the connector type, use the DescribeConnectorProfiles action. In the response, find the value that Amazon AppFlow returns for the connectorType parameter.</p> <p>To look up the API version that you specified in a connector profile, use the DescribeConnectorProfiles action.</p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.reset_connector_metadata_cache_request.ResetConnectorMetadataCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.reset_connector_metadata_cache_response.ResetConnectorMetadataCacheResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.reset_connector_metadata_cache

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.reset_connector_metadata_cache.async_reset_connector_metadata_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.reset_connector_metadata_cache_request.ResetConnectorMetadataCacheRequest = {}
        if connector_profile_name is not None:
            input_["connector_profile_name"] = connector_profile_name
        if connector_type is not None:
            input_["connector_type"] = connector_type
        if connector_entity_name is not None:
            input_["connector_entity_name"] = connector_entity_name
        if entities_path is not None:
            input_["entities_path"] = entities_path
        if api_version is not None:
            input_["api_version"] = api_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_flow(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        client_token: Optional["capo_appflow.types.client_token.ClientToken"] = None,
    ) -> "capo_appflow.types.start_flow_response.StartFlowResponse":
        """<p> Activates an existing flow. For on-demand flows, this operation runs the flow immediately. For schedule and event-triggered flows, this operation activates the flow. </p>

        Args:
            flow_name: <p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>
            client_token: <p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>StartFlow</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs for flows that run on a schedule or based on an event. However, the error doesn't occur for flows that run on demand. You set the conditions that initiate your flow for the <code>triggerConfig</code> parameter.</p> <p>If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>StartFlow</code>. The token is active for 8 hours.</p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause a service quota (such as the number of flows) to be exceeded. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.start_flow_request.StartFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.start_flow_response.StartFlowResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.start_flow

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.start_flow.async_start_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.start_flow_request.StartFlowRequest = {
            "flow_name": flow_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_flow(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
    ) -> "capo_appflow.types.stop_flow_response.StopFlowResponse":
        """<p> Deactivates the existing flow. For on-demand flows, this operation returns an <code>unsupportedOperationException</code> error message. For schedule and event-triggered flows, this operation deactivates the flow. </p>

        Args:
            flow_name: <p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.unsupported_operation_exception.UnsupportedOperationException: <p> The requested operation is not supported for the current flow. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.stop_flow_request.StopFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.stop_flow_response.StopFlowResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.stop_flow

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.stop_flow.async_stop_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.stop_flow_request.StopFlowRequest = {
            "flow_name": flow_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_appflow.types.arn.ARN",
        tags: "capo_appflow.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
    ) -> "capo_appflow.types.tag_resource_response.TagResourceResponse":
        """<p> Applies a tag to the specified flow. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to tag. </p>
            tags: <p> The tags used to organize, track, or control access for your flow. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.tag_resource

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unregister_connector(
        self,
        connector_label: "capo_appflow.types.connector_label.ConnectorLabel",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        force_delete: Optional["capo_appflow.types.boolean.Boolean"] = None,
    ) -> "capo_appflow.types.unregister_connector_response.UnregisterConnectorResponse":
        """<p>Unregisters the custom connector registered in your account that matches the connector label provided in the request.</p>

        Args:
            connector_label: <p>The label of the connector. The label is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account.</p>
            force_delete: <p>Indicates whether Amazon AppFlow should unregister the connector, even if it is currently in use in one or more connector profiles. The default value is false.</p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.unregister_connector_request.UnregisterConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.unregister_connector_response.UnregisterConnectorResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.unregister_connector

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.unregister_connector.async_unregister_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.unregister_connector_request.UnregisterConnectorRequest = {
            "connector_label": connector_label
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_appflow.types.arn.ARN",
        tag_keys: "capo_appflow.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
    ) -> "capo_appflow.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes a tag from the specified flow. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to untag. </p>
            tag_keys: <p> The tag keys associated with the tag that you want to remove from your flow. </p>

        Raises:
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.untag_resource

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connector_profile(
        self,
        connector_profile_name: "capo_appflow.types.connector_profile_name.ConnectorProfileName",
        connection_mode: "capo_appflow.types.connection_mode.ConnectionMode",
        connector_profile_config: "capo_appflow.types.connector_profile_config.ConnectorProfileConfig",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        client_token: Optional["capo_appflow.types.client_token.ClientToken"] = None,
    ) -> "capo_appflow.types.update_connector_profile_response.UpdateConnectorProfileResponse":
        """<p> Updates a given connector profile associated with your account. </p>

        Args:
            connector_profile_name: <p> The name of the connector profile and is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. </p>
            connection_mode: <p> Indicates the connection mode and if it is public or private. </p>
            connector_profile_config: <p> Defines the connector-specific profile configuration and credentials. </p>
            client_token: <p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>UpdateConnectorProfile</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>UpdateConnectorProfile</code>. The token is active for 8 hours.</p>

        Raises:
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.update_connector_profile_request.UpdateConnectorProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.update_connector_profile_response.UpdateConnectorProfileResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.update_connector_profile

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.update_connector_profile.async_update_connector_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.update_connector_profile_request.UpdateConnectorProfileRequest = {
            "connector_profile_name": connector_profile_name,
            "connection_mode": connection_mode,
            "connector_profile_config": connector_profile_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connector_registration(
        self,
        connector_label: "capo_appflow.types.connector_label.ConnectorLabel",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        description: Optional["capo_appflow.types.description.Description"] = None,
        connector_provisioning_config: Optional[
            "capo_appflow.types.connector_provisioning_config.ConnectorProvisioningConfig"
        ] = None,
        client_token: Optional["capo_appflow.types.client_token.ClientToken"] = None,
    ) -> "capo_appflow.types.update_connector_registration_response.UpdateConnectorRegistrationResponse":
        """<p>Updates a custom connector that you've previously registered. This operation updates the connector with one of the following:</p> <ul> <li> <p>The latest version of the AWS Lambda function that's assigned to the connector</p> </li> <li> <p>A new AWS Lambda function that you specify</p> </li> </ul>

        Args:
            connector_label: <p>The name of the connector. The name is unique for each connector registration in your AWS account.</p>
            description: <p>A description about the update that you're applying to the connector.</p>
            client_token: <p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>UpdateConnectorRegistration</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>UpdateConnectorRegistration</code>. The token is active for 8 hours.</p>

        Raises:
            capo_appflow.errors.access_denied_exception.AccessDeniedException: <p>AppFlow/Requester has invalid or missing permissions.</p>
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.connector_server_exception.ConnectorServerException: <p> An error occurred when retrieving data from the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause a service quota (such as the number of flows) to be exceeded. </p>
            capo_appflow.errors.throttling_exception.ThrottlingException: <p>API calls have exceeded the maximum allowed API request rate per account and per Region. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.update_connector_registration_request.UpdateConnectorRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.update_connector_registration_response.UpdateConnectorRegistrationResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.update_connector_registration

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.update_connector_registration.async_update_connector_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.update_connector_registration_request.UpdateConnectorRegistrationRequest = {
            "connector_label": connector_label
        }
        if description is not None:
            input_["description"] = description
        if connector_provisioning_config is not None:
            input_["connector_provisioning_config"] = connector_provisioning_config
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_flow(
        self,
        flow_name: "capo_appflow.types.flow_name.FlowName",
        trigger_config: "capo_appflow.types.trigger_config.TriggerConfig",
        source_flow_config: "capo_appflow.types.source_flow_config.SourceFlowConfig",
        destination_flow_config_list: "capo_appflow.types.destination_flow_config_list.DestinationFlowConfigList",
        tasks: "capo_appflow.types.tasks.Tasks",
        *,
        config_overrides: Optional[AsyncAppflowClientConfig] = None,
        description: Optional[
            "capo_appflow.types.flow_description.FlowDescription"
        ] = None,
        metadata_catalog_config: Optional[
            "capo_appflow.types.metadata_catalog_config.MetadataCatalogConfig"
        ] = None,
        client_token: Optional["capo_appflow.types.client_token.ClientToken"] = None,
    ) -> "capo_appflow.types.update_flow_response.UpdateFlowResponse":
        """<p> Updates an existing flow. </p>

        Args:
            flow_name: <p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>
            description: <p> A description of the flow. </p>
            trigger_config: <p> The trigger settings that determine how and when the flow runs. </p>
            destination_flow_config_list: <p> The configuration that controls how Amazon AppFlow transfers data to the destination connector. </p>
            tasks: <p> A list of tasks that Amazon AppFlow performs while transferring the data in the flow run. </p>
            metadata_catalog_config: <p>Specifies the configuration that Amazon AppFlow uses when it catalogs the data that's transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.</p>
            client_token: <p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>UpdateFlow</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>UpdateFlow</code>. The token is active for 8 hours.</p>

        Raises:
            capo_appflow.errors.access_denied_exception.AccessDeniedException: <p>AppFlow/Requester has invalid or missing permissions.</p>
            capo_appflow.errors.conflict_exception.ConflictException: <p> There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again. </p>
            capo_appflow.errors.connector_authentication_exception.ConnectorAuthenticationException: <p> An error occurred when authenticating with the connector endpoint. </p>
            capo_appflow.errors.connector_server_exception.ConnectorServerException: <p> An error occurred when retrieving data from the connector endpoint. </p>
            capo_appflow.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_appflow.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource specified in the request (such as the source or destination connector profile) is not found. </p>
            capo_appflow.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause a service quota (such as the number of flows) to be exceeded. </p>
            capo_appflow.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_appflow.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_appflow.types.update_flow_request.UpdateFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_appflow.types.update_flow_response.UpdateFlowResponse"
        ]:
            import capo_appflow._operations.sandstone_configuration_service_lambda.update_flow

            (
                output,
                http_response,
            ) = await capo_appflow._operations.sandstone_configuration_service_lambda.update_flow.async_update_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appflow.types.update_flow_request.UpdateFlowRequest = {
            "flow_name": flow_name,
            "trigger_config": trigger_config,
            "source_flow_config": source_flow_config,
            "destination_flow_config_list": destination_flow_config_list,
            "tasks": tasks,
        }
        if description is not None:
            input_["description"] = description
        if metadata_catalog_config is not None:
            input_["metadata_catalog_config"] = metadata_catalog_config
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

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

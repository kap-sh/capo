"""Generated from Smithy shape ``com.amazonaws.supplychain#GalaxyPublicAPIGateway``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_supplychain._auth._signers
import capo_supplychain._auth._sigv4
from capo_supplychain._auth._identity import Credentials
from capo_supplychain._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_supplychain._auth._zapros_handler import AuthMiddleware
from capo_supplychain._pagination import resolve_path as _resolve_path
from capo_supplychain._resources.galaxy_public_api_gateway.bill_of_materials_import_job_resource import (
    AsyncBillOfMaterialsImportJobResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.data_integration_flow_resource import (
    AsyncDataIntegrationFlowResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.data_lake_dataset_resource import (
    AsyncDataLakeDatasetResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.data_lake_namespace_resource import (
    AsyncDataLakeNamespaceResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.instance_resource import (
    AsyncInstanceResource,
)
from capo_supplychain._services._aws_config import aaws_config
from capo_supplychain._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_supplychain.types.asc_resource_arn
    import capo_supplychain.types.client_token
    import capo_supplychain.types.configuration_s3_uri
    import capo_supplychain.types.create_bill_of_materials_import_job_request
    import capo_supplychain.types.create_bill_of_materials_import_job_response
    import capo_supplychain.types.create_data_integration_flow_request
    import capo_supplychain.types.create_data_integration_flow_response
    import capo_supplychain.types.create_data_lake_dataset_request
    import capo_supplychain.types.create_data_lake_dataset_response
    import capo_supplychain.types.create_data_lake_namespace_request
    import capo_supplychain.types.create_data_lake_namespace_response
    import capo_supplychain.types.create_instance_request
    import capo_supplychain.types.create_instance_response
    import capo_supplychain.types.data_integration_event
    import capo_supplychain.types.data_integration_event_data
    import capo_supplychain.types.data_integration_event_dataset_target_configuration
    import capo_supplychain.types.data_integration_event_group_id
    import capo_supplychain.types.data_integration_event_max_results
    import capo_supplychain.types.data_integration_event_next_token
    import capo_supplychain.types.data_integration_event_type
    import capo_supplychain.types.data_integration_flow
    import capo_supplychain.types.data_integration_flow_execution
    import capo_supplychain.types.data_integration_flow_execution_max_results
    import capo_supplychain.types.data_integration_flow_execution_next_token
    import capo_supplychain.types.data_integration_flow_max_results
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.data_integration_flow_next_token
    import capo_supplychain.types.data_integration_flow_source_list
    import capo_supplychain.types.data_integration_flow_target
    import capo_supplychain.types.data_integration_flow_transformation
    import capo_supplychain.types.data_lake_dataset
    import capo_supplychain.types.data_lake_dataset_description
    import capo_supplychain.types.data_lake_dataset_max_results
    import capo_supplychain.types.data_lake_dataset_name
    import capo_supplychain.types.data_lake_dataset_next_token
    import capo_supplychain.types.data_lake_dataset_partition_spec
    import capo_supplychain.types.data_lake_dataset_schema
    import capo_supplychain.types.data_lake_namespace
    import capo_supplychain.types.data_lake_namespace_description
    import capo_supplychain.types.data_lake_namespace_max_results
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.data_lake_namespace_next_token
    import capo_supplychain.types.delete_data_integration_flow_request
    import capo_supplychain.types.delete_data_integration_flow_response
    import capo_supplychain.types.delete_data_lake_dataset_request
    import capo_supplychain.types.delete_data_lake_dataset_response
    import capo_supplychain.types.delete_data_lake_namespace_request
    import capo_supplychain.types.delete_data_lake_namespace_response
    import capo_supplychain.types.delete_instance_request
    import capo_supplychain.types.delete_instance_response
    import capo_supplychain.types.get_bill_of_materials_import_job_request
    import capo_supplychain.types.get_bill_of_materials_import_job_response
    import capo_supplychain.types.get_data_integration_event_request
    import capo_supplychain.types.get_data_integration_event_response
    import capo_supplychain.types.get_data_integration_flow_execution_request
    import capo_supplychain.types.get_data_integration_flow_execution_response
    import capo_supplychain.types.get_data_integration_flow_request
    import capo_supplychain.types.get_data_integration_flow_response
    import capo_supplychain.types.get_data_lake_dataset_request
    import capo_supplychain.types.get_data_lake_dataset_response
    import capo_supplychain.types.get_data_lake_namespace_request
    import capo_supplychain.types.get_data_lake_namespace_response
    import capo_supplychain.types.get_instance_request
    import capo_supplychain.types.get_instance_response
    import capo_supplychain.types.instance
    import capo_supplychain.types.instance_description
    import capo_supplychain.types.instance_max_results
    import capo_supplychain.types.instance_name
    import capo_supplychain.types.instance_name_list
    import capo_supplychain.types.instance_next_token
    import capo_supplychain.types.instance_state_list
    import capo_supplychain.types.instance_web_app_dns_domain
    import capo_supplychain.types.kms_key_arn
    import capo_supplychain.types.list_data_integration_events_request
    import capo_supplychain.types.list_data_integration_events_response
    import capo_supplychain.types.list_data_integration_flow_executions_request
    import capo_supplychain.types.list_data_integration_flow_executions_response
    import capo_supplychain.types.list_data_integration_flows_request
    import capo_supplychain.types.list_data_integration_flows_response
    import capo_supplychain.types.list_data_lake_datasets_request
    import capo_supplychain.types.list_data_lake_datasets_response
    import capo_supplychain.types.list_data_lake_namespaces_request
    import capo_supplychain.types.list_data_lake_namespaces_response
    import capo_supplychain.types.list_instances_request
    import capo_supplychain.types.list_instances_response
    import capo_supplychain.types.list_tags_for_resource_request
    import capo_supplychain.types.list_tags_for_resource_response
    import capo_supplychain.types.send_data_integration_event_request
    import capo_supplychain.types.send_data_integration_event_response
    import capo_supplychain.types.tag_key_list
    import capo_supplychain.types.tag_map
    import capo_supplychain.types.tag_resource_request
    import capo_supplychain.types.tag_resource_response
    import capo_supplychain.types.untag_resource_request
    import capo_supplychain.types.untag_resource_response
    import capo_supplychain.types.update_data_integration_flow_request
    import capo_supplychain.types.update_data_integration_flow_response
    import capo_supplychain.types.update_data_lake_dataset_request
    import capo_supplychain.types.update_data_lake_dataset_response
    import capo_supplychain.types.update_data_lake_namespace_request
    import capo_supplychain.types.update_data_lake_namespace_response
    import capo_supplychain.types.update_instance_request
    import capo_supplychain.types.update_instance_response
    import capo_supplychain.types.uuid


class AsyncSupplyChainClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSupplyChainClient:
    """A client for the ``SupplyChain`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncSupplyChainClientConfig(
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
        self.bill_of_materials_import_job_resource = (
            AsyncBillOfMaterialsImportJobResource(self)
        )
        self.data_integration_flow_resource = AsyncDataIntegrationFlowResource(self)
        self.data_lake_dataset_resource = AsyncDataLakeDatasetResource(self)
        self.data_lake_namespace_resource = AsyncDataLakeNamespaceResource(self)
        self.instance_resource = AsyncInstanceResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSupplyChainClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSupplyChainClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def get_data_integration_event(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        event_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_integration_event_response.GetDataIntegrationEventResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain Data Integration Event. Developers can view the eventType, eventGroupId, eventTimestamp, datasetTarget, datasetLoadExecution.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            event_id: <p>The unique event identifier.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetDataIntegrationEvent

            >>> await client.get_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_id='19739c8e-cd2e-4cbc-a2f7-0dc43239f042')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_data_integration_event_request.GetDataIntegrationEventRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_data_integration_event_response.GetDataIntegrationEventResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_event

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_event.async_get_data_integration_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_data_integration_event_request.GetDataIntegrationEventRequest = {
            "instance_id": instance_id,
            "event_id": event_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_integration_flow_execution(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        flow_name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        execution_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_integration_flow_execution_response.GetDataIntegrationFlowExecutionResponse":
        """<p>Get the flow execution.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            flow_name: <p>The flow name.</p>
            execution_id: <p>The flow execution identifier.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetDataIntegrationFlowExecution for S3 source

            >>> await client.get_data_integration_flow_execution(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', flow_name='source-product', execution_id='edbbdd3f-c0f9-49d9-ab01-f64542f803b7')
            Successful GetDataIntegrationFlowExecution for DATASET source

            >>> await client.get_data_integration_flow_execution(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', flow_name='target-product', execution_id='9daf6071-d12c-4eef-864c-73cea2557825')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_data_integration_flow_execution_request.GetDataIntegrationFlowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_data_integration_flow_execution_response.GetDataIntegrationFlowExecutionResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow_execution

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow_execution.async_get_data_integration_flow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_data_integration_flow_execution_request.GetDataIntegrationFlowExecutionRequest = {
            "instance_id": instance_id,
            "flow_name": flow_name,
            "execution_id": execution_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_integration_events(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        event_type: Optional[
            "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
        ] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_event_max_results.DataIntegrationEventMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_integration_events_response.ListDataIntegrationEventsResponse":
        """<p>Enables you to programmatically list all data integration events for the provided Amazon Web Services Supply Chain instance.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            event_type: <p>List data integration events for the specified eventType.</p>
            next_token: <p>The pagination token to fetch the next page of the data integration events.</p>
            max_results: <p>Specify the maximum number of data integration events to fetch in one paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListDataIntegrationEvents

            >>> await client.list_data_integration_events(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_data_integration_events_request.ListDataIntegrationEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_data_integration_events_response.ListDataIntegrationEventsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_events

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_events.async_list_data_integration_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_data_integration_events_request.ListDataIntegrationEventsRequest = {
            "instance_id": instance_id
        }
        if event_type is not None:
            input_["event_type"] = event_type
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

    async def iter_list_data_integration_events(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        event_type: Optional[
            "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
        ] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_event_max_results.DataIntegrationEventMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_supplychain.types.data_integration_event.DataIntegrationEvent]":
        _token = next_token
        while True:
            _response = await self.list_data_integration_events(
                instance_id,
                config_overrides=config_overrides,
                event_type=event_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_integration_flow_executions(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        flow_name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_execution_next_token.DataIntegrationFlowExecutionNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_execution_max_results.DataIntegrationFlowExecutionMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_integration_flow_executions_response.ListDataIntegrationFlowExecutionsResponse":
        """<p>List flow executions.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            flow_name: <p>The flow name.</p>
            next_token: <p>The pagination token to fetch next page of flow executions.</p>
            max_results: <p>The number to specify the max number of flow executions to fetch in this paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListDataIntegrationFlowExecutions

            >>> await client.list_data_integration_flow_executions(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', flow_name='source-product')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_data_integration_flow_executions_request.ListDataIntegrationFlowExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_data_integration_flow_executions_response.ListDataIntegrationFlowExecutionsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flow_executions

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flow_executions.async_list_data_integration_flow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_data_integration_flow_executions_request.ListDataIntegrationFlowExecutionsRequest = {
            "instance_id": instance_id,
            "flow_name": flow_name,
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

    async def iter_list_data_integration_flow_executions(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        flow_name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_execution_next_token.DataIntegrationFlowExecutionNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_execution_max_results.DataIntegrationFlowExecutionMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_supplychain.types.data_integration_flow_execution.DataIntegrationFlowExecution]":
        _token = next_token
        while True:
            _response = await self.list_data_integration_flow_executions(
                instance_id,
                flow_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("flow_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for an Amazon Web ServicesSupply Chain resource. You can list all the tags added to a resource. By listing the tags, developers can view the tag level information on a resource and perform actions such as, deleting a resource associated with a particular tag.</p>

        Args:
            resource_arn: <p>The Amazon Web Services Supply chain resource ARN that needs tags to be listed.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListTagsForResource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/data-integration-flows/my_flow1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_data_integration_event(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        event_type: "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType",
        data: "capo_supplychain.types.data_integration_event_data.DataIntegrationEventData",
        event_group_id: "capo_supplychain.types.data_integration_event_group_id.DataIntegrationEventGroupId",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        event_timestamp: Optional[datetime.datetime] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
        dataset_target: Optional[
            "capo_supplychain.types.data_integration_event_dataset_target_configuration.DataIntegrationEventDatasetTargetConfiguration"
        ] = None,
    ) -> "capo_supplychain.types.send_data_integration_event_response.SendDataIntegrationEventResponse":
        """<p>Send the data payload for the event with real-time data for analysis or monitoring. The real-time data events are stored in an Amazon Web Services service before being processed and stored in data lake.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            event_type: <p>The data event type.</p> <ul> <li> <p> <b>scn.data.dataset</b> - Send data directly to any specified dataset.</p> </li> <li> <p> <b>scn.data.supplyplan</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/supply-plan-entity.html">supply_plan</a> dataset.</p> </li> <li> <p> <b>scn.data.shipmentstoporder</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-order-entity.html">shipment_stop_order</a> dataset.</p> </li> <li> <p> <b>scn.data.shipmentstop</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-entity.html">shipment_stop</a> dataset.</p> </li> <li> <p> <b>scn.data.shipment</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-entity.html">shipment</a> dataset.</p> </li> <li> <p> <b>scn.data.reservation</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-reservation-entity.html">reservation</a> dataset.</p> </li> <li> <p> <b>scn.data.processproduct</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-product-entity.html">process_product</a> dataset.</p> </li> <li> <p> <b>scn.data.processoperation</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-operation-entity.html">process_operation</a> dataset.</p> </li> <li> <p> <b>scn.data.processheader</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-header-entity.html">process_header</a> dataset.</p> </li> <li> <p> <b>scn.data.forecast</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-forecast-entity.html">forecast</a> dataset.</p> </li> <li> <p> <b>scn.data.inventorylevel</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory_mgmnt-inv-level-entity.html">inv_level</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorder</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-entity.html">inbound_order</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorderline</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-entity.html">inbound_order_line</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorderlineschedule</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-schedule-entity.html">inbound_order_line_schedule</a> dataset.</p> </li> <li> <p> <b>scn.data.outboundorderline</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-order-line-entity.html">outbound_order_line</a> dataset.</p> </li> <li> <p> <b>scn.data.outboundshipment</b> - Send data to <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-shipment-entity.html">outbound_shipment</a> dataset.</p> </li> </ul>
            data: <p>The data payload of the event, should follow the data schema of the target dataset, or see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">Data entities supported in AWS Supply Chain</a>. To send single data record, use JsonObject format; to send multiple data records, use JsonArray format.</p> <p>Note that for AWS Supply Chain dataset under <b>asc</b> namespace, it has a connection_id internal field that is not allowed to be provided by client directly, they will be auto populated.</p>
            event_group_id: <p>Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning. Noted under one eventGroupId of same eventType and instanceId, events are processed sequentially in the order they are received by the server.</p>
            event_timestamp: <p>The timestamp (in epoch seconds) associated with the event. If not provided, it will be assigned with current timestamp.</p>
            client_token: <p>The idempotent client token. The token is active for 8 hours, and within its lifetime, it ensures the request completes only once upon retry with same client token. If omitted, the AWS SDK generates a unique value so that AWS SDK can safely retry the request upon network errors.</p>
            dataset_target: <p>The target dataset configuration for <b>scn.data.dataset</b> event type.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful SendDataIntegrationEvent for inboundorder event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inboundorder', data='{"id": "inbound-order-id-test-123", "tpartner_id": "partner-id-test-123" }', event_group_id='inboundOrderId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for inboundorderline event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inboundorderline', data='{"id": "inbound-order-line-id-test-123", "order_id": "order-id-test-123", "tpartner_id": "partner-id-test-123", "product_id": "product-id-test-123", "quantity_submitted": "100.0" }', event_group_id='inboundOrderLineId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for inboundorderlineschedule event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inboundorderlineschedule', data='{"id": "inbound-order-line-schedule-id-test-123", "order_id": "order-id-test-123", "order_line_id": "order-line-id-test-123", "product_id": "product-id-test-123"}', event_group_id='inboundOrderLineScheduleId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for forecast event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.forecast', data='{"snapshot_date": "1672470400000", "product_id": "product-id-test-123", "site_id": "site-id-test-123", "region_id": "region-id-test-123", "product_group_id": "product-group-id-test-123", "forecast_start_dttm": "1672470400000", "forecast_end_dttm": "1672470400000" }', event_group_id='forecastId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for inventorylevel event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inventorylevel', data='{"snapshot_date": "1672470400000", "site_id": "site-id-test-123", "product_id": "product-id-test-123", "on_hand_inventory": "100.0", "inv_condition": "good", "lot_number": "lot-number-test-123"}', event_group_id='inventoryLevelId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for outboundorderline event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.outboundorderline', data='{"id": "outbound-orderline-id-test-123", "cust_order_id": "cust-order-id-test-123", "product_id": "product-id-test-123" }', event_group_id='outboundOrderLineId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for outboundshipment event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.outboundshipment', data='{"id": "outbound-shipment-id-test-123", "cust_order_id": "cust-order-id-test-123", "cust_order_line_id": "cust-order-line-id-test-123", "product_id": "product-id-test-123" }', event_group_id='outboundShipmentId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for processheader event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.processheader', data='{"process_id": "process-id-test-123" }', event_group_id='processHeaderId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for processoperation event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.processoperation', data='{"process_operation_id": "process-operation-id-test-123", "process_id": "process-id-test-123" }', event_group_id='processOperationId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for processproduct event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.processproduct', data='{"process_product_id": "process-product-id-test-123", "process_id": "process-id-test-123" }', event_group_id='processProductId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for reservation event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.reservation', data='{"reservation_id": "reservation-id-test-123", "reservation_detail_id": "reservation-detail-id-test-123" }', event_group_id='reservationId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for shipment event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.shipment', data='{"id": "shipment-id-test-123", "supplier_tpartner_id": "supplier-tpartner-id-test-123", "product_id": "product-id-test-123", "order_id": "order-id-test-123", "order_line_id": "order-line-id-test-123", "package_id": "package-id-test-123" }', event_group_id='shipmentId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for shipmentstop event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.shipmentstop', data='{"shipment_stop_id": "shipment-stop-id-test-123", "shipment_id": "shipment-id-test-123" }', event_group_id='shipmentStopId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for shipmentstoporder event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.shipmentstoporder', data='{"shipment_stop_order_id": "shipment-stop-order-id-test-123", "shipment_stop_id": "shipment-stop-id-test-123", "shipment_id": "shipment-id-test-123" }', event_group_id='shipmentStopOrderId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for supplyplan event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.supplyplan', data='{"supply_plan_id": "supply-plan-id-test-123" }', event_group_id='supplyPlanId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for dataset event type

            >>> await client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.dataset', data='{"dataset_id": "datset-id-test-123" }', event_group_id='datasetId', event_timestamp=1515531081.123, dataset_target={'datasetIdentifier': 'arn:aws:scn:us-west-2:135808960812:instance/8928ae12-15e5-4441-825d-ec2184f0a43a/namespaces/asc/datasets/product', 'operationType': 'APPEND'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.send_data_integration_event_request.SendDataIntegrationEventRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.send_data_integration_event_response.SendDataIntegrationEventResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.send_data_integration_event

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.send_data_integration_event.async_send_data_integration_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.send_data_integration_event_request.SendDataIntegrationEventRequest = {
            "instance_id": instance_id,
            "event_type": event_type,
            "data": data,
            "event_group_id": event_group_id,
        }
        if event_timestamp is not None:
            input_["event_timestamp"] = event_timestamp
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if dataset_target is not None:
            input_["dataset_target"] = dataset_target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn",
        tags: "capo_supplychain.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.tag_resource_response.TagResourceResponse":
        """<p>You can create tags during or after creating a resource such as instance, data flow, or dataset in AWS Supply chain. During the data ingestion process, you can add tags such as dev, test, or prod to data flows created during the data ingestion process in the AWS Supply Chain datasets. You can use these tags to identify a group of resources or a single resource used by the developer.</p>

        Args:
            resource_arn: <p>The Amazon Web Services Supply chain resource ARN that needs to be tagged.</p>
            tags: <p>The tags of the Amazon Web Services Supply chain resource to be created.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful TagResource

            >>> await client.tag_resource(resource_arn='arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/data-integration-flows/my_flow1', tags={'tagKey1': 'tagValue1'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.tag_resource

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.tag_resource_request.TagResourceRequest = {
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

    async def untag_resource(
        self,
        resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn",
        tag_keys: "capo_supplychain.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.untag_resource_response.UntagResourceResponse":
        """<p>You can delete tags for an Amazon Web Services Supply chain resource such as instance, data flow, or dataset in AWS Supply Chain. During the data ingestion process, you can delete tags such as dev, test, or prod to data flows created during the data ingestion process in the AWS Supply Chain datasets. </p>

        Args:
            resource_arn: <p>The Amazon Web Services Supply chain resource ARN that needs to be untagged.</p>
            tag_keys: <p>The list of tag keys to be deleted for an Amazon Web Services Supply Chain resource.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful UntagResource

            >>> await client.untag_resource(resource_arn='arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/data-integration-flows/my_flow1', tag_keys=['tagKey1'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.untag_resource

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_bill_of_materials_import_job(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        s3uri: "capo_supplychain.types.configuration_s3_uri.ConfigurationS3Uri",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse":
        """<p>CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of Materials (BOM) entity. For information on the product_bom entity, see the AWS Supply Chain User Guide.</p> <p>The CSV file must be located in an Amazon S3 location accessible to AWS Supply Chain. It is recommended to use the same Amazon S3 bucket created during your AWS Supply Chain instance creation.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            s3uri: <p>The S3 URI of the CSV file to be imported. The bucket must grant permissions for AWS Supply Chain to read the file.</p>
            client_token: <p>An idempotency token ensures the API request is only completed no more than once. This way, retrying the request will not trigger the operation multiple times. A client token is a unique, case-sensitive string of 33 to 128 ASCII characters. To make an idempotent API request, specify a client token in the request. You should not reuse the same client token for other requests. If you retry a successful request with the same client token, the request will succeed with no further actions being taken, and you will receive the same API response as the original successful request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateBillOfMaterialsImportJob

            >>> await client.create_bill_of_materials_import_job(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', s3uri='s3://mybucketname/pathelemene/file.csv', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job.async_create_bill_of_materials_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest = {
            "instance_id": instance_id,
            "s3uri": s3uri,
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

    async def get_bill_of_materials_import_job(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        job_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse":
        """<p>Get status and details of a BillOfMaterialsImportJob.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            job_id: <p>The BillOfMaterialsImportJob identifier.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetBillOfMaterialsImportJob for a successful job

            >>> await client.get_bill_of_materials_import_job(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
            Invoke GetBillOfMaterialsImportJob for an in-progress job

            >>> await client.get_bill_of_materials_import_job(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job.async_get_bill_of_materials_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest = {
            "instance_id": instance_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_integration_flow(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        sources: "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList",
        transformation: "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation",
        target: "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
    ) -> "capo_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically create a data pipeline to ingest data from source systems such as Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>Name of the DataIntegrationFlow.</p>
            sources: <p>The source configurations for DataIntegrationFlow.</p>
            transformation: <p>The transformation configurations for DataIntegrationFlow.</p>
            target: <p>The target configurations for DataIntegrationFlow.</p>
            tags: <p>The tags of the DataIntegrationFlow to be created</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful CreateDataIntegrationFlow for s3 to dataset flow

            >>> await client.create_data_integration_flow(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT * FROM testSourceName'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}}, tags={'tagKey1': 'tagValue1'})
            Successful CreateDataIntegrationFlow for dataset to dataset flow

            >>> await client.create_data_integration_flow(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'DESC'}]}}}}}, tags={'tagKey1': 'tagValue1'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow.async_create_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
            "sources": sources,
            "transformation": transformation,
            "target": target,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_integration_flow(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse":
        """<p>Enables you to programmatically view a specific data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow created.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetDataIntegrationFlow

            >>> await client.get_data_integration_flow(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow.async_get_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_integration_flow(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        sources: Optional[
            "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
        ] = None,
        transformation: Optional[
            "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
        ] = None,
        target: Optional[
            "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
        ] = None,
    ) -> "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically update an existing data pipeline to ingest data from the source systems such as, Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be updated.</p>
            sources: <p>The new source configurations for the DataIntegrationFlow.</p>
            transformation: <p>The new transformation configurations for the DataIntegrationFlow.</p>
            target: <p>The new target configurations for the DataIntegrationFlow.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful UpdateDataIntegrationFlow for s3 to dataset flow to update SQL transformation

            >>> await client.update_data_integration_flow(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': "SELECT connection_id, bukrs AS id, txtmd AS description FROM testSourceName WHERE langu = 'E'"}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}})
            Successful UpdateDataIntegrationFlow for dataset to dataset flow to update sources

            >>> await client.update_data_integration_flow(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2_updated'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'ASC'}]}}}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow.async_update_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
        }
        if sources is not None:
            input_["sources"] = sources
        if transformation is not None:
            input_["transformation"] = transformation
        if target is not None:
            input_["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_integration_flow(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse":
        """<p>Enable you to programmatically delete an existing data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be deleted.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful DeleteDataIntegrationFlow

            >>> await client.delete_data_integration_flow(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow.async_delete_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest = {
            "instance_id": instance_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_integration_flows(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse":
        """<p>Enables you to programmatically list all data pipelines for the provided Amazon Web Services Supply Chain instance.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>
            max_results: <p>Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListDataIntegrationFlow

            >>> await client.list_data_integration_flows(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows.async_list_data_integration_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest = {
            "instance_id": instance_id
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

    async def iter_list_data_integration_flows(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_supplychain.types.data_integration_flow.DataIntegrationFlow]":
        _token = next_token
        while True:
            _response = await self.list_data_integration_flows(
                instance_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("flows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_data_lake_dataset(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "capo_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        schema: Optional[
            "capo_supplychain.types.data_lake_dataset_schema.DataLakeDatasetSchema"
        ] = None,
        description: Optional[
            "capo_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"
        ] = None,
        partition_spec: Optional[
            "capo_supplychain.types.data_lake_dataset_partition_spec.DataLakeDatasetPartitionSpec"
        ] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
    ) -> "capo_supplychain.types.create_data_lake_dataset_response.CreateDataLakeDatasetResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain data lake dataset. Developers can create the datasets using their pre-defined or custom schema for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> name space, the name must be one of the supported data entities under <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>
            schema: <p>The custom schema of the data lake dataset and required for dataset in <b>default</b> and custom namespaces.</p>
            description: <p>The description of the dataset.</p>
            partition_spec: <p>The partition specification of the dataset. Partitioning can effectively improve the dataset query performance by reducing the amount of data scanned during query execution. But partitioning or not will affect how data get ingested by data ingestion methods, such as SendDataIntegrationEvent's dataset UPSERT will upsert records within partition (instead of within whole dataset). For more details, refer to those data ingestion documentations.</p>
            tags: <p>The tags of the dataset.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an AWS Supply Chain inbound order dataset

            >>> await client.create_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order', description='This is an AWS Supply Chain inbound order dataset', tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
            Create a custom dataset

            >>> await client.create_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset', description='This is a custom dataset', schema={'name': 'MyDataset', 'fields': [{'name': 'id', 'type': 'INT', 'isRequired': True}, {'name': 'description', 'type': 'STRING', 'isRequired': True}, {'name': 'price', 'type': 'DOUBLE', 'isRequired': False}, {'name': 'creation_time', 'type': 'TIMESTAMP', 'isRequired': False}, {'name': 'quantity', 'type': 'LONG', 'isRequired': False}], 'primaryKeys': [{'name': 'id'}]}, partition_spec={'fields': [{'name': 'creation_time', 'transform': {'type': 'DAY'}}, {'name': 'description', 'transform': {'type': 'IDENTITY'}}]}, tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_data_lake_dataset_request.CreateDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_data_lake_dataset_response.CreateDataLakeDatasetResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_data_lake_dataset

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_data_lake_dataset.async_create_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.create_data_lake_dataset_request.CreateDataLakeDatasetRequest = {
            "instance_id": instance_id,
            "namespace": namespace,
            "name": name,
        }
        if schema is not None:
            input_["schema"] = schema
        if description is not None:
            input_["description"] = description
        if partition_spec is not None:
            input_["partition_spec"] = partition_spec
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_lake_dataset(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "capo_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_lake_dataset_response.GetDataLakeDatasetResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain data lake dataset. Developers can view the data lake dataset information such as namespace, schema, and so on for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get properties of an existing AWS Supply Chain inbound order dataset

            >>> await client.get_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order')
            Get proporties of an existing custom dataset

            >>> await client.get_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_data_lake_dataset_request.GetDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_data_lake_dataset_response.GetDataLakeDatasetResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_lake_dataset

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_data_lake_dataset.async_get_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_data_lake_dataset_request.GetDataLakeDatasetRequest = {
            "instance_id": instance_id,
            "namespace": namespace,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_lake_dataset(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "capo_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        description: Optional[
            "capo_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"
        ] = None,
    ) -> "capo_supplychain.types.update_data_lake_dataset_response.UpdateDataLakeDatasetResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain data lake dataset. Developers can update the description of a data lake dataset for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>
            description: <p>The updated description of the data lake dataset.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update description of an existing AWS Supply Chain inbound order dataset

            >>> await client.update_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order', description='This is an updated AWS Supply Chain inbound order dataset')
            Update description of an existing custom dataset

            >>> await client.update_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset', description='This is an updated custom dataset')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.update_data_lake_dataset_request.UpdateDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.update_data_lake_dataset_response.UpdateDataLakeDatasetResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_data_lake_dataset

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.update_data_lake_dataset.async_update_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.update_data_lake_dataset_request.UpdateDataLakeDatasetRequest = {
            "instance_id": instance_id,
            "namespace": namespace,
            "name": name,
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

    async def delete_data_lake_dataset(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "capo_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_data_lake_dataset_response.DeleteDataLakeDatasetResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain data lake dataset. Developers can delete the existing datasets for a given instance ID, namespace, and instance name.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an AWS Supply Chain inbound_order dataset

            >>> await client.delete_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order')
            Delete a custom dataset

            >>> await client.delete_data_lake_dataset(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.delete_data_lake_dataset_request.DeleteDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.delete_data_lake_dataset_response.DeleteDataLakeDatasetResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_dataset

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_dataset.async_delete_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.delete_data_lake_dataset_request.DeleteDataLakeDatasetRequest = {
            "instance_id": instance_id,
            "namespace": namespace,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_lake_datasets(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_lake_dataset_next_token.DataLakeDatasetNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_lake_dataset_max_results.DataLakeDatasetMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_lake_datasets_response.ListDataLakeDatasetsResponse":
        """<p>Enables you to programmatically view the list of Amazon Web Services Supply Chain data lake datasets. Developers can view the datasets and the corresponding information such as namespace, schema, and so on for a given instance ID and namespace.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            next_token: <p>The pagination token to fetch next page of datasets.</p>
            max_results: <p>The max number of datasets to fetch in this paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List AWS Supply Chain datasets

            >>> await client.list_data_lake_datasets(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc')
            List custom datasets using pagination

            >>> await client.list_data_lake_datasets(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', max_results=2, next_token='next_token_returned_from_previous_list_request')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_data_lake_datasets_request.ListDataLakeDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_data_lake_datasets_response.ListDataLakeDatasetsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_lake_datasets

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_data_lake_datasets.async_list_data_lake_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_data_lake_datasets_request.ListDataLakeDatasetsRequest = {
            "instance_id": instance_id,
            "namespace": namespace,
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

    async def iter_list_data_lake_datasets(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_lake_dataset_next_token.DataLakeDatasetNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_lake_dataset_max_results.DataLakeDatasetMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_supplychain.types.data_lake_dataset.DataLakeDataset]":
        _token = next_token
        while True:
            _response = await self.list_data_lake_datasets(
                instance_id,
                namespace,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_data_lake_namespace(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        description: Optional[
            "capo_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
        ] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
    ) -> "capo_supplychain.types.create_data_lake_namespace_response.CreateDataLakeNamespaceResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain data lake namespace. Developers can create the namespaces for a given instance ID.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot create namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>
            description: <p>The description of the namespace.</p>
            tags: <p>The tags of the namespace.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a data lake namespace

            >>> await client.create_data_lake_namespace(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace', description='This is my AWS Supply Chain namespace', tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_data_lake_namespace_request.CreateDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_data_lake_namespace_response.CreateDataLakeNamespaceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_data_lake_namespace

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_data_lake_namespace.async_create_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.create_data_lake_namespace_request.CreateDataLakeNamespaceRequest = {
            "instance_id": instance_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_lake_namespace(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_lake_namespace_response.GetDataLakeNamespaceResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain data lake namespace. Developers can view the data lake namespace information such as description for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Besides the namespaces user created, you can also specify the pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - Pre-defined namespace containing Amazon Web Services Supply Chain supported datasets, see <a href="https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - Pre-defined namespace containing datasets with custom user-defined schemas.</p> </li> </ul>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get properties of an existing AWS Supply Chain namespace

            >>> await client.get_data_lake_namespace(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace')
            Get proporties of an existing pre-defined AWS Supply Chain namespace

            >>> await client.get_data_lake_namespace(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='asc')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_data_lake_namespace_request.GetDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_data_lake_namespace_response.GetDataLakeNamespaceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_lake_namespace

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_data_lake_namespace.async_get_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_data_lake_namespace_request.GetDataLakeNamespaceRequest = {
            "instance_id": instance_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_lake_namespace(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        description: Optional[
            "capo_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
        ] = None,
    ) -> "capo_supplychain.types.update_data_lake_namespace_response.UpdateDataLakeNamespaceResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain data lake namespace. Developers can update the description of a data lake namespace for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot update namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>
            description: <p>The updated description of the data lake namespace.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update description of an existing AWS Supply Chain namespace

            >>> await client.update_data_lake_namespace(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace', description='This is an updated AWS Supply Chain namespace')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.update_data_lake_namespace_request.UpdateDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.update_data_lake_namespace_response.UpdateDataLakeNamespaceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_data_lake_namespace

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.update_data_lake_namespace.async_update_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.update_data_lake_namespace_request.UpdateDataLakeNamespaceRequest = {
            "instance_id": instance_id,
            "name": name,
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

    async def delete_data_lake_namespace(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_data_lake_namespace_response.DeleteDataLakeNamespaceResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain data lake namespace and its underling datasets. Developers can delete the existing namespaces for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot delete pre-defined namespace like <b>asc</b>, <b>default</b> which are only deleted through instance deletion.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an AWS Supply Chain namespace

            >>> await client.delete_data_lake_namespace(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.delete_data_lake_namespace_request.DeleteDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.delete_data_lake_namespace_response.DeleteDataLakeNamespaceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_namespace

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_namespace.async_delete_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.delete_data_lake_namespace_request.DeleteDataLakeNamespaceRequest = {
            "instance_id": instance_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_lake_namespaces(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_lake_namespace_next_token.DataLakeNamespaceNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_lake_namespace_max_results.DataLakeNamespaceMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_lake_namespaces_response.ListDataLakeNamespacesResponse":
        """<p>Enables you to programmatically view the list of Amazon Web Services Supply Chain data lake namespaces. Developers can view the namespaces and the corresponding information such as description for a given instance ID. Note that this API only return custom namespaces, instance pre-defined namespaces are not included.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch next page of namespaces.</p>
            max_results: <p>The max number of namespaces to fetch in this paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List AWS Supply Chain namespaces

            >>> await client.list_data_lake_namespaces(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5')
            List AWS Supply Chain namespaces using pagination

            >>> await client.list_data_lake_namespaces(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', max_results=1, next_token='next_token_returned_from_previous_list_request')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_data_lake_namespaces_request.ListDataLakeNamespacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_data_lake_namespaces_response.ListDataLakeNamespacesResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_lake_namespaces

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_data_lake_namespaces.async_list_data_lake_namespaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_data_lake_namespaces_request.ListDataLakeNamespacesRequest = {
            "instance_id": instance_id
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

    async def iter_list_data_lake_namespaces(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_lake_namespace_next_token.DataLakeNamespaceNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_lake_namespace_max_results.DataLakeNamespaceMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_supplychain.types.data_lake_namespace.DataLakeNamespace]":
        _token = next_token
        while True:
            _response = await self.list_data_lake_namespaces(
                instance_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("namespaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_instance(
        self,
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        instance_name: Optional[
            "capo_supplychain.types.instance_name.InstanceName"
        ] = None,
        instance_description: Optional[
            "capo_supplychain.types.instance_description.InstanceDescription"
        ] = None,
        kms_key_arn: Optional["capo_supplychain.types.kms_key_arn.KmsKeyArn"] = None,
        web_app_dns_domain: Optional[
            "capo_supplychain.types.instance_web_app_dns_domain.InstanceWebAppDnsDomain"
        ] = None,
        tags: Optional["capo_supplychain.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_supplychain.types.create_instance_response.CreateInstanceResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain instance by applying KMS keys and relevant information associated with the API without using the Amazon Web Services console.</p> <p>This is an asynchronous operation. Upon receiving a CreateInstance request, Amazon Web Services Supply Chain immediately returns the instance resource, instance ID, and the initializing state while simultaneously creating all required Amazon Web Services resources for an instance creation. You can use GetInstance to check the status of the instance. If the instance results in an unhealthy state, you need to check the error message, delete the current instance, and recreate a new one based on the mitigation from the error message.</p>

        Args:
            instance_name: <p>The AWS Supply Chain instance name.</p>
            instance_description: <p>The AWS Supply Chain instance description.</p>
            kms_key_arn: <p>The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon Web Services owned KMS key. If you don't provide anything here, AWS Supply Chain uses the Amazon Web Services owned KMS key.</p>
            web_app_dns_domain: <p>The DNS subdomain of the web app. This would be "example" in the URL "example.scn.global.on.aws". You can set this to a custom value, as long as the domain isn't already being used by someone else. The name may only include alphanumeric characters and hyphens.</p>
            tags: <p>The Amazon Web Services tags of an instance to be created.</p>
            client_token: <p>The client token for idempotency.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful CreateInstance request with all input data

            >>> await client.create_instance(instance_name='example instance name', instance_description='example instance description', kms_key_arn='arn:aws:kms:us-west-2:123456789012:key/b14ffc39-b7d4-45ab-991a-6257a7f0d24d', tags={'tagKey1': 'tagValue1'})
            Successful CreateInstance request with no input data

            >>> await client.create_instance()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.create_instance_request.CreateInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.create_instance_response.CreateInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.create_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.create_instance.async_create_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.create_instance_request.CreateInstanceRequest = {}
        if instance_name is not None:
            input_["instance_name"] = instance_name
        if instance_description is not None:
            input_["instance_description"] = instance_description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if web_app_dns_domain is not None:
            input_["web_app_dns_domain"] = web_app_dns_domain
        if tags is not None:
            input_["tags"] = tags
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

    async def get_instance(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_instance_response.GetInstanceResponse":
        """<p>Enables you to programmatically retrieve the information related to an Amazon Web Services Supply Chain instance ID.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetInstance request

            >>> await client.get_instance(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
            Successful GetInstance request with error message

            >>> await client.get_instance(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.get_instance_request.GetInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.get_instance_response.GetInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.get_instance.async_get_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_instance_request.GetInstanceRequest = {
            "instance_id": instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_instance(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        instance_name: Optional[
            "capo_supplychain.types.instance_name.InstanceName"
        ] = None,
        instance_description: Optional[
            "capo_supplychain.types.instance_description.InstanceDescription"
        ] = None,
    ) -> "capo_supplychain.types.update_instance_response.UpdateInstanceResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain instance description by providing all the relevant information such as account ID, instance ID and so on without using the AWS console.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            instance_name: <p>The AWS Supply Chain instance name.</p>
            instance_description: <p>The AWS Supply Chain instance description.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful UpdateInstance request

            >>> await client.update_instance(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793', instance_name='updated example instance name', instance_description='updated example instance description')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.update_instance_request.UpdateInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.update_instance_response.UpdateInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.update_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.update_instance.async_update_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.update_instance_request.UpdateInstanceRequest = {
            "instance_id": instance_id
        }
        if instance_name is not None:
            input_["instance_name"] = instance_name
        if instance_description is not None:
            input_["instance_description"] = instance_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_instance(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.delete_instance_response.DeleteInstanceResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain instance by deleting the KMS keys and relevant information associated with the API without using the Amazon Web Services console.</p> <p>This is an asynchronous operation. Upon receiving a DeleteInstance request, Amazon Web Services Supply Chain immediately returns a response with the instance resource, delete state while cleaning up all Amazon Web Services resources created during the instance creation process. You can use the GetInstance action to check the instance status.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful DeleteInstance request

            >>> await client.delete_instance(instance_id='9e193580-7cc5-45f7-9609-c43ba0ada793')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.delete_instance_request.DeleteInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.delete_instance_response.DeleteInstanceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.delete_instance

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.delete_instance.async_delete_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.delete_instance_request.DeleteInstanceRequest = {
            "instance_id": instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_instances(
        self,
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.instance_next_token.InstanceNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.instance_max_results.InstanceMaxResults"
        ] = None,
        instance_name_filter: Optional[
            "capo_supplychain.types.instance_name_list.InstanceNameList"
        ] = None,
        instance_state_filter: Optional[
            "capo_supplychain.types.instance_state_list.InstanceStateList"
        ] = None,
    ) -> "capo_supplychain.types.list_instances_response.ListInstancesResponse":
        """<p>List all Amazon Web Services Supply Chain instances for a specific account. Enables you to programmatically list all Amazon Web Services Supply Chain instances based on their account ID, instance name, and state of the instance (active or delete).</p>

        Args:
            next_token: <p>The pagination token to fetch the next page of instances.</p>
            max_results: <p>Specify the maximum number of instances to fetch in this paginated request.</p>
            instance_name_filter: <p>The filter to ListInstances based on their names.</p>
            instance_state_filter: <p>The filter to ListInstances based on their state.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListInstance request with no input data

            >>> await client.list_instances()
            Successful ListInstance request with filters

            >>> await client.list_instances(instance_name_filter=['example instance name'], instance_state_filter=['Active'])
            Successful ListInstance request with maxResult override

            >>> await client.list_instances(max_results=1)
            Successful ListInstance request with nextToken

            >>> await client.list_instances(next_token='AAQA-EFRSURBSGhtcng0c0dxbENwUHdnckVIbkFYNU1QVjRTZWN2ak5iMFVicC8zemlHOVF3SEpjSC9WTWJVVXBMV2Z1N3ZvZlQ0WEFBQUFmakI4QmdrcWhraUc5dzBCQndhZ2J6QnRBZ0VBTUdnR0NTcUdTSWIzRFFFSEFUQWVCZ2xnaGtnQlpRTUVBUzR3RVFRTTJibW9LemgrSWZTY0RaZEdBZ0VRZ0R2dDhsQnVGbGJ0dnFTZityWmNSWEVPbG93emJoSjhxOGNMbGQ1UGMvY0VRbWlTR3pQUFd4N2RraXY5Y0ovcS9vSmFYZVBGdWVHaU0zWmd0dz09n-rC1ejA5--7ltJxpDT2xP_i8xGqDPMOZfjpp8q6l5NuP9_bnBURvwwYhdqDriMK5_f96LuPEnPbuML-ItfgEiCcUy0p2tApvpZkZqOG5fbqP-4C5aDYPTffHLyq-MMqvfrGVJzL1nvkpZcnTkVR9VJsu5b8I0qqDW0H8EMKGgTo78U9lr4sj3Usi9VMwZxgKCBmr03HhFLYXOW--XMbIx0CTZF0fYIcRxmA_sVS6J7gpaB9yMcnzs5VUKokoA5JTcAPY5d1Y1VyE8KKxv51cfPgXw8OYCDbFQncw8mZPmE-VqxjFbksmk_FmghpPn9j2Ppoe-zr0LQ%3D', max_results=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_supplychain.types.list_instances_request.ListInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_supplychain.types.list_instances_response.ListInstancesResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_instances

            (
                output,
                http_response,
            ) = await capo_supplychain._operations.galaxy_public_api_gateway.list_instances.async_list_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_instances_request.ListInstancesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if instance_name_filter is not None:
            input_["instance_name_filter"] = instance_name_filter
        if instance_state_filter is not None:
            input_["instance_state_filter"] = instance_state_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_instances(
        self,
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.instance_next_token.InstanceNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.instance_max_results.InstanceMaxResults"
        ] = None,
        instance_name_filter: Optional[
            "capo_supplychain.types.instance_name_list.InstanceNameList"
        ] = None,
        instance_state_filter: Optional[
            "capo_supplychain.types.instance_state_list.InstanceStateList"
        ] = None,
    ) -> "AsyncIterator[capo_supplychain.types.instance.Instance]":
        _token = next_token
        while True:
            _response = await self.list_instances(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                instance_name_filter=instance_name_filter,
                instance_state_filter=instance_state_filter,
            )
            _page = _resolve_path(_response, ("instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

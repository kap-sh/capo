"""Generated from Smithy shape ``com.amazonaws.osis#AmazonOpenSearchIngestionService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_osis._auth._signers
import capo_osis._auth._sigv4
from capo_osis._auth._identity import Credentials
from capo_osis._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_osis._auth._zapros_handler import AuthMiddleware
from capo_osis._pagination import resolve_path as _resolve_path
from capo_osis._services._aws_config import aaws_config
from capo_osis._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_osis.types.blueprint_format
    import capo_osis.types.buffer_options
    import capo_osis.types.create_pipeline_endpoint_request
    import capo_osis.types.create_pipeline_endpoint_response
    import capo_osis.types.create_pipeline_request
    import capo_osis.types.create_pipeline_response
    import capo_osis.types.delete_pipeline_endpoint_request
    import capo_osis.types.delete_pipeline_endpoint_response
    import capo_osis.types.delete_pipeline_request
    import capo_osis.types.delete_pipeline_response
    import capo_osis.types.delete_resource_policy_request
    import capo_osis.types.delete_resource_policy_response
    import capo_osis.types.encryption_at_rest_options
    import capo_osis.types.get_pipeline_blueprint_request
    import capo_osis.types.get_pipeline_blueprint_response
    import capo_osis.types.get_pipeline_change_progress_request
    import capo_osis.types.get_pipeline_change_progress_response
    import capo_osis.types.get_pipeline_request
    import capo_osis.types.get_pipeline_response
    import capo_osis.types.get_resource_policy_request
    import capo_osis.types.get_resource_policy_response
    import capo_osis.types.list_pipeline_blueprints_request
    import capo_osis.types.list_pipeline_blueprints_response
    import capo_osis.types.list_pipeline_endpoint_connections_request
    import capo_osis.types.list_pipeline_endpoint_connections_response
    import capo_osis.types.list_pipeline_endpoints_request
    import capo_osis.types.list_pipeline_endpoints_response
    import capo_osis.types.list_pipelines_request
    import capo_osis.types.list_pipelines_response
    import capo_osis.types.list_tags_for_resource_request
    import capo_osis.types.list_tags_for_resource_response
    import capo_osis.types.log_publishing_options
    import capo_osis.types.max_results
    import capo_osis.types.next_token
    import capo_osis.types.pipeline_arn
    import capo_osis.types.pipeline_configuration_body
    import capo_osis.types.pipeline_endpoint
    import capo_osis.types.pipeline_endpoint_connection
    import capo_osis.types.pipeline_endpoint_id
    import capo_osis.types.pipeline_endpoint_ids_list
    import capo_osis.types.pipeline_endpoint_vpc_options
    import capo_osis.types.pipeline_name
    import capo_osis.types.pipeline_role_arn
    import capo_osis.types.pipeline_units
    import capo_osis.types.put_resource_policy_request
    import capo_osis.types.put_resource_policy_response
    import capo_osis.types.resource_policy
    import capo_osis.types.revoke_pipeline_endpoint_connections_request
    import capo_osis.types.revoke_pipeline_endpoint_connections_response
    import capo_osis.types.start_pipeline_request
    import capo_osis.types.start_pipeline_response
    import capo_osis.types.stop_pipeline_request
    import capo_osis.types.stop_pipeline_response
    import capo_osis.types.string
    import capo_osis.types.string_list
    import capo_osis.types.tag_list
    import capo_osis.types.tag_resource_request
    import capo_osis.types.tag_resource_response
    import capo_osis.types.untag_resource_request
    import capo_osis.types.untag_resource_response
    import capo_osis.types.update_pipeline_request
    import capo_osis.types.update_pipeline_response
    import capo_osis.types.validate_pipeline_request
    import capo_osis.types.validate_pipeline_response
    import capo_osis.types.vpc_options


class AsyncOSISClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncOSISClient:
    """A client for the ``OSIS`` service.

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
        self._config = AsyncOSISClientConfig(
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
        self, config_overrides: Optional[AsyncOSISClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncOSISClientConfig = config_overrides or {}
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

    async def create_pipeline(
        self,
        pipeline_name: "capo_osis.types.pipeline_name.PipelineName",
        min_units: "capo_osis.types.pipeline_units.PipelineUnits",
        max_units: "capo_osis.types.pipeline_units.PipelineUnits",
        pipeline_configuration_body: "capo_osis.types.pipeline_configuration_body.PipelineConfigurationBody",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        log_publishing_options: Optional[
            "capo_osis.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        vpc_options: Optional["capo_osis.types.vpc_options.VpcOptions"] = None,
        buffer_options: Optional["capo_osis.types.buffer_options.BufferOptions"] = None,
        encryption_at_rest_options: Optional[
            "capo_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        tags: Optional["capo_osis.types.tag_list.TagList"] = None,
        pipeline_role_arn: Optional[
            "capo_osis.types.pipeline_role_arn.PipelineRoleArn"
        ] = None,
    ) -> "capo_osis.types.create_pipeline_response.CreatePipelineResponse":
        r"""<p>Creates an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html">Creating Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_name: <p>The name of the OpenSearch Ingestion pipeline to create. Pipeline names are unique across the pipelines owned by an account within an Amazon Web Services Region.</p>
            min_units: <p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>
            max_units: <p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs).</p>
            pipeline_configuration_body: <p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>
            log_publishing_options: <p>Key-value pairs to configure log publishing.</p>
            vpc_options: <p>Container for the values required to configure VPC access for the pipeline. If you don't specify these values, OpenSearch Ingestion creates the pipeline with a public endpoint.</p>
            buffer_options: <p>Key-value pairs to configure persistent buffering for the pipeline.</p>
            encryption_at_rest_options: <p>Key-value pairs to configure encryption for data that is written to a persistent buffer.</p>
            tags: <p>List of tags to add to the pipeline upon creation.</p>
            pipeline_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access Amazon Web Services resources.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>You attempted to create a resource that already exists.</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.create_pipeline_request.CreatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.create_pipeline_response.CreatePipelineResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.create_pipeline

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.create_pipeline.async_create_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.create_pipeline_request.CreatePipelineRequest = {
            "pipeline_name": pipeline_name,
            "min_units": min_units,
            "max_units": max_units,
            "pipeline_configuration_body": pipeline_configuration_body,
        }
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if buffer_options is not None:
            input_["buffer_options"] = buffer_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if tags is not None:
            input_["tags"] = tags
        if pipeline_role_arn is not None:
            input_["pipeline_role_arn"] = pipeline_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_pipeline_endpoint(
        self,
        pipeline_arn: "capo_osis.types.pipeline_arn.PipelineArn",
        vpc_options: "capo_osis.types.pipeline_endpoint_vpc_options.PipelineEndpointVpcOptions",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.create_pipeline_endpoint_response.CreatePipelineEndpointResponse":
        """<p>Creates a VPC endpoint for an OpenSearch Ingestion pipeline. Pipeline endpoints allow you to ingest data from your VPC into pipelines that you have access to.</p>

        Args:
            pipeline_arn: <p>The Amazon Resource Name (ARN) of the pipeline to create the endpoint for.</p>
            vpc_options: <p>Container for the VPC configuration for the pipeline endpoint, including subnet IDs and security group IDs.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.create_pipeline_endpoint_request.CreatePipelineEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.create_pipeline_endpoint_response.CreatePipelineEndpointResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.create_pipeline_endpoint

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.create_pipeline_endpoint.async_create_pipeline_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.create_pipeline_endpoint_request.CreatePipelineEndpointRequest = {
            "pipeline_arn": pipeline_arn,
            "vpc_options": vpc_options,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pipeline(
        self,
        pipeline_name: "capo_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.delete_pipeline_response.DeletePipelineResponse":
        """<p>Deletes an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/delete-pipeline.html">Deleting Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to delete.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.delete_pipeline_request.DeletePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.delete_pipeline_response.DeletePipelineResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.delete_pipeline

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.delete_pipeline.async_delete_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.delete_pipeline_request.DeletePipelineRequest = {
            "pipeline_name": pipeline_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pipeline_endpoint(
        self,
        endpoint_id: "capo_osis.types.pipeline_endpoint_id.PipelineEndpointId",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.delete_pipeline_endpoint_response.DeletePipelineEndpointResponse":
        """<p>Deletes a VPC endpoint for an OpenSearch Ingestion pipeline.</p>

        Args:
            endpoint_id: <p>The unique identifier of the pipeline endpoint to delete.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.delete_pipeline_endpoint_request.DeletePipelineEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.delete_pipeline_endpoint_response.DeletePipelineEndpointResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.delete_pipeline_endpoint

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.delete_pipeline_endpoint.async_delete_pipeline_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.delete_pipeline_endpoint_request.DeletePipelineEndpointRequest = {
            "endpoint_id": endpoint_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_osis.types.pipeline_arn.PipelineArn",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a resource-based policy from an OpenSearch Ingestion resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to delete the policy.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pipeline(
        self,
        pipeline_name: "capo_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.get_pipeline_response.GetPipelineResponse":
        """<p>Retrieves information about an OpenSearch Ingestion pipeline.</p>

        Args:
            pipeline_name: <p>The name of the pipeline.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.get_pipeline_request.GetPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.get_pipeline_response.GetPipelineResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.get_pipeline

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.get_pipeline.async_get_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.get_pipeline_request.GetPipelineRequest = {
            "pipeline_name": pipeline_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pipeline_blueprint(
        self,
        blueprint_name: "capo_osis.types.string.String",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        format: Optional["capo_osis.types.blueprint_format.BlueprintFormat"] = None,
    ) -> "capo_osis.types.get_pipeline_blueprint_response.GetPipelineBlueprintResponse":
        """<p>Retrieves information about a specific blueprint for OpenSearch Ingestion. Blueprints are templates for the configuration needed for a <code>CreatePipeline</code> request. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#pipeline-blueprint">Using blueprints to create a pipeline</a>.</p>

        Args:
            blueprint_name: <p>The name of the blueprint to retrieve.</p>
            format: <p>The format format of the blueprint to retrieve.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.get_pipeline_blueprint_request.GetPipelineBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.get_pipeline_blueprint_response.GetPipelineBlueprintResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.get_pipeline_blueprint

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.get_pipeline_blueprint.async_get_pipeline_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.get_pipeline_blueprint_request.GetPipelineBlueprintRequest = {
            "blueprint_name": blueprint_name
        }
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pipeline_change_progress(
        self,
        pipeline_name: "capo_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.get_pipeline_change_progress_response.GetPipelineChangeProgressResponse":
        """<p>Returns progress information for the current change happening on an OpenSearch Ingestion pipeline. Currently, this operation only returns information when a pipeline is being created.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#get-pipeline-progress">Tracking the status of pipeline creation</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.get_pipeline_change_progress_request.GetPipelineChangeProgressRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.get_pipeline_change_progress_response.GetPipelineChangeProgressResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.get_pipeline_change_progress

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.get_pipeline_change_progress.async_get_pipeline_change_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.get_pipeline_change_progress_request.GetPipelineChangeProgressRequest = {
            "pipeline_name": pipeline_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_osis.types.pipeline_arn.PipelineArn",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy attached to an OpenSearch Ingestion resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to retrieve the policy.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_pipeline_blueprints(
        self, *, config_overrides: Optional[AsyncOSISClientConfig] = None
    ) -> "capo_osis.types.list_pipeline_blueprints_response.ListPipelineBlueprintsResponse":
        """<p>Retrieves a list of all available blueprints for Data Prepper. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#pipeline-blueprint">Using blueprints to create a pipeline</a>.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>An invalid pagination token provided in the request.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.list_pipeline_blueprints_request.ListPipelineBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.list_pipeline_blueprints_response.ListPipelineBlueprintsResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.list_pipeline_blueprints

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.list_pipeline_blueprints.async_list_pipeline_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.list_pipeline_blueprints_request.ListPipelineBlueprintsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_pipeline_endpoint_connections(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["capo_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_osis.types.next_token.NextToken"] = None,
    ) -> "capo_osis.types.list_pipeline_endpoint_connections_response.ListPipelineEndpointConnectionsResponse":
        """<p>Lists the pipeline endpoints connected to pipelines in your account.</p>

        Args:
            max_results: <p>The maximum number of pipeline endpoint connections to return in the response.</p>
            next_token: <p>If your initial <code>ListPipelineEndpointConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPipelineEndpointConnections</code> operations, which returns results in the next page.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.list_pipeline_endpoint_connections_request.ListPipelineEndpointConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.list_pipeline_endpoint_connections_response.ListPipelineEndpointConnectionsResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoint_connections

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoint_connections.async_list_pipeline_endpoint_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.list_pipeline_endpoint_connections_request.ListPipelineEndpointConnectionsRequest = {}
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

    async def iter_list_pipeline_endpoint_connections(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["capo_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_osis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_osis.types.pipeline_endpoint_connection.PipelineEndpointConnection]":
        _token = next_token
        while True:
            _response = await self.list_pipeline_endpoint_connections(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pipeline_endpoint_connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipeline_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["capo_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_osis.types.next_token.NextToken"] = None,
    ) -> (
        "capo_osis.types.list_pipeline_endpoints_response.ListPipelineEndpointsResponse"
    ):
        """<p>Lists all pipeline endpoints in your account.</p>

        Args:
            max_results: <p>The maximum number of pipeline endpoints to return in the response.</p>
            next_token: <p>If your initial <code>ListPipelineEndpoints</code> operation returns a <code>NextToken</code>, you can include the returned <code>NextToken</code> in subsequent <code>ListPipelineEndpoints</code> operations, which returns results in the next page.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.list_pipeline_endpoints_request.ListPipelineEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.list_pipeline_endpoints_response.ListPipelineEndpointsResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoints

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.list_pipeline_endpoints.async_list_pipeline_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.list_pipeline_endpoints_request.ListPipelineEndpointsRequest = {}
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

    async def iter_list_pipeline_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["capo_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_osis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_osis.types.pipeline_endpoint.PipelineEndpoint]":
        _token = next_token
        while True:
            _response = await self.list_pipeline_endpoints(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pipeline_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["capo_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_osis.types.next_token.NextToken"] = None,
    ) -> "capo_osis.types.list_pipelines_response.ListPipelinesResponse":
        """<p>Lists all OpenSearch Ingestion pipelines in the current Amazon Web Services account and Region. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/list-pipeline.html">Viewing Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListPipelines</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPipelines</code> operations, which returns results in the next page.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>An invalid pagination token provided in the request.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.list_pipelines_request.ListPipelinesRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.list_pipelines_response.ListPipelinesResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.list_pipelines

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.list_pipelines.async_list_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.list_pipelines_request.ListPipelinesRequest = {}
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

    async def iter_list_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        max_results: Optional["capo_osis.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_osis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_osis.types.list_pipelines_response.ListPipelinesResponse]":
        _token = next_token
        while True:
            _response = await self.list_pipelines(
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
        arn: "capo_osis.types.pipeline_arn.PipelineArn",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all resource tags associated with an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html">Tagging Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pipeline to retrieve tags for.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_osis.types.pipeline_arn.PipelineArn",
        policy: "capo_osis.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Attaches a resource-based policy to an OpenSearch Ingestion resource. Resource-based policies grant permissions to principals to perform actions on the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to attach the policy to.</p>
            policy: <p>The resource-based policy document in JSON format.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_pipeline_endpoint_connections(
        self,
        pipeline_arn: "capo_osis.types.pipeline_arn.PipelineArn",
        endpoint_ids: "capo_osis.types.pipeline_endpoint_ids_list.PipelineEndpointIdsList",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.revoke_pipeline_endpoint_connections_response.RevokePipelineEndpointConnectionsResponse":
        """<p>Revokes pipeline endpoints from specified endpoint IDs.</p>

        Args:
            pipeline_arn: <p>The Amazon Resource Name (ARN) of the pipeline from which to revoke endpoint connections.</p>
            endpoint_ids: <p>A list of endpoint IDs for which to revoke access to the pipeline.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.revoke_pipeline_endpoint_connections_request.RevokePipelineEndpointConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.revoke_pipeline_endpoint_connections_response.RevokePipelineEndpointConnectionsResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.revoke_pipeline_endpoint_connections

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.revoke_pipeline_endpoint_connections.async_revoke_pipeline_endpoint_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.revoke_pipeline_endpoint_connections_request.RevokePipelineEndpointConnectionsRequest = {
            "pipeline_arn": pipeline_arn,
            "endpoint_ids": endpoint_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_pipeline(
        self,
        pipeline_name: "capo_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.start_pipeline_response.StartPipelineResponse":
        """<p>Starts an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--stop-start.html#pipeline--start">Starting an OpenSearch Ingestion pipeline</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to start.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.start_pipeline_request.StartPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.start_pipeline_response.StartPipelineResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.start_pipeline

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.start_pipeline.async_start_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.start_pipeline_request.StartPipelineRequest = {
            "pipeline_name": pipeline_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_pipeline(
        self,
        pipeline_name: "capo_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.stop_pipeline_response.StopPipelineResponse":
        """<p>Stops an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline--stop-start.html#pipeline--stop">Stopping an OpenSearch Ingestion pipeline</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to stop.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.stop_pipeline_request.StopPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.stop_pipeline_response.StopPipelineResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.stop_pipeline

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.stop_pipeline.async_stop_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.stop_pipeline_request.StopPipelineRequest = {
            "pipeline_name": pipeline_name
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
        arn: "capo_osis.types.pipeline_arn.PipelineArn",
        tags: "capo_osis.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.tag_resource_response.TagResourceResponse":
        """<p>Tags an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html">Tagging Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pipeline to tag.</p>
            tags: <p>The list of key-value tags to add to the pipeline.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.limit_exceeded_exception.LimitExceededException: <p>You attempted to create more than the allowed number of tags.</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
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
        arn: "capo_osis.types.pipeline_arn.PipelineArn",
        tag_keys: "capo_osis.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-pipeline.html">Tagging Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pipeline to remove tags from.</p>
            tag_keys: <p>The tag keys to remove.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_pipeline(
        self,
        pipeline_name: "capo_osis.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
        min_units: Optional["capo_osis.types.pipeline_units.PipelineUnits"] = None,
        max_units: Optional["capo_osis.types.pipeline_units.PipelineUnits"] = None,
        pipeline_configuration_body: Optional[
            "capo_osis.types.pipeline_configuration_body.PipelineConfigurationBody"
        ] = None,
        log_publishing_options: Optional[
            "capo_osis.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        buffer_options: Optional["capo_osis.types.buffer_options.BufferOptions"] = None,
        encryption_at_rest_options: Optional[
            "capo_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        pipeline_role_arn: Optional[
            "capo_osis.types.pipeline_role_arn.PipelineRoleArn"
        ] = None,
    ) -> "capo_osis.types.update_pipeline_response.UpdatePipelineResponse":
        r"""<p>Updates an OpenSearch Ingestion pipeline. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/update-pipeline.html">Updating Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to update.</p>
            min_units: <p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>
            max_units: <p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs)</p>
            pipeline_configuration_body: <p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>
            log_publishing_options: <p>Key-value pairs to configure log publishing.</p>
            buffer_options: <p>Key-value pairs to configure persistent buffering for the pipeline.</p>
            encryption_at_rest_options: <p>Key-value pairs to configure encryption for data that is written to a persistent buffer.</p>
            pipeline_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access Amazon Web Services resources.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.conflict_exception.ConflictException: <p>The client attempted to remove a resource that is currently in use.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.resource_not_found_exception.ResourceNotFoundException: <p>You attempted to access or delete a resource that does not exist.</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.update_pipeline_request.UpdatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.update_pipeline_response.UpdatePipelineResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.update_pipeline

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.update_pipeline.async_update_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.update_pipeline_request.UpdatePipelineRequest = {
            "pipeline_name": pipeline_name
        }
        if min_units is not None:
            input_["min_units"] = min_units
        if max_units is not None:
            input_["max_units"] = max_units
        if pipeline_configuration_body is not None:
            input_["pipeline_configuration_body"] = pipeline_configuration_body
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if buffer_options is not None:
            input_["buffer_options"] = buffer_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if pipeline_role_arn is not None:
            input_["pipeline_role_arn"] = pipeline_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def validate_pipeline(
        self,
        pipeline_configuration_body: "capo_osis.types.pipeline_configuration_body.PipelineConfigurationBody",
        *,
        config_overrides: Optional[AsyncOSISClientConfig] = None,
    ) -> "capo_osis.types.validate_pipeline_response.ValidatePipelineResponse":
        r"""<p>Checks whether an OpenSearch Ingestion pipeline configuration is valid prior to creation. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html">Creating Amazon OpenSearch Ingestion pipelines</a>.</p>

        Args:
            pipeline_configuration_body: <p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>

        Raises:
            capo_osis.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to access the resource.</p>
            capo_osis.errors.disabled_operation_exception.DisabledOperationException: <p>Exception is thrown when an operation has been disabled.</p>
            capo_osis.errors.internal_exception.InternalException: <p>The request failed because of an unknown error, exception, or failure (the failure is internal to the service).</p>
            capo_osis.errors.validation_exception.ValidationException: <p>An exception for missing or invalid input fields.</p>
            capo_osis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_osis.types.validate_pipeline_request.ValidatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_osis.types.validate_pipeline_response.ValidatePipelineResponse"
        ]:
            import capo_osis._operations.amazon_open_search_ingestion_service.validate_pipeline

            (
                output,
                http_response,
            ) = await capo_osis._operations.amazon_open_search_ingestion_service.validate_pipeline.async_validate_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_osis.types.validate_pipeline_request.ValidatePipelineRequest = {
            "pipeline_configuration_body": pipeline_configuration_body
        }

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

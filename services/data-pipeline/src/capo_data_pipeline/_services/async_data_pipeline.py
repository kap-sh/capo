"""Generated from Smithy shape ``com.amazonaws.datapipeline#DataPipeline``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_data_pipeline._auth._signers
import capo_data_pipeline._auth._sigv4
from capo_data_pipeline._auth._identity import Credentials
from capo_data_pipeline._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_data_pipeline._auth._zapros_handler import AuthMiddleware
from capo_data_pipeline._pagination import resolve_path as _resolve_path
from capo_data_pipeline._services._aws_config import aaws_config
from capo_data_pipeline._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_data_pipeline.types.activate_pipeline_input
    import capo_data_pipeline.types.activate_pipeline_output
    import capo_data_pipeline.types.add_tags_input
    import capo_data_pipeline.types.add_tags_output
    import capo_data_pipeline.types.boolean
    import capo_data_pipeline.types.cancel_active
    import capo_data_pipeline.types.create_pipeline_input
    import capo_data_pipeline.types.create_pipeline_output
    import capo_data_pipeline.types.deactivate_pipeline_input
    import capo_data_pipeline.types.deactivate_pipeline_output
    import capo_data_pipeline.types.delete_pipeline_input
    import capo_data_pipeline.types.describe_objects_input
    import capo_data_pipeline.types.describe_objects_output
    import capo_data_pipeline.types.describe_pipelines_input
    import capo_data_pipeline.types.describe_pipelines_output
    import capo_data_pipeline.types.error_message
    import capo_data_pipeline.types.evaluate_expression_input
    import capo_data_pipeline.types.evaluate_expression_output
    import capo_data_pipeline.types.field_list
    import capo_data_pipeline.types.get_pipeline_definition_input
    import capo_data_pipeline.types.get_pipeline_definition_output
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.id_list
    import capo_data_pipeline.types.instance_identity
    import capo_data_pipeline.types.int
    import capo_data_pipeline.types.list_pipelines_input
    import capo_data_pipeline.types.list_pipelines_output
    import capo_data_pipeline.types.long_string
    import capo_data_pipeline.types.parameter_object_list
    import capo_data_pipeline.types.parameter_value_list
    import capo_data_pipeline.types.pipeline_id_name
    import capo_data_pipeline.types.pipeline_object
    import capo_data_pipeline.types.pipeline_object_list
    import capo_data_pipeline.types.poll_for_task_input
    import capo_data_pipeline.types.poll_for_task_output
    import capo_data_pipeline.types.put_pipeline_definition_input
    import capo_data_pipeline.types.put_pipeline_definition_output
    import capo_data_pipeline.types.query
    import capo_data_pipeline.types.query_objects_input
    import capo_data_pipeline.types.query_objects_output
    import capo_data_pipeline.types.remove_tags_input
    import capo_data_pipeline.types.remove_tags_output
    import capo_data_pipeline.types.report_task_progress_input
    import capo_data_pipeline.types.report_task_progress_output
    import capo_data_pipeline.types.report_task_runner_heartbeat_input
    import capo_data_pipeline.types.report_task_runner_heartbeat_output
    import capo_data_pipeline.types.set_status_input
    import capo_data_pipeline.types.set_task_status_input
    import capo_data_pipeline.types.set_task_status_output
    import capo_data_pipeline.types.string
    import capo_data_pipeline.types.string_list
    import capo_data_pipeline.types.tag_list
    import capo_data_pipeline.types.task_id
    import capo_data_pipeline.types.task_status
    import capo_data_pipeline.types.timestamp
    import capo_data_pipeline.types.validate_pipeline_definition_input
    import capo_data_pipeline.types.validate_pipeline_definition_output


class AsyncDataPipelineClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDataPipelineClient:
    """A client for the ``DataPipeline`` service.

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
        self._config = AsyncDataPipelineClientConfig(
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
        self, config_overrides: Optional[AsyncDataPipelineClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDataPipelineClientConfig = config_overrides or {}
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

    async def activate_pipeline(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        parameter_values: Optional[
            "capo_data_pipeline.types.parameter_value_list.ParameterValueList"
        ] = None,
        start_timestamp: Optional[
            "capo_data_pipeline.types.timestamp.timestamp"
        ] = None,
    ) -> "capo_data_pipeline.types.activate_pipeline_output.ActivatePipelineOutput":
        """<p>Validates the specified pipeline and starts processing pipeline tasks. If the pipeline does not pass validation, activation fails.</p> <p>If you need to pause the pipeline to investigate an issue with a component, such as a data source or script, call <a>DeactivatePipeline</a>.</p> <p>To activate a finished pipeline, modify the end date for the pipeline and then activate it.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.ActivatePipeline Content-Length: 39 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE"} </request> <response> HTTP/1.1 200 x-amzn-RequestId: ee19d5bf-074e-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 2 Date: Mon, 12 Nov 2012 17:50:53 GMT {} </response> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            parameter_values: <p>A list of parameter values to pass to the pipeline at activation.</p>
            start_timestamp: <p>The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.activate_pipeline_input.ActivatePipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.activate_pipeline_output.ActivatePipelineOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.activate_pipeline

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.activate_pipeline.async_activate_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.activate_pipeline_input.ActivatePipelineInput = {
            "pipeline_id": pipeline_id
        }
        if parameter_values is not None:
            input_["parameter_values"] = parameter_values
        if start_timestamp is not None:
            input_["start_timestamp"] = start_timestamp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_tags(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        tags: "capo_data_pipeline.types.tag_list.tagList",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
    ) -> "capo_data_pipeline.types.add_tags_output.AddTagsOutput":
        """<p>Adds or modifies tags for the specified pipeline.</p>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            tags: <p>The tags to add, as key/value pairs.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.add_tags_input.AddTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.add_tags_output.AddTagsOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.add_tags

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.add_tags.async_add_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.add_tags_input.AddTagsInput = {
            "pipeline_id": pipeline_id,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_pipeline(
        self,
        name: "capo_data_pipeline.types.id.id",
        unique_id: "capo_data_pipeline.types.id.id",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        description: Optional["capo_data_pipeline.types.string.string"] = None,
        tags: Optional["capo_data_pipeline.types.tag_list.tagList"] = None,
    ) -> "capo_data_pipeline.types.create_pipeline_output.CreatePipelineOutput":
        """<p>Creates a new, empty pipeline. Use <a>PutPipelineDefinition</a> to populate the pipeline.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.CreatePipeline Content-Length: 91 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"name": "myPipeline", "uniqueId": "123456789", "description": "This is my first pipeline"} </request> <response> HTTP/1.1 200 x-amzn-RequestId: b16911ce-0774-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 40 Date: Mon, 12 Nov 2012 17:50:53 GMT {"pipelineId": "df-06372391ZG65EXAMPLE"} </response> </examples>

        Args:
            name: <p>The name for the pipeline. You can use the same name for multiple pipelines associated with your AWS account, because AWS Data Pipeline assigns each pipeline a unique pipeline identifier.</p>
            unique_id: <p>A unique identifier. This identifier is not the same as the pipeline identifier assigned by AWS Data Pipeline. You are responsible for defining the format and ensuring the uniqueness of this identifier. You use this parameter to ensure idempotency during repeated calls to <code>CreatePipeline</code>. For example, if the first call to <code>CreatePipeline</code> does not succeed, you can pass in the same unique identifier and pipeline name combination on a subsequent call to <code>CreatePipeline</code>. <code>CreatePipeline</code> ensures that if a pipeline already exists with the same name and unique identifier, a new pipeline is not created. Instead, you'll receive the pipeline identifier from the previous attempt. The uniqueness of the name and unique identifier combination is scoped to the AWS account or IAM user credentials.</p>
            description: <p>The description for the pipeline.</p>
            tags: <p>A list of tags to associate with the pipeline at creation. Tags let you control access to pipelines. For more information, see <a href="http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html">Controlling User Access to Pipelines</a> in the <i>AWS Data Pipeline Developer Guide</i>.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.create_pipeline_input.CreatePipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.create_pipeline_output.CreatePipelineOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.create_pipeline

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.create_pipeline.async_create_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.create_pipeline_input.CreatePipelineInput = {
            "name": name,
            "unique_id": unique_id,
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

    async def deactivate_pipeline(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        cancel_active: Optional[
            "capo_data_pipeline.types.cancel_active.cancelActive"
        ] = None,
    ) -> "capo_data_pipeline.types.deactivate_pipeline_output.DeactivatePipelineOutput":
        """<p>Deactivates the specified running pipeline. The pipeline is set to the <code>DEACTIVATING</code> state until the deactivation process completes.</p> <p>To resume a deactivated pipeline, use <a>ActivatePipeline</a>. By default, the pipeline resumes from the last completed execution. Optionally, you can specify the date and time to resume the pipeline.</p>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            cancel_active: <p>Indicates whether to cancel any running objects. The default is true, which sets the state of any running objects to <code>CANCELED</code>. If this value is false, the pipeline is deactivated after all running objects finish.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.deactivate_pipeline_input.DeactivatePipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.deactivate_pipeline_output.DeactivatePipelineOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.deactivate_pipeline

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.deactivate_pipeline.async_deactivate_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.deactivate_pipeline_input.DeactivatePipelineInput = {
            "pipeline_id": pipeline_id
        }
        if cancel_active is not None:
            input_["cancel_active"] = cancel_active

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pipeline(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
    ) -> None:
        """<p>Deletes a pipeline, its pipeline definition, and its run history. AWS Data Pipeline attempts to cancel instances associated with the pipeline that are currently being processed by task runners.</p> <p>Deleting a pipeline cannot be undone. You cannot query or restore a deleted pipeline. To temporarily pause a pipeline instead of deleting it, call <a>SetStatus</a> with the status set to <code>PAUSE</code> on individual components. Components that are paused by <a>SetStatus</a> can be resumed.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.DeletePipeline Content-Length: 50 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE"} </request> <response> x-amzn-RequestId: b7a88c81-0754-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 0 Date: Mon, 12 Nov 2012 17:50:53 GMT Unexpected response: 200, OK, undefined </response> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.delete_pipeline_input.DeletePipelineInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_data_pipeline._operations.data_pipeline.delete_pipeline

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.delete_pipeline.async_delete_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.delete_pipeline_input.DeletePipelineInput = {
            "pipeline_id": pipeline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_objects(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        object_ids: "capo_data_pipeline.types.id_list.idList",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        evaluate_expressions: Optional[
            "capo_data_pipeline.types.boolean.boolean"
        ] = None,
        marker: Optional["capo_data_pipeline.types.string.string"] = None,
    ) -> "capo_data_pipeline.types.describe_objects_output.DescribeObjectsOutput":
        """<p>Gets the object definitions for a set of objects associated with the pipeline. Object definitions are composed of a set of fields that define the properties of the object.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.DescribeObjects Content-Length: 98 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE", "objectIds": ["Schedule"], "evaluateExpressions": true} </request> <response> x-amzn-RequestId: 4c18ea5d-0777-11e2-8a14-21bb8a1f50ef Content-Type: application/x-amz-json-1.1 Content-Length: 1488 Date: Mon, 12 Nov 2012 17:50:53 GMT {"hasMoreResults": false, "pipelineObjects": [ {"fields": [ {"key": "startDateTime", "stringValue": "2012-12-12T00:00:00"}, {"key": "parent", "refValue": "Default"}, {"key": "@sphere", "stringValue": "COMPONENT"}, {"key": "type", "stringValue": "Schedule"}, {"key": "period", "stringValue": "1 hour"}, {"key": "endDateTime", "stringValue": "2012-12-21T18:00:00"}, {"key": "@version", "stringValue": "1"}, {"key": "@status", "stringValue": "PENDING"}, {"key": "@pipelineId", "stringValue": "df-06372391ZG65EXAMPLE"} ], "id": "Schedule", "name": "Schedule"} ] } </response> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline that contains the object definitions.</p>
            object_ids: <p>The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to <code>DescribeObjects</code>.</p>
            evaluate_expressions: <p>Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.</p>
            marker: <p>The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call <code>DescribeObjects</code> with the marker value from the previous call to retrieve the next set of results.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.describe_objects_input.DescribeObjectsInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.describe_objects_output.DescribeObjectsOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.describe_objects

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.describe_objects.async_describe_objects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.describe_objects_input.DescribeObjectsInput = {
            "pipeline_id": pipeline_id,
            "object_ids": object_ids,
        }
        if evaluate_expressions is not None:
            input_["evaluate_expressions"] = evaluate_expressions
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_objects(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        object_ids: "capo_data_pipeline.types.id_list.idList",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        evaluate_expressions: Optional[
            "capo_data_pipeline.types.boolean.boolean"
        ] = None,
        marker: Optional["capo_data_pipeline.types.string.string"] = None,
    ) -> "AsyncIterator[capo_data_pipeline.types.pipeline_object.PipelineObject]":
        _token = marker
        while True:
            _response = await self.describe_objects(
                pipeline_id,
                object_ids,
                config_overrides=config_overrides,
                evaluate_expressions=evaluate_expressions,
                marker=_token,
            )
            _page = _resolve_path(_response, ("pipeline_objects",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_pipelines(
        self,
        pipeline_ids: "capo_data_pipeline.types.id_list.idList",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
    ) -> "capo_data_pipeline.types.describe_pipelines_output.DescribePipelinesOutput":
        """<p>Retrieves metadata about one or more pipelines. The information retrieved includes the name of the pipeline, the pipeline identifier, its current state, and the user account that owns the pipeline. Using account credentials, you can retrieve metadata about pipelines that you or your IAM users have created. If you are using an IAM user account, you can retrieve metadata about only those pipelines for which you have read permissions.</p> <p>To retrieve the full pipeline definition instead of metadata about the pipeline, call <a>GetPipelineDefinition</a>.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.DescribePipelines Content-Length: 70 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineIds": ["df-08785951KAKJEXAMPLE"] } </request> <response> x-amzn-RequestId: 02870eb7-0736-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 767 Date: Mon, 12 Nov 2012 17:50:53 GMT {"pipelineDescriptionList": [ {"description": "This is my first pipeline", "fields": [ {"key": "@pipelineState", "stringValue": "SCHEDULED"}, {"key": "description", "stringValue": "This is my first pipeline"}, {"key": "name", "stringValue": "myPipeline"}, {"key": "@creationTime", "stringValue": "2012-12-13T01:24:06"}, {"key": "@id", "stringValue": "df-0937003356ZJEXAMPLE"}, {"key": "@sphere", "stringValue": "PIPELINE"}, {"key": "@version", "stringValue": "1"}, {"key": "@userId", "stringValue": "924374875933"}, {"key": "@accountId", "stringValue": "924374875933"}, {"key": "uniqueId", "stringValue": "1234567890"} ], "name": "myPipeline", "pipelineId": "df-0937003356ZJEXAMPLE"} ] } </response> </examples>

        Args:
            pipeline_ids: <p>The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call <a>ListPipelines</a>.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.describe_pipelines_input.DescribePipelinesInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.describe_pipelines_output.DescribePipelinesOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.describe_pipelines

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.describe_pipelines.async_describe_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.describe_pipelines_input.DescribePipelinesInput = {
            "pipeline_ids": pipeline_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def evaluate_expression(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        object_id: "capo_data_pipeline.types.id.id",
        expression: "capo_data_pipeline.types.long_string.longString",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
    ) -> "capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput":
        """<p>Task runners call <code>EvaluateExpression</code> to evaluate a string in the context of the specified object. For example, a task runner can evaluate SQL queries stored in Amazon S3.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.DescribePipelines Content-Length: 164 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-08785951KAKJEXAMPLE", "objectId": "Schedule", "expression": "Transform started at #{startDateTime} and finished at #{endDateTime}"} </request> <response> x-amzn-RequestId: 02870eb7-0736-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 103 Date: Mon, 12 Nov 2012 17:50:53 GMT {"evaluatedExpression": "Transform started at 2012-12-12T00:00:00 and finished at 2012-12-21T18:00:00"} </response> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            object_id: <p>The ID of the object.</p>
            expression: <p>The expression to evaluate.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.task_not_found_exception.TaskNotFoundException: <p>The specified task was not found. </p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.evaluate_expression_input.EvaluateExpressionInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.evaluate_expression_output.EvaluateExpressionOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.evaluate_expression

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.evaluate_expression.async_evaluate_expression(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.evaluate_expression_input.EvaluateExpressionInput = {
            "pipeline_id": pipeline_id,
            "object_id": object_id,
            "expression": expression,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pipeline_definition(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        version: Optional["capo_data_pipeline.types.string.string"] = None,
    ) -> "capo_data_pipeline.types.get_pipeline_definition_output.GetPipelineDefinitionOutput":
        """<p>Gets the definition of the specified pipeline. You can call <code>GetPipelineDefinition</code> to retrieve the pipeline definition that you provided using <a>PutPipelineDefinition</a>.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.GetPipelineDefinition Content-Length: 40 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE"} </request> <response> x-amzn-RequestId: e28309e5-0776-11e2-8a14-21bb8a1f50ef Content-Type: application/x-amz-json-1.1 Content-Length: 890 Date: Mon, 12 Nov 2012 17:50:53 GMT {"pipelineObjects": [ {"fields": [ {"key": "workerGroup", "stringValue": "workerGroup"} ], "id": "Default", "name": "Default"}, {"fields": [ {"key": "startDateTime", "stringValue": "2012-09-25T17:00:00"}, {"key": "type", "stringValue": "Schedule"}, {"key": "period", "stringValue": "1 hour"}, {"key": "endDateTime", "stringValue": "2012-09-25T18:00:00"} ], "id": "Schedule", "name": "Schedule"}, {"fields": [ {"key": "schedule", "refValue": "Schedule"}, {"key": "command", "stringValue": "echo hello"}, {"key": "parent", "refValue": "Default"}, {"key": "type", "stringValue": "ShellCommandActivity"} ], "id": "SayHello", "name": "SayHello"} ] } </response> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            version: <p>The version of the pipeline definition to retrieve. Set this parameter to <code>latest</code> (default) to use the last definition saved to the pipeline or <code>active</code> to use the last definition that was activated.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.get_pipeline_definition_input.GetPipelineDefinitionInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.get_pipeline_definition_output.GetPipelineDefinitionOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.get_pipeline_definition

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.get_pipeline_definition.async_get_pipeline_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.get_pipeline_definition_input.GetPipelineDefinitionInput = {
            "pipeline_id": pipeline_id
        }
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        marker: Optional["capo_data_pipeline.types.string.string"] = None,
    ) -> "capo_data_pipeline.types.list_pipelines_output.ListPipelinesOutput":
        """<p>Lists the pipeline identifiers for all active pipelines that you have permission to access.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.ListPipelines Content-Length: 14 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {}</request> <response> Status: x-amzn-RequestId: b3104dc5-0734-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 39 Date: Mon, 12 Nov 2012 17:50:53 GMT {"PipelineIdList": [ {"id": "df-08785951KAKJEXAMPLE", "name": "MyPipeline"}, {"id": "df-08662578ISYEXAMPLE", "name": "MySecondPipeline"} ] }</response> </examples>

        Args:
            marker: <p>The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call <code>ListPipelines</code> with the marker value from the previous call to retrieve the next set of results.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.list_pipelines_input.ListPipelinesInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.list_pipelines_output.ListPipelinesOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.list_pipelines

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.list_pipelines.async_list_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.list_pipelines_input.ListPipelinesInput = {}
        if marker is not None:
            input_["marker"] = marker

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
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        marker: Optional["capo_data_pipeline.types.string.string"] = None,
    ) -> "AsyncIterator[capo_data_pipeline.types.pipeline_id_name.PipelineIdName]":
        _token = marker
        while True:
            _response = await self.list_pipelines(
                config_overrides=config_overrides,
                marker=_token,
            )
            _page = _resolve_path(_response, ("pipeline_id_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def poll_for_task(
        self,
        worker_group: "capo_data_pipeline.types.string.string",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        hostname: Optional["capo_data_pipeline.types.id.id"] = None,
        instance_identity: Optional[
            "capo_data_pipeline.types.instance_identity.InstanceIdentity"
        ] = None,
    ) -> "capo_data_pipeline.types.poll_for_task_output.PollForTaskOutput":
        """<p>Task runners call <code>PollForTask</code> to receive a task to perform from AWS Data Pipeline. The task runner specifies which tasks it can perform by setting a value for the <code>workerGroup</code> parameter. The task returned can come from any of the pipelines that match the <code>workerGroup</code> value passed in by the task runner and that was launched using the IAM user credentials specified by the task runner.</p> <p>If tasks are ready in the work queue, <code>PollForTask</code> returns a response immediately. If no tasks are available in the queue, <code>PollForTask</code> uses long-polling and holds on to a poll connection for up to a 90 seconds, during which time the first newly scheduled task is handed to the task runner. To accomodate this, set the socket timeout in your task runner to 90 seconds. The task runner should not call <code>PollForTask</code> again on the same <code>workerGroup</code> until it receives a response, and this can take up to 90 seconds. </p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.PollForTask Content-Length: 59 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"workerGroup": "MyworkerGroup", "hostname": "example.com"} </request> <response> x-amzn-RequestId: 41c713d2-0775-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 39 Date: Mon, 12 Nov 2012 17:50:53 GMT {"taskObject": {"attemptId": "@SayHello_2012-12-12T00:00:00_Attempt=1", "objects": {"@SayHello_2012-12-12T00:00:00_Attempt=1": {"fields": [ {"key": "@componentParent", "refValue": "SayHello"}, {"key": "@scheduledStartTime", "stringValue": "2012-12-12T00:00:00"}, {"key": "parent", "refValue": "SayHello"}, {"key": "@sphere", "stringValue": "ATTEMPT"}, {"key": "workerGroup", "stringValue": "workerGroup"}, {"key": "@instanceParent", "refValue": "@SayHello_2012-12-12T00:00:00"}, {"key": "type", "stringValue": "ShellCommandActivity"}, {"key": "@status", "stringValue": "WAITING_FOR_RUNNER"}, {"key": "@version", "stringValue": "1"}, {"key": "schedule", "refValue": "Schedule"}, {"key": "@actualStartTime", "stringValue": "2012-12-13T01:40:50"}, {"key": "command", "stringValue": "echo hello"}, {"key": "@scheduledEndTime", "stringValue": "2012-12-12T01:00:00"}, {"key": "@activeInstances", "refValue": "@SayHello_2012-12-12T00:00:00"}, {"key": "@pipelineId", "stringValue": "df-0937003356ZJEXAMPLE"} ], "id": "@SayHello_2012-12-12T00:00:00_Attempt=1", "name": "@SayHello_2012-12-12T00:00:00_Attempt=1"} }, "pipelineId": "df-0937003356ZJEXAMPLE", "taskId": "2xaM4wRs5zOsIH+g9U3oVHfAgAlbSqU6XduncB0HhZ3xMnmvfePZPn4dIbYXHyWyRK+cU15MqDHwdrvftx/4wv+sNS4w34vJfv7QA9aOoOazW28l1GYSb2ZRR0N0paiQp+d1MhSKo10hOTWOsVK5S5Lnx9Qm6omFgXHyIvZRIvTlrQMpr1xuUrflyGOfbFOGpOLpvPE172MYdqpZKnbSS4TcuqgQKSWV2833fEubI57DPOP7ghWa2TcYeSIv4pdLYG53fTuwfbnbdc98g2LNUQzSVhSnt7BoqyNwht2aQ6b/UHg9A80+KVpuXuqmz3m1MXwHFgxjdmuesXNOrrlGpeLCcRWD+aGo0RN1NqhQRzNAig8V4GlaPTQzMsRCljKqvrIyAoP3Tt2XEGsHkkQo12rEX8Z90957XX2qKRwhruwYzqGkSLWjINoLdAxUJdpRXRc5DJTrBd3D5mdzn7kY1l7NEh4kFHJDt3Cx4Z3Mk8MYCACyCk/CEyy9DwuPi66cLz0NBcgbCM5LKjTBOwo1m+am+pvM1kSposE9FPP1+RFGb8k6jQBTJx3TRz1yKilnGXQTZ5xvdOFpJrklIT0OXP1MG3+auM9FlJA+1dX90QoNJE5z7axmK//MOGXUdkqFe2kiDkorqjxwDvc0Js9pVKfKvAmW8YqUbmI9l0ERpWCXXnLVHNmPWz3jaPY+OBAmuJWDmxB/Z8p94aEDg4BVXQ7LvsKQ3DLYhaB7yJ390CJT+i0mm+EBqY60V6YikPSWDFrYQ/NPi2b1DgE19mX8zHqw8qprIl4yh1Ckx2Iige4En/N5ktOoIxnASxAw/TzcE2skxdw5KlHDF+UTj71m16CR/dIaKlXijlfNlNzUBo/bNSadCQn3G5NoO501wPKI:XO50TgDNyo8EXAMPLE/g==:1"} } </response> </examples>

        Args:
            worker_group: <p>The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for <code>workerGroup</code> in the call to <code>PollForTask</code>. There are no wildcard values permitted in <code>workerGroup</code>; the string must be an exact, case-sensitive, match.</p>
            hostname: <p>The public DNS name of the calling task runner.</p>
            instance_identity: <p>Identity information for the EC2 instance that is hosting the task runner. You can get this value from the instance using <code>http://169.254.169.254/latest/meta-data/instance-id</code>. For more information, see <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html">Instance Metadata</a> in the <i>Amazon Elastic Compute Cloud User Guide.</i> Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.task_not_found_exception.TaskNotFoundException: <p>The specified task was not found. </p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.poll_for_task_input.PollForTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.poll_for_task_output.PollForTaskOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.poll_for_task

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.poll_for_task.async_poll_for_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.poll_for_task_input.PollForTaskInput = {
            "worker_group": worker_group
        }
        if hostname is not None:
            input_["hostname"] = hostname
        if instance_identity is not None:
            input_["instance_identity"] = instance_identity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_pipeline_definition(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        pipeline_objects: "capo_data_pipeline.types.pipeline_object_list.PipelineObjectList",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        parameter_objects: Optional[
            "capo_data_pipeline.types.parameter_object_list.ParameterObjectList"
        ] = None,
        parameter_values: Optional[
            "capo_data_pipeline.types.parameter_value_list.ParameterValueList"
        ] = None,
    ) -> "capo_data_pipeline.types.put_pipeline_definition_output.PutPipelineDefinitionOutput":
        """<p>Adds tasks, schedules, and preconditions to the specified pipeline. You can use <code>PutPipelineDefinition</code> to populate a new pipeline.</p> <p> <code>PutPipelineDefinition</code> also validates the configuration as it adds it to the pipeline. Changes to the pipeline are saved unless one of the following three validation errors exists in the pipeline. </p> <ol> <li>An object is missing a name or identifier field.</li> <li>A string or reference field is empty.</li> <li>The number of objects in the pipeline exceeds the maximum allowed objects.</li> <li>The pipeline is in a FINISHED state.</li> </ol> <p> Pipeline object definitions are passed to the <code>PutPipelineDefinition</code> action and returned by the <a>GetPipelineDefinition</a> action. </p> <examples> <example> <name>Example 1</name> <description> This example sets an valid pipeline configuration and returns success. </description> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.PutPipelineDefinition Content-Length: 914 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-0937003356ZJEXAMPLE", "pipelineObjects": [ {"id": "Default", "name": "Default", "fields": [ {"key": "workerGroup", "stringValue": "workerGroup"} ] }, {"id": "Schedule", "name": "Schedule", "fields": [ {"key": "startDateTime", "stringValue": "2012-12-12T00:00:00"}, {"key": "type", "stringValue": "Schedule"}, {"key": "period", "stringValue": "1 hour"}, {"key": "endDateTime", "stringValue": "2012-12-21T18:00:00"} ] }, {"id": "SayHello", "name": "SayHello", "fields": [ {"key": "type", "stringValue": "ShellCommandActivity"}, {"key": "command", "stringValue": "echo hello"}, {"key": "parent", "refValue": "Default"}, {"key": "schedule", "refValue": "Schedule"} ] } ] } </request> <response> HTTP/1.1 200 x-amzn-RequestId: f74afc14-0754-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 18 Date: Mon, 12 Nov 2012 17:50:53 GMT {"errored": false} </response> </example> <example> <name>Example 2</name> <description> This example sets an invalid pipeline configuration (the value for <code>workerGroup</code> is an empty string) and returns an error message. </description> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.PutPipelineDefinition Content-Length: 903 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE", "pipelineObjects": [ {"id": "Default", "name": "Default", "fields": [ {"key": "workerGroup", "stringValue": ""} ] }, {"id": "Schedule", "name": "Schedule", "fields": [ {"key": "startDateTime", "stringValue": "2012-09-25T17:00:00"}, {"key": "type", "stringValue": "Schedule"}, {"key": "period", "stringValue": "1 hour"}, {"key": "endDateTime", "stringValue": "2012-09-25T18:00:00"} ] }, {"id": "SayHello", "name": "SayHello", "fields": [ {"key": "type", "stringValue": "ShellCommandActivity"}, {"key": "command", "stringValue": "echo hello"}, {"key": "parent", "refValue": "Default"}, {"key": "schedule", "refValue": "Schedule"} ] } ] } </request> <response> HTTP/1.1 200 x-amzn-RequestId: f74afc14-0754-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 18 Date: Mon, 12 Nov 2012 17:50:53 GMT {"__type": "com.amazon.setl.webservice#InvalidRequestException", "message": "Pipeline definition has errors: Could not save the pipeline definition due to FATAL errors: [com.amazon.setl.webservice.ValidationError@108d7ea9] Please call Validate to validate your pipeline"} </response> </example> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            pipeline_objects: <p>The objects that define the pipeline. These objects overwrite the existing pipeline definition.</p>
            parameter_objects: <p>The parameter objects used with the pipeline.</p>
            parameter_values: <p>The parameter values used with the pipeline.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.put_pipeline_definition_input.PutPipelineDefinitionInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.put_pipeline_definition_output.PutPipelineDefinitionOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.put_pipeline_definition

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.put_pipeline_definition.async_put_pipeline_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.put_pipeline_definition_input.PutPipelineDefinitionInput = {
            "pipeline_id": pipeline_id,
            "pipeline_objects": pipeline_objects,
        }
        if parameter_objects is not None:
            input_["parameter_objects"] = parameter_objects
        if parameter_values is not None:
            input_["parameter_values"] = parameter_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def query_objects(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        sphere: "capo_data_pipeline.types.string.string",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        query: Optional["capo_data_pipeline.types.query.Query"] = None,
        marker: Optional["capo_data_pipeline.types.string.string"] = None,
        limit: Optional["capo_data_pipeline.types.int.int"] = None,
    ) -> "capo_data_pipeline.types.query_objects_output.QueryObjectsOutput":
        """<p>Queries the specified pipeline for the names of objects that match the specified set of conditions.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.QueryObjects Content-Length: 123 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE", "query": {"selectors": [ ] }, "sphere": "INSTANCE", "marker": "", "limit": 10} </request> <response> x-amzn-RequestId: 14d704c1-0775-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 72 Date: Mon, 12 Nov 2012 17:50:53 GMT {"hasMoreResults": false, "ids": ["@SayHello_1_2012-09-25T17:00:00"] } </response> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            query: <p>The query that defines the objects to be returned. The <code>Query</code> object can contain a maximum of ten selectors. The conditions in the query are limited to top-level String fields in the object. These filters can be applied to components, instances, and attempts.</p>
            sphere: <p>Indicates whether the query applies to components or instances. The possible values are: <code>COMPONENT</code>, <code>INSTANCE</code>, and <code>ATTEMPT</code>.</p>
            marker: <p>The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call <code>QueryObjects</code> with the marker value from the previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of object names that <code>QueryObjects</code> will return in a single call. The default value is 100. </p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.query_objects_input.QueryObjectsInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.query_objects_output.QueryObjectsOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.query_objects

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.query_objects.async_query_objects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.query_objects_input.QueryObjectsInput = {
            "pipeline_id": pipeline_id,
            "sphere": sphere,
        }
        if query is not None:
            input_["query"] = query
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_query_objects(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        sphere: "capo_data_pipeline.types.string.string",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        query: Optional["capo_data_pipeline.types.query.Query"] = None,
        marker: Optional["capo_data_pipeline.types.string.string"] = None,
        limit: Optional["capo_data_pipeline.types.int.int"] = None,
    ) -> "AsyncIterator[capo_data_pipeline.types.id.id]":
        _token = marker
        while True:
            _response = await self.query_objects(
                pipeline_id,
                sphere,
                config_overrides=config_overrides,
                query=query,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def remove_tags(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        tag_keys: "capo_data_pipeline.types.string_list.stringList",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
    ) -> "capo_data_pipeline.types.remove_tags_output.RemoveTagsOutput":
        """<p>Removes existing tags from the specified pipeline.</p>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            tag_keys: <p>The keys of the tags to remove.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.remove_tags_input.RemoveTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.remove_tags_output.RemoveTagsOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.remove_tags

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.remove_tags.async_remove_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.remove_tags_input.RemoveTagsInput = {
            "pipeline_id": pipeline_id,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def report_task_progress(
        self,
        task_id: "capo_data_pipeline.types.task_id.taskId",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        fields: Optional["capo_data_pipeline.types.field_list.fieldList"] = None,
    ) -> (
        "capo_data_pipeline.types.report_task_progress_output.ReportTaskProgressOutput"
    ):
        """<p>Task runners call <code>ReportTaskProgress</code> when assigned a task to acknowledge that it has the task. If the web service does not receive this acknowledgement within 2 minutes, it assigns the task in a subsequent <a>PollForTask</a> call. After this initial acknowledgement, the task runner only needs to report progress every 15 minutes to maintain its ownership of the task. You can change this reporting time from 15 minutes by specifying a <code>reportProgressTimeout</code> field in your pipeline.</p> <p>If a task runner does not report its status after 5 minutes, AWS Data Pipeline assumes that the task runner is unable to process the task and reassigns the task in a subsequent response to <a>PollForTask</a>. Task runners should call <code>ReportTaskProgress</code> every 60 seconds.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.ReportTaskProgress Content-Length: 832 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"taskId": "aaGgHT4LuH0T0Y0oLrJRjas5qH0d8cDPADxqq3tn+zCWGELkCdV2JprLreXm1oxeP5EFZHFLJ69kjSsLYE0iYHYBYVGBrB+E/pYq7ANEEeGJFnSBMRiXZVA+8UJ3OzcInvXeinqBmBaKwii7hnnKb/AXjXiNTXyxgydX1KAyg1AxkwBYG4cfPYMZbuEbQJFJvv5C/2+GVXz1w94nKYTeUeepwUOFOuRLS6JVtZoYwpF56E+Yfk1IcGpFOvCZ01B4Bkuu7x3J+MD/j6kJgZLAgbCJQtI3eiW3kdGmX0p0I2BdY1ZsX6b4UiSvM3OMj6NEHJCJL4E0ZfitnhCoe24Kvjo6C2hFbZq+ei/HPgSXBQMSagkr4vS9c0ChzxH2+LNYvec6bY4kymkaZI1dvOzmpa0FcnGf5AjSK4GpsViZ/ujz6zxFv81qBXzjF0/4M1775rjV1VUdyKaixiA/sJiACNezqZqETidp8d24BDPRhGsj6pBCrnelqGFrk/gXEXUsJ+xwMifRC8UVwiKekpAvHUywVk7Ku4jH/n3i2VoLRP6FXwpUbelu34iiZ9czpXyLtyPKwxa87dlrnRVURwkcVjOt2Mcrcaqe+cbWHvNRhyrPkkdfSF3ac8/wfgVbXvLEB2k9mKc67aD9rvdc1PKX09Tk8BKklsMTpZ3TRCd4NzQlJKigMe8Jat9+1tKj4Ole5ZzW6uyTu2s2iFjEV8KXu4MaiRJyNKCdKeGhhZWY37Qk4NBK4Ppgu+C6Y41dpfOh288SLDEVx0/UySlqOEdhba7c6BiPp5r3hKj3mk9lFy5OYp1aoGLeeFmjXveTnPdf2gkWqXXg7AUbJ7jEs1F0lKZQg4szep2gcKyAJXgvXLfJJHcha8Lfb/Ee7wYmyOcAaRpDBoFNSbtoVXar46teIrpho+ZDvynUXvU0grHWGOk=:wn3SgymHZM99bEXAMPLE", "fields": [ {"key": "percentComplete", "stringValue": "50"} ] } </request> <response> x-amzn-RequestId: 640bd023-0775-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 18 Date: Mon, 12 Nov 2012 17:50:53 GMT {"canceled": false} </response> </examples>

        Args:
            task_id: <p>The ID of the task assigned to the task runner. This value is provided in the response for <a>PollForTask</a>.</p>
            fields: <p>Key-value pairs that define the properties of the ReportTaskProgressInput object.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.task_not_found_exception.TaskNotFoundException: <p>The specified task was not found. </p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.report_task_progress_input.ReportTaskProgressInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.report_task_progress_output.ReportTaskProgressOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.report_task_progress

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.report_task_progress.async_report_task_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.report_task_progress_input.ReportTaskProgressInput = {
            "task_id": task_id
        }
        if fields is not None:
            input_["fields"] = fields

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def report_task_runner_heartbeat(
        self,
        taskrunner_id: "capo_data_pipeline.types.id.id",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        worker_group: Optional["capo_data_pipeline.types.string.string"] = None,
        hostname: Optional["capo_data_pipeline.types.id.id"] = None,
    ) -> "capo_data_pipeline.types.report_task_runner_heartbeat_output.ReportTaskRunnerHeartbeatOutput":
        """<p>Task runners call <code>ReportTaskRunnerHeartbeat</code> every 15 minutes to indicate that they are operational. If the AWS Data Pipeline Task Runner is launched on a resource managed by AWS Data Pipeline, the web service can use this call to detect when the task runner application has failed and restart a new instance.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.ReportTaskRunnerHeartbeat Content-Length: 84 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"taskrunnerId": "1234567890", "workerGroup": "wg-12345", "hostname": "example.com"} </request> <response> Status: x-amzn-RequestId: b3104dc5-0734-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 20 Date: Mon, 12 Nov 2012 17:50:53 GMT {"terminate": false} </response> </examples>

        Args:
            taskrunner_id: <p>The ID of the task runner. This value should be unique across your AWS account. In the case of AWS Data Pipeline Task Runner launched on a resource managed by AWS Data Pipeline, the web service provides a unique identifier when it launches the application. If you have written a custom task runner, you should assign a unique identifier for the task runner.</p>
            worker_group: <p>The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for <code>workerGroup</code>. There are no wildcard values permitted in <code>workerGroup</code>; the string must be an exact, case-sensitive, match.</p>
            hostname: <p>The public DNS name of the task runner.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.report_task_runner_heartbeat_input.ReportTaskRunnerHeartbeatInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.report_task_runner_heartbeat_output.ReportTaskRunnerHeartbeatOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.report_task_runner_heartbeat

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.report_task_runner_heartbeat.async_report_task_runner_heartbeat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.report_task_runner_heartbeat_input.ReportTaskRunnerHeartbeatInput = {
            "taskrunner_id": taskrunner_id
        }
        if worker_group is not None:
            input_["worker_group"] = worker_group
        if hostname is not None:
            input_["hostname"] = hostname

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_status(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        object_ids: "capo_data_pipeline.types.id_list.idList",
        status: "capo_data_pipeline.types.string.string",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
    ) -> None:
        """<p>Requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline. This update might not occur immediately, but is eventually consistent. The status that can be set depends on the type of object (for example, DataNode or Activity). You cannot perform this operation on <code>FINISHED</code> pipelines and attempting to do so returns <code>InvalidRequestException</code>.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.SetStatus Content-Length: 100 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-0634701J7KEXAMPLE", "objectIds": ["o-08600941GHJWMBR9E2"], "status": "pause"} </request> <response> x-amzn-RequestId: e83b8ab7-076a-11e2-af6f-6bc7a6be60d9 Content-Type: application/x-amz-json-1.1 Content-Length: 0 Date: Mon, 12 Nov 2012 17:50:53 GMT Unexpected response: 200, OK, undefined </response> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline that contains the objects.</p>
            object_ids: <p>The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.</p>
            status: <p>The status to be set on all the objects specified in <code>objectIds</code>. For components, use <code>PAUSE</code> or <code>RESUME</code>. For instances, use <code>TRY_CANCEL</code>, <code>RERUN</code>, or <code>MARK_FINISHED</code>.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.set_status_input.SetStatusInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_data_pipeline._operations.data_pipeline.set_status

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.set_status.async_set_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.set_status_input.SetStatusInput = {
            "pipeline_id": pipeline_id,
            "object_ids": object_ids,
            "status": status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_task_status(
        self,
        task_id: "capo_data_pipeline.types.task_id.taskId",
        task_status: "capo_data_pipeline.types.task_status.TaskStatus",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        error_id: Optional["capo_data_pipeline.types.string.string"] = None,
        error_message: Optional[
            "capo_data_pipeline.types.error_message.errorMessage"
        ] = None,
        error_stack_trace: Optional["capo_data_pipeline.types.string.string"] = None,
    ) -> "capo_data_pipeline.types.set_task_status_output.SetTaskStatusOutput":
        """<p>Task runners call <code>SetTaskStatus</code> to notify AWS Data Pipeline that a task is completed and provide information about the final status. A task runner makes this call regardless of whether the task was sucessful. A task runner does not need to call <code>SetTaskStatus</code> for tasks that are canceled by the web service during a call to <a>ReportTaskProgress</a>.</p> <examples> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.SetTaskStatus Content-Length: 847 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"taskId": "aaGgHT4LuH0T0Y0oLrJRjas5qH0d8cDPADxqq3tn+zCWGELkCdV2JprLreXm1oxeP5EFZHFLJ69kjSsLYE0iYHYBYVGBrB+E/pYq7ANEEeGJFnSBMRiXZVA+8UJ3OzcInvXeinqBmBaKwii7hnnKb/AXjXiNTXyxgydX1KAyg1AxkwBYG4cfPYMZbuEbQJFJvv5C/2+GVXz1w94nKYTeUeepwUOFOuRLS6JVtZoYwpF56E+Yfk1IcGpFOvCZ01B4Bkuu7x3J+MD/j6kJgZLAgbCJQtI3eiW3kdGmX0p0I2BdY1ZsX6b4UiSvM3OMj6NEHJCJL4E0ZfitnhCoe24Kvjo6C2hFbZq+ei/HPgSXBQMSagkr4vS9c0ChzxH2+LNYvec6bY4kymkaZI1dvOzmpa0FcnGf5AjSK4GpsViZ/ujz6zxFv81qBXzjF0/4M1775rjV1VUdyKaixiA/sJiACNezqZqETidp8d24BDPRhGsj6pBCrnelqGFrk/gXEXUsJ+xwMifRC8UVwiKekpAvHUywVk7Ku4jH/n3i2VoLRP6FXwpUbelu34iiZ9czpXyLtyPKwxa87dlrnRVURwkcVjOt2Mcrcaqe+cbWHvNRhyrPkkdfSF3ac8/wfgVbXvLEB2k9mKc67aD9rvdc1PKX09Tk8BKklsMTpZ3TRCd4NzQlJKigMe8Jat9+1tKj4Ole5ZzW6uyTu2s2iFjEV8KXu4MaiRJyNKCdKeGhhZWY37Qk4NBK4Ppgu+C6Y41dpfOh288SLDEVx0/UySlqOEdhba7c6BiPp5r3hKj3mk9lFy5OYp1aoGLeeFmjXveTnPdf2gkWqXXg7AUbJ7jEs1F0lKZQg4szep2gcKyAJXgvXLfJJHcha8Lfb/Ee7wYmyOcAaRpDBoFNSbtoVXar46teIrpho+ZDvynUXvU0grHWGOk=:wn3SgymHZM99bEXAMPLE", "taskStatus": "FINISHED"} </request> <response> x-amzn-RequestId: 8c8deb53-0788-11e2-af9c-6bc7a6be6qr8 Content-Type: application/x-amz-json-1.1 Content-Length: 0 Date: Mon, 12 Nov 2012 17:50:53 GMT {} </response> </examples>

        Args:
            task_id: <p>The ID of the task assigned to the task runner. This value is provided in the response for <a>PollForTask</a>.</p>
            task_status: <p>If <code>FINISHED</code>, the task successfully completed. If <code>FAILED</code>, the task ended unsuccessfully. Preconditions use false.</p>
            error_id: <p>If an error occurred during the task, this value specifies the error code. This value is set on the physical attempt object. It is used to display error information to the user. It should not start with string "Service_" which is reserved by the system.</p>
            error_message: <p>If an error occurred during the task, this value specifies a text description of the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.</p>
            error_stack_trace: <p>If an error occurred during the task, this value specifies the stack trace associated with the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.task_not_found_exception.TaskNotFoundException: <p>The specified task was not found. </p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.set_task_status_input.SetTaskStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.set_task_status_output.SetTaskStatusOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.set_task_status

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.set_task_status.async_set_task_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.set_task_status_input.SetTaskStatusInput = {
            "task_id": task_id,
            "task_status": task_status,
        }
        if error_id is not None:
            input_["error_id"] = error_id
        if error_message is not None:
            input_["error_message"] = error_message
        if error_stack_trace is not None:
            input_["error_stack_trace"] = error_stack_trace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def validate_pipeline_definition(
        self,
        pipeline_id: "capo_data_pipeline.types.id.id",
        pipeline_objects: "capo_data_pipeline.types.pipeline_object_list.PipelineObjectList",
        *,
        config_overrides: Optional[AsyncDataPipelineClientConfig] = None,
        parameter_objects: Optional[
            "capo_data_pipeline.types.parameter_object_list.ParameterObjectList"
        ] = None,
        parameter_values: Optional[
            "capo_data_pipeline.types.parameter_value_list.ParameterValueList"
        ] = None,
    ) -> "capo_data_pipeline.types.validate_pipeline_definition_output.ValidatePipelineDefinitionOutput":
        """<p>Validates the specified pipeline definition to ensure that it is well formed and can be run without error.</p> <examples> <example> <name>Example 1</name> <description> This example sets an valid pipeline configuration and returns success. </description> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.ValidatePipelineDefinition Content-Length: 936 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE", "pipelineObjects": [ {"id": "Default", "name": "Default", "fields": [ {"key": "workerGroup", "stringValue": "MyworkerGroup"} ] }, {"id": "Schedule", "name": "Schedule", "fields": [ {"key": "startDateTime", "stringValue": "2012-09-25T17:00:00"}, {"key": "type", "stringValue": "Schedule"}, {"key": "period", "stringValue": "1 hour"}, {"key": "endDateTime", "stringValue": "2012-09-25T18:00:00"} ] }, {"id": "SayHello", "name": "SayHello", "fields": [ {"key": "type", "stringValue": "ShellCommandActivity"}, {"key": "command", "stringValue": "echo hello"}, {"key": "parent", "refValue": "Default"}, {"key": "schedule", "refValue": "Schedule"} ] } ] } </request> <response> x-amzn-RequestId: 92c9f347-0776-11e2-8a14-21bb8a1f50ef Content-Type: application/x-amz-json-1.1 Content-Length: 18 Date: Mon, 12 Nov 2012 17:50:53 GMT {"errored": false} </response> </example> <example> <name>Example 2</name> <description> This example sets an invalid pipeline configuration and returns the associated set of validation errors. </description> <request> POST / HTTP/1.1 Content-Type: application/x-amz-json-1.1 X-Amz-Target: DataPipeline.ValidatePipelineDefinition Content-Length: 903 Host: datapipeline.us-east-1.amazonaws.com X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT Authorization: AuthParams {"pipelineId": "df-06372391ZG65EXAMPLE", "pipelineObjects": [ {"id": "Default", "name": "Default", "fields": [ {"key": "workerGroup", "stringValue": "MyworkerGroup"} ] }, {"id": "Schedule", "name": "Schedule", "fields": [ {"key": "startDateTime", "stringValue": "bad-time"}, {"key": "type", "stringValue": "Schedule"}, {"key": "period", "stringValue": "1 hour"}, {"key": "endDateTime", "stringValue": "2012-09-25T18:00:00"} ] }, {"id": "SayHello", "name": "SayHello", "fields": [ {"key": "type", "stringValue": "ShellCommandActivity"}, {"key": "command", "stringValue": "echo hello"}, {"key": "parent", "refValue": "Default"}, {"key": "schedule", "refValue": "Schedule"} ] } ] } </request> <response> x-amzn-RequestId: 496a1f5a-0e6a-11e2-a61c-bd6312c92ddd Content-Type: application/x-amz-json-1.1 Content-Length: 278 Date: Mon, 12 Nov 2012 17:50:53 GMT {"errored": true, "validationErrors": [ {"errors": ["INVALID_FIELD_VALUE: 'startDateTime' value must be a literal datetime value."], "id": "Schedule"} ] } </response> </example> </examples>

        Args:
            pipeline_id: <p>The ID of the pipeline.</p>
            pipeline_objects: <p>The objects that define the pipeline changes to validate against the pipeline.</p>
            parameter_objects: <p>The parameter objects used with the pipeline.</p>
            parameter_values: <p>The parameter values used with the pipeline.</p>

        Raises:
            capo_data_pipeline.errors.internal_service_error.InternalServiceError: <p>An internal service error occurred.</p>
            capo_data_pipeline.errors.invalid_request_exception.InvalidRequestException: <p>The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.</p>
            capo_data_pipeline.errors.pipeline_deleted_exception.PipelineDeletedException: <p>The specified pipeline has been deleted.</p>
            capo_data_pipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The specified pipeline was not found. Verify that you used the correct user and account identifiers.</p>
            capo_data_pipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_data_pipeline.types.validate_pipeline_definition_input.ValidatePipelineDefinitionInput]",
        ) -> AsyncOperationResponse[
            "capo_data_pipeline.types.validate_pipeline_definition_output.ValidatePipelineDefinitionOutput"
        ]:
            import capo_data_pipeline._operations.data_pipeline.validate_pipeline_definition

            (
                output,
                http_response,
            ) = await capo_data_pipeline._operations.data_pipeline.validate_pipeline_definition.async_validate_pipeline_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_data_pipeline.types.validate_pipeline_definition_input.ValidatePipelineDefinitionInput = {
            "pipeline_id": pipeline_id,
            "pipeline_objects": pipeline_objects,
        }
        if parameter_objects is not None:
            input_["parameter_objects"] = parameter_objects
        if parameter_values is not None:
            input_["parameter_values"] = parameter_values

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

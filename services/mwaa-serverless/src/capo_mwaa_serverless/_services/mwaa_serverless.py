"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#AmazonMWAAServerless``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mwaa_serverless._auth._signers
import capo_mwaa_serverless._auth._sigv4
from capo_mwaa_serverless._auth._identity import Credentials
from capo_mwaa_serverless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mwaa_serverless._auth._zapros_handler import AuthMiddleware
from capo_mwaa_serverless._pagination import resolve_path as _resolve_path
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.task_instance_resource import (
    TaskInstanceResource,
)
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_resource import (
    WorkflowResource,
)
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_run_resource import (
    WorkflowRunResource,
)
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_version_resource import (
    WorkflowVersionResource,
)
from capo_mwaa_serverless._services._aws_config import aws_config
from capo_mwaa_serverless._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.code
    import capo_mwaa_serverless.types.create_workflow_request
    import capo_mwaa_serverless.types.create_workflow_response
    import capo_mwaa_serverless.types.definition_s3_location
    import capo_mwaa_serverless.types.delete_workflow_request
    import capo_mwaa_serverless.types.delete_workflow_response
    import capo_mwaa_serverless.types.description_string
    import capo_mwaa_serverless.types.encryption_configuration
    import capo_mwaa_serverless.types.engine_version
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.get_task_instance_request
    import capo_mwaa_serverless.types.get_task_instance_response
    import capo_mwaa_serverless.types.get_workflow_request
    import capo_mwaa_serverless.types.get_workflow_response
    import capo_mwaa_serverless.types.get_workflow_run_request
    import capo_mwaa_serverless.types.get_workflow_run_response
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.idempotency_token_string
    import capo_mwaa_serverless.types.list_tags_for_resource_request
    import capo_mwaa_serverless.types.list_tags_for_resource_response
    import capo_mwaa_serverless.types.list_task_instances_request
    import capo_mwaa_serverless.types.list_task_instances_response
    import capo_mwaa_serverless.types.list_workflow_runs_request
    import capo_mwaa_serverless.types.list_workflow_runs_response
    import capo_mwaa_serverless.types.list_workflow_versions_request
    import capo_mwaa_serverless.types.list_workflow_versions_response
    import capo_mwaa_serverless.types.list_workflows_request
    import capo_mwaa_serverless.types.list_workflows_response
    import capo_mwaa_serverless.types.logging_configuration
    import capo_mwaa_serverless.types.name_string
    import capo_mwaa_serverless.types.network_configuration
    import capo_mwaa_serverless.types.object_map
    import capo_mwaa_serverless.types.role_arn
    import capo_mwaa_serverless.types.start_workflow_run_request
    import capo_mwaa_serverless.types.start_workflow_run_response
    import capo_mwaa_serverless.types.stop_workflow_run_request
    import capo_mwaa_serverless.types.stop_workflow_run_response
    import capo_mwaa_serverless.types.tag_keys
    import capo_mwaa_serverless.types.tag_resource_request
    import capo_mwaa_serverless.types.tag_resource_response
    import capo_mwaa_serverless.types.taggable_resource_arn
    import capo_mwaa_serverless.types.tags
    import capo_mwaa_serverless.types.task_instance_summary
    import capo_mwaa_serverless.types.untag_resource_request
    import capo_mwaa_serverless.types.untag_resource_response
    import capo_mwaa_serverless.types.update_workflow_request
    import capo_mwaa_serverless.types.update_workflow_response
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_run_summary
    import capo_mwaa_serverless.types.workflow_summary
    import capo_mwaa_serverless.types.workflow_version
    import capo_mwaa_serverless.types.workflow_version_summary


class MWAAServerlessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MWAAServerlessClient:
    """A client for the ``MWAAServerless`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = MWAAServerlessClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.task_instance_resource = TaskInstanceResource(self)
        self.workflow_resource = WorkflowResource(self)
        self.workflow_run_resource = WorkflowRunResource(self)
        self.workflow_version_resource = WorkflowVersionResource(self)

    def operation_options(
        self, config_overrides: Optional[MWAAServerlessClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MWAAServerlessClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags that are associated with a specified Amazon Managed Workflows for Apache Airflow Serverless resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_tags_for_resource

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_mwaa_serverless.types.tags.Tags",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an Amazon Managed Workflows for Apache Airflow Serverless resource. Tags are key-value pairs that help you organize and categorize your resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>
            tags: <p>A map of tags to add to the resource. Each tag consists of a key-value pair.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.tag_resource

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_mwaa_serverless.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an Amazon Managed Workflows for Apache Airflow Serverless resource. This operation removes the specified tags from the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of tag keys to remove from the resource. Only the keys are required; the values are ignored.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.untag_resource

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.untag_resource_request.UntagResourceRequest = {
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

    def get_task_instance(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        task_instance_id: "capo_mwaa_serverless.types.id_string.IdString",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> (
        "capo_mwaa_serverless.types.get_task_instance_response.GetTaskInstanceResponse"
    ):
        """<p>Retrieves detailed information about a specific task instance within a workflow run. Task instances represent individual tasks that are executed as part of a workflow in the Amazon Managed Workflows for Apache Airflow Serverless environment. Each task instance runs in an isolated ECS container with dedicated resources and security boundaries. The service tracks task execution state, retry attempts, and provides detailed timing and error information for troubleshooting and monitoring purposes.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the task instance.</p>
            task_instance_id: <p>The unique identifier of the task instance to retrieve.</p>
            run_id: <p>The unique identifier of the workflow run that contains the task instance.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.get_task_instance_request.GetTaskInstanceRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.get_task_instance_response.GetTaskInstanceResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_task_instance

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_task_instance.get_task_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.get_task_instance_request.GetTaskInstanceRequest = {
            "workflow_arn": workflow_arn,
            "task_instance_id": task_instance_id,
            "run_id": run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_task_instances(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mwaa_serverless.types.list_task_instances_response.ListTaskInstancesResponse":
        """<p>Lists all task instances for a specific workflow run, with optional pagination support.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run for which you want a list of task instances.</p>
            max_results: <p>The maximum number of task instances to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListTaskInstances</code>.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_task_instances_request.ListTaskInstancesRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_task_instances_response.ListTaskInstancesResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_task_instances

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_task_instances.list_task_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.list_task_instances_request.ListTaskInstancesRequest = {
            "workflow_arn": workflow_arn,
            "run_id": run_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_task_instances(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "Iterator[capo_mwaa_serverless.types.task_instance_summary.TaskInstanceSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_task_instances(
                workflow_arn,
                run_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("task_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_workflow(
        self,
        name: "capo_mwaa_serverless.types.name_string.NameString",
        definition_s3_location: "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location",
        role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        client_token: Optional[
            "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        code: Optional["capo_mwaa_serverless.types.code.Code"] = None,
        description: Optional[
            "capo_mwaa_serverless.types.description_string.DescriptionString"
        ] = None,
        encryption_configuration: Optional[
            "capo_mwaa_serverless.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
        ] = None,
        engine_version: Optional[
            "capo_mwaa_serverless.types.engine_version.EngineVersion"
        ] = None,
        network_configuration: Optional[
            "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        tags: Optional["capo_mwaa_serverless.types.tags.Tags"] = None,
        trigger_mode: Optional[
            "capo_mwaa_serverless.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_mwaa_serverless.types.create_workflow_response.CreateWorkflowResponse":
        """<p>Creates a new workflow in Amazon Managed Workflows for Apache Airflow Serverless. This operation initializes a workflow with the specified configuration including the workflow definition, execution role, and optional settings for encryption, logging, and networking. You must provide the workflow definition as a YAML file stored in Amazon S3 that defines the DAG structure using supported Amazon Web Services operators. Amazon Managed Workflows for Apache Airflow Serverless automatically creates the first version of the workflow and sets up the necessary execution environment with multi-tenant isolation and security controls.</p>

        Args:
            name: <p>The name of the workflow. You must use unique workflow names within your Amazon Web Services account. The service generates a unique identifier that is appended to ensure temporal uniqueness across the account lifecycle.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow creation requests.</p>
            definition_s3_location: <p>The Amazon S3 location where the workflow definition file is stored. This must point to a valid YAML file that defines the workflow structure using supported Amazon Web Services operators and tasks. Amazon Managed Workflows for Apache Airflow Serverless takes a snapshot of the definition at creation time, so subsequent changes to the Amazon S3 object will not affect the workflow unless you create a new version. In your YAML definition, include task dependencies, scheduling information, and operator configurations that are compatible with the Amazon Managed Workflows for Apache Airflow Serverless execution environment.</p>
            code: <p>The location of code artifacts in Amazon S3 for the workflow. The service copies the code from this location at the time of the request.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when executing the workflow. This role must have the necessary permissions to access the required Amazon Web Services services and resources that your workflow tasks will interact with. The role is used for task execution in the isolated, multi-tenant environment and should follow the principle of least privilege. Amazon Managed Workflows for Apache Airflow Serverless validates role access during workflow creation but runtime permission checks are performed by the target services.</p>
            description: <p>An optional description of the workflow that you can use to provide additional context about the workflow's purpose and functionality.</p>
            encryption_configuration: <p>The configuration for encrypting workflow data at rest and in transit. Specifies the encryption type and optional KMS key for customer-managed encryption.</p>
            logging_configuration: <p>The configuration for workflow logging. Specifies the CloudWatch log group where workflow execution logs are stored. Amazon Managed Workflows for Apache Airflow Serverless automatically exports worker logs and task-level information to the specified log group in your account using remote logging functionality. This provides comprehensive observability for debugging and monitoring workflow execution across the distributed, serverless environment.</p>
            engine_version: <p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for this workflow. This determines the feature set, supported operators, and execution environment capabilities available to your workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains backward compatibility across versions while introducing new features and improvements. Currently supports version 1 with plans for additional versions as the service evolves.</p>
            network_configuration: <p>Network configuration for the workflow execution environment, including VPC security groups and subnets for secure network access. When specified, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your customer VPC to provide secure connectivity to your resources. If not specified, tasks run in the service's default worker VPC with network isolation from other customers. This configuration enables secure access to VPC-only resources like RDS databases or private endpoints.</p>
            tags: <p>A map of tags to assign to the workflow resource. Tags are key-value pairs that are used for resource organization and cost allocation.</p>
            trigger_mode: <p>The trigger mode for the workflow execution.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.create_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.create_workflow.create_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.create_workflow_request.CreateWorkflowRequest = {
            "name": name,
            "definition_s3_location": definition_s3_location,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if code is not None:
            input_["code"] = code
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if tags is not None:
            input_["tags"] = tags
        if trigger_mode is not None:
            input_["trigger_mode"] = trigger_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workflow(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
        ] = None,
    ) -> "capo_mwaa_serverless.types.get_workflow_response.GetWorkflowResponse":
        """<p>Retrieves detailed information about a workflow, including its configuration, status, and metadata.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to retrieve.</p>
            workflow_version: <p>Optional. The specific version of the workflow to retrieve. If not specified, the latest version is returned.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.get_workflow_request.GetWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow.get_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.get_workflow_request.GetWorkflowRequest = {
            "workflow_arn": workflow_arn
        }
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workflow(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        definition_s3_location: "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location",
        role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        code: Optional["capo_mwaa_serverless.types.code.Code"] = None,
        description: Optional[
            "capo_mwaa_serverless.types.description_string.DescriptionString"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
        ] = None,
        engine_version: Optional[
            "capo_mwaa_serverless.types.engine_version.EngineVersion"
        ] = None,
        network_configuration: Optional[
            "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        trigger_mode: Optional[
            "capo_mwaa_serverless.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_mwaa_serverless.types.update_workflow_response.UpdateWorkflowResponse":
        """<p>Updates an existing workflow with new configuration settings. This operation allows you to modify the workflow definition, role, and other settings. When you update a workflow, Amazon Managed Workflows for Apache Airflow Serverless automatically creates a new version with the updated configuration and disables scheduling on all previous versions to ensure only one version is actively scheduled at a time. The update operation maintains workflow history while providing a clean transition to the new configuration.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to update.</p>
            definition_s3_location: <p>The Amazon S3 location where the updated workflow definition file is stored.</p>
            code: <p>The location of code artifacts in Amazon S3 for the updated workflow. The service copies the code from this location at the time of the request.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when it executes the updated workflow.</p>
            description: <p>An updated description for the workflow.</p>
            logging_configuration: <p>Updated logging configuration for the workflow.</p>
            engine_version: <p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for the updated workflow.</p>
            network_configuration: <p>Updated network configuration for the workflow execution environment.</p>
            trigger_mode: <p>The trigger mode for the workflow execution.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.update_workflow_request.UpdateWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.update_workflow_response.UpdateWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.update_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.update_workflow.update_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.update_workflow_request.UpdateWorkflowRequest = {
            "workflow_arn": workflow_arn,
            "definition_s3_location": definition_s3_location,
            "role_arn": role_arn,
        }
        if code is not None:
            input_["code"] = code
        if description is not None:
            input_["description"] = description
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if trigger_mode is not None:
            input_["trigger_mode"] = trigger_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workflow(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
        ] = None,
    ) -> "capo_mwaa_serverless.types.delete_workflow_response.DeleteWorkflowResponse":
        """<p>Deletes a workflow and all its versions. This operation permanently removes the workflow and cannot be undone. Amazon Managed Workflows for Apache Airflow Serverless ensures that all associated resources are properly cleaned up, including stopping any running executions, removing scheduled triggers, and cleaning up execution history. The deletion process respects the multi-tenant isolation boundaries and ensures that no residual data or configurations remain that could affect other customers or workflows.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to delete.</p>
            workflow_version: <p>Optional. The specific version of the workflow to delete. If not specified, all versions of the workflow are deleted.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.delete_workflow_response.DeleteWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.delete_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.delete_workflow.delete_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.delete_workflow_request.DeleteWorkflowRequest = {
            "workflow_arn": workflow_arn
        }
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workflows(
        self,
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mwaa_serverless.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists all workflows in your account, with optional pagination support. This operation returns summary information for workflows, showing only the most recently created version of each workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains workflow metadata in a highly available, distributed storage system that enables efficient querying and filtering. The service implements proper access controls to ensure you can only view workflows that you have permissions to access, supporting both individual and team-based workflow management scenarios.</p>

        Args:
            max_results: <p>The maximum number of workflows you want to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflows</code>.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflows

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.list_workflows_request.ListWorkflowsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workflows(
        self,
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mwaa_serverless.types.workflow_summary.WorkflowSummary]":
        _token = next_token
        while True:
            _response = self.list_workflows(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_workflow_run(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        client_token: Optional[
            "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        override_parameters: Optional[
            "capo_mwaa_serverless.types.object_map.ObjectMap"
        ] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "capo_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse":
        """<p>Starts a new execution of a workflow. This operation creates a workflow run that executes the tasks that are defined in the workflow. Amazon Managed Workflows for Apache Airflow Serverless schedules the workflow execution across its managed Airflow environment, automatically scaling ECS worker tasks based on the workload. The service handles task isolation, dependency resolution, and provides comprehensive monitoring and logging throughout the execution lifecycle.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to run.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow run requests.</p>
            override_parameters: <p>Optional parameters to override default workflow parameters for this specific run. These parameters are passed to the workflow during execution and can be used to customize behavior without modifying the workflow definition. Parameters are made available as environment variables to tasks and you can reference them within the YAML workflow definition using standard parameter substitution syntax.</p>
            workflow_version: <p>Optional. The specific version of the workflow to execute. If not specified, the latest version is used.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run.start_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest = {
            "workflow_arn": workflow_arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if override_parameters is not None:
            input_["override_parameters"] = override_parameters
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workflow_run(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves detailed information about a specific workflow run, including its status, execution details, and task instances.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run to retrieve.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run.get_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest = {
            "workflow_arn": workflow_arn,
            "run_id": run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_workflow_run(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> (
        "capo_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
    ):
        """<p>Stops a running workflow execution. This operation terminates all running tasks and prevents new tasks from starting. Amazon Managed Workflows for Apache Airflow Serverless gracefully shuts down the workflow execution by stopping task scheduling and terminating active ECS worker containers. The operation transitions the workflow run to a <code>STOPPING</code> state and then to <code>STOPPED</code> once all cleanup is complete. In-flight tasks may complete or be terminated depending on their current execution state.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run you want to stop.</p>
            run_id: <p>The unique identifier of the workflow run to stop.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run.stop_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest = {
            "workflow_arn": workflow_arn,
            "run_id": run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workflow_runs(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "capo_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all runs for a specified workflow, with optional pagination and filtering support.</p>

        Args:
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowRuns</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want a list of runs.</p>
            workflow_version: <p>Optional. The specific version of the workflow for which you want a list of runs. If not specified, runs for all versions are returned.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs.list_workflow_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest = {
            "workflow_arn": workflow_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workflow_runs(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "Iterator[capo_mwaa_serverless.types.workflow_run_summary.WorkflowRunSummary]":
        _token = next_token
        while True:
            _response = self.list_workflow_runs(
                workflow_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                workflow_version=workflow_version,
            )
            _page = _resolve_path(_response, ("workflow_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_workflow_versions(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse":
        """<p>Lists all versions of a specified workflow, with optional pagination support.</p>

        Args:
            max_results: <p>The maximum number of workflow versions to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowVersions</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want to list versions.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions.list_workflow_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest = {
            "workflow_arn": workflow_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workflow_versions(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mwaa_serverless.types.workflow_version_summary.WorkflowVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_workflow_versions(
                workflow_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workflow_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

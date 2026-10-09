"""Generated from Smithy shape ``com.amazonaws.braket#Braket``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_braket._auth._signers
import capo_braket._auth._sigv4
from capo_braket._auth._identity import Credentials
from capo_braket._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_braket._auth._zapros_handler import AuthMiddleware
from capo_braket._pagination import resolve_path as _resolve_path
from capo_braket._resources.braket.device_resource import AsyncDeviceResource
from capo_braket._resources.braket.job_resource import AsyncJobResource
from capo_braket._resources.braket.quantum_task_resource import AsyncQuantumTaskResource
from capo_braket._resources.braket.spending_limit_resource import (
    AsyncSpendingLimitResource,
)
from capo_braket._services._aws_config import aaws_config
from capo_braket._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_braket.types.algorithm_specification
    import capo_braket.types.associations
    import capo_braket.types.cancel_job_request
    import capo_braket.types.cancel_job_response
    import capo_braket.types.cancel_quantum_task_request
    import capo_braket.types.cancel_quantum_task_response
    import capo_braket.types.create_job_request
    import capo_braket.types.create_job_response
    import capo_braket.types.create_quantum_task_request
    import capo_braket.types.create_quantum_task_response
    import capo_braket.types.create_spending_limit_request
    import capo_braket.types.create_spending_limit_response
    import capo_braket.types.delete_spending_limit_request
    import capo_braket.types.delete_spending_limit_response
    import capo_braket.types.device_arn
    import capo_braket.types.device_config
    import capo_braket.types.device_summary
    import capo_braket.types.experimental_capabilities
    import capo_braket.types.get_device_request
    import capo_braket.types.get_device_response
    import capo_braket.types.get_job_request
    import capo_braket.types.get_job_response
    import capo_braket.types.get_quantum_task_request
    import capo_braket.types.get_quantum_task_response
    import capo_braket.types.hybrid_job_additional_attribute_names_list
    import capo_braket.types.hyper_parameters
    import capo_braket.types.input_config_list
    import capo_braket.types.instance_config
    import capo_braket.types.job_arn
    import capo_braket.types.job_checkpoint_config
    import capo_braket.types.job_output_data_config
    import capo_braket.types.job_stopping_condition
    import capo_braket.types.job_summary
    import capo_braket.types.job_token
    import capo_braket.types.json_value
    import capo_braket.types.list_tags_for_resource_request
    import capo_braket.types.list_tags_for_resource_response
    import capo_braket.types.quantum_task_additional_attribute_names_list
    import capo_braket.types.quantum_task_arn
    import capo_braket.types.quantum_task_summary
    import capo_braket.types.role_arn
    import capo_braket.types.search_devices_filter_list
    import capo_braket.types.search_devices_request
    import capo_braket.types.search_devices_response
    import capo_braket.types.search_jobs_filter_list
    import capo_braket.types.search_jobs_request
    import capo_braket.types.search_jobs_response
    import capo_braket.types.search_quantum_tasks_filter_list
    import capo_braket.types.search_quantum_tasks_request
    import capo_braket.types.search_quantum_tasks_response
    import capo_braket.types.search_spending_limits_filter_list
    import capo_braket.types.search_spending_limits_request
    import capo_braket.types.search_spending_limits_response
    import capo_braket.types.spending_limit_arn
    import capo_braket.types.spending_limit_summary
    import capo_braket.types.string64
    import capo_braket.types.tag_keys
    import capo_braket.types.tag_resource_request
    import capo_braket.types.tag_resource_response
    import capo_braket.types.tags_map
    import capo_braket.types.time_period
    import capo_braket.types.untag_resource_request
    import capo_braket.types.untag_resource_response
    import capo_braket.types.update_spending_limit_request
    import capo_braket.types.update_spending_limit_response


class AsyncBraketClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncBraketClient:
    """A client for the ``Braket`` service.

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
        self._config = AsyncBraketClientConfig(
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

        # resources
        self.device_resource = AsyncDeviceResource(self)
        self.job_resource = AsyncJobResource(self)
        self.quantum_task_resource = AsyncQuantumTaskResource(self)
        self.spending_limit_resource = AsyncSpendingLimitResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBraketClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBraketClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> (
        "capo_braket.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Shows the tags associated with this resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> for the resource whose tags to display.</p>

        Raises:
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_braket._operations.braket.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: str,
        tags: "capo_braket.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.tag_resource_response.TagResourceResponse":
        """<p>Add a tag to the specified resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> of the resource to which a tag will be added.</p>
            tags: <p>Specify the tags to add to the resource. Tags can be specified as a key-value map.</p>

        Raises:
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_braket._operations.braket.tag_resource

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_braket.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> for the resource from which to remove the tags.</p>
            tag_keys: <p>Specify the keys for the tags to remove from the resource.</p>

        Raises:
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_braket._operations.braket.untag_resource

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.untag_resource_request.UntagResourceRequest = {
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

    async def get_device(
        self,
        device_arn: "capo_braket.types.device_arn.DeviceArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.get_device_response.GetDeviceResponse":
        """<p>Retrieves the devices available in Amazon Braket.</p> <note> <p>For backwards compatibility with older versions of BraketSchemas, OpenQASM information is omitted from GetDevice API calls. To get this information the user-agent needs to present a recent version of the BraketSchemas (1.8.0 or later). The Braket SDK automatically reports this for you. If you do not see OpenQASM results in the GetDevice response when using a Braket SDK, you may need to set AWS_EXECUTION_ENV environment variable to configure user-agent. See the code examples provided below for how to do this for the AWS CLI, Boto3, and the Go, Java, and JavaScript/TypeScript SDKs.</p> </note>

        Args:
            device_arn: <p>The ARN of the device to retrieve.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.get_device_request.GetDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.get_device_response.GetDeviceResponse"
        ]:
            import capo_braket._operations.braket.get_device

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.get_device.async_get_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.get_device_request.GetDeviceRequest = {
            "device_arn": device_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_devices(
        self,
        filters: "capo_braket.types.search_devices_filter_list.SearchDevicesFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_braket.types.search_devices_response.SearchDevicesResponse":
        """<p>Searches for devices using the specified filters.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchDevicesFilter objects to use when searching for devices.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.search_devices_request.SearchDevicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.search_devices_response.SearchDevicesResponse"
        ]:
            import capo_braket._operations.braket.search_devices

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.search_devices.async_search_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.search_devices_request.SearchDevicesRequest = {
            "filters": filters
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

    async def iter_search_devices(
        self,
        filters: "capo_braket.types.search_devices_filter_list.SearchDevicesFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_braket.types.device_summary.DeviceSummary]":
        _token = next_token
        while True:
            _response = await self.search_devices(
                filters,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_job(
        self,
        client_token: "capo_braket.types.string64.String64",
        algorithm_specification: "capo_braket.types.algorithm_specification.AlgorithmSpecification",
        output_data_config: "capo_braket.types.job_output_data_config.JobOutputDataConfig",
        job_name: str,
        role_arn: "capo_braket.types.role_arn.RoleArn",
        instance_config: "capo_braket.types.instance_config.InstanceConfig",
        device_config: "capo_braket.types.device_config.DeviceConfig",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        input_data_config: Optional[
            "capo_braket.types.input_config_list.InputConfigList"
        ] = None,
        checkpoint_config: Optional[
            "capo_braket.types.job_checkpoint_config.JobCheckpointConfig"
        ] = None,
        stopping_condition: Optional[
            "capo_braket.types.job_stopping_condition.JobStoppingCondition"
        ] = None,
        hyper_parameters: Optional[
            "capo_braket.types.hyper_parameters.HyperParameters"
        ] = None,
        tags: Optional["capo_braket.types.tags_map.TagsMap"] = None,
        associations: Optional["capo_braket.types.associations.Associations"] = None,
    ) -> "capo_braket.types.create_job_response.CreateJobResponse":
        """<p>Creates an Amazon Braket hybrid job.</p>

        Args:
            client_token: <p>The client token associated with this request that guarantees that the request is idempotent.</p>
            algorithm_specification: <p>Definition of the Amazon Braket job to be created. Specifies the container image the job uses and information about the Python scripts used for entry and training.</p>
            input_data_config: <p>A list of parameters that specify the name and type of input data and where it is located.</p>
            output_data_config: <p>The path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.</p>
            checkpoint_config: <p>Information about the output locations for hybrid job checkpoint data.</p>
            job_name: <p>The name of the Amazon Braket hybrid job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and hybrid job details to the users' s3 buckets.</p>
            stopping_condition: <p> The user-defined criteria that specifies when a hybrid job stops running.</p>
            instance_config: <p>Configuration of the resource instances to use while running the hybrid job on Amazon Braket.</p>
            hyper_parameters: <p>Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the training job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of the hyperparameter.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.</p> </important>
            device_config: <p>The quantum processing unit (QPU) or simulator used to create an Amazon Braket hybrid job.</p>
            tags: <p>Tags to be added to the hybrid job you're creating.</p>
            associations: <p>The list of Amazon Braket resources associated with the hybrid job.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_braket.errors.device_offline_exception.DeviceOfflineException: <p>The specified device is currently offline.</p>
            capo_braket.errors.device_retired_exception.DeviceRetiredException: <p>The specified device has been retired.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.create_job_request.CreateJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.create_job_response.CreateJobResponse"
        ]:
            import capo_braket._operations.braket.create_job

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.create_job.async_create_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.create_job_request.CreateJobRequest = {
            "client_token": client_token,
            "algorithm_specification": algorithm_specification,
            "output_data_config": output_data_config,
            "job_name": job_name,
            "role_arn": role_arn,
            "instance_config": instance_config,
            "device_config": device_config,
        }
        if input_data_config is not None:
            input_["input_data_config"] = input_data_config
        if checkpoint_config is not None:
            input_["checkpoint_config"] = checkpoint_config
        if stopping_condition is not None:
            input_["stopping_condition"] = stopping_condition
        if hyper_parameters is not None:
            input_["hyper_parameters"] = hyper_parameters
        if tags is not None:
            input_["tags"] = tags
        if associations is not None:
            input_["associations"] = associations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_job(
        self,
        job_arn: "capo_braket.types.job_arn.JobArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        additional_attribute_names: Optional[
            "capo_braket.types.hybrid_job_additional_attribute_names_list.HybridJobAdditionalAttributeNamesList"
        ] = None,
    ) -> "capo_braket.types.get_job_response.GetJobResponse":
        """<p>Retrieves the specified Amazon Braket hybrid job.</p>

        Args:
            job_arn: <p>The ARN of the hybrid job to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported. </p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.get_job_request.GetJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.get_job_response.GetJobResponse"
        ]:
            import capo_braket._operations.braket.get_job

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.get_job.async_get_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.get_job_request.GetJobRequest = {"job_arn": job_arn}
        if additional_attribute_names is not None:
            input_["additional_attribute_names"] = additional_attribute_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_job(
        self,
        job_arn: "capo_braket.types.job_arn.JobArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.cancel_job_response.CancelJobResponse":
        """<p>Cancels an Amazon Braket hybrid job.</p>

        Args:
            job_arn: <p>The ARN of the Amazon Braket hybrid job to cancel.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.cancel_job_request.CancelJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.cancel_job_response.CancelJobResponse"
        ]:
            import capo_braket._operations.braket.cancel_job

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.cancel_job.async_cancel_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.cancel_job_request.CancelJobRequest = {
            "job_arn": job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_jobs(
        self,
        filters: "capo_braket.types.search_jobs_filter_list.SearchJobsFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_braket.types.search_jobs_response.SearchJobsResponse":
        """<p>Searches for Amazon Braket hybrid jobs that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchJobsFilter objects to use when searching for hybrid jobs.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.search_jobs_request.SearchJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.search_jobs_response.SearchJobsResponse"
        ]:
            import capo_braket._operations.braket.search_jobs

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.search_jobs.async_search_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.search_jobs_request.SearchJobsRequest = {
            "filters": filters
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

    async def iter_search_jobs(
        self,
        filters: "capo_braket.types.search_jobs_filter_list.SearchJobsFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_braket.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = await self.search_jobs(
                filters,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_quantum_task(
        self,
        client_token: "capo_braket.types.string64.String64",
        device_arn: "capo_braket.types.device_arn.DeviceArn",
        shots: int,
        output_s3_bucket: str,
        output_s3_key_prefix: str,
        action: "capo_braket.types.json_value.JsonValue",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        device_parameters: Optional["capo_braket.types.json_value.JsonValue"] = None,
        tags: Optional["capo_braket.types.tags_map.TagsMap"] = None,
        job_token: Optional["capo_braket.types.job_token.JobToken"] = None,
        associations: Optional["capo_braket.types.associations.Associations"] = None,
        experimental_capabilities: Optional[
            "capo_braket.types.experimental_capabilities.ExperimentalCapabilities"
        ] = None,
    ) -> "capo_braket.types.create_quantum_task_response.CreateQuantumTaskResponse":
        """<p>Creates a quantum task.</p>

        Args:
            client_token: <p>The client token associated with the request.</p>
            device_arn: <p>The ARN of the device to run the quantum task on.</p>
            device_parameters: <p>The parameters for the device to run the quantum task on.</p>
            shots: <p>The number of shots to use for the quantum task.</p>
            output_s3_bucket: <p>The S3 bucket to store quantum task result files in.</p>
            output_s3_key_prefix: <p>The key prefix for the location in the S3 bucket to store quantum task results in.</p>
            action: <p>The action associated with the quantum task.</p>
            tags: <p>Tags to be added to the quantum task you're creating.</p>
            job_token: <p>The token for an Amazon Braket hybrid job that associates it with the quantum task.</p>
            associations: <p>The list of Amazon Braket resources associated with the quantum task.</p>
            experimental_capabilities: <p>Enable experimental capabilities for the quantum task.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.device_offline_exception.DeviceOfflineException: <p>The specified device is currently offline.</p>
            capo_braket.errors.device_retired_exception.DeviceRetiredException: <p>The specified device has been retired.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.create_quantum_task_request.CreateQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.create_quantum_task_response.CreateQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.create_quantum_task

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.create_quantum_task.async_create_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.create_quantum_task_request.CreateQuantumTaskRequest = {
            "client_token": client_token,
            "device_arn": device_arn,
            "shots": shots,
            "output_s3_bucket": output_s3_bucket,
            "output_s3_key_prefix": output_s3_key_prefix,
            "action": action,
        }
        if device_parameters is not None:
            input_["device_parameters"] = device_parameters
        if tags is not None:
            input_["tags"] = tags
        if job_token is not None:
            input_["job_token"] = job_token
        if associations is not None:
            input_["associations"] = associations
        if experimental_capabilities is not None:
            input_["experimental_capabilities"] = experimental_capabilities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_quantum_task(
        self,
        quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        additional_attribute_names: Optional[
            "capo_braket.types.quantum_task_additional_attribute_names_list.QuantumTaskAdditionalAttributeNamesList"
        ] = None,
    ) -> "capo_braket.types.get_quantum_task_response.GetQuantumTaskResponse":
        """<p>Retrieves the specified quantum task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.get_quantum_task_request.GetQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.get_quantum_task_response.GetQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.get_quantum_task

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.get_quantum_task.async_get_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.get_quantum_task_request.GetQuantumTaskRequest = {
            "quantum_task_arn": quantum_task_arn
        }
        if additional_attribute_names is not None:
            input_["additional_attribute_names"] = additional_attribute_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_quantum_task(
        self,
        quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn",
        client_token: "capo_braket.types.string64.String64",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse":
        """<p>Cancels the specified task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to cancel.</p>
            client_token: <p>The client token associated with the cancellation request.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.cancel_quantum_task

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.cancel_quantum_task.async_cancel_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest = {
            "quantum_task_arn": quantum_task_arn,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_quantum_tasks(
        self,
        filters: "capo_braket.types.search_quantum_tasks_filter_list.SearchQuantumTasksFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse":
        """<p>Searches for tasks that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>Maximum number of results to return in the response.</p>
            filters: <p>Array of <code>SearchQuantumTasksFilter</code> objects to use when searching for quantum tasks.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse"
        ]:
            import capo_braket._operations.braket.search_quantum_tasks

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.search_quantum_tasks.async_search_quantum_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest = {
            "filters": filters
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

    async def iter_search_quantum_tasks(
        self,
        filters: "capo_braket.types.search_quantum_tasks_filter_list.SearchQuantumTasksFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_braket.types.quantum_task_summary.QuantumTaskSummary]":
        _token = next_token
        while True:
            _response = await self.search_quantum_tasks(
                filters,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("quantum_tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_spending_limit(
        self,
        client_token: "capo_braket.types.string64.String64",
        device_arn: "capo_braket.types.device_arn.DeviceArn",
        spending_limit: str,
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        time_period: Optional["capo_braket.types.time_period.TimePeriod"] = None,
        tags: Optional["capo_braket.types.tags_map.TagsMap"] = None,
    ) -> "capo_braket.types.create_spending_limit_response.CreateSpendingLimitResponse":
        """<p>Creates a spending limit for a specified quantum device. Spending limits help you control costs by setting maximum amounts that can be spent on quantum computing tasks within a specified time period. Simulators do not support spending limits.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>
            device_arn: <p>The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.</p>
            spending_limit: <p>The maximum amount that can be spent on the specified device, in USD.</p>
            time_period: <p>The time period during which the spending limit is active, including start and end dates.</p>
            tags: <p>The tags to apply to the spending limit. Each tag consists of a key and an optional value.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.device_retired_exception.DeviceRetiredException: <p>The specified device has been retired.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.create_spending_limit_request.CreateSpendingLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.create_spending_limit_response.CreateSpendingLimitResponse"
        ]:
            import capo_braket._operations.braket.create_spending_limit

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.create_spending_limit.async_create_spending_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.create_spending_limit_request.CreateSpendingLimitRequest = {
            "client_token": client_token,
            "device_arn": device_arn,
            "spending_limit": spending_limit,
        }
        if time_period is not None:
            input_["time_period"] = time_period
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_spending_limit(
        self,
        spending_limit_arn: "capo_braket.types.spending_limit_arn.SpendingLimitArn",
        client_token: "capo_braket.types.string64.String64",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        spending_limit: Optional[str] = None,
        time_period: Optional["capo_braket.types.time_period.TimePeriod"] = None,
    ) -> "capo_braket.types.update_spending_limit_response.UpdateSpendingLimitResponse":
        """<p>Updates an existing spending limit. You can modify the spending amount or time period. Changes take effect immediately.</p>

        Args:
            spending_limit_arn: <p>The Amazon Resource Name (ARN) of the spending limit to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>
            spending_limit: <p>The new maximum amount that can be spent on the specified device, in USD.</p>
            time_period: <p>The new time period during which the spending limit is active, including start and end dates.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.update_spending_limit_request.UpdateSpendingLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.update_spending_limit_response.UpdateSpendingLimitResponse"
        ]:
            import capo_braket._operations.braket.update_spending_limit

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.update_spending_limit.async_update_spending_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.update_spending_limit_request.UpdateSpendingLimitRequest = {
            "spending_limit_arn": spending_limit_arn,
            "client_token": client_token,
        }
        if spending_limit is not None:
            input_["spending_limit"] = spending_limit
        if time_period is not None:
            input_["time_period"] = time_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_spending_limit(
        self,
        spending_limit_arn: "capo_braket.types.spending_limit_arn.SpendingLimitArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.delete_spending_limit_response.DeleteSpendingLimitResponse":
        """<p>Deletes an existing spending limit. This operation permanently removes the spending limit and cannot be undone. After deletion, the associated device becomes unrestricted for spending.</p>

        Args:
            spending_limit_arn: <p>The Amazon Resource Name (ARN) of the spending limit to delete.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.delete_spending_limit_request.DeleteSpendingLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.delete_spending_limit_response.DeleteSpendingLimitResponse"
        ]:
            import capo_braket._operations.braket.delete_spending_limit

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.delete_spending_limit.async_delete_spending_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.delete_spending_limit_request.DeleteSpendingLimitRequest = {
            "spending_limit_arn": spending_limit_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_spending_limits(
        self,
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_braket.types.search_spending_limits_filter_list.SearchSpendingLimitsFilterList"
        ] = None,
    ) -> (
        "capo_braket.types.search_spending_limits_response.SearchSpendingLimitsResponse"
    ):
        """<p>Searches and lists spending limits based on specified filters. This operation supports pagination and allows filtering by various criteria to find specific spending limits. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            next_token: <p>The token to retrieve the next page of results. This value is returned from a previous call to SearchSpendingLimits when there are more results available.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 100. Default is 20.</p>
            filters: <p>The filters to apply when searching for spending limits. Use filters to narrow down the results based on specific criteria.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.search_spending_limits_request.SearchSpendingLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.search_spending_limits_response.SearchSpendingLimitsResponse"
        ]:
            import capo_braket._operations.braket.search_spending_limits

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.search_spending_limits.async_search_spending_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.search_spending_limits_request.SearchSpendingLimitsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_spending_limits(
        self,
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_braket.types.search_spending_limits_filter_list.SearchSpendingLimitsFilterList"
        ] = None,
    ) -> "AsyncIterator[capo_braket.types.spending_limit_summary.SpendingLimitSummary]":
        _token = next_token
        while True:
            _response = await self.search_spending_limits(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("spending_limits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MediaConvert``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_mediaconvert._auth._signers
import capo_mediaconvert._auth._sigv4
from capo_mediaconvert._auth._identity import Credentials
from capo_mediaconvert._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediaconvert._auth._zapros_handler import AuthMiddleware
from capo_mediaconvert._pagination import resolve_path as _resolve_path
from capo_mediaconvert._services._aws_config import aaws_config
from capo_mediaconvert._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__integer_min0
    import capo_mediaconvert.types.__integer_min1_max20
    import capo_mediaconvert.types.__integer_min_negative50_max50
    import capo_mediaconvert.types.__list_of__string
    import capo_mediaconvert.types.__list_of_hop_destination
    import capo_mediaconvert.types.__list_of_jobs_query_filter
    import capo_mediaconvert.types.__list_of_probe_input_file
    import capo_mediaconvert.types.__map_of__string
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.acceleration_settings
    import capo_mediaconvert.types.associate_certificate_request
    import capo_mediaconvert.types.associate_certificate_response
    import capo_mediaconvert.types.billing_tags_source
    import capo_mediaconvert.types.cancel_job_request
    import capo_mediaconvert.types.cancel_job_response
    import capo_mediaconvert.types.create_job_request
    import capo_mediaconvert.types.create_job_response
    import capo_mediaconvert.types.create_job_template_request
    import capo_mediaconvert.types.create_job_template_response
    import capo_mediaconvert.types.create_preset_request
    import capo_mediaconvert.types.create_preset_response
    import capo_mediaconvert.types.create_queue_request
    import capo_mediaconvert.types.create_queue_response
    import capo_mediaconvert.types.create_resource_share_request
    import capo_mediaconvert.types.create_resource_share_response
    import capo_mediaconvert.types.delete_job_template_request
    import capo_mediaconvert.types.delete_job_template_response
    import capo_mediaconvert.types.delete_policy_request
    import capo_mediaconvert.types.delete_policy_response
    import capo_mediaconvert.types.delete_preset_request
    import capo_mediaconvert.types.delete_preset_response
    import capo_mediaconvert.types.delete_queue_request
    import capo_mediaconvert.types.delete_queue_response
    import capo_mediaconvert.types.describe_endpoints_mode
    import capo_mediaconvert.types.describe_endpoints_request
    import capo_mediaconvert.types.describe_endpoints_response
    import capo_mediaconvert.types.disassociate_certificate_request
    import capo_mediaconvert.types.disassociate_certificate_response
    import capo_mediaconvert.types.endpoint
    import capo_mediaconvert.types.get_job_request
    import capo_mediaconvert.types.get_job_response
    import capo_mediaconvert.types.get_job_template_request
    import capo_mediaconvert.types.get_job_template_response
    import capo_mediaconvert.types.get_jobs_query_results_request
    import capo_mediaconvert.types.get_jobs_query_results_response
    import capo_mediaconvert.types.get_policy_request
    import capo_mediaconvert.types.get_policy_response
    import capo_mediaconvert.types.get_preset_request
    import capo_mediaconvert.types.get_preset_response
    import capo_mediaconvert.types.get_queue_request
    import capo_mediaconvert.types.get_queue_response
    import capo_mediaconvert.types.job
    import capo_mediaconvert.types.job_engine_version
    import capo_mediaconvert.types.job_settings
    import capo_mediaconvert.types.job_status
    import capo_mediaconvert.types.job_template
    import capo_mediaconvert.types.job_template_list_by
    import capo_mediaconvert.types.job_template_settings
    import capo_mediaconvert.types.list_job_templates_request
    import capo_mediaconvert.types.list_job_templates_response
    import capo_mediaconvert.types.list_jobs_request
    import capo_mediaconvert.types.list_jobs_response
    import capo_mediaconvert.types.list_presets_request
    import capo_mediaconvert.types.list_presets_response
    import capo_mediaconvert.types.list_queues_request
    import capo_mediaconvert.types.list_queues_response
    import capo_mediaconvert.types.list_tags_for_resource_request
    import capo_mediaconvert.types.list_tags_for_resource_response
    import capo_mediaconvert.types.list_versions_request
    import capo_mediaconvert.types.list_versions_response
    import capo_mediaconvert.types.order
    import capo_mediaconvert.types.policy
    import capo_mediaconvert.types.preset
    import capo_mediaconvert.types.preset_list_by
    import capo_mediaconvert.types.preset_settings
    import capo_mediaconvert.types.pricing_plan
    import capo_mediaconvert.types.probe_request
    import capo_mediaconvert.types.probe_response
    import capo_mediaconvert.types.put_policy_request
    import capo_mediaconvert.types.put_policy_response
    import capo_mediaconvert.types.queue
    import capo_mediaconvert.types.queue_list_by
    import capo_mediaconvert.types.queue_status
    import capo_mediaconvert.types.reservation_plan_settings
    import capo_mediaconvert.types.search_jobs_request
    import capo_mediaconvert.types.search_jobs_response
    import capo_mediaconvert.types.simulate_reserved_queue
    import capo_mediaconvert.types.start_jobs_query_request
    import capo_mediaconvert.types.start_jobs_query_response
    import capo_mediaconvert.types.status_update_interval
    import capo_mediaconvert.types.tag_resource_request
    import capo_mediaconvert.types.tag_resource_response
    import capo_mediaconvert.types.untag_resource_request
    import capo_mediaconvert.types.untag_resource_response
    import capo_mediaconvert.types.update_job_template_request
    import capo_mediaconvert.types.update_job_template_response
    import capo_mediaconvert.types.update_preset_request
    import capo_mediaconvert.types.update_preset_response
    import capo_mediaconvert.types.update_queue_request
    import capo_mediaconvert.types.update_queue_response


class AsyncMediaConvertClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMediaConvertClient:
    """A client for the ``MediaConvert`` service.

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
        self._config = AsyncMediaConvertClientConfig(
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
        self, config_overrides: Optional[AsyncMediaConvertClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMediaConvertClientConfig = config_overrides or {}
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

    async def associate_certificate(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        arn: Optional["capo_mediaconvert.types.__string.__string"] = None,
    ) -> "capo_mediaconvert.types.associate_certificate_response.AssociateCertificateResponse":
        """Associates an AWS Certificate Manager (ACM) Amazon Resource Name (ARN) with AWS Elemental MediaConvert.

        Args:
            arn: The ARN of the ACM certificate that you want to associate with your MediaConvert resource.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.associate_certificate_request.AssociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.associate_certificate_response.AssociateCertificateResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.associate_certificate

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.associate_certificate.async_associate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.associate_certificate_request.AssociateCertificateRequest = {}
        if arn is not None:
            input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_job(
        self,
        id: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.cancel_job_response.CancelJobResponse":
        """Permanently cancel a job. Once you have canceled a job, you can't start it again.

        Args:
            id: The Job ID of the job to be cancelled.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.cancel_job_request.CancelJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.cancel_job_response.CancelJobResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.cancel_job

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.cancel_job.async_cancel_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.cancel_job_request.CancelJobRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_job(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        acceleration_settings: Optional[
            "capo_mediaconvert.types.acceleration_settings.AccelerationSettings"
        ] = None,
        billing_tags_source: Optional[
            "capo_mediaconvert.types.billing_tags_source.BillingTagsSource"
        ] = None,
        client_request_token: Optional[
            "capo_mediaconvert.types.__string.__string"
        ] = None,
        hop_destinations: Optional[
            "capo_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
        ] = None,
        job_engine_version: Optional[
            "capo_mediaconvert.types.__string.__string"
        ] = None,
        job_template: Optional["capo_mediaconvert.types.__string.__string"] = None,
        priority: Optional[
            "capo_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
        ] = None,
        queue: Optional["capo_mediaconvert.types.__string.__string"] = None,
        role: Optional["capo_mediaconvert.types.__string.__string"] = None,
        settings: Optional["capo_mediaconvert.types.job_settings.JobSettings"] = None,
        simulate_reserved_queue: Optional[
            "capo_mediaconvert.types.simulate_reserved_queue.SimulateReservedQueue"
        ] = None,
        status_update_interval: Optional[
            "capo_mediaconvert.types.status_update_interval.StatusUpdateInterval"
        ] = None,
        tags: Optional[
            "capo_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
        user_metadata: Optional[
            "capo_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediaconvert.types.create_job_response.CreateJobResponse":
        """Create a new transcoding job. For information about jobs and job settings, see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            acceleration_settings: Optional. Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide.
            billing_tags_source: Optionally choose a Billing tags source that AWS Billing and Cost Management will use to display tags for individual output costs on any billing report that you set up. Leave blank to use the default value, Job.
            client_request_token: Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html.
            hop_destinations: Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide.
            job_engine_version: Use Job engine versions to run jobs for your production workflow on one version, while you test and validate the latest version. Job engine versions represent periodically grouped MediaConvert releases with new features, updates, improvements, and fixes. Job engine versions are in a YYYY-MM-DD format. Note that the Job engine version feature is not publicly available at this time. To request access, contact AWS support.
            job_template: Optional. When you create a job, you can either specify a job template or specify the transcoding settings individually.
            priority: Optional. Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0.
            queue: Optional. When you create a job, you can specify a queue to send it to. If you don't specify, the job will go to the default queue. For more about queues, see the User Guide topic at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html.
            role: Required. The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html.
            settings: JobSettings contains all the transcode settings for a job.
            simulate_reserved_queue: Optional. Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default.
            status_update_interval: Optional. Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.
            tags: Optional. The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. Use standard AWS tags on your job for automatic integration with AWS services and for custom integrations and workflows.
            user_metadata: Optional. User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs. Use only for existing integrations or workflows that rely on job metadata tags. Otherwise, we recommend that you use standard AWS tags.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.create_job_request.CreateJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.create_job_response.CreateJobResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.create_job

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.create_job.async_create_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.create_job_request.CreateJobRequest = {}
        if acceleration_settings is not None:
            input_["acceleration_settings"] = acceleration_settings
        if billing_tags_source is not None:
            input_["billing_tags_source"] = billing_tags_source
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if hop_destinations is not None:
            input_["hop_destinations"] = hop_destinations
        if job_engine_version is not None:
            input_["job_engine_version"] = job_engine_version
        if job_template is not None:
            input_["job_template"] = job_template
        if priority is not None:
            input_["priority"] = priority
        if queue is not None:
            input_["queue"] = queue
        if role is not None:
            input_["role"] = role
        if settings is not None:
            input_["settings"] = settings
        if simulate_reserved_queue is not None:
            input_["simulate_reserved_queue"] = simulate_reserved_queue
        if status_update_interval is not None:
            input_["status_update_interval"] = status_update_interval
        if tags is not None:
            input_["tags"] = tags
        if user_metadata is not None:
            input_["user_metadata"] = user_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_job_template(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        acceleration_settings: Optional[
            "capo_mediaconvert.types.acceleration_settings.AccelerationSettings"
        ] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        description: Optional["capo_mediaconvert.types.__string.__string"] = None,
        hop_destinations: Optional[
            "capo_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
        ] = None,
        name: Optional["capo_mediaconvert.types.__string.__string"] = None,
        priority: Optional[
            "capo_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
        ] = None,
        queue: Optional["capo_mediaconvert.types.__string.__string"] = None,
        settings: Optional[
            "capo_mediaconvert.types.job_template_settings.JobTemplateSettings"
        ] = None,
        status_update_interval: Optional[
            "capo_mediaconvert.types.status_update_interval.StatusUpdateInterval"
        ] = None,
        tags: Optional[
            "capo_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> (
        "capo_mediaconvert.types.create_job_template_response.CreateJobTemplateResponse"
    ):
        """Create a new job template. For information about job templates see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            acceleration_settings: Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide.
            category: Optional. A category for the job template you are creating
            description: Optional. A description of the job template you are creating.
            hop_destinations: Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide.
            name: The name of the job template you are creating.
            priority: Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0.
            queue: Optional. The queue that jobs created from this template are assigned to. If you don't specify this, jobs will go to the default queue.
            settings: JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it.
            status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.create_job_template_request.CreateJobTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.create_job_template_response.CreateJobTemplateResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.create_job_template

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.create_job_template.async_create_job_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.create_job_template_request.CreateJobTemplateRequest = {}
        if acceleration_settings is not None:
            input_["acceleration_settings"] = acceleration_settings
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        if hop_destinations is not None:
            input_["hop_destinations"] = hop_destinations
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority
        if queue is not None:
            input_["queue"] = queue
        if settings is not None:
            input_["settings"] = settings
        if status_update_interval is not None:
            input_["status_update_interval"] = status_update_interval
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_preset(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        description: Optional["capo_mediaconvert.types.__string.__string"] = None,
        name: Optional["capo_mediaconvert.types.__string.__string"] = None,
        settings: Optional[
            "capo_mediaconvert.types.preset_settings.PresetSettings"
        ] = None,
        tags: Optional[
            "capo_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediaconvert.types.create_preset_response.CreatePresetResponse":
        """Create a new preset. For information about job templates see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            category: Optional. A category for the preset you are creating.
            description: Optional. A description of the preset you are creating.
            name: The name of the preset you are creating.
            settings: Settings for preset
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.create_preset_request.CreatePresetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.create_preset_response.CreatePresetResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.create_preset

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.create_preset.async_create_preset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.create_preset_request.CreatePresetRequest = {}
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if settings is not None:
            input_["settings"] = settings
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_queue(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        concurrent_jobs: Optional["capo_mediaconvert.types.__integer.__integer"] = None,
        description: Optional["capo_mediaconvert.types.__string.__string"] = None,
        maximum_concurrent_feeds: Optional[
            "capo_mediaconvert.types.__integer_min0.__integerMin0"
        ] = None,
        name: Optional["capo_mediaconvert.types.__string.__string"] = None,
        pricing_plan: Optional[
            "capo_mediaconvert.types.pricing_plan.PricingPlan"
        ] = None,
        reservation_plan_settings: Optional[
            "capo_mediaconvert.types.reservation_plan_settings.ReservationPlanSettings"
        ] = None,
        status: Optional["capo_mediaconvert.types.queue_status.QueueStatus"] = None,
        tags: Optional[
            "capo_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediaconvert.types.create_queue_response.CreateQueueResponse":
        """Create a new transcoding queue. For information about queues, see Working With Queues in the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html

        Args:
            concurrent_jobs: Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, specify the number of jobs you can process concurrently in your reservation plan instead.
            description: Optional. A description of the queue that you are creating.
            maximum_concurrent_feeds: Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently.
            name: The name of the queue that you are creating.
            pricing_plan: Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. When you use the API to create a queue, the default is on-demand.
            reservation_plan_settings: Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.
            status: Initial state of the queue. If you create a paused queue, then jobs in that queue won't begin.
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.create_queue_request.CreateQueueRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.create_queue_response.CreateQueueResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.create_queue

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.create_queue.async_create_queue(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.create_queue_request.CreateQueueRequest = {}
        if concurrent_jobs is not None:
            input_["concurrent_jobs"] = concurrent_jobs
        if description is not None:
            input_["description"] = description
        if maximum_concurrent_feeds is not None:
            input_["maximum_concurrent_feeds"] = maximum_concurrent_feeds
        if name is not None:
            input_["name"] = name
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if reservation_plan_settings is not None:
            input_["reservation_plan_settings"] = reservation_plan_settings
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resource_share(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        job_id: Optional["capo_mediaconvert.types.__string.__string"] = None,
        support_case_id: Optional["capo_mediaconvert.types.__string.__string"] = None,
    ) -> "capo_mediaconvert.types.create_resource_share_response.CreateResourceShareResponse":
        """Create a new resource share request for MediaConvert resources with AWS Support.

        Args:
            job_id: Specify MediaConvert Job ID or ARN to share
            support_case_id: AWS Support case identifier

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.create_resource_share_request.CreateResourceShareRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.create_resource_share_response.CreateResourceShareResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.create_resource_share

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.create_resource_share.async_create_resource_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.create_resource_share_request.CreateResourceShareRequest = {}
        if job_id is not None:
            input_["job_id"] = job_id
        if support_case_id is not None:
            input_["support_case_id"] = support_case_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_job_template(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> (
        "capo_mediaconvert.types.delete_job_template_response.DeleteJobTemplateResponse"
    ):
        """Permanently delete a job template you have created.

        Args:
            name: The name of the job template to be deleted.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.delete_job_template_request.DeleteJobTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.delete_job_template_response.DeleteJobTemplateResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.delete_job_template

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.delete_job_template.async_delete_job_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.delete_job_template_request.DeleteJobTemplateRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_policy(
        self, *, config_overrides: Optional[AsyncMediaConvertClientConfig] = None
    ) -> "capo_mediaconvert.types.delete_policy_response.DeletePolicyResponse":
        """Permanently delete a policy that you created.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.delete_policy_request.DeletePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.delete_policy_response.DeletePolicyResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.delete_policy

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.delete_policy.async_delete_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.delete_policy_request.DeletePolicyRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_preset(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.delete_preset_response.DeletePresetResponse":
        """Permanently delete a preset you have created.

        Args:
            name: The name of the preset to be deleted.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.delete_preset_request.DeletePresetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.delete_preset_response.DeletePresetResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.delete_preset

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.delete_preset.async_delete_preset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.delete_preset_request.DeletePresetRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_queue(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.delete_queue_response.DeleteQueueResponse":
        """Permanently delete a queue you have created.

        Args:
            name: The name of the queue that you want to delete.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.delete_queue_request.DeleteQueueRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.delete_queue_response.DeleteQueueResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.delete_queue

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.delete_queue.async_delete_queue(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.delete_queue_request.DeleteQueueRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        max_results: Optional["capo_mediaconvert.types.__integer.__integer"] = None,
        mode: Optional[
            "capo_mediaconvert.types.describe_endpoints_mode.DescribeEndpointsMode"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
    ) -> (
        "capo_mediaconvert.types.describe_endpoints_response.DescribeEndpointsResponse"
    ):
        """Send a request with an empty body to the regional API endpoint to get your account API endpoint. Note that DescribeEndpoints is no longer required. We recommend that you send your requests directly to the regional endpoint instead.

        Args:
            max_results: Optional. Max number of endpoints, up to twenty, that will be returned at one time.
            mode: Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn't already exist. Specify GET_ONLY to return your endpoints if any exist, or an empty list if none exist.
            next_token: Use this string, provided with the response to a previous request, to request the next batch of endpoints.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.describe_endpoints_request.DescribeEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.describe_endpoints_response.DescribeEndpointsResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.describe_endpoints

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.describe_endpoints.async_describe_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.describe_endpoints_request.DescribeEndpointsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if mode is not None:
            input_["mode"] = mode
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        max_results: Optional["capo_mediaconvert.types.__integer.__integer"] = None,
        mode: Optional[
            "capo_mediaconvert.types.describe_endpoints_mode.DescribeEndpointsMode"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_mediaconvert.types.endpoint.Endpoint]":
        _token = next_token
        while True:
            _response = await self.describe_endpoints(
                config_overrides=config_overrides,
                max_results=max_results,
                mode=mode,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disassociate_certificate(
        self,
        arn: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.disassociate_certificate_response.DisassociateCertificateResponse":
        """Removes an association between the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert resource.

        Args:
            arn: The ARN of the ACM certificate that you want to disassociate from your MediaConvert resource.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.disassociate_certificate_request.DisassociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.disassociate_certificate_response.DisassociateCertificateResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.disassociate_certificate

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.disassociate_certificate.async_disassociate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.disassociate_certificate_request.DisassociateCertificateRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_job(
        self,
        id: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.get_job_response.GetJobResponse":
        """Retrieve the JSON for a specific transcoding job.

        Args:
            id: the job ID of the job.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.get_job_request.GetJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.get_job_response.GetJobResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.get_job

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.get_job.async_get_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.get_job_request.GetJobRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_jobs_query_results(
        self,
        id: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.get_jobs_query_results_response.GetJobsQueryResultsResponse":
        """Retrieve a JSON array of up to twenty of your most recent jobs matched by a jobs query.

        Args:
            id: The ID of the jobs query.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.get_jobs_query_results_request.GetJobsQueryResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.get_jobs_query_results_response.GetJobsQueryResultsResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.get_jobs_query_results

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.get_jobs_query_results.async_get_jobs_query_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.get_jobs_query_results_request.GetJobsQueryResultsRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_job_template(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.get_job_template_response.GetJobTemplateResponse":
        """Retrieve the JSON for a specific job template.

        Args:
            name: The name of the job template.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.get_job_template_request.GetJobTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.get_job_template_response.GetJobTemplateResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.get_job_template

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.get_job_template.async_get_job_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.get_job_template_request.GetJobTemplateRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_policy(
        self, *, config_overrides: Optional[AsyncMediaConvertClientConfig] = None
    ) -> "capo_mediaconvert.types.get_policy_response.GetPolicyResponse":
        """Retrieve the JSON for your policy.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.get_policy_request.GetPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.get_policy

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.get_policy.async_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.get_policy_request.GetPolicyRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_preset(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.get_preset_response.GetPresetResponse":
        """Retrieve the JSON for a specific preset.

        Args:
            name: The name of the preset.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.get_preset_request.GetPresetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.get_preset_response.GetPresetResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.get_preset

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.get_preset.async_get_preset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.get_preset_request.GetPresetRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_queue(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.get_queue_response.GetQueueResponse":
        """Retrieve the JSON for a specific queue.

        Args:
            name: The name of the queue that you want information about.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.get_queue_request.GetQueueRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.get_queue_response.GetQueueResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.get_queue

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.get_queue.async_get_queue(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.get_queue_request.GetQueueRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
        queue: Optional["capo_mediaconvert.types.__string.__string"] = None,
        status: Optional["capo_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "capo_mediaconvert.types.list_jobs_response.ListJobsResponse":
        """Retrieve a JSON array of up to twenty of your most recently created jobs. This array includes in-process, completed, and errored jobs. This will return the jobs themselves, not just a list of the jobs. To retrieve the twenty next most recent jobs, use the nextToken string returned with the array.

        Args:
            max_results: Optional. Number of jobs, up to twenty, that will be returned at one time.
            next_token: Optional. Use this string, provided with the response to a previous request, to request the next batch of jobs.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
            queue: Optional. Provide a queue name to get back only jobs from that queue.
            status: Optional. A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.list_jobs_request.ListJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.list_jobs_response.ListJobsResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.list_jobs

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.list_jobs_request.ListJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order
        if queue is not None:
            input_["queue"] = queue
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
        queue: Optional["capo_mediaconvert.types.__string.__string"] = None,
        status: Optional["capo_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "AsyncIterator[capo_mediaconvert.types.job.Job]":
        _token = next_token
        while True:
            _response = await self.list_jobs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                order=order,
                queue=queue,
                status=status,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_job_templates(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        list_by: Optional[
            "capo_mediaconvert.types.job_template_list_by.JobTemplateListBy"
        ] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
    ) -> "capo_mediaconvert.types.list_job_templates_response.ListJobTemplatesResponse":
        """Retrieve a JSON array of up to twenty of your job templates. This will return the templates themselves, not just a list of them. To retrieve the next twenty templates, use the nextToken string returned with the array

        Args:
            category: Optionally, specify a job template category to limit responses to only job templates from that category.
            list_by: Optional. When you request a list of job templates, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name.
            max_results: Optional. Number of job templates, up to twenty, that will be returned at one time.
            next_token: Use this string, provided with the response to a previous request, to request the next batch of job templates.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.list_job_templates_request.ListJobTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.list_job_templates_response.ListJobTemplatesResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.list_job_templates

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.list_job_templates.async_list_job_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.list_job_templates_request.ListJobTemplatesRequest = {}
        if category is not None:
            input_["category"] = category
        if list_by is not None:
            input_["list_by"] = list_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_job_templates(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        list_by: Optional[
            "capo_mediaconvert.types.job_template_list_by.JobTemplateListBy"
        ] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
    ) -> "AsyncIterator[capo_mediaconvert.types.job_template.JobTemplate]":
        _token = next_token
        while True:
            _response = await self.list_job_templates(
                config_overrides=config_overrides,
                category=category,
                list_by=list_by,
                max_results=max_results,
                next_token=_token,
                order=order,
            )
            _page = _resolve_path(_response, ("job_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_presets(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        list_by: Optional["capo_mediaconvert.types.preset_list_by.PresetListBy"] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
    ) -> "capo_mediaconvert.types.list_presets_response.ListPresetsResponse":
        """Retrieve a JSON array of up to twenty of your presets. This will return the presets themselves, not just a list of them. To retrieve the next twenty presets, use the nextToken string returned with the array.

        Args:
            category: Optionally, specify a preset category to limit responses to only presets from that category.
            list_by: Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name.
            max_results: Optional. Number of presets, up to twenty, that will be returned at one time
            next_token: Use this string, provided with the response to a previous request, to request the next batch of presets.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.list_presets_request.ListPresetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.list_presets_response.ListPresetsResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.list_presets

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.list_presets.async_list_presets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.list_presets_request.ListPresetsRequest = {}
        if category is not None:
            input_["category"] = category
        if list_by is not None:
            input_["list_by"] = list_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_presets(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        list_by: Optional["capo_mediaconvert.types.preset_list_by.PresetListBy"] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
    ) -> "AsyncIterator[capo_mediaconvert.types.preset.Preset]":
        _token = next_token
        while True:
            _response = await self.list_presets(
                config_overrides=config_overrides,
                category=category,
                list_by=list_by,
                max_results=max_results,
                next_token=_token,
                order=order,
            )
            _page = _resolve_path(_response, ("presets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_queues(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        list_by: Optional["capo_mediaconvert.types.queue_list_by.QueueListBy"] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
    ) -> "capo_mediaconvert.types.list_queues_response.ListQueuesResponse":
        """Retrieve a JSON array of up to twenty of your queues. This will return the queues themselves, not just a list of them. To retrieve the next twenty queues, use the nextToken string returned with the array.

        Args:
            list_by: Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by creation date.
            max_results: Optional. Number of queues, up to twenty, that will be returned at one time.
            next_token: Use this string, provided with the response to a previous request, to request the next batch of queues.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.list_queues_request.ListQueuesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.list_queues_response.ListQueuesResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.list_queues

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.list_queues.async_list_queues(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.list_queues_request.ListQueuesRequest = {}
        if list_by is not None:
            input_["list_by"] = list_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_queues(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        list_by: Optional["capo_mediaconvert.types.queue_list_by.QueueListBy"] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
    ) -> "AsyncIterator[capo_mediaconvert.types.queue.Queue]":
        _token = next_token
        while True:
            _response = await self.list_queues(
                config_overrides=config_overrides,
                list_by=list_by,
                max_results=max_results,
                next_token=_token,
                order=order,
            )
            _page = _resolve_path(_response, ("queues",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        arn: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
    ) -> "capo_mediaconvert.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Retrieve the tags for a MediaConvert resource.

        Args:
            arn: The Amazon Resource Name (ARN) of the resource that you want to list tags for. To get the ARN, send a GET request with the resource name.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
        }

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
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
    ) -> "capo_mediaconvert.types.list_versions_response.ListVersionsResponse":
        """Retrieve a JSON array of all available Job engine versions and the date they expire.

        Args:
            max_results: Optional. Number of valid Job engine versions, up to twenty, that will be returned at one time.
            next_token: Optional. Use this string, provided with the response to a previous request, to request the next batch of Job engine versions.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.list_versions_request.ListVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.list_versions_response.ListVersionsResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.list_versions

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.list_versions.async_list_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.list_versions_request.ListVersionsRequest = {}
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
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_mediaconvert.types.job_engine_version.JobEngineVersion]":
        _token = next_token
        while True:
            _response = await self.list_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def probe(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        input_files: Optional[
            "capo_mediaconvert.types.__list_of_probe_input_file.__listOfProbeInputFile"
        ] = None,
    ) -> "capo_mediaconvert.types.probe_response.ProbeResponse":
        """Use Probe to obtain detailed information about your input media files. Probe returns a JSON that includes container, codec, frame rate, resolution, track count, audio layout, captions, and more. You can use this information to learn more about your media files, or to help make decisions while automating your transcoding workflow. Probe supports the following input container formats: MP4, QuickTime (MOV), 3GP, 3G2, Matroska (MKV), WebM, MXF, MPEG-TS, MPEG-PS, AVI, WAV, MP3, FLAC, Ogg, and ASF (Windows Media / WMA). The fields that Probe returns vary by container and codec. A field isn't returned when the source doesn't contain it, or when it isn't available for that container and codec.

        Args:
            input_files: Specify a media file to probe.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.unprocessable_entity_exception.UnprocessableEntityException: The input file was recognized but appears to be malformed or corrupt.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.probe_request.ProbeRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.probe_response.ProbeResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.probe

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.probe.async_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.probe_request.ProbeRequest = {}
        if input_files is not None:
            input_["input_files"] = input_files

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_policy(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        policy: Optional["capo_mediaconvert.types.policy.Policy"] = None,
    ) -> "capo_mediaconvert.types.put_policy_response.PutPolicyResponse":
        """Create or change your policy. For more information about policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            policy: A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.put_policy_request.PutPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.put_policy_response.PutPolicyResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.put_policy

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.put_policy.async_put_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.put_policy_request.PutPolicyRequest = {}
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        input_file: Optional["capo_mediaconvert.types.__string.__string"] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
        queue: Optional["capo_mediaconvert.types.__string.__string"] = None,
        status: Optional["capo_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "capo_mediaconvert.types.search_jobs_response.SearchJobsResponse":
        """Retrieve a JSON array that includes job details for up to twenty of your most recent jobs. Optionally filter results further according to input file, queue, or status. To retrieve the twenty next most recent jobs, use the nextToken string returned with the array.

        Args:
            input_file: Optional. Provide your input file URL or your partial input file name. The maximum length for an input file is 300 characters.
            max_results: Optional. Number of jobs, up to twenty, that will be returned at one time.
            next_token: Optional. Use this string, provided with the response to a previous request, to request the next batch of jobs.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
            queue: Optional. Provide a queue name, or a queue ARN, to return only jobs from that queue.
            status: Optional. A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.search_jobs_request.SearchJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.search_jobs_response.SearchJobsResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.search_jobs

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.search_jobs.async_search_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.search_jobs_request.SearchJobsRequest = {}
        if input_file is not None:
            input_["input_file"] = input_file
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order
        if queue is not None:
            input_["queue"] = queue
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        input_file: Optional["capo_mediaconvert.types.__string.__string"] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
        queue: Optional["capo_mediaconvert.types.__string.__string"] = None,
        status: Optional["capo_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "AsyncIterator[capo_mediaconvert.types.job.Job]":
        _token = next_token
        while True:
            _response = await self.search_jobs(
                config_overrides=config_overrides,
                input_file=input_file,
                max_results=max_results,
                next_token=_token,
                order=order,
                queue=queue,
                status=status,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_jobs_query(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        filter_list: Optional[
            "capo_mediaconvert.types.__list_of_jobs_query_filter.__listOfJobsQueryFilter"
        ] = None,
        max_results: Optional[
            "capo_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["capo_mediaconvert.types.__string.__string"] = None,
        order: Optional["capo_mediaconvert.types.order.Order"] = None,
    ) -> "capo_mediaconvert.types.start_jobs_query_response.StartJobsQueryResponse":
        """Start an asynchronous jobs query using the provided filters. To receive the list of jobs that match your query, call the GetJobsQueryResults API using the query ID returned by this API.

        Args:
            filter_list: Optional. Provide an array of JobsQueryFilters for your StartJobsQuery request.
            max_results: Optional. Number of jobs, up to twenty, that will be included in the jobs query.
            next_token: Use this string to request the next batch of jobs matched by a jobs query.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.start_jobs_query_request.StartJobsQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.start_jobs_query_response.StartJobsQueryResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.start_jobs_query

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.start_jobs_query.async_start_jobs_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.start_jobs_query_request.StartJobsQueryRequest = {}
        if filter_list is not None:
            input_["filter_list"] = filter_list
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        arn: Optional["capo_mediaconvert.types.__string.__string"] = None,
        tags: Optional[
            "capo_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediaconvert.types.tag_resource_response.TagResourceResponse":
        """Add tags to a MediaConvert queue, preset, job, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-mediaconvert-resources.html.

        Args:
            arn: The Amazon Resource Name (ARN) of the resource that you want to tag. To get the ARN, send a GET request with the resource name.
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.tag_resource

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.tag_resource_request.TagResourceRequest = {}
        if arn is not None:
            input_["arn"] = arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        arn: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        tag_keys: Optional[
            "capo_mediaconvert.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_mediaconvert.types.untag_resource_response.UntagResourceResponse":
        """Remove tags from a MediaConvert queue, preset, job, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-mediaconvert-resources.html.

        Args:
            arn: The Amazon Resource Name (ARN) of the resource that you want to remove tags from. To get the ARN, send a GET request with the resource name.
            tag_keys: The keys of the tags that you want to remove from the resource.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.untag_resource

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_job_template(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        acceleration_settings: Optional[
            "capo_mediaconvert.types.acceleration_settings.AccelerationSettings"
        ] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        description: Optional["capo_mediaconvert.types.__string.__string"] = None,
        hop_destinations: Optional[
            "capo_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
        ] = None,
        priority: Optional[
            "capo_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
        ] = None,
        queue: Optional["capo_mediaconvert.types.__string.__string"] = None,
        settings: Optional[
            "capo_mediaconvert.types.job_template_settings.JobTemplateSettings"
        ] = None,
        status_update_interval: Optional[
            "capo_mediaconvert.types.status_update_interval.StatusUpdateInterval"
        ] = None,
    ) -> (
        "capo_mediaconvert.types.update_job_template_response.UpdateJobTemplateResponse"
    ):
        """Modify one of your existing job templates.

        Args:
            acceleration_settings: Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide.
            category: The new category for the job template, if you are changing it.
            description: The new description for the job template, if you are changing it.
            hop_destinations: Optional list of hop destinations.
            name: The name of the job template you are modifying
            priority: Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0.
            queue: The new queue for the job template, if you are changing it.
            settings: JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it.
            status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.update_job_template_request.UpdateJobTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.update_job_template_response.UpdateJobTemplateResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.update_job_template

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.update_job_template.async_update_job_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.update_job_template_request.UpdateJobTemplateRequest = {
            "name": name
        }
        if acceleration_settings is not None:
            input_["acceleration_settings"] = acceleration_settings
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        if hop_destinations is not None:
            input_["hop_destinations"] = hop_destinations
        if priority is not None:
            input_["priority"] = priority
        if queue is not None:
            input_["queue"] = queue
        if settings is not None:
            input_["settings"] = settings
        if status_update_interval is not None:
            input_["status_update_interval"] = status_update_interval

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_preset(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        category: Optional["capo_mediaconvert.types.__string.__string"] = None,
        description: Optional["capo_mediaconvert.types.__string.__string"] = None,
        settings: Optional[
            "capo_mediaconvert.types.preset_settings.PresetSettings"
        ] = None,
    ) -> "capo_mediaconvert.types.update_preset_response.UpdatePresetResponse":
        """Modify one of your existing presets.

        Args:
            category: The new category for the preset, if you are changing it.
            description: The new description for the preset, if you are changing it.
            name: The name of the preset you are modifying.
            settings: Settings for preset

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.update_preset_request.UpdatePresetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.update_preset_response.UpdatePresetResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.update_preset

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.update_preset.async_update_preset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.update_preset_request.UpdatePresetRequest = {
            "name": name
        }
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        if settings is not None:
            input_["settings"] = settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_queue(
        self,
        name: "capo_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaConvertClientConfig] = None,
        concurrent_jobs: Optional["capo_mediaconvert.types.__integer.__integer"] = None,
        description: Optional["capo_mediaconvert.types.__string.__string"] = None,
        maximum_concurrent_feeds: Optional[
            "capo_mediaconvert.types.__integer_min0.__integerMin0"
        ] = None,
        reservation_plan_settings: Optional[
            "capo_mediaconvert.types.reservation_plan_settings.ReservationPlanSettings"
        ] = None,
        status: Optional["capo_mediaconvert.types.queue_status.QueueStatus"] = None,
    ) -> "capo_mediaconvert.types.update_queue_response.UpdateQueueResponse":
        """Modify one of your existing queues.

        Args:
            concurrent_jobs: Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, update your reservation plan instead in order to increase your yearly commitment.
            description: The new description for the queue, if you are changing it.
            maximum_concurrent_feeds: Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently.
            name: The name of the queue that you are modifying.
            reservation_plan_settings: The new details of your pricing plan for your reserved queue. When you set up a new pricing plan to replace an expired one, you enter into another 12-month commitment. When you add capacity to your queue by increasing the number of RTS, you extend the term of your commitment to 12 months from when you add capacity. After you make these commitments, you can't cancel them.
            status: Pause or activate a queue by changing its status between ACTIVE and PAUSED. If you pause a queue, jobs in that queue won't begin. Jobs that are running when you pause the queue continue to run until they finish or result in an error.

        Raises:
            capo_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            capo_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            capo_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            capo_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            capo_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            capo_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            capo_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            capo_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconvert.types.update_queue_request.UpdateQueueRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconvert.types.update_queue_response.UpdateQueueResponse"
        ]:
            import capo_mediaconvert._operations.media_convert.update_queue

            (
                output,
                http_response,
            ) = await capo_mediaconvert._operations.media_convert.update_queue.async_update_queue(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediaconvert.types.update_queue_request.UpdateQueueRequest = {
            "name": name
        }
        if concurrent_jobs is not None:
            input_["concurrent_jobs"] = concurrent_jobs
        if description is not None:
            input_["description"] = description
        if maximum_concurrent_feeds is not None:
            input_["maximum_concurrent_feeds"] = maximum_concurrent_feeds
        if reservation_plan_settings is not None:
            input_["reservation_plan_settings"] = reservation_plan_settings
        if status is not None:
            input_["status"] = status

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

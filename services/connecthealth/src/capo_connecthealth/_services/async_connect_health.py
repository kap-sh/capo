"""Generated from Smithy shape ``com.amazonaws.connecthealth#ConnectHealth``."""

import uuid
import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_connecthealth._auth._signers
import capo_connecthealth._auth._sigv4
from capo_connecthealth._auth._identity import Credentials
from capo_connecthealth._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_connecthealth._auth._zapros_handler import AuthMiddleware
from capo_connecthealth._iter import ensure_async_iterator
from capo_connecthealth._pagination import resolve_path as _resolve_path
from capo_connecthealth._services._aws_config import aaws_config
from capo_connecthealth._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RateLimiter,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    arate_limit,
    aretry,
    awatch_event_stream,
)

if TYPE_CHECKING:
    import capo_connecthealth.types.activate_subscription_input
    import capo_connecthealth.types.activate_subscription_output
    import capo_connecthealth.types.artifact_source_id
    import capo_connecthealth.types.bounded_safe_string
    import capo_connecthealth.types.create_dataset_input
    import capo_connecthealth.types.create_dataset_output
    import capo_connecthealth.types.create_domain_input
    import capo_connecthealth.types.create_domain_output
    import capo_connecthealth.types.create_subscription_input
    import capo_connecthealth.types.create_subscription_output
    import capo_connecthealth.types.create_web_app_configuration
    import capo_connecthealth.types.dataset_config
    import capo_connecthealth.types.dataset_id
    import capo_connecthealth.types.dataset_summary
    import capo_connecthealth.types.dataset_type
    import capo_connecthealth.types.deactivate_subscription_input
    import capo_connecthealth.types.deactivate_subscription_output
    import capo_connecthealth.types.delete_dataset_input
    import capo_connecthealth.types.delete_dataset_output
    import capo_connecthealth.types.delete_domain_input
    import capo_connecthealth.types.delete_domain_output
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.domain_name
    import capo_connecthealth.types.domain_status
    import capo_connecthealth.types.domain_summary
    import capo_connecthealth.types.feedback_artifact_type
    import capo_connecthealth.types.feedback_comments
    import capo_connecthealth.types.get_dataset_input
    import capo_connecthealth.types.get_dataset_output
    import capo_connecthealth.types.get_domain_input
    import capo_connecthealth.types.get_domain_output
    import capo_connecthealth.types.get_medical_coding_job_request
    import capo_connecthealth.types.get_medical_coding_job_response
    import capo_connecthealth.types.get_medical_scribe_listening_session_input
    import capo_connecthealth.types.get_medical_scribe_listening_session_output
    import capo_connecthealth.types.get_patient_insights_job_request
    import capo_connecthealth.types.get_patient_insights_job_response
    import capo_connecthealth.types.get_subscription_input
    import capo_connecthealth.types.get_subscription_output
    import capo_connecthealth.types.idempotency_token
    import capo_connecthealth.types.input_data_config
    import capo_connecthealth.types.insights_context
    import capo_connecthealth.types.job_id
    import capo_connecthealth.types.kms_key_arn
    import capo_connecthealth.types.list_datasets_input
    import capo_connecthealth.types.list_datasets_output
    import capo_connecthealth.types.list_domains_input
    import capo_connecthealth.types.list_domains_output
    import capo_connecthealth.types.list_subscriptions_input
    import capo_connecthealth.types.list_subscriptions_output
    import capo_connecthealth.types.list_tags_for_resource_input
    import capo_connecthealth.types.list_tags_for_resource_output
    import capo_connecthealth.types.medical_codes_encounter_context
    import capo_connecthealth.types.medical_codes_patient_context
    import capo_connecthealth.types.medical_coding_output_data_config
    import capo_connecthealth.types.medical_scribe_input_stream
    import capo_connecthealth.types.medical_scribe_language_code
    import capo_connecthealth.types.medical_scribe_media_encoding
    import capo_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import capo_connecthealth.types.non_empty_string
    import capo_connecthealth.types.output_data_config
    import capo_connecthealth.types.patient_insights_encounter_context
    import capo_connecthealth.types.patient_insights_patient_context
    import capo_connecthealth.types.s3_uri
    import capo_connecthealth.types.scribe_session_id
    import capo_connecthealth.types.sensitive_non_empty_string
    import capo_connecthealth.types.start_medical_coding_job_request
    import capo_connecthealth.types.start_medical_coding_job_response
    import capo_connecthealth.types.start_medical_scribe_listening_session_input
    import capo_connecthealth.types.start_medical_scribe_listening_session_output
    import capo_connecthealth.types.start_patient_insights_job_request
    import capo_connecthealth.types.start_patient_insights_job_response
    import capo_connecthealth.types.submit_feedback_request
    import capo_connecthealth.types.submit_feedback_response
    import capo_connecthealth.types.subscription_description
    import capo_connecthealth.types.subscription_id
    import capo_connecthealth.types.tag_key_list
    import capo_connecthealth.types.tag_map
    import capo_connecthealth.types.tag_resource_input
    import capo_connecthealth.types.untag_resource_input
    import capo_connecthealth.types.user_context


class AsyncConnectHealthClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncConnectHealthClient:
    """A client for the ``ConnectHealth`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        retry_mode: Literal["standard", "adaptive"] | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = AsyncClient(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = RateLimiter()
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
                AsyncClient(raw_handler)
            )
        self._config = AsyncConnectHealthClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncConnectHealthClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        interceptors_.append(arate_limit())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def activate_subscription(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.activate_subscription_output.ActivateSubscriptionOutput":
        """<p>Activates a Subscription to enable billing for a user.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            subscription_id: <p>The unique identifier of the Subscription.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.activate_subscription_input.ActivateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.activate_subscription_output.ActivateSubscriptionOutput"
        ]:
            import capo_connecthealth._operations.connect_health.activate_subscription

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.activate_subscription.async_activate_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ActivateSubscription")
        )
        input_: capo_connecthealth.types.activate_subscription_input.ActivateSubscriptionInput = {
            "domain_id": domain_id,
            "subscription_id": subscription_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        name: "capo_connecthealth.types.bounded_safe_string.BoundedSafeString",
        config: "capo_connecthealth.types.dataset_config.DatasetConfig",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_connecthealth.types.create_dataset_output.CreateDatasetOutput":
        """<p>Creates a Dataset in a Domain and starts building it. A new dataset has the status CREATING. When it's ready to use, its status changes to ACTIVE, or to CREATE_FAILED if it fails to build. To check the status, call GetDataset.</p> <p>This operation is idempotent: if you retry a request with the same clientToken, it returns the dataset that the first request created.</p> <p>For a medical coding dataset, Amazon Connect Health uses the coded examples that are in the s3InputPath when you create the dataset, and writes evaluation scores to the s3OutputPath. Later changes to the s3InputPath don't change the dataset. To use this operation, you must have s3:GetObject and s3:ListBucket permissions for the input location and s3:PutObject permission for the output location, and kms:Decrypt and kms:GenerateDataKey permissions if you encrypt the locations with an AWS KMS key.</p> <p>Datasets are in preview release and are subject to change.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            name: <p>A name for the dataset.</p>
            config: <p>The configuration of the dataset. The member that you set determines the dataset type. You can't change the configuration after you create the dataset.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation returns the dataset that the first request created. If you reuse a clientToken with different parameters, the request fails with ConflictException. Use a new clientToken for a request with different parameters.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.conflict_exception.ConflictException: <p>This error is thrown when a resource update is no longer valid due to assumptions about initial state changing.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.create_dataset_input.CreateDatasetInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.create_dataset_output.CreateDatasetOutput"
        ]:
            import capo_connecthealth._operations.connect_health.create_dataset

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateDataset")
        )
        input_: capo_connecthealth.types.create_dataset_input.CreateDatasetInput = {
            "domain_id": domain_id,
            "name": name,
            "config": config,
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

    async def create_domain(
        self,
        name: "capo_connecthealth.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        kms_key_arn: Optional["capo_connecthealth.types.kms_key_arn.KmsKeyArn"] = None,
        web_app_setup_configuration: Optional[
            "capo_connecthealth.types.create_web_app_configuration.CreateWebAppConfiguration"
        ] = None,
        tags: Optional["capo_connecthealth.types.tag_map.TagMap"] = None,
    ) -> "capo_connecthealth.types.create_domain_output.CreateDomainOutput":
        """<p>Creates a new Domain for managing HealthAgent resources.</p>

        Args:
            name: <p>The name for the new Domain.</p>
            kms_key_arn: <p>The ARN of the KMS key to use for encrypting data in this Domain.</p>
            web_app_setup_configuration: <p>Configuration for the Domain web application. Optional, but if provided all fields are required.</p>
            tags: <p>Tags to associate with the Domain.</p>

        Raises:
            capo_connecthealth.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.create_domain_input.CreateDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.create_domain_output.CreateDomainOutput"
        ]:
            import capo_connecthealth._operations.connect_health.create_domain

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateDomain")
        )
        input_: capo_connecthealth.types.create_domain_input.CreateDomainInput = {
            "name": name
        }
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if web_app_setup_configuration is not None:
            input_["web_app_setup_configuration"] = web_app_setup_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_subscription(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.create_subscription_output.CreateSubscriptionOutput":
        """<p>Creates a new Subscription within a Domain for billing and user management.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.create_subscription_input.CreateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.create_subscription_output.CreateSubscriptionOutput"
        ]:
            import capo_connecthealth._operations.connect_health.create_subscription

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.create_subscription.async_create_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateSubscription")
        )
        input_: capo_connecthealth.types.create_subscription_input.CreateSubscriptionInput = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deactivate_subscription(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.deactivate_subscription_output.DeactivateSubscriptionOutput":
        """<p>Deactivates a Subscription to stop billing for a user.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            subscription_id: <p>The unique identifier of the Subscription.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.deactivate_subscription_input.DeactivateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.deactivate_subscription_output.DeactivateSubscriptionOutput"
        ]:
            import capo_connecthealth._operations.connect_health.deactivate_subscription

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.deactivate_subscription.async_deactivate_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeactivateSubscription")
        )
        input_: capo_connecthealth.types.deactivate_subscription_input.DeactivateSubscriptionInput = {
            "domain_id": domain_id,
            "subscription_id": subscription_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        dataset_id: "capo_connecthealth.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.delete_dataset_output.DeleteDatasetOutput":
        """<p>Starts deleting a Dataset and the resources that Amazon Connect Health built for it. You can delete a dataset whose status is ACTIVE, CREATE_FAILED, or DELETE_FAILED. The dataset moves to DELETING, and then to DELETED. If the delete fails, the dataset moves to DELETE_FAILED, and you can call DeleteDataset again.</p> <p>Medical coding jobs that already use the dataset finish. Amazon Connect Health rejects new requests that specify the dataset.</p> <p>Datasets are in preview release and are subject to change.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            dataset_id: <p>The unique identifier of the dataset to delete.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.conflict_exception.ConflictException: <p>This error is thrown when a resource update is no longer valid due to assumptions about initial state changing.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.delete_dataset_input.DeleteDatasetInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.delete_dataset_output.DeleteDatasetOutput"
        ]:
            import capo_connecthealth._operations.connect_health.delete_dataset

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteDataset")
        )
        input_: capo_connecthealth.types.delete_dataset_input.DeleteDatasetInput = {
            "domain_id": domain_id,
            "dataset_id": dataset_id,
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
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.delete_domain_output.DeleteDomainOutput":
        """<p>Deletes a Domain and all associated resources.</p>

        Args:
            domain_id: <p>The id of the Domain to delete</p>

        Raises:
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.delete_domain_input.DeleteDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import capo_connecthealth._operations.connect_health.delete_domain

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteDomain")
        )
        input_: capo_connecthealth.types.delete_domain_input.DeleteDomainInput = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dataset(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        dataset_id: "capo_connecthealth.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.get_dataset_output.GetDatasetOutput":
        """<p>Retrieves information about a Dataset, including its status and, after it is built, its results. A dataset whose status is DELETED returns ResourceNotFoundException.</p> <p>Datasets are in preview release and are subject to change.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            dataset_id: <p>The unique identifier of the dataset.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.get_dataset_input.GetDatasetInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.get_dataset_output.GetDatasetOutput"
        ]:
            import capo_connecthealth._operations.connect_health.get_dataset

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.get_dataset.async_get_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetDataset")
        )
        input_: capo_connecthealth.types.get_dataset_input.GetDatasetInput = {
            "domain_id": domain_id,
            "dataset_id": dataset_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.get_domain_output.GetDomainOutput":
        """<p>Retrieves information about a Domain.</p>

        Args:
            domain_id: <p>The id of the Domain to get</p>

        Raises:
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.get_domain_input.GetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.get_domain_output.GetDomainOutput"
        ]:
            import capo_connecthealth._operations.connect_health.get_domain

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetDomain")
        )
        input_: capo_connecthealth.types.get_domain_input.GetDomainInput = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_medical_coding_job(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        job_id: "capo_connecthealth.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.get_medical_coding_job_response.GetMedicalCodingJobResponse":
        """<p>Retrieves information about a medical coding job, including its status and, when it succeeds, the location of its results.</p> <p>Medical coding jobs are in preview release and are subject to change.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            job_id: <p>The unique identifier of the medical coding job.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.get_medical_coding_job_request.GetMedicalCodingJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.get_medical_coding_job_response.GetMedicalCodingJobResponse"
        ]:
            import capo_connecthealth._operations.connect_health.get_medical_coding_job

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.get_medical_coding_job.async_get_medical_coding_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_connecthealth.types.get_medical_coding_job_response.GetMedicalCodingJobResponse",
        ) -> dict[str, Any]:
            import capo_connecthealth.types.get_medical_coding_job_response

            return capo_connecthealth.types.get_medical_coding_job_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetMedicalCodingJob", redact_output=_redact_output),
        )
        input_: capo_connecthealth.types.get_medical_coding_job_request.GetMedicalCodingJobRequest = {
            "domain_id": domain_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_medical_scribe_listening_session(
        self,
        session_id: "capo_connecthealth.types.scribe_session_id.ScribeSessionId",
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.get_medical_scribe_listening_session_output.GetMedicalScribeListeningSessionOutput":
        """<p>Retrieves details about an existing Medical Scribe listening session</p>

        Args:
            session_id: <p>The Session identifier</p>
            domain_id: <p>The Domain identifier</p>
            subscription_id: <p>The Subscription identifier</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.get_medical_scribe_listening_session_input.GetMedicalScribeListeningSessionInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.get_medical_scribe_listening_session_output.GetMedicalScribeListeningSessionOutput"
        ]:
            import capo_connecthealth._operations.connect_health.get_medical_scribe_listening_session

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.get_medical_scribe_listening_session.async_get_medical_scribe_listening_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetMedicalScribeListeningSession")
        )
        input_: capo_connecthealth.types.get_medical_scribe_listening_session_input.GetMedicalScribeListeningSessionInput = {
            "session_id": session_id,
            "domain_id": domain_id,
            "subscription_id": subscription_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_patient_insights_job(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        job_id: "capo_connecthealth.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.get_patient_insights_job_response.GetPatientInsightsJobResponse":
        """<p>Get details of a started patient insights job.</p>

        Args:
            domain_id: <p/>
            job_id: <p/>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.get_patient_insights_job_request.GetPatientInsightsJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.get_patient_insights_job_response.GetPatientInsightsJobResponse"
        ]:
            import capo_connecthealth._operations.connect_health.get_patient_insights_job

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.get_patient_insights_job.async_get_patient_insights_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_connecthealth.types.get_patient_insights_job_response.GetPatientInsightsJobResponse",
        ) -> dict[str, Any]:
            import capo_connecthealth.types.get_patient_insights_job_response

            return capo_connecthealth.types.get_patient_insights_job_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetPatientInsightsJob", redact_output=_redact_output),
        )
        input_: capo_connecthealth.types.get_patient_insights_job_request.GetPatientInsightsJobRequest = {
            "domain_id": domain_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.get_subscription_output.GetSubscriptionOutput":
        """<p>Retrieves information about a Subscription.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            subscription_id: <p>The unique identifier of the Subscription.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.get_subscription_input.GetSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.get_subscription_output.GetSubscriptionOutput"
        ]:
            import capo_connecthealth._operations.connect_health.get_subscription

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.get_subscription.async_get_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetSubscription")
        )
        input_: capo_connecthealth.types.get_subscription_input.GetSubscriptionInput = {
            "domain_id": domain_id,
            "subscription_id": subscription_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_datasets(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        type: Optional["capo_connecthealth.types.dataset_type.DatasetType"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_connecthealth.types.list_datasets_output.ListDatasetsOutput":
        """<p>Lists the Datasets in a Domain. You can list only the datasets of one type. The operation doesn't return datasets whose status is DELETED, and the order of the results isn't specified. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>Datasets are in preview release and are subject to change.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            type: <p>Returns only datasets of this type.</p>
            next_token: <p>The token for the next page of results, from a previous ListDatasets response. If you don't specify a value, the operation returns the first page of results.</p>
            max_results: <p>The maximum number of datasets to return in one page. The default is 100.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.list_datasets_input.ListDatasetsInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.list_datasets_output.ListDatasetsOutput"
        ]:
            import capo_connecthealth._operations.connect_health.list_datasets

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListDatasets")
        )
        input_: capo_connecthealth.types.list_datasets_input.ListDatasetsInput = {
            "domain_id": domain_id
        }
        if type is not None:
            input_["type"] = type
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

    async def iter_list_datasets(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        type: Optional["capo_connecthealth.types.dataset_type.DatasetType"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_connecthealth.types.dataset_summary.DatasetSummary]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                domain_id,
                config_overrides=config_overrides,
                type=type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_domains(
        self,
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        status: Optional["capo_connecthealth.types.domain_status.DomainStatus"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_connecthealth.types.list_domains_output.ListDomainsOutput":
        """<p>Lists Domains for a given account.</p>

        Args:
            status: <p>Filter by Domain status.</p>
            max_results: <p>Maximum number of results to return.</p>
            next_token: <p>Token for pagination.</p>

        Raises:
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.list_domains_input.ListDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.list_domains_output.ListDomainsOutput"
        ]:
            import capo_connecthealth._operations.connect_health.list_domains

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListDomains")
        )
        input_: capo_connecthealth.types.list_domains_input.ListDomainsInput = {}
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

    async def iter_list_domains(
        self,
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        status: Optional["capo_connecthealth.types.domain_status.DomainStatus"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_connecthealth.types.domain_summary.DomainSummary]":
        _token = next_token
        while True:
            _response = await self.list_domains(
                config_overrides=config_overrides,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("domains",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscriptions(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_connecthealth.types.list_subscriptions_output.ListSubscriptionsOutput":
        """<p>Lists all Subscriptions within a Domain.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            max_results: <p>Maximum number of results to return.</p>
            next_token: <p>Token for pagination.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.list_subscriptions_input.ListSubscriptionsInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.list_subscriptions_output.ListSubscriptionsOutput"
        ]:
            import capo_connecthealth._operations.connect_health.list_subscriptions

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListSubscriptions")
        )
        input_: capo_connecthealth.types.list_subscriptions_input.ListSubscriptionsInput = {
            "domain_id": domain_id
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

    async def iter_list_subscriptions(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_connecthealth.types.subscription_description.SubscriptionDescription]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "capo_connecthealth.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with the specified resource</p>

        Args:
            resource_arn: <p>The ARN of the resource to list tags for</p>

        Raises:
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_connecthealth._operations.connect_health.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_connecthealth.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_medical_coding_job(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        text: "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        output_data_config: "capo_connecthealth.types.medical_coding_output_data_config.MedicalCodingOutputDataConfig",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        patient_context: Optional[
            "capo_connecthealth.types.medical_codes_patient_context.MedicalCodesPatientContext"
        ] = None,
        encounter_context: Optional[
            "capo_connecthealth.types.medical_codes_encounter_context.MedicalCodesEncounterContext"
        ] = None,
        dataset_id: Optional["capo_connecthealth.types.dataset_id.DatasetId"] = None,
        client_token: Optional[
            "capo_connecthealth.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_connecthealth.types.start_medical_coding_job_response.StartMedicalCodingJobResponse":
        """<p>Starts an asynchronous job that generates medical codes (ICD-10 and CPT) for clinical text. Call GetMedicalCodingJob to check the status of the job. When the job succeeds, Amazon Connect Health writes the results to the output Amazon S3 location.</p> <p>To tailor the codes to your organization, specify an ACTIVE medical coding dataset in the Domain. If you don't specify a dataset, the job uses the general medical coding knowledge base.</p> <p>Medical coding jobs are in preview release and are subject to change.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            text: <p>The clinical text to generate medical codes for, such as a clinical note.</p>
            patient_context: <p>Patient context for the job. Providing this information can improve the accuracy of the medical codes.</p>
            encounter_context: <p>Encounter context for the job. Providing this information can improve the accuracy of the medical codes.</p>
            output_data_config: <p>The output configuration for the job.</p>
            dataset_id: <p>The unique identifier of an ACTIVE medical coding dataset in the Domain to code against. If you don't specify a dataset, the job uses the general medical coding knowledge base.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.conflict_exception.ConflictException: <p>This error is thrown when a resource update is no longer valid due to assumptions about initial state changing.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.start_medical_coding_job_request.StartMedicalCodingJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.start_medical_coding_job_response.StartMedicalCodingJobResponse"
        ]:
            import capo_connecthealth._operations.connect_health.start_medical_coding_job

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.start_medical_coding_job.async_start_medical_coding_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connecthealth.types.start_medical_coding_job_request.StartMedicalCodingJobRequest",
        ) -> dict[str, Any]:
            import capo_connecthealth.types.start_medical_coding_job_request

            return capo_connecthealth.types.start_medical_coding_job_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("StartMedicalCodingJob", redact_input=_redact_input),
        )
        input_: capo_connecthealth.types.start_medical_coding_job_request.StartMedicalCodingJobRequest = {
            "domain_id": domain_id,
            "text": text,
            "output_data_config": output_data_config,
        }
        if patient_context is not None:
            input_["patient_context"] = patient_context
        if encounter_context is not None:
            input_["encounter_context"] = encounter_context
        if dataset_id is not None:
            input_["dataset_id"] = dataset_id
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

    @asynccontextmanager
    async def start_medical_scribe_listening_session(
        self,
        session_id: "capo_connecthealth.types.scribe_session_id.ScribeSessionId",
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId",
        language_code: "capo_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode",
        media_sample_rate_hertz: "capo_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz",
        media_encoding: "capo_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        input_stream: Optional[
            "AsyncIterator[capo_connecthealth.types.medical_scribe_input_stream._MedicalScribeInputStream] | capo_connecthealth.types.medical_scribe_input_stream._MedicalScribeInputStream"
        ] = None,
    ) -> "AsyncGenerator[capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput]":
        """<p>Starts a new Medical Scribe listening session for real-time audio transcription</p>

        Args:
            session_id: <p>The Session identifier</p>
            domain_id: <p>The Domain identifier</p>
            subscription_id: <p>The Subscription identifier</p>
            language_code: <p>The Language Code for the audio in the session</p>
            media_sample_rate_hertz: <p>The sample rate of the input audio</p>
            media_encoding: <p>The encoding for the input audio</p>
            input_stream: <p/>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput"
        ]:
            import capo_connecthealth._operations.connect_health.start_medical_scribe_listening_session

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.start_medical_scribe_listening_session.async_start_medical_scribe_listening_session(
                req.options, req.input
            )
            awatch_event_stream(output, "response_stream", req.options)
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput",
        ) -> dict[str, Any]:
            import capo_connecthealth.types.start_medical_scribe_listening_session_input

            return capo_connecthealth.types.start_medical_scribe_listening_session_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput",
        ) -> dict[str, Any]:
            import capo_connecthealth.types.start_medical_scribe_listening_session_output

            return capo_connecthealth.types.start_medical_scribe_listening_session_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "StartMedicalScribeListeningSession",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput = {
            "session_id": session_id,
            "domain_id": domain_id,
            "subscription_id": subscription_id,
            "language_code": language_code,
            "media_sample_rate_hertz": media_sample_rate_hertz,
            "media_encoding": media_encoding,
        }
        if input_stream is not None:
            input_["input_stream"] = ensure_async_iterator(input_stream)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def start_patient_insights_job(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        patient_context: "capo_connecthealth.types.patient_insights_patient_context.PatientInsightsPatientContext",
        insights_context: "capo_connecthealth.types.insights_context.InsightsContext",
        encounter_context: "capo_connecthealth.types.patient_insights_encounter_context.PatientInsightsEncounterContext",
        user_context: "capo_connecthealth.types.user_context.UserContext",
        input_data_config: "capo_connecthealth.types.input_data_config.InputDataConfig",
        output_data_config: "capo_connecthealth.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        client_token: Optional[
            "capo_connecthealth.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_connecthealth.types.start_patient_insights_job_response.StartPatientInsightsJobResponse":
        """<p>Starts a new patient insights job.</p>

        Args:
            domain_id: <p/>
            patient_context: <p/>
            insights_context: <p/>
            encounter_context: <p/>
            user_context: <p/>
            input_data_config: <p/>
            output_data_config: <p/>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.conflict_exception.ConflictException: <p>This error is thrown when a resource update is no longer valid due to assumptions about initial state changing.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.start_patient_insights_job_request.StartPatientInsightsJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.start_patient_insights_job_response.StartPatientInsightsJobResponse"
        ]:
            import capo_connecthealth._operations.connect_health.start_patient_insights_job

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.start_patient_insights_job.async_start_patient_insights_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connecthealth.types.start_patient_insights_job_request.StartPatientInsightsJobRequest",
        ) -> dict[str, Any]:
            import capo_connecthealth.types.start_patient_insights_job_request

            return capo_connecthealth.types.start_patient_insights_job_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("StartPatientInsightsJob", redact_input=_redact_input),
        )
        input_: capo_connecthealth.types.start_patient_insights_job_request.StartPatientInsightsJobRequest = {
            "domain_id": domain_id,
            "patient_context": patient_context,
            "insights_context": insights_context,
            "encounter_context": encounter_context,
            "user_context": user_context,
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
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

    async def submit_feedback(
        self,
        domain_id: "capo_connecthealth.types.domain_id.DomainId",
        artifact_source_id: "capo_connecthealth.types.artifact_source_id.ArtifactSourceId",
        artifact_type: "capo_connecthealth.types.feedback_artifact_type.FeedbackArtifactType",
        signed_artifact_s3_uri: "capo_connecthealth.types.s3_uri.S3Uri",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        subscription_id: Optional[
            "capo_connecthealth.types.subscription_id.SubscriptionId"
        ] = None,
        generated_artifact_s3_uri: Optional[
            "capo_connecthealth.types.s3_uri.S3Uri"
        ] = None,
        comments: Optional[
            "capo_connecthealth.types.feedback_comments.FeedbackComments"
        ] = None,
        client_token: Optional[
            "capo_connecthealth.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_connecthealth.types.submit_feedback_response.SubmitFeedbackResponse":
        """<p>Submits feedback on a clinical document or a set of medical codes that Amazon Connect Health generated.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            artifact_source_id: <p>The identifier of the artifact source. For a clinical document, this is the session ID. For a set of medical codes, this is the medical coding job ID.</p>
            subscription_id: <p>The unique identifier of the Subscription.</p>
            artifact_type: <p>The type of artifact that you submit feedback for. The following values are valid:</p> <ul> <li> <p>CLINICAL_DOC is the clinical document generated for an ambient documentation session.</p> </li> <li> <p>MEDICAL_CODES is the set of medical codes generated by a medical coding job.</p> </li> </ul>
            signed_artifact_s3_uri: <p>The Amazon Simple Storage Service (Amazon S3) URI of the final artifact that the clinician signed.</p>
            generated_artifact_s3_uri: <p>The Amazon S3 URI of the clinical document or set of medical codes that Amazon Connect Health generated.</p>
            comments: <p>Optional comments about the feedback.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>

        Raises:
            capo_connecthealth.errors.access_denied_exception.AccessDeniedException: <p>This error is thrown when the client does not supply proper credentials to the API.</p>
            capo_connecthealth.errors.internal_server_exception.InternalServerException: <p>This error is thrown when a transient error causes our API to fail.</p>
            capo_connecthealth.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error is thrown when the requested resource is not found.</p>
            capo_connecthealth.errors.throttling_exception.ThrottlingException: <p>This error is thrown when the client exceeds the allowed request rate.</p>
            capo_connecthealth.errors.validation_exception.ValidationException: <p>This error is thrown when the client supplies invalid input to the API.</p>
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.submit_feedback_request.SubmitFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_connecthealth.types.submit_feedback_response.SubmitFeedbackResponse"
        ]:
            import capo_connecthealth._operations.connect_health.submit_feedback

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.submit_feedback.async_submit_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connecthealth.types.submit_feedback_request.SubmitFeedbackRequest",
        ) -> dict[str, Any]:
            import capo_connecthealth.types.submit_feedback_request

            return capo_connecthealth.types.submit_feedback_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("SubmitFeedback", redact_input=_redact_input),
        )
        input_: capo_connecthealth.types.submit_feedback_request.SubmitFeedbackRequest = {
            "domain_id": domain_id,
            "artifact_source_id": artifact_source_id,
            "artifact_type": artifact_type,
            "signed_artifact_s3_uri": signed_artifact_s3_uri,
        }
        if subscription_id is not None:
            input_["subscription_id"] = subscription_id
        if generated_artifact_s3_uri is not None:
            input_["generated_artifact_s3_uri"] = generated_artifact_s3_uri
        if comments is not None:
            input_["comments"] = comments
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

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_connecthealth.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> None:
        """<p>Associates the specified tags with the specified resource</p>

        Args:
            resource_arn: <p>The ARN of the resource to tag</p>
            tags: <p>The tags to add to the resource</p>

        Raises:
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_connecthealth._operations.connect_health.tag_resource

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_connecthealth.types.tag_resource_input.TagResourceInput = {
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
        tag_keys: "capo_connecthealth.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> None:
        """<p>Removes the specified tags from the specified resource</p>

        Args:
            resource_arn: <p>The ARN of the resource to untag</p>
            tag_keys: <p>The tag keys to remove from the resource</p>

        Raises:
            capo_connecthealth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connecthealth.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_connecthealth._operations.connect_health.untag_resource

            (
                output,
                http_response,
            ) = await capo_connecthealth._operations.connect_health.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_connecthealth.types.untag_resource_input.UntagResourceInput = {
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

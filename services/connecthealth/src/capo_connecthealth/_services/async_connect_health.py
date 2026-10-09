"""Generated from Smithy shape ``com.amazonaws.connecthealth#ConnectHealth``."""

import uuid
import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

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
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_connecthealth.types.activate_subscription_input
    import capo_connecthealth.types.activate_subscription_output
    import capo_connecthealth.types.create_domain_input
    import capo_connecthealth.types.create_domain_output
    import capo_connecthealth.types.create_subscription_input
    import capo_connecthealth.types.create_subscription_output
    import capo_connecthealth.types.create_web_app_configuration
    import capo_connecthealth.types.deactivate_subscription_input
    import capo_connecthealth.types.deactivate_subscription_output
    import capo_connecthealth.types.delete_domain_input
    import capo_connecthealth.types.delete_domain_output
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.domain_name
    import capo_connecthealth.types.domain_status
    import capo_connecthealth.types.domain_summary
    import capo_connecthealth.types.get_domain_input
    import capo_connecthealth.types.get_domain_output
    import capo_connecthealth.types.get_medical_scribe_listening_session_input
    import capo_connecthealth.types.get_medical_scribe_listening_session_output
    import capo_connecthealth.types.get_patient_insights_job_request
    import capo_connecthealth.types.get_patient_insights_job_response
    import capo_connecthealth.types.get_subscription_input
    import capo_connecthealth.types.get_subscription_output
    import capo_connecthealth.types.input_data_config
    import capo_connecthealth.types.insights_context
    import capo_connecthealth.types.job_id
    import capo_connecthealth.types.kms_key_arn
    import capo_connecthealth.types.list_domains_input
    import capo_connecthealth.types.list_domains_output
    import capo_connecthealth.types.list_subscriptions_input
    import capo_connecthealth.types.list_subscriptions_output
    import capo_connecthealth.types.list_tags_for_resource_input
    import capo_connecthealth.types.list_tags_for_resource_output
    import capo_connecthealth.types.medical_scribe_input_stream
    import capo_connecthealth.types.medical_scribe_language_code
    import capo_connecthealth.types.medical_scribe_media_encoding
    import capo_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import capo_connecthealth.types.non_empty_string
    import capo_connecthealth.types.output_data_config
    import capo_connecthealth.types.patient_insights_encounter_context
    import capo_connecthealth.types.patient_insights_patient_context
    import capo_connecthealth.types.scribe_session_id
    import capo_connecthealth.types.start_medical_scribe_listening_session_input
    import capo_connecthealth.types.start_medical_scribe_listening_session_output
    import capo_connecthealth.types.start_patient_insights_job_request
    import capo_connecthealth.types.start_patient_insights_job_response
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
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncConnectHealthClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncConnectHealthClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncConnectHealthClientConfig = config_overrides or {}
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

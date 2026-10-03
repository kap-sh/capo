"""Generated from Smithy shape ``com.amazonaws.voiceid#VoiceID``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_voice_id._auth._signers
import capo_voice_id._auth._sigv4
from capo_voice_id._auth._identity import Credentials
from capo_voice_id._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_voice_id._auth._zapros_handler import AuthMiddleware
from capo_voice_id._pagination import resolve_path as _resolve_path
from capo_voice_id._resources.voice_id.domain_resource import DomainResource
from capo_voice_id._services._aws_config import aws_config
from capo_voice_id._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_voice_id.types.amazon_resource_name
    import capo_voice_id.types.associate_fraudster_request
    import capo_voice_id.types.associate_fraudster_response
    import capo_voice_id.types.client_token_string
    import capo_voice_id.types.create_domain_request
    import capo_voice_id.types.create_domain_response
    import capo_voice_id.types.create_watchlist_request
    import capo_voice_id.types.create_watchlist_response
    import capo_voice_id.types.delete_domain_request
    import capo_voice_id.types.delete_fraudster_request
    import capo_voice_id.types.delete_speaker_request
    import capo_voice_id.types.delete_watchlist_request
    import capo_voice_id.types.describe_domain_request
    import capo_voice_id.types.describe_domain_response
    import capo_voice_id.types.describe_fraudster_registration_job_request
    import capo_voice_id.types.describe_fraudster_registration_job_response
    import capo_voice_id.types.describe_fraudster_request
    import capo_voice_id.types.describe_fraudster_response
    import capo_voice_id.types.describe_speaker_enrollment_job_request
    import capo_voice_id.types.describe_speaker_enrollment_job_response
    import capo_voice_id.types.describe_speaker_request
    import capo_voice_id.types.describe_speaker_response
    import capo_voice_id.types.describe_watchlist_request
    import capo_voice_id.types.describe_watchlist_response
    import capo_voice_id.types.description
    import capo_voice_id.types.disassociate_fraudster_request
    import capo_voice_id.types.disassociate_fraudster_response
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.domain_name
    import capo_voice_id.types.domain_summary
    import capo_voice_id.types.enrollment_config
    import capo_voice_id.types.evaluate_session_request
    import capo_voice_id.types.evaluate_session_response
    import capo_voice_id.types.fraudster_id
    import capo_voice_id.types.fraudster_registration_job_status
    import capo_voice_id.types.fraudster_registration_job_summary
    import capo_voice_id.types.fraudster_summary
    import capo_voice_id.types.iam_role_arn
    import capo_voice_id.types.input_data_config
    import capo_voice_id.types.job_id
    import capo_voice_id.types.job_name
    import capo_voice_id.types.list_domains_request
    import capo_voice_id.types.list_domains_response
    import capo_voice_id.types.list_fraudster_registration_jobs_request
    import capo_voice_id.types.list_fraudster_registration_jobs_response
    import capo_voice_id.types.list_fraudsters_request
    import capo_voice_id.types.list_fraudsters_response
    import capo_voice_id.types.list_speaker_enrollment_jobs_request
    import capo_voice_id.types.list_speaker_enrollment_jobs_response
    import capo_voice_id.types.list_speakers_request
    import capo_voice_id.types.list_speakers_response
    import capo_voice_id.types.list_tags_for_resource_request
    import capo_voice_id.types.list_tags_for_resource_response
    import capo_voice_id.types.list_watchlists_request
    import capo_voice_id.types.list_watchlists_response
    import capo_voice_id.types.max_results_for_list
    import capo_voice_id.types.max_results_for_list_domain_fe
    import capo_voice_id.types.next_token
    import capo_voice_id.types.opt_out_speaker_request
    import capo_voice_id.types.opt_out_speaker_response
    import capo_voice_id.types.output_data_config
    import capo_voice_id.types.registration_config
    import capo_voice_id.types.server_side_encryption_configuration
    import capo_voice_id.types.session_name_or_id
    import capo_voice_id.types.speaker_enrollment_job_status
    import capo_voice_id.types.speaker_enrollment_job_summary
    import capo_voice_id.types.speaker_id
    import capo_voice_id.types.speaker_summary
    import capo_voice_id.types.start_fraudster_registration_job_request
    import capo_voice_id.types.start_fraudster_registration_job_response
    import capo_voice_id.types.start_speaker_enrollment_job_request
    import capo_voice_id.types.start_speaker_enrollment_job_response
    import capo_voice_id.types.tag_key_list
    import capo_voice_id.types.tag_list
    import capo_voice_id.types.tag_resource_request
    import capo_voice_id.types.tag_resource_response
    import capo_voice_id.types.untag_resource_request
    import capo_voice_id.types.untag_resource_response
    import capo_voice_id.types.update_domain_request
    import capo_voice_id.types.update_domain_response
    import capo_voice_id.types.update_watchlist_request
    import capo_voice_id.types.update_watchlist_response
    import capo_voice_id.types.watchlist_description
    import capo_voice_id.types.watchlist_id
    import capo_voice_id.types.watchlist_name
    import capo_voice_id.types.watchlist_summary


class VoiceIDClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class VoiceIDClient:
    """A client for the ``VoiceID`` service.

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
        self._config = VoiceIDClientConfig(
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
        self.domain_resource = DomainResource(self)

    def operation_options(
        self, config_overrides: Optional[VoiceIDClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: VoiceIDClientConfig = config_overrides or {}
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

    def associate_fraudster(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId",
        fraudster_id: "capo_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.associate_fraudster_response.AssociateFraudsterResponse":
        """<p>Associates the fraudsters with the watchlist specified in the same domain. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            watchlist_id: <p>The identifier of the watchlist you want to associate with the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster to be associated with the watchlist.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.associate_fraudster_request.AssociateFraudsterRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.associate_fraudster_response.AssociateFraudsterResponse"
        ]:
            import capo_voice_id._operations.voice_id.associate_fraudster

            output, http_response = (
                capo_voice_id._operations.voice_id.associate_fraudster.associate_fraudster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.associate_fraudster_request.AssociateFraudsterRequest = {
            "domain_id": domain_id,
            "watchlist_id": watchlist_id,
            "fraudster_id": fraudster_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_watchlist(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        name: "capo_voice_id.types.watchlist_name.WatchlistName",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        description: Optional[
            "capo_voice_id.types.watchlist_description.WatchlistDescription"
        ] = None,
        client_token: Optional[
            "capo_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_voice_id.types.create_watchlist_response.CreateWatchlistResponse":
        """<p>Creates a watchlist that fraudsters can be a part of.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            name: <p>The name of the watchlist.</p>
            description: <p>A brief description of this watchlist.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.create_watchlist_request.CreateWatchlistRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.create_watchlist_response.CreateWatchlistResponse"
        ]:
            import capo_voice_id._operations.voice_id.create_watchlist

            output, http_response = (
                capo_voice_id._operations.voice_id.create_watchlist.create_watchlist(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.create_watchlist_request.CreateWatchlistRequest = {
            "domain_id": domain_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
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

    def delete_fraudster(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        fraudster_id: "capo_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified fraudster from Voice ID. This action disassociates the fraudster from any watchlists it is a part of.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster you want to delete.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.delete_fraudster_request.DeleteFraudsterRequest]",
        ) -> OperationResponse[None]:
            import capo_voice_id._operations.voice_id.delete_fraudster

            output, http_response = (
                capo_voice_id._operations.voice_id.delete_fraudster.delete_fraudster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.delete_fraudster_request.DeleteFraudsterRequest = {
            "domain_id": domain_id,
            "fraudster_id": fraudster_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_speaker(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        speaker_id: "capo_voice_id.types.speaker_id.SpeakerId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified speaker from Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker.</p>
            speaker_id: <p>The identifier of the speaker you want to delete.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.delete_speaker_request.DeleteSpeakerRequest]",
        ) -> OperationResponse[None]:
            import capo_voice_id._operations.voice_id.delete_speaker

            output, http_response = (
                capo_voice_id._operations.voice_id.delete_speaker.delete_speaker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.delete_speaker_request.DeleteSpeakerRequest = {
            "domain_id": domain_id,
            "speaker_id": speaker_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_watchlist(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified watchlist from Voice ID. This API throws an exception when there are fraudsters in the watchlist that you are trying to delete. You must delete the fraudsters, and then delete the watchlist. Every domain has a default watchlist which cannot be deleted. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            watchlist_id: <p>The identifier of the watchlist to be deleted.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.delete_watchlist_request.DeleteWatchlistRequest]",
        ) -> OperationResponse[None]:
            import capo_voice_id._operations.voice_id.delete_watchlist

            output, http_response = (
                capo_voice_id._operations.voice_id.delete_watchlist.delete_watchlist(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.delete_watchlist_request.DeleteWatchlistRequest = {
            "domain_id": domain_id,
            "watchlist_id": watchlist_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fraudster(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        fraudster_id: "capo_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_fraudster_response.DescribeFraudsterResponse":
        """<p>Describes the specified fraudster.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.describe_fraudster_request.DescribeFraudsterRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.describe_fraudster_response.DescribeFraudsterResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_fraudster

            output, http_response = (
                capo_voice_id._operations.voice_id.describe_fraudster.describe_fraudster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_fraudster_request.DescribeFraudsterRequest = {
            "domain_id": domain_id,
            "fraudster_id": fraudster_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fraudster_registration_job(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        job_id: "capo_voice_id.types.job_id.JobId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_fraudster_registration_job_response.DescribeFraudsterRegistrationJobResponse":
        """<p>Describes the specified fraudster registration job.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster registration job.</p>
            job_id: <p>The identifier of the fraudster registration job you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.describe_fraudster_registration_job_request.DescribeFraudsterRegistrationJobRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.describe_fraudster_registration_job_response.DescribeFraudsterRegistrationJobResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_fraudster_registration_job

            output, http_response = (
                capo_voice_id._operations.voice_id.describe_fraudster_registration_job.describe_fraudster_registration_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_fraudster_registration_job_request.DescribeFraudsterRegistrationJobRequest = {
            "domain_id": domain_id,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_speaker(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        speaker_id: "capo_voice_id.types.speaker_id.SpeakerId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_speaker_response.DescribeSpeakerResponse":
        """<p>Describes the specified speaker.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker.</p>
            speaker_id: <p>The identifier of the speaker you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.describe_speaker_request.DescribeSpeakerRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.describe_speaker_response.DescribeSpeakerResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_speaker

            output, http_response = (
                capo_voice_id._operations.voice_id.describe_speaker.describe_speaker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_speaker_request.DescribeSpeakerRequest = {
            "domain_id": domain_id,
            "speaker_id": speaker_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_speaker_enrollment_job(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        job_id: "capo_voice_id.types.job_id.JobId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_speaker_enrollment_job_response.DescribeSpeakerEnrollmentJobResponse":
        """<p>Describes the specified speaker enrollment job.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker enrollment job.</p>
            job_id: <p>The identifier of the speaker enrollment job you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.describe_speaker_enrollment_job_request.DescribeSpeakerEnrollmentJobRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.describe_speaker_enrollment_job_response.DescribeSpeakerEnrollmentJobResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_speaker_enrollment_job

            output, http_response = (
                capo_voice_id._operations.voice_id.describe_speaker_enrollment_job.describe_speaker_enrollment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_speaker_enrollment_job_request.DescribeSpeakerEnrollmentJobRequest = {
            "domain_id": domain_id,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_watchlist(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_watchlist_response.DescribeWatchlistResponse":
        """<p>Describes the specified watchlist.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            watchlist_id: <p>The identifier of the watchlist that you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.describe_watchlist_request.DescribeWatchlistRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.describe_watchlist_response.DescribeWatchlistResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_watchlist

            output, http_response = (
                capo_voice_id._operations.voice_id.describe_watchlist.describe_watchlist(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_watchlist_request.DescribeWatchlistRequest = {
            "domain_id": domain_id,
            "watchlist_id": watchlist_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_fraudster(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId",
        fraudster_id: "capo_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.disassociate_fraudster_response.DisassociateFraudsterResponse":
        """<p>Disassociates the fraudsters from the watchlist specified. Voice ID always expects a fraudster to be a part of at least one watchlist. If you try to disassociate a fraudster from its only watchlist, a <code>ValidationException</code> is thrown. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            watchlist_id: <p>The identifier of the watchlist that you want to disassociate from the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster to be disassociated from the watchlist.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.disassociate_fraudster_request.DisassociateFraudsterRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.disassociate_fraudster_response.DisassociateFraudsterResponse"
        ]:
            import capo_voice_id._operations.voice_id.disassociate_fraudster

            output, http_response = (
                capo_voice_id._operations.voice_id.disassociate_fraudster.disassociate_fraudster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.disassociate_fraudster_request.DisassociateFraudsterRequest = {
            "domain_id": domain_id,
            "watchlist_id": watchlist_id,
            "fraudster_id": fraudster_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def evaluate_session(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        session_name_or_id: "capo_voice_id.types.session_name_or_id.SessionNameOrId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.evaluate_session_response.EvaluateSessionResponse":
        """<p>Evaluates a specified session based on audio data accumulated during a streaming Amazon Connect Voice ID call.</p>

        Args:
            domain_id: <p>The identifier of the domain where the session started.</p>
            session_name_or_id: <p>The session identifier, or name of the session, that you want to evaluate. In Voice ID integration, this is the Contact-Id.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.evaluate_session_request.EvaluateSessionRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.evaluate_session_response.EvaluateSessionResponse"
        ]:
            import capo_voice_id._operations.voice_id.evaluate_session

            output, http_response = (
                capo_voice_id._operations.voice_id.evaluate_session.evaluate_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.evaluate_session_request.EvaluateSessionRequest = {
            "domain_id": domain_id,
            "session_name_or_id": session_name_or_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_fraudster_registration_jobs(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        job_status: Optional[
            "capo_voice_id.types.fraudster_registration_job_status.FraudsterRegistrationJobStatus"
        ] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_fraudster_registration_jobs_response.ListFraudsterRegistrationJobsResponse":
        """<p>Lists all the fraudster registration jobs in the domain with the given <code>JobStatus</code>. If <code>JobStatus</code> is not provided, this lists all fraudster registration jobs in the given domain. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster registration Jobs.</p>
            job_status: <p>Provides the status of your fraudster registration job.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_fraudster_registration_jobs_request.ListFraudsterRegistrationJobsRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_fraudster_registration_jobs_response.ListFraudsterRegistrationJobsResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_fraudster_registration_jobs

            output, http_response = (
                capo_voice_id._operations.voice_id.list_fraudster_registration_jobs.list_fraudster_registration_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.list_fraudster_registration_jobs_request.ListFraudsterRegistrationJobsRequest = {
            "domain_id": domain_id
        }
        if job_status is not None:
            input_["job_status"] = job_status
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

    def iter_list_fraudster_registration_jobs(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        job_status: Optional[
            "capo_voice_id.types.fraudster_registration_job_status.FraudsterRegistrationJobStatus"
        ] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_voice_id.types.fraudster_registration_job_summary.FraudsterRegistrationJobSummary]":
        _token = next_token
        while True:
            _response = self.list_fraudster_registration_jobs(
                domain_id,
                config_overrides=config_overrides,
                job_status=job_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_fraudsters(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        watchlist_id: Optional["capo_voice_id.types.watchlist_id.WatchlistId"] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_fraudsters_response.ListFraudstersResponse":
        """<p>Lists all fraudsters in a specified watchlist or domain.</p>

        Args:
            domain_id: <p>The identifier of the domain. </p>
            watchlist_id: <p>The identifier of the watchlist. If provided, all fraudsters in the watchlist are listed. If not provided, all fraudsters in the domain are listed.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_fraudsters_request.ListFraudstersRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_fraudsters_response.ListFraudstersResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_fraudsters

            output, http_response = (
                capo_voice_id._operations.voice_id.list_fraudsters.list_fraudsters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.list_fraudsters_request.ListFraudstersRequest = {
            "domain_id": domain_id
        }
        if watchlist_id is not None:
            input_["watchlist_id"] = watchlist_id
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

    def iter_list_fraudsters(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        watchlist_id: Optional["capo_voice_id.types.watchlist_id.WatchlistId"] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_voice_id.types.fraudster_summary.FraudsterSummary]":
        _token = next_token
        while True:
            _response = self.list_fraudsters(
                domain_id,
                config_overrides=config_overrides,
                watchlist_id=watchlist_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fraudster_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_speaker_enrollment_jobs(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        job_status: Optional[
            "capo_voice_id.types.speaker_enrollment_job_status.SpeakerEnrollmentJobStatus"
        ] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_speaker_enrollment_jobs_response.ListSpeakerEnrollmentJobsResponse":
        """<p>Lists all the speaker enrollment jobs in the domain with the specified <code>JobStatus</code>. If <code>JobStatus</code> is not provided, this lists all jobs with all possible speaker enrollment job statuses.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker enrollment jobs.</p>
            job_status: <p>Provides the status of your speaker enrollment Job.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_speaker_enrollment_jobs_request.ListSpeakerEnrollmentJobsRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_speaker_enrollment_jobs_response.ListSpeakerEnrollmentJobsResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_speaker_enrollment_jobs

            output, http_response = (
                capo_voice_id._operations.voice_id.list_speaker_enrollment_jobs.list_speaker_enrollment_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.list_speaker_enrollment_jobs_request.ListSpeakerEnrollmentJobsRequest = {
            "domain_id": domain_id
        }
        if job_status is not None:
            input_["job_status"] = job_status
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

    def iter_list_speaker_enrollment_jobs(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        job_status: Optional[
            "capo_voice_id.types.speaker_enrollment_job_status.SpeakerEnrollmentJobStatus"
        ] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_voice_id.types.speaker_enrollment_job_summary.SpeakerEnrollmentJobSummary]":
        _token = next_token
        while True:
            _response = self.list_speaker_enrollment_jobs(
                domain_id,
                config_overrides=config_overrides,
                job_status=job_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_speakers(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_speakers_response.ListSpeakersResponse":
        """<p>Lists all speakers in a specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_speakers_request.ListSpeakersRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_speakers_response.ListSpeakersResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_speakers

            output, http_response = (
                capo_voice_id._operations.voice_id.list_speakers.list_speakers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.list_speakers_request.ListSpeakersRequest = {
            "domain_id": domain_id
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

    def iter_list_speakers(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_voice_id.types.speaker_summary.SpeakerSummary]":
        _token = next_token
        while True:
            _response = self.list_speakers(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("speaker_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_voice_id.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a specified Voice ID resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Voice ID resource for which you want to list the tags.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_tags_for_resource

            output, http_response = (
                capo_voice_id._operations.voice_id.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_watchlists(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_watchlists_response.ListWatchlistsResponse":
        """<p>Lists all watchlists in a specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_watchlists_request.ListWatchlistsRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_watchlists_response.ListWatchlistsResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_watchlists

            output, http_response = (
                capo_voice_id._operations.voice_id.list_watchlists.list_watchlists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.list_watchlists_request.ListWatchlistsRequest = {
            "domain_id": domain_id
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

    def iter_list_watchlists(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_voice_id.types.watchlist_summary.WatchlistSummary]":
        _token = next_token
        while True:
            _response = self.list_watchlists(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("watchlist_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def opt_out_speaker(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        speaker_id: "capo_voice_id.types.speaker_id.SpeakerId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.opt_out_speaker_response.OptOutSpeakerResponse":
        """<p>Opts out a speaker from Voice ID. A speaker can be opted out regardless of whether or not they already exist in Voice ID. If they don't yet exist, a new speaker is created in an opted out state. If they already exist, their existing status is overridden and they are opted out. Enrollment and evaluation authentication requests are rejected for opted out speakers, and opted out speakers have no voice embeddings stored in Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker.</p>
            speaker_id: <p>The identifier of the speaker you want opted-out.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.opt_out_speaker_request.OptOutSpeakerRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.opt_out_speaker_response.OptOutSpeakerResponse"
        ]:
            import capo_voice_id._operations.voice_id.opt_out_speaker

            output, http_response = (
                capo_voice_id._operations.voice_id.opt_out_speaker.opt_out_speaker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.opt_out_speaker_request.OptOutSpeakerRequest = {
            "domain_id": domain_id,
            "speaker_id": speaker_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_fraudster_registration_job(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        data_access_role_arn: "capo_voice_id.types.iam_role_arn.IamRoleArn",
        input_data_config: "capo_voice_id.types.input_data_config.InputDataConfig",
        output_data_config: "capo_voice_id.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        client_token: Optional[
            "capo_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        job_name: Optional["capo_voice_id.types.job_name.JobName"] = None,
        registration_config: Optional[
            "capo_voice_id.types.registration_config.RegistrationConfig"
        ] = None,
    ) -> "capo_voice_id.types.start_fraudster_registration_job_response.StartFraudsterRegistrationJobResponse":
        """<p>Starts a new batch fraudster registration job using provided details.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            job_name: <p>The name of the new fraudster registration job.</p>
            domain_id: <p>The identifier of the domain that contains the fraudster registration job and in which the fraudsters are registered.</p>
            data_access_role_arn: <p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the Job output file. Refer to the <a href="https://docs.aws.amazon.com/connect/latest/adminguide/voiceid-fraudster-watchlist.html">Create and edit a fraudster watchlist</a> documentation for the permissions needed in this role.</p>
            registration_config: <p>The registration config containing details such as the action to take when a duplicate fraudster is detected, and the similarity threshold to use for detecting a duplicate fraudster. </p>
            input_data_config: <p>The input data config containing an S3 URI for the input manifest file that contains the list of fraudster registration requests.</p>
            output_data_config: <p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.start_fraudster_registration_job_request.StartFraudsterRegistrationJobRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.start_fraudster_registration_job_response.StartFraudsterRegistrationJobResponse"
        ]:
            import capo_voice_id._operations.voice_id.start_fraudster_registration_job

            output, http_response = (
                capo_voice_id._operations.voice_id.start_fraudster_registration_job.start_fraudster_registration_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.start_fraudster_registration_job_request.StartFraudsterRegistrationJobRequest = {
            "domain_id": domain_id,
            "data_access_role_arn": data_access_role_arn,
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if job_name is not None:
            input_["job_name"] = job_name
        if registration_config is not None:
            input_["registration_config"] = registration_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_speaker_enrollment_job(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        data_access_role_arn: "capo_voice_id.types.iam_role_arn.IamRoleArn",
        input_data_config: "capo_voice_id.types.input_data_config.InputDataConfig",
        output_data_config: "capo_voice_id.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        client_token: Optional[
            "capo_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        job_name: Optional["capo_voice_id.types.job_name.JobName"] = None,
        enrollment_config: Optional[
            "capo_voice_id.types.enrollment_config.EnrollmentConfig"
        ] = None,
    ) -> "capo_voice_id.types.start_speaker_enrollment_job_response.StartSpeakerEnrollmentJobResponse":
        """<p>Starts a new batch speaker enrollment job using specified details.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            job_name: <p>A name for your speaker enrollment job.</p>
            domain_id: <p>The identifier of the domain that contains the speaker enrollment job and in which the speakers are enrolled. </p>
            data_access_role_arn: <p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/voiceid-batch-enrollment.html">Batch enrollment using audio data from prior calls</a> for the permissions needed in this role.</p>
            enrollment_config: <p>The enrollment config that contains details such as the action to take when a speaker is already enrolled in Voice ID or when a speaker is identified as a fraudster.</p>
            input_data_config: <p>The input data config containing the S3 location for the input manifest file that contains the list of speaker enrollment requests.</p>
            output_data_config: <p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.start_speaker_enrollment_job_request.StartSpeakerEnrollmentJobRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.start_speaker_enrollment_job_response.StartSpeakerEnrollmentJobResponse"
        ]:
            import capo_voice_id._operations.voice_id.start_speaker_enrollment_job

            output, http_response = (
                capo_voice_id._operations.voice_id.start_speaker_enrollment_job.start_speaker_enrollment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.start_speaker_enrollment_job_request.StartSpeakerEnrollmentJobRequest = {
            "domain_id": domain_id,
            "data_access_role_arn": data_access_role_arn,
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if job_name is not None:
            input_["job_name"] = job_name
        if enrollment_config is not None:
            input_["enrollment_config"] = enrollment_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_voice_id.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_voice_id.types.tag_list.TagList",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a Voice ID resource with the provided list of tags.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Voice ID resource you want to tag.</p>
            tags: <p>The list of tags to assign to the specified resource.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_voice_id._operations.voice_id.tag_resource

            output, http_response = (
                capo_voice_id._operations.voice_id.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_voice_id.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_voice_id.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes specified tags from a specified Amazon Connect Voice ID resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Voice ID resource you want to remove tags from.</p>
            tag_keys: <p>The list of tag keys you want to remove from the specified resource.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_voice_id._operations.voice_id.untag_resource

            output, http_response = (
                capo_voice_id._operations.voice_id.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.untag_resource_request.UntagResourceRequest = {
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

    def update_watchlist(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        name: Optional["capo_voice_id.types.watchlist_name.WatchlistName"] = None,
        description: Optional[
            "capo_voice_id.types.watchlist_description.WatchlistDescription"
        ] = None,
    ) -> "capo_voice_id.types.update_watchlist_response.UpdateWatchlistResponse":
        """<p>Updates the specified watchlist. Every domain has a default watchlist which cannot be updated. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            watchlist_id: <p>The identifier of the watchlist to be updated.</p>
            name: <p>The name of the watchlist.</p>
            description: <p>A brief description about this watchlist.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.update_watchlist_request.UpdateWatchlistRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.update_watchlist_response.UpdateWatchlistResponse"
        ]:
            import capo_voice_id._operations.voice_id.update_watchlist

            output, http_response = (
                capo_voice_id._operations.voice_id.update_watchlist.update_watchlist(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.update_watchlist_request.UpdateWatchlistRequest = {
            "domain_id": domain_id,
            "watchlist_id": watchlist_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain(
        self,
        name: "capo_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        description: Optional["capo_voice_id.types.description.Description"] = None,
        client_token: Optional[
            "capo_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["capo_voice_id.types.tag_list.TagList"] = None,
    ) -> "capo_voice_id.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain that contains all Amazon Connect Voice ID data, such as speakers, fraudsters, customer audio, and voiceprints. Every domain is created with a default watchlist that fraudsters can be a part of.</p>

        Args:
            name: <p>The name of the domain.</p>
            description: <p>A brief description of this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/encryption-at-rest.html#encryption-at-rest-voiceid"> Amazon Connect Voice ID encryption at rest</a> for more details on how the KMS key is used. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A list of tags you want added to the domain.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded the service quota. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas">Voice ID Service Quotas</a> and try your request again.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.create_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.create_domain_request.CreateDomainRequest = {
            "name": name,
            "server_side_encryption_configuration": server_side_encryption_configuration,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_domain(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "capo_voice_id.types.describe_domain_response.DescribeDomainResponse":
        """<p>Describes the specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain that you are describing.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.describe_domain_request.DescribeDomainRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.describe_domain_response.DescribeDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.describe_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.describe_domain.describe_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.describe_domain_request.DescribeDomainRequest = {
            "domain_id": domain_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_domain(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        name: "capo_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        description: Optional["capo_voice_id.types.description.Description"] = None,
    ) -> "capo_voice_id.types.update_domain_response.UpdateDomainResponse":
        """<p>Updates the specified domain. This API has clobber behavior, and clears and replaces all attributes. If an optional field, such as 'Description' is not provided, it is removed from the domain.</p>

        Args:
            domain_id: <p>The identifier of the domain to be updated.</p>
            name: <p>The name of the domain.</p>
            description: <p>A brief description about this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Changing the domain's associated KMS key immediately triggers an asynchronous process to remove dependency on the old KMS key, such that the domain's data can only be accessed using the new KMS key. The domain's <code>ServerSideEncryptionUpdateDetails</code> contains the details for this process.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.update_domain_request.UpdateDomainRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.update_domain_response.UpdateDomainResponse"
        ]:
            import capo_voice_id._operations.voice_id.update_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.update_domain.update_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.update_domain_request.UpdateDomainRequest = {
            "domain_id": domain_id,
            "name": name,
            "server_side_encryption_configuration": server_side_encryption_configuration,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain(
        self,
        domain_id: "capo_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified domain from Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain you want to delete.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.conflict_exception.ConflictException: <p>The request failed due to a conflict. Check the <code>ConflictType</code> and error message for more details.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found. Check the <code>ResourceType</code> and error message for more details.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[None]:
            import capo_voice_id._operations.voice_id.delete_domain

            output, http_response = (
                capo_voice_id._operations.voice_id.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.delete_domain_request.DeleteDomainRequest = {
            "domain_id": domain_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_domains(
        self,
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list_domain_fe.MaxResultsForListDomainFe"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "capo_voice_id.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all the domains in the Amazon Web Services account. </p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>

        Raises:
            capo_voice_id.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. Check the error message and try again.</p>
            capo_voice_id.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unknown error on the server side.</p>
            capo_voice_id.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please slow down your request rate. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas"> Amazon Connect Voice ID Service API throttling quotas </a> and try your request again.</p>
            capo_voice_id.errors.validation_exception.ValidationException: <p>The request failed one or more validations; check the error message for more details.</p>
            capo_voice_id.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_voice_id.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "capo_voice_id.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_voice_id._operations.voice_id.list_domains

            output, http_response = (
                capo_voice_id._operations.voice_id.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_voice_id.types.list_domains_request.ListDomainsRequest = {}
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

    def iter_list_domains(
        self,
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "capo_voice_id.types.max_results_for_list_domain_fe.MaxResultsForListDomainFe"
        ] = None,
        next_token: Optional["capo_voice_id.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_voice_id.types.domain_summary.DomainSummary]":
        _token = next_token
        while True:
            _response = self.list_domains(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("domain_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

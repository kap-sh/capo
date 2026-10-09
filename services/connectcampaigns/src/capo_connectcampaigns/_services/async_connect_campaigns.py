"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#AmazonConnectCampaignService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_connectcampaigns._auth._signers
import capo_connectcampaigns._auth._sigv4
from capo_connectcampaigns._auth._identity import Credentials
from capo_connectcampaigns._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_connectcampaigns._auth._zapros_handler import AuthMiddleware
from capo_connectcampaigns._pagination import resolve_path as _resolve_path
from capo_connectcampaigns._services._aws_config import aaws_config
from capo_connectcampaigns._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_connectcampaigns.types.answer_machine_detection_config
    import capo_connectcampaigns.types.arn
    import capo_connectcampaigns.types.campaign_filters
    import capo_connectcampaigns.types.campaign_id
    import capo_connectcampaigns.types.campaign_id_list
    import capo_connectcampaigns.types.campaign_name
    import capo_connectcampaigns.types.campaign_summary
    import capo_connectcampaigns.types.contact_flow_id
    import capo_connectcampaigns.types.create_campaign_request
    import capo_connectcampaigns.types.create_campaign_response
    import capo_connectcampaigns.types.delete_campaign_request
    import capo_connectcampaigns.types.delete_connect_instance_config_request
    import capo_connectcampaigns.types.delete_instance_onboarding_job_request
    import capo_connectcampaigns.types.describe_campaign_request
    import capo_connectcampaigns.types.describe_campaign_response
    import capo_connectcampaigns.types.dial_request_list
    import capo_connectcampaigns.types.dialer_config
    import capo_connectcampaigns.types.encryption_config
    import capo_connectcampaigns.types.get_campaign_state_batch_request
    import capo_connectcampaigns.types.get_campaign_state_batch_response
    import capo_connectcampaigns.types.get_campaign_state_request
    import capo_connectcampaigns.types.get_campaign_state_response
    import capo_connectcampaigns.types.get_connect_instance_config_request
    import capo_connectcampaigns.types.get_connect_instance_config_response
    import capo_connectcampaigns.types.get_instance_onboarding_job_status_request
    import capo_connectcampaigns.types.get_instance_onboarding_job_status_response
    import capo_connectcampaigns.types.instance_id
    import capo_connectcampaigns.types.list_campaigns_request
    import capo_connectcampaigns.types.list_campaigns_response
    import capo_connectcampaigns.types.list_tags_for_resource_request
    import capo_connectcampaigns.types.list_tags_for_resource_response
    import capo_connectcampaigns.types.max_results
    import capo_connectcampaigns.types.next_token
    import capo_connectcampaigns.types.outbound_call_config
    import capo_connectcampaigns.types.pause_campaign_request
    import capo_connectcampaigns.types.put_dial_request_batch_request
    import capo_connectcampaigns.types.put_dial_request_batch_response
    import capo_connectcampaigns.types.resume_campaign_request
    import capo_connectcampaigns.types.source_phone_number
    import capo_connectcampaigns.types.start_campaign_request
    import capo_connectcampaigns.types.start_instance_onboarding_job_request
    import capo_connectcampaigns.types.start_instance_onboarding_job_response
    import capo_connectcampaigns.types.stop_campaign_request
    import capo_connectcampaigns.types.tag_key_list
    import capo_connectcampaigns.types.tag_map
    import capo_connectcampaigns.types.tag_resource_request
    import capo_connectcampaigns.types.untag_resource_request
    import capo_connectcampaigns.types.update_campaign_dialer_config_request
    import capo_connectcampaigns.types.update_campaign_name_request
    import capo_connectcampaigns.types.update_campaign_outbound_call_config_request


class AsyncConnectCampaignsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncConnectCampaignsClient:
    """A client for the ``ConnectCampaigns`` service.

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
        self._config = AsyncConnectCampaignsClientConfig(
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
        self, config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncConnectCampaignsClientConfig = config_overrides or {}
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

    async def create_campaign(
        self,
        name: "capo_connectcampaigns.types.campaign_name.CampaignName",
        connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId",
        dialer_config: "capo_connectcampaigns.types.dialer_config.DialerConfig",
        outbound_call_config: "capo_connectcampaigns.types.outbound_call_config.OutboundCallConfig",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
        tags: Optional["capo_connectcampaigns.types.tag_map.TagMap"] = None,
    ) -> "capo_connectcampaigns.types.create_campaign_response.CreateCampaignResponse":
        """Creates a campaign for the specified Amazon Connect account. This API is idempotent.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: Request would cause a service quota to be exceeded.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.create_campaign_request.CreateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.create_campaign

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.create_campaign.async_create_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.create_campaign_request.CreateCampaignRequest = {
            "name": name,
            "connect_instance_id": connect_instance_id,
            "dialer_config": dialer_config,
            "outbound_call_config": outbound_call_config,
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

    async def delete_campaign(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Deletes a campaign from the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.delete_campaign

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.delete_campaign.async_delete_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.delete_campaign_request.DeleteCampaignRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connect_instance_config(
        self,
        connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Deletes a connect instance config from the specified AWS account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.invalid_state_exception.InvalidStateException: The request could not be processed because of conflict in the current state.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.delete_connect_instance_config_request.DeleteConnectInstanceConfigRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.delete_connect_instance_config

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.delete_connect_instance_config.async_delete_connect_instance_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.delete_connect_instance_config_request.DeleteConnectInstanceConfigRequest = {
            "connect_instance_id": connect_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_instance_onboarding_job(
        self,
        connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Delete the Connect Campaigns onboarding job for the specified Amazon Connect instance.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.invalid_state_exception.InvalidStateException: The request could not be processed because of conflict in the current state.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.delete_instance_onboarding_job_request.DeleteInstanceOnboardingJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.delete_instance_onboarding_job

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.delete_instance_onboarding_job.async_delete_instance_onboarding_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.delete_instance_onboarding_job_request.DeleteInstanceOnboardingJobRequest = {
            "connect_instance_id": connect_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_campaign(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.describe_campaign_response.DescribeCampaignResponse":
        """Describes the specific campaign.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.describe_campaign_request.DescribeCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.describe_campaign_response.DescribeCampaignResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.describe_campaign

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.describe_campaign.async_describe_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.describe_campaign_request.DescribeCampaignRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_state(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.get_campaign_state_response.GetCampaignStateResponse":
        """Get state of a campaign for the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.get_campaign_state_request.GetCampaignStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.get_campaign_state_response.GetCampaignStateResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state.async_get_campaign_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.get_campaign_state_request.GetCampaignStateRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_state_batch(
        self,
        campaign_ids: "capo_connectcampaigns.types.campaign_id_list.CampaignIdList",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.get_campaign_state_batch_response.GetCampaignStateBatchResponse":
        """Get state of campaigns for the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.get_campaign_state_batch_request.GetCampaignStateBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.get_campaign_state_batch_response.GetCampaignStateBatchResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state_batch

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state_batch.async_get_campaign_state_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.get_campaign_state_batch_request.GetCampaignStateBatchRequest = {
            "campaign_ids": campaign_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connect_instance_config(
        self,
        connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.get_connect_instance_config_response.GetConnectInstanceConfigResponse":
        """Get the specific Connect instance config.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.get_connect_instance_config_request.GetConnectInstanceConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.get_connect_instance_config_response.GetConnectInstanceConfigResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.get_connect_instance_config

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.get_connect_instance_config.async_get_connect_instance_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.get_connect_instance_config_request.GetConnectInstanceConfigRequest = {
            "connect_instance_id": connect_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance_onboarding_job_status(
        self,
        connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.get_instance_onboarding_job_status_response.GetInstanceOnboardingJobStatusResponse":
        """Get the specific instance onboarding job status.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.get_instance_onboarding_job_status_request.GetInstanceOnboardingJobStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.get_instance_onboarding_job_status_response.GetInstanceOnboardingJobStatusResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.get_instance_onboarding_job_status

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.get_instance_onboarding_job_status.async_get_instance_onboarding_job_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.get_instance_onboarding_job_status_request.GetInstanceOnboardingJobStatusRequest = {
            "connect_instance_id": connect_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_campaigns(
        self,
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
        max_results: Optional[
            "capo_connectcampaigns.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_connectcampaigns.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcampaigns.types.campaign_filters.CampaignFilters"
        ] = None,
    ) -> "capo_connectcampaigns.types.list_campaigns_response.ListCampaignsResponse":
        """Provides summary information about the campaigns under the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.list_campaigns

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.list_campaigns.async_list_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.list_campaigns_request.ListCampaignsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_campaigns(
        self,
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
        max_results: Optional[
            "capo_connectcampaigns.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_connectcampaigns.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcampaigns.types.campaign_filters.CampaignFilters"
        ] = None,
    ) -> "AsyncIterator[capo_connectcampaigns.types.campaign_summary.CampaignSummary]":
        _token = next_token
        while True:
            _response = await self.list_campaigns(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("campaign_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        arn: "capo_connectcampaigns.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for a resource.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def pause_campaign(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Pauses a campaign for the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.invalid_campaign_state_exception.InvalidCampaignStateException: The request could not be processed because of conflict in the current state of the campaign.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.pause_campaign_request.PauseCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.pause_campaign

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.pause_campaign.async_pause_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.pause_campaign_request.PauseCampaignRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_dial_request_batch(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        dial_requests: "capo_connectcampaigns.types.dial_request_list.DialRequestList",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.put_dial_request_batch_response.PutDialRequestBatchResponse":
        """Creates dials requests for the specified campaign Amazon Connect account. This API is idempotent.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.invalid_campaign_state_exception.InvalidCampaignStateException: The request could not be processed because of conflict in the current state of the campaign.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.put_dial_request_batch_request.PutDialRequestBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.put_dial_request_batch_response.PutDialRequestBatchResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.put_dial_request_batch

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.put_dial_request_batch.async_put_dial_request_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.put_dial_request_batch_request.PutDialRequestBatchRequest = {
            "id": id,
            "dial_requests": dial_requests,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resume_campaign(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Stops a campaign for the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.invalid_campaign_state_exception.InvalidCampaignStateException: The request could not be processed because of conflict in the current state of the campaign.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.resume_campaign_request.ResumeCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.resume_campaign

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.resume_campaign.async_resume_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.resume_campaign_request.ResumeCampaignRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_campaign(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Starts a campaign for the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.invalid_campaign_state_exception.InvalidCampaignStateException: The request could not be processed because of conflict in the current state of the campaign.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.start_campaign_request.StartCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.start_campaign

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.start_campaign.async_start_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.start_campaign_request.StartCampaignRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_instance_onboarding_job(
        self,
        connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId",
        encryption_config: "capo_connectcampaigns.types.encryption_config.EncryptionConfig",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> "capo_connectcampaigns.types.start_instance_onboarding_job_response.StartInstanceOnboardingJobResponse":
        """Onboard the specific Amazon Connect instance to Connect Campaigns.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.start_instance_onboarding_job_request.StartInstanceOnboardingJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcampaigns.types.start_instance_onboarding_job_response.StartInstanceOnboardingJobResponse"
        ]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.start_instance_onboarding_job

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.start_instance_onboarding_job.async_start_instance_onboarding_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.start_instance_onboarding_job_request.StartInstanceOnboardingJobRequest = {
            "connect_instance_id": connect_instance_id,
            "encryption_config": encryption_config,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_campaign(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Stops a campaign for the specified Amazon Connect account.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.invalid_campaign_state_exception.InvalidCampaignStateException: The request could not be processed because of conflict in the current state of the campaign.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.stop_campaign_request.StopCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.stop_campaign

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.stop_campaign.async_stop_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.stop_campaign_request.StopCampaignRequest = {
            "id": id
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
        arn: "capo_connectcampaigns.types.arn.Arn",
        tags: "capo_connectcampaigns.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Tag a resource.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.tag_resource_request.TagResourceRequest = {
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
        arn: "capo_connectcampaigns.types.arn.Arn",
        tag_keys: "capo_connectcampaigns.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Untag a resource.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_campaign_dialer_config(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        dialer_config: "capo_connectcampaigns.types.dialer_config.DialerConfig",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Updates the dialer config of a campaign. This API is idempotent.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.update_campaign_dialer_config_request.UpdateCampaignDialerConfigRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_dialer_config

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_dialer_config.async_update_campaign_dialer_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.update_campaign_dialer_config_request.UpdateCampaignDialerConfigRequest = {
            "id": id,
            "dialer_config": dialer_config,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_campaign_name(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        name: "capo_connectcampaigns.types.campaign_name.CampaignName",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
    ) -> None:
        """Updates the name of a campaign. This API is idempotent.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.update_campaign_name_request.UpdateCampaignNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_name

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_name.async_update_campaign_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.update_campaign_name_request.UpdateCampaignNameRequest = {
            "id": id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_campaign_outbound_call_config(
        self,
        id: "capo_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncConnectCampaignsClientConfig] = None,
        connect_contact_flow_id: Optional[
            "capo_connectcampaigns.types.contact_flow_id.ContactFlowId"
        ] = None,
        connect_source_phone_number: Optional[
            "capo_connectcampaigns.types.source_phone_number.SourcePhoneNumber"
        ] = None,
        answer_machine_detection_config: Optional[
            "capo_connectcampaigns.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
        ] = None,
    ) -> None:
        """Updates the outbound call config of a campaign. This API is idempotent.

        Raises:
            capo_connectcampaigns.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_connectcampaigns.errors.conflict_exception.ConflictException: The request could not be processed because of conflict in the current state of the resource.
            capo_connectcampaigns.errors.internal_server_exception.InternalServerException: Request processing failed because of an error or failure with the service.
            capo_connectcampaigns.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_connectcampaigns.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_connectcampaigns.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_connectcampaigns.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcampaigns.types.update_campaign_outbound_call_config_request.UpdateCampaignOutboundCallConfigRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_outbound_call_config

            (
                output,
                http_response,
            ) = await capo_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_outbound_call_config.async_update_campaign_outbound_call_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcampaigns.types.update_campaign_outbound_call_config_request.UpdateCampaignOutboundCallConfigRequest = {
            "id": id
        }
        if connect_contact_flow_id is not None:
            input_["connect_contact_flow_id"] = connect_contact_flow_id
        if connect_source_phone_number is not None:
            input_["connect_source_phone_number"] = connect_source_phone_number
        if answer_machine_detection_config is not None:
            input_["answer_machine_detection_config"] = answer_machine_detection_config

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

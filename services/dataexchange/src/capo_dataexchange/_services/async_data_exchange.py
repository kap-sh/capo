"""Generated from Smithy shape ``com.amazonaws.dataexchange#DataExchange``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_dataexchange._auth._signers
import capo_dataexchange._auth._sigv4
from capo_dataexchange._auth._identity import Credentials
from capo_dataexchange._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_dataexchange._auth._zapros_handler import AuthMiddleware
from capo_dataexchange._pagination import resolve_path as _resolve_path
from capo_dataexchange._services._aws_config import aaws_config
from capo_dataexchange._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_dataexchange.types.__boolean
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.__string_min0_max4096
    import capo_dataexchange.types.__string_min0_max16384
    import capo_dataexchange.types.__string_min10_max512
    import capo_dataexchange.types.accept_data_grant_request
    import capo_dataexchange.types.accept_data_grant_response
    import capo_dataexchange.types.acceptance_state_filter_values
    import capo_dataexchange.types.action
    import capo_dataexchange.types.asset_configuration
    import capo_dataexchange.types.asset_entry
    import capo_dataexchange.types.asset_name
    import capo_dataexchange.types.asset_type
    import capo_dataexchange.types.cancel_job_request
    import capo_dataexchange.types.client_token
    import capo_dataexchange.types.create_data_grant_request
    import capo_dataexchange.types.create_data_grant_response
    import capo_dataexchange.types.create_data_set_request
    import capo_dataexchange.types.create_data_set_response
    import capo_dataexchange.types.create_event_action_request
    import capo_dataexchange.types.create_event_action_response
    import capo_dataexchange.types.create_job_request
    import capo_dataexchange.types.create_job_response
    import capo_dataexchange.types.create_revision_request
    import capo_dataexchange.types.create_revision_response
    import capo_dataexchange.types.data_grant_arn
    import capo_dataexchange.types.data_grant_id
    import capo_dataexchange.types.data_grant_name
    import capo_dataexchange.types.data_grant_summary_entry
    import capo_dataexchange.types.data_set_entry
    import capo_dataexchange.types.delete_asset_request
    import capo_dataexchange.types.delete_data_grant_request
    import capo_dataexchange.types.delete_data_set_request
    import capo_dataexchange.types.delete_event_action_request
    import capo_dataexchange.types.delete_revision_request
    import capo_dataexchange.types.description
    import capo_dataexchange.types.event
    import capo_dataexchange.types.event_action_entry
    import capo_dataexchange.types.get_asset_request
    import capo_dataexchange.types.get_asset_response
    import capo_dataexchange.types.get_data_grant_request
    import capo_dataexchange.types.get_data_grant_response
    import capo_dataexchange.types.get_data_set_request
    import capo_dataexchange.types.get_data_set_response
    import capo_dataexchange.types.get_event_action_request
    import capo_dataexchange.types.get_event_action_response
    import capo_dataexchange.types.get_job_request
    import capo_dataexchange.types.get_job_response
    import capo_dataexchange.types.get_received_data_grant_request
    import capo_dataexchange.types.get_received_data_grant_response
    import capo_dataexchange.types.get_revision_request
    import capo_dataexchange.types.get_revision_response
    import capo_dataexchange.types.grant_distribution_scope
    import capo_dataexchange.types.id
    import capo_dataexchange.types.job_entry
    import capo_dataexchange.types.list_data_grants_request
    import capo_dataexchange.types.list_data_grants_response
    import capo_dataexchange.types.list_data_set_revisions_request
    import capo_dataexchange.types.list_data_set_revisions_response
    import capo_dataexchange.types.list_data_sets_request
    import capo_dataexchange.types.list_data_sets_response
    import capo_dataexchange.types.list_event_actions_request
    import capo_dataexchange.types.list_event_actions_response
    import capo_dataexchange.types.list_jobs_request
    import capo_dataexchange.types.list_jobs_response
    import capo_dataexchange.types.list_of__string
    import capo_dataexchange.types.list_received_data_grants_request
    import capo_dataexchange.types.list_received_data_grants_response
    import capo_dataexchange.types.list_revision_assets_request
    import capo_dataexchange.types.list_revision_assets_response
    import capo_dataexchange.types.list_tags_for_resource_request
    import capo_dataexchange.types.list_tags_for_resource_response
    import capo_dataexchange.types.map_of__string
    import capo_dataexchange.types.max_results
    import capo_dataexchange.types.name
    import capo_dataexchange.types.notification_details
    import capo_dataexchange.types.notification_type
    import capo_dataexchange.types.received_data_grant_summaries_entry
    import capo_dataexchange.types.receiver_principal
    import capo_dataexchange.types.request_details
    import capo_dataexchange.types.revision_entry
    import capo_dataexchange.types.revoke_revision_request
    import capo_dataexchange.types.revoke_revision_response
    import capo_dataexchange.types.scope_details
    import capo_dataexchange.types.send_api_asset_request
    import capo_dataexchange.types.send_api_asset_response
    import capo_dataexchange.types.send_data_set_notification_request
    import capo_dataexchange.types.send_data_set_notification_response
    import capo_dataexchange.types.start_job_request
    import capo_dataexchange.types.start_job_response
    import capo_dataexchange.types.tag_resource_request
    import capo_dataexchange.types.timestamp
    import capo_dataexchange.types.type
    import capo_dataexchange.types.untag_resource_request
    import capo_dataexchange.types.update_asset_request
    import capo_dataexchange.types.update_asset_response
    import capo_dataexchange.types.update_data_set_request
    import capo_dataexchange.types.update_data_set_response
    import capo_dataexchange.types.update_event_action_request
    import capo_dataexchange.types.update_event_action_response
    import capo_dataexchange.types.update_revision_request
    import capo_dataexchange.types.update_revision_response


class AsyncDataExchangeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncDataExchangeClient:
    """A client for the ``DataExchange`` service.

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
        self._config = AsyncDataExchangeClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncDataExchangeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDataExchangeClientConfig = config_overrides or {}
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

    async def accept_data_grant(
        self,
        data_grant_arn: "capo_dataexchange.types.data_grant_arn.DataGrantArn",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.accept_data_grant_response.AcceptDataGrantResponse":
        """<p>This operation accepts a data grant.</p>

        Args:
            data_grant_arn: <p>The Amazon Resource Name (ARN) of the data grant to accept.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.accept_data_grant_request.AcceptDataGrantRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.accept_data_grant_response.AcceptDataGrantResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.accept_data_grant

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.accept_data_grant.async_accept_data_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.accept_data_grant_request.AcceptDataGrantRequest = {
            "data_grant_arn": data_grant_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_job(
        self,
        job_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation cancels a job. Jobs can be cancelled only when they are in the WAITING state.</p>

        Args:
            job_id: <p>The unique identifier for a job.</p>

        Raises:
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.cancel_job_request.CancelJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.cancel_job

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.cancel_job.async_cancel_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.cancel_job_request.CancelJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_grant(
        self,
        name: "capo_dataexchange.types.data_grant_name.DataGrantName",
        grant_distribution_scope: "capo_dataexchange.types.grant_distribution_scope.GrantDistributionScope",
        receiver_principal: "capo_dataexchange.types.receiver_principal.ReceiverPrincipal",
        source_data_set_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        ends_at: Optional["capo_dataexchange.types.timestamp.Timestamp"] = None,
        description: Optional["capo_dataexchange.types.description.Description"] = None,
        tags: Optional["capo_dataexchange.types.map_of__string.MapOf__string"] = None,
    ) -> "capo_dataexchange.types.create_data_grant_response.CreateDataGrantResponse":
        """<p>This operation creates a data grant.</p>

        Args:
            name: <p>The name of the data grant.</p>
            grant_distribution_scope: <p>The distribution scope of the data grant.</p>
            receiver_principal: <p>The Amazon Web Services account ID of the data grant receiver.</p>
            source_data_set_id: <p>The ID of the data set used to create the data grant.</p>
            ends_at: <p>The timestamp of when access to the associated data set ends.</p>
            description: <p>The description of the data grant.</p>
            tags: <p>The tags to add to the data grant. A tag is a key-value pair.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request has exceeded the quotas imposed by the service.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.create_data_grant_request.CreateDataGrantRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.create_data_grant_response.CreateDataGrantResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.create_data_grant

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.create_data_grant.async_create_data_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.create_data_grant_request.CreateDataGrantRequest = {
            "name": name,
            "grant_distribution_scope": grant_distribution_scope,
            "receiver_principal": receiver_principal,
            "source_data_set_id": source_data_set_id,
        }
        if ends_at is not None:
            input_["ends_at"] = ends_at
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

    async def create_data_set(
        self,
        asset_type: "capo_dataexchange.types.asset_type.AssetType",
        description: "capo_dataexchange.types.description.Description",
        name: "capo_dataexchange.types.name.Name",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        tags: Optional["capo_dataexchange.types.map_of__string.MapOf__string"] = None,
    ) -> "capo_dataexchange.types.create_data_set_response.CreateDataSetResponse":
        """<p>This operation creates a data set.</p>

        Args:
            asset_type: <p>The type of asset that is added to a data set.</p>
            description: <p>A description for the data set. This value can be up to 16,348 characters long.</p>
            name: <p>The name of the data set.</p>
            tags: <p>A data set tag is an optional label that you can assign to a data set when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request has exceeded the quotas imposed by the service.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.create_data_set_request.CreateDataSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.create_data_set_response.CreateDataSetResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.create_data_set

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.create_data_set.async_create_data_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.create_data_set_request.CreateDataSetRequest = {
            "asset_type": asset_type,
            "description": description,
            "name": name,
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

    async def create_event_action(
        self,
        action: "capo_dataexchange.types.action.Action",
        event: "capo_dataexchange.types.event.Event",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        tags: Optional["capo_dataexchange.types.map_of__string.MapOf__string"] = None,
    ) -> (
        "capo_dataexchange.types.create_event_action_response.CreateEventActionResponse"
    ):
        """<p>This operation creates an event action.</p>

        Args:
            action: <p>What occurs after a certain event.</p>
            event: <p>What occurs to start an action.</p>
            tags: <p>Key-value pairs that you can associate with the event action.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request has exceeded the quotas imposed by the service.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.create_event_action_request.CreateEventActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.create_event_action_response.CreateEventActionResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.create_event_action

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.create_event_action.async_create_event_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.create_event_action_request.CreateEventActionRequest = {
            "action": action,
            "event": event,
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

    async def create_job(
        self,
        details: "capo_dataexchange.types.request_details.RequestDetails",
        type: "capo_dataexchange.types.type.Type",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        asset_configuration: Optional[
            "capo_dataexchange.types.asset_configuration.AssetConfiguration"
        ] = None,
    ) -> "capo_dataexchange.types.create_job_response.CreateJobResponse":
        """<p>This operation creates a job.</p>

        Args:
            asset_configuration: <p>The configuration for the asset, including tags to be applied to assets created by the job.</p>
            details: <p>The details for the CreateJob request.</p>
            type: <p>The type of job to be created.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.create_job_request.CreateJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.create_job_response.CreateJobResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.create_job

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.create_job.async_create_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.create_job_request.CreateJobRequest = {
            "details": details,
            "type": type,
        }
        if asset_configuration is not None:
            input_["asset_configuration"] = asset_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_revision(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        comment: Optional[
            "capo_dataexchange.types.__string_min0_max16384.__stringMin0Max16384"
        ] = None,
        tags: Optional["capo_dataexchange.types.map_of__string.MapOf__string"] = None,
    ) -> "capo_dataexchange.types.create_revision_response.CreateRevisionResponse":
        """<p>This operation creates a revision for a data set.</p>

        Args:
            comment: <p>An optional comment about the revision.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            tags: <p>A revision tag is an optional label that you can assign to a revision when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.create_revision_request.CreateRevisionRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.create_revision_response.CreateRevisionResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.create_revision

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.create_revision.async_create_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.create_revision_request.CreateRevisionRequest = {
            "data_set_id": data_set_id
        }
        if comment is not None:
            input_["comment"] = comment
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset(
        self,
        asset_id: "capo_dataexchange.types.id.Id",
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes an asset.</p>

        Args:
            asset_id: <p>The unique identifier for an asset.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.delete_asset_request.DeleteAssetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.delete_asset

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.delete_asset_request.DeleteAssetRequest = {
            "asset_id": asset_id,
            "data_set_id": data_set_id,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_grant(
        self,
        data_grant_id: "capo_dataexchange.types.data_grant_id.DataGrantId",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes a data grant.</p>

        Args:
            data_grant_id: <p>The ID of the data grant to delete.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.delete_data_grant_request.DeleteDataGrantRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.delete_data_grant

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.delete_data_grant.async_delete_data_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.delete_data_grant_request.DeleteDataGrantRequest = {
            "data_grant_id": data_grant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_set(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes a data set.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.delete_data_set_request.DeleteDataSetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.delete_data_set

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.delete_data_set.async_delete_data_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.delete_data_set_request.DeleteDataSetRequest = {
            "data_set_id": data_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_event_action(
        self,
        event_action_id: "capo_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes the event action.</p>

        Args:
            event_action_id: <p>The unique identifier for the event action.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.delete_event_action_request.DeleteEventActionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.delete_event_action

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.delete_event_action.async_delete_event_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.delete_event_action_request.DeleteEventActionRequest = {
            "event_action_id": event_action_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_revision(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes a revision.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.delete_revision_request.DeleteRevisionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.delete_revision

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.delete_revision.async_delete_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.delete_revision_request.DeleteRevisionRequest = {
            "data_set_id": data_set_id,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset(
        self,
        asset_id: "capo_dataexchange.types.id.Id",
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.get_asset_response.GetAssetResponse":
        """<p>This operation returns information about an asset.</p>

        Args:
            asset_id: <p>The unique identifier for an asset.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.get_asset_request.GetAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.get_asset_response.GetAssetResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.get_asset

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.get_asset.async_get_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.get_asset_request.GetAssetRequest = {
            "asset_id": asset_id,
            "data_set_id": data_set_id,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_grant(
        self,
        data_grant_id: "capo_dataexchange.types.data_grant_id.DataGrantId",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.get_data_grant_response.GetDataGrantResponse":
        """<p>This operation returns information about a data grant.</p>

        Args:
            data_grant_id: <p>The ID of the data grant.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.get_data_grant_request.GetDataGrantRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.get_data_grant_response.GetDataGrantResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.get_data_grant

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.get_data_grant.async_get_data_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.get_data_grant_request.GetDataGrantRequest = {
            "data_grant_id": data_grant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_set(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.get_data_set_response.GetDataSetResponse":
        """<p>This operation returns information about a data set.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.get_data_set_request.GetDataSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.get_data_set_response.GetDataSetResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.get_data_set

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.get_data_set.async_get_data_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.get_data_set_request.GetDataSetRequest = {
            "data_set_id": data_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_event_action(
        self,
        event_action_id: "capo_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.get_event_action_response.GetEventActionResponse":
        """<p>This operation retrieves information about an event action.</p>

        Args:
            event_action_id: <p>The unique identifier for the event action.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.get_event_action_request.GetEventActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.get_event_action_response.GetEventActionResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.get_event_action

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.get_event_action.async_get_event_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.get_event_action_request.GetEventActionRequest = {
            "event_action_id": event_action_id
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
        job_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.get_job_response.GetJobResponse":
        """<p>This operation returns information about a job.</p>

        Args:
            job_id: <p>The unique identifier for a job.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.get_job_request.GetJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.get_job_response.GetJobResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.get_job

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.get_job.async_get_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.get_job_request.GetJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_received_data_grant(
        self,
        data_grant_arn: "capo_dataexchange.types.data_grant_arn.DataGrantArn",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.get_received_data_grant_response.GetReceivedDataGrantResponse":
        """<p>This operation returns information about a received data grant.</p>

        Args:
            data_grant_arn: <p>The Amazon Resource Name (ARN) of the data grant.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.get_received_data_grant_request.GetReceivedDataGrantRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.get_received_data_grant_response.GetReceivedDataGrantResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.get_received_data_grant

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.get_received_data_grant.async_get_received_data_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.get_received_data_grant_request.GetReceivedDataGrantRequest = {
            "data_grant_arn": data_grant_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_revision(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.get_revision_response.GetRevisionResponse":
        """<p>This operation returns information about a revision.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.get_revision_request.GetRevisionRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.get_revision_response.GetRevisionResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.get_revision

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.get_revision.async_get_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.get_revision_request.GetRevisionRequest = {
            "data_set_id": data_set_id,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_grants(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "capo_dataexchange.types.list_data_grants_response.ListDataGrantsResponse":
        """<p>This operation returns information about all data grants.</p>

        Args:
            max_results: <p>The maximum number of results to be included in the next page.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_data_grants_request.ListDataGrantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_data_grants_response.ListDataGrantsResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_data_grants

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_data_grants.async_list_data_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_data_grants_request.ListDataGrantsRequest = {}
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

    async def iter_list_data_grants(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_dataexchange.types.data_grant_summary_entry.DataGrantSummaryEntry]":
        _token = next_token
        while True:
            _response = await self.list_data_grants(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("data_grant_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_set_revisions(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "capo_dataexchange.types.list_data_set_revisions_response.ListDataSetRevisionsResponse":
        """<p>This operation lists a data set's revisions sorted by CreatedAt in descending order.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_data_set_revisions_request.ListDataSetRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_data_set_revisions_response.ListDataSetRevisionsResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_data_set_revisions

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_data_set_revisions.async_list_data_set_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_data_set_revisions_request.ListDataSetRevisionsRequest = {
            "data_set_id": data_set_id
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

    async def iter_list_data_set_revisions(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_dataexchange.types.revision_entry.RevisionEntry]":
        _token = next_token
        while True:
            _response = await self.list_data_set_revisions(
                data_set_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("revisions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_sets(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
        origin: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "capo_dataexchange.types.list_data_sets_response.ListDataSetsResponse":
        """<p>This operation lists your data sets. When listing by origin OWNED, results are sorted by CreatedAt in descending order. When listing by origin ENTITLED, there is no order.</p>

        Args:
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            origin: <p>A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_data_sets_request.ListDataSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_data_sets_response.ListDataSetsResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_data_sets

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_data_sets.async_list_data_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_data_sets_request.ListDataSetsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if origin is not None:
            input_["origin"] = origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_data_sets(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
        origin: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_dataexchange.types.data_set_entry.DataSetEntry]":
        _token = next_token
        while True:
            _response = await self.list_data_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                origin=origin,
            )
            _page = _resolve_path(_response, ("data_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_event_actions(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        event_source_id: Optional["capo_dataexchange.types.__string.__string"] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "capo_dataexchange.types.list_event_actions_response.ListEventActionsResponse":
        """<p>This operation lists your event actions.</p>

        Args:
            event_source_id: <p>The unique identifier for the event source.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_event_actions_request.ListEventActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_event_actions_response.ListEventActionsResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_event_actions

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_event_actions.async_list_event_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_event_actions_request.ListEventActionsRequest = {}
        if event_source_id is not None:
            input_["event_source_id"] = event_source_id
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

    async def iter_list_event_actions(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        event_source_id: Optional["capo_dataexchange.types.__string.__string"] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_dataexchange.types.event_action_entry.EventActionEntry]":
        _token = next_token
        while True:
            _response = await self.list_event_actions(
                config_overrides=config_overrides,
                event_source_id=event_source_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("event_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_jobs(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        data_set_id: Optional["capo_dataexchange.types.__string.__string"] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
        revision_id: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "capo_dataexchange.types.list_jobs_response.ListJobsResponse":
        """<p>This operation lists your jobs sorted by CreatedAt in descending order.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_jobs_request.ListJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_jobs_response.ListJobsResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_jobs

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_jobs_request.ListJobsRequest = {}
        if data_set_id is not None:
            input_["data_set_id"] = data_set_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if revision_id is not None:
            input_["revision_id"] = revision_id

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
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        data_set_id: Optional["capo_dataexchange.types.__string.__string"] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
        revision_id: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_dataexchange.types.job_entry.JobEntry]":
        _token = next_token
        while True:
            _response = await self.list_jobs(
                config_overrides=config_overrides,
                data_set_id=data_set_id,
                max_results=max_results,
                next_token=_token,
                revision_id=revision_id,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_received_data_grants(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
        acceptance_state: Optional[
            "capo_dataexchange.types.acceptance_state_filter_values.AcceptanceStateFilterValues"
        ] = None,
    ) -> "capo_dataexchange.types.list_received_data_grants_response.ListReceivedDataGrantsResponse":
        """<p>This operation returns information about all received data grants.</p>

        Args:
            max_results: <p>The maximum number of results to be included in the next page.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            acceptance_state: <p>The acceptance state of the data grants to list.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_received_data_grants_request.ListReceivedDataGrantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_received_data_grants_response.ListReceivedDataGrantsResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_received_data_grants

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_received_data_grants.async_list_received_data_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_received_data_grants_request.ListReceivedDataGrantsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if acceptance_state is not None:
            input_["acceptance_state"] = acceptance_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_received_data_grants(
        self,
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
        acceptance_state: Optional[
            "capo_dataexchange.types.acceptance_state_filter_values.AcceptanceStateFilterValues"
        ] = None,
    ) -> "AsyncIterator[capo_dataexchange.types.received_data_grant_summaries_entry.ReceivedDataGrantSummariesEntry]":
        _token = next_token
        while True:
            _response = await self.list_received_data_grants(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                acceptance_state=acceptance_state,
            )
            _page = _resolve_path(_response, ("data_grant_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_revision_assets(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "capo_dataexchange.types.list_revision_assets_response.ListRevisionAssetsResponse":
        """<p>This operation lists a revision's assets sorted alphabetically in descending order.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_revision_assets_request.ListRevisionAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_revision_assets_response.ListRevisionAssetsResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_revision_assets

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_revision_assets.async_list_revision_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_revision_assets_request.ListRevisionAssetsRequest = {
            "data_set_id": data_set_id,
            "revision_id": revision_id,
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

    async def iter_list_revision_assets(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        max_results: Optional["capo_dataexchange.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_dataexchange.types.asset_entry.AssetEntry]":
        _token = next_token
        while True:
            _response = await self.list_revision_assets(
                data_set_id,
                revision_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>This operation lists the tags on the resource.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>

        Raises:
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_revision(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        revocation_comment: "capo_dataexchange.types.__string_min10_max512.__stringMin10Max512",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.revoke_revision_response.RevokeRevisionResponse":
        """<p>This operation revokes subscribers' access to a revision.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>
            revocation_comment: <p>A required comment to inform subscribers of the reason their access to the revision was revoked.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.revoke_revision_request.RevokeRevisionRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.revoke_revision_response.RevokeRevisionResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.revoke_revision

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.revoke_revision.async_revoke_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.revoke_revision_request.RevokeRevisionRequest = {
            "data_set_id": data_set_id,
            "revision_id": revision_id,
            "revocation_comment": revocation_comment,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_api_asset(
        self,
        asset_id: "capo_dataexchange.types.__string.__string",
        data_set_id: "capo_dataexchange.types.__string.__string",
        revision_id: "capo_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        body: Optional["capo_dataexchange.types.__string.__string"] = None,
        query_string_parameters: Optional[
            "capo_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
        request_headers: Optional[
            "capo_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
        method: Optional["capo_dataexchange.types.__string.__string"] = None,
        path: Optional["capo_dataexchange.types.__string.__string"] = None,
    ) -> "capo_dataexchange.types.send_api_asset_response.SendApiAssetResponse":
        """<p>This operation invokes an API Gateway API asset. The request is proxied to the provider’s API Gateway API.</p>

        Args:
            body: <p>The request body.</p>
            query_string_parameters: <p>Attach query string parameters to the end of the URI (for example, /v1/examplePath?exampleParam=exampleValue).</p>
            asset_id: <p>Asset ID value for the API request.</p>
            data_set_id: <p>Data set ID value for the API request.</p>
            request_headers: <p>Any header value prefixed with x-amzn-dataexchange-header- will have that stripped before sending the Asset API request. Use this when you want to override a header that AWS Data Exchange uses. Alternatively, you can use the header without a prefix to the HTTP request.</p>
            method: <p>HTTP method value for the API request. Alternatively, you can use the appropriate verb in your request.</p>
            path: <p>URI path value for the API request. Alternatively, you can set the URI path directly by invoking /v1/{pathValue}.</p>
            revision_id: <p>Revision ID value for the API request.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.send_api_asset_request.SendApiAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.send_api_asset_response.SendApiAssetResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.send_api_asset

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.send_api_asset.async_send_api_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.send_api_asset_request.SendApiAssetRequest = {
            "asset_id": asset_id,
            "data_set_id": data_set_id,
            "revision_id": revision_id,
        }
        if body is not None:
            input_["body"] = body
        if query_string_parameters is not None:
            input_["query_string_parameters"] = query_string_parameters
        if request_headers is not None:
            input_["request_headers"] = request_headers
        if method is not None:
            input_["method"] = method
        if path is not None:
            input_["path"] = path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_data_set_notification(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        type: "capo_dataexchange.types.notification_type.NotificationType",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        scope: Optional["capo_dataexchange.types.scope_details.ScopeDetails"] = None,
        client_token: Optional[
            "capo_dataexchange.types.client_token.ClientToken"
        ] = None,
        comment: Optional[
            "capo_dataexchange.types.__string_min0_max4096.__stringMin0Max4096"
        ] = None,
        details: Optional[
            "capo_dataexchange.types.notification_details.NotificationDetails"
        ] = None,
    ) -> "capo_dataexchange.types.send_data_set_notification_response.SendDataSetNotificationResponse":
        """<p>The type of event associated with the data set.</p>

        Args:
            scope: <p>Affected scope of this notification such as the underlying resources affected by the notification event.</p>
            client_token: <p>Idempotency key for the notification, this key allows us to deduplicate notifications that are sent in quick succession erroneously.</p>
            comment: <p>Free-form text field for providers to add information about their notifications.</p>
            data_set_id: <p>Affected data set of the notification.</p>
            details: <p>Extra details specific to this notification type.</p>
            type: <p>The type of the notification. Describing the kind of event the notification is alerting you to.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.send_data_set_notification_request.SendDataSetNotificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.send_data_set_notification_response.SendDataSetNotificationResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.send_data_set_notification

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.send_data_set_notification.async_send_data_set_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.send_data_set_notification_request.SendDataSetNotificationRequest = {
            "data_set_id": data_set_id,
            "type": type,
        }
        if scope is not None:
            input_["scope"] = scope
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if comment is not None:
            input_["comment"] = comment
        if details is not None:
            input_["details"] = details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_job(
        self,
        job_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.start_job_response.StartJobResponse":
        """<p>This operation starts a job.</p>

        Args:
            job_id: <p>The unique identifier for a job.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.start_job_request.StartJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.start_job_response.StartJobResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.start_job

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.start_job.async_start_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.start_job_request.StartJobRequest = {
            "job_id": job_id
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
        resource_arn: "capo_dataexchange.types.__string.__string",
        tags: "capo_dataexchange.types.map_of__string.MapOf__string",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation tags a resource.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>
            tags: <p>A label that consists of a customer-defined key and an optional value.</p>

        Raises:
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.tag_resource

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_dataexchange.types.__string.__string",
        tag_keys: "capo_dataexchange.types.list_of__string.ListOf__string",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation removes one or more tags from a resource.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>
            tag_keys: <p>The key tags.</p>

        Raises:
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_dataexchange._operations.data_exchange.untag_resource

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_asset(
        self,
        asset_id: "capo_dataexchange.types.id.Id",
        data_set_id: "capo_dataexchange.types.id.Id",
        name: "capo_dataexchange.types.asset_name.AssetName",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
    ) -> "capo_dataexchange.types.update_asset_response.UpdateAssetResponse":
        """<p>This operation updates an asset.</p>

        Args:
            asset_id: <p>The unique identifier for an asset.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            name: <p>The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of "Database(s) included in the LF-tag policy" or "Table(s) included in LF-tag policy" are used as the name.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.update_asset_request.UpdateAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.update_asset_response.UpdateAssetResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.update_asset

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.update_asset.async_update_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.update_asset_request.UpdateAssetRequest = {
            "asset_id": asset_id,
            "data_set_id": data_set_id,
            "name": name,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_set(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        description: Optional["capo_dataexchange.types.description.Description"] = None,
        name: Optional["capo_dataexchange.types.name.Name"] = None,
    ) -> "capo_dataexchange.types.update_data_set_response.UpdateDataSetResponse":
        """<p>This operation updates a data set.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            description: <p>The description for the data set.</p>
            name: <p>The name of the data set.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.update_data_set_request.UpdateDataSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.update_data_set_response.UpdateDataSetResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.update_data_set

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.update_data_set.async_update_data_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.update_data_set_request.UpdateDataSetRequest = {
            "data_set_id": data_set_id
        }
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_event_action(
        self,
        event_action_id: "capo_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        action: Optional["capo_dataexchange.types.action.Action"] = None,
    ) -> (
        "capo_dataexchange.types.update_event_action_response.UpdateEventActionResponse"
    ):
        """<p>This operation updates the event action.</p>

        Args:
            action: <p>What occurs after a certain event.</p>
            event_action_id: <p>The unique identifier for the event action.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.update_event_action_request.UpdateEventActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.update_event_action_response.UpdateEventActionResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.update_event_action

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.update_event_action.async_update_event_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.update_event_action_request.UpdateEventActionRequest = {
            "event_action_id": event_action_id
        }
        if action is not None:
            input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_revision(
        self,
        data_set_id: "capo_dataexchange.types.id.Id",
        revision_id: "capo_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[AsyncDataExchangeClientConfig] = None,
        comment: Optional[
            "capo_dataexchange.types.__string_min0_max16384.__stringMin0Max16384"
        ] = None,
        finalized: Optional["capo_dataexchange.types.__boolean.__boolean"] = None,
    ) -> "capo_dataexchange.types.update_revision_response.UpdateRevisionResponse":
        """<p>This operation updates a revision.</p>

        Args:
            comment: <p>An optional comment about the revision.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            finalized: <p>Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it's in this read-only state, you can publish the revision to your products.</p>
            revision_id: <p>The unique identifier for a revision.</p>

        Raises:
            capo_dataexchange.errors.access_denied_exception.AccessDeniedException: <p>Access to the resource is denied.</p>
            capo_dataexchange.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_dataexchange.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_dataexchange.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_dataexchange.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_dataexchange.errors.validation_exception.ValidationException: <p>The request was invalid.</p>
            capo_dataexchange.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dataexchange.types.update_revision_request.UpdateRevisionRequest]",
        ) -> AsyncOperationResponse[
            "capo_dataexchange.types.update_revision_response.UpdateRevisionResponse"
        ]:
            import capo_dataexchange._operations.data_exchange.update_revision

            (
                output,
                http_response,
            ) = await capo_dataexchange._operations.data_exchange.update_revision.async_update_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dataexchange.types.update_revision_request.UpdateRevisionRequest = {
            "data_set_id": data_set_id,
            "revision_id": revision_id,
        }
        if comment is not None:
            input_["comment"] = comment
        if finalized is not None:
            input_["finalized"] = finalized

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

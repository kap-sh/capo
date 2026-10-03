"""Generated from Smithy shape ``com.amazonaws.mailmanager#MailManagerSvc``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_mailmanager._auth._signers
import capo_mailmanager._auth._sigv4
from capo_mailmanager._auth._identity import Credentials
from capo_mailmanager._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mailmanager._auth._zapros_handler import AuthMiddleware
from capo_mailmanager._pagination import resolve_path as _resolve_path
from capo_mailmanager._resources.mail_manager_svc.addon_instance_resource import (
    AsyncAddonInstanceResource,
)
from capo_mailmanager._resources.mail_manager_svc.addon_subscription_resource import (
    AsyncAddonSubscriptionResource,
)
from capo_mailmanager._resources.mail_manager_svc.address_list_resource import (
    AsyncAddressListResource,
)
from capo_mailmanager._resources.mail_manager_svc.archive_resource import (
    AsyncArchiveResource,
)
from capo_mailmanager._resources.mail_manager_svc.ingress_point_resource import (
    AsyncIngressPointResource,
)
from capo_mailmanager._resources.mail_manager_svc.relay_resource import (
    AsyncRelayResource,
)
from capo_mailmanager._resources.mail_manager_svc.rule_set_resource import (
    AsyncRuleSetResource,
)
from capo_mailmanager._resources.mail_manager_svc.traffic_policy_resource import (
    AsyncTrafficPolicyResource,
)
from capo_mailmanager._services._aws_config import aaws_config
from capo_mailmanager._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_mailmanager.types.accept_action
    import capo_mailmanager.types.addon_instance
    import capo_mailmanager.types.addon_instance_id
    import capo_mailmanager.types.addon_name
    import capo_mailmanager.types.addon_subscription
    import capo_mailmanager.types.addon_subscription_id
    import capo_mailmanager.types.address
    import capo_mailmanager.types.address_filter
    import capo_mailmanager.types.address_list
    import capo_mailmanager.types.address_list_id
    import capo_mailmanager.types.address_list_name
    import capo_mailmanager.types.address_page_size
    import capo_mailmanager.types.archive
    import capo_mailmanager.types.archive_filters
    import capo_mailmanager.types.archive_id
    import capo_mailmanager.types.archive_id_string
    import capo_mailmanager.types.archive_name_string
    import capo_mailmanager.types.archive_retention
    import capo_mailmanager.types.archived_message_id
    import capo_mailmanager.types.create_addon_instance_request
    import capo_mailmanager.types.create_addon_instance_response
    import capo_mailmanager.types.create_addon_subscription_request
    import capo_mailmanager.types.create_addon_subscription_response
    import capo_mailmanager.types.create_address_list_import_job_request
    import capo_mailmanager.types.create_address_list_import_job_response
    import capo_mailmanager.types.create_address_list_request
    import capo_mailmanager.types.create_address_list_response
    import capo_mailmanager.types.create_archive_request
    import capo_mailmanager.types.create_archive_response
    import capo_mailmanager.types.create_ingress_point_request
    import capo_mailmanager.types.create_ingress_point_response
    import capo_mailmanager.types.create_relay_request
    import capo_mailmanager.types.create_relay_response
    import capo_mailmanager.types.create_rule_set_request
    import capo_mailmanager.types.create_rule_set_response
    import capo_mailmanager.types.create_traffic_policy_request
    import capo_mailmanager.types.create_traffic_policy_response
    import capo_mailmanager.types.delete_addon_instance_request
    import capo_mailmanager.types.delete_addon_instance_response
    import capo_mailmanager.types.delete_addon_subscription_request
    import capo_mailmanager.types.delete_addon_subscription_response
    import capo_mailmanager.types.delete_address_list_request
    import capo_mailmanager.types.delete_address_list_response
    import capo_mailmanager.types.delete_archive_request
    import capo_mailmanager.types.delete_archive_response
    import capo_mailmanager.types.delete_ingress_point_request
    import capo_mailmanager.types.delete_ingress_point_response
    import capo_mailmanager.types.delete_relay_request
    import capo_mailmanager.types.delete_relay_response
    import capo_mailmanager.types.delete_rule_set_request
    import capo_mailmanager.types.delete_rule_set_response
    import capo_mailmanager.types.delete_traffic_policy_request
    import capo_mailmanager.types.delete_traffic_policy_response
    import capo_mailmanager.types.deregister_member_from_address_list_request
    import capo_mailmanager.types.deregister_member_from_address_list_response
    import capo_mailmanager.types.export_destination_configuration
    import capo_mailmanager.types.export_id
    import capo_mailmanager.types.export_max_results
    import capo_mailmanager.types.export_summary
    import capo_mailmanager.types.get_addon_instance_request
    import capo_mailmanager.types.get_addon_instance_response
    import capo_mailmanager.types.get_addon_subscription_request
    import capo_mailmanager.types.get_addon_subscription_response
    import capo_mailmanager.types.get_address_list_import_job_request
    import capo_mailmanager.types.get_address_list_import_job_response
    import capo_mailmanager.types.get_address_list_request
    import capo_mailmanager.types.get_address_list_response
    import capo_mailmanager.types.get_archive_export_request
    import capo_mailmanager.types.get_archive_export_response
    import capo_mailmanager.types.get_archive_message_content_request
    import capo_mailmanager.types.get_archive_message_content_response
    import capo_mailmanager.types.get_archive_message_request
    import capo_mailmanager.types.get_archive_message_response
    import capo_mailmanager.types.get_archive_request
    import capo_mailmanager.types.get_archive_response
    import capo_mailmanager.types.get_archive_search_request
    import capo_mailmanager.types.get_archive_search_response
    import capo_mailmanager.types.get_archive_search_results_request
    import capo_mailmanager.types.get_archive_search_results_response
    import capo_mailmanager.types.get_ingress_point_request
    import capo_mailmanager.types.get_ingress_point_response
    import capo_mailmanager.types.get_member_of_address_list_request
    import capo_mailmanager.types.get_member_of_address_list_response
    import capo_mailmanager.types.get_relay_request
    import capo_mailmanager.types.get_relay_response
    import capo_mailmanager.types.get_rule_set_request
    import capo_mailmanager.types.get_rule_set_response
    import capo_mailmanager.types.get_traffic_policy_request
    import capo_mailmanager.types.get_traffic_policy_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.import_data_format
    import capo_mailmanager.types.import_job
    import capo_mailmanager.types.ingress_point
    import capo_mailmanager.types.ingress_point_configuration
    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.ingress_point_name
    import capo_mailmanager.types.ingress_point_status_to_update
    import capo_mailmanager.types.ingress_point_type
    import capo_mailmanager.types.job_id
    import capo_mailmanager.types.job_name
    import capo_mailmanager.types.kms_key_arn
    import capo_mailmanager.types.list_addon_instances_request
    import capo_mailmanager.types.list_addon_instances_response
    import capo_mailmanager.types.list_addon_subscriptions_request
    import capo_mailmanager.types.list_addon_subscriptions_response
    import capo_mailmanager.types.list_address_list_import_jobs_request
    import capo_mailmanager.types.list_address_list_import_jobs_response
    import capo_mailmanager.types.list_address_lists_request
    import capo_mailmanager.types.list_address_lists_response
    import capo_mailmanager.types.list_archive_exports_request
    import capo_mailmanager.types.list_archive_exports_response
    import capo_mailmanager.types.list_archive_searches_request
    import capo_mailmanager.types.list_archive_searches_response
    import capo_mailmanager.types.list_archives_request
    import capo_mailmanager.types.list_archives_response
    import capo_mailmanager.types.list_ingress_points_request
    import capo_mailmanager.types.list_ingress_points_response
    import capo_mailmanager.types.list_members_of_address_list_request
    import capo_mailmanager.types.list_members_of_address_list_response
    import capo_mailmanager.types.list_relays_request
    import capo_mailmanager.types.list_relays_response
    import capo_mailmanager.types.list_rule_sets_request
    import capo_mailmanager.types.list_rule_sets_response
    import capo_mailmanager.types.list_tags_for_resource_request
    import capo_mailmanager.types.list_tags_for_resource_response
    import capo_mailmanager.types.list_traffic_policies_request
    import capo_mailmanager.types.list_traffic_policies_response
    import capo_mailmanager.types.max_message_size_bytes
    import capo_mailmanager.types.network_configuration
    import capo_mailmanager.types.page_size
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.policy_statement_list
    import capo_mailmanager.types.register_member_to_address_list_request
    import capo_mailmanager.types.register_member_to_address_list_response
    import capo_mailmanager.types.relay
    import capo_mailmanager.types.relay_authentication
    import capo_mailmanager.types.relay_id
    import capo_mailmanager.types.relay_name
    import capo_mailmanager.types.relay_server_name
    import capo_mailmanager.types.relay_server_port
    import capo_mailmanager.types.rule_set
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.rule_set_name
    import capo_mailmanager.types.rules
    import capo_mailmanager.types.saved_address
    import capo_mailmanager.types.search_id
    import capo_mailmanager.types.search_max_results
    import capo_mailmanager.types.search_summary
    import capo_mailmanager.types.start_address_list_import_job_request
    import capo_mailmanager.types.start_address_list_import_job_response
    import capo_mailmanager.types.start_archive_export_request
    import capo_mailmanager.types.start_archive_export_response
    import capo_mailmanager.types.start_archive_search_request
    import capo_mailmanager.types.start_archive_search_response
    import capo_mailmanager.types.stop_address_list_import_job_request
    import capo_mailmanager.types.stop_address_list_import_job_response
    import capo_mailmanager.types.stop_archive_export_request
    import capo_mailmanager.types.stop_archive_export_response
    import capo_mailmanager.types.stop_archive_search_request
    import capo_mailmanager.types.stop_archive_search_response
    import capo_mailmanager.types.tag_key_list
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.tag_resource_request
    import capo_mailmanager.types.tag_resource_response
    import capo_mailmanager.types.taggable_resource_arn
    import capo_mailmanager.types.tls_policy
    import capo_mailmanager.types.traffic_policy
    import capo_mailmanager.types.traffic_policy_id
    import capo_mailmanager.types.traffic_policy_name
    import capo_mailmanager.types.trust_store_response_option
    import capo_mailmanager.types.untag_resource_request
    import capo_mailmanager.types.untag_resource_response
    import capo_mailmanager.types.update_archive_request
    import capo_mailmanager.types.update_archive_response
    import capo_mailmanager.types.update_ingress_point_request
    import capo_mailmanager.types.update_ingress_point_response
    import capo_mailmanager.types.update_relay_request
    import capo_mailmanager.types.update_relay_response
    import capo_mailmanager.types.update_rule_set_request
    import capo_mailmanager.types.update_rule_set_response
    import capo_mailmanager.types.update_traffic_policy_request
    import capo_mailmanager.types.update_traffic_policy_response


class AsyncMailManagerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMailManagerClient:
    """A client for the ``MailManager`` service.

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
        self._config = AsyncMailManagerClientConfig(
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
        self.addon_instance_resource = AsyncAddonInstanceResource(self)
        self.addon_subscription_resource = AsyncAddonSubscriptionResource(self)
        self.address_list_resource = AsyncAddressListResource(self)
        self.archive_resource = AsyncArchiveResource(self)
        self.ingress_point_resource = AsyncIngressPointResource(self)
        self.relay_resource = AsyncRelayResource(self)
        self.rule_set_resource = AsyncRuleSetResource(self)
        self.traffic_policy_resource = AsyncTrafficPolicyResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncMailManagerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMailManagerClientConfig = config_overrides or {}
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

    async def create_address_list_import_job(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        name: "capo_mailmanager.types.job_name.JobName",
        import_data_format: "capo_mailmanager.types.import_data_format.ImportDataFormat",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_mailmanager.types.create_address_list_import_job_response.CreateAddressListImportJobResponse":
        """<p>Creates an import job for an address list.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            address_list_id: <p>The unique identifier of the address list for importing addresses to.</p>
            name: <p>A user-friendly name for the import job.</p>
            import_data_format: <p>The format of the input for an import job.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_address_list_import_job_request.CreateAddressListImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_address_list_import_job_response.CreateAddressListImportJobResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_address_list_import_job

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_address_list_import_job.async_create_address_list_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_address_list_import_job_request.CreateAddressListImportJobRequest = {
            "address_list_id": address_list_id,
            "name": name,
            "import_data_format": import_data_format,
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

    async def deregister_member_from_address_list(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        address: "capo_mailmanager.types.address.Address",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.deregister_member_from_address_list_response.DeregisterMemberFromAddressListResponse":
        """<p>Removes a member from an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list to remove the address from.</p>
            address: <p>The address to be removed from the address list.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.deregister_member_from_address_list_request.DeregisterMemberFromAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.deregister_member_from_address_list_response.DeregisterMemberFromAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.deregister_member_from_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.deregister_member_from_address_list.async_deregister_member_from_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.deregister_member_from_address_list_request.DeregisterMemberFromAddressListRequest = {
            "address_list_id": address_list_id,
            "address": address,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_address_list_import_job(
        self,
        job_id: "capo_mailmanager.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_address_list_import_job_response.GetAddressListImportJobResponse":
        """<p>Fetch attributes of an import job.</p>

        Args:
            job_id: <p>The identifier of the import job that needs to be retrieved.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_address_list_import_job_request.GetAddressListImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_address_list_import_job_response.GetAddressListImportJobResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_address_list_import_job

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_address_list_import_job.async_get_address_list_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_address_list_import_job_request.GetAddressListImportJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_archive_export(
        self,
        export_id: "capo_mailmanager.types.export_id.ExportId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_archive_export_response.GetArchiveExportResponse":
        """<p>Retrieves the details and current status of a specific email archive export job.</p>

        Args:
            export_id: <p>The identifier of the export job to get details for.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_archive_export_request.GetArchiveExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_archive_export_response.GetArchiveExportResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive_export

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_archive_export.async_get_archive_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_export_request.GetArchiveExportRequest = {
            "export_id": export_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_archive_message(
        self,
        archived_message_id: "capo_mailmanager.types.archived_message_id.ArchivedMessageId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> (
        "capo_mailmanager.types.get_archive_message_response.GetArchiveMessageResponse"
    ):
        """<p>Returns a pre-signed URL that provides temporary download access to the specific email message stored in the archive. </p>

        Args:
            archived_message_id: <p>The unique identifier of the archived email message.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_archive_message_request.GetArchiveMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_archive_message_response.GetArchiveMessageResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive_message

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_archive_message.async_get_archive_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_message_request.GetArchiveMessageRequest = {
            "archived_message_id": archived_message_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_archive_message_content(
        self,
        archived_message_id: "capo_mailmanager.types.archived_message_id.ArchivedMessageId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_archive_message_content_response.GetArchiveMessageContentResponse":
        """<p>Returns the textual content of a specific email message stored in the archive. Attachments are not included. </p>

        Args:
            archived_message_id: <p>The unique identifier of the archived email message.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_archive_message_content_request.GetArchiveMessageContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_archive_message_content_response.GetArchiveMessageContentResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive_message_content

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_archive_message_content.async_get_archive_message_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_message_content_request.GetArchiveMessageContentRequest = {
            "archived_message_id": archived_message_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_archive_search(
        self,
        search_id: "capo_mailmanager.types.search_id.SearchId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_archive_search_response.GetArchiveSearchResponse":
        """<p>Retrieves the details and current status of a specific email archive search job.</p>

        Args:
            search_id: <p>The identifier of the search job to get details for.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_archive_search_request.GetArchiveSearchRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_archive_search_response.GetArchiveSearchResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive_search

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_archive_search.async_get_archive_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_search_request.GetArchiveSearchRequest = {
            "search_id": search_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_archive_search_results(
        self,
        search_id: "capo_mailmanager.types.search_id.SearchId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_archive_search_results_response.GetArchiveSearchResultsResponse":
        """<p>Returns the results of a completed email archive search job.</p>

        Args:
            search_id: <p>The identifier of the completed search job.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_archive_search_results_request.GetArchiveSearchResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_archive_search_results_response.GetArchiveSearchResultsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive_search_results

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_archive_search_results.async_get_archive_search_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_search_results_request.GetArchiveSearchResultsRequest = {
            "search_id": search_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_member_of_address_list(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        address: "capo_mailmanager.types.address.Address",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_member_of_address_list_response.GetMemberOfAddressListResponse":
        """<p>Fetch attributes of a member in an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list to retrieve the address from.</p>
            address: <p>The address to be retrieved from the address list.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_member_of_address_list_request.GetMemberOfAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_member_of_address_list_response.GetMemberOfAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_member_of_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_member_of_address_list.async_get_member_of_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_member_of_address_list_request.GetMemberOfAddressListRequest = {
            "address_list_id": address_list_id,
            "address": address,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_address_list_import_jobs(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_address_list_import_jobs_response.ListAddressListImportJobsResponse":
        """<p>Lists jobs for an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list for listing import jobs.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of import jobs that are returned per call. You can use NextToken to retrieve the next page of jobs.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_address_list_import_jobs_request.ListAddressListImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_address_list_import_jobs_response.ListAddressListImportJobsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_address_list_import_jobs

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_address_list_import_jobs.async_list_address_list_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_address_list_import_jobs_request.ListAddressListImportJobsRequest = {
            "address_list_id": address_list_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_address_list_import_jobs(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.import_job.ImportJob]":
        _token = next_token
        while True:
            _response = await self.list_address_list_import_jobs(
                address_list_id,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_archive_exports(
        self,
        archive_id: "capo_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_archive_exports_response.ListArchiveExportsResponse":
        """<p>Returns a list of email archive export jobs.</p>

        Args:
            archive_id: <p>The identifier of the archive.</p>
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archive export jobs that are returned per call. You can use NextToken to obtain further pages of archives. </p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_archive_exports_request.ListArchiveExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_archive_exports_response.ListArchiveExportsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_archive_exports

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_archive_exports.async_list_archive_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_archive_exports_request.ListArchiveExportsRequest = {
            "archive_id": archive_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_archive_exports(
        self,
        archive_id: "capo_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.export_summary.ExportSummary]":
        _token = next_token
        while True:
            _response = await self.list_archive_exports(
                archive_id,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("exports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_archive_searches(
        self,
        archive_id: "capo_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_archive_searches_response.ListArchiveSearchesResponse":
        """<p>Returns a list of email archive search jobs.</p>

        Args:
            archive_id: <p>The identifier of the archive.</p>
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archive search jobs that are returned per call. You can use NextToken to obtain further pages of archives. </p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_archive_searches_request.ListArchiveSearchesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_archive_searches_response.ListArchiveSearchesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_archive_searches

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_archive_searches.async_list_archive_searches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_archive_searches_request.ListArchiveSearchesRequest = {
            "archive_id": archive_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_archive_searches(
        self,
        archive_id: "capo_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.search_summary.SearchSummary]":
        _token = next_token
        while True:
            _response = await self.list_archive_searches(
                archive_id,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("searches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_members_of_address_list(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        filter: Optional["capo_mailmanager.types.address_filter.AddressFilter"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional[
            "capo_mailmanager.types.address_page_size.AddressPageSize"
        ] = None,
    ) -> "capo_mailmanager.types.list_members_of_address_list_response.ListMembersOfAddressListResponse":
        """<p>Lists members of an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list to list the addresses from.</p>
            filter: <p>Filter to be used to limit the results.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of address list members that are returned per call. You can use NextToken to retrieve the next page of members.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_members_of_address_list_request.ListMembersOfAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_members_of_address_list_response.ListMembersOfAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_members_of_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_members_of_address_list.async_list_members_of_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_members_of_address_list_request.ListMembersOfAddressListRequest = {
            "address_list_id": address_list_id
        }
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_members_of_address_list(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        filter: Optional["capo_mailmanager.types.address_filter.AddressFilter"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional[
            "capo_mailmanager.types.address_page_size.AddressPageSize"
        ] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.saved_address.SavedAddress]":
        _token = next_token
        while True:
            _response = await self.list_members_of_address_list(
                address_list_id,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("addresses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_mailmanager.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Retrieves the list of tags (keys and values) assigned to the resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to retrieve tags from.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_member_to_address_list(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        address: "capo_mailmanager.types.address.Address",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.register_member_to_address_list_response.RegisterMemberToAddressListResponse":
        """<p>Adds a member to an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list where the address should be added.</p>
            address: <p>The address to be added to the address list.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.register_member_to_address_list_request.RegisterMemberToAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.register_member_to_address_list_response.RegisterMemberToAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.register_member_to_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.register_member_to_address_list.async_register_member_to_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.register_member_to_address_list_request.RegisterMemberToAddressListRequest = {
            "address_list_id": address_list_id,
            "address": address,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_address_list_import_job(
        self,
        job_id: "capo_mailmanager.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.start_address_list_import_job_response.StartAddressListImportJobResponse":
        """<p>Starts an import job for an address list.</p>

        Args:
            job_id: <p>The identifier of the import job that needs to be started.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.start_address_list_import_job_request.StartAddressListImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.start_address_list_import_job_response.StartAddressListImportJobResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.start_address_list_import_job

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.start_address_list_import_job.async_start_address_list_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.start_address_list_import_job_request.StartAddressListImportJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_archive_export(
        self,
        archive_id: "capo_mailmanager.types.archive_id.ArchiveId",
        from_timestamp: datetime.datetime,
        to_timestamp: datetime.datetime,
        export_destination_configuration: "capo_mailmanager.types.export_destination_configuration.ExportDestinationConfiguration",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        filters: Optional[
            "capo_mailmanager.types.archive_filters.ArchiveFilters"
        ] = None,
        max_results: Optional[
            "capo_mailmanager.types.export_max_results.ExportMaxResults"
        ] = None,
        include_metadata: Optional[bool] = None,
    ) -> "capo_mailmanager.types.start_archive_export_response.StartArchiveExportResponse":
        """<p>Initiates an export of emails from the specified archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to export emails from.</p>
            filters: <p>Criteria to filter which emails are included in the export.</p>
            from_timestamp: <p>The start of the timestamp range to include emails from.</p>
            to_timestamp: <p>The end of the timestamp range to include emails from.</p>
            max_results: <p>The maximum number of email items to include in the export.</p>
            export_destination_configuration: <p>Details on where to deliver the exported email data.</p>
            include_metadata: <p>Whether to include message metadata as JSON files in the export.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.start_archive_export_request.StartArchiveExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.start_archive_export_response.StartArchiveExportResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.start_archive_export

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.start_archive_export.async_start_archive_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.start_archive_export_request.StartArchiveExportRequest = {
            "archive_id": archive_id,
            "from_timestamp": from_timestamp,
            "to_timestamp": to_timestamp,
            "export_destination_configuration": export_destination_configuration,
        }
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if include_metadata is not None:
            input_["include_metadata"] = include_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_archive_search(
        self,
        archive_id: "capo_mailmanager.types.archive_id.ArchiveId",
        from_timestamp: datetime.datetime,
        to_timestamp: datetime.datetime,
        max_results: "capo_mailmanager.types.search_max_results.SearchMaxResults",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        filters: Optional[
            "capo_mailmanager.types.archive_filters.ArchiveFilters"
        ] = None,
    ) -> "capo_mailmanager.types.start_archive_search_response.StartArchiveSearchResponse":
        """<p>Initiates a search across emails in the specified archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to search emails in.</p>
            filters: <p>Criteria to filter which emails are included in the search results.</p>
            from_timestamp: <p>The start timestamp of the range to search emails from.</p>
            to_timestamp: <p>The end timestamp of the range to search emails from.</p>
            max_results: <p>The maximum number of search results to return.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.start_archive_search_request.StartArchiveSearchRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.start_archive_search_response.StartArchiveSearchResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.start_archive_search

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.start_archive_search.async_start_archive_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.start_archive_search_request.StartArchiveSearchRequest = {
            "archive_id": archive_id,
            "from_timestamp": from_timestamp,
            "to_timestamp": to_timestamp,
            "max_results": max_results,
        }
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_address_list_import_job(
        self,
        job_id: "capo_mailmanager.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.stop_address_list_import_job_response.StopAddressListImportJobResponse":
        """<p>Stops an ongoing import job for an address list.</p>

        Args:
            job_id: <p>The identifier of the import job that needs to be stopped.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.stop_address_list_import_job_request.StopAddressListImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.stop_address_list_import_job_response.StopAddressListImportJobResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.stop_address_list_import_job

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.stop_address_list_import_job.async_stop_address_list_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.stop_address_list_import_job_request.StopAddressListImportJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_archive_export(
        self,
        export_id: "capo_mailmanager.types.export_id.ExportId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> (
        "capo_mailmanager.types.stop_archive_export_response.StopArchiveExportResponse"
    ):
        """<p>Stops an in-progress export of emails from an archive.</p>

        Args:
            export_id: <p>The identifier of the export job to stop.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.stop_archive_export_request.StopArchiveExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.stop_archive_export_response.StopArchiveExportResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.stop_archive_export

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.stop_archive_export.async_stop_archive_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.stop_archive_export_request.StopArchiveExportRequest = {
            "export_id": export_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_archive_search(
        self,
        search_id: "capo_mailmanager.types.search_id.SearchId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> (
        "capo_mailmanager.types.stop_archive_search_response.StopArchiveSearchResponse"
    ):
        """<p>Stops an in-progress archive search job.</p>

        Args:
            search_id: <p>The identifier of the search job to stop.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.stop_archive_search_request.StopArchiveSearchRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.stop_archive_search_response.StopArchiveSearchResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.stop_archive_search

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.stop_archive_search.async_stop_archive_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.stop_archive_search_request.StopArchiveSearchRequest = {
            "search_id": search_id
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
        resource_arn: "capo_mailmanager.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_mailmanager.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.tag_resource_response.TagResourceResponse":
        """<p> Adds one or more tags (keys and values) to a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that you want to tag. </p>
            tags: <p> The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }. </p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.tag_resource

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_mailmanager.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_mailmanager.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.untag_resource_response.UntagResourceResponse":
        """<p> Remove one or more tags (keys and values) from a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that you want to untag. </p>
            tag_keys: <p> The keys of the key-value pairs for the tag or tags you want to remove from the specified resource. </p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.untag_resource

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_addon_instance(
        self,
        addon_subscription_id: "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_addon_instance_response.CreateAddonInstanceResponse":
        """<p>Creates an Add On instance for the subscription indicated in the request. The resulting Amazon Resource Name (ARN) can be used in a conditional statement for a rule set or traffic policy. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_subscription_id: <p>The unique ID of a previously created subscription that an Add On instance is created for. You can only have one instance per subscription.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_addon_instance_request.CreateAddonInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_addon_instance_response.CreateAddonInstanceResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_addon_instance

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_addon_instance.async_create_addon_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_addon_instance_request.CreateAddonInstanceRequest = {
            "addon_subscription_id": addon_subscription_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_addon_instance(
        self,
        addon_instance_id: "capo_mailmanager.types.addon_instance_id.AddonInstanceId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_addon_instance_response.GetAddonInstanceResponse":
        """<p>Gets detailed information about an Add On instance.</p>

        Args:
            addon_instance_id: <p>The Add On instance ID to retrieve information for.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_addon_instance_request.GetAddonInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_addon_instance_response.GetAddonInstanceResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_addon_instance

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_addon_instance.async_get_addon_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_addon_instance_request.GetAddonInstanceRequest = {
            "addon_instance_id": addon_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_addon_instance(
        self,
        addon_instance_id: "capo_mailmanager.types.addon_instance_id.AddonInstanceId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_addon_instance_response.DeleteAddonInstanceResponse":
        """<p>Deletes an Add On instance.</p>

        Args:
            addon_instance_id: <p>The Add On instance ID to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_addon_instance_request.DeleteAddonInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_addon_instance_response.DeleteAddonInstanceResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_addon_instance

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_addon_instance.async_delete_addon_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_addon_instance_request.DeleteAddonInstanceRequest = {
            "addon_instance_id": addon_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_addon_instances(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_addon_instances_response.ListAddonInstancesResponse":
        """<p>Lists all Add On instances in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_addon_instances_request.ListAddonInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_addon_instances_response.ListAddonInstancesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_addon_instances

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_addon_instances.async_list_addon_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_addon_instances_request.ListAddonInstancesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_addon_instances(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.addon_instance.AddonInstance]":
        _token = next_token
        while True:
            _response = await self.list_addon_instances(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("addon_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_addon_subscription(
        self,
        addon_name: "capo_mailmanager.types.addon_name.AddonName",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse":
        """<p>Creates a subscription for an Add On representing the acceptance of its terms of use and additional pricing. The subscription can then be used to create an instance for use in rule sets or traffic policies.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_name: <p>The name of the Add On to subscribe to. You can only have one subscription for each Add On name.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_addon_subscription

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_addon_subscription.async_create_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest = {
            "addon_name": addon_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_addon_subscription(
        self,
        addon_subscription_id: "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse":
        """<p>Gets detailed information about an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to retrieve information for.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_addon_subscription

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_addon_subscription.async_get_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest = {
            "addon_subscription_id": addon_subscription_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_addon_subscription(
        self,
        addon_subscription_id: "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse":
        """<p>Deletes an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_addon_subscription

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_addon_subscription.async_delete_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest = {
            "addon_subscription_id": addon_subscription_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_addon_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse":
        """<p>Lists all Add On subscriptions in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_addon_subscriptions

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_addon_subscriptions.async_list_addon_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_addon_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.addon_subscription.AddonSubscription]":
        _token = next_token
        while True:
            _response = await self.list_addon_subscriptions(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("addon_subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_address_list(
        self,
        address_list_name: "capo_mailmanager.types.address_list_name.AddressListName",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> (
        "capo_mailmanager.types.create_address_list_response.CreateAddressListResponse"
    ):
        """<p>Creates a new address list.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            address_list_name: <p>A user-friendly name for the address list.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_address_list_request.CreateAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_address_list_response.CreateAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_address_list.async_create_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_address_list_request.CreateAddressListRequest = {
            "address_list_name": address_list_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_address_list(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_address_list_response.GetAddressListResponse":
        """<p>Fetch attributes of an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to be retrieved.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_address_list_request.GetAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_address_list_response.GetAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_address_list.async_get_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_address_list_request.GetAddressListRequest = {
            "address_list_id": address_list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_address_list(
        self,
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> (
        "capo_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
    ):
        """<p>Deletes an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to delete.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_address_list_request.DeleteAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_address_list.async_delete_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_address_list_request.DeleteAddressListRequest = {
            "address_list_id": address_list_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_address_lists(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_address_lists_response.ListAddressListsResponse":
        """<p>Lists address lists for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of address list resources that are returned per call. You can use NextToken to retrieve the next page of address lists.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_address_lists_request.ListAddressListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_address_lists_response.ListAddressListsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_address_lists

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_address_lists.async_list_address_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_address_lists_request.ListAddressListsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_address_lists(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.address_list.AddressList]":
        _token = next_token
        while True:
            _response = await self.list_address_lists(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("address_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_archive(
        self,
        archive_name: "capo_mailmanager.types.archive_name_string.ArchiveNameString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        retention: Optional[
            "capo_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
        kms_key_arn: Optional["capo_mailmanager.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_archive_response.CreateArchiveResponse":
        """<p>Creates a new email archive resource for storing and retaining emails.</p>

        Args:
            client_token: <p>A unique token Amazon SES uses to recognize retries of this request.</p>
            archive_name: <p>A unique name for the new archive.</p>
            retention: <p>The period for retaining emails in the archive before automatic deletion.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_archive_request.CreateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_archive_response.CreateArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_archive.async_create_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_archive_request.CreateArchiveRequest = {
            "archive_name": archive_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if retention is not None:
            input_["retention"] = retention
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_archive(
        self,
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_archive_response.GetArchiveResponse":
        """<p>Retrieves the full details and current state of a specified email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to retrieve.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_archive_request.GetArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_archive_response.GetArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_archive.async_get_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_archive_request.GetArchiveRequest = {
            "archive_id": archive_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_archive(
        self,
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        archive_name: Optional[
            "capo_mailmanager.types.archive_name_string.ArchiveNameString"
        ] = None,
        retention: Optional[
            "capo_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
    ) -> "capo_mailmanager.types.update_archive_response.UpdateArchiveResponse":
        """<p>Updates the attributes of an existing email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to update.</p>
            archive_name: <p>A new, unique name for the archive.</p>
            retention: <p>A new retention period for emails in the archive.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_archive_request.UpdateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_archive_response.UpdateArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_archive.async_update_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_archive_request.UpdateArchiveRequest = {
            "archive_id": archive_id
        }
        if archive_name is not None:
            input_["archive_name"] = archive_name
        if retention is not None:
            input_["retention"] = retention

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_archive(
        self,
        archive_id: "capo_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_archive_response.DeleteArchiveResponse":
        """<p>Initiates deletion of an email archive. This changes the archive state to pending deletion. In this state, no new emails can be added, and existing archived emails become inaccessible (search, export, download). The archive and all of its contents will be permanently deleted 30 days after entering the pending deletion state, regardless of the configured retention period. </p>

        Args:
            archive_id: <p>The identifier of the archive to delete.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_archive_request.DeleteArchiveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_archive_response.DeleteArchiveResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_archive

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_archive.async_delete_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_archive_request.DeleteArchiveRequest = {
            "archive_id": archive_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_archives(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_archives_response.ListArchivesResponse":
        """<p>Returns a list of all email archives in your account.</p>

        Args:
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archives that are returned per call. You can use NextToken to obtain further pages of archives. </p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_archives_request.ListArchivesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_archives_response.ListArchivesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_archives

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_archives.async_list_archives(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_archives_request.ListArchivesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_archives(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.archive.Archive]":
        _token = next_token
        while True:
            _response = await self.list_archives(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("archives",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_ingress_point(
        self,
        ingress_point_name: "capo_mailmanager.types.ingress_point_name.IngressPointName",
        type: "capo_mailmanager.types.ingress_point_type.IngressPointType",
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        ingress_point_configuration: Optional[
            "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
        ] = None,
        network_configuration: Optional[
            "capo_mailmanager.types.network_configuration.NetworkConfiguration"
        ] = None,
        tls_policy: Optional["capo_mailmanager.types.tls_policy.TlsPolicy"] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_ingress_point_response.CreateIngressPointResponse":
        """<p>Provision a new ingress endpoint resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            ingress_point_name: <p>A user friendly name for an ingress endpoint resource.</p>
            type: <p>The type of the ingress endpoint to create.</p>
            rule_set_id: <p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>
            traffic_policy_id: <p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>
            ingress_point_configuration: <p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>
            network_configuration: <p>Specifies the network configuration for the ingress point. This allows you to create an IPv4-only, Dual-Stack, or PrivateLink type of ingress point. If not specified, the default network type is IPv4-only. </p>
            tls_policy: <p>The Transport Layer Security (TLS) policy for the ingress point. The FIPS value is only valid in US and Canada regions.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Open IngressPoint

            >>> await client.create_ingress_point(ingress_point_name='ingressPointName', type='OPEN', rule_set_id='rs-12345', traffic_policy_id='tp-12345', tags=[{'Key': 'key', 'Value': 'value'}])
            Create Auth IngressPoint with Password

            >>> await client.create_ingress_point(ingress_point_name='ingressPointName', type='AUTH', rule_set_id='rs-12345', traffic_policy_id='tp-12345', ingress_point_configuration={'SmtpPassword': 'smtpPassword'}, tags=[{'Key': 'key', 'Value': 'value'}])
            Create Auth IngressPoint with SecretsManager Secret

            >>> await client.create_ingress_point(ingress_point_name='ingressPointName', type='AUTH', rule_set_id='rs-12345', traffic_policy_id='tp-12345', ingress_point_configuration={'SecretArn': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:abcde'}, tags=[{'Key': 'key', 'Value': 'value'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_ingress_point_request.CreateIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_ingress_point_response.CreateIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_ingress_point.async_create_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_ingress_point_request.CreateIngressPointRequest = {
            "ingress_point_name": ingress_point_name,
            "type": type,
            "rule_set_id": rule_set_id,
            "traffic_policy_id": traffic_policy_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ingress_point_configuration is not None:
            input_["ingress_point_configuration"] = ingress_point_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ingress_point(
        self,
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        include_trust_store_contents: Optional[
            "capo_mailmanager.types.trust_store_response_option.TrustStoreResponseOption"
        ] = None,
    ) -> "capo_mailmanager.types.get_ingress_point_response.GetIngressPointResponse":
        """<p>Fetch ingress endpoint resource attributes.</p>

        Args:
            ingress_point_id: <p>The identifier of an ingress endpoint.</p>
            include_trust_store_contents: <p>Whether to include the trust store contents in the response. Use INCLUDE to retrieve trust store certificate and CRL contents.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get Open IngressPoint

            >>> await client.get_ingress_point(ingress_point_id='inp-12345')
            Get Auth IngressPoint

            >>> await client.get_ingress_point(ingress_point_id='inp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_ingress_point_request.GetIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_ingress_point_response.GetIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_ingress_point.async_get_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_ingress_point_request.GetIngressPointRequest = {
            "ingress_point_id": ingress_point_id
        }
        if include_trust_store_contents is not None:
            input_["include_trust_store_contents"] = include_trust_store_contents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ingress_point(
        self,
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        ingress_point_name: Optional[
            "capo_mailmanager.types.ingress_point_name.IngressPointName"
        ] = None,
        status_to_update: Optional[
            "capo_mailmanager.types.ingress_point_status_to_update.IngressPointStatusToUpdate"
        ] = None,
        rule_set_id: Optional["capo_mailmanager.types.rule_set_id.RuleSetId"] = None,
        traffic_policy_id: Optional[
            "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
        ] = None,
        ingress_point_configuration: Optional[
            "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
        ] = None,
        tls_policy: Optional["capo_mailmanager.types.tls_policy.TlsPolicy"] = None,
    ) -> "capo_mailmanager.types.update_ingress_point_response.UpdateIngressPointResponse":
        """<p>Update attributes of a provisioned ingress endpoint resource.</p>

        Args:
            ingress_point_id: <p>The identifier for the ingress endpoint you want to update.</p>
            ingress_point_name: <p>A user friendly name for the ingress endpoint resource.</p>
            status_to_update: <p>The update status of an ingress endpoint.</p>
            rule_set_id: <p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>
            traffic_policy_id: <p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>
            ingress_point_configuration: <p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>
            tls_policy: <p>The Transport Layer Security (TLS) policy for the ingress point. Valid values are REQUIRED, OPTIONAL. Only ingress endpoints using REQUIRED or OPTIONAL as TlsPolicy can be updated.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Open/Auth IngressPoint with new Name

            >>> await client.update_ingress_point(ingress_point_id='inp-12345', ingress_point_name='ingressPointNewName')
            Update Open/Auth IngressPoint with new RuleSetId / TrafficPolicyId

            >>> await client.update_ingress_point(ingress_point_id='inp-12345', rule_set_id='rs-12345', traffic_policy_id='tp-12345')
            Update Auth IngressPoint with new SmtpPassword

            >>> await client.update_ingress_point(ingress_point_id='inp-12345', ingress_point_configuration={'SmtpPassword': 'newSmtpPassword'})
            Update Auth IngressPoint with new SecretArn

            >>> await client.update_ingress_point(ingress_point_id='inp-12345', ingress_point_configuration={'SecretArn': 'arn:aws:secretsmanager:us-west-2:123456789012:secret:abcde'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_ingress_point_request.UpdateIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_ingress_point_response.UpdateIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_ingress_point.async_update_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_ingress_point_request.UpdateIngressPointRequest = {
            "ingress_point_id": ingress_point_id
        }
        if ingress_point_name is not None:
            input_["ingress_point_name"] = ingress_point_name
        if status_to_update is not None:
            input_["status_to_update"] = status_to_update
        if rule_set_id is not None:
            input_["rule_set_id"] = rule_set_id
        if traffic_policy_id is not None:
            input_["traffic_policy_id"] = traffic_policy_id
        if ingress_point_configuration is not None:
            input_["ingress_point_configuration"] = ingress_point_configuration
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ingress_point(
        self,
        ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_ingress_point_response.DeleteIngressPointResponse":
        """<p>Delete an ingress endpoint resource.</p>

        Args:
            ingress_point_id: <p>The identifier of the ingress endpoint resource that you want to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete IngressPoint

            >>> await client.delete_ingress_point(ingress_point_id='inp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_ingress_point_request.DeleteIngressPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_ingress_point_response.DeleteIngressPointResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_ingress_point

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_ingress_point.async_delete_ingress_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_ingress_point_request.DeleteIngressPointRequest = {
            "ingress_point_id": ingress_point_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ingress_points(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_mailmanager.types.list_ingress_points_response.ListIngressPointsResponse"
    ):
        """<p>List all ingress endpoint resources.</p>

        Args:
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List IngressPoints

            >>> await client.list_ingress_points()
            List IngressPoints with PageSize

            >>> await client.list_ingress_points(page_size=10)
            List IngressPoints with NextToken

            >>> await client.list_ingress_points(next_token='nextToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_ingress_points_request.ListIngressPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_ingress_points_response.ListIngressPointsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_ingress_points

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_ingress_points.async_list_ingress_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_ingress_points_request.ListIngressPointsRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_ingress_points(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.ingress_point.IngressPoint]":
        _token = next_token
        while True:
            _response = await self.list_ingress_points(
                config_overrides=config_overrides,
                page_size=page_size,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ingress_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_relay(
        self,
        relay_name: "capo_mailmanager.types.relay_name.RelayName",
        server_name: "capo_mailmanager.types.relay_server_name.RelayServerName",
        server_port: "capo_mailmanager.types.relay_server_port.RelayServerPort",
        authentication: "capo_mailmanager.types.relay_authentication.RelayAuthentication",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_relay_response.CreateRelayResponse":
        """<p>Creates a relay resource which can be used in rules to relay incoming emails to defined relay destinations. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            relay_name: <p>The unique name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_relay_request.CreateRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_relay_response.CreateRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_relay.async_create_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_relay_request.CreateRelayRequest = {
            "relay_name": relay_name,
            "server_name": server_name,
            "server_port": server_port,
            "authentication": authentication,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relay(
        self,
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_relay_response.GetRelayResponse":
        """<p>Fetch the relay resource and it's attributes.</p>

        Args:
            relay_id: <p>A unique relay identifier.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_relay_request.GetRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_relay_response.GetRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_relay.async_get_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_relay_request.GetRelayRequest = {
            "relay_id": relay_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_relay(
        self,
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        relay_name: Optional["capo_mailmanager.types.relay_name.RelayName"] = None,
        server_name: Optional[
            "capo_mailmanager.types.relay_server_name.RelayServerName"
        ] = None,
        server_port: Optional[
            "capo_mailmanager.types.relay_server_port.RelayServerPort"
        ] = None,
        authentication: Optional[
            "capo_mailmanager.types.relay_authentication.RelayAuthentication"
        ] = None,
    ) -> "capo_mailmanager.types.update_relay_response.UpdateRelayResponse":
        """<p>Updates the attributes of an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>
            relay_name: <p>The name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_relay_request.UpdateRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_relay_response.UpdateRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_relay.async_update_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_relay_request.UpdateRelayRequest = {
            "relay_id": relay_id
        }
        if relay_name is not None:
            input_["relay_name"] = relay_name
        if server_name is not None:
            input_["server_name"] = server_name
        if server_port is not None:
            input_["server_port"] = server_port
        if authentication is not None:
            input_["authentication"] = authentication

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_relay(
        self,
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_relay_response.DeleteRelayResponse":
        """<p>Deletes an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_relay_request.DeleteRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_relay_response.DeleteRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_relay.async_delete_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_relay_request.DeleteRelayRequest = {
            "relay_id": relay_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_relays(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional[int] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_mailmanager.types.list_relays_response.ListRelaysResponse":
        """<p>Lists all the existing relay resources.</p>

        Args:
            page_size: <p>The number of relays to be returned in one request.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_relays_request.ListRelaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_relays_response.ListRelaysResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_relays

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_relays.async_list_relays(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_relays_request.ListRelaysRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_relays(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional[int] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.relay.Relay]":
        _token = next_token
        while True:
            _response = await self.list_relays(
                config_overrides=config_overrides,
                page_size=page_size,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("relays",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_rule_set(
        self,
        rule_set_name: "capo_mailmanager.types.rule_set_name.RuleSetName",
        rules: "capo_mailmanager.types.rules.Rules",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_rule_set_response.CreateRuleSetResponse":
        """<p>Provision a new rule set.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            rule_set_name: <p>A user-friendly name for the rule set.</p>
            rules: <p>Conditional rules that are evaluated for determining actions on email.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_rule_set_request.CreateRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_rule_set_response.CreateRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_rule_set.async_create_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_rule_set_request.CreateRuleSetRequest = {
            "rule_set_name": rule_set_name,
            "rules": rules,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_rule_set(
        self,
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_rule_set_response.GetRuleSetResponse":
        """<p>Fetch attributes of a rule set.</p>

        Args:
            rule_set_id: <p>The identifier of an existing rule set to be retrieved.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_rule_set_request.GetRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_rule_set_response.GetRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_rule_set.async_get_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_rule_set_request.GetRuleSetRequest = {
            "rule_set_id": rule_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rule_set(
        self,
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        rule_set_name: Optional[
            "capo_mailmanager.types.rule_set_name.RuleSetName"
        ] = None,
        rules: Optional["capo_mailmanager.types.rules.Rules"] = None,
    ) -> "capo_mailmanager.types.update_rule_set_response.UpdateRuleSetResponse":
        """<p>Update attributes of an already provisioned rule set.</p>

        Args:
            rule_set_id: <p>The identifier of a rule set you want to update.</p>
            rule_set_name: <p>A user-friendly name for the rule set resource.</p>
            rules: <p>A new set of rules to replace the current rules of the rule set—these rules will override all the rules of the rule set.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_rule_set_request.UpdateRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_rule_set_response.UpdateRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_rule_set.async_update_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_rule_set_request.UpdateRuleSetRequest = {
            "rule_set_id": rule_set_id
        }
        if rule_set_name is not None:
            input_["rule_set_name"] = rule_set_name
        if rules is not None:
            input_["rules"] = rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rule_set(
        self,
        rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_rule_set_response.DeleteRuleSetResponse":
        """<p>Delete a rule set.</p>

        Args:
            rule_set_id: <p>The identifier of an existing rule set resource to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_rule_set_request.DeleteRuleSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_rule_set_response.DeleteRuleSetResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_rule_set

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_rule_set.async_delete_rule_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_rule_set_request.DeleteRuleSetRequest = {
            "rule_set_id": rule_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_rule_sets(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_rule_sets_response.ListRuleSetsResponse":
        """<p>List rule sets for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of rule set resources that are returned per call. You can use NextToken to obtain further rule sets.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_rule_sets_request.ListRuleSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_rule_sets_response.ListRuleSetsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_rule_sets

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_rule_sets.async_list_rule_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_rule_sets_request.ListRuleSetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_rule_sets(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.rule_set.RuleSet]":
        _token = next_token
        while True:
            _response = await self.list_rule_sets(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("rule_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_traffic_policy(
        self,
        traffic_policy_name: "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName",
        policy_statements: "capo_mailmanager.types.policy_statement_list.PolicyStatementList",
        default_action: "capo_mailmanager.types.accept_action.AcceptAction",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        max_message_size_bytes: Optional[
            "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse":
        """<p>Provision a new traffic policy resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>Conditional statements for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create TrafficPolicy

            >>> await client.create_traffic_policy(traffic_policy_name='trafficPolicyName', policy_statements=[{'Conditions': [{'IpExpression': {'Evaluate': {'Attribute': 'SENDER_IP'}, 'Operator': 'CIDR_MATCHES', 'Values': ['0.0.0.0/12']}}], 'Action': 'ALLOW'}], default_action='DENY')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_traffic_policy.async_create_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest = {
            "traffic_policy_name": traffic_policy_name,
            "policy_statements": policy_statements,
            "default_action": default_action,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if max_message_size_bytes is not None:
            input_["max_message_size_bytes"] = max_message_size_bytes
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_traffic_policy(
        self,
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse":
        """<p>Fetch attributes of a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy resource.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get TrafficPolicy

            >>> await client.get_traffic_policy(traffic_policy_id='tp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_traffic_policy.async_get_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_traffic_policy(
        self,
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        traffic_policy_name: Optional[
            "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName"
        ] = None,
        policy_statements: Optional[
            "capo_mailmanager.types.policy_statement_list.PolicyStatementList"
        ] = None,
        default_action: Optional[
            "capo_mailmanager.types.accept_action.AcceptAction"
        ] = None,
        max_message_size_bytes: Optional[
            "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
    ) -> "capo_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse":
        """<p>Update attributes of an already provisioned traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to update.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>The list of conditions to be updated for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update TrafficPolicy with new Name

            >>> await client.update_traffic_policy(traffic_policy_id='tp-12345', traffic_policy_name='trafficPolicyNewName')
            Update TrafficPolicy with new PolicyStatements

            >>> await client.update_traffic_policy(traffic_policy_id='tp-12345', policy_statements=[{'Conditions': [{'StringExpression': {'Evaluate': {'Attribute': 'RECIPIENT'}, 'Operator': 'EQUALS', 'Values': ['example@amazon.com', 'example@gmail.com']}}], 'Action': 'ALLOW'}])
            Update TrafficPolicy with new DefaultAction

            >>> await client.update_traffic_policy(traffic_policy_id='tp-12345', default_action='ALLOW')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_traffic_policy.async_update_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
        }
        if traffic_policy_name is not None:
            input_["traffic_policy_name"] = traffic_policy_name
        if policy_statements is not None:
            input_["policy_statements"] = policy_statements
        if default_action is not None:
            input_["default_action"] = default_action
        if max_message_size_bytes is not None:
            input_["max_message_size_bytes"] = max_message_size_bytes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_traffic_policy(
        self,
        traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse":
        """<p>Delete a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete TrafficPolicy

            >>> await client.delete_traffic_policy(traffic_policy_id='tp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_traffic_policy

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_traffic_policy.async_delete_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest = {
            "traffic_policy_id": traffic_policy_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_traffic_policies(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse":
        """<p>List traffic policy resources.</p>

        Args:
            page_size: <p>The maximum number of traffic policy resources that are returned per call. You can use NextToken to obtain further traffic policies.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List TrafficPolicies

            >>> await client.list_traffic_policies()
            List TrafficPolicies with PageSize

            >>> await client.list_traffic_policies(page_size=10)
            List TrafficPolicies with NextToken

            >>> await client.list_traffic_policies(next_token='nextToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_traffic_policies

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_traffic_policies.async_list_traffic_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_traffic_policies(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_mailmanager.types.traffic_policy.TrafficPolicy]":
        _token = next_token
        while True:
            _response = await self.list_traffic_policies(
                config_overrides=config_overrides,
                page_size=page_size,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("traffic_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

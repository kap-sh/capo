"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceQuotasV20190624``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_service_quotas._auth._signers
import capo_service_quotas._auth._sigv4
from capo_service_quotas._auth._identity import Credentials
from capo_service_quotas._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_service_quotas._auth._zapros_handler import AuthMiddleware
from capo_service_quotas._pagination import resolve_path as _resolve_path
from capo_service_quotas._services._aws_config import aaws_config
from capo_service_quotas._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_service_quotas.types.amazon_resource_name
    import capo_service_quotas.types.applied_level_enum
    import capo_service_quotas.types.associate_service_quota_template_request
    import capo_service_quotas.types.associate_service_quota_template_response
    import capo_service_quotas.types.aws_region
    import capo_service_quotas.types.create_support_case_request
    import capo_service_quotas.types.create_support_case_response
    import capo_service_quotas.types.delete_service_quota_increase_request_from_template_request
    import capo_service_quotas.types.delete_service_quota_increase_request_from_template_response
    import capo_service_quotas.types.disassociate_service_quota_template_request
    import capo_service_quotas.types.disassociate_service_quota_template_response
    import capo_service_quotas.types.exclusion_list
    import capo_service_quotas.types.get_association_for_service_quota_template_request
    import capo_service_quotas.types.get_association_for_service_quota_template_response
    import capo_service_quotas.types.get_auto_management_configuration_request
    import capo_service_quotas.types.get_auto_management_configuration_response
    import capo_service_quotas.types.get_aws_default_service_quota_request
    import capo_service_quotas.types.get_aws_default_service_quota_response
    import capo_service_quotas.types.get_quota_utilization_report_request
    import capo_service_quotas.types.get_quota_utilization_report_response
    import capo_service_quotas.types.get_requested_service_quota_change_request
    import capo_service_quotas.types.get_requested_service_quota_change_response
    import capo_service_quotas.types.get_service_quota_increase_request_from_template_request
    import capo_service_quotas.types.get_service_quota_increase_request_from_template_response
    import capo_service_quotas.types.get_service_quota_request
    import capo_service_quotas.types.get_service_quota_response
    import capo_service_quotas.types.input_tag_keys
    import capo_service_quotas.types.input_tags
    import capo_service_quotas.types.list_aws_default_service_quotas_request
    import capo_service_quotas.types.list_aws_default_service_quotas_response
    import capo_service_quotas.types.list_requested_service_quota_change_history_by_quota_request
    import capo_service_quotas.types.list_requested_service_quota_change_history_by_quota_response
    import capo_service_quotas.types.list_requested_service_quota_change_history_request
    import capo_service_quotas.types.list_requested_service_quota_change_history_response
    import capo_service_quotas.types.list_service_quota_increase_requests_in_template_request
    import capo_service_quotas.types.list_service_quota_increase_requests_in_template_response
    import capo_service_quotas.types.list_service_quotas_request
    import capo_service_quotas.types.list_service_quotas_response
    import capo_service_quotas.types.list_services_request
    import capo_service_quotas.types.list_services_response
    import capo_service_quotas.types.list_tags_for_resource_request
    import capo_service_quotas.types.list_tags_for_resource_response
    import capo_service_quotas.types.max_results
    import capo_service_quotas.types.max_results_utilization
    import capo_service_quotas.types.next_token
    import capo_service_quotas.types.opt_in_level
    import capo_service_quotas.types.opt_in_type
    import capo_service_quotas.types.put_service_quota_increase_request_into_template_request
    import capo_service_quotas.types.put_service_quota_increase_request_into_template_response
    import capo_service_quotas.types.quota_code
    import capo_service_quotas.types.quota_context_id
    import capo_service_quotas.types.quota_value
    import capo_service_quotas.types.report_id
    import capo_service_quotas.types.request_id
    import capo_service_quotas.types.request_service_quota_increase_request
    import capo_service_quotas.types.request_service_quota_increase_response
    import capo_service_quotas.types.request_status
    import capo_service_quotas.types.requested_service_quota_change
    import capo_service_quotas.types.service_code
    import capo_service_quotas.types.service_info
    import capo_service_quotas.types.service_quota
    import capo_service_quotas.types.service_quota_increase_request_in_template
    import capo_service_quotas.types.start_auto_management_request
    import capo_service_quotas.types.start_auto_management_response
    import capo_service_quotas.types.start_quota_utilization_report_request
    import capo_service_quotas.types.start_quota_utilization_report_response
    import capo_service_quotas.types.stop_auto_management_request
    import capo_service_quotas.types.stop_auto_management_response
    import capo_service_quotas.types.support_case_allowed
    import capo_service_quotas.types.tag_resource_request
    import capo_service_quotas.types.tag_resource_response
    import capo_service_quotas.types.untag_resource_request
    import capo_service_quotas.types.untag_resource_response
    import capo_service_quotas.types.update_auto_management_request
    import capo_service_quotas.types.update_auto_management_response


class AsyncServiceQuotasClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncServiceQuotasClient:
    """A client for the ``ServiceQuotas`` service.

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
        self._config = AsyncServiceQuotasClientConfig(
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
        self, config_overrides: Optional[AsyncServiceQuotasClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncServiceQuotasClientConfig = config_overrides or {}
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

    async def associate_service_quota_template(
        self, *, config_overrides: Optional[AsyncServiceQuotasClientConfig] = None
    ) -> "capo_service_quotas.types.associate_service_quota_template_response.AssociateServiceQuotaTemplateResponse":
        """<p>Associates your quota request template with your organization. When a new Amazon Web Services account is created in your organization, the quota increase requests in the template are automatically applied to the account. You can add a quota increase request for any adjustable quota to your template.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.aws_service_access_not_enabled_exception.AWSServiceAccessNotEnabledException: <p>The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>The Amazon Web Services account making this call is not a member of an organization.</p>
            capo_service_quotas.errors.organization_not_in_all_features_mode_exception.OrganizationNotInAllFeaturesModeException: <p>The organization that your Amazon Web Services account belongs to is not in All Features mode.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.templates_not_available_in_region_exception.TemplatesNotAvailableInRegionException: <p>The Service Quotas template is not available in this Amazon Web Services Region.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.associate_service_quota_template_request.AssociateServiceQuotaTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.associate_service_quota_template_response.AssociateServiceQuotaTemplateResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.associate_service_quota_template

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.associate_service_quota_template.async_associate_service_quota_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.associate_service_quota_template_request.AssociateServiceQuotaTemplateRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_support_case(
        self,
        request_id: "capo_service_quotas.types.request_id.RequestId",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.create_support_case_response.CreateSupportCaseResponse":
        """<p>Creates a Support case for an existing quota increase request. This call only creates a Support case if the request has a <code>Pending</code> status. </p>

        Args:
            request_id: <p>The ID of the pending quota increase request for which you want to open a Support case. </p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The resource is in an invalid state.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.create_support_case_request.CreateSupportCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.create_support_case_response.CreateSupportCaseResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.create_support_case

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.create_support_case.async_create_support_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.create_support_case_request.CreateSupportCaseRequest = {
            "request_id": request_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service_quota_increase_request_from_template(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        aws_region: "capo_service_quotas.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.delete_service_quota_increase_request_from_template_response.DeleteServiceQuotaIncreaseRequestFromTemplateResponse":
        """<p>Deletes the quota increase request for the specified quota from your quota request template.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>
            aws_region: <p>Specifies the Amazon Web Services Region for which the request was made.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.aws_service_access_not_enabled_exception.AWSServiceAccessNotEnabledException: <p>The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>The Amazon Web Services account making this call is not a member of an organization.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.templates_not_available_in_region_exception.TemplatesNotAvailableInRegionException: <p>The Service Quotas template is not available in this Amazon Web Services Region.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.delete_service_quota_increase_request_from_template_request.DeleteServiceQuotaIncreaseRequestFromTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.delete_service_quota_increase_request_from_template_response.DeleteServiceQuotaIncreaseRequestFromTemplateResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.delete_service_quota_increase_request_from_template

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.delete_service_quota_increase_request_from_template.async_delete_service_quota_increase_request_from_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.delete_service_quota_increase_request_from_template_request.DeleteServiceQuotaIncreaseRequestFromTemplateRequest = {
            "service_code": service_code,
            "quota_code": quota_code,
            "aws_region": aws_region,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_service_quota_template(
        self, *, config_overrides: Optional[AsyncServiceQuotasClientConfig] = None
    ) -> "capo_service_quotas.types.disassociate_service_quota_template_response.DisassociateServiceQuotaTemplateResponse":
        """<p>Disables your quota request template. After a template is disabled, the quota increase requests in the template are not applied to new Amazon Web Services accounts in your organization. Disabling a quota request template does not apply its quota increase requests.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.aws_service_access_not_enabled_exception.AWSServiceAccessNotEnabledException: <p>The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>The Amazon Web Services account making this call is not a member of an organization.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.service_quota_template_not_in_use_exception.ServiceQuotaTemplateNotInUseException: <p>The quota request template is not associated with your organization.</p>
            capo_service_quotas.errors.templates_not_available_in_region_exception.TemplatesNotAvailableInRegionException: <p>The Service Quotas template is not available in this Amazon Web Services Region.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.disassociate_service_quota_template_request.DisassociateServiceQuotaTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.disassociate_service_quota_template_response.DisassociateServiceQuotaTemplateResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.disassociate_service_quota_template

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.disassociate_service_quota_template.async_disassociate_service_quota_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.disassociate_service_quota_template_request.DisassociateServiceQuotaTemplateRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_association_for_service_quota_template(
        self, *, config_overrides: Optional[AsyncServiceQuotasClientConfig] = None
    ) -> "capo_service_quotas.types.get_association_for_service_quota_template_response.GetAssociationForServiceQuotaTemplateResponse":
        """<p>Retrieves the status of the association for the quota request template.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.aws_service_access_not_enabled_exception.AWSServiceAccessNotEnabledException: <p>The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>The Amazon Web Services account making this call is not a member of an organization.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.service_quota_template_not_in_use_exception.ServiceQuotaTemplateNotInUseException: <p>The quota request template is not associated with your organization.</p>
            capo_service_quotas.errors.templates_not_available_in_region_exception.TemplatesNotAvailableInRegionException: <p>The Service Quotas template is not available in this Amazon Web Services Region.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.get_association_for_service_quota_template_request.GetAssociationForServiceQuotaTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.get_association_for_service_quota_template_response.GetAssociationForServiceQuotaTemplateResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.get_association_for_service_quota_template

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.get_association_for_service_quota_template.async_get_association_for_service_quota_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.get_association_for_service_quota_template_request.GetAssociationForServiceQuotaTemplateRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_auto_management_configuration(
        self, *, config_overrides: Optional[AsyncServiceQuotasClientConfig] = None
    ) -> "capo_service_quotas.types.get_auto_management_configuration_response.GetAutoManagementConfigurationResponse":
        """<p>Retrieves information about your <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html">Service Quotas Automatic Management</a> configuration. Automatic Management monitors your Service Quotas utilization and notifies you before you run out of your allocated quotas.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.get_auto_management_configuration_request.GetAutoManagementConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.get_auto_management_configuration_response.GetAutoManagementConfigurationResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.get_auto_management_configuration

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.get_auto_management_configuration.async_get_auto_management_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.get_auto_management_configuration_request.GetAutoManagementConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_aws_default_service_quota(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.get_aws_default_service_quota_response.GetAWSDefaultServiceQuotaResponse":
        """<p>Retrieves the default value for the specified quota. The default value does not reflect any quota increases.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.get_aws_default_service_quota_request.GetAWSDefaultServiceQuotaRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.get_aws_default_service_quota_response.GetAWSDefaultServiceQuotaResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.get_aws_default_service_quota

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.get_aws_default_service_quota.async_get_aws_default_service_quota(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.get_aws_default_service_quota_request.GetAWSDefaultServiceQuotaRequest = {
            "service_code": service_code,
            "quota_code": quota_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_quota_utilization_report(
        self,
        report_id: "capo_service_quotas.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results_utilization.MaxResultsUtilization"
        ] = None,
    ) -> "capo_service_quotas.types.get_quota_utilization_report_response.GetQuotaUtilizationReportResponse":
        """<p>Retrieves the quota utilization report for your Amazon Web Services account. This operation returns paginated results showing your quota usage across all Amazon Web Services services, sorted by utilization percentage in descending order (highest utilization first).</p> <p>You must first initiate a report using the <code>StartQuotaUtilizationReport</code> operation. The report generation process is asynchronous and may take several seconds to complete. Poll this operation periodically to check the status and retrieve results when the report is ready.</p> <p>Each report contains up to 1,000 quota records per page. Use the <code>NextToken</code> parameter to retrieve additional pages of results. Reports are automatically deleted after 15 minutes.</p>

        Args:
            report_id: <p>The unique identifier for the quota utilization report. This identifier is returned by the <code>StartQuotaUtilizationReport</code> operation.</p>
            next_token: <p>A token that indicates the next page of results to retrieve. This token is returned in the response when there are more results available. Omit this parameter for the first request.</p>
            max_results: <p>The maximum number of results to return per page. The default value is 1,000 and the maximum allowed value is 1,000.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.get_quota_utilization_report_request.GetQuotaUtilizationReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.get_quota_utilization_report_response.GetQuotaUtilizationReportResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.get_quota_utilization_report

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.get_quota_utilization_report.async_get_quota_utilization_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.get_quota_utilization_report_request.GetQuotaUtilizationReportRequest = {
            "report_id": report_id
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

    async def get_requested_service_quota_change(
        self,
        request_id: "capo_service_quotas.types.request_id.RequestId",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.get_requested_service_quota_change_response.GetRequestedServiceQuotaChangeResponse":
        """<p>Retrieves information about the specified quota increase request.</p>

        Args:
            request_id: <p>Specifies the ID of the quota increase request.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.get_requested_service_quota_change_request.GetRequestedServiceQuotaChangeRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.get_requested_service_quota_change_response.GetRequestedServiceQuotaChangeResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.get_requested_service_quota_change

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.get_requested_service_quota_change.async_get_requested_service_quota_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.get_requested_service_quota_change_request.GetRequestedServiceQuotaChangeRequest = {
            "request_id": request_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_quota(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        context_id: Optional[
            "capo_service_quotas.types.quota_context_id.QuotaContextId"
        ] = None,
    ) -> "capo_service_quotas.types.get_service_quota_response.GetServiceQuotaResponse":
        """<p>Retrieves the applied quota value for the specified account-level or resource-level quota. For some quotas, only the default values are available. If the applied quota value is not available for a quota, the quota is not retrieved.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>
            context_id: <p>Specifies the resource with an Amazon Resource Name (ARN).</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.get_service_quota_request.GetServiceQuotaRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.get_service_quota_response.GetServiceQuotaResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.get_service_quota

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.get_service_quota.async_get_service_quota(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.get_service_quota_request.GetServiceQuotaRequest = {
            "service_code": service_code,
            "quota_code": quota_code,
        }
        if context_id is not None:
            input_["context_id"] = context_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_quota_increase_request_from_template(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        aws_region: "capo_service_quotas.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.get_service_quota_increase_request_from_template_response.GetServiceQuotaIncreaseRequestFromTemplateResponse":
        """<p>Retrieves information about the specified quota increase request in your quota request template.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>
            aws_region: <p>Specifies the Amazon Web Services Region for which you made the request.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.aws_service_access_not_enabled_exception.AWSServiceAccessNotEnabledException: <p>The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>The Amazon Web Services account making this call is not a member of an organization.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.templates_not_available_in_region_exception.TemplatesNotAvailableInRegionException: <p>The Service Quotas template is not available in this Amazon Web Services Region.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.get_service_quota_increase_request_from_template_request.GetServiceQuotaIncreaseRequestFromTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.get_service_quota_increase_request_from_template_response.GetServiceQuotaIncreaseRequestFromTemplateResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.get_service_quota_increase_request_from_template

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.get_service_quota_increase_request_from_template.async_get_service_quota_increase_request_from_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.get_service_quota_increase_request_from_template_request.GetServiceQuotaIncreaseRequestFromTemplateRequest = {
            "service_code": service_code,
            "quota_code": quota_code,
            "aws_region": aws_region,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_aws_default_service_quotas(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_service_quotas.types.list_aws_default_service_quotas_response.ListAWSDefaultServiceQuotasResponse":
        """<p>Lists the default values for the quotas for the specified Amazon Web Services service. A default value does not reflect any quota increases.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            next_token: <p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>
            max_results: <p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.list_aws_default_service_quotas_request.ListAWSDefaultServiceQuotasRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.list_aws_default_service_quotas_response.ListAWSDefaultServiceQuotasResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.list_aws_default_service_quotas

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.list_aws_default_service_quotas.async_list_aws_default_service_quotas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.list_aws_default_service_quotas_request.ListAWSDefaultServiceQuotasRequest = {
            "service_code": service_code
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

    async def iter_list_aws_default_service_quotas(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_service_quotas.types.service_quota.ServiceQuota]":
        _token = next_token
        while True:
            _response = await self.list_aws_default_service_quotas(
                service_code,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("quotas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_requested_service_quota_change_history(
        self,
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        service_code: Optional[
            "capo_service_quotas.types.service_code.ServiceCode"
        ] = None,
        status: Optional[
            "capo_service_quotas.types.request_status.RequestStatus"
        ] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
        quota_requested_at_level: Optional[
            "capo_service_quotas.types.applied_level_enum.AppliedLevelEnum"
        ] = None,
    ) -> "capo_service_quotas.types.list_requested_service_quota_change_history_response.ListRequestedServiceQuotaChangeHistoryResponse":
        """<p>Retrieves the quota increase requests for the specified Amazon Web Services service. Filter responses to return quota requests at either the account level, resource level, or all levels. Responses include any open or closed requests within 90 days.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            status: <p>Specifies that you want to filter the results to only the requests with the matching status.</p>
            next_token: <p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>
            max_results: <p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            quota_requested_at_level: <p>Filters the response to return quota requests for the <code>ACCOUNT</code>, <code>RESOURCE</code>, or <code>ALL</code> levels. <code>ACCOUNT</code> is the default.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.list_requested_service_quota_change_history_request.ListRequestedServiceQuotaChangeHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.list_requested_service_quota_change_history_response.ListRequestedServiceQuotaChangeHistoryResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.list_requested_service_quota_change_history

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.list_requested_service_quota_change_history.async_list_requested_service_quota_change_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.list_requested_service_quota_change_history_request.ListRequestedServiceQuotaChangeHistoryRequest = {}
        if service_code is not None:
            input_["service_code"] = service_code
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if quota_requested_at_level is not None:
            input_["quota_requested_at_level"] = quota_requested_at_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_requested_service_quota_change_history(
        self,
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        service_code: Optional[
            "capo_service_quotas.types.service_code.ServiceCode"
        ] = None,
        status: Optional[
            "capo_service_quotas.types.request_status.RequestStatus"
        ] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
        quota_requested_at_level: Optional[
            "capo_service_quotas.types.applied_level_enum.AppliedLevelEnum"
        ] = None,
    ) -> "AsyncIterator[capo_service_quotas.types.requested_service_quota_change.RequestedServiceQuotaChange]":
        _token = next_token
        while True:
            _response = await self.list_requested_service_quota_change_history(
                config_overrides=config_overrides,
                service_code=service_code,
                status=status,
                next_token=_token,
                max_results=max_results,
                quota_requested_at_level=quota_requested_at_level,
            )
            _page = _resolve_path(_response, ("requested_quotas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_requested_service_quota_change_history_by_quota(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        status: Optional[
            "capo_service_quotas.types.request_status.RequestStatus"
        ] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
        quota_requested_at_level: Optional[
            "capo_service_quotas.types.applied_level_enum.AppliedLevelEnum"
        ] = None,
    ) -> "capo_service_quotas.types.list_requested_service_quota_change_history_by_quota_response.ListRequestedServiceQuotaChangeHistoryByQuotaResponse":
        """<p>Retrieves the quota increase requests for the specified quota. Filter responses to return quota requests at either the account level, resource level, or all levels.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>
            status: <p>Specifies that you want to filter the results to only the requests with the matching status.</p>
            next_token: <p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>
            max_results: <p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            quota_requested_at_level: <p>Filters the response to return quota requests for the <code>ACCOUNT</code>, <code>RESOURCE</code>, or <code>ALL</code> levels. <code>ACCOUNT</code> is the default.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.list_requested_service_quota_change_history_by_quota_request.ListRequestedServiceQuotaChangeHistoryByQuotaRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.list_requested_service_quota_change_history_by_quota_response.ListRequestedServiceQuotaChangeHistoryByQuotaResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.list_requested_service_quota_change_history_by_quota

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.list_requested_service_quota_change_history_by_quota.async_list_requested_service_quota_change_history_by_quota(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.list_requested_service_quota_change_history_by_quota_request.ListRequestedServiceQuotaChangeHistoryByQuotaRequest = {
            "service_code": service_code,
            "quota_code": quota_code,
        }
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if quota_requested_at_level is not None:
            input_["quota_requested_at_level"] = quota_requested_at_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_requested_service_quota_change_history_by_quota(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        status: Optional[
            "capo_service_quotas.types.request_status.RequestStatus"
        ] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
        quota_requested_at_level: Optional[
            "capo_service_quotas.types.applied_level_enum.AppliedLevelEnum"
        ] = None,
    ) -> "AsyncIterator[capo_service_quotas.types.requested_service_quota_change.RequestedServiceQuotaChange]":
        _token = next_token
        while True:
            _response = await self.list_requested_service_quota_change_history_by_quota(
                service_code,
                quota_code,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
                quota_requested_at_level=quota_requested_at_level,
            )
            _page = _resolve_path(_response, ("requested_quotas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_quota_increase_requests_in_template(
        self,
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        service_code: Optional[
            "capo_service_quotas.types.service_code.ServiceCode"
        ] = None,
        aws_region: Optional["capo_service_quotas.types.aws_region.AwsRegion"] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_service_quotas.types.list_service_quota_increase_requests_in_template_response.ListServiceQuotaIncreaseRequestsInTemplateResponse":
        """<p>Lists the quota increase requests in the specified quota request template.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            aws_region: <p>Specifies the Amazon Web Services Region for which you made the request.</p>
            next_token: <p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>
            max_results: <p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.aws_service_access_not_enabled_exception.AWSServiceAccessNotEnabledException: <p>The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>The Amazon Web Services account making this call is not a member of an organization.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.templates_not_available_in_region_exception.TemplatesNotAvailableInRegionException: <p>The Service Quotas template is not available in this Amazon Web Services Region.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.list_service_quota_increase_requests_in_template_request.ListServiceQuotaIncreaseRequestsInTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.list_service_quota_increase_requests_in_template_response.ListServiceQuotaIncreaseRequestsInTemplateResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.list_service_quota_increase_requests_in_template

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.list_service_quota_increase_requests_in_template.async_list_service_quota_increase_requests_in_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.list_service_quota_increase_requests_in_template_request.ListServiceQuotaIncreaseRequestsInTemplateRequest = {}
        if service_code is not None:
            input_["service_code"] = service_code
        if aws_region is not None:
            input_["aws_region"] = aws_region
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

    async def iter_list_service_quota_increase_requests_in_template(
        self,
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        service_code: Optional[
            "capo_service_quotas.types.service_code.ServiceCode"
        ] = None,
        aws_region: Optional["capo_service_quotas.types.aws_region.AwsRegion"] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_service_quotas.types.service_quota_increase_request_in_template.ServiceQuotaIncreaseRequestInTemplate]":
        _token = next_token
        while True:
            _response = await self.list_service_quota_increase_requests_in_template(
                config_overrides=config_overrides,
                service_code=service_code,
                aws_region=aws_region,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("service_quota_increase_request_in_template_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_quotas(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
        quota_code: Optional["capo_service_quotas.types.quota_code.QuotaCode"] = None,
        quota_applied_at_level: Optional[
            "capo_service_quotas.types.applied_level_enum.AppliedLevelEnum"
        ] = None,
    ) -> "capo_service_quotas.types.list_service_quotas_response.ListServiceQuotasResponse":
        """<p>Lists the applied quota values for the specified Amazon Web Services service. For some quotas, only the default values are available. If the applied quota value is not available for a quota, the quota is not retrieved. Filter responses to return applied quota values at either the account level, resource level, or all levels.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            next_token: <p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>
            max_results: <p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>
            quota_applied_at_level: <p>Filters the response to return applied quota values for the <code>ACCOUNT</code>, <code>RESOURCE</code>, or <code>ALL</code> levels. <code>ACCOUNT</code> is the default.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.list_service_quotas_request.ListServiceQuotasRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.list_service_quotas_response.ListServiceQuotasResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.list_service_quotas

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.list_service_quotas.async_list_service_quotas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.list_service_quotas_request.ListServiceQuotasRequest = {
            "service_code": service_code
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if quota_code is not None:
            input_["quota_code"] = quota_code
        if quota_applied_at_level is not None:
            input_["quota_applied_at_level"] = quota_applied_at_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_quotas(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
        quota_code: Optional["capo_service_quotas.types.quota_code.QuotaCode"] = None,
        quota_applied_at_level: Optional[
            "capo_service_quotas.types.applied_level_enum.AppliedLevelEnum"
        ] = None,
    ) -> "AsyncIterator[capo_service_quotas.types.service_quota.ServiceQuota]":
        _token = next_token
        while True:
            _response = await self.list_service_quotas(
                service_code,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                quota_code=quota_code,
                quota_applied_at_level=quota_applied_at_level,
            )
            _page = _resolve_path(_response, ("quotas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_services(
        self,
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_service_quotas.types.list_services_response.ListServicesResponse":
        """<p>Lists the names and codes for the Amazon Web Services services integrated with Service Quotas.</p>

        Args:
            next_token: <p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>
            max_results: <p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.list_services_request.ListServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.list_services_response.ListServicesResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.list_services

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.list_services_request.ListServicesRequest = {}
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

    async def iter_list_services(
        self,
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        next_token: Optional["capo_service_quotas.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_service_quotas.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_service_quotas.types.service_info.ServiceInfo]":
        _token = next_token
        while True:
            _response = await self.list_services(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_service_quotas.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of the tags assigned to the specified applied quota.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the applied quota for which you want to list tags. You can get this information by using the Service Quotas console, or by listing the quotas using the <a href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">list-service-quotas</a> CLI command or the <a href="https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html">ListServiceQuotas</a> Amazon Web Services API operation.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_service_quota_increase_request_into_template(
        self,
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        aws_region: "capo_service_quotas.types.aws_region.AwsRegion",
        desired_value: "capo_service_quotas.types.quota_value.QuotaValue",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.put_service_quota_increase_request_into_template_response.PutServiceQuotaIncreaseRequestIntoTemplateResponse":
        """<p>Adds a quota increase request to your quota request template.</p>

        Args:
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            aws_region: <p>Specifies the Amazon Web Services Region to which the template applies.</p>
            desired_value: <p>Specifies the new, increased value for the quota.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.aws_service_access_not_enabled_exception.AWSServiceAccessNotEnabledException: <p>The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>The Amazon Web Services account making this call is not a member of an organization.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.quota_exceeded_exception.QuotaExceededException: <p>You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.templates_not_available_in_region_exception.TemplatesNotAvailableInRegionException: <p>The Service Quotas template is not available in this Amazon Web Services Region.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.put_service_quota_increase_request_into_template_request.PutServiceQuotaIncreaseRequestIntoTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.put_service_quota_increase_request_into_template_response.PutServiceQuotaIncreaseRequestIntoTemplateResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.put_service_quota_increase_request_into_template

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.put_service_quota_increase_request_into_template.async_put_service_quota_increase_request_into_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.put_service_quota_increase_request_into_template_request.PutServiceQuotaIncreaseRequestIntoTemplateRequest = {
            "quota_code": quota_code,
            "service_code": service_code,
            "aws_region": aws_region,
            "desired_value": desired_value,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def request_service_quota_increase(
        self,
        service_code: "capo_service_quotas.types.service_code.ServiceCode",
        quota_code: "capo_service_quotas.types.quota_code.QuotaCode",
        desired_value: "capo_service_quotas.types.quota_value.QuotaValue",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        context_id: Optional[
            "capo_service_quotas.types.quota_context_id.QuotaContextId"
        ] = None,
        support_case_allowed: Optional[
            "capo_service_quotas.types.support_case_allowed.SupportCaseAllowed"
        ] = None,
    ) -> "capo_service_quotas.types.request_service_quota_increase_response.RequestServiceQuotaIncreaseResponse":
        """<p>Submits a quota increase request for the specified quota at the account or resource level.</p>

        Args:
            service_code: <p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>
            quota_code: <p>Specifies the quota identifier. To find the quota code for a specific quota, use the <a>ListServiceQuotas</a> operation, and look for the <code>QuotaCode</code> response in the output for the quota you want.</p>
            desired_value: <p>Specifies the new, increased value for the quota.</p>
            context_id: <p>Specifies the resource with an Amazon Resource Name (ARN).</p>
            support_case_allowed: <p>Specifies if an Amazon Web Services Support case can be opened for the quota increase request. This parameter is optional. </p> <p>By default, this flag is set to <code>True</code> and Amazon Web Services may create a support case for some quota increase requests. You can set this flag to <code>False</code> if you do not want a support case created when you request a quota increase. If you set the flag to <code>False</code>, Amazon Web Services does not open a support case and updates the request status to <code>Not approved</code>. </p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.dependency_access_denied_exception.DependencyAccessDeniedException: <p>You can't perform this action because a dependency does not have access.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The resource is in an invalid state.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.quota_exceeded_exception.QuotaExceededException: <p>You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_service_quotas.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.request_service_quota_increase_request.RequestServiceQuotaIncreaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.request_service_quota_increase_response.RequestServiceQuotaIncreaseResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.request_service_quota_increase

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.request_service_quota_increase.async_request_service_quota_increase(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.request_service_quota_increase_request.RequestServiceQuotaIncreaseRequest = {
            "service_code": service_code,
            "quota_code": quota_code,
            "desired_value": desired_value,
        }
        if context_id is not None:
            input_["context_id"] = context_id
        if support_case_allowed is not None:
            input_["support_case_allowed"] = support_case_allowed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_auto_management(
        self,
        opt_in_level: "capo_service_quotas.types.opt_in_level.OptInLevel",
        opt_in_type: "capo_service_quotas.types.opt_in_type.OptInType",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        notification_arn: Optional[
            "capo_service_quotas.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        exclusion_list: Optional[
            "capo_service_quotas.types.exclusion_list.ExclusionList"
        ] = None,
    ) -> "capo_service_quotas.types.start_auto_management_response.StartAutoManagementResponse":
        """<p>Starts <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html">Service Quotas Automatic Management</a> for an Amazon Web Services account, including notification preferences and excluded quotas configurations. Automatic Management monitors your Service Quotas utilization and notifies you before you run out of your allocated quotas.</p>

        Args:
            opt_in_level: <p>Sets the opt-in level for Automatic Management. Only Amazon Web Services account level is supported.</p>
            opt_in_type: <p>Sets the opt-in type for Automatic Management. There are two modes: Notify only and Notify and Auto-Adjust. Currently, only NotifyOnly is available.</p>
            notification_arn: <p>The <a href="https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html#rlp-table">User Notifications</a> Amazon Resource Name (ARN) for Automatic Management notifications.</p>
            exclusion_list: <p>List of Amazon Web Services services excluded from Automatic Management. You won't be notified of Service Quotas utilization for Amazon Web Services services added to the Automatic Management exclusion list. </p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.start_auto_management_request.StartAutoManagementRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.start_auto_management_response.StartAutoManagementResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.start_auto_management

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.start_auto_management.async_start_auto_management(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.start_auto_management_request.StartAutoManagementRequest = {
            "opt_in_level": opt_in_level,
            "opt_in_type": opt_in_type,
        }
        if notification_arn is not None:
            input_["notification_arn"] = notification_arn
        if exclusion_list is not None:
            input_["exclusion_list"] = exclusion_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_quota_utilization_report(
        self, *, config_overrides: Optional[AsyncServiceQuotasClientConfig] = None
    ) -> "capo_service_quotas.types.start_quota_utilization_report_response.StartQuotaUtilizationReportResponse":
        """<p>Initiates the generation of a quota utilization report for your Amazon Web Services account. This asynchronous operation analyzes your quota usage across all Amazon Web Services services and returns a unique report identifier that you can use to retrieve the results.</p> <p>The report generation process may take several seconds to complete, depending on the number of quotas in your account. Use the <code>GetQuotaUtilizationReport</code> operation to check the status and retrieve the results when the report is ready.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.start_quota_utilization_report_request.StartQuotaUtilizationReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.start_quota_utilization_report_response.StartQuotaUtilizationReportResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.start_quota_utilization_report

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.start_quota_utilization_report.async_start_quota_utilization_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.start_quota_utilization_report_request.StartQuotaUtilizationReportRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_auto_management(
        self, *, config_overrides: Optional[AsyncServiceQuotasClientConfig] = None
    ) -> "capo_service_quotas.types.stop_auto_management_response.StopAutoManagementResponse":
        """<p>Stops <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html">Service Quotas Automatic Management</a> for an Amazon Web Services account and removes all associated configurations. Automatic Management monitors your Service Quotas utilization and notifies you before you run out of your allocated quotas.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.stop_auto_management_request.StopAutoManagementRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.stop_auto_management_response.StopAutoManagementResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.stop_auto_management

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.stop_auto_management.async_stop_auto_management(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.stop_auto_management_request.StopAutoManagementRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_service_quotas.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_service_quotas.types.input_tags.InputTags",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to the specified applied quota. You can include one or more tags to add to the quota.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the applied quota. You can get this information by using the Service Quotas console, or by listing the quotas using the <a href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">list-service-quotas</a> CLI command or the <a href="https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html">ListServiceQuotas</a> Amazon Web Services API operation.</p>
            tags: <p>The tags that you want to add to the resource.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The specified tag is a reserved word and cannot be used.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.too_many_tags_exception.TooManyTagsException: <p>You've exceeded the number of tags allowed for a resource. For more information, see <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/sq-tagging.html#sq-tagging-restrictions">Tag restrictions</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.tag_resource

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_service_quotas.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_service_quotas.types.input_tag_keys.InputTagKeys",
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
    ) -> "capo_service_quotas.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified applied quota. You can specify one or more tags to remove.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the applied quota that you want to untag. You can get this information by using the Service Quotas console, or by listing the quotas using the <a href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">list-service-quotas</a> CLI command or the <a href="https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html">ListServiceQuotas</a> Amazon Web Services API operation.</p>
            tag_keys: <p>The keys of the tags that you want to remove from the resource.</p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.untag_resource

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_auto_management(
        self,
        *,
        config_overrides: Optional[AsyncServiceQuotasClientConfig] = None,
        opt_in_type: Optional["capo_service_quotas.types.opt_in_type.OptInType"] = None,
        notification_arn: Optional[
            "capo_service_quotas.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        exclusion_list: Optional[
            "capo_service_quotas.types.exclusion_list.ExclusionList"
        ] = None,
    ) -> "capo_service_quotas.types.update_auto_management_response.UpdateAutoManagementResponse":
        """<p>Updates your <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html">Service Quotas Automatic Management</a> configuration, including notification preferences and excluded quotas. Automatic Management monitors your Service Quotas utilization and notifies you before you run out of your allocated quotas.</p>

        Args:
            opt_in_type: <p>Information on the opt-in type for your Automatic Management configuration. There are two modes: Notify only and Notify and Auto-Adjust. Currently, only NotifyOnly is available.</p>
            notification_arn: <p>The <a href="https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html#rlp-table">User Notifications</a> Amazon Resource Name (ARN) for Automatic Management notifications you want to update.</p>
            exclusion_list: <p>List of Amazon Web Services services you want to exclude from Automatic Management. You won't be notified of Service Quotas utilization for Amazon Web Services services added to the Automatic Management exclusion list. </p>

        Raises:
            capo_service_quotas.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_service_quotas.errors.illegal_argument_exception.IllegalArgumentException: <p>Invalid input was provided.</p>
            capo_service_quotas.errors.no_such_resource_exception.NoSuchResourceException: <p>The specified resource does not exist.</p>
            capo_service_quotas.errors.service_exception.ServiceException: <p>Something went wrong.</p>
            capo_service_quotas.errors.too_many_requests_exception.TooManyRequestsException: <p>Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.</p>
            capo_service_quotas.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_quotas.types.update_auto_management_request.UpdateAutoManagementRequest]",
        ) -> AsyncOperationResponse[
            "capo_service_quotas.types.update_auto_management_response.UpdateAutoManagementResponse"
        ]:
            import capo_service_quotas._operations.service_quotas_v20190624.update_auto_management

            (
                output,
                http_response,
            ) = await capo_service_quotas._operations.service_quotas_v20190624.update_auto_management.async_update_auto_management(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_quotas.types.update_auto_management_request.UpdateAutoManagementRequest = {}
        if opt_in_type is not None:
            input_["opt_in_type"] = opt_in_type
        if notification_arn is not None:
            input_["notification_arn"] = notification_arn
        if exclusion_list is not None:
            input_["exclusion_list"] = exclusion_list

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

"""Generated from Smithy shape ``com.amazonaws.billing#AWSBilling``."""

import datetime
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_billing._auth._signers
import capo_billing._auth._sigv4
from capo_billing._auth._identity import Credentials
from capo_billing._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_billing._auth._zapros_handler import AuthMiddleware
from capo_billing._pagination import resolve_path as _resolve_path
from capo_billing._services._aws_config import aws_config
from capo_billing._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.active_time_range
    import capo_billing.types.associate_source_views_request
    import capo_billing.types.associate_source_views_response
    import capo_billing.types.billing_feature
    import capo_billing.types.billing_feature_filters
    import capo_billing.types.billing_features
    import capo_billing.types.billing_preferences_per_key
    import capo_billing.types.billing_view_arn
    import capo_billing.types.billing_view_arn_list
    import capo_billing.types.billing_view_description
    import capo_billing.types.billing_view_list_element
    import capo_billing.types.billing_view_name
    import capo_billing.types.billing_view_segment_time_range
    import capo_billing.types.billing_view_segments_list_element
    import capo_billing.types.billing_view_source_views_list
    import capo_billing.types.billing_view_type_list
    import capo_billing.types.billing_views_max_results
    import capo_billing.types.client_token
    import capo_billing.types.create_billing_view_request
    import capo_billing.types.create_billing_view_response
    import capo_billing.types.credit_allocation_history_entry
    import capo_billing.types.delete_billing_view_request
    import capo_billing.types.delete_billing_view_response
    import capo_billing.types.disassociate_source_views_request
    import capo_billing.types.disassociate_source_views_response
    import capo_billing.types.enterprise_support_billing_month
    import capo_billing.types.expression
    import capo_billing.types.get_billing_preferences_request
    import capo_billing.types.get_billing_preferences_response
    import capo_billing.types.get_billing_view_request
    import capo_billing.types.get_billing_view_response
    import capo_billing.types.get_credit_allocation_history_request
    import capo_billing.types.get_credit_allocation_history_response
    import capo_billing.types.get_credits_request
    import capo_billing.types.get_credits_response
    import capo_billing.types.get_enterprise_support_charge_summary_request
    import capo_billing.types.get_enterprise_support_charge_summary_response
    import capo_billing.types.get_enterprise_support_contract_details_request
    import capo_billing.types.get_enterprise_support_contract_details_response
    import capo_billing.types.get_resource_policy_request
    import capo_billing.types.get_resource_policy_response
    import capo_billing.types.linked_account_charge
    import capo_billing.types.list_billing_view_segments_request
    import capo_billing.types.list_billing_view_segments_response
    import capo_billing.types.list_billing_views_request
    import capo_billing.types.list_billing_views_response
    import capo_billing.types.list_enterprise_support_linked_account_charges_request
    import capo_billing.types.list_enterprise_support_linked_account_charges_response
    import capo_billing.types.list_source_views_for_billing_view_request
    import capo_billing.types.list_source_views_for_billing_view_response
    import capo_billing.types.list_tags_for_resource_request
    import capo_billing.types.list_tags_for_resource_response
    import capo_billing.types.page_token
    import capo_billing.types.promo_code
    import capo_billing.types.redeem_credits_request
    import capo_billing.types.redeem_credits_response
    import capo_billing.types.resource_arn
    import capo_billing.types.resource_tag_key_list
    import capo_billing.types.resource_tag_list
    import capo_billing.types.string_searches
    import capo_billing.types.tag_resource_request
    import capo_billing.types.tag_resource_response
    import capo_billing.types.untag_resource_request
    import capo_billing.types.untag_resource_response
    import capo_billing.types.update_billing_preferences_request
    import capo_billing.types.update_billing_preferences_response
    import capo_billing.types.update_billing_view_request
    import capo_billing.types.update_billing_view_response


class BillingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class BillingClient:
    """A client for the ``Billing`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = BillingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[BillingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BillingClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def associate_source_views(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        source_views: "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.associate_source_views_response.AssociateSourceViewsResponse":
        """<p> Associates one or more source billing views with an existing billing view. This allows creating aggregate billing views that combine data from multiple sources. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing view to associate source views with. </p>
            source_views: <p> A list of ARNs of the source billing views to associate. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit of resources you can create, or exceeded the size of an individual resource. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke AssociateSourceViews

            >>> client.associate_source_views(arn='arn:aws:billing::123456789012:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', source_views=['arn:aws:billing::123456789012:billingview/primary', 'arn:aws:billing::123456789012:billingview/custom-d3f9c7e4-8b2f-4a6e-9d3b-2f7c8a1e5f6d'])
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.associate_source_views_request.AssociateSourceViewsRequest]",
        ) -> OperationResponse[
            "capo_billing.types.associate_source_views_response.AssociateSourceViewsResponse"
        ]:
            import capo_billing._operations.aws_billing.associate_source_views

            output, http_response = (
                capo_billing._operations.aws_billing.associate_source_views.associate_source_views(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.associate_source_views_request.AssociateSourceViewsRequest = {
            "arn": arn,
            "source_views": source_views,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_billing_view(
        self,
        name: "capo_billing.types.billing_view_name.BillingViewName",
        source_views: "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        description: Optional[
            "capo_billing.types.billing_view_description.BillingViewDescription"
        ] = None,
        data_filter_expression: Optional[
            "capo_billing.types.expression.Expression"
        ] = None,
        client_token: Optional["capo_billing.types.client_token.ClientToken"] = None,
        resource_tags: Optional[
            "capo_billing.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> "capo_billing.types.create_billing_view_response.CreateBillingViewResponse":
        """<p> Creates a billing view with the specified billing view attributes. </p>

        Args:
            name: <p> The name of the billing view. </p>
            description: <p> The description of the billing view. </p>
            source_views: <p>A list of billing views used as the data source for the custom billing view.</p>
            data_filter_expression: <p> See <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>
            client_token: <p>A unique, case-sensitive identifier you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. If the original request completes successfully, any subsequent retries complete successfully without performing any further actions with an idempotent request. </p>
            resource_tags: <p>A list of key value map specifying tags associated to the billing view being created. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit of resources you can create, or exceeded the size of an individual resource. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateBillingView

            >>> client.create_billing_view(name='Example Custom Billing View', source_views=['arn:aws:billing::123456789101:billingview/primary'], description='Custom Billing View Example', data_filter_expression={'dimensions': {'key': 'LINKED_ACCOUNT', 'values': ['000000000000']}})
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.create_billing_view_request.CreateBillingViewRequest]",
        ) -> OperationResponse[
            "capo_billing.types.create_billing_view_response.CreateBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.create_billing_view

            output, http_response = (
                capo_billing._operations.aws_billing.create_billing_view.create_billing_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.create_billing_view_request.CreateBillingViewRequest = {
            "name": name,
            "source_views": source_views,
        }
        if description is not None:
            input_["description"] = description
        if data_filter_expression is not None:
            input_["data_filter_expression"] = data_filter_expression
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_billing.types.delete_billing_view_response.DeleteBillingViewResponse":
        """<p>Deletes the specified billing view.</p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            force: <p> If set to true, forces deletion of the billing view even if it has derived resources (e.g. other billing views or budgets). Use with caution as this may break dependent resources. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke DeleteBillingView

            >>> client.delete_billing_view(arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.delete_billing_view_request.DeleteBillingViewRequest]",
        ) -> OperationResponse[
            "capo_billing.types.delete_billing_view_response.DeleteBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.delete_billing_view

            output, http_response = (
                capo_billing._operations.aws_billing.delete_billing_view.delete_billing_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.delete_billing_view_request.DeleteBillingViewRequest = {
            "arn": arn
        }
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_source_views(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        source_views: "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.disassociate_source_views_response.DisassociateSourceViewsResponse":
        """<p> Removes the association between one or more source billing views and an existing billing view. This allows modifying the composition of aggregate billing views. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing view to disassociate source views from. </p>
            source_views: <p> A list of ARNs of the source billing views to disassociate. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke DisassociateSourceViews

            >>> client.disassociate_source_views(arn='arn:aws:billing::123456789012:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', source_views=['arn:aws:billing::123456789012:billingview/primary', 'arn:aws:billing::123456789012:billingview/custom-d3f9c7e4-8b2f-4a6e-9d3b-2f7c8a1e5f6d'])
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.disassociate_source_views_request.DisassociateSourceViewsRequest]",
        ) -> OperationResponse[
            "capo_billing.types.disassociate_source_views_response.DisassociateSourceViewsResponse"
        ]:
            import capo_billing._operations.aws_billing.disassociate_source_views

            output, http_response = (
                capo_billing._operations.aws_billing.disassociate_source_views.disassociate_source_views(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.disassociate_source_views_request.DisassociateSourceViewsRequest = {
            "arn": arn,
            "source_views": source_views,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_billing_preferences(
        self,
        features: "capo_billing.types.billing_features.BillingFeatures",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_billing.types.billing_feature_filters.BillingFeatureFilters"
        ] = None,
    ) -> "capo_billing.types.get_billing_preferences_response.GetBillingPreferencesResponse":
        """<p>Retrieves billing preferences for the specified feature. Each feature controls a distinct billing capability: which accounts can share Reserved Instances or credits, whether billing alerts are enabled, the historical record of sharing changes, and per-credit options.</p>

        Args:
            next_token: <p>Pagination token from a previous response. Pass the value returned in <code>nextToken</code> to retrieve the next page of results.</p>
            max_results: <p>The maximum number of records to return per page. Range: 1 to 50. Default: 50.</p>
            features: <p>The feature to retrieve. Specify exactly one value. Valid values: <code>BILLING_ALERTS</code>, <code>RI_SHARING</code>, <code>RI_SHARING_HISTORY</code>, <code>CREDIT_SHARING</code>, <code>CREDIT_SHARING_HISTORY</code>, <code>CREDIT_LEVEL_SHARING</code>, <code>CREDIT_PREFERENCE_OPTIONS</code>.</p>
            filters: <p>Filters to narrow results. Specify exactly one filter when supplied. The supported filter name is <code>PREFERENCE_KEY</code>, which accepts 1 to 10 values to match preference keys.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.get_billing_preferences_request.GetBillingPreferencesRequest]",
        ) -> OperationResponse[
            "capo_billing.types.get_billing_preferences_response.GetBillingPreferencesResponse"
        ]:
            import capo_billing._operations.aws_billing.get_billing_preferences

            output, http_response = (
                capo_billing._operations.aws_billing.get_billing_preferences.get_billing_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_billing_preferences_request.GetBillingPreferencesRequest = {
            "features": features
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.get_billing_view_response.GetBillingViewResponse":
        """<p>Returns the metadata associated to the specified billing view ARN. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetBillingView

            >>> client.get_billing_view(arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.get_billing_view_request.GetBillingViewRequest]",
        ) -> OperationResponse[
            "capo_billing.types.get_billing_view_response.GetBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.get_billing_view

            output, http_response = (
                capo_billing._operations.aws_billing.get_billing_view.get_billing_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_billing_view_request.GetBillingViewRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_credit_allocation_history(
        self,
        account_id: "capo_billing.types.account_id.AccountId",
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        credit_id: Optional[int] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_billing.types.get_credit_allocation_history_response.GetCreditAllocationHistoryResponse":
        """<p>Returns the per-billing-month allocation history for credits applied to an Amazon Web Services account's bills. Traverses the consolidated billing family to capture cross-account credit applications. Supports pagination and optional filtering to a single credit.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID whose allocation history to retrieve. Must be a 12-digit numeric string.</p>
            credit_id: <p>Filters the result to a single credit. When omitted, returns allocation entries for all credits.</p>
            start_date: <p>Inclusive start date as Unix epoch seconds. Must be on or before <code>endDate</code>. The range from <code>startDate</code> to <code>endDate</code> cannot exceed 24 billing months.</p>
            end_date: <p>Inclusive end date as Unix epoch seconds.</p>
            next_token: <p>Pagination token from a previous response. Pass the value returned in <code>nextToken</code> to retrieve the next page of results.</p>
            max_results: <p>The maximum number of records to return per page. Range: 1 to 1000. Default: 100.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.get_credit_allocation_history_request.GetCreditAllocationHistoryRequest]",
        ) -> OperationResponse[
            "capo_billing.types.get_credit_allocation_history_response.GetCreditAllocationHistoryResponse"
        ]:
            import capo_billing._operations.aws_billing.get_credit_allocation_history

            output, http_response = (
                capo_billing._operations.aws_billing.get_credit_allocation_history.get_credit_allocation_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_credit_allocation_history_request.GetCreditAllocationHistoryRequest = {
            "account_id": account_id,
            "start_date": start_date,
            "end_date": end_date,
        }
        if credit_id is not None:
            input_["credit_id"] = credit_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_credit_allocation_history(
        self,
        account_id: "capo_billing.types.account_id.AccountId",
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        credit_id: Optional[int] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_billing.types.credit_allocation_history_entry.CreditAllocationHistoryEntry]":
        _token = next_token
        while True:
            _response = self.get_credit_allocation_history(
                account_id,
                start_date,
                end_date,
                config_overrides=config_overrides,
                credit_id=credit_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("credit_allocation_history_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_credits(
        self,
        account_id: str,
        start_date: datetime.datetime,
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        end_date: Optional[datetime.datetime] = None,
        payer_account_flag: Optional[bool] = None,
    ) -> "capo_billing.types.get_credits_response.GetCreditsResponse":
        """<p>Returns the list of Amazon Web Services account credits for the specified account. Each credit includes its identifier, type, monetary amounts, applicable products, expiration, sharing configuration, and current enabled status.</p> <p>When the caller is the management account of a consolidated billing family and <code>payerAccountFlag</code> is <code>true</code>, the response aggregates credits across the entire family. Otherwise, the response includes only credits owned by the account specified in <code>accountId</code>.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID. Must be a 12-digit numeric string.</p>
            start_date: <p>The start date for the credit period as Unix epoch seconds. Must be a past date that is not more than one year before the current date.</p>
            end_date: <p>The end date for the credit period as Unix epoch seconds. Must not be a future date and must be on or after <code>startDate</code>. Defaults to the current date when omitted.</p>
            payer_account_flag: <p>When <code>true</code> and the caller is the management account, the response aggregates credits across the entire consolidated billing family. When <code>false</code> or omitted, returns only credits for the specified <code>accountId</code>.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.get_credits_request.GetCreditsRequest]",
        ) -> OperationResponse[
            "capo_billing.types.get_credits_response.GetCreditsResponse"
        ]:
            import capo_billing._operations.aws_billing.get_credits

            output, http_response = (
                capo_billing._operations.aws_billing.get_credits.get_credits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_credits_request.GetCreditsRequest = {
            "account_id": account_id,
            "start_date": start_date,
        }
        if end_date is not None:
            input_["end_date"] = end_date
        if payer_account_flag is not None:
            input_["payer_account_flag"] = payer_account_flag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_enterprise_support_charge_summary(
        self,
        billing_month: "capo_billing.types.enterprise_support_billing_month.EnterpriseSupportBillingMonth",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.get_enterprise_support_charge_summary_response.GetEnterpriseSupportChargeSummaryResponse":
        """<p>Returns a summary of Enterprise Support data aggregated across all accounts in the Enterprise Support profile.</p>

        Args:
            billing_month: <p>The billing month in YYYY-MM format. This must be a month in the past.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.get_enterprise_support_charge_summary_request.GetEnterpriseSupportChargeSummaryRequest]",
        ) -> OperationResponse[
            "capo_billing.types.get_enterprise_support_charge_summary_response.GetEnterpriseSupportChargeSummaryResponse"
        ]:
            import capo_billing._operations.aws_billing.get_enterprise_support_charge_summary

            output, http_response = (
                capo_billing._operations.aws_billing.get_enterprise_support_charge_summary.get_enterprise_support_charge_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_enterprise_support_charge_summary_request.GetEnterpriseSupportChargeSummaryRequest = {
            "billing_month": billing_month
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_enterprise_support_contract_details(
        self,
        billing_month: "capo_billing.types.enterprise_support_billing_month.EnterpriseSupportBillingMonth",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.get_enterprise_support_contract_details_response.GetEnterpriseSupportContractDetailsResponse":
        """<p>Returns Enterprise Support contract details.</p>

        Args:
            billing_month: <p>The billing month in YYYY-MM format. This must be a month in the past.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.get_enterprise_support_contract_details_request.GetEnterpriseSupportContractDetailsRequest]",
        ) -> OperationResponse[
            "capo_billing.types.get_enterprise_support_contract_details_response.GetEnterpriseSupportContractDetailsResponse"
        ]:
            import capo_billing._operations.aws_billing.get_enterprise_support_contract_details

            output, http_response = (
                capo_billing._operations.aws_billing.get_enterprise_support_contract_details.get_enterprise_support_contract_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_enterprise_support_contract_details_request.GetEnterpriseSupportContractDetailsRequest = {
            "billing_month": billing_month
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns the resource-based policy document attached to the resource in <code>JSON</code> format. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the billing view resource to which the policy is attached to. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetResourcePolicy

            >>> client.get_resource_policy(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_billing.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_billing._operations.aws_billing.get_resource_policy

            output, http_response = (
                capo_billing._operations.aws_billing.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_billing_views(
        self,
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        active_time_range: Optional[
            "capo_billing.types.active_time_range.ActiveTimeRange"
        ] = None,
        arns: Optional[
            "capo_billing.types.billing_view_arn_list.BillingViewArnList"
        ] = None,
        billing_view_types: Optional[
            "capo_billing.types.billing_view_type_list.BillingViewTypeList"
        ] = None,
        names: Optional["capo_billing.types.string_searches.StringSearches"] = None,
        owner_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        source_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "capo_billing.types.list_billing_views_response.ListBillingViewsResponse":
        """<p>Lists the billing views available for a given time period. </p> <p>Every Amazon Web Services account has a unique <code>PRIMARY</code> billing view that represents the billing data available by default. Accounts that use Billing Conductor also have <code>BILLING_GROUP</code> billing views representing pro forma costs associated with each created billing group.</p>

        Args:
            active_time_range: <p> The time range for the billing views listed. <code>PRIMARY</code> billing view is always listed. <code>BILLING_GROUP</code> billing views are listed for time ranges when the associated billing group resource in Billing Conductor is active. The time range must be within one calendar month. </p>
            arns: <p>The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            billing_view_types: <p>The type of billing view.</p>
            names: <p> Filters the list of billing views by name. You can specify search criteria to match billing view names based on the search option provided. </p>
            owner_account_id: <p> The list of owners of the billing view. </p>
            source_account_id: <p> Filters the results to include only billing views that use the specified account as a source. </p>
            max_results: <p>The maximum number of billing views to retrieve. Default is 100. </p>
            next_token: <p>The pagination token that is used on subsequent calls to list billing views.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListBillingViews

            >>> client.list_billing_views(active_time_range={'activeAfterInclusive': 1719792000, 'activeBeforeInclusive': 1722470399.999})
            Error example for ListBillingViews

            >>> client.list_billing_views(active_time_range={'activeAfterInclusive': 1719792001, 'activeBeforeInclusive': 1719792000})
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.list_billing_views_request.ListBillingViewsRequest]",
        ) -> OperationResponse[
            "capo_billing.types.list_billing_views_response.ListBillingViewsResponse"
        ]:
            import capo_billing._operations.aws_billing.list_billing_views

            output, http_response = (
                capo_billing._operations.aws_billing.list_billing_views.list_billing_views(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_billing_views_request.ListBillingViewsRequest = {}
        if active_time_range is not None:
            input_["active_time_range"] = active_time_range
        if arns is not None:
            input_["arns"] = arns
        if billing_view_types is not None:
            input_["billing_view_types"] = billing_view_types
        if names is not None:
            input_["names"] = names
        if owner_account_id is not None:
            input_["owner_account_id"] = owner_account_id
        if source_account_id is not None:
            input_["source_account_id"] = source_account_id
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

    def iter_list_billing_views(
        self,
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        active_time_range: Optional[
            "capo_billing.types.active_time_range.ActiveTimeRange"
        ] = None,
        arns: Optional[
            "capo_billing.types.billing_view_arn_list.BillingViewArnList"
        ] = None,
        billing_view_types: Optional[
            "capo_billing.types.billing_view_type_list.BillingViewTypeList"
        ] = None,
        names: Optional["capo_billing.types.string_searches.StringSearches"] = None,
        owner_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        source_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> (
        "Iterator[capo_billing.types.billing_view_list_element.BillingViewListElement]"
    ):
        _token = next_token
        while True:
            _response = self.list_billing_views(
                config_overrides=config_overrides,
                active_time_range=active_time_range,
                arns=arns,
                billing_view_types=billing_view_types,
                names=names,
                owner_account_id=owner_account_id,
                source_account_id=source_account_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("billing_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_billing_view_segments(
        self,
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        time_range: Optional[
            "capo_billing.types.billing_view_segment_time_range.BillingViewSegmentTimeRange"
        ] = None,
        arn: Optional["capo_billing.types.billing_view_arn.BillingViewArn"] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "capo_billing.types.list_billing_view_segments_response.ListBillingViewSegmentsResponse":
        """<p>Lists the segments of a billing view over a given time period. Each segment identifies the billing domain (<code>PRO_FORMA</code> or <code>BILLABLE</code>) and the account relationships that apply during its time range.</p> <p>If you don't provide an <code>arn</code>, the response includes segments for the caller's <code>PRIMARY</code> billing view.</p> <p>If a mid-period change occurs, the response includes multiple segments, each with its own time range. The response omits hidden segments, so the segments it returns might not cover the entire requested time period.</p>

        Args:
            time_range: <p> The billing period to query. If you don't provide a time range, the current billing period, which is the calendar month in UTC, is used. </p>
            arn: <p> The Amazon Resource Name (ARN) that uniquely identifies the billing view to query. If you don't provide an ARN, the caller's <code>PRIMARY</code> billing view is used. The ARN must reference a primary billing view. Custom billing views aren't supported. </p>
            max_results: <p> The number of entries a paginated response contains. Valid values range from 1 to 100. The default is 100. </p>
            next_token: <p> The pagination token that is used on subsequent calls to list billing view segments. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListBillingViewSegments

            >>> client.list_billing_view_segments(time_range={'beginDateInclusive': 1719792000, 'endDateExclusive': 1722470400})
            Error example for ListBillingViewSegments

            >>> client.list_billing_view_segments(time_range={'beginDateInclusive': 1722470400, 'endDateExclusive': 1719792000})
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.list_billing_view_segments_request.ListBillingViewSegmentsRequest]",
        ) -> OperationResponse[
            "capo_billing.types.list_billing_view_segments_response.ListBillingViewSegmentsResponse"
        ]:
            import capo_billing._operations.aws_billing.list_billing_view_segments

            output, http_response = (
                capo_billing._operations.aws_billing.list_billing_view_segments.list_billing_view_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_billing_view_segments_request.ListBillingViewSegmentsRequest = {}
        if time_range is not None:
            input_["time_range"] = time_range
        if arn is not None:
            input_["arn"] = arn
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

    def iter_list_billing_view_segments(
        self,
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        time_range: Optional[
            "capo_billing.types.billing_view_segment_time_range.BillingViewSegmentTimeRange"
        ] = None,
        arn: Optional["capo_billing.types.billing_view_arn.BillingViewArn"] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "Iterator[capo_billing.types.billing_view_segments_list_element.BillingViewSegmentsListElement]":
        _token = next_token
        while True:
            _response = self.list_billing_view_segments(
                config_overrides=config_overrides,
                time_range=time_range,
                arn=arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_enterprise_support_linked_account_charges(
        self,
        billing_month: "capo_billing.types.enterprise_support_billing_month.EnterpriseSupportBillingMonth",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "capo_billing.types.list_enterprise_support_linked_account_charges_response.ListEnterpriseSupportLinkedAccountChargesResponse":
        """<p>Returns Support-eligible spend broken down at linked account level.</p>

        Args:
            billing_month: <p>The billing month in YYYY-MM format. This must be a month in the past.</p>
            account_id: <p>An optional linked account ID to filter results to a specific account.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The pagination token for the next page of results.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.list_enterprise_support_linked_account_charges_request.ListEnterpriseSupportLinkedAccountChargesRequest]",
        ) -> OperationResponse[
            "capo_billing.types.list_enterprise_support_linked_account_charges_response.ListEnterpriseSupportLinkedAccountChargesResponse"
        ]:
            import capo_billing._operations.aws_billing.list_enterprise_support_linked_account_charges

            output, http_response = (
                capo_billing._operations.aws_billing.list_enterprise_support_linked_account_charges.list_enterprise_support_linked_account_charges(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_enterprise_support_linked_account_charges_request.ListEnterpriseSupportLinkedAccountChargesRequest = {
            "billing_month": billing_month
        }
        if account_id is not None:
            input_["account_id"] = account_id
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

    def iter_list_enterprise_support_linked_account_charges(
        self,
        billing_month: "capo_billing.types.enterprise_support_billing_month.EnterpriseSupportBillingMonth",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "Iterator[capo_billing.types.linked_account_charge.LinkedAccountCharge]":
        _token = next_token
        while True:
            _response = self.list_enterprise_support_linked_account_charges(
                billing_month,
                config_overrides=config_overrides,
                account_id=account_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("linked_account",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_source_views_for_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "capo_billing.types.list_source_views_for_billing_view_response.ListSourceViewsForBillingViewResponse":
        """<p>Lists the source views (managed Amazon Web Services billing views) associated with the billing view. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            max_results: <p> The number of entries a paginated response contains. </p>
            next_token: <p> The pagination token that is used on subsequent calls to list billing views. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListSourceViewsForBillingView

            >>> client.list_source_views_for_billing_view(arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.list_source_views_for_billing_view_request.ListSourceViewsForBillingViewRequest]",
        ) -> OperationResponse[
            "capo_billing.types.list_source_views_for_billing_view_response.ListSourceViewsForBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.list_source_views_for_billing_view

            output, http_response = (
                capo_billing._operations.aws_billing.list_source_views_for_billing_view.list_source_views_for_billing_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_source_views_for_billing_view_request.ListSourceViewsForBillingViewRequest = {
            "arn": arn
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

    def iter_list_source_views_for_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "Iterator[capo_billing.types.billing_view_arn.BillingViewArn]":
        _token = next_token
        while True:
            _response = self.list_source_views_for_billing_view(
                arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("source_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> (
        "capo_billing.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists tags associated with the billing view resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListTagsForResource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_billing.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_billing._operations.aws_billing.list_tags_for_resource

            output, http_response = (
                capo_billing._operations.aws_billing.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def redeem_credits(
        self,
        promo_code: "capo_billing.types.promo_code.PromoCode",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.redeem_credits_response.RedeemCreditsResponse":
        """<p>Redeems an Amazon Web Services promotional credit code on behalf of the calling account. On success, a new credit is added to the account's credit ledger with the amount, validity period, and applicable products defined by the promotion. The credit is then automatically applied to subsequent bills according to the standard credit application order.</p>

        Args:
            promo_code: <p>The promotional credit code to redeem.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.redeem_credits_request.RedeemCreditsRequest]",
        ) -> OperationResponse[
            "capo_billing.types.redeem_credits_response.RedeemCreditsResponse"
        ]:
            import capo_billing._operations.aws_billing.redeem_credits

            output, http_response = (
                capo_billing._operations.aws_billing.redeem_credits.redeem_credits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.redeem_credits_request.RedeemCreditsRequest = {
            "promo_code": promo_code
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
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        resource_tags: "capo_billing.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.tag_resource_response.TagResourceResponse":
        """<p> An API operation for adding one or more tags (key-value pairs) to a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>
            resource_tags: <p> A list of tag key value pairs that are associated with the resource. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke TagResource

            >>> client.tag_resource(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', resource_tags=[{'key': 'ExampleTagKey', 'value': 'ExampleTagValue'}])
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_billing.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_billing._operations.aws_billing.tag_resource

            output, http_response = (
                capo_billing._operations.aws_billing.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tags": resource_tags,
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
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        resource_tag_keys: "capo_billing.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes one or more tags from a resource. Specify only tag keys in your request. Don't specify the value. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>
            resource_tag_keys: <p> A list of tag key value pairs that are associated with the resource. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UntagResource

            >>> client.untag_resource(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', resource_tag_keys=['ExampleTagKey'])
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_billing.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_billing._operations.aws_billing.untag_resource

            output, http_response = (
                capo_billing._operations.aws_billing.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tag_keys": resource_tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_billing_preferences(
        self,
        feature: "capo_billing.types.billing_feature.BillingFeature",
        billing_preferences_per_key: "capo_billing.types.billing_preferences_per_key.BillingPreferencesPerKey",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
    ) -> "capo_billing.types.update_billing_preferences_response.UpdateBillingPreferencesResponse":
        """<p>Updates billing preferences for the specified feature. Each feature targets a distinct billing capability and has its own set of supported keys. The action sets the value for each provided key; keys not present in the request are unchanged.</p> <p>Sharing keys (<code>RI_SHARING</code>, <code>CREDIT_SHARING</code>, <code>CREDIT_LEVEL_SHARING</code>, and sharing keys under <code>CREDIT_PREFERENCE_OPTIONS</code>) may only be set by the management account of a consolidated billing family. The <code>credit/{creditId}/status</code> key may be set by member accounts for credits they own, or by the management account for any credit in the family.</p>

        Args:
            feature: <p>The feature to update. Valid values: <code>BILLING_ALERTS</code>, <code>RI_SHARING</code>, <code>CREDIT_SHARING</code>, <code>CREDIT_LEVEL_SHARING</code>, <code>CREDIT_PREFERENCE_OPTIONS</code>. The history features (<code>RI_SHARING_HISTORY</code> and <code>CREDIT_SHARING_HISTORY</code>) are read-only and cannot be updated.</p>
            billing_preferences_per_key: <p>Key/value pairs to apply. All keys in a single request must be valid for the specified <code>feature</code> and must not be duplicated. For <code>CREDIT_PREFERENCE_OPTIONS</code>, all keys must reference the same <code>creditId</code>.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.update_billing_preferences_request.UpdateBillingPreferencesRequest]",
        ) -> OperationResponse[
            "capo_billing.types.update_billing_preferences_response.UpdateBillingPreferencesResponse"
        ]:
            import capo_billing._operations.aws_billing.update_billing_preferences

            output, http_response = (
                capo_billing._operations.aws_billing.update_billing_preferences.update_billing_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.update_billing_preferences_request.UpdateBillingPreferencesRequest = {
            "feature": feature,
            "billing_preferences_per_key": billing_preferences_per_key,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[BillingClientConfig] = None,
        name: Optional["capo_billing.types.billing_view_name.BillingViewName"] = None,
        description: Optional[
            "capo_billing.types.billing_view_description.BillingViewDescription"
        ] = None,
        data_filter_expression: Optional[
            "capo_billing.types.expression.Expression"
        ] = None,
    ) -> "capo_billing.types.update_billing_view_response.UpdateBillingViewResponse":
        """<p>An API to update the attributes of the billing view. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            name: <p> The name of the billing view. </p>
            description: <p> The description of the billing view. </p>
            data_filter_expression: <p>See <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit of resources you can create, or exceeded the size of an individual resource. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateBillingView

            >>> client.update_billing_view(name='Example Custom Billing View', arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', description='Custom Billing View Example -- updated description', data_filter_expression={'dimensions': {'key': 'LINKED_ACCOUNT', 'values': ['000000000000']}})
        """

        def _handler(
            req: "OperationRequest[capo_billing.types.update_billing_view_request.UpdateBillingViewRequest]",
        ) -> OperationResponse[
            "capo_billing.types.update_billing_view_response.UpdateBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.update_billing_view

            output, http_response = (
                capo_billing._operations.aws_billing.update_billing_view.update_billing_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.update_billing_view_request.UpdateBillingViewRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if data_filter_expression is not None:
            input_["data_filter_expression"] = data_filter_expression

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

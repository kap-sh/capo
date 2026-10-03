"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#AWSBCMPricingCalculator``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bcm_pricing_calculator._auth._signers
import capo_bcm_pricing_calculator._auth._sigv4
from capo_bcm_pricing_calculator._auth._identity import Credentials
from capo_bcm_pricing_calculator._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bcm_pricing_calculator._auth._zapros_handler import AuthMiddleware
from capo_bcm_pricing_calculator._pagination import resolve_path as _resolve_path
from capo_bcm_pricing_calculator._resources.awsbcm_pricing_calculator.bill_estimate import (
    AsyncBillEstimate,
)
from capo_bcm_pricing_calculator._resources.awsbcm_pricing_calculator.bill_scenario import (
    AsyncBillScenario,
)
from capo_bcm_pricing_calculator._resources.awsbcm_pricing_calculator.workload_estimate import (
    AsyncWorkloadEstimate,
)
from capo_bcm_pricing_calculator._services._aws_config import aaws_config
from capo_bcm_pricing_calculator._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.arn
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_request
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_response
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_request
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_response
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_request
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_response
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_request
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_response
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_request
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_response
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_request
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_response
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_request
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_response
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_request
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_response
    import capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary
    import capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary
    import capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary
    import capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary
    import capo_bcm_pricing_calculator.types.bill_estimate_name
    import capo_bcm_pricing_calculator.types.bill_estimate_summary
    import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item
    import capo_bcm_pricing_calculator.types.bill_scenario_name
    import capo_bcm_pricing_calculator.types.bill_scenario_summary
    import capo_bcm_pricing_calculator.types.bill_scenario_usage_modification_item
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.cost_category_arn
    import capo_bcm_pricing_calculator.types.create_bill_estimate_request
    import capo_bcm_pricing_calculator.types.create_bill_estimate_response
    import capo_bcm_pricing_calculator.types.create_bill_scenario_request
    import capo_bcm_pricing_calculator.types.create_bill_scenario_response
    import capo_bcm_pricing_calculator.types.create_workload_estimate_request
    import capo_bcm_pricing_calculator.types.create_workload_estimate_response
    import capo_bcm_pricing_calculator.types.delete_bill_estimate_request
    import capo_bcm_pricing_calculator.types.delete_bill_estimate_response
    import capo_bcm_pricing_calculator.types.delete_bill_scenario_request
    import capo_bcm_pricing_calculator.types.delete_bill_scenario_response
    import capo_bcm_pricing_calculator.types.delete_workload_estimate_request
    import capo_bcm_pricing_calculator.types.delete_workload_estimate_response
    import capo_bcm_pricing_calculator.types.filter_timestamp
    import capo_bcm_pricing_calculator.types.get_bill_estimate_request
    import capo_bcm_pricing_calculator.types.get_bill_estimate_response
    import capo_bcm_pricing_calculator.types.get_bill_scenario_request
    import capo_bcm_pricing_calculator.types.get_bill_scenario_response
    import capo_bcm_pricing_calculator.types.get_preferences_request
    import capo_bcm_pricing_calculator.types.get_preferences_response
    import capo_bcm_pricing_calculator.types.get_workload_estimate_request
    import capo_bcm_pricing_calculator.types.get_workload_estimate_response
    import capo_bcm_pricing_calculator.types.group_sharing_preference_enum
    import capo_bcm_pricing_calculator.types.list_bill_estimate_commitments_request
    import capo_bcm_pricing_calculator.types.list_bill_estimate_commitments_response
    import capo_bcm_pricing_calculator.types.list_bill_estimate_input_commitment_modifications_request
    import capo_bcm_pricing_calculator.types.list_bill_estimate_input_commitment_modifications_response
    import capo_bcm_pricing_calculator.types.list_bill_estimate_input_usage_modifications_request
    import capo_bcm_pricing_calculator.types.list_bill_estimate_input_usage_modifications_response
    import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filters
    import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_request
    import capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_response
    import capo_bcm_pricing_calculator.types.list_bill_estimates_filters
    import capo_bcm_pricing_calculator.types.list_bill_estimates_request
    import capo_bcm_pricing_calculator.types.list_bill_estimates_response
    import capo_bcm_pricing_calculator.types.list_bill_scenario_commitment_modifications_request
    import capo_bcm_pricing_calculator.types.list_bill_scenario_commitment_modifications_response
    import capo_bcm_pricing_calculator.types.list_bill_scenario_usage_modifications_request
    import capo_bcm_pricing_calculator.types.list_bill_scenario_usage_modifications_response
    import capo_bcm_pricing_calculator.types.list_bill_scenarios_filters
    import capo_bcm_pricing_calculator.types.list_bill_scenarios_request
    import capo_bcm_pricing_calculator.types.list_bill_scenarios_response
    import capo_bcm_pricing_calculator.types.list_tags_for_resource_request
    import capo_bcm_pricing_calculator.types.list_tags_for_resource_response
    import capo_bcm_pricing_calculator.types.list_usage_filters
    import capo_bcm_pricing_calculator.types.list_workload_estimate_usage_request
    import capo_bcm_pricing_calculator.types.list_workload_estimate_usage_response
    import capo_bcm_pricing_calculator.types.list_workload_estimates_filters
    import capo_bcm_pricing_calculator.types.list_workload_estimates_request
    import capo_bcm_pricing_calculator.types.list_workload_estimates_response
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.rate_types
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.resource_tag_keys
    import capo_bcm_pricing_calculator.types.tag_resource_request
    import capo_bcm_pricing_calculator.types.tag_resource_response
    import capo_bcm_pricing_calculator.types.tags
    import capo_bcm_pricing_calculator.types.untag_resource_request
    import capo_bcm_pricing_calculator.types.untag_resource_response
    import capo_bcm_pricing_calculator.types.update_bill_estimate_request
    import capo_bcm_pricing_calculator.types.update_bill_estimate_response
    import capo_bcm_pricing_calculator.types.update_bill_scenario_request
    import capo_bcm_pricing_calculator.types.update_bill_scenario_response
    import capo_bcm_pricing_calculator.types.update_preferences_request
    import capo_bcm_pricing_calculator.types.update_preferences_response
    import capo_bcm_pricing_calculator.types.update_workload_estimate_request
    import capo_bcm_pricing_calculator.types.update_workload_estimate_response
    import capo_bcm_pricing_calculator.types.workload_estimate_name
    import capo_bcm_pricing_calculator.types.workload_estimate_rate_type
    import capo_bcm_pricing_calculator.types.workload_estimate_summary
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_item
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_max_results


class AsyncBCMPricingCalculatorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncBCMPricingCalculatorClient:
    """A client for the ``BCMPricingCalculator`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
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
        self._config = AsyncBCMPricingCalculatorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.bill_estimate = AsyncBillEstimate(self)
        self.bill_scenario = AsyncBillScenario(self)
        self.workload_estimate = AsyncWorkloadEstimate(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBCMPricingCalculatorClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def get_preferences(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_preferences_response.GetPreferencesResponse":
        """<p> Retrieves the current preferences for Pricing Calculator. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.get_preferences_request.GetPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.get_preferences_response.GetPreferencesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_preferences

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_preferences.async_get_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.get_preferences_request.GetPreferencesRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        arn: "capo_bcm_pricing_calculator.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Lists all tags associated with a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to list tags for. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
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
        arn: "capo_bcm_pricing_calculator.types.arn.Arn",
        tags: "capo_bcm_pricing_calculator.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.tag_resource_response.TagResourceResponse":
        """<p> Adds one or more tags to a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to add tags to. </p>
            tags: <p> The tags to add to the resource. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.tag_resource

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.tag_resource_request.TagResourceRequest = {
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
        arn: "capo_bcm_pricing_calculator.types.arn.Arn",
        tag_keys: "capo_bcm_pricing_calculator.types.resource_tag_keys.ResourceTagKeys",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes one or more tags from a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to remove tags from. </p>
            tag_keys: <p> The keys of the tags to remove from the resource. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.untag_resource

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_preferences(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        management_account_rate_type_selections: Optional[
            "capo_bcm_pricing_calculator.types.rate_types.RateTypes"
        ] = None,
        member_account_rate_type_selections: Optional[
            "capo_bcm_pricing_calculator.types.rate_types.RateTypes"
        ] = None,
        standalone_account_rate_type_selections: Optional[
            "capo_bcm_pricing_calculator.types.rate_types.RateTypes"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_preferences_response.UpdatePreferencesResponse":
        """<p> Updates the preferences for Pricing Calculator. </p>

        Args:
            management_account_rate_type_selections: <p> The updated preferred rate types for the management account. </p>
            member_account_rate_type_selections: <p> The updated preferred rate types for member accounts. </p>
            standalone_account_rate_type_selections: <p> The updated preferred rate types for a standalone account. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.update_preferences_request.UpdatePreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.update_preferences_response.UpdatePreferencesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_preferences

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_preferences.async_update_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.update_preferences_request.UpdatePreferencesRequest = {}
        if management_account_rate_type_selections is not None:
            input_["management_account_rate_type_selections"] = (
                management_account_rate_type_selections
            )
        if member_account_rate_type_selections is not None:
            input_["member_account_rate_type_selections"] = (
                member_account_rate_type_selections
            )
        if standalone_account_rate_type_selections is not None:
            input_["standalone_account_rate_type_selections"] = (
                standalone_account_rate_type_selections
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bill_estimate(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        name: "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse":
        """<p> Create a Bill estimate from a Bill scenario. In the Bill scenario you can model usage addition, usage changes, and usage removal. You can also model commitment addition and commitment removal. After all changes in a Bill scenario is made satisfactorily, you can call this API with a Bill scenario ID to generate the Bill estimate. Bill estimate calculates the pre-tax cost for your consolidated billing family, incorporating all modeled usage and commitments alongside existing usage and commitments from your most recent completed anniversary bill, with any applicable discounts applied. </p>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to create a Bill estimate. </p>
            name: <p> The name of the Bill estimate that will be created. Names must be unique for an account. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>
            tags: <p> An optional list of tags to associate with the specified BillEstimate. You can use resource tags to control access to your BillEstimate using IAM policies. Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags: </p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services. </p> </li> <li> <p>The maximum length of a key is 128 characters.</p> </li> <li> <p>The maximum length of a value is 256 characters.</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code>.</p> </li> <li> <p>Keys and values are case sensitive.</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services.</p> </li> </ul>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate.async_create_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest = {
            "bill_scenario_id": bill_scenario_id,
            "name": name,
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

    async def get_bill_estimate(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse":
        """<p> Retrieves details of a specific bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to retrieve. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate.async_get_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bill_estimate(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        name: Optional[
            "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse":
        """<p> Updates an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to update. </p>
            name: <p> The new name for the bill estimate. </p>
            expires_at: <p> The new expiration date for the bill estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate.async_update_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if expires_at is not None:
            input_["expires_at"] = expires_at

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bill_estimate(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse":
        """<p> Deletes an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to delete. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate.async_delete_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_bill_estimates(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_estimates_filters.ListBillEstimatesFilters"
        ] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse":
        """<p> Lists all bill estimates for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill estimates. </p>
            created_at_filter: <p> Filter bill estimates based on the creation date. </p>
            expires_at_filter: <p> Filter bill estimates based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates.async_list_bill_estimates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if created_at_filter is not None:
            input_["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input_["expires_at_filter"] = expires_at_filter
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

    async def iter_list_bill_estimates(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_estimates_filters.ListBillEstimatesFilters"
        ] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_estimate_summary.BillEstimateSummary]":
        _token = next_token
        while True:
            _response = await self.list_bill_estimates(
                config_overrides=config_overrides,
                filters=filters,
                created_at_filter=created_at_filter,
                expires_at_filter=expires_at_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bill_estimate_commitments(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_estimate_commitments_response.ListBillEstimateCommitmentsResponse":
        """<p> Lists the commitments associated with a bill estimate. </p>

        Args:
            bill_estimate_id: <p> The unique identifier of the bill estimate to list commitments for. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_estimate_commitments_request.ListBillEstimateCommitmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_estimate_commitments_response.ListBillEstimateCommitmentsResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_commitments

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_commitments.async_list_bill_estimate_commitments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_estimate_commitments_request.ListBillEstimateCommitmentsRequest = {
            "bill_estimate_id": bill_estimate_id
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

    async def iter_list_bill_estimate_commitments(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_estimate_commitment_summary.BillEstimateCommitmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_bill_estimate_commitments(
                bill_estimate_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bill_estimate_input_commitment_modifications(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_estimate_input_commitment_modifications_response.ListBillEstimateInputCommitmentModificationsResponse":
        """<p> Lists the input commitment modifications associated with a bill estimate. </p>

        Args:
            bill_estimate_id: <p> The unique identifier of the bill estimate to list input commitment modifications for. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_estimate_input_commitment_modifications_request.ListBillEstimateInputCommitmentModificationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_estimate_input_commitment_modifications_response.ListBillEstimateInputCommitmentModificationsResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_input_commitment_modifications

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_input_commitment_modifications.async_list_bill_estimate_input_commitment_modifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_estimate_input_commitment_modifications_request.ListBillEstimateInputCommitmentModificationsRequest = {
            "bill_estimate_id": bill_estimate_id
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

    async def iter_list_bill_estimate_input_commitment_modifications(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_estimate_input_commitment_modification_summary.BillEstimateInputCommitmentModificationSummary]":
        _token = next_token
        while True:
            _response = await self.list_bill_estimate_input_commitment_modifications(
                bill_estimate_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bill_estimate_input_usage_modifications(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_usage_filters.ListUsageFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_estimate_input_usage_modifications_response.ListBillEstimateInputUsageModificationsResponse":
        """<p> Lists the input usage modifications associated with a bill estimate. </p>

        Args:
            bill_estimate_id: <p> The unique identifier of the bill estimate to list input usage modifications for. </p>
            filters: <p> Filters to apply to the list of input usage modifications. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_estimate_input_usage_modifications_request.ListBillEstimateInputUsageModificationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_estimate_input_usage_modifications_response.ListBillEstimateInputUsageModificationsResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_input_usage_modifications

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_input_usage_modifications.async_list_bill_estimate_input_usage_modifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_estimate_input_usage_modifications_request.ListBillEstimateInputUsageModificationsRequest = {
            "bill_estimate_id": bill_estimate_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_bill_estimate_input_usage_modifications(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_usage_filters.ListUsageFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_estimate_input_usage_modification_summary.BillEstimateInputUsageModificationSummary]":
        _token = next_token
        while True:
            _response = await self.list_bill_estimate_input_usage_modifications(
                bill_estimate_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bill_estimate_line_items(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filters.ListBillEstimateLineItemsFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_response.ListBillEstimateLineItemsResponse":
        """<p> Lists the line items associated with a bill estimate. </p>

        Args:
            bill_estimate_id: <p> The unique identifier of the bill estimate to list line items for. </p>
            filters: <p> Filters to apply to the list of line items. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_request.ListBillEstimateLineItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_response.ListBillEstimateLineItemsResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_line_items

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimate_line_items.async_list_bill_estimate_line_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_request.ListBillEstimateLineItemsRequest = {
            "bill_estimate_id": bill_estimate_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_bill_estimate_line_items(
        self,
        bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_estimate_line_items_filters.ListBillEstimateLineItemsFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_estimate_line_item_summary.BillEstimateLineItemSummary]":
        _token = next_token
        while True:
            _response = await self.list_bill_estimate_line_items(
                bill_estimate_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_bill_scenario(
        self,
        name: "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
        group_sharing_preference: Optional[
            "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse":
        """<p> Creates a new bill scenario to model potential changes to Amazon Web Services usage and costs. </p>

        Args:
            name: <p> A descriptive name for the bill scenario. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            tags: <p> The tags to apply to the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario.async_create_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if group_sharing_preference is not None:
            input_["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input_["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bill_scenario(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse":
        """<p> Retrieves details of a specific bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to retrieve. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario.async_get_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bill_scenario(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        name: Optional[
            "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
        group_sharing_preference: Optional[
            "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse":
        """<p> Updates an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to update. </p>
            name: <p> The new name for the bill scenario. </p>
            expires_at: <p> The new expiration date for the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario.async_update_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if expires_at is not None:
            input_["expires_at"] = expires_at
        if group_sharing_preference is not None:
            input_["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input_["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bill_scenario(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse":
        """<p> Deletes an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to delete. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario.async_delete_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_bill_scenarios(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_scenarios_filters.ListBillScenariosFilters"
        ] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse":
        """<p> Lists all bill scenarios for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill scenarios. </p>
            created_at_filter: <p> Filter bill scenarios based on the creation date. </p>
            expires_at_filter: <p> Filter bill scenarios based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios.async_list_bill_scenarios(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if created_at_filter is not None:
            input_["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input_["expires_at_filter"] = expires_at_filter
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

    async def iter_list_bill_scenarios(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_scenarios_filters.ListBillScenariosFilters"
        ] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_scenario_summary.BillScenarioSummary]":
        _token = next_token
        while True:
            _response = await self.list_bill_scenarios(
                config_overrides=config_overrides,
                filters=filters,
                created_at_filter=created_at_filter,
                expires_at_filter=expires_at_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bill_scenario_commitment_modifications(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_scenario_commitment_modifications_response.ListBillScenarioCommitmentModificationsResponse":
        """<p> Lists the commitment modifications associated with a bill scenario. </p>

        Args:
            bill_scenario_id: <p> The unique identifier of the bill scenario to list commitment modifications for. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_scenario_commitment_modifications_request.ListBillScenarioCommitmentModificationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_scenario_commitment_modifications_response.ListBillScenarioCommitmentModificationsResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenario_commitment_modifications

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenario_commitment_modifications.async_list_bill_scenario_commitment_modifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_scenario_commitment_modifications_request.ListBillScenarioCommitmentModificationsRequest = {
            "bill_scenario_id": bill_scenario_id
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

    async def iter_list_bill_scenario_commitment_modifications(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_item.BillScenarioCommitmentModificationItem]":
        _token = next_token
        while True:
            _response = await self.list_bill_scenario_commitment_modifications(
                bill_scenario_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_create_bill_scenario_commitment_modification(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        commitment_modifications: "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries.BatchCreateBillScenarioCommitmentModificationEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_response.BatchCreateBillScenarioCommitmentModificationResponse":
        """<p> Create Compute Savings Plans, EC2 Instance Savings Plans, or EC2 Reserved Instances commitments that you want to model in a Bill Scenario. </p> <note> <p>The <code>BatchCreateBillScenarioCommitmentModification</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:CreateBillScenarioCommitmentModification</code> in your policies.</p> </note>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to create the modeled commitment. </p>
            commitment_modifications: <p> List of commitments that you want to model in the Bill Scenario. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_request.BatchCreateBillScenarioCommitmentModificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_response.BatchCreateBillScenarioCommitmentModificationResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_create_bill_scenario_commitment_modification

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_create_bill_scenario_commitment_modification.async_batch_create_bill_scenario_commitment_modification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_request.BatchCreateBillScenarioCommitmentModificationRequest = {
            "bill_scenario_id": bill_scenario_id,
            "commitment_modifications": commitment_modifications,
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

    async def batch_delete_bill_scenario_commitment_modification(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        ids: "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries.BatchDeleteBillScenarioCommitmentModificationEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_response.BatchDeleteBillScenarioCommitmentModificationResponse":
        """<p> Delete commitment that you have created in a Bill Scenario. You can only delete a commitment that you had added and cannot model deletion (or removal) of a existing commitment. If you want model deletion of an existing commitment, see the negate <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction.html"> BillScenarioCommitmentModificationAction</a> of <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModification.html"> BatchCreateBillScenarioCommitmentModification</a> operation. </p> <note> <p>The <code>BatchDeleteBillScenarioCommitmentModification</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:DeleteBillScenarioCommitmentModification</code> in your policies.</p> </note>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to delete the modeled commitment. </p>
            ids: <p> List of commitments that you want to delete from the Bill Scenario. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_request.BatchDeleteBillScenarioCommitmentModificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_response.BatchDeleteBillScenarioCommitmentModificationResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_delete_bill_scenario_commitment_modification

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_delete_bill_scenario_commitment_modification.async_batch_delete_bill_scenario_commitment_modification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_request.BatchDeleteBillScenarioCommitmentModificationRequest = {
            "bill_scenario_id": bill_scenario_id,
            "ids": ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_bill_scenario_commitment_modification(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        commitment_modifications: "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries.BatchUpdateBillScenarioCommitmentModificationEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_response.BatchUpdateBillScenarioCommitmentModificationResponse":
        """<p> Update a newly added or existing commitment. You can update the commitment group based on a commitment ID and a Bill scenario ID. </p> <note> <p>The <code>BatchUpdateBillScenarioCommitmentModification</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:UpdateBillScenarioCommitmentModification</code> in your policies.</p> </note>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to modify the commitment group of a modeled commitment. </p>
            commitment_modifications: <p> List of commitments that you want to update in a Bill Scenario. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_request.BatchUpdateBillScenarioCommitmentModificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_response.BatchUpdateBillScenarioCommitmentModificationResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_update_bill_scenario_commitment_modification

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_update_bill_scenario_commitment_modification.async_batch_update_bill_scenario_commitment_modification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_request.BatchUpdateBillScenarioCommitmentModificationRequest = {
            "bill_scenario_id": bill_scenario_id,
            "commitment_modifications": commitment_modifications,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_bill_scenario_usage_modifications(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_usage_filters.ListUsageFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_scenario_usage_modifications_response.ListBillScenarioUsageModificationsResponse":
        """<p> Lists the usage modifications associated with a bill scenario. </p>

        Args:
            bill_scenario_id: <p> The unique identifier of the bill scenario to list usage modifications for. </p>
            filters: <p> Filters to apply to the list of usage modifications. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_scenario_usage_modifications_request.ListBillScenarioUsageModificationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_scenario_usage_modifications_response.ListBillScenarioUsageModificationsResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenario_usage_modifications

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenario_usage_modifications.async_list_bill_scenario_usage_modifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_bill_scenario_usage_modifications_request.ListBillScenarioUsageModificationsRequest = {
            "bill_scenario_id": bill_scenario_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_bill_scenario_usage_modifications(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_usage_filters.ListUsageFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.bill_scenario_usage_modification_item.BillScenarioUsageModificationItem]":
        _token = next_token
        while True:
            _response = await self.list_bill_scenario_usage_modifications(
                bill_scenario_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_create_bill_scenario_usage_modification(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        usage_modifications: "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries.BatchCreateBillScenarioUsageModificationEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse":
        """<p> Create Amazon Web Services service usage that you want to model in a Bill Scenario. </p> <note> <p>The <code>BatchCreateBillScenarioUsageModification</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:CreateBillScenarioUsageModification</code> in your policies.</p> </note>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to create the modeled usage. </p>
            usage_modifications: <p> List of usage that you want to model in the Bill Scenario. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request.BatchCreateBillScenarioUsageModificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_response.BatchCreateBillScenarioUsageModificationResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_create_bill_scenario_usage_modification

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_create_bill_scenario_usage_modification.async_batch_create_bill_scenario_usage_modification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_request.BatchCreateBillScenarioUsageModificationRequest = {
            "bill_scenario_id": bill_scenario_id,
            "usage_modifications": usage_modifications,
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

    async def batch_delete_bill_scenario_usage_modification(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        ids: "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries.BatchDeleteBillScenarioUsageModificationEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_response.BatchDeleteBillScenarioUsageModificationResponse":
        """<p> Delete usage that you have created in a Bill Scenario. You can only delete usage that you had added and cannot model deletion (or removal) of a existing usage. If you want model removal of an existing usage, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModification.html"> BatchUpdateBillScenarioUsageModification</a>. </p> <note> <p>The <code>BatchDeleteBillScenarioUsageModification</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:DeleteBillScenarioUsageModification</code> in your policies.</p> </note>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to delete the modeled usage. </p>
            ids: <p> List of usage that you want to delete from the Bill Scenario. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_request.BatchDeleteBillScenarioUsageModificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_response.BatchDeleteBillScenarioUsageModificationResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_delete_bill_scenario_usage_modification

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_delete_bill_scenario_usage_modification.async_batch_delete_bill_scenario_usage_modification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_request.BatchDeleteBillScenarioUsageModificationRequest = {
            "bill_scenario_id": bill_scenario_id,
            "ids": ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_bill_scenario_usage_modification(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        usage_modifications: "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries.BatchUpdateBillScenarioUsageModificationEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_response.BatchUpdateBillScenarioUsageModificationResponse":
        """<p> Update a newly added or existing usage lines. You can update the usage amounts, usage hour, and usage group based on a usage ID and a Bill scenario ID. </p> <note> <p>The <code>BatchUpdateBillScenarioUsageModification</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:UpdateBillScenarioUsageModification</code> in your policies.</p> </note>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to modify the usage lines. </p>
            usage_modifications: <p> List of usage lines that you want to update in a Bill Scenario identified by the usage ID. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_request.BatchUpdateBillScenarioUsageModificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_response.BatchUpdateBillScenarioUsageModificationResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_update_bill_scenario_usage_modification

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_update_bill_scenario_usage_modification.async_batch_update_bill_scenario_usage_modification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_request.BatchUpdateBillScenarioUsageModificationRequest = {
            "bill_scenario_id": bill_scenario_id,
            "usage_modifications": usage_modifications,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_workload_estimate(
        self,
        name: "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        rate_type: Optional[
            "capo_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse":
        """<p> Creates a new workload estimate to model costs for a specific workload. </p>

        Args:
            name: <p> A descriptive name for the workload estimate. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            rate_type: <p> The type of pricing rates to use for the estimate. </p>
            tags: <p> The tags to apply to the workload estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate.async_create_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rate_type is not None:
            input_["rate_type"] = rate_type
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workload_estimate(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse":
        """<p> Retrieves details of a specific workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to retrieve. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate.async_get_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workload_estimate(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        name: Optional[
            "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse":
        """<p> Updates an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to update. </p>
            name: <p> The new name for the workload estimate. </p>
            expires_at: <p> The new expiration date for the workload estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate.async_update_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if expires_at is not None:
            input_["expires_at"] = expires_at

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workload_estimate(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse":
        """<p> Deletes an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to delete. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate.async_delete_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workload_estimates(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_workload_estimates_filters.ListWorkloadEstimatesFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse":
        """<p> Lists all workload estimates for the account. </p>

        Args:
            created_at_filter: <p> Filter workload estimates based on the creation date. </p>
            expires_at_filter: <p> Filter workload estimates based on the expiration date. </p>
            filters: <p> Filters to apply to the list of workload estimates. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates.async_list_workload_estimates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest = {}
        if created_at_filter is not None:
            input_["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input_["expires_at_filter"] = expires_at_filter
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_workload_estimates(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_workload_estimates_filters.ListWorkloadEstimatesFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.workload_estimate_summary.WorkloadEstimateSummary]":
        _token = next_token
        while True:
            _response = await self.list_workload_estimates(
                config_overrides=config_overrides,
                created_at_filter=created_at_filter,
                expires_at_filter=expires_at_filter,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workload_estimate_usage(
        self,
        workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_usage_filters.ListUsageFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.workload_estimate_usage_max_results.WorkloadEstimateUsageMaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_workload_estimate_usage_response.ListWorkloadEstimateUsageResponse":
        """<p> Lists the usage associated with a workload estimate. </p>

        Args:
            workload_estimate_id: <p> The unique identifier of the workload estimate to list usage for. </p>
            filters: <p> Filters to apply to the list of usage items. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_workload_estimate_usage_request.ListWorkloadEstimateUsageRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_workload_estimate_usage_response.ListWorkloadEstimateUsageResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimate_usage

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimate_usage.async_list_workload_estimate_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.list_workload_estimate_usage_request.ListWorkloadEstimateUsageRequest = {
            "workload_estimate_id": workload_estimate_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_workload_estimate_usage(
        self,
        workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_usage_filters.ListUsageFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.workload_estimate_usage_max_results.WorkloadEstimateUsageMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bcm_pricing_calculator.types.workload_estimate_usage_item.WorkloadEstimateUsageItem]":
        _token = next_token
        while True:
            _response = await self.list_workload_estimate_usage(
                workload_estimate_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_create_workload_estimate_usage(
        self,
        workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        usage: "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries.BatchCreateWorkloadEstimateUsageEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_response.BatchCreateWorkloadEstimateUsageResponse":
        """<p> Create Amazon Web Services service usage that you want to model in a Workload Estimate. </p> <note> <p>The <code>BatchCreateWorkloadEstimateUsage</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:CreateWorkloadEstimateUsage</code> in your policies.</p> </note>

        Args:
            workload_estimate_id: <p> The ID of the Workload estimate for which you want to create the modeled usage. </p>
            usage: <p> List of usage that you want to model in the Workload estimate. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_request.BatchCreateWorkloadEstimateUsageRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_response.BatchCreateWorkloadEstimateUsageResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_create_workload_estimate_usage

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_create_workload_estimate_usage.async_batch_create_workload_estimate_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_request.BatchCreateWorkloadEstimateUsageRequest = {
            "workload_estimate_id": workload_estimate_id,
            "usage": usage,
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

    async def batch_delete_workload_estimate_usage(
        self,
        workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        ids: "capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries.BatchDeleteWorkloadEstimateUsageEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_response.BatchDeleteWorkloadEstimateUsageResponse":
        """<p> Delete usage that you have created in a Workload estimate. You can only delete usage that you had added and cannot model deletion (or removal) of a existing usage. If you want model removal of an existing usage, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsage.html"> BatchUpdateWorkloadEstimateUsage</a>. </p> <note> <p>The <code>BatchDeleteWorkloadEstimateUsage</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:DeleteWorkloadEstimateUsage</code> in your policies.</p> </note>

        Args:
            workload_estimate_id: <p> The ID of the Workload estimate for which you want to delete the modeled usage. </p>
            ids: <p> List of usage that you want to delete from the Workload estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_request.BatchDeleteWorkloadEstimateUsageRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_response.BatchDeleteWorkloadEstimateUsageResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_delete_workload_estimate_usage

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_delete_workload_estimate_usage.async_batch_delete_workload_estimate_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_request.BatchDeleteWorkloadEstimateUsageRequest = {
            "workload_estimate_id": workload_estimate_id,
            "ids": ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_workload_estimate_usage(
        self,
        workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        usage: "capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries.BatchUpdateWorkloadEstimateUsageEntries",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_response.BatchUpdateWorkloadEstimateUsageResponse":
        """<p> Update a newly added or existing usage lines. You can update the usage amounts and usage group based on a usage ID and a Workload estimate ID. </p> <note> <p>The <code>BatchUpdateWorkloadEstimateUsage</code> operation doesn't have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission <code>bcm-pricing-calculator:UpdateWorkloadEstimateUsage</code> in your policies.</p> </note>

        Args:
            workload_estimate_id: <p> The ID of the Workload estimate for which you want to modify the usage lines. </p>
            usage: <p> List of usage line amounts and usage group that you want to update in a Workload estimate identified by the usage ID. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_request.BatchUpdateWorkloadEstimateUsageRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_response.BatchUpdateWorkloadEstimateUsageResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_update_workload_estimate_usage

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.batch_update_workload_estimate_usage.async_batch_update_workload_estimate_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_request.BatchUpdateWorkloadEstimateUsageRequest = {
            "workload_estimate_id": workload_estimate_id,
            "usage": usage,
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

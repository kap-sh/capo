"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#AWSPricingPlanManager``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pricing_plan_manager._auth._signers
import capo_pricing_plan_manager._auth._sigv4
from capo_pricing_plan_manager._auth._identity import Credentials
from capo_pricing_plan_manager._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pricing_plan_manager._auth._zapros_handler import AuthMiddleware
from capo_pricing_plan_manager._pagination import resolve_path as _resolve_path
from capo_pricing_plan_manager._services._aws_config import aaws_config
from capo_pricing_plan_manager._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.approval_mode
    import capo_pricing_plan_manager.types.approve_paid_subscription_input
    import capo_pricing_plan_manager.types.approve_paid_subscription_output
    import capo_pricing_plan_manager.types.associate_resources_to_subscription_input
    import capo_pricing_plan_manager.types.associate_resources_to_subscription_output
    import capo_pricing_plan_manager.types.cancel_subscription_change_input
    import capo_pricing_plan_manager.types.cancel_subscription_change_output
    import capo_pricing_plan_manager.types.cancel_subscription_input
    import capo_pricing_plan_manager.types.cancel_subscription_output
    import capo_pricing_plan_manager.types.create_subscription_input
    import capo_pricing_plan_manager.types.create_subscription_output
    import capo_pricing_plan_manager.types.disassociate_resources_from_subscription_input
    import capo_pricing_plan_manager.types.disassociate_resources_from_subscription_output
    import capo_pricing_plan_manager.types.get_subscription_input
    import capo_pricing_plan_manager.types.get_subscription_output
    import capo_pricing_plan_manager.types.idempotency_token
    import capo_pricing_plan_manager.types.list_subscriptions_input
    import capo_pricing_plan_manager.types.list_subscriptions_output
    import capo_pricing_plan_manager.types.resource_arns
    import capo_pricing_plan_manager.types.subscription_arn
    import capo_pricing_plan_manager.types.subscription_summary
    import capo_pricing_plan_manager.types.update_subscription_input
    import capo_pricing_plan_manager.types.update_subscription_output


class AsyncPricingPlanManagerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPricingPlanManagerClient:
    """A client for the ``PricingPlanManager`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        self._config = AsyncPricingPlanManagerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPricingPlanManagerClientConfig = config_overrides or {}
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
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def approve_paid_subscription(
        self,
        arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn",
        if_match: str,
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        client_token: Optional[
            "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_pricing_plan_manager.types.approve_paid_subscription_output.ApprovePaidSubscriptionOutput":
        """<p>Approves a subscription that is in <code>PENDING_APPROVAL</code> status, activating it and starting billing.</p> <note> <p>This operation requires the current <code>ETag</code> value for concurrency control. Retrieve it from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response.</p> </note>

        Args:
            arn: <p>The ARN of the subscription to approve.</p>
            if_match: <p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response. This ensures you are approving the expected version of the subscription.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This typically occurs when the <code>ETag</code> value in the <code>If-Match</code> header does not match the current version of the subscription. Retrieve the latest version and retry.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Approve a pending paid subscription

            >>> await client.approve_paid_subscription(arn='arn:aws:pricingplanmanager::123456789012:subscription/sub-1234567890', if_match='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.approve_paid_subscription_input.ApprovePaidSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.approve_paid_subscription_output.ApprovePaidSubscriptionOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.approve_paid_subscription

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.approve_paid_subscription.async_approve_paid_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.approve_paid_subscription_input.ApprovePaidSubscriptionInput = {
            "arn": arn,
            "if_match": if_match,
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

    async def associate_resources_to_subscription(
        self,
        arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn",
        resource_arns: "capo_pricing_plan_manager.types.resource_arns.ResourceArns",
        if_match: str,
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        client_token: Optional[
            "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_pricing_plan_manager.types.associate_resources_to_subscription_output.AssociateResourcesToSubscriptionOutput":
        """<p>Adds one or more resources to an existing subscription. The subscription must be in an active state that is not pending other changes.</p> <note> <p>For subscriptions in the CloudFront plan family, the associated resources must include exactly one Amazon CloudFront distribution and one WAF web ACL. You can also include other supported resources, such as Amazon Route 53 hosted zones, and CloudFront KeyValueStores.</p> </note>

        Args:
            arn: <p>The ARN of the subscription to add resources to.</p>
            resource_arns: <p>The ARNs of the resources to add to the subscription.</p>
            if_match: <p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This typically occurs when the <code>ETag</code> value in the <code>If-Match</code> header does not match the current version of the subscription. Retrieve the latest version and retry.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Associate additional resources to a subscription

            >>> await client.associate_resources_to_subscription(arn='arn:aws:pricingplanmanager::123456789012:subscription/sub-1234567890', resource_arns=['arn:aws:route53:::hostedzone/Z0123456789EXAMPLE'], if_match='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.associate_resources_to_subscription_input.AssociateResourcesToSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.associate_resources_to_subscription_output.AssociateResourcesToSubscriptionOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.associate_resources_to_subscription

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.associate_resources_to_subscription.async_associate_resources_to_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.associate_resources_to_subscription_input.AssociateResourcesToSubscriptionInput = {
            "arn": arn,
            "resource_arns": resource_arns,
            "if_match": if_match,
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

    async def cancel_subscription(
        self,
        arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn",
        if_match: str,
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        client_token: Optional[
            "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_pricing_plan_manager.types.cancel_subscription_output.CancelSubscriptionOutput":
        """<p>Cancels a flat-rate pricing subscription.</p> <note> <p>For active subscriptions, the cancellation is scheduled to take effect at the end of the current billing period. The subscription remains active until that date. To revert a pending cancellation, use <code>CancelSubscriptionChange</code>.</p> <p>For subscriptions in <code>PENDING_APPROVAL</code> status, the subscription is deleted immediately without scheduling.</p> </note>

        Args:
            arn: <p>The ARN of the subscription to cancel.</p>
            if_match: <p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This typically occurs when the <code>ETag</code> value in the <code>If-Match</code> header does not match the current version of the subscription. Retrieve the latest version and retry.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a subscription

            >>> await client.cancel_subscription(arn='arn:aws:pricingplanmanager::123456789012:subscription/sub-1234567890', if_match='2')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.cancel_subscription_input.CancelSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.cancel_subscription_output.CancelSubscriptionOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.cancel_subscription

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.cancel_subscription.async_cancel_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.cancel_subscription_input.CancelSubscriptionInput = {
            "arn": arn,
            "if_match": if_match,
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

    async def cancel_subscription_change(
        self,
        arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn",
        if_match: str,
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        client_token: Optional[
            "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_pricing_plan_manager.types.cancel_subscription_change_output.CancelSubscriptionChangeOutput":
        """<p>Cancels a pending scheduled change on a subscription, such as a pending downgrade or cancellation. The subscription returns to its state before the change was scheduled.</p> <note> <p>You cannot cancel a scheduled change close to its effective date. If the change is within the processing window, this operation returns an error.</p> </note>

        Args:
            arn: <p>The ARN of the subscription whose pending change you want to cancel.</p>
            if_match: <p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This typically occurs when the <code>ETag</code> value in the <code>If-Match</code> header does not match the current version of the subscription. Retrieve the latest version and retry.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a pending subscription change

            >>> await client.cancel_subscription_change(arn='arn:aws:pricingplanmanager::123456789012:subscription/sub-1234567890', if_match='3')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.cancel_subscription_change_input.CancelSubscriptionChangeInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.cancel_subscription_change_output.CancelSubscriptionChangeOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.cancel_subscription_change

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.cancel_subscription_change.async_cancel_subscription_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.cancel_subscription_change_input.CancelSubscriptionChangeInput = {
            "arn": arn,
            "if_match": if_match,
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

    async def create_subscription(
        self,
        plan_family: str,
        plan_tier: str,
        resource_arns: "capo_pricing_plan_manager.types.resource_arns.ResourceArns",
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        usage_level: Optional[str] = None,
        approval_mode: Optional[
            "capo_pricing_plan_manager.types.approval_mode.ApprovalMode"
        ] = None,
        client_token: Optional[
            "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_pricing_plan_manager.types.create_subscription_output.CreateSubscriptionOutput":
        """<p>Creates a flat-rate pricing subscription for the specified resources.</p> <note> <p>When <code>approvalMode</code> is set to <code>MANUAL</code>, paid-tier subscriptions are created in <code>PENDING_APPROVAL</code> status and require a separate <code>ApprovePaidSubscription</code> call before billing starts. Free-tier subscriptions are always activated immediately regardless of approval mode.</p> <p>When <code>approvalMode</code> is set to <code>IMMEDIATE</code> or is not specified, the subscription is activated immediately.</p> </note>

        Args:
            plan_family: <p>The pricing plan family to subscribe to, such as <code>CloudFront</code>.</p>
            plan_tier: <p>The tier level for the subscription, such as <code>FREE</code>, <code>PRO</code>, <code>BUSINESS</code>, or <code>PREMIUM</code>.</p>
            usage_level: <p>The usage level within the plan tier. Specify <code>DEFAULT</code> for the base configuration, or a higher level if your plan tier supports it.</p>
            resource_arns: <p>The ARNs of the resources to include in the subscription. Specify one or more supported resources.</p> <note> <p>For subscriptions in the CloudFront plan family, the resources must include exactly one Amazon CloudFront distribution and exactly one WAF web ACL. You can also include other supported resources, such as Amazon Route 53 hosted zones and CloudFront KeyValueStores.</p> </note>
            approval_mode: <p>Determines whether the subscription requires explicit approval before billing starts. Set to <code>MANUAL</code> to require a separate <code>ApprovePaidSubscription</code> call, or <code>IMMEDIATE</code> to activate the subscription right away. For paid tier plans, this defaults to <code>MANUAL</code> if not specified. For the <code>FREE</code> plan tier, only <code>IMMEDIATE</code> is supported, and it is the default.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the request is handled only once. If you send the same request with the same client token, the API returns the original response without creating a duplicate subscription.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This typically occurs when the <code>ETag</code> value in the <code>If-Match</code> header does not match the current version of the subscription. Retrieve the latest version and retry.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service limit. You have reached the maximum number of subscriptions allowed for your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a flat-rate pricing subscription (deferred approval)

            >>> await client.create_subscription(plan_family='CloudFront', plan_tier='PRO', resource_arns=['arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE', 'arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4'], approval_mode='MANUAL')
            Create a subscription with approval mode

            >>> await client.create_subscription(plan_family='CloudFront', plan_tier='PRO', resource_arns=['arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE', 'arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4'], approval_mode='IMMEDIATE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.create_subscription_input.CreateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.create_subscription_output.CreateSubscriptionOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.create_subscription

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.create_subscription.async_create_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.create_subscription_input.CreateSubscriptionInput = {
            "plan_family": plan_family,
            "plan_tier": plan_tier,
            "resource_arns": resource_arns,
        }
        if usage_level is not None:
            input_["usage_level"] = usage_level
        if approval_mode is not None:
            input_["approval_mode"] = approval_mode
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

    async def disassociate_resources_from_subscription(
        self,
        arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn",
        resource_arns: "capo_pricing_plan_manager.types.resource_arns.ResourceArns",
        if_match: str,
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        client_token: Optional[
            "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_pricing_plan_manager.types.disassociate_resources_from_subscription_output.DisassociateResourcesFromSubscriptionOutput":
        """<p>Removes one or more resources from an existing subscription.</p> <note> <p>For subscriptions in the CloudFront plan family, the associated resources must always include exactly one Amazon CloudFront distribution and exactly one WAF web ACL. You cannot remove these required resources.</p> </note>

        Args:
            arn: <p>The ARN of the subscription to remove resources from.</p>
            resource_arns: <p>The ARNs of the resources to remove from the subscription. For subscriptions in the CloudFront plan family, you cannot remove the required CloudFront distribution or WAF web ACL.</p>
            if_match: <p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This typically occurs when the <code>ETag</code> value in the <code>If-Match</code> header does not match the current version of the subscription. Retrieve the latest version and retry.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove a resource from a subscription

            >>> await client.disassociate_resources_from_subscription(arn='arn:aws:pricingplanmanager::123456789012:subscription/sub-1234567890', resource_arns=['arn:aws:route53:::hostedzone/Z0123456789EXAMPLE'], if_match='2')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.disassociate_resources_from_subscription_input.DisassociateResourcesFromSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.disassociate_resources_from_subscription_output.DisassociateResourcesFromSubscriptionOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.disassociate_resources_from_subscription

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.disassociate_resources_from_subscription.async_disassociate_resources_from_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.disassociate_resources_from_subscription_input.DisassociateResourcesFromSubscriptionInput = {
            "arn": arn,
            "resource_arns": resource_arns,
            "if_match": if_match,
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

    async def get_subscription(
        self,
        arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn",
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
    ) -> (
        "capo_pricing_plan_manager.types.get_subscription_output.GetSubscriptionOutput"
    ):
        """<p>Returns the details of a flat-rate pricing subscription, including its current status, associated resources, and any pending scheduled changes.</p>

        Args:
            arn: <p>The ARN of the subscription to retrieve.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get subscription details

            >>> await client.get_subscription(arn='arn:aws:pricingplanmanager::123456789012:subscription/sub-1234567890')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.get_subscription_input.GetSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.get_subscription_output.GetSubscriptionOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.get_subscription

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.get_subscription.async_get_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.get_subscription_input.GetSubscriptionInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_pricing_plan_manager.types.list_subscriptions_output.ListSubscriptionsOutput":
        """<p>Returns a summary of all flat-rate pricing subscriptions in the calling account.</p>

        Args:
            next_token: <p>A token from a previous <code>ListSubscriptions</code> response. If the response included a <code>nextToken</code>, there are more results available. Pass this value to retrieve the next page of results.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all subscriptions

            >>> await client.list_subscriptions()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.list_subscriptions_input.ListSubscriptionsInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.list_subscriptions_output.ListSubscriptionsOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.list_subscriptions

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.list_subscriptions_input.ListSubscriptionsInput = {}
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
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_pricing_plan_manager.types.subscription_summary.SubscriptionSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subscription_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_subscription(
        self,
        arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn",
        plan_tier: str,
        if_match: str,
        *,
        config_overrides: Optional[AsyncPricingPlanManagerClientConfig] = None,
        usage_level: Optional[str] = None,
        client_token: Optional[
            "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_pricing_plan_manager.types.update_subscription_output.UpdateSubscriptionOutput":
        """<p>Changes the plan tier of an existing subscription.</p> <note> <p>Upgrades take effect immediately. Downgrades are scheduled and the current tier remains unchanged until the end of the billing cycle (calendar month). You cannot update a subscription while a scheduled change is pending. To make a new change, first cancel the pending change using <code>CancelSubscriptionChange</code>.</p> <p>This operation replaces the plan tier value. If you omit the optional <code>usageLevel</code> field, it is reset to the default.</p> </note>

        Args:
            arn: <p>The ARN of the subscription to update.</p>
            plan_tier: <p>The new tier level for the subscription.</p>
            usage_level: <p>The usage level within the plan tier. Specify <code>DEFAULT</code> for the base configuration. If omitted, the usage level is reset to the default.</p>
            if_match: <p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response. This ensures you are updating the expected version of the subscription.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>

        Raises:
            capo_pricing_plan_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.</p>
            capo_pricing_plan_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This typically occurs when the <code>ETag</code> value in the <code>If-Match</code> header does not match the current version of the subscription. Retrieve the latest version and retry.</p>
            capo_pricing_plan_manager.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred on the server. Retry the request.</p>
            capo_pricing_plan_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.</p>
            capo_pricing_plan_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service limit. You have reached the maximum number of subscriptions allowed for your account.</p>
            capo_pricing_plan_manager.errors.throttling_exception.ThrottlingException: <p>The request rate exceeds the allowed limit. Wait briefly and retry the request.</p>
            capo_pricing_plan_manager.errors.validation_exception.ValidationException: <p>The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.</p>
            capo_pricing_plan_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a subscription plan tier

            >>> await client.update_subscription(arn='arn:aws:pricingplanmanager::123456789012:subscription/sub-1234567890', plan_tier='BUSINESS', if_match='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pricing_plan_manager.types.update_subscription_input.UpdateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_pricing_plan_manager.types.update_subscription_output.UpdateSubscriptionOutput"
        ]:
            import capo_pricing_plan_manager._operations.aws_pricing_plan_manager.update_subscription

            (
                output,
                http_response,
            ) = await capo_pricing_plan_manager._operations.aws_pricing_plan_manager.update_subscription.async_update_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pricing_plan_manager.types.update_subscription_input.UpdateSubscriptionInput = {
            "arn": arn,
            "plan_tier": plan_tier,
            "if_match": if_match,
        }
        if usage_level is not None:
            input_["usage_level"] = usage_level
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

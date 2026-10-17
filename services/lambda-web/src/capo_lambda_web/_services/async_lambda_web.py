"""Generated from Smithy shape ``com.amazonaws.lambdaweb#LambdaWeb``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lambda_web._auth._signers
import capo_lambda_web._auth._sigv4
from capo_lambda_web._auth._identity import Credentials
from capo_lambda_web._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lambda_web._auth._zapros_handler import AuthMiddleware
from capo_lambda_web._pagination import resolve_path as _resolve_path
from capo_lambda_web._resources.lambda_web.web_function import AsyncWebFunction
from capo_lambda_web._services._aws_config import aaws_config
from capo_lambda_web._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    aretry,
)

if TYPE_CHECKING:
    import capo_lambda_web.types.auth_type
    import capo_lambda_web.types.auto_deployment_mode
    import capo_lambda_web.types.build_config
    import capo_lambda_web.types.create_web_function_endpoint_request
    import capo_lambda_web.types.create_web_function_endpoint_response
    import capo_lambda_web.types.create_web_function_request
    import capo_lambda_web.types.create_web_function_response
    import capo_lambda_web.types.create_web_function_revision_request
    import capo_lambda_web.types.create_web_function_revision_response
    import capo_lambda_web.types.delete_resource_policy_request
    import capo_lambda_web.types.delete_web_function_endpoint_request
    import capo_lambda_web.types.delete_web_function_request
    import capo_lambda_web.types.delete_web_function_revision_request
    import capo_lambda_web.types.description
    import capo_lambda_web.types.endpoint_config
    import capo_lambda_web.types.endpoint_name
    import capo_lambda_web.types.endpoint_type
    import capo_lambda_web.types.filter_list
    import capo_lambda_web.types.function_endpoint_summary
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.function_revision_summary
    import capo_lambda_web.types.function_summary
    import capo_lambda_web.types.get_resource_policy_request
    import capo_lambda_web.types.get_resource_policy_response
    import capo_lambda_web.types.get_web_account_settings_request
    import capo_lambda_web.types.get_web_account_settings_response
    import capo_lambda_web.types.get_web_function_endpoint_request
    import capo_lambda_web.types.get_web_function_endpoint_response
    import capo_lambda_web.types.get_web_function_request
    import capo_lambda_web.types.get_web_function_response
    import capo_lambda_web.types.get_web_function_revision_request
    import capo_lambda_web.types.get_web_function_revision_response
    import capo_lambda_web.types.kms_key_arn
    import capo_lambda_web.types.list_tags_request
    import capo_lambda_web.types.list_tags_response
    import capo_lambda_web.types.list_web_function_endpoints_request
    import capo_lambda_web.types.list_web_function_endpoints_response
    import capo_lambda_web.types.list_web_function_revisions_request
    import capo_lambda_web.types.list_web_function_revisions_response
    import capo_lambda_web.types.list_web_functions_request
    import capo_lambda_web.types.list_web_functions_response
    import capo_lambda_web.types.max_results
    import capo_lambda_web.types.next_token
    import capo_lambda_web.types.policy_revision_id
    import capo_lambda_web.types.put_resource_policy_request
    import capo_lambda_web.types.put_resource_policy_response
    import capo_lambda_web.types.region_list
    import capo_lambda_web.types.resource_arn
    import capo_lambda_web.types.resource_policy
    import capo_lambda_web.types.revision_config
    import capo_lambda_web.types.revision_id
    import capo_lambda_web.types.revision_weight_list
    import capo_lambda_web.types.scaling_config
    import capo_lambda_web.types.service_config
    import capo_lambda_web.types.tag_key_list
    import capo_lambda_web.types.tag_resource_request
    import capo_lambda_web.types.tags
    import capo_lambda_web.types.throttle_config
    import capo_lambda_web.types.untag_resource_request
    import capo_lambda_web.types.update_web_function_endpoint_request
    import capo_lambda_web.types.update_web_function_endpoint_response


class AsyncLambdaWebClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLambdaWebClient:
    """A client for the ``LambdaWeb`` service.

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
        client = AsyncClient(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
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
        self._config = AsyncLambdaWebClientConfig(
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

        # resources
        self.web_function = AsyncWebFunction(self)

    def operation_options(
        self,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLambdaWebClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
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

    async def delete_resource_policy(
        self,
        resource_arn: "capo_lambda_web.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        revision_id: Optional[
            "capo_lambda_web.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> None:
        """<p>Removes the resource-based policy from a web function.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the web function.</p>
            revision_id: <p>The revision ID of the policy. Use this to prevent deleting a policy that has been updated since you last retrieved it. If you don't specify a value, the policy is deleted regardless of its current revision.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteResourcePolicy")
        )
        input_: capo_lambda_web.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_lambda_web.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> "capo_lambda_web.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy attached to a web function.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the web function.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetResourcePolicy")
        )
        input_: capo_lambda_web.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_web_account_settings(
        self, *, config_overrides: Optional[AsyncLambdaWebClientConfig] = None
    ) -> "capo_lambda_web.types.get_web_account_settings_response.GetWebAccountSettingsResponse":
        """<p>Retrieves details about your AWS Lambda Web Functions account settings for the current AWS Region, including the quotas that apply to web functions and your current usage.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.get_web_account_settings_request.GetWebAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.get_web_account_settings_response.GetWebAccountSettingsResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.get_web_account_settings

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.get_web_account_settings.async_get_web_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetWebAccountSettings")
        )
        input_: capo_lambda_web.types.get_web_account_settings_request.GetWebAccountSettingsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags(
        self,
        resource: "capo_lambda_web.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> "capo_lambda_web.types.list_tags_response.ListTagsResponse":
        """<p>Returns a list of tags applied to a web function.</p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) of the web function.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.list_tags_response.ListTagsResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.list_tags

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListTags")
        )
        input_: capo_lambda_web.types.list_tags_request.ListTagsRequest = {
            "resource": resource
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_lambda_web.types.resource_arn.ResourceArn",
        policy: "capo_lambda_web.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        revision_id: Optional[
            "capo_lambda_web.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_lambda_web.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Adds or updates a resource-based policy on a web function. A resource-based policy grants permissions to other AWS accounts or services to perform actions on the web function.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the web function.</p>
            policy: <p>The JSON-formatted resource-based policy to attach to the web function.</p>
            revision_id: <p>The revision ID of the existing policy. Use this to prevent conflicts when updating a policy concurrently. If you don't specify a value, the update proceeds without checking the current revision.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("PutResourcePolicy")
        )
        input_: capo_lambda_web.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource: "capo_lambda_web.types.resource_arn.ResourceArn",
        tags: "capo_lambda_web.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> None:
        """<p>Adds tags to a web function. If a tag key already exists, the existing value is overwritten with the new value.</p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) of the web function.</p>
            tags: <p>A map of tag keys and values to add to the web function.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.tag_resource

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_lambda_web.types.tag_resource_request.TagResourceRequest = {
            "resource": resource,
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
        resource: "capo_lambda_web.types.resource_arn.ResourceArn",
        tag_keys: "capo_lambda_web.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> None:
        """<p>Removes tags from a web function.</p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) of the web function.</p>
            tag_keys: <p>A list of tag keys to remove from the web function.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.untag_resource

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_lambda_web.types.untag_resource_request.UntagResourceRequest = {
            "resource": resource,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_web_function(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        revision_config: Optional[
            "capo_lambda_web.types.revision_config.RevisionConfig"
        ] = None,
        endpoint_config: Optional[
            "capo_lambda_web.types.endpoint_config.EndpointConfig"
        ] = None,
        tags: Optional["capo_lambda_web.types.tags.Tags"] = None,
    ) -> "capo_lambda_web.types.create_web_function_response.CreateWebFunctionResponse":
        """<p>Creates a web function with an initial revision and endpoint. To create a web function, you provide the function name, revision configuration (code and service settings), and endpoint configuration.</p> <p>To use this operation, you must have the <code>CreateWebFunction</code> permission on the web function. You don't need separate permissions for the initial revision or endpoint.</p>

        Args:
            function_name: <p>The name of the web function. The name can contain letters, numbers, hyphens (-), and underscores (_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.</p>
            revision_config: <p>The configuration for the initial revision of the web function, including code and service settings.</p>
            endpoint_config: <p>The configuration for the initial endpoint of the web function.</p>
            tags: <p>A map of tag keys and values to apply to the web function.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.create_web_function_response.CreateWebFunctionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.create_web_function

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.create_web_function.async_create_web_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest",
        ) -> dict[str, Any]:
            import capo_lambda_web.types.create_web_function_request

            return capo_lambda_web.types.create_web_function_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateWebFunction", redact_input=_redact_input),
        )
        input_: capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest = {
            "function_name": function_name
        }
        if revision_config is not None:
            input_["revision_config"] = revision_config
        if endpoint_config is not None:
            input_["endpoint_config"] = endpoint_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_web_function(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> "capo_lambda_web.types.get_web_function_response.GetWebFunctionResponse":
        """<p>Retrieves details about a web function, including its current state and configuration.</p>

        Args:
            function_name: <p>The web function to retrieve.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.get_web_function_request.GetWebFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.get_web_function_response.GetWebFunctionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.get_web_function

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.get_web_function.async_get_web_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetWebFunction")
        )
        input_: capo_lambda_web.types.get_web_function_request.GetWebFunctionRequest = {
            "function_name": function_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_web_function(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> None:
        """<p>Deletes a web function and all of its associated revisions and endpoints.</p> <p>To use this operation, you must have the <code>DeleteWebFunction</code> permission on the web function. You don't need the <code>DeleteWebFunctionRevision</code> or <code>DeleteWebFunctionEndpoint</code> permission.</p>

        Args:
            function_name: <p>The web function to delete.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.delete_web_function_request.DeleteWebFunctionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.delete_web_function

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.delete_web_function.async_delete_web_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteWebFunction")
        )
        input_: capo_lambda_web.types.delete_web_function_request.DeleteWebFunctionRequest = {
            "function_name": function_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_web_functions(
        self,
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "capo_lambda_web.types.list_web_functions_response.ListWebFunctionsResponse":
        """<p>Lists web functions in your account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            filters: <p>A list of filters to apply to the results. The only supported filter name is <code>state</code>. If you don't specify a filter, the operation returns all web functions.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.</p>
            next_token: <p>The pagination token that's returned by a previous request to retrieve the next page of results.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.list_web_functions_request.ListWebFunctionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.list_web_functions_response.ListWebFunctionsResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.list_web_functions

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.list_web_functions.async_list_web_functions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListWebFunctions")
        )
        input_: capo_lambda_web.types.list_web_functions_request.ListWebFunctionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_web_functions(
        self,
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lambda_web.types.function_summary.FunctionSummary]":
        _token = next_token
        while True:
            _response = await self.list_web_functions(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("functions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_web_function_endpoint(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        endpoint_name: "capo_lambda_web.types.endpoint_name.EndpointName",
        endpoint_type: "capo_lambda_web.types.endpoint_type.EndpointType",
        auth_type: "capo_lambda_web.types.auth_type.AuthType",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        description: Optional["capo_lambda_web.types.description.Description"] = None,
        auto_deployment_mode: Optional[
            "capo_lambda_web.types.auto_deployment_mode.AutoDeploymentMode"
        ] = None,
        revision_weights: Optional[
            "capo_lambda_web.types.revision_weight_list.RevisionWeightList"
        ] = None,
        regions: Optional["capo_lambda_web.types.region_list.RegionList"] = None,
        scaling_config: Optional[
            "capo_lambda_web.types.scaling_config.ScalingConfig"
        ] = None,
        throttle_config: Optional[
            "capo_lambda_web.types.throttle_config.ThrottleConfig"
        ] = None,
    ) -> "capo_lambda_web.types.create_web_function_endpoint_response.CreateWebFunctionEndpointResponse":
        """<p>Creates an endpoint for a web function. An endpoint exposes the web function over HTTPS and routes traffic to one or more revisions.</p> <p>To use this operation, you must have the <code>CreateWebFunctionEndpoint</code> permission on the web function, not on the endpoint being created.</p>

        Args:
            function_name: <p>The web function to create the endpoint for.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            endpoint_name: <p>The name of the endpoint to create. The name can contain letters, numbers, hyphens (-), and underscores (_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.</p>
            description: <p>A description of the endpoint.</p>
            endpoint_type: <p>The type of endpoint to create. Determines how traffic is served and routed across Regions.</p> <p>Valid values:</p> <ul> <li> <p> <code>HomeRegion</code> – Serves traffic from the Region where you created the web function.</p> </li> <li> <p> <code>MultiRegion</code> – Replicates across the Regions that you choose and routes each request to the nearest one.</p> </li> <li> <p> <code>PerRegion</code> – Creates a separate endpoint in each Region that you choose.</p> </li> </ul>
            auth_type: <p>The authorization type for the endpoint.</p> <p>Valid values:</p> <ul> <li> <p> <code>ApplicationManaged</code> – Your application handles authorization.</p> </li> <li> <p> <code>IamAuth</code> – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).</p> </li> </ul>
            auto_deployment_mode: <p>The auto-deployment mode for the endpoint. Controls whether the endpoint automatically serves the newest revision. If you don't specify a value, the default is <code>Disabled</code>, and this default is returned in the response.</p> <p>Valid values:</p> <ul> <li> <p> <code>LatestRevision</code> – The endpoint automatically serves the newest revision.</p> </li> <li> <p> <code>Disabled</code> – Revision routing stays fixed until you change it.</p> </li> </ul>
            revision_weights: <p>A list of revision weights that determine how traffic is distributed across revisions. You can specify up to two revisions for canary or blue-green deployments.</p>
            regions: <p>The list of Regions for the endpoint. Required when the endpoint type is <code>MultiRegion</code> or <code>PerRegion</code>: specify at least one Region other than the Region where you create the endpoint (the home Region). The home Region is added automatically if you don't include it; specifying only the home Region isn't allowed. When the endpoint type is <code>HomeRegion</code>, omit this field or specify only the home Region.</p>
            scaling_config: <p>The scaling configuration for the endpoint. There is no default value. If you don't specify a scaling configuration, it is absent from the response.</p>
            throttle_config: <p>The throttling configuration for the endpoint. There is no default value. If you don't specify a throttling configuration, it is absent from the response.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.create_web_function_endpoint_request.CreateWebFunctionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.create_web_function_endpoint_response.CreateWebFunctionEndpointResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.create_web_function_endpoint

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.create_web_function_endpoint.async_create_web_function_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateWebFunctionEndpoint")
        )
        input_: capo_lambda_web.types.create_web_function_endpoint_request.CreateWebFunctionEndpointRequest = {
            "function_name": function_name,
            "endpoint_name": endpoint_name,
            "endpoint_type": endpoint_type,
            "auth_type": auth_type,
        }
        if description is not None:
            input_["description"] = description
        if auto_deployment_mode is not None:
            input_["auto_deployment_mode"] = auto_deployment_mode
        if revision_weights is not None:
            input_["revision_weights"] = revision_weights
        if regions is not None:
            input_["regions"] = regions
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if throttle_config is not None:
            input_["throttle_config"] = throttle_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_web_function_endpoint(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        endpoint_name: "capo_lambda_web.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> "capo_lambda_web.types.get_web_function_endpoint_response.GetWebFunctionEndpointResponse":
        """<p>Retrieves details about a web function endpoint, including its current state, configuration, and domain name.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            endpoint_name: <p>The endpoint to retrieve.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The endpoint name, for example <code>my-endpoint</code>.</p> </li> <li> <p>The endpoint ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the endpoint name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.get_web_function_endpoint_request.GetWebFunctionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.get_web_function_endpoint_response.GetWebFunctionEndpointResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.get_web_function_endpoint

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.get_web_function_endpoint.async_get_web_function_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetWebFunctionEndpoint")
        )
        input_: capo_lambda_web.types.get_web_function_endpoint_request.GetWebFunctionEndpointRequest = {
            "function_name": function_name,
            "endpoint_name": endpoint_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_web_function_endpoint(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        endpoint_name: "capo_lambda_web.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        description: Optional["capo_lambda_web.types.description.Description"] = None,
        auth_type: Optional["capo_lambda_web.types.auth_type.AuthType"] = None,
        auto_deployment_mode: Optional[
            "capo_lambda_web.types.auto_deployment_mode.AutoDeploymentMode"
        ] = None,
        revision_weights: Optional[
            "capo_lambda_web.types.revision_weight_list.RevisionWeightList"
        ] = None,
        scaling_config: Optional[
            "capo_lambda_web.types.scaling_config.ScalingConfig"
        ] = None,
        throttle_config: Optional[
            "capo_lambda_web.types.throttle_config.ThrottleConfig"
        ] = None,
    ) -> "capo_lambda_web.types.update_web_function_endpoint_response.UpdateWebFunctionEndpointResponse":
        """<p>Updates the configuration of a web function endpoint. You can modify the authorization type, auto-deployment mode, revision weights, scaling, and throttling settings.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            endpoint_name: <p>The endpoint to update.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The endpoint name, for example <code>my-endpoint</code>.</p> </li> <li> <p>The endpoint ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the endpoint name, it is limited to 64 characters in length.</p>
            description: <p>A description of the endpoint. Omit this field to keep the current description.</p>
            auth_type: <p>The authorization type for the endpoint. Omit this field to keep the current authorization type.</p> <p>Valid values:</p> <ul> <li> <p> <code>ApplicationManaged</code> – Your application handles authorization.</p> </li> <li> <p> <code>IamAuth</code> – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).</p> </li> </ul>
            auto_deployment_mode: <p>The auto-deployment mode for the endpoint. Omit this field to keep the current auto-deployment mode.</p> <p>Valid values:</p> <ul> <li> <p> <code>LatestRevision</code> – The endpoint automatically serves the newest revision.</p> </li> <li> <p> <code>Disabled</code> – Revision routing stays fixed until you change it.</p> </li> </ul>
            revision_weights: <p>A list of revision weights that determine how traffic is distributed across revisions.</p>
            scaling_config: <p>The scaling configuration for the endpoint. Omit this field to keep the current scaling configuration. To clear a previously set <code>maxEnvironments</code> value, specify an empty object.</p>
            throttle_config: <p>The throttling configuration for the endpoint. Omit this field to keep the current throttling configuration. To clear a previously set <code>rateLimit</code> value, specify an empty object.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.update_web_function_endpoint_request.UpdateWebFunctionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.update_web_function_endpoint_response.UpdateWebFunctionEndpointResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.update_web_function_endpoint

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.update_web_function_endpoint.async_update_web_function_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateWebFunctionEndpoint")
        )
        input_: capo_lambda_web.types.update_web_function_endpoint_request.UpdateWebFunctionEndpointRequest = {
            "function_name": function_name,
            "endpoint_name": endpoint_name,
        }
        if description is not None:
            input_["description"] = description
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if auto_deployment_mode is not None:
            input_["auto_deployment_mode"] = auto_deployment_mode
        if revision_weights is not None:
            input_["revision_weights"] = revision_weights
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if throttle_config is not None:
            input_["throttle_config"] = throttle_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_web_function_endpoint(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        endpoint_name: "capo_lambda_web.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> None:
        """<p>Deletes a web function endpoint.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            endpoint_name: <p>The endpoint to delete.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The endpoint name, for example <code>my-endpoint</code>.</p> </li> <li> <p>The endpoint ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the endpoint name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.delete_web_function_endpoint_request.DeleteWebFunctionEndpointRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.delete_web_function_endpoint

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.delete_web_function_endpoint.async_delete_web_function_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteWebFunctionEndpoint")
        )
        input_: capo_lambda_web.types.delete_web_function_endpoint_request.DeleteWebFunctionEndpointRequest = {
            "function_name": function_name,
            "endpoint_name": endpoint_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_web_function_endpoints(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "capo_lambda_web.types.list_web_function_endpoints_response.ListWebFunctionEndpointsResponse":
        """<p>Lists endpoints for a web function. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            filters: <p>A list of filters to apply to the results. Supported filter names: <code>authType</code>, <code>autoDeploymentMode</code>, <code>endpointType</code>, <code>state</code>, and <code>updateStatus</code>. If you don't specify a filter, the operation returns all endpoints for the web function.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.</p>
            next_token: <p>The pagination token that's returned by a previous request to retrieve the next page of results.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.list_web_function_endpoints_request.ListWebFunctionEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.list_web_function_endpoints_response.ListWebFunctionEndpointsResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.list_web_function_endpoints

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.list_web_function_endpoints.async_list_web_function_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListWebFunctionEndpoints")
        )
        input_: capo_lambda_web.types.list_web_function_endpoints_request.ListWebFunctionEndpointsRequest = {
            "function_name": function_name
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_web_function_endpoints(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lambda_web.types.function_endpoint_summary.FunctionEndpointSummary]":
        _token = next_token
        while True:
            _response = await self.list_web_function_endpoints(
                function_name,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_web_function_revision(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        build_config: "capo_lambda_web.types.build_config.BuildConfig",
        service_config: "capo_lambda_web.types.service_config.ServiceConfig",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        description: Optional["capo_lambda_web.types.description.Description"] = None,
        kms_key_arn: Optional["capo_lambda_web.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_lambda_web.types.create_web_function_revision_response.CreateWebFunctionRevisionResponse":
        """<p>Creates an immutable revision for a web function. A revision represents a specific version of the function code and configuration.</p> <p>To use this operation, you must have the <code>CreateWebFunctionRevision</code> permission on the web function, not on the revision being created.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            description: <p>A description of the revision.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used to encrypt the revision's code and environment variables.</p>
            build_config: <p>The build configuration for the revision, including code location and runtime settings.</p>
            service_config: <p>The service configuration for the revision, including execution role, timeout, and concurrency settings.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.create_web_function_revision_request.CreateWebFunctionRevisionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.create_web_function_revision_response.CreateWebFunctionRevisionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.create_web_function_revision

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.create_web_function_revision.async_create_web_function_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_lambda_web.types.create_web_function_revision_request.CreateWebFunctionRevisionRequest",
        ) -> dict[str, Any]:
            import capo_lambda_web.types.create_web_function_revision_request

            return capo_lambda_web.types.create_web_function_revision_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_lambda_web.types.create_web_function_revision_response.CreateWebFunctionRevisionResponse",
        ) -> dict[str, Any]:
            import capo_lambda_web.types.create_web_function_revision_response

            return capo_lambda_web.types.create_web_function_revision_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "CreateWebFunctionRevision",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_lambda_web.types.create_web_function_revision_request.CreateWebFunctionRevisionRequest = {
            "function_name": function_name,
            "build_config": build_config,
            "service_config": service_config,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_web_function_revision(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        revision_id: "capo_lambda_web.types.revision_id.RevisionId",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> "capo_lambda_web.types.get_web_function_revision_response.GetWebFunctionRevisionResponse":
        """<p>Retrieves details about a web function revision, including its state and configuration.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            revision_id: <p>The revision to retrieve.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The revision identifier.</p> </li> <li> <p>The revision ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.get_web_function_revision_request.GetWebFunctionRevisionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.get_web_function_revision_response.GetWebFunctionRevisionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.get_web_function_revision

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.get_web_function_revision.async_get_web_function_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_lambda_web.types.get_web_function_revision_response.GetWebFunctionRevisionResponse",
        ) -> dict[str, Any]:
            import capo_lambda_web.types.get_web_function_revision_response

            return capo_lambda_web.types.get_web_function_revision_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetWebFunctionRevision", redact_output=_redact_output),
        )
        input_: capo_lambda_web.types.get_web_function_revision_request.GetWebFunctionRevisionRequest = {
            "function_name": function_name,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_web_function_revision(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        revision_id: "capo_lambda_web.types.revision_id.RevisionId",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> None:
        """<p>Deletes a web function revision. You cannot delete a revision that is currently serving traffic on an endpoint.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            revision_id: <p>The revision to delete.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The revision identifier.</p> </li> <li> <p>The revision ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.delete_web_function_revision_request.DeleteWebFunctionRevisionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.delete_web_function_revision

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.delete_web_function_revision.async_delete_web_function_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteWebFunctionRevision")
        )
        input_: capo_lambda_web.types.delete_web_function_revision_request.DeleteWebFunctionRevisionRequest = {
            "function_name": function_name,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_web_function_revisions(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "capo_lambda_web.types.list_web_function_revisions_response.ListWebFunctionRevisionsResponse":
        """<p>Lists revisions for a web function. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            function_name: <p>The web function.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            filters: <p>A list of filters to apply to the results. The only supported filter name is <code>state</code>. If you don't specify a filter, the operation returns all revisions for the web function.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.</p>
            next_token: <p>The pagination token that's returned by a previous request to retrieve the next page of results.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.list_web_function_revisions_request.ListWebFunctionRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.list_web_function_revisions_response.ListWebFunctionRevisionsResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.list_web_function_revisions

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.list_web_function_revisions.async_list_web_function_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListWebFunctionRevisions")
        )
        input_: capo_lambda_web.types.list_web_function_revisions_request.ListWebFunctionRevisionsRequest = {
            "function_name": function_name
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_web_function_revisions(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lambda_web.types.function_revision_summary.FunctionRevisionSummary]":
        _token = next_token
        while True:
            _response = await self.list_web_function_revisions(
                function_name,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("revisions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

"""Generated from Smithy shape ``com.amazonaws.mpa#AWSFluffyCoreService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_mpa._auth._signers
import capo_mpa._auth._sigv4
from capo_mpa._auth._identity import Credentials
from capo_mpa._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mpa._auth._zapros_handler import AuthMiddleware
from capo_mpa._pagination import resolve_path as _resolve_path
from capo_mpa._resources.aws_fluffy_core_service.approval_team import AsyncApprovalTeam
from capo_mpa._resources.aws_fluffy_core_service.identity_source import (
    AsyncIdentitySource,
)
from capo_mpa._resources.aws_fluffy_core_service.session import AsyncSession
from capo_mpa._services._aws_config import aaws_config
from capo_mpa._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_mpa.types.approval_strategy
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.approval_team_name
    import capo_mpa.types.approval_team_request_approvers
    import capo_mpa.types.cancel_session_request
    import capo_mpa.types.cancel_session_response
    import capo_mpa.types.create_approval_team_request
    import capo_mpa.types.create_approval_team_response
    import capo_mpa.types.create_identity_source_request
    import capo_mpa.types.create_identity_source_response
    import capo_mpa.types.delete_identity_source_request
    import capo_mpa.types.delete_inactive_approval_team_version_request
    import capo_mpa.types.delete_inactive_approval_team_version_response
    import capo_mpa.types.description
    import capo_mpa.types.filters
    import capo_mpa.types.get_approval_team_request
    import capo_mpa.types.get_approval_team_response
    import capo_mpa.types.get_identity_source_request
    import capo_mpa.types.get_identity_source_response
    import capo_mpa.types.get_policy_version_request
    import capo_mpa.types.get_policy_version_response
    import capo_mpa.types.get_resource_policy_request
    import capo_mpa.types.get_resource_policy_response
    import capo_mpa.types.get_session_request
    import capo_mpa.types.get_session_response
    import capo_mpa.types.identity_source_for_list
    import capo_mpa.types.identity_source_parameters
    import capo_mpa.types.list_approval_teams_request
    import capo_mpa.types.list_approval_teams_response
    import capo_mpa.types.list_approval_teams_response_approval_team
    import capo_mpa.types.list_identity_sources_request
    import capo_mpa.types.list_identity_sources_response
    import capo_mpa.types.list_policies_request
    import capo_mpa.types.list_policies_response
    import capo_mpa.types.list_policy_versions_request
    import capo_mpa.types.list_policy_versions_response
    import capo_mpa.types.list_resource_policies_request
    import capo_mpa.types.list_resource_policies_response
    import capo_mpa.types.list_resource_policies_response_resource_policy
    import capo_mpa.types.list_sessions_request
    import capo_mpa.types.list_sessions_response
    import capo_mpa.types.list_sessions_response_session
    import capo_mpa.types.list_tags_for_resource_request
    import capo_mpa.types.list_tags_for_resource_response
    import capo_mpa.types.max_results
    import capo_mpa.types.policies_references
    import capo_mpa.types.policy
    import capo_mpa.types.policy_type
    import capo_mpa.types.policy_version_summary
    import capo_mpa.types.qualified_policy_arn
    import capo_mpa.types.session_arn
    import capo_mpa.types.start_active_approval_team_deletion_request
    import capo_mpa.types.start_active_approval_team_deletion_response
    import capo_mpa.types.start_approval_team_baseline_approver_ids
    import capo_mpa.types.start_approval_team_baseline_request
    import capo_mpa.types.start_approval_team_baseline_response
    import capo_mpa.types.string
    import capo_mpa.types.tag_key_list
    import capo_mpa.types.tag_resource_request
    import capo_mpa.types.tag_resource_response
    import capo_mpa.types.tags
    import capo_mpa.types.token
    import capo_mpa.types.unqualified_policy_arn
    import capo_mpa.types.untag_resource_request
    import capo_mpa.types.untag_resource_response
    import capo_mpa.types.update_actions
    import capo_mpa.types.update_approval_team_request
    import capo_mpa.types.update_approval_team_response


class AsyncMPAClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMPAClient:
    """A client for the ``MPA`` service.

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
        self._config = AsyncMPAClientConfig(
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
        self.approval_team = AsyncApprovalTeam(self)
        self.identity_source = AsyncIdentitySource(self)
        self.session = AsyncSession(self)

    def operation_options(
        self, config_overrides: Optional[AsyncMPAClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMPAClientConfig = config_overrides or {}
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

    async def get_policy_version(
        self,
        policy_version_arn: "capo_mpa.types.qualified_policy_arn.QualifiedPolicyArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.get_policy_version_response.GetPolicyVersionResponse":
        """<p>Returns details for the version of a policy. Policies define the permissions for team resources.</p>

        Args:
            policy_version_arn: <p>Amazon Resource Name (ARN) for the policy.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.get_policy_version_request.GetPolicyVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.get_policy_version_response.GetPolicyVersionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_policy_version

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.get_policy_version.async_get_policy_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.get_policy_version_request.GetPolicyVersionRequest = {
            "policy_version_arn": policy_version_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_mpa.types.string.String",
        policy_name: "capo_mpa.types.string.String",
        policy_type: "capo_mpa.types.policy_type.PolicyType",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns details about a policy for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>
            policy_name: <p>Name of the policy.</p>
            policy_type: <p>The type of policy.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.invalid_parameter_exception.InvalidParameterException: <p>The request contains an invalid parameter value.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy_name": policy_name,
            "policy_type": policy_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_policies(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_policies_response.ListPoliciesResponse":
        """<p>Returns a list of policies. Policies define the permissions for team resources.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_policies_request.ListPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_policies_response.ListPoliciesResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_policies

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_policies.async_list_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_policies_request.ListPoliciesRequest = {}
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

    async def iter_list_policies(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_mpa.types.policy.Policy]":
        _token = next_token
        while True:
            _response = await self.list_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_policy_versions(
        self,
        policy_arn: "capo_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_policy_versions_response.ListPolicyVersionsResponse":
        """<p>Returns a list of the versions for policies. Policies define the permissions for team resources.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            policy_arn: <p>Amazon Resource Name (ARN) for the policy.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_policy_versions_request.ListPolicyVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_policy_versions_response.ListPolicyVersionsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_policy_versions

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_policy_versions.async_list_policy_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_policy_versions_request.ListPolicyVersionsRequest = {
            "policy_arn": policy_arn
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

    async def iter_list_policy_versions(
        self,
        policy_arn: "capo_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_mpa.types.policy_version_summary.PolicyVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_policy_versions(
                policy_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("policy_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_policies(
        self,
        resource_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_resource_policies_response.ListResourcePoliciesResponse":
        """<p>Returns a list of policies for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_resource_policies_request.ListResourcePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_resource_policies_response.ListResourcePoliciesResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_resource_policies

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_resource_policies.async_list_resource_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_resource_policies_request.ListResourcePoliciesRequest = {
            "resource_arn": resource_arn
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

    async def iter_list_resource_policies(
        self,
        resource_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_mpa.types.list_resource_policies_response_resource_policy.ListResourcePoliciesResponseResourcePolicy]":
        _token = next_token
        while True:
            _response = await self.list_resource_policies(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of the tags for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_mpa.types.string.String",
        tags: "capo_mpa.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.tag_resource_response.TagResourceResponse":
        """<p>Creates or updates a resource tag. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource you want to tag.</p>
            tags: <p>Tags that you have added to the specified resource.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeds the maximum number of tags allowed for this resource. Remove some tags, and try again.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_mpa.types.string.String",
        tag_keys: "capo_mpa.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a resource tag. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. </p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource you want to untag.</p>
            tag_keys: <p>Array of tag key-value pairs that you want to untag.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_approval_team(
        self,
        approval_strategy: "capo_mpa.types.approval_strategy.ApprovalStrategy",
        approvers: "capo_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers",
        description: "capo_mpa.types.description.Description",
        policies: "capo_mpa.types.policies_references.PoliciesReferences",
        name: "capo_mpa.types.approval_team_name.ApprovalTeamName",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        client_token: Optional["capo_mpa.types.token.Token"] = None,
        tags: Optional["capo_mpa.types.tags.Tags"] = None,
    ) -> "capo_mpa.types.create_approval_team_response.CreateApprovalTeamResponse":
        """<p>Creates a new approval team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Approval team</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>
            approval_strategy: <p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>
            approvers: <p>An array of <code>ApprovalTeamRequesterApprovers</code> objects. Contains details for the approvers in the team.</p>
            description: <p>Description for the team.</p>
            policies: <p>An array of <code>PolicyReference</code> objects. Contains a list of policies that define the permissions for team resources.</p>
            name: <p>Name of the team.</p>
            tags: <p>Tags you want to attach to the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for your account. Request a quota increase or reduce your request size.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.create_approval_team_request.CreateApprovalTeamRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.create_approval_team_response.CreateApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.create_approval_team

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.create_approval_team.async_create_approval_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.create_approval_team_request.CreateApprovalTeamRequest = {
            "approval_strategy": approval_strategy,
            "approvers": approvers,
            "description": description,
            "policies": policies,
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

    async def get_approval_team(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.get_approval_team_response.GetApprovalTeamResponse":
        """<p>Returns details for an approval team.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.get_approval_team_request.GetApprovalTeamRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.get_approval_team_response.GetApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_approval_team

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.get_approval_team.async_get_approval_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.get_approval_team_request.GetApprovalTeamRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_approval_team(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        approval_strategy: Optional[
            "capo_mpa.types.approval_strategy.ApprovalStrategy"
        ] = None,
        approvers: Optional[
            "capo_mpa.types.approval_team_request_approvers.ApprovalTeamRequestApprovers"
        ] = None,
        description: Optional["capo_mpa.types.description.Description"] = None,
        update_actions: Optional["capo_mpa.types.update_actions.UpdateActions"] = None,
    ) -> "capo_mpa.types.update_approval_team_response.UpdateApprovalTeamResponse":
        """<p>Updates an approval team. You can request to update the team description, approval threshold, and approvers in the team.</p> <note> <p> <b>Updates require team approval</b> </p> <p>Updates to an active team must be approved by the team.</p> </note>

        Args:
            approval_strategy: <p>An <code>ApprovalStrategy</code> object. Contains details for how the team grants approval.</p>
            approvers: <p>An array of <code>ApprovalTeamRequestApprover</code> objects. Contains details for the approvers in the team.</p>
            description: <p>Description for the team.</p>
            arn: <p>Amazon Resource Name (ARN) for the team.</p>
            update_actions: <p>A list of <code>UpdateAction</code> to perform when updating the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for your account. Request a quota increase or reduce your request size.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.update_approval_team_request.UpdateApprovalTeamRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.update_approval_team_response.UpdateApprovalTeamResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.update_approval_team

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.update_approval_team.async_update_approval_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.update_approval_team_request.UpdateApprovalTeamRequest = {
            "arn": arn
        }
        if approval_strategy is not None:
            input_["approval_strategy"] = approval_strategy
        if approvers is not None:
            input_["approvers"] = approvers
        if description is not None:
            input_["description"] = description
        if update_actions is not None:
            input_["update_actions"] = update_actions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_inactive_approval_team_version(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        version_id: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.delete_inactive_approval_team_version_response.DeleteInactiveApprovalTeamVersionResponse":
        """<p>Deletes an inactive approval team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html">Team health</a> in the <i>Multi-party approval User Guide</i>.</p> <p>You can also use this operation to delete a team draft. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/update-team.html#update-team-draft-status">Interacting with drafts</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            arn: <p>Amaazon Resource Name (ARN) for the team.</p>
            version_id: <p>Version ID for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.delete_inactive_approval_team_version_request.DeleteInactiveApprovalTeamVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.delete_inactive_approval_team_version_response.DeleteInactiveApprovalTeamVersionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.delete_inactive_approval_team_version

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.delete_inactive_approval_team_version.async_delete_inactive_approval_team_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.delete_inactive_approval_team_version_request.DeleteInactiveApprovalTeamVersionRequest = {
            "arn": arn,
            "version_id": version_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_approval_teams(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_approval_teams_response.ListApprovalTeamsResponse":
        """<p>Returns a list of approval teams.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_approval_teams_request.ListApprovalTeamsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_approval_teams_response.ListApprovalTeamsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_approval_teams

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_approval_teams.async_list_approval_teams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_approval_teams_request.ListApprovalTeamsRequest = {}
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

    async def iter_list_approval_teams(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_mpa.types.list_approval_teams_response_approval_team.ListApprovalTeamsResponseApprovalTeam]":
        _token = next_token
        while True:
            _response = await self.list_approval_teams(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("approval_teams",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_active_approval_team_deletion(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        pending_window_days: Optional[int] = None,
    ) -> "capo_mpa.types.start_active_approval_team_deletion_response.StartActiveApprovalTeamDeletionResponse":
        """<p>Starts the deletion process for an active approval team.</p> <note> <p> <b>Deletions require team approval</b> </p> <p>Requests to delete an active team must be approved by the team.</p> </note>

        Args:
            pending_window_days: <p>Number of days between when the team approves the delete request and when the team is deleted.</p>
            arn: <p>Amazon Resource Name (ARN) for the team.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.start_active_approval_team_deletion_request.StartActiveApprovalTeamDeletionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.start_active_approval_team_deletion_response.StartActiveApprovalTeamDeletionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.start_active_approval_team_deletion

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.start_active_approval_team_deletion.async_start_active_approval_team_deletion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.start_active_approval_team_deletion_request.StartActiveApprovalTeamDeletionRequest = {
            "arn": arn
        }
        if pending_window_days is not None:
            input_["pending_window_days"] = pending_window_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_approval_team_baseline(
        self,
        arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        approver_ids: Optional[
            "capo_mpa.types.start_approval_team_baseline_approver_ids.StartApprovalTeamBaselineApproverIds"
        ] = None,
    ) -> "capo_mpa.types.start_approval_team_baseline_response.StartApprovalTeamBaselineResponse":
        """<p>Starts a baseline session for specified approvers on an <code>ACTIVE</code> approval team.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            approver_ids: <p>Array of approver IDs.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.start_approval_team_baseline_request.StartApprovalTeamBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.start_approval_team_baseline_response.StartApprovalTeamBaselineResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.start_approval_team_baseline

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.start_approval_team_baseline.async_start_approval_team_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.start_approval_team_baseline_request.StartApprovalTeamBaselineRequest = {
            "arn": arn
        }
        if approver_ids is not None:
            input_["approver_ids"] = approver_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_identity_source(
        self,
        identity_source_parameters: "capo_mpa.types.identity_source_parameters.IdentitySourceParameters",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        client_token: Optional["capo_mpa.types.token.Token"] = None,
        tags: Optional["capo_mpa.types.tags.Tags"] = None,
    ) -> "capo_mpa.types.create_identity_source_response.CreateIdentitySourceResponse":
        """<p>Creates a new identity source. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_parameters: <p>A <code> IdentitySourceParameters</code> object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>
            tags: <p>Tag you want to attach to the identity source.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for your account. Request a quota increase or reduce your request size.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.create_identity_source_request.CreateIdentitySourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.create_identity_source_response.CreateIdentitySourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.create_identity_source

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.create_identity_source.async_create_identity_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.create_identity_source_request.CreateIdentitySourceRequest = {
            "identity_source_parameters": identity_source_parameters
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

    async def get_identity_source(
        self,
        identity_source_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.get_identity_source_response.GetIdentitySourceResponse":
        """<p>Returns details for an identity source. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_arn: <p>Amazon Resource Name (ARN) for the identity source.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.get_identity_source_request.GetIdentitySourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.get_identity_source_response.GetIdentitySourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_identity_source

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.get_identity_source.async_get_identity_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.get_identity_source_request.GetIdentitySourceRequest = {
            "identity_source_arn": identity_source_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_identity_source(
        self,
        identity_source_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> None:
        """<p>Deletes an identity source. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_arn: <p>Amazon Resource Name (ARN) for identity source.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.delete_identity_source_request.DeleteIdentitySourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_mpa._operations.aws_fluffy_core_service.delete_identity_source

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.delete_identity_source.async_delete_identity_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.delete_identity_source_request.DeleteIdentitySourceRequest = {
            "identity_source_arn": identity_source_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_identity_sources(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_identity_sources_response.ListIdentitySourcesResponse":
        """<p>Returns a list of identity sources. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_identity_sources_request.ListIdentitySourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_identity_sources_response.ListIdentitySourcesResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_identity_sources

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_identity_sources.async_list_identity_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_identity_sources_request.ListIdentitySourcesRequest = {}
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

    async def iter_list_identity_sources(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_mpa.types.identity_source_for_list.IdentitySourceForList]":
        _token = next_token
        while True:
            _response = await self.list_identity_sources(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("identity_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_session(
        self,
        session_arn: "capo_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.get_session_response.GetSessionResponse":
        """<p>Returns details for an approval session. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.get_session_response.GetSessionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_session

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.get_session_request.GetSessionRequest = {
            "session_arn": session_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_session(
        self,
        session_arn: "capo_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.cancel_session_response.CancelSessionResponse":
        """<p>Cancels an approval session. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.cancel_session_request.CancelSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.cancel_session_response.CancelSessionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.cancel_session

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.cancel_session.async_cancel_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.cancel_session_request.CancelSessionRequest = {
            "session_arn": session_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_sessions(
        self,
        approval_team_arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
        filters: Optional["capo_mpa.types.filters.Filters"] = None,
    ) -> "capo_mpa.types.list_sessions_response.ListSessionsResponse":
        """<p>Returns a list of approval sessions. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            approval_team_arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            filters: <p>An array of <code>Filter</code> objects. Contains the filter to apply when listing sessions.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_sessions

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_sessions_request.ListSessionsRequest = {
            "approval_team_arn": approval_team_arn
        }
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

    async def iter_list_sessions(
        self,
        approval_team_arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
        filters: Optional["capo_mpa.types.filters.Filters"] = None,
    ) -> "AsyncIterator[capo_mpa.types.list_sessions_response_session.ListSessionsResponseSession]":
        _token = next_token
        while True:
            _response = await self.list_sessions(
                approval_team_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

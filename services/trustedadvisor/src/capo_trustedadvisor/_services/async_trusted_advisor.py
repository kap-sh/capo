"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#TrustedAdvisor``."""

import datetime
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_trustedadvisor._auth._signers
import capo_trustedadvisor._auth._sigv4
from capo_trustedadvisor._auth._identity import Credentials
from capo_trustedadvisor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_trustedadvisor._auth._zapros_handler import AuthMiddleware
from capo_trustedadvisor._pagination import resolve_path as _resolve_path
from capo_trustedadvisor._services._aws_config import aaws_config
from capo_trustedadvisor._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_trustedadvisor.types.account_id
    import capo_trustedadvisor.types.account_recommendation_identifier
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary
    import capo_trustedadvisor.types.aws_resource_arn
    import capo_trustedadvisor.types.batch_update_recommendation_resource_exclusion_request
    import capo_trustedadvisor.types.batch_update_recommendation_resource_exclusion_response
    import capo_trustedadvisor.types.check_arn
    import capo_trustedadvisor.types.check_identifier
    import capo_trustedadvisor.types.check_summary
    import capo_trustedadvisor.types.exclusion_status
    import capo_trustedadvisor.types.get_organization_recommendation_request
    import capo_trustedadvisor.types.get_organization_recommendation_response
    import capo_trustedadvisor.types.get_recommendation_request
    import capo_trustedadvisor.types.get_recommendation_response
    import capo_trustedadvisor.types.list_checks_request
    import capo_trustedadvisor.types.list_checks_response
    import capo_trustedadvisor.types.list_organization_recommendation_accounts_request
    import capo_trustedadvisor.types.list_organization_recommendation_accounts_response
    import capo_trustedadvisor.types.list_organization_recommendation_resources_request
    import capo_trustedadvisor.types.list_organization_recommendation_resources_response
    import capo_trustedadvisor.types.list_organization_recommendations_request
    import capo_trustedadvisor.types.list_organization_recommendations_response
    import capo_trustedadvisor.types.list_recommendation_resources_request
    import capo_trustedadvisor.types.list_recommendation_resources_response
    import capo_trustedadvisor.types.list_recommendations_for_resource_request
    import capo_trustedadvisor.types.list_recommendations_for_resource_response
    import capo_trustedadvisor.types.list_recommendations_request
    import capo_trustedadvisor.types.list_recommendations_response
    import capo_trustedadvisor.types.organization_recommendation_identifier
    import capo_trustedadvisor.types.organization_recommendation_resource_summary
    import capo_trustedadvisor.types.organization_recommendation_summary
    import capo_trustedadvisor.types.recommendation_aws_service
    import capo_trustedadvisor.types.recommendation_for_resource_summary
    import capo_trustedadvisor.types.recommendation_language
    import capo_trustedadvisor.types.recommendation_pillar
    import capo_trustedadvisor.types.recommendation_resource_exclusion_list
    import capo_trustedadvisor.types.recommendation_resource_summary
    import capo_trustedadvisor.types.recommendation_source
    import capo_trustedadvisor.types.recommendation_status
    import capo_trustedadvisor.types.recommendation_summary
    import capo_trustedadvisor.types.recommendation_type
    import capo_trustedadvisor.types.recommendation_update_reason
    import capo_trustedadvisor.types.resource_status
    import capo_trustedadvisor.types.update_organization_recommendation_lifecycle_request
    import capo_trustedadvisor.types.update_recommendation_lifecycle_request
    import capo_trustedadvisor.types.update_recommendation_lifecycle_stage
    import capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code


class AsyncTrustedAdvisorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncTrustedAdvisorClient:
    """A client for the ``TrustedAdvisor`` service.

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
        self._config = AsyncTrustedAdvisorClientConfig(
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
        self, config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTrustedAdvisorClientConfig = config_overrides or {}
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

    async def batch_update_recommendation_resource_exclusion(
        self,
        recommendation_resource_exclusions: "capo_trustedadvisor.types.recommendation_resource_exclusion_list.RecommendationResourceExclusionList",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
    ) -> "capo_trustedadvisor.types.batch_update_recommendation_resource_exclusion_response.BatchUpdateRecommendationResourceExclusionResponse":
        """<p>Update one or more exclusion statuses for a list of recommendation resources. This API supports up to 25 unique recommendation resource ARNs per request. This API currently doesn't support prioritized recommendation resources. This API updates global recommendations, eliminating the need to call the API in each AWS Region. After submitting an exclusion update, note that it might take a few minutes for the changes to be reflected in the system.</p>

        Args:
            recommendation_resource_exclusions: <p>A list of recommendation resource ARNs and exclusion status to update</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.conflict_exception.ConflictException: <p>Exception that the request was denied due to conflictions in state</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Batch updates the exclusion status for a list of recommendation resources

            >>> await client.batch_update_recommendation_resource_exclusion(recommendation_resource_exclusions=[{'arn': 'arn:aws:trustedadvisor::000000000000:recommendation-resource/55fa4d2e-bbb7-491a-833b-5773e9589578/18959a1f1973cff8e706e9d9bde28bba36cd602a6b2cb86c8b61252835236010', 'isExcluded': True}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.batch_update_recommendation_resource_exclusion_request.BatchUpdateRecommendationResourceExclusionRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.batch_update_recommendation_resource_exclusion_response.BatchUpdateRecommendationResourceExclusionResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.batch_update_recommendation_resource_exclusion

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.batch_update_recommendation_resource_exclusion.async_batch_update_recommendation_resource_exclusion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.batch_update_recommendation_resource_exclusion_request.BatchUpdateRecommendationResourceExclusionRequest = {
            "recommendation_resource_exclusions": recommendation_resource_exclusions
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_organization_recommendation(
        self,
        organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
    ) -> "capo_trustedadvisor.types.get_organization_recommendation_response.GetOrganizationRecommendationResponse":
        """<p>Get a specific recommendation within an AWS Organizations organization. This API supports only prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            organization_recommendation_identifier: <p>The Recommendation identifier</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception that the requested resource has not been found</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an AWS Organization's Recommendation by ARN

            >>> await client.get_organization_recommendation(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.get_organization_recommendation_request.GetOrganizationRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.get_organization_recommendation_response.GetOrganizationRecommendationResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.get_organization_recommendation

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.get_organization_recommendation.async_get_organization_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.get_organization_recommendation_request.GetOrganizationRecommendationRequest = {
            "organization_recommendation_identifier": organization_recommendation_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recommendation(
        self,
        recommendation_identifier: "capo_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "capo_trustedadvisor.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Get a specific Recommendation. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            recommendation_identifier: <p>The Recommendation identifier</p>
            language: <p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception that the requested resource has not been found</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a Recommendation by ARN

            >>> await client.get_recommendation(recommendation_identifier='arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.get_recommendation

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.get_recommendation.async_get_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.get_recommendation_request.GetRecommendationRequest = {
            "recommendation_identifier": recommendation_identifier
        }
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_checks(
        self,
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "capo_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "capo_trustedadvisor.types.list_checks_response.ListChecksResponse":
        """<p>List a filterable set of Checks. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            pillar: <p>The pillar of the check</p>
            aws_service: <p>The aws service associated with the check</p>
            source: <p>The source of the check</p>
            language: <p>The ISO 639-1 code for the language that you want your checks to appear in.</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all AWS Trusted Advisor Checks

            >>> await client.list_checks()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.list_checks_request.ListChecksRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.list_checks_response.ListChecksResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.list_checks

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.list_checks.async_list_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.list_checks_request.ListChecksRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if pillar is not None:
            input_["pillar"] = pillar
        if aws_service is not None:
            input_["aws_service"] = aws_service
        if source is not None:
            input_["source"] = source
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_checks(
        self,
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "capo_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "AsyncIterator[capo_trustedadvisor.types.check_summary.CheckSummary]":
        _token = next_token
        while True:
            _response = await self.list_checks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                pillar=pillar,
                aws_service=aws_service,
                source=source,
                language=language,
            )
            _page = _resolve_path(_response, ("check_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_organization_recommendation_accounts(
        self,
        organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        affected_account_id: Optional[
            "capo_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_trustedadvisor.types.list_organization_recommendation_accounts_response.ListOrganizationRecommendationAccountsResponse":
        """<p>Lists the accounts that own the resources for an organization aggregate recommendation. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            organization_recommendation_identifier: <p>The Recommendation identifier</p>
            affected_account_id: <p>An account affected by this organization recommendation</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception that the requested resource has not been found</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all Accounts for an AWS Organization's Recommendation

            >>> await client.list_organization_recommendation_accounts(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.list_organization_recommendation_accounts_request.ListOrganizationRecommendationAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.list_organization_recommendation_accounts_response.ListOrganizationRecommendationAccountsResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_accounts

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_accounts.async_list_organization_recommendation_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.list_organization_recommendation_accounts_request.ListOrganizationRecommendationAccountsRequest = {
            "organization_recommendation_identifier": organization_recommendation_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if affected_account_id is not None:
            input_["affected_account_id"] = affected_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_organization_recommendation_accounts(
        self,
        organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        affected_account_id: Optional[
            "capo_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_trustedadvisor.types.account_recommendation_lifecycle_summary.AccountRecommendationLifecycleSummary]":
        _token = next_token
        while True:
            _response = await self.list_organization_recommendation_accounts(
                organization_recommendation_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                affected_account_id=affected_account_id,
            )
            _page = _resolve_path(
                _response, ("account_recommendation_lifecycle_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_organization_recommendation_resources(
        self,
        organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "capo_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "capo_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        affected_account_id: Optional[
            "capo_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_trustedadvisor.types.list_organization_recommendation_resources_response.ListOrganizationRecommendationResourcesResponse":
        """<p>List Resources of a Recommendation within an Organization. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            status: <p>The status of the resource</p>
            exclusion_status: <p>The exclusion status of the resource</p>
            region_code: <p>The AWS Region code of the resource</p>
            organization_recommendation_identifier: <p>The AWS Organization organization's Recommendation identifier</p>
            affected_account_id: <p>An account affected by this organization recommendation</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception that the requested resource has not been found</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all Resources for an AWS Organization's Recommendation

            >>> await client.list_organization_recommendation_resources(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/5a694939-2e54-45a2-ae72-730598fa89d0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.list_organization_recommendation_resources_request.ListOrganizationRecommendationResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.list_organization_recommendation_resources_response.ListOrganizationRecommendationResourcesResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_resources

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_resources.async_list_organization_recommendation_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.list_organization_recommendation_resources_request.ListOrganizationRecommendationResourcesRequest = {
            "organization_recommendation_identifier": organization_recommendation_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if exclusion_status is not None:
            input_["exclusion_status"] = exclusion_status
        if region_code is not None:
            input_["region_code"] = region_code
        if affected_account_id is not None:
            input_["affected_account_id"] = affected_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_organization_recommendation_resources(
        self,
        organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "capo_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "capo_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        affected_account_id: Optional[
            "capo_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_trustedadvisor.types.organization_recommendation_resource_summary.OrganizationRecommendationResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_organization_recommendation_resources(
                organization_recommendation_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                exclusion_status=exclusion_status,
                region_code=region_code,
                affected_account_id=affected_account_id,
            )
            _page = _resolve_path(
                _response, ("organization_recommendation_resource_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_organization_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "capo_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "capo_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "capo_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "capo_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
    ) -> "capo_trustedadvisor.types.list_organization_recommendations_response.ListOrganizationRecommendationsResponse":
        """<p>List a filterable set of Recommendations within an Organization. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            type: <p>The type of the Recommendation</p>
            status: <p>The status of the Recommendation</p>
            pillar: <p>The pillar of the Recommendation</p>
            aws_service: <p>The aws service associated with the Recommendation</p>
            source: <p>The source of the Recommendation</p>
            check_identifier: <p>The check identifier of the Recommendation</p>
            after_last_updated_at: <p>After the last update of the Recommendation</p>
            before_last_updated_at: <p>Before the last update of the Recommendation</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all of an AWS Organization's Recommendations

            >>> await client.list_organization_recommendations()
            Filter and return a max of one AWS Organization Recommendation that is a part of the "security" pillar

            >>> await client.list_organization_recommendations(pillar='security', max_results=100)
            Use the "nextToken" returned from a previous request to fetch the next page of filtered AWS Organization Recommendations that are a part of the "security" pillar

            >>> await client.list_organization_recommendations(next_token='<REDACTED>', pillar='security', max_results=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.list_organization_recommendations_request.ListOrganizationRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.list_organization_recommendations_response.ListOrganizationRecommendationsResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.list_organization_recommendations

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.list_organization_recommendations.async_list_organization_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.list_organization_recommendations_request.ListOrganizationRecommendationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type is not None:
            input_["type"] = type
        if status is not None:
            input_["status"] = status
        if pillar is not None:
            input_["pillar"] = pillar
        if aws_service is not None:
            input_["aws_service"] = aws_service
        if source is not None:
            input_["source"] = source
        if check_identifier is not None:
            input_["check_identifier"] = check_identifier
        if after_last_updated_at is not None:
            input_["after_last_updated_at"] = after_last_updated_at
        if before_last_updated_at is not None:
            input_["before_last_updated_at"] = before_last_updated_at

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_organization_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "capo_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "capo_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "capo_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "capo_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
    ) -> "AsyncIterator[capo_trustedadvisor.types.organization_recommendation_summary.OrganizationRecommendationSummary]":
        _token = next_token
        while True:
            _response = await self.list_organization_recommendations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                type=type,
                status=status,
                pillar=pillar,
                aws_service=aws_service,
                source=source,
                check_identifier=check_identifier,
                after_last_updated_at=after_last_updated_at,
                before_last_updated_at=before_last_updated_at,
            )
            _page = _resolve_path(_response, ("organization_recommendation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommendation_resources(
        self,
        recommendation_identifier: "capo_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "capo_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "capo_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "capo_trustedadvisor.types.list_recommendation_resources_response.ListRecommendationResourcesResponse":
        """<p>List Resources of a Recommendation. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            status: <p>The status of the resource</p>
            exclusion_status: <p>The exclusion status of the resource</p>
            region_code: <p>The AWS Region code of the resource</p>
            recommendation_identifier: <p>The Recommendation identifier</p>
            language: <p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception that the requested resource has not been found</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all Resources for a Recommendation

            >>> await client.list_recommendation_resources(recommendation_identifier='arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.list_recommendation_resources_request.ListRecommendationResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.list_recommendation_resources_response.ListRecommendationResourcesResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.list_recommendation_resources

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.list_recommendation_resources.async_list_recommendation_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.list_recommendation_resources_request.ListRecommendationResourcesRequest = {
            "recommendation_identifier": recommendation_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if exclusion_status is not None:
            input_["exclusion_status"] = exclusion_status
        if region_code is not None:
            input_["region_code"] = region_code
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recommendation_resources(
        self,
        recommendation_identifier: "capo_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "capo_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "capo_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "AsyncIterator[capo_trustedadvisor.types.recommendation_resource_summary.RecommendationResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_recommendation_resources(
                recommendation_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                exclusion_status=exclusion_status,
                region_code=region_code,
                language=language,
            )
            _page = _resolve_path(_response, ("recommendation_resource_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "capo_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "capo_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "capo_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "capo_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "capo_trustedadvisor.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>List a filterable set of Recommendations. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            type: <p>The type of the Recommendation</p>
            status: <p>The status of the Recommendation</p>
            pillar: <p>The pillar of the Recommendation</p>
            aws_service: <p>The aws service associated with the Recommendation</p>
            source: <p>The source of the Recommendation</p>
            check_identifier: <p>The check identifier of the Recommendation</p>
            after_last_updated_at: <p>After the last update of the Recommendation</p>
            before_last_updated_at: <p>Before the last update of the Recommendation</p>
            language: <p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all Recommendations

            >>> await client.list_recommendations()
            Filter and return a max of one Recommendation that is a part of AWS IAM

            >>> await client.list_recommendations(aws_service='iam', max_results=100)
            Use the "nextToken" returned from a previous request to fetch the next page of filtered Recommendations

            >>> await client.list_recommendations(next_token='<REDACTED>', aws_service='rds', max_results=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.list_recommendations

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.list_recommendations.async_list_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.list_recommendations_request.ListRecommendationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type is not None:
            input_["type"] = type
        if status is not None:
            input_["status"] = status
        if pillar is not None:
            input_["pillar"] = pillar
        if aws_service is not None:
            input_["aws_service"] = aws_service
        if source is not None:
            input_["source"] = source
        if check_identifier is not None:
            input_["check_identifier"] = check_identifier
        if after_last_updated_at is not None:
            input_["after_last_updated_at"] = after_last_updated_at
        if before_last_updated_at is not None:
            input_["before_last_updated_at"] = before_last_updated_at
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "capo_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "capo_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "capo_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "capo_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "AsyncIterator[capo_trustedadvisor.types.recommendation_summary.RecommendationSummary]":
        _token = next_token
        while True:
            _response = await self.list_recommendations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                type=type,
                status=status,
                pillar=pillar,
                aws_service=aws_service,
                source=source,
                check_identifier=check_identifier,
                after_last_updated_at=after_last_updated_at,
                before_last_updated_at=before_last_updated_at,
                language=language,
            )
            _page = _resolve_path(_response, ("recommendation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommendations_for_resource(
        self,
        aws_resource_arn: "capo_trustedadvisor.types.aws_resource_arn.AwsResourceArn",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        status: Optional[
            "capo_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        check_arn: Optional["capo_trustedadvisor.types.check_arn.CheckArn"] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "capo_trustedadvisor.types.list_recommendations_for_resource_response.ListRecommendationsForResourceResponse":
        """<p>List all Trusted Advisor recommendations for a given AWS resource ARN.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page</p>
            aws_resource_arn: <p>The ARN of the AWS resource to query recommendations for</p>
            pillar: <p>The pillar that the recommendation belongs to</p>
            status: <p>The current status of the Recommendation Resource</p>
            check_arn: <p>The AWS Trusted Advisor Check ARN that relates to the Recommendation</p>
            language: <p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all Trusted Advisor Recommendations for an AWS Resource

            >>> await client.list_recommendations_for_resource(aws_resource_arn='arn:aws:ec2:us-east-1:000000000000:instance/i-0abcd1234efgh5678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.list_recommendations_for_resource_request.ListRecommendationsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_trustedadvisor.types.list_recommendations_for_resource_response.ListRecommendationsForResourceResponse"
        ]:
            import capo_trustedadvisor._operations.trusted_advisor.list_recommendations_for_resource

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.list_recommendations_for_resource.async_list_recommendations_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.list_recommendations_for_resource_request.ListRecommendationsForResourceRequest = {
            "aws_resource_arn": aws_resource_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if pillar is not None:
            input_["pillar"] = pillar
        if status is not None:
            input_["status"] = status
        if check_arn is not None:
            input_["check_arn"] = check_arn
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recommendations_for_resource(
        self,
        aws_resource_arn: "capo_trustedadvisor.types.aws_resource_arn.AwsResourceArn",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        pillar: Optional[
            "capo_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        status: Optional[
            "capo_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        check_arn: Optional["capo_trustedadvisor.types.check_arn.CheckArn"] = None,
        language: Optional[
            "capo_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "AsyncIterator[capo_trustedadvisor.types.recommendation_for_resource_summary.RecommendationForResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_recommendations_for_resource(
                aws_resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                pillar=pillar,
                status=status,
                check_arn=check_arn,
                language=language,
            )
            _page = _resolve_path(_response, ("recommendation_for_resource_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_organization_recommendation_lifecycle(
        self,
        lifecycle_stage: "capo_trustedadvisor.types.update_recommendation_lifecycle_stage.UpdateRecommendationLifecycleStage",
        organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        update_reason: Optional[
            "capo_trustedadvisor.types.recommendation_update_reason.RecommendationUpdateReason"
        ] = None,
        update_reason_code: Optional[
            "capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.UpdateRecommendationLifecycleStageReasonCode"
        ] = None,
    ) -> None:
        """<p>Update the lifecycle of a Recommendation within an Organization. This API only supports prioritized recommendations and updates global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            lifecycle_stage: <p>The new lifecycle stage</p>
            update_reason: <p>Reason for the lifecycle stage change</p>
            update_reason_code: <p>Reason code for the lifecycle state change</p>
            organization_recommendation_identifier: <p>The Recommendation identifier for AWS Trusted Advisor Priority recommendations</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.conflict_exception.ConflictException: <p>Exception that the request was denied due to conflictions in state</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception that the requested resource has not been found</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update the lifecycle stage of an AWS Organization's Recommendation that is managed by AWS Trusted Advisor Priority

            >>> await client.update_organization_recommendation_lifecycle(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/96b5e5ca-7930-444c-90c6-06d386128100', lifecycle_stage='dismissed', update_reason_code='not_applicable', update_reason='Does not apply to this resource')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.update_organization_recommendation_lifecycle_request.UpdateOrganizationRecommendationLifecycleRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_trustedadvisor._operations.trusted_advisor.update_organization_recommendation_lifecycle

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.update_organization_recommendation_lifecycle.async_update_organization_recommendation_lifecycle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.update_organization_recommendation_lifecycle_request.UpdateOrganizationRecommendationLifecycleRequest = {
            "lifecycle_stage": lifecycle_stage,
            "organization_recommendation_identifier": organization_recommendation_identifier,
        }
        if update_reason is not None:
            input_["update_reason"] = update_reason
        if update_reason_code is not None:
            input_["update_reason_code"] = update_reason_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_recommendation_lifecycle(
        self,
        lifecycle_stage: "capo_trustedadvisor.types.update_recommendation_lifecycle_stage.UpdateRecommendationLifecycleStage",
        recommendation_identifier: "capo_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[AsyncTrustedAdvisorClientConfig] = None,
        update_reason: Optional[
            "capo_trustedadvisor.types.recommendation_update_reason.RecommendationUpdateReason"
        ] = None,
        update_reason_code: Optional[
            "capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.UpdateRecommendationLifecycleStageReasonCode"
        ] = None,
    ) -> None:
        """<p>Update the lifecyle of a Recommendation. This API only supports prioritized recommendations and updates global priority recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            lifecycle_stage: <p>The new lifecycle stage</p>
            update_reason: <p>Reason for the lifecycle stage change</p>
            update_reason_code: <p>Reason code for the lifecycle state change</p>
            recommendation_identifier: <p>The Recommendation identifier for AWS Trusted Advisor Priority recommendations</p>

        Raises:
            capo_trustedadvisor.errors.access_denied_exception.AccessDeniedException: <p>Exception that access has been denied due to insufficient access</p>
            capo_trustedadvisor.errors.conflict_exception.ConflictException: <p>Exception that the request was denied due to conflictions in state</p>
            capo_trustedadvisor.errors.internal_server_exception.InternalServerException: <p>Exception to notify that an unexpected internal error occurred during processing of the request</p>
            capo_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception that the requested resource has not been found</p>
            capo_trustedadvisor.errors.throttling_exception.ThrottlingException: <p>Exception to notify that requests are being throttled</p>
            capo_trustedadvisor.errors.validation_exception.ValidationException: <p>Exception that the request failed to satisfy service constraints</p>
            capo_trustedadvisor.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update the lifecycle stage of a Recommendation managed by AWS Trusted Advisor Priority

            >>> await client.update_recommendation_lifecycle(recommendation_identifier='arn:aws:trustedadvisor::000000000000:recommendation/861c9c6e-f169-405a-8b59-537a8caccd7a', lifecycle_stage='resolved', update_reason_code='valid_business_case', update_reason='Resolved the recommendation')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_trustedadvisor.types.update_recommendation_lifecycle_request.UpdateRecommendationLifecycleRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_trustedadvisor._operations.trusted_advisor.update_recommendation_lifecycle

            (
                output,
                http_response,
            ) = await capo_trustedadvisor._operations.trusted_advisor.update_recommendation_lifecycle.async_update_recommendation_lifecycle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_trustedadvisor.types.update_recommendation_lifecycle_request.UpdateRecommendationLifecycleRequest = {
            "lifecycle_stage": lifecycle_stage,
            "recommendation_identifier": recommendation_identifier,
        }
        if update_reason is not None:
            input_["update_reason"] = update_reason
        if update_reason_code is not None:
            input_["update_reason_code"] = update_reason_code

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

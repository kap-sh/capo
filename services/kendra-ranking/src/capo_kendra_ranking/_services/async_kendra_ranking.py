"""Generated from Smithy shape ``com.amazonaws.kendraranking#AWSKendraRerankingFrontendService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_kendra_ranking._auth._signers
import capo_kendra_ranking._auth._sigv4
from capo_kendra_ranking._auth._identity import Credentials
from capo_kendra_ranking._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kendra_ranking._auth._zapros_handler import AuthMiddleware
from capo_kendra_ranking._pagination import resolve_path as _resolve_path
from capo_kendra_ranking._services._aws_config import aaws_config
from capo_kendra_ranking._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_kendra_ranking.types.amazon_resource_name
    import capo_kendra_ranking.types.capacity_units_configuration
    import capo_kendra_ranking.types.client_token_name
    import capo_kendra_ranking.types.create_rescore_execution_plan_request
    import capo_kendra_ranking.types.create_rescore_execution_plan_response
    import capo_kendra_ranking.types.delete_rescore_execution_plan_request
    import capo_kendra_ranking.types.describe_rescore_execution_plan_request
    import capo_kendra_ranking.types.describe_rescore_execution_plan_response
    import capo_kendra_ranking.types.description
    import capo_kendra_ranking.types.document_list
    import capo_kendra_ranking.types.list_rescore_execution_plans_request
    import capo_kendra_ranking.types.list_rescore_execution_plans_response
    import capo_kendra_ranking.types.list_tags_for_resource_request
    import capo_kendra_ranking.types.list_tags_for_resource_response
    import capo_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request
    import capo_kendra_ranking.types.next_token
    import capo_kendra_ranking.types.rescore_execution_plan_id
    import capo_kendra_ranking.types.rescore_execution_plan_name
    import capo_kendra_ranking.types.rescore_request
    import capo_kendra_ranking.types.rescore_result
    import capo_kendra_ranking.types.search_query
    import capo_kendra_ranking.types.tag_key_list
    import capo_kendra_ranking.types.tag_list
    import capo_kendra_ranking.types.tag_resource_request
    import capo_kendra_ranking.types.tag_resource_response
    import capo_kendra_ranking.types.untag_resource_request
    import capo_kendra_ranking.types.untag_resource_response
    import capo_kendra_ranking.types.update_rescore_execution_plan_request


class AsyncKendraRankingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncKendraRankingClient:
    """A client for the ``KendraRanking`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        self._config = AsyncKendraRankingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncKendraRankingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKendraRankingClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_rescore_execution_plan(
        self,
        name: "capo_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
        description: Optional[
            "capo_kendra_ranking.types.description.Description"
        ] = None,
        capacity_units: Optional[
            "capo_kendra_ranking.types.capacity_units_configuration.CapacityUnitsConfiguration"
        ] = None,
        tags: Optional["capo_kendra_ranking.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_kendra_ranking.types.client_token_name.ClientTokenName"
        ] = None,
    ) -> "capo_kendra_ranking.types.create_rescore_execution_plan_response.CreateRescoreExecutionPlanResponse":
        """<p>Creates a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API. You set the number of capacity units that you require for Amazon Kendra Intelligent Ranking to rescore or re-rank a search service's results.</p> <p>For an example of using the <code>CreateRescoreExecutionPlan</code> API, including using the Python and Java SDKs, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html">Semantically ranking a search service's results</a>.</p>

        Args:
            name: <p>A name for the rescore execution plan.</p>
            description: <p>A description for the rescore execution plan.</p>
            capacity_units: <p>You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html">Adjusting capacity</a>.</p>
            tags: <p>A list of key-value pairs that identify or categorize your rescore execution plan. You can also use tags to help control access to the rescore execution plan. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token that you provide to identify the request to create a rescore execution plan. Multiple calls to the <code>CreateRescoreExecutionPlanRequest</code> API with the same client token will create only one rescore execution plan.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistencies with your resources and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra Intelligent Ranking service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.create_rescore_execution_plan_request.CreateRescoreExecutionPlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_kendra_ranking.types.create_rescore_execution_plan_response.CreateRescoreExecutionPlanResponse"
        ]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.create_rescore_execution_plan

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.create_rescore_execution_plan.async_create_rescore_execution_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.create_rescore_execution_plan_request.CreateRescoreExecutionPlanRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if capacity_units is not None:
            input_["capacity_units"] = capacity_units
        if tags is not None:
            input_["tags"] = tags
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

    async def delete_rescore_execution_plan(
        self,
        id: "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
    ) -> None:
        """<p>Deletes a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>

        Args:
            id: <p>The identifier of the rescore execution plan that you want to delete.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistencies with your resources and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn't exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.delete_rescore_execution_plan_request.DeleteRescoreExecutionPlanRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.delete_rescore_execution_plan

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.delete_rescore_execution_plan.async_delete_rescore_execution_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.delete_rescore_execution_plan_request.DeleteRescoreExecutionPlanRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_rescore_execution_plan(
        self,
        id: "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
    ) -> "capo_kendra_ranking.types.describe_rescore_execution_plan_response.DescribeRescoreExecutionPlanResponse":
        """<p>Gets information about a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>

        Args:
            id: <p>The identifier of the rescore execution plan that you want to get information on.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn't exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.describe_rescore_execution_plan_request.DescribeRescoreExecutionPlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_kendra_ranking.types.describe_rescore_execution_plan_response.DescribeRescoreExecutionPlanResponse"
        ]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.describe_rescore_execution_plan

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.describe_rescore_execution_plan.async_describe_rescore_execution_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.describe_rescore_execution_plan_request.DescribeRescoreExecutionPlanRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_rescore_execution_plans(
        self,
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
        next_token: Optional["capo_kendra_ranking.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request.MaxResultsIntegerForListRescoreExecutionPlansRequest"
        ] = None,
    ) -> "capo_kendra_ranking.types.list_rescore_execution_plans_response.ListRescoreExecutionPlansResponse":
        """<p>Lists your rescore execution plans. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>

        Args:
            next_token: <p>If the response is truncated, Amazon Kendra Intelligent Ranking returns a pagination token in the response. You can use this pagination token to retrieve the next set of rescore execution plans.</p>
            max_results: <p>The maximum number of rescore execution plans to return.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.list_rescore_execution_plans_request.ListRescoreExecutionPlansRequest]",
        ) -> AsyncOperationResponse[
            "capo_kendra_ranking.types.list_rescore_execution_plans_response.ListRescoreExecutionPlansResponse"
        ]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_rescore_execution_plans

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_rescore_execution_plans.async_list_rescore_execution_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.list_rescore_execution_plans_request.ListRescoreExecutionPlansRequest = {}
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

    async def iter_list_rescore_execution_plans(
        self,
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
        next_token: Optional["capo_kendra_ranking.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request.MaxResultsIntegerForListRescoreExecutionPlansRequest"
        ] = None,
    ) -> "AsyncIterator[capo_kendra_ranking.types.list_rescore_execution_plans_response.ListRescoreExecutionPlansResponse]":
        _token = next_token
        while True:
            _response = await self.list_rescore_execution_plans(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_kendra_ranking.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
    ) -> "capo_kendra_ranking.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets a list of tags associated with a specified resource. A rescore execution plan is an example of a resource that can have tags associated with it.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rescore execution plan to get a list of tags for.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The resource you want to use is unavailable. Please check you have provided the correct resource information and try again.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_kendra_ranking.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rescore(
        self,
        rescore_execution_plan_id: "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        search_query: "capo_kendra_ranking.types.search_query.SearchQuery",
        documents: "capo_kendra_ranking.types.document_list.DocumentList",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
    ) -> "capo_kendra_ranking.types.rescore_result.RescoreResult":
        """<p>Rescores or re-ranks search results from a search service such as OpenSearch (self managed). You use the semantic search capabilities of Amazon Kendra Intelligent Ranking to improve the search service's results.</p>

        Args:
            rescore_execution_plan_id: <p>The identifier of the rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>
            search_query: <p>The input query from the search service.</p>
            documents: <p>The list of documents for Amazon Kendra Intelligent Ranking to rescore or rank on.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistencies with your resources and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn't exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.rescore_request.RescoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_kendra_ranking.types.rescore_result.RescoreResult"
        ]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.rescore

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.rescore.async_rescore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.rescore_request.RescoreRequest = {
            "rescore_execution_plan_id": rescore_execution_plan_id,
            "search_query": search_query,
            "documents": documents,
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
        resource_arn: "capo_kendra_ranking.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_kendra_ranking.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
    ) -> "capo_kendra_ranking.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a specified tag to a specified rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API. If the tag already exists, the existing value is replaced with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rescore execution plan to tag.</p>
            tags: <p>A list of tag keys to add to a rescore execution plan. If a tag already exists, the existing value is replaced with the new value.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The resource you want to use is unavailable. Please check you have provided the correct resource information and try again.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_kendra_ranking.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_kendra_ranking.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_kendra_ranking.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
    ) -> "capo_kendra_ranking.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> operation.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rescore execution plan to remove the tag.</p>
            tag_keys: <p>A list of tag keys to remove from the rescore execution plan. If a tag key does not exist on the resource, it is ignored.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The resource you want to use is unavailable. Please check you have provided the correct resource information and try again.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_kendra_ranking.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_rescore_execution_plan(
        self,
        id: "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        *,
        config_overrides: Optional[AsyncKendraRankingClientConfig] = None,
        name: Optional[
            "capo_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName"
        ] = None,
        description: Optional[
            "capo_kendra_ranking.types.description.Description"
        ] = None,
        capacity_units: Optional[
            "capo_kendra_ranking.types.capacity_units_configuration.CapacityUnitsConfiguration"
        ] = None,
    ) -> None:
        """<p>Updates a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API. You can update the number of capacity units you require for Amazon Kendra Intelligent Ranking to rescore or re-rank a search service's results.</p>

        Args:
            id: <p>The identifier of the rescore execution plan that you want to update.</p>
            name: <p>A new name for the rescore execution plan.</p>
            description: <p>A new description for the rescore execution plan.</p>
            capacity_units: <p>You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html">Adjusting capacity</a>.</p>

        Raises:
            capo_kendra_ranking.errors.access_denied_exception.AccessDeniedException: <p>You don’t have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra_ranking.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistencies with your resources and try again.</p>
            capo_kendra_ranking.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra Intelligent Ranking service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra_ranking.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn't exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra_ranking.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra Intelligent Ranking service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra_ranking.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra_ranking.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra Intelligent Ranking service. Please provide the correct input and try again.</p>
            capo_kendra_ranking.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kendra_ranking.types.update_rescore_execution_plan_request.UpdateRescoreExecutionPlanRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.update_rescore_execution_plan

            (
                output,
                http_response,
            ) = await capo_kendra_ranking._operations.aws_kendra_reranking_frontend_service.update_rescore_execution_plan.async_update_rescore_execution_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra_ranking.types.update_rescore_execution_plan_request.UpdateRescoreExecutionPlanRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if capacity_units is not None:
            input_["capacity_units"] = capacity_units

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

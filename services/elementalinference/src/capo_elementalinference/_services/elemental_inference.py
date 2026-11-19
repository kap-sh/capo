"""Generated from Smithy shape ``com.amazonaws.elementalinference#ElementalInference``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_elementalinference._auth._signers
import capo_elementalinference._auth._sigv4
from capo_elementalinference._auth._identity import Credentials
from capo_elementalinference._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elementalinference._auth._zapros_handler import AuthMiddleware
from capo_elementalinference._pagination import resolve_path as _resolve_path
from capo_elementalinference._resources.elemental_inference.dictionary_resource import (
    DictionaryResource,
)
from capo_elementalinference._resources.elemental_inference.feed_resource import (
    FeedResource,
)
from capo_elementalinference._resources.elemental_inference.function_resource import (
    FunctionResource,
)
from capo_elementalinference._resources.elemental_inference.question_set_resource import (
    QuestionSetResource,
)
from capo_elementalinference._services._aws_config import aws_config
from capo_elementalinference._services._pipeline import (
    Interceptor,
    OperationLogging,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    ThreadSafeRateLimiter,
    ThreadSafeRetryQuota,
    execute_pipeline,
    log_operation,
    rate_limit,
    retry,
)

if TYPE_CHECKING:
    import capo_elementalinference.types.associate_feed_request
    import capo_elementalinference.types.associate_feed_response
    import capo_elementalinference.types.associated_resource_name
    import capo_elementalinference.types.choose_one_question_list
    import capo_elementalinference.types.create_dictionary_request
    import capo_elementalinference.types.create_dictionary_response
    import capo_elementalinference.types.create_feed_request
    import capo_elementalinference.types.create_feed_response
    import capo_elementalinference.types.create_function_request
    import capo_elementalinference.types.create_function_response
    import capo_elementalinference.types.create_output_list
    import capo_elementalinference.types.create_question_set_request
    import capo_elementalinference.types.create_question_set_response
    import capo_elementalinference.types.create_question_set_version_request
    import capo_elementalinference.types.create_question_set_version_response
    import capo_elementalinference.types.create_schedule_action_request
    import capo_elementalinference.types.create_schedule_action_response
    import capo_elementalinference.types.data_source_sport
    import capo_elementalinference.types.delete_dictionary_request
    import capo_elementalinference.types.delete_dictionary_response
    import capo_elementalinference.types.delete_feed_policy_request
    import capo_elementalinference.types.delete_feed_request
    import capo_elementalinference.types.delete_feed_response
    import capo_elementalinference.types.delete_function_request
    import capo_elementalinference.types.delete_function_response
    import capo_elementalinference.types.delete_question_set_request
    import capo_elementalinference.types.delete_question_set_response
    import capo_elementalinference.types.delete_question_set_version_request
    import capo_elementalinference.types.delete_question_set_version_response
    import capo_elementalinference.types.delete_schedule_action_request
    import capo_elementalinference.types.delete_schedule_action_response
    import capo_elementalinference.types.dictionary_entries_payload
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.dictionary_language
    import capo_elementalinference.types.dictionary_summary
    import capo_elementalinference.types.disassociate_feed_request
    import capo_elementalinference.types.disassociate_feed_response
    import capo_elementalinference.types.event_bridge_delivery_mode
    import capo_elementalinference.types.export_dictionary_entries_request
    import capo_elementalinference.types.export_dictionary_entries_response
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.feed_summary
    import capo_elementalinference.types.fixture_date
    import capo_elementalinference.types.fixture_id
    import capo_elementalinference.types.fixture_summary
    import capo_elementalinference.types.function_description
    import capo_elementalinference.types.function_id
    import capo_elementalinference.types.function_summary
    import capo_elementalinference.types.function_target
    import capo_elementalinference.types.get_dictionary_request
    import capo_elementalinference.types.get_dictionary_response
    import capo_elementalinference.types.get_feed_policy_request
    import capo_elementalinference.types.get_feed_policy_response
    import capo_elementalinference.types.get_feed_request
    import capo_elementalinference.types.get_feed_response
    import capo_elementalinference.types.get_fixture_request
    import capo_elementalinference.types.get_fixture_response
    import capo_elementalinference.types.get_function_request
    import capo_elementalinference.types.get_function_response
    import capo_elementalinference.types.get_question_set_request
    import capo_elementalinference.types.get_question_set_response
    import capo_elementalinference.types.iam_role_arn
    import capo_elementalinference.types.jsonata_expression
    import capo_elementalinference.types.list_dictionaries_request
    import capo_elementalinference.types.list_dictionaries_response
    import capo_elementalinference.types.list_feeds_request
    import capo_elementalinference.types.list_feeds_response
    import capo_elementalinference.types.list_functions_request
    import capo_elementalinference.types.list_functions_response
    import capo_elementalinference.types.list_question_set_versions_request
    import capo_elementalinference.types.list_question_set_versions_response
    import capo_elementalinference.types.list_question_sets_request
    import capo_elementalinference.types.list_question_sets_response
    import capo_elementalinference.types.list_schedule_actions_request
    import capo_elementalinference.types.list_schedule_actions_response
    import capo_elementalinference.types.list_tags_for_resource_request
    import capo_elementalinference.types.list_tags_for_resource_response
    import capo_elementalinference.types.policy_document
    import capo_elementalinference.types.published_question_set_version
    import capo_elementalinference.types.put_feed_policy_request
    import capo_elementalinference.types.put_feed_policy_response
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.question_set_sha256
    import capo_elementalinference.types.question_set_summary
    import capo_elementalinference.types.question_set_version
    import capo_elementalinference.types.question_set_version_description
    import capo_elementalinference.types.question_set_version_summary
    import capo_elementalinference.types.resource_arn
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.schedule_action
    import capo_elementalinference.types.schedule_action_operations
    import capo_elementalinference.types.schedule_action_start_configuration
    import capo_elementalinference.types.search_filter_list
    import capo_elementalinference.types.search_fixtures_request
    import capo_elementalinference.types.search_fixtures_response
    import capo_elementalinference.types.tag_key_list
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.tag_resource_request
    import capo_elementalinference.types.untag_resource_request
    import capo_elementalinference.types.update_dictionary_request
    import capo_elementalinference.types.update_dictionary_response
    import capo_elementalinference.types.update_feed_request
    import capo_elementalinference.types.update_feed_response
    import capo_elementalinference.types.update_function_request
    import capo_elementalinference.types.update_function_response
    import capo_elementalinference.types.update_output_list
    import capo_elementalinference.types.update_question_set_request
    import capo_elementalinference.types.update_question_set_response
    import capo_elementalinference.types.yes_no_per_option_question_list
    import capo_elementalinference.types.yes_no_question_list


class ElementalInferenceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ElementalInferenceClient:
    """A client for the ``ElementalInference`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        retry_mode: Literal["standard", "adaptive"] | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = Client(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = ThreadSafeRetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = ThreadSafeRateLimiter()
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
                Client(raw_handler)
            )
        self._config = ElementalInferenceClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.dictionary_resource = DictionaryResource(self)
        self.feed_resource = FeedResource(self)
        self.function_resource = FunctionResource(self)
        self.question_set_resource = QuestionSetResource(self)

    def operation_options(
        self,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ElementalInferenceClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(log_operation(operation_logging))
        interceptors_.append(retry())
        interceptors_.append(rate_limit())
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
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

    def get_fixture(
        self,
        fixture_id: "capo_elementalinference.types.fixture_id.FixtureId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_fixture_response.GetFixtureResponse":
        """<p>Retrieves information about the specified fixture (a sports event, such as a specific basketball game). You obtain a fixtureId from SearchFixtures, or from the clipping output of a feed. </p>

        Args:
            fixture_id: <p>The ID of the fixture to retrieve, as returned by SearchFixtures.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.gateway_timed_out_exception.GatewayTimedOutException: <p>The request timed out before the service returned a response. This is a temporary condition. Retry the request. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unable to handle the request. Retry the request. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_fixture_request.GetFixtureRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_fixture_response.GetFixtureResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_fixture

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_fixture.get_fixture(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetFixture")
        )
        input_: capo_elementalinference.types.get_fixture_request.GetFixtureRequest = {
            "fixture_id": fixture_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_elementalinference.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags that are on an Elemental Inference resource in the current region.</p>

        Args:
            resource_arn: <p>The ARN of the resource whose tags you want to query.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_tags_for_resource

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_elementalinference.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_fixtures(
        self,
        sport: "capo_elementalinference.types.data_source_sport.DataSourceSport",
        start_date: "capo_elementalinference.types.fixture_date.FixtureDate",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        end_date: Optional[
            "capo_elementalinference.types.fixture_date.FixtureDate"
        ] = None,
        filters: Optional[
            "capo_elementalinference.types.search_filter_list.SearchFilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "capo_elementalinference.types.search_fixtures_response.SearchFixturesResponse"
    ):
        """<p>Searches for the fixtures (sports events, such as a specific basketball game) that are available for a sport in a date window. Each fixture in the response includes a fixtureId that you specify in the clipping output of a feed, so that Elemental Inference maps the event data for that fixture onto the clipping metadata. This operation is paginated: if there are more fixtures than fit in one page, the response includes a nextToken that you pass in a subsequent request. </p>

        Args:
            sport: <p>The sport to search for fixtures. Valid values: basketball (search for basketball fixtures), american-football (search for american-football fixtures). </p>
            start_date: <p>The first day of the search window, in UTC. The search includes fixtures that are scheduled on this day. </p> <p>Specify the date in ISO 8601 format, as <code>YYYY-MM-DD</code>. For example, 2026-03-14. </p>
            end_date: <p>The last day of the search window, in UTC. The search includes fixtures that are scheduled on this day. Specify the date in ISO 8601 format, as <code>YYYY-MM-DD</code>. </p> <p>If you omit this parameter, Elemental Inference searches only the day that you specified in startDate. The window from startDate through endDate must not exceed seven days. </p>
            filters: <p>An array of filters that narrow the results. Each filter applies to one dimension of a fixture, such as the competitor. You can specify up to 10 filters. </p> <p>A fixture must satisfy every filter in the array in order to appear in the results. Within one filter, a fixture must match at least one of the values. </p>
            max_results: <p>The maximum number of fixtures to return for each API request.</p> <p>The service might return fewer fixtures than the maxResults value. When more fixtures match the search, the response also includes a nextToken value that you can use to fetch the next batch of results. </p>
            next_token: <p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a SearchFixtures request with maxResults set at 5. The service returns the first batch of results (up to 5) and a nextToken value. To see the next batch of results, you submit the SearchFixtures request a second time, with the same search criteria, and specify the nextToken value. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.gateway_timed_out_exception.GatewayTimedOutException: <p>The request timed out before the service returned a response. This is a temporary condition. Retry the request. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unable to handle the request. Retry the request. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.search_fixtures_request.SearchFixturesRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.search_fixtures_response.SearchFixturesResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.search_fixtures

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.search_fixtures.search_fixtures(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("SearchFixtures")
        )
        input_: capo_elementalinference.types.search_fixtures_request.SearchFixturesRequest = {
            "sport": sport,
            "start_date": start_date,
        }
        if end_date is not None:
            input_["end_date"] = end_date
        if filters is not None:
            input_["filters"] = filters
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

    def iter_search_fixtures(
        self,
        sport: "capo_elementalinference.types.data_source_sport.DataSourceSport",
        start_date: "capo_elementalinference.types.fixture_date.FixtureDate",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        end_date: Optional[
            "capo_elementalinference.types.fixture_date.FixtureDate"
        ] = None,
        filters: Optional[
            "capo_elementalinference.types.search_filter_list.SearchFilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.fixture_summary.FixtureSummary]":
        _token = next_token
        while True:
            _response = self.search_fixtures(
                sport,
                start_date,
                config_overrides=config_overrides,
                end_date=end_date,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fixtures",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def tag_resource(
        self,
        resource_arn: "capo_elementalinference.types.resource_arn.ResourceArn",
        tags: "capo_elementalinference.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Associates the specified tags to the resource identified by the specified resourceArn in the current region. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted. </p>

        Args:
            resource_arn: <p>The ARN of the resource where you want to add tags.</p>
            tags: <p>A list of tags to add to the resource.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_elementalinference._operations.elemental_inference.tag_resource

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_elementalinference.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
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
        resource_arn: "capo_elementalinference.types.resource_arn.ResourceArn",
        tag_keys: "capo_elementalinference.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Deletes specified tags from the specified resource in the current region.</p>

        Args:
            resource_arn: <p>The ARN of the resource where you want to delete one or more tags.</p>
            tag_keys: <p>The keys of the tags to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_elementalinference._operations.elemental_inference.untag_resource

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_elementalinference.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_dictionary(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        language: "capo_elementalinference.types.dictionary_language.DictionaryLanguage",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        entries: Optional[
            "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_dictionary_response.CreateDictionaryResponse":
        """<p>Creates a custom dictionary for improving transcription accuracy. A dictionary contains custom words and phrases that the ASR engine might not recognize, such as brand names, technical terms, or proper nouns. You can reference a dictionary when configuring a smart subtitles output. </p>

        Args:
            name: <p>A user-friendly name for this dictionary.</p>
            language: <p>The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por. </p>
            entries: <p>The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters. </p>
            tags: <p>Optional tags to associate with the dictionary.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_dictionary_request.CreateDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_dictionary_response.CreateDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_dictionary.create_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateDictionary")
        )
        input_: capo_elementalinference.types.create_dictionary_request.CreateDictionaryRequest = {
            "name": name,
            "language": language,
        }
        if entries is not None:
            input_["entries"] = entries
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dictionary(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_dictionary_response.GetDictionaryResponse":
        """<p>Retrieves information about the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to retrieve.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_dictionary_request.GetDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_dictionary_response.GetDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_dictionary.get_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetDictionary")
        )
        input_: capo_elementalinference.types.get_dictionary_request.GetDictionaryRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_dictionary(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
        language: Optional[
            "capo_elementalinference.types.dictionary_language.DictionaryLanguage"
        ] = None,
        entries: Optional[
            "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
    ) -> "capo_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse":
        """<p>Updates the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to update.</p>
            name: <p>A new name for the dictionary. If not specified, the name is not changed.</p>
            language: <p>A new language for the dictionary. If not specified, the language is not changed.</p>
            entries: <p>New dictionary entries. If not specified, the entries are not changed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_dictionary.update_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateDictionary")
        )
        input_: capo_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if language is not None:
            input_["language"] = language
        if entries is not None:
            input_["entries"] = entries

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_dictionary(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse":
        """<p>Deletes the specified dictionary. You cannot delete a dictionary that is referenced by a feed. You must first remove the dictionary reference from the feed's subtitling configuration. </p>

        Args:
            id: <p>The ID of the dictionary to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_dictionary

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_dictionary.delete_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteDictionary")
        )
        input_: capo_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_dictionaries(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_dictionaries_response.ListDictionariesResponse":
        """<p>Lists the dictionaries in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_dictionaries_request.ListDictionariesRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_dictionaries_response.ListDictionariesResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_dictionaries

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_dictionaries.list_dictionaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListDictionaries")
        )
        input_: capo_elementalinference.types.list_dictionaries_request.ListDictionariesRequest = {}
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

    def iter_list_dictionaries(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.dictionary_summary.DictionarySummary]":
        _token = next_token
        while True:
            _response = self.list_dictionaries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dictionaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def export_dictionary_entries(
        self,
        id: "capo_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse":
        """<p>Exports the entries from the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary whose entries you want to export.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.export_dictionary_entries

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.export_dictionary_entries.export_dictionary_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ExportDictionaryEntries")
        )
        input_: capo_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_feed(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        access_role_arn: Optional[
            "capo_elementalinference.types.iam_role_arn.IamRoleArn"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_feed_response.CreateFeedResponse":
        """<p>Creates a feed. The feed is the target for the live media stream that is being sent by the calling application. An example of a calling application is AWS Elemental MediaLive. </p> <p>The key contents of the feed is an array of outputs. Each output represents an Elemental Inference feature. After you create the feed, you must associate a resource with the feed. At that point, you will have a useable feed: resource - feed - output or outputs. </p>

        Args:
            name: <p>A user-friendly name for this feed.</p>
            access_role_arn: <p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. For example, the smart crop feature uses this role to read graphics-compositing templates from your Amazon S3 bucket. You specify one access role for each feed. </p>
            outputs: <p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>
            tags: <p>Optional tags. You can also add tags later, using TagResource.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_feed_request.CreateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_feed_response.CreateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_feed.create_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateFeed")
        )
        input_: capo_elementalinference.types.create_feed_request.CreateFeedRequest = {
            "name": name,
            "outputs": outputs,
        }
        if access_role_arn is not None:
            input_["access_role_arn"] = access_role_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_feed_response.GetFeedResponse":
        """<p>Retrieves information about the specified feed.</p>

        Args:
            id: <p>The ID of the feed to query.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_feed_request.GetFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_feed_response.GetFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_feed.get_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetFeed")
        )
        input_: capo_elementalinference.types.get_feed_request.GetFeedRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_feed(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        id: "capo_elementalinference.types.feed_id.FeedId",
        outputs: "capo_elementalinference.types.update_output_list.UpdateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        access_role_arn: Optional[
            "capo_elementalinference.types.iam_role_arn.IamRoleArn"
        ] = None,
    ) -> "capo_elementalinference.types.update_feed_response.UpdateFeedResponse":
        """<p>Updates the name and/or outputs in a feed. </p> <p>UpdateFeed is a PUT operation, which means that the payload that you specify completely overwrites the existing payload. </p> <p>This means that if you want to touch the array of outputs, you must pass in the full new list. So you must omit outputs you want to delete, and include outputs you want to add or modify. </p> <p>If you want to patch the array of outputs to make selective additions, use AssociateFeed. </p>

        Args:
            name: <p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>
            access_role_arn: <p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. You can specify the existing role (to leave it unchanged) or a new role. You specify one access role for each feed. </p>
            id: <p>The ID of the feed to update.</p>
            outputs: <p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.update_feed_request.UpdateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_feed_response.UpdateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_feed.update_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateFeed")
        )
        input_: capo_elementalinference.types.update_feed_request.UpdateFeedRequest = {
            "name": name,
            "id": id,
            "outputs": outputs,
        }
        if access_role_arn is not None:
            input_["access_role_arn"] = access_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse":
        """<p>Deletes the specified feed. You can delete the feed at any time. Elemental Inference doesn't block you from deleting a feed when the calling application is calling PutMedia or GetMetadata on that feed, although both these calls will start to fail. For more information about managing inactive feeds, see the Elemental Inference User Guide. </p>

        Args:
            id: <p>The ID of the feed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_feed_request.DeleteFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_feed_response.DeleteFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_feed.delete_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteFeed")
        )
        input_: capo_elementalinference.types.delete_feed_request.DeleteFeedRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_feeds(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_feeds_response.ListFeedsResponse":
        """<p>Displays a list of feeds that belong to this AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request.</p> <p>For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page. </p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>
            next_token: <p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_feeds_request.ListFeedsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_feeds_response.ListFeedsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_feeds

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_feeds.list_feeds(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListFeeds")
        )
        input_: capo_elementalinference.types.list_feeds_request.ListFeedsRequest = {}
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

    def iter_list_feeds(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.feed_summary.FeedSummary]":
        _token = next_token
        while True:
            _response = self.list_feeds(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("feeds",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        outputs: "capo_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse":
        """<p>Associates a resource with the feed. The resource provides the input that Elemental Inference needs in order to perform an Elemental Inference feature, such as cropping video. You always provide the resource by associating it with a feed. You can associate only one resource with each feed. With an association, a specific source media is claiming ownership of the feed. </p> <p>AssociateFeed is a PATCH operation, which means that you can include only parameters that you want to change. Parameters that you don't include will not be affected by the operation. </p> <p>Specifically:</p> <ul> <li> <p>You can add more outputs to the existing outputs. New outputs will be appended.</p> </li> <li> <p>You can't modify an existing output (for example to change its name). Instead, use UpdateFeed. </p> </li> <li> <p>You can't delete an existing output. Instead, use UpdateFeed.</p> </li> </ul> <p>Also note that you can't change the feed name with AssociateFeed. Instead, use UpdateFeed. </p>

        Args:
            id: <p>The ID of the feed.</p>
            associated_resource_name: <p>An identifier for the resource. This name must not resemble an ARN.</p> <p>The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia). </p>
            outputs: <p>An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed. </p>
            dry_run: <p>Set to true if you want to do a dry run of the associate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.associate_feed_request.AssociateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.associate_feed_response.AssociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.associate_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.associate_feed.associate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("AssociateFeed")
        )
        input_: capo_elementalinference.types.associate_feed_request.AssociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
            "outputs": outputs,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_schedule_action(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        action_name: "capo_elementalinference.types.resource_name.ResourceName",
        start_configuration: "capo_elementalinference.types.schedule_action_start_configuration.ScheduleActionStartConfiguration",
        operations: "capo_elementalinference.types.schedule_action_operations.ScheduleActionOperations",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.create_schedule_action_response.CreateScheduleActionResponse":
        """<p>Creates a schedule action on a feed. A schedule action applies configuration changes to the feed at a time that you specify, in the same way as an UpdateFeed request. </p> <p>Elemental Inference validates the targets of the action when you create it.</p>

        Args:
            id: <p>Specifies the ID of the feed that you want to add the schedule action to.</p>
            action_name: <p>A name for the schedule action. The name must be unique within the feed. You can reuse the name of an action that you deleted. </p>
            start_configuration: <p>Specifies when the action runs.</p>
            operations: <p>Specifies the list of configuration changes that you want to make to the feed. Elemental Inference applies all the operations in an action together, in the order that you specify them. If any operation fails, Elemental Inference doesn't apply any of them. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_schedule_action_request.CreateScheduleActionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_schedule_action_response.CreateScheduleActionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_schedule_action

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_schedule_action.create_schedule_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateScheduleAction")
        )
        input_: capo_elementalinference.types.create_schedule_action_request.CreateScheduleActionRequest = {
            "id": id,
            "action_name": action_name,
            "start_configuration": start_configuration,
            "operations": operations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource-based policy attached to the specified feed. After you delete the policy, the operation revokes the cross-account access that the policy granted. </p>

        Args:
            id: <p>The ID of the feed whose policy you want to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_feed_policy_request.DeleteFeedPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_elementalinference._operations.elemental_inference.delete_feed_policy

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_feed_policy.delete_feed_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteFeedPolicy")
        )
        input_: capo_elementalinference.types.delete_feed_policy_request.DeleteFeedPolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_schedule_action(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        action_name: "capo_elementalinference.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_schedule_action_response.DeleteScheduleActionResponse":
        """<p>Deletes a schedule action from a feed. A deleted action never runs.</p> <p>You can delete only an action whose status is PENDING. Deleting an action doesn't reverse changes that the action already made to the feed. When you delete or archive a feed, Elemental Inference deletes all the schedule actions on that feed. </p>

        Args:
            id: <p>The ID of the feed that holds the schedule action.</p>
            action_name: <p>The name of the schedule action that you want to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_schedule_action_request.DeleteScheduleActionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_schedule_action_response.DeleteScheduleActionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_schedule_action

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_schedule_action.delete_schedule_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteScheduleAction")
        )
        input_: capo_elementalinference.types.delete_schedule_action_request.DeleteScheduleActionRequest = {
            "id": id,
            "action_name": action_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_feed(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "capo_elementalinference.types.associated_resource_name.AssociatedResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse":
        """<p>Releases the resource (the source media) that is associated with this feed. The outputs in the feed become DISABLED. </p>

        Args:
            id: <p>The ID of the feed where you want to release the resource.</p>
            associated_resource_name: <p>The name of the resource currently associated with the feed.</p>
            dry_run: <p>Set to true if you want to do a dry run of the disassociate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.disassociate_feed

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.disassociate_feed.disassociate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DisassociateFeed")
        )
        input_: capo_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest = {
            "id": id,
            "associated_resource_name": associated_resource_name,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_feed_policy_response.GetFeedPolicyResponse":
        """<p>Retrieves the resource-based policy attached to the specified feed.</p>

        Args:
            id: <p>The ID of the feed whose policy you want to retrieve.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_feed_policy_request.GetFeedPolicyRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_feed_policy_response.GetFeedPolicyResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_feed_policy

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_feed_policy.get_feed_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetFeedPolicy")
        )
        input_: capo_elementalinference.types.get_feed_policy_request.GetFeedPolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_schedule_actions(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_schedule_actions_response.ListScheduleActionsResponse":
        """<p>Displays a list of the schedule actions on a feed, including the status of each action and, for a failed action, information about why it failed. </p> <p>Elemental Inference keeps an action whose status is COMPLETED or FAILED for about 48 hours after its scheduled time, and then deletes it automatically. </p>

        Args:
            id: <p>The ID of the feed that you want to query.</p>
            max_results: <p>The maximum number of results to return for each API request. If you don't specify MaxResults, Elemental Inference returns a maximum of 10 results for each page. </p>
            next_token: <p>The token that identifies the batch of results that you want to see. To see the next batch, submit the request a second time and specify the NextToken value that Elemental Inference returned. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_schedule_actions_request.ListScheduleActionsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_schedule_actions_response.ListScheduleActionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_schedule_actions

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_schedule_actions.list_schedule_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListScheduleActions")
        )
        input_: capo_elementalinference.types.list_schedule_actions_request.ListScheduleActionsRequest = {
            "id": id
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

    def iter_list_schedule_actions(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.schedule_action.ScheduleAction]":
        _token = next_token
        while True:
            _response = self.list_schedule_actions(
                id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schedule_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_feed_policy(
        self,
        id: "capo_elementalinference.types.feed_id.FeedId",
        policy: "capo_elementalinference.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.put_feed_policy_response.PutFeedPolicyResponse":
        """<p>Attaches or replaces a resource-based policy on the specified feed. A resource-based policy grants cross-account access to the feed. </p>

        Args:
            id: <p>The ID of the feed to attach the policy to.</p>
            policy: <p>The resource-based policy document to attach to the feed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.put_feed_policy_request.PutFeedPolicyRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.put_feed_policy_response.PutFeedPolicyResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.put_feed_policy

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.put_feed_policy.put_feed_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("PutFeedPolicy")
        )
        input_: capo_elementalinference.types.put_feed_policy_request.PutFeedPolicyRequest = {
            "id": id,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_function(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        target: "capo_elementalinference.types.function_target.FunctionTarget",
        request_expression: "capo_elementalinference.types.jsonata_expression.JsonataExpression",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        response_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.function_description.FunctionDescription"
        ] = None,
        event_bridge_delivery: Optional[
            "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_elementalinference.types.create_function_response.CreateFunctionResponse"
    ):
        """<p>Creates a function. A function analyzes a feed by building a request from the feed's media and metadata, optionally sending that request to an Amazon Bedrock model in your account, and publishing the result to the feed's metadata timeline. </p> <p>A function runs only after you attach it to a feed as a function output. For more information, see <a href="https://docs.aws.amazon.com/elemental-inference/latest/userguide/functions.html">Using functions</a> in the <i>AWS Elemental Inference User Guide</i>. </p>

        Args:
            name: <p>A name for this function.</p>
            target: <p>The destination for the request that the function builds.</p>
            request_expression: <p>The JSONata expression that builds the request. Elemental Inference evaluates it against the media object of the feed, which holds the media and metadata that the function asked for. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference evaluates the expression against sample media and rejects it if the evaluation fails. For a Bedrock target, the result must be a JSON object; Elemental Inference doesn't check that the object is a valid request body for the model. The expression can reference at most one of media.transcript, media.contextual, and media.clip. For a passthrough target, it can't reference media.frames. </p>
            response_expression: <p>The JSONata expression that selects what to store. Elemental Inference evaluates it against the result as its root: the model response for a Bedrock target, or the output of the request expression for a passthrough target. If a function has no response expression, Elemental Inference stores the entire result. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference checks that the expression is valid JSONata. For a passthrough target, it also evaluates the request and response expressions together against sample media, and rejects them if they produce no value. </p>
            description: <p>The description of the function. Maximum length: 1,024 characters.</p>
            event_bridge_delivery: <p>Specifies whether Elemental Inference also sends this function's results to Amazon EventBridge. Elemental Inference sends a result only when the result is a JSON object with a top-level <code>eventBridge</code> field set to <code>true</code>. It sends the result, unchanged, as a Function Metadata Generated event to the default event bus in your account, after the result is available from GetMetadata. If the result is larger than 64 KB, the event has <code>resultOmitted</code> set to <code>true</code> in place of the result. </p> <p>Valid values:</p> <ul> <li> <p>ENABLED – Elemental Inference sends each marked result as an event.</p> </li> <li> <p>DISABLED (default) – Elemental Inference doesn't send events.</p> </li> </ul> <p>For a Bedrock target, ENABLED requires a response expression, because the model response itself never has a top-level <code>eventBridge</code> field. A feed output that runs a function with ENABLED can't use a fixedInterval trigger shorter than 4 seconds. </p>
            tags: <p>The tags to associate with this function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_function_request.CreateFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_function_response.CreateFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_function.create_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_elementalinference.types.create_function_request.CreateFunctionRequest",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.create_function_request

            return (
                capo_elementalinference.types.create_function_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_elementalinference.types.create_function_response.CreateFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.create_function_response

            return (
                capo_elementalinference.types.create_function_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "CreateFunction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_elementalinference.types.create_function_request.CreateFunctionRequest = {
            "name": name,
            "target": target,
            "request_expression": request_expression,
        }
        if response_expression is not None:
            input_["response_expression"] = response_expression
        if description is not None:
            input_["description"] = description
        if event_bridge_delivery is not None:
            input_["event_bridge_delivery"] = event_bridge_delivery
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function(
        self,
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the details of a function, including its expressions, the media context that Elemental Inference derived from the request expression, and the feeds that currently reference it. </p>

        Args:
            id: <p>The ID of the function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_elementalinference.types.get_function_response.GetFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.get_function_response

            return capo_elementalinference.types.get_function_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetFunction", redact_output=_redact_output),
        )
        input_: capo_elementalinference.types.get_function_request.GetFunctionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function(
        self,
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
        target: Optional[
            "capo_elementalinference.types.function_target.FunctionTarget"
        ] = None,
        request_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        response_expression: Optional[
            "capo_elementalinference.types.jsonata_expression.JsonataExpression"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.function_description.FunctionDescription"
        ] = None,
        event_bridge_delivery: Optional[
            "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
        ] = None,
    ) -> (
        "capo_elementalinference.types.update_function_response.UpdateFunctionResponse"
    ):
        """<p>Updates a function. Include only the parameters that you want to change; parameters that you don't include aren't affected. Elemental Inference validates the updated expressions in the same way as CreateFunction. </p> <p>While a feed references the function, you can change only its expressions and its description, and you can set eventBridgeDelivery to DISABLED but not to ENABLED. The request expression must keep referencing the same media context, as reported in contextTypes. Changing an expression changes the behavior of every feed that references the function. </p>

        Args:
            id: <p>The ID of the function.</p>
            name: <p>A new name for the function. You can't change the name while the function is referenced by a feed. </p>
            target: <p>A new target for the function. You can't change the target while the function is referenced by a feed. </p>
            request_expression: <p>A new request expression for the function. Elemental Inference derives contextTypes again from the new expression. While a feed references the function, the new expression must reference the same media context as the current one. </p>
            response_expression: <p>A new response expression for the function. To remove the response expression, specify an empty string. A function with a Bedrock target and eventBridgeDelivery set to ENABLED must keep a response expression. </p>
            description: <p>A new description for the function.</p>
            event_bridge_delivery: <p>Specifies whether Elemental Inference also sends this function's marked results to Amazon EventBridge, as described for CreateFunction. If you omit this parameter, the current value is kept. While a feed references the function, you can change this value to DISABLED, but not to ENABLED. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.update_function_request.UpdateFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_function_response.UpdateFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_function.update_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_elementalinference.types.update_function_request.UpdateFunctionRequest",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.update_function_request

            return (
                capo_elementalinference.types.update_function_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_elementalinference.types.update_function_response.UpdateFunctionResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.update_function_response

            return (
                capo_elementalinference.types.update_function_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateFunction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_elementalinference.types.update_function_request.UpdateFunctionRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if target is not None:
            input_["target"] = target
        if request_expression is not None:
            input_["request_expression"] = request_expression
        if response_expression is not None:
            input_["response_expression"] = response_expression
        if description is not None:
            input_["description"] = description
        if event_bridge_delivery is not None:
            input_["event_bridge_delivery"] = event_bridge_delivery

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function(
        self,
        id: "capo_elementalinference.types.function_id.FunctionId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> (
        "capo_elementalinference.types.delete_function_response.DeleteFunctionResponse"
    ):
        """<p>Deletes a function. If any feed still references the function, the operation returns a ConflictException. A disabled function output still references the function. Use GetFunction to find those feeds, then remove the function output from each one with UpdateFeed, or delete the feed, before retrying. </p> <p>Deleting a function doesn't delete the metadata that it has already produced.</p>

        Args:
            id: <p>The ID of the function.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_function

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteFunction")
        )
        input_: capo_elementalinference.types.delete_function_request.DeleteFunctionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_functions(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_functions_response.ListFunctionsResponse":
        """<p>Lists the functions in this account, in this Region. Each entry is a summary. To get the expressions of a function, use GetFunction. </p>

        Args:
            max_results: <p>The maximum number of functions to return in one response. Valid range: 1 to 100. The default is 100. </p>
            next_token: <p>The token that identifies the page of results to return. Use the nextToken value from a previous response. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_functions

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_elementalinference.types.list_functions_response.ListFunctionsResponse",
        ) -> dict[str, Any]:
            import capo_elementalinference.types.list_functions_response

            return (
                capo_elementalinference.types.list_functions_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("ListFunctions", redact_output=_redact_output),
        )
        input_: capo_elementalinference.types.list_functions_request.ListFunctionsRequest = {}
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

    def iter_list_functions(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.function_summary.FunctionSummary]":
        _token = next_token
        while True:
            _response = self.list_functions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("functions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_question_set(
        self,
        name: "capo_elementalinference.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        yes_no: Optional[
            "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
        ] = None,
        yes_no_per_option: Optional[
            "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
        ] = None,
        choose_one: Optional[
            "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
        ] = None,
        tags: Optional["capo_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "capo_elementalinference.types.create_question_set_response.CreateQuestionSetResponse":
        """<p>Creates a question set. Use a question set to get answers about content that's specific to your business, in addition to the built-in contextual metadata classifications. A question set contains your own questions. You ask Elemental Inference these questions about each shot or scene of the media in a contextual metadata output, and Elemental Inference answers each question with scores. To use a question set, reference it in the customQuestions property of the contextual metadata configuration of a feed output. </p> <p>CreateQuestionSet creates the question set with a DRAFT version that contains the questions in the request. To change DRAFT, use UpdateQuestionSet. To publish DRAFT as a numbered version, use CreateQuestionSetVersion. You can't change a published version. </p> <p>A question set can contain the following types of questions. You must specify at least one question. </p> <ul> <li> <p>yesNo – Elemental Inference answers yes or no.</p> </li> <li> <p>yesNoPerOption – Elemental Inference answers yes or no for each option.</p> </li> <li> <p>chooseOne – Elemental Inference chooses one of the options.</p> </li> </ul> <p>A version can contain up to 100 scored items, where each yesNo question, each option of a yesNoPerOption question, and each chooseOne question counts as one item. The name of each question must be unique across all three types. </p>

        Args:
            yes_no: <p>An array of questions that Elemental Inference answers with yes or no. You can specify up to 50 yesNo questions. An empty array is the same as omitting this property. </p>
            yes_no_per_option: <p>An array of questions that you ask about each of their options. Elemental Inference answers yes or no for each option. You can specify up to 10 yesNoPerOption questions. An empty array is the same as omitting this property. </p>
            choose_one: <p>An array of questions that Elemental Inference answers by choosing one of their options. You can specify up to 10 chooseOne questions. An empty array is the same as omitting this property. </p>
            name: <p>A user-friendly name for this question set.</p>
            tags: <p>Optional tags to associate with the question set. You can also add tags later, using TagResource. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_question_set_request.CreateQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_question_set_response.CreateQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_question_set.create_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateQuestionSet")
        )
        input_: capo_elementalinference.types.create_question_set_request.CreateQuestionSetRequest = {
            "name": name
        }
        if yes_no is not None:
            input_["yes_no"] = yes_no
        if yes_no_per_option is not None:
            input_["yes_no_per_option"] = yes_no_per_option
        if choose_one is not None:
            input_["choose_one"] = choose_one
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_question_set(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        question_set_version: Optional[
            "capo_elementalinference.types.question_set_version.QuestionSetVersion"
        ] = None,
    ) -> (
        "capo_elementalinference.types.get_question_set_response.GetQuestionSetResponse"
    ):
        """<p>Retrieves information about the specified question set at one version. By default, GetQuestionSet returns the DRAFT version. To retrieve a published version, specify questionSetVersion. </p>

        Args:
            id: <p>The ID of the question set to retrieve.</p>
            question_set_version: <p>The version of the question set to retrieve: DRAFT or the number of a published version. If you don't specify a version, Elemental Inference returns DRAFT. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.get_question_set_request.GetQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.get_question_set_response.GetQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.get_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.get_question_set.get_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetQuestionSet")
        )
        input_: capo_elementalinference.types.get_question_set_request.GetQuestionSetRequest = {
            "id": id
        }
        if question_set_version is not None:
            input_["question_set_version"] = question_set_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_question_set(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        yes_no: Optional[
            "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
        ] = None,
        yes_no_per_option: Optional[
            "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
        ] = None,
        choose_one: Optional[
            "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
        ] = None,
        name: Optional[
            "capo_elementalinference.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_elementalinference.types.update_question_set_response.UpdateQuestionSetResponse":
        """<p>Updates the DRAFT version of the specified question set. UpdateQuestionSet doesn't create a version and doesn't change published versions. To publish the updated DRAFT as a new version, use CreateQuestionSetVersion. </p> <p>UpdateQuestionSet replaces questions one type at a time. For each of yesNo, yesNoPerOption, and chooseOne: if you omit the array, DRAFT keeps its questions of that type. If you include the array, it replaces all the questions of that type in DRAFT. If you include an empty array, DRAFT no longer has questions of that type. The updated DRAFT must follow the same rules as in CreateQuestionSet, and Elemental Inference applies those rules to the questions that DRAFT keeps as well as to the questions in the request. </p> <p>Feeds that reference the DRAFT version use the updated questions. To make sure that the questions for a feed don't change, reference a published version instead. </p>

        Args:
            id: <p>The ID of the question set to update.</p>
            yes_no: <p>An array of questions that Elemental Inference answers with yes or no, to replace all the yesNo questions in DRAFT. You can specify up to 50 yesNo questions. If not specified, the yesNo questions are not changed. To remove all the yesNo questions, specify an empty array. </p>
            yes_no_per_option: <p>An array of questions that you ask about each of their options, to replace all the yesNoPerOption questions in DRAFT. You can specify up to 10 yesNoPerOption questions. If not specified, the yesNoPerOption questions are not changed. To remove all the yesNoPerOption questions, specify an empty array. </p>
            choose_one: <p>An array of questions that Elemental Inference answers by choosing one of their options, to replace all the chooseOne questions in DRAFT. You can specify up to 10 chooseOne questions. If not specified, the chooseOne questions are not changed. To remove all the chooseOne questions, specify an empty array. </p>
            name: <p>A new name for the question set. If not specified, the name is not changed.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.update_question_set_request.UpdateQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.update_question_set_response.UpdateQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.update_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.update_question_set.update_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateQuestionSet")
        )
        input_: capo_elementalinference.types.update_question_set_request.UpdateQuestionSetRequest = {
            "id": id
        }
        if yes_no is not None:
            input_["yes_no"] = yes_no
        if yes_no_per_option is not None:
            input_["yes_no_per_option"] = yes_no_per_option
        if choose_one is not None:
            input_["choose_one"] = choose_one
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_question_set(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_question_set_response.DeleteQuestionSetResponse":
        """<p>Deletes the specified question set, including its DRAFT version and all its published versions. You can't delete a question set while any feed references any of its versions, including an archived feed. You must first remove the question set from the customQuestions configuration of each feed output that references it, or delete those feeds. </p>

        Args:
            id: <p>The ID of the question set to delete.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_question_set_request.DeleteQuestionSetRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_question_set_response.DeleteQuestionSetResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_question_set

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_question_set.delete_question_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteQuestionSet")
        )
        input_: capo_elementalinference.types.delete_question_set_request.DeleteQuestionSetRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_question_sets(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_question_sets_response.ListQuestionSetsResponse":
        """<p>Lists the question sets in your account. The response doesn't include the questions in each question set. To retrieve them, use GetQuestionSet. </p>

        Args:
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_question_sets_request.ListQuestionSetsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_question_sets_response.ListQuestionSetsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_question_sets

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_question_sets.list_question_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListQuestionSets")
        )
        input_: capo_elementalinference.types.list_question_sets_request.ListQuestionSetsRequest = {}
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

    def iter_list_question_sets(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.question_set_summary.QuestionSetSummary]":
        _token = next_token
        while True:
            _response = self.list_question_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("question_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_question_set_version(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        sha256: Optional[
            "capo_elementalinference.types.question_set_sha256.QuestionSetSha256"
        ] = None,
        description: Optional[
            "capo_elementalinference.types.question_set_version_description.QuestionSetVersionDescription"
        ] = None,
    ) -> "capo_elementalinference.types.create_question_set_version_response.CreateQuestionSetVersionResponse":
        """<p>Publishes the DRAFT version of the specified question set as a new version. The new version has the same name and questions as DRAFT, and you can't change it. DRAFT doesn't change, so you can continue to update it. </p> <p>Version numbers start at 1, and each new version has the next number. Elemental Inference never reuses a version number, even after you delete that version. </p> <p>If DRAFT hasn't changed since the latest published version, Elemental Inference doesn't create a version. Instead, it returns the latest version. A change to the name of the question set counts as a change to DRAFT. </p> <p>A question set can have a limited number of versions. If the question set already has the maximum number of versions, Elemental Inference returns ServiceQuotaExceededException. To free space for a new version, delete a version that you no longer need, or create a new question set. </p>

        Args:
            id: <p>The ID of the question set whose DRAFT version you want to publish.</p>
            sha256: <p>The SHA-256 hash of the DRAFT version that you want to publish, as returned by GetQuestionSet or UpdateQuestionSet. If you specify this value, Elemental Inference publishes DRAFT only if its current hash matches. If it doesn't match, because DRAFT changed after you retrieved it, the request fails with ConflictException. </p> <p>If you don't specify this value, Elemental Inference publishes DRAFT as it is when it receives the request. </p>
            description: <p>A description of the new version. You can't change the description after Elemental Inference publishes the version. If DRAFT hasn't changed since the latest version, Elemental Inference ignores this value and returns the latest version with its existing description. </p> <p>The description can be up to 256 characters. It can contain the letters A-Z and a-z, the digits 0-9, underscores, spaces, and the following characters: <code>- . ' , @ : ;</code>. </p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase. </p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.create_question_set_version_request.CreateQuestionSetVersionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.create_question_set_version_response.CreateQuestionSetVersionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.create_question_set_version

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.create_question_set_version.create_question_set_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateQuestionSetVersion")
        )
        input_: capo_elementalinference.types.create_question_set_version_request.CreateQuestionSetVersionRequest = {
            "id": id
        }
        if sha256 is not None:
            input_["sha256"] = sha256
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_question_set_version(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        question_set_version: "capo_elementalinference.types.published_question_set_version.PublishedQuestionSetVersion",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "capo_elementalinference.types.delete_question_set_version_response.DeleteQuestionSetVersionResponse":
        """<p>Deletes a published version of the specified question set. You can't delete a version while a feed references it, including an archived feed. You can't restore a deleted version, and Elemental Inference doesn't reuse its number. </p> <p>You can't delete the DRAFT version on its own. To delete DRAFT, delete the question set by using DeleteQuestionSet. </p> <p>Deleting a version doesn't change the latestVersion of the question set, even if you delete the highest version. </p>

        Args:
            id: <p>The ID of the question set that contains the version.</p>
            question_set_version: <p>The number of the published version to delete. You can't specify DRAFT.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.delete_question_set_version_request.DeleteQuestionSetVersionRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.delete_question_set_version_response.DeleteQuestionSetVersionResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.delete_question_set_version

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.delete_question_set_version.delete_question_set_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteQuestionSetVersion")
        )
        input_: capo_elementalinference.types.delete_question_set_version_request.DeleteQuestionSetVersionRequest = {
            "id": id,
            "question_set_version": question_set_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_question_set_versions(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_elementalinference.types.list_question_set_versions_response.ListQuestionSetVersionsResponse":
        """<p>Lists the versions of the specified question set. The list starts with the DRAFT version, followed by the published versions from the highest version number to the lowest. The list doesn't include deleted versions. </p> <p>The response doesn't include the questions in each version. To retrieve them, use GetQuestionSet and specify questionSetVersion. </p>

        Args:
            id: <p>The ID of the question set whose versions you want to list.</p>
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>

        Raises:
            capo_elementalinference.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support. </p>
            capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the action doesn't exist.</p>
            capo_elementalinference.errors.too_many_request_exception.TooManyRequestException: <p>The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying. </p>
            capo_elementalinference.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying. </p>
            capo_elementalinference.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elementalinference.types.list_question_set_versions_request.ListQuestionSetVersionsRequest]",
        ) -> OperationResponse[
            "capo_elementalinference.types.list_question_set_versions_response.ListQuestionSetVersionsResponse"
        ]:
            import capo_elementalinference._operations.elemental_inference.list_question_set_versions

            output, http_response = (
                capo_elementalinference._operations.elemental_inference.list_question_set_versions.list_question_set_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListQuestionSetVersions")
        )
        input_: capo_elementalinference.types.list_question_set_versions_request.ListQuestionSetVersionsRequest = {
            "id": id
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

    def iter_list_question_set_versions(
        self,
        id: "capo_elementalinference.types.question_set_id.QuestionSetId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_elementalinference.types.question_set_version_summary.QuestionSetVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_question_set_versions(
                id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

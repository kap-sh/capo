"""Generated from Smithy shape ``com.amazonaws.freetier#AWSFreeTierService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_freetier._auth._signers
import capo_freetier._auth._sigv4
from capo_freetier._auth._identity import Credentials
from capo_freetier._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_freetier._auth._zapros_handler import AuthMiddleware
from capo_freetier._pagination import resolve_path as _resolve_path
from capo_freetier._services._aws_config import aws_config
from capo_freetier._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_freetier.types.account_plan_type
    import capo_freetier.types.activity_id
    import capo_freetier.types.activity_summary
    import capo_freetier.types.expression
    import capo_freetier.types.filter_activity_statuses
    import capo_freetier.types.free_tier_usage
    import capo_freetier.types.get_account_activity_request
    import capo_freetier.types.get_account_activity_response
    import capo_freetier.types.get_account_plan_state_request
    import capo_freetier.types.get_account_plan_state_response
    import capo_freetier.types.get_free_tier_usage_request
    import capo_freetier.types.get_free_tier_usage_response
    import capo_freetier.types.language_code
    import capo_freetier.types.list_account_activities_request
    import capo_freetier.types.list_account_activities_response
    import capo_freetier.types.max_results
    import capo_freetier.types.next_page_token
    import capo_freetier.types.upgrade_account_plan_request
    import capo_freetier.types.upgrade_account_plan_response


class FreeTierClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class FreeTierClient:
    """A client for the ``FreeTier`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = FreeTierClientConfig(
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
        self, config_overrides: Optional[FreeTierClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: FreeTierClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def get_account_activity(
        self,
        activity_id: "capo_freetier.types.activity_id.ActivityId",
        *,
        config_overrides: Optional[FreeTierClientConfig] = None,
        language_code: Optional[
            "capo_freetier.types.language_code.LanguageCode"
        ] = None,
    ) -> "capo_freetier.types.get_account_activity_response.GetAccountActivityResponse":
        """<p> Returns a specific activity record that is available to the customer. </p>

        Args:
            activity_id: <p> A unique identifier that identifies the activity. </p>
            language_code: <p> The language code used to return translated title and description fields. </p>

        Raises:
            capo_freetier.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_freetier.errors.resource_not_found_exception.ResourceNotFoundException: <p> This exception is thrown when the requested resource cannot be found. </p>
            capo_freetier.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_freetier.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_freetier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Fetching an Account activity by id

            >>> client.get_account_activity(activity_id='d622f48bf4014286a2686ab10cacfb2e', language_code='en-US')
        """

        def _handler(
            req: "OperationRequest[capo_freetier.types.get_account_activity_request.GetAccountActivityRequest]",
        ) -> OperationResponse[
            "capo_freetier.types.get_account_activity_response.GetAccountActivityResponse"
        ]:
            import capo_freetier._operations.aws_free_tier_service.get_account_activity

            output, http_response = (
                capo_freetier._operations.aws_free_tier_service.get_account_activity.get_account_activity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_freetier.types.get_account_activity_request.GetAccountActivityRequest = {
            "activity_id": activity_id
        }
        if language_code is not None:
            input_["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_plan_state(
        self, *, config_overrides: Optional[FreeTierClientConfig] = None
    ) -> "capo_freetier.types.get_account_plan_state_response.GetAccountPlanStateResponse":
        """<p> This returns all of the information related to the state of the account plan related to Free Tier. </p>

        Raises:
            capo_freetier.errors.access_denied_exception.AccessDeniedException: <p> You don't have sufficient access to perform this action. </p>
            capo_freetier.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_freetier.errors.resource_not_found_exception.ResourceNotFoundException: <p> This exception is thrown when the requested resource cannot be found. </p>
            capo_freetier.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_freetier.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_freetier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Fetching account plan state by id

            >>> client.get_account_plan_state()
            Attempt to fetch account plan state by id with insufficient permissions

            >>> client.get_account_plan_state()
            Internal service error

            >>> client.get_account_plan_state()
            Attempt to fetch plan state by id for an account without account plan

            >>> client.get_account_plan_state()
            Request rate exceeds limits

            >>> client.get_account_plan_state()
        """

        def _handler(
            req: "OperationRequest[capo_freetier.types.get_account_plan_state_request.GetAccountPlanStateRequest]",
        ) -> OperationResponse[
            "capo_freetier.types.get_account_plan_state_response.GetAccountPlanStateResponse"
        ]:
            import capo_freetier._operations.aws_free_tier_service.get_account_plan_state

            output, http_response = (
                capo_freetier._operations.aws_free_tier_service.get_account_plan_state.get_account_plan_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_freetier.types.get_account_plan_state_request.GetAccountPlanStateRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_free_tier_usage(
        self,
        *,
        config_overrides: Optional[FreeTierClientConfig] = None,
        filter: Optional["capo_freetier.types.expression.Expression"] = None,
        max_results: Optional["capo_freetier.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_freetier.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_freetier.types.get_free_tier_usage_response.GetFreeTierUsageResponse":
        """<p>Returns a list of all Free Tier usage objects that match your filters.</p>

        Args:
            filter: <p>An expression that specifies the conditions that you want each <code>FreeTierUsage</code> object to meet.</p>
            max_results: <p>The maximum number of results to return in the response. <code>MaxResults</code> means that there can be up to the specified number of values, but there might be fewer results based on your filters.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>

        Raises:
            capo_freetier.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_freetier.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_freetier.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_freetier.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_freetier.types.get_free_tier_usage_request.GetFreeTierUsageRequest]",
        ) -> OperationResponse[
            "capo_freetier.types.get_free_tier_usage_response.GetFreeTierUsageResponse"
        ]:
            import capo_freetier._operations.aws_free_tier_service.get_free_tier_usage

            output, http_response = (
                capo_freetier._operations.aws_free_tier_service.get_free_tier_usage.get_free_tier_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_freetier.types.get_free_tier_usage_request.GetFreeTierUsageRequest = {}
        if filter is not None:
            input_["filter"] = filter
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

    def iter_get_free_tier_usage(
        self,
        *,
        config_overrides: Optional[FreeTierClientConfig] = None,
        filter: Optional["capo_freetier.types.expression.Expression"] = None,
        max_results: Optional["capo_freetier.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_freetier.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "Iterator[capo_freetier.types.free_tier_usage.FreeTierUsage]":
        _token = next_token
        while True:
            _response = self.get_free_tier_usage(
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("free_tier_usages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_account_activities(
        self,
        *,
        config_overrides: Optional[FreeTierClientConfig] = None,
        filter_activity_statuses: Optional[
            "capo_freetier.types.filter_activity_statuses.FilterActivityStatuses"
        ] = None,
        next_token: Optional[
            "capo_freetier.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_freetier.types.max_results.MaxResults"] = None,
        language_code: Optional[
            "capo_freetier.types.language_code.LanguageCode"
        ] = None,
    ) -> "capo_freetier.types.list_account_activities_response.ListAccountActivitiesResponse":
        """<p> Returns a list of activities that are available. This operation supports pagination and filtering by status. </p>

        Args:
            filter_activity_statuses: <p> The activity status filter. This field can be used to filter the response by activities status. </p>
            next_token: <p> A token from a previous paginated response. If this is specified, the response includes records beginning from this token (inclusive), up to the number specified by <code>maxResults</code>. </p>
            max_results: <p> The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. </p>
            language_code: <p> The language code used to return translated titles. </p>

        Raises:
            capo_freetier.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_freetier.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_freetier.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_freetier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Fetching a page of completed activities

            >>> client.list_account_activities(filter_activity_statuses=['COMPLETED'], max_results=1, language_code='en-US')
        """

        def _handler(
            req: "OperationRequest[capo_freetier.types.list_account_activities_request.ListAccountActivitiesRequest]",
        ) -> OperationResponse[
            "capo_freetier.types.list_account_activities_response.ListAccountActivitiesResponse"
        ]:
            import capo_freetier._operations.aws_free_tier_service.list_account_activities

            output, http_response = (
                capo_freetier._operations.aws_free_tier_service.list_account_activities.list_account_activities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_freetier.types.list_account_activities_request.ListAccountActivitiesRequest = {}
        if filter_activity_statuses is not None:
            input_["filter_activity_statuses"] = filter_activity_statuses
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if language_code is not None:
            input_["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_account_activities(
        self,
        *,
        config_overrides: Optional[FreeTierClientConfig] = None,
        filter_activity_statuses: Optional[
            "capo_freetier.types.filter_activity_statuses.FilterActivityStatuses"
        ] = None,
        next_token: Optional[
            "capo_freetier.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_freetier.types.max_results.MaxResults"] = None,
        language_code: Optional[
            "capo_freetier.types.language_code.LanguageCode"
        ] = None,
    ) -> "Iterator[capo_freetier.types.activity_summary.ActivitySummary]":
        _token = next_token
        while True:
            _response = self.list_account_activities(
                config_overrides=config_overrides,
                filter_activity_statuses=filter_activity_statuses,
                next_token=_token,
                max_results=max_results,
                language_code=language_code,
            )
            _page = _resolve_path(_response, ("activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def upgrade_account_plan(
        self,
        account_plan_type: "capo_freetier.types.account_plan_type.AccountPlanType",
        *,
        config_overrides: Optional[FreeTierClientConfig] = None,
    ) -> "capo_freetier.types.upgrade_account_plan_response.UpgradeAccountPlanResponse":
        """<p> The account plan type for the Amazon Web Services account. </p>

        Args:
            account_plan_type: <p> The target account plan type. This makes it explicit about the change and latest value of the <code>accountPlanType</code>. </p>

        Raises:
            capo_freetier.errors.access_denied_exception.AccessDeniedException: <p> You don't have sufficient access to perform this action. </p>
            capo_freetier.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_freetier.errors.resource_not_found_exception.ResourceNotFoundException: <p> This exception is thrown when the requested resource cannot be found. </p>
            capo_freetier.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_freetier.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_freetier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Upgrading an account plan to PAID

            >>> client.upgrade_account_plan(account_plan_type='PAID')
            Attempt to upgrade an account with insufficient permissions

            >>> client.upgrade_account_plan(account_plan_type='PAID')
            Attempt to downgrade an account from PAID to FREE

            >>> client.upgrade_account_plan(account_plan_type='FREE')
            Internal service error

            >>> client.upgrade_account_plan(account_plan_type='PAID')
            Attempt to upgrade a non-existent account plan

            >>> client.upgrade_account_plan(account_plan_type='PAID')
            Request rate exceeds limits

            >>> client.upgrade_account_plan(account_plan_type='PAID')
        """

        def _handler(
            req: "OperationRequest[capo_freetier.types.upgrade_account_plan_request.UpgradeAccountPlanRequest]",
        ) -> OperationResponse[
            "capo_freetier.types.upgrade_account_plan_response.UpgradeAccountPlanResponse"
        ]:
            import capo_freetier._operations.aws_free_tier_service.upgrade_account_plan

            output, http_response = (
                capo_freetier._operations.aws_free_tier_service.upgrade_account_plan.upgrade_account_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_freetier.types.upgrade_account_plan_request.UpgradeAccountPlanRequest = {
            "account_plan_type": account_plan_type
        }

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

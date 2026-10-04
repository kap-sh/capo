"""Generated from Smithy shape ``com.amazonaws.health#AWSHealth_20160804``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_health._auth._signers
import capo_health._auth._sigv4
from capo_health._auth._identity import Credentials
from capo_health._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_health._auth._zapros_handler import AuthMiddleware
from capo_health._pagination import resolve_path as _resolve_path
from capo_health._services._aws_config import aaws_config
from capo_health._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_health.types.account_id
    import capo_health.types.affected_entity
    import capo_health.types.describe_affected_accounts_for_organization_request
    import capo_health.types.describe_affected_accounts_for_organization_response
    import capo_health.types.describe_affected_entities_for_organization_request
    import capo_health.types.describe_affected_entities_for_organization_response
    import capo_health.types.describe_affected_entities_request
    import capo_health.types.describe_affected_entities_response
    import capo_health.types.describe_entity_aggregates_for_organization_request
    import capo_health.types.describe_entity_aggregates_for_organization_response
    import capo_health.types.describe_entity_aggregates_request
    import capo_health.types.describe_entity_aggregates_response
    import capo_health.types.describe_event_aggregates_request
    import capo_health.types.describe_event_aggregates_response
    import capo_health.types.describe_event_details_for_organization_request
    import capo_health.types.describe_event_details_for_organization_response
    import capo_health.types.describe_event_details_request
    import capo_health.types.describe_event_details_response
    import capo_health.types.describe_event_types_request
    import capo_health.types.describe_event_types_response
    import capo_health.types.describe_events_for_organization_request
    import capo_health.types.describe_events_for_organization_response
    import capo_health.types.describe_events_request
    import capo_health.types.describe_events_response
    import capo_health.types.describe_health_service_status_for_organization_response
    import capo_health.types.describe_service_lifecycle_request
    import capo_health.types.describe_service_lifecycle_response
    import capo_health.types.entity_filter
    import capo_health.types.event
    import capo_health.types.event_aggregate
    import capo_health.types.event_aggregate_field
    import capo_health.types.event_arn
    import capo_health.types.event_arn_list
    import capo_health.types.event_arns_list
    import capo_health.types.event_filter
    import capo_health.types.event_type
    import capo_health.types.event_type_filter
    import capo_health.types.lifecycle_max_results
    import capo_health.types.locale
    import capo_health.types.max_results
    import capo_health.types.max_results_lower_range
    import capo_health.types.next_token
    import capo_health.types.organization_account_ids_list
    import capo_health.types.organization_entity_account_filters_list
    import capo_health.types.organization_entity_filters_list
    import capo_health.types.organization_event
    import capo_health.types.organization_event_arns_list
    import capo_health.types.organization_event_detail_filters_list
    import capo_health.types.organization_event_filter
    import capo_health.types.service_lifecycle
    import capo_health.types.service_lifecycle_filter


class AsyncHealthClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncHealthClient:
    """A client for the ``Health`` service.

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
        self._config = AsyncHealthClientConfig(
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
        self, config_overrides: Optional[AsyncHealthClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncHealthClientConfig = config_overrides or {}
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

    async def describe_affected_accounts_for_organization(
        self,
        event_arn: "capo_health.types.event_arn.eventArn",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional["capo_health.types.max_results.maxResults"] = None,
    ) -> "capo_health.types.describe_affected_accounts_for_organization_response.DescribeAffectedAccountsForOrganizationResponse":
        """<p>Returns a list of accounts in the organization from Organizations that are affected by the provided event. For more information about the different types of Health events, see <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html">Event</a>. </p> <p>Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html">EnableHealthServiceAccessForOrganization</a> operation from your organization's management account.</p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the next request to return more results.</p> </note>

        Args:
            event_arn: <p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>
            max_results: <p>The maximum number of items to return in one batch, between 10 and 100, inclusive.</p>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_affected_accounts_for_organization_request.DescribeAffectedAccountsForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_affected_accounts_for_organization_response.DescribeAffectedAccountsForOrganizationResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_affected_accounts_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_affected_accounts_for_organization.async_describe_affected_accounts_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_affected_accounts_for_organization_request.DescribeAffectedAccountsForOrganizationRequest = {
            "event_arn": event_arn
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

    async def iter_describe_affected_accounts_for_organization(
        self,
        event_arn: "capo_health.types.event_arn.eventArn",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional["capo_health.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_health.types.account_id.accountId]":
        _token = next_token
        while True:
            _response = await self.describe_affected_accounts_for_organization(
                event_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("affected_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_affected_entities(
        self,
        filter: "capo_health.types.entity_filter.EntityFilter",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
    ) -> "capo_health.types.describe_affected_entities_response.DescribeAffectedEntitiesResponse":
        """<p>Returns a list of entities that have been affected by the specified events, based on the specified filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the Amazon Web Services service. Events that have impact beyond that of the affected entities, or where the extent of impact is unknown, include at least one entity indicating this.</p> <p>At least one event ARN is required.</p> <note> <ul> <li> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the next request to return more results.</p> </li> <li> <p>This operation supports resource-level permissions. You can use this operation to allow or deny access to specific Health events. For more information, see <a href="https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions">Resource- and action-based conditions</a> in the <i>Health User Guide</i>.</p> </li> </ul> </note>

        Args:
            filter: <p>Values to narrow the results returned. At least one event ARN is required.</p>
            locale: <p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>
            max_results: <p>The maximum number of items to return in one batch, between 1 and 100, inclusive.</p>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.unsupported_locale.UnsupportedLocale: <p>The specified locale is not supported.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_affected_entities_request.DescribeAffectedEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_affected_entities_response.DescribeAffectedEntitiesResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_affected_entities

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_affected_entities.async_describe_affected_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_affected_entities_request.DescribeAffectedEntitiesRequest = {
            "filter": filter
        }
        if locale is not None:
            input_["locale"] = locale
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

    async def iter_describe_affected_entities(
        self,
        filter: "capo_health.types.entity_filter.EntityFilter",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
    ) -> "AsyncIterator[capo_health.types.affected_entity.AffectedEntity]":
        _token = next_token
        while True:
            _response = await self.describe_affected_entities(
                filter,
                config_overrides=config_overrides,
                locale=locale,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_affected_entities_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        organization_entity_filters: Optional[
            "capo_health.types.organization_entity_filters_list.OrganizationEntityFiltersList"
        ] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
        organization_entity_account_filters: Optional[
            "capo_health.types.organization_entity_account_filters_list.OrganizationEntityAccountFiltersList"
        ] = None,
    ) -> "capo_health.types.describe_affected_entities_for_organization_response.DescribeAffectedEntitiesForOrganizationResponse":
        """<p>Returns a list of entities that have been affected by one or more events for one or more accounts in your organization in Organizations, based on the filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the Amazon Web Services service.</p> <p>At least one event Amazon Resource Name (ARN) and account ID are required.</p> <p>Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html">EnableHealthServiceAccessForOrganization</a> operation from your organization's management account.</p> <note> <ul> <li> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the next request to return more results.</p> </li> <li> <p>This operation doesn't support resource-level permissions. You can't use this operation to allow or deny access to specific Health events. For more information, see <a href="https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions">Resource- and action-based conditions</a> in the <i>Health User Guide</i>.</p> </li> </ul> </note>

        Args:
            organization_entity_filters: <p>A JSON set of elements including the <code>awsAccountId</code> and the <code>eventArn</code>.</p>
            locale: <p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>
            max_results: <p>The maximum number of items to return in one batch, between 1 and 100, inclusive.</p>
            organization_entity_account_filters: <p>A JSON set of elements including the <code>awsAccountId</code>, <code>eventArn</code> and a set of <code>statusCodes</code>.</p>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.unsupported_locale.UnsupportedLocale: <p>The specified locale is not supported.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_affected_entities_for_organization_request.DescribeAffectedEntitiesForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_affected_entities_for_organization_response.DescribeAffectedEntitiesForOrganizationResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_affected_entities_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_affected_entities_for_organization.async_describe_affected_entities_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_affected_entities_for_organization_request.DescribeAffectedEntitiesForOrganizationRequest = {}
        if organization_entity_filters is not None:
            input_["organization_entity_filters"] = organization_entity_filters
        if locale is not None:
            input_["locale"] = locale
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if organization_entity_account_filters is not None:
            input_["organization_entity_account_filters"] = (
                organization_entity_account_filters
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_affected_entities_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        organization_entity_filters: Optional[
            "capo_health.types.organization_entity_filters_list.OrganizationEntityFiltersList"
        ] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
        organization_entity_account_filters: Optional[
            "capo_health.types.organization_entity_account_filters_list.OrganizationEntityAccountFiltersList"
        ] = None,
    ) -> "AsyncIterator[capo_health.types.affected_entity.AffectedEntity]":
        _token = next_token
        while True:
            _response = await self.describe_affected_entities_for_organization(
                config_overrides=config_overrides,
                organization_entity_filters=organization_entity_filters,
                locale=locale,
                next_token=_token,
                max_results=max_results,
                organization_entity_account_filters=organization_entity_account_filters,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_entity_aggregates(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        event_arns: Optional["capo_health.types.event_arns_list.EventArnsList"] = None,
    ) -> "capo_health.types.describe_entity_aggregates_response.DescribeEntityAggregatesResponse":
        """<p>Returns the number of entities that are affected by each of the specified events.</p>

        Args:
            event_arns: <p>A list of event ARNs (unique identifiers). For example: <code>"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"</code> </p>

        Raises:
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_entity_aggregates_request.DescribeEntityAggregatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_entity_aggregates_response.DescribeEntityAggregatesResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_entity_aggregates

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_entity_aggregates.async_describe_entity_aggregates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_entity_aggregates_request.DescribeEntityAggregatesRequest = {}
        if event_arns is not None:
            input_["event_arns"] = event_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_entity_aggregates_for_organization(
        self,
        event_arns: "capo_health.types.organization_event_arns_list.OrganizationEventArnsList",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        aws_account_ids: Optional[
            "capo_health.types.organization_account_ids_list.OrganizationAccountIdsList"
        ] = None,
    ) -> "capo_health.types.describe_entity_aggregates_for_organization_response.DescribeEntityAggregatesForOrganizationResponse":
        """<p>Returns a list of entity aggregates for your Organizations that are affected by each of the specified events.</p>

        Args:
            event_arns: <p>A list of event ARNs (unique identifiers). For example: <code>"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"</code> </p>
            aws_account_ids: <p>A list of 12-digit Amazon Web Services account numbers that contains the affected entities.</p>

        Raises:
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_entity_aggregates_for_organization_request.DescribeEntityAggregatesForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_entity_aggregates_for_organization_response.DescribeEntityAggregatesForOrganizationResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_entity_aggregates_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_entity_aggregates_for_organization.async_describe_entity_aggregates_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_entity_aggregates_for_organization_request.DescribeEntityAggregatesForOrganizationRequest = {
            "event_arns": event_arns
        }
        if aws_account_ids is not None:
            input_["aws_account_ids"] = aws_account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_event_aggregates(
        self,
        aggregate_field: "capo_health.types.event_aggregate_field.eventAggregateField",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional["capo_health.types.event_filter.EventFilter"] = None,
        max_results: Optional["capo_health.types.max_results.maxResults"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
    ) -> "capo_health.types.describe_event_aggregates_response.DescribeEventAggregatesResponse":
        """<p>Returns the number of events of each event type (issue, scheduled change, and account notification). If no filter is specified, the counts of all events in each category are returned.</p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the next request to return more results.</p> </note>

        Args:
            filter: <p>Values to narrow the results returned.</p>
            aggregate_field: <p>The only currently supported value is <code>eventTypeCategory</code>.</p>
            max_results: <p>The maximum number of items to return in one batch, between 10 and 100, inclusive.</p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_event_aggregates_request.DescribeEventAggregatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_event_aggregates_response.DescribeEventAggregatesResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_event_aggregates

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_event_aggregates.async_describe_event_aggregates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_event_aggregates_request.DescribeEventAggregatesRequest = {
            "aggregate_field": aggregate_field
        }
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_describe_event_aggregates(
        self,
        aggregate_field: "capo_health.types.event_aggregate_field.eventAggregateField",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional["capo_health.types.event_filter.EventFilter"] = None,
        max_results: Optional["capo_health.types.max_results.maxResults"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
    ) -> "AsyncIterator[capo_health.types.event_aggregate.EventAggregate]":
        _token = next_token
        while True:
            _response = await self.describe_event_aggregates(
                aggregate_field,
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("event_aggregates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_event_details(
        self,
        event_arns: "capo_health.types.event_arn_list.eventArnList",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
    ) -> (
        "capo_health.types.describe_event_details_response.DescribeEventDetailsResponse"
    ):
        """<p>Returns detailed information about one or more specified events. Information includes standard event data (Amazon Web Services Region, service, and so on, as returned by <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html">DescribeEvents</a>), a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included. To retrieve the entities, use the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html">DescribeAffectedEntities</a> operation.</p> <p>If a specified event can't be retrieved, an error message is returned for that event.</p> <note> <p>This operation supports resource-level permissions. You can use this operation to allow or deny access to specific Health events. For more information, see <a href="https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions">Resource- and action-based conditions</a> in the <i>Health User Guide</i>.</p> </note>

        Args:
            event_arns: <p>A list of event ARNs (unique identifiers). For example: <code>"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"</code> </p>
            locale: <p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>

        Raises:
            capo_health.errors.unsupported_locale.UnsupportedLocale: <p>The specified locale is not supported.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_event_details_request.DescribeEventDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_event_details_response.DescribeEventDetailsResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_event_details

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_event_details.async_describe_event_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_event_details_request.DescribeEventDetailsRequest = {
            "event_arns": event_arns
        }
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_event_details_for_organization(
        self,
        organization_event_detail_filters: "capo_health.types.organization_event_detail_filters_list.OrganizationEventDetailFiltersList",
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
    ) -> "capo_health.types.describe_event_details_for_organization_response.DescribeEventDetailsForOrganizationResponse":
        """<p>Returns detailed information about one or more specified events for one or more Amazon Web Services accounts in your organization. This information includes standard event data (such as the Amazon Web Services Region and service), an event description, and (depending on the event) possible metadata. This operation doesn't return affected entities, such as the resources related to the event. To return affected entities, use the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html">DescribeAffectedEntitiesForOrganization</a> operation.</p> <note> <p>Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html">EnableHealthServiceAccessForOrganization</a> operation from your organization's management account.</p> </note> <p>When you call the <code>DescribeEventDetailsForOrganization</code> operation, specify the <code>organizationEventDetailFilters</code> object in the request. Depending on the Health event type, note the following differences:</p> <ul> <li> <p>To return event details for a public event, you must specify a null value for the <code>awsAccountId</code> parameter. If you specify an account ID for a public event, Health returns an error message because public events aren't specific to an account.</p> </li> <li> <p>To return event details for an event that is specific to an account in your organization, you must specify the <code>awsAccountId</code> parameter in the request. If you don't specify an account ID, Health returns an error message because the event is specific to an account in your organization. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html">Event</a>.</p> <note> <p>This operation doesn't support resource-level permissions. You can't use this operation to allow or deny access to specific Health events. For more information, see <a href="https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions">Resource- and action-based conditions</a> in the <i>Health User Guide</i>.</p> </note>

        Args:
            organization_event_detail_filters: <p>A set of JSON elements that includes the <code>awsAccountId</code> and the <code>eventArn</code>.</p>
            locale: <p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>

        Raises:
            capo_health.errors.unsupported_locale.UnsupportedLocale: <p>The specified locale is not supported.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_event_details_for_organization_request.DescribeEventDetailsForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_event_details_for_organization_response.DescribeEventDetailsForOrganizationResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_event_details_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_event_details_for_organization.async_describe_event_details_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_event_details_for_organization_request.DescribeEventDetailsForOrganizationRequest = {
            "organization_event_detail_filters": organization_event_detail_filters
        }
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_events(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional["capo_health.types.event_filter.EventFilter"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
    ) -> "capo_health.types.describe_events_response.DescribeEventsResponse":
        """<p> Returns information about events that meet the specified filter criteria. Events are returned in a summary form and do not include the detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html">DescribeEventDetails</a> and <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html">DescribeAffectedEntities</a> operations.</p> <p>If no filter criteria are specified, all events are returned. Results are sorted by <code>lastModifiedTime</code>, starting with the most recent event.</p> <note> <ul> <li> <p>When you call the <code>DescribeEvents</code> operation and specify an entity for the <code>entityValues</code> parameter, Health might return public events that aren't specific to that resource. For example, if you call <code>DescribeEvents</code> and specify an ID for an Amazon Elastic Compute Cloud (Amazon EC2) instance, Health might return events that aren't specific to that resource or service. To get events that are specific to a service, use the <code>services</code> parameter in the <code>filter</code> object. For more information, see <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html">Event</a>.</p> </li> <li> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the next request to return more results.</p> </li> </ul> </note>

        Args:
            filter: <p>Values to narrow the results returned.</p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>
            max_results: <p>The maximum number of items to return in one batch, between 1 and 100, inclusive.</p>
            locale: <p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.unsupported_locale.UnsupportedLocale: <p>The specified locale is not supported.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_events_request.DescribeEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_events_response.DescribeEventsResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_events

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_events_request.DescribeEventsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_events(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional["capo_health.types.event_filter.EventFilter"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
    ) -> "AsyncIterator[capo_health.types.event.Event]":
        _token = next_token
        while True:
            _response = await self.describe_events(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
                locale=locale,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_events_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional[
            "capo_health.types.organization_event_filter.OrganizationEventFilter"
        ] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
    ) -> "capo_health.types.describe_events_for_organization_response.DescribeEventsForOrganizationResponse":
        """<p>Returns information about events across your organization in Organizations. You can use the<code>filters</code> parameter to specify the events that you want to return. Events are returned in a summary form and don't include the affected accounts, detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the following operations:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedAccountsForOrganization.html">DescribeAffectedAccountsForOrganization</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html">DescribeEventDetailsForOrganization</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html">DescribeAffectedEntitiesForOrganization</a> </p> </li> </ul> <p>If you don't specify a <code>filter</code>, the <code>DescribeEventsForOrganizations</code> returns all events across your organization. Results are sorted by <code>lastModifiedTime</code>, starting with the most recent event. </p> <p>For more information about the different types of Health events, see <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html">Event</a>.</p> <p>Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html">EnableHealthServiceAccessForOrganization</a> operation from your organization's management account.</p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the next request to return more results.</p> </note>

        Args:
            filter: <p>Values to narrow the results returned.</p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>
            max_results: <p>The maximum number of items to return in one batch, between 1 and 100, inclusive.</p>
            locale: <p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.unsupported_locale.UnsupportedLocale: <p>The specified locale is not supported.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_events_for_organization_request.DescribeEventsForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_events_for_organization_response.DescribeEventsForOrganizationResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_events_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_events_for_organization.async_describe_events_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_events_for_organization_request.DescribeEventsForOrganizationRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_events_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional[
            "capo_health.types.organization_event_filter.OrganizationEventFilter"
        ] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.max_results_lower_range.maxResultsLowerRange"
        ] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
    ) -> "AsyncIterator[capo_health.types.organization_event.OrganizationEvent]":
        _token = next_token
        while True:
            _response = await self.describe_events_for_organization(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
                locale=locale,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_event_types(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional["capo_health.types.event_type_filter.EventTypeFilter"] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional["capo_health.types.max_results.maxResults"] = None,
    ) -> "capo_health.types.describe_event_types_response.DescribeEventTypesResponse":
        """<p>Returns the event types that meet the specified filter criteria. You can use this API operation to find information about the Health event, such as the category, Amazon Web Services service, and event code. The metadata for each event appears in the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EventType.html">EventType</a> object. </p> <p>If you don't specify a filter criteria, the API operation returns all event types, in no particular order. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the next request to return more results.</p> </note>

        Args:
            filter: <p>Values to narrow the results returned.</p>
            locale: <p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>
            max_results: <p>The maximum number of items to return in one batch, between 10 and 100, inclusive.</p> <note> <p>If you don't specify the <code>maxResults</code> parameter, this operation returns a maximum of 30 items by default.</p> </note>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.unsupported_locale.UnsupportedLocale: <p>The specified locale is not supported.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_event_types_request.DescribeEventTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_event_types_response.DescribeEventTypesResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_event_types

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_event_types.async_describe_event_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_event_types_request.DescribeEventTypesRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if locale is not None:
            input_["locale"] = locale
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

    async def iter_describe_event_types(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional["capo_health.types.event_type_filter.EventTypeFilter"] = None,
        locale: Optional["capo_health.types.locale.locale"] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional["capo_health.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_health.types.event_type.EventType]":
        _token = next_token
        while True:
            _response = await self.describe_event_types(
                config_overrides=config_overrides,
                filter=filter,
                locale=locale,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_health_service_status_for_organization(
        self, *, config_overrides: Optional[AsyncHealthClientConfig] = None
    ) -> "capo_health.types.describe_health_service_status_for_organization_response.DescribeHealthServiceStatusForOrganizationResponse":
        """<p>This operation provides status information on enabling or disabling Health to work with your organization. To call this operation, you must use the organization's management account.</p>

        Raises:
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_health_service_status_for_organization_response.DescribeHealthServiceStatusForOrganizationResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_health_service_status_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_health_service_status_for_organization.async_describe_health_service_status_for_organization(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_service_lifecycle(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional[
            "capo_health.types.service_lifecycle_filter.ServiceLifecycleFilter"
        ] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.lifecycle_max_results.LifecycleMaxResults"
        ] = None,
    ) -> "capo_health.types.describe_service_lifecycle_response.DescribeServiceLifecycleResponse":
        """<p>Returns lifecycle information for Amazon Web Services services, including end-of-life dates, version recommendations, and lifecycle events.</p>

        Args:
            filter: <p>Values to narrow the results returned.</p>
            next_token: <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>
            max_results: <p>The maximum number of items to return in one batch, between 1 and 20, inclusive.</p>

        Raises:
            capo_health.errors.invalid_pagination_token.InvalidPaginationToken: <p>The specified pagination token (<code>nextToken</code>) is not valid.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve service lifecycle information
            The following example returns service lifecycle information, including support milestones and lifecycle events for each service version.

            >>> await client.describe_service_lifecycle(max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_health.types.describe_service_lifecycle_request.DescribeServiceLifecycleRequest]",
        ) -> AsyncOperationResponse[
            "capo_health.types.describe_service_lifecycle_response.DescribeServiceLifecycleResponse"
        ]:
            import capo_health._operations.aws_health_20160804.describe_service_lifecycle

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.describe_service_lifecycle.async_describe_service_lifecycle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_health.types.describe_service_lifecycle_request.DescribeServiceLifecycleRequest = {}
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_describe_service_lifecycle(
        self,
        *,
        config_overrides: Optional[AsyncHealthClientConfig] = None,
        filter: Optional[
            "capo_health.types.service_lifecycle_filter.ServiceLifecycleFilter"
        ] = None,
        next_token: Optional["capo_health.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_health.types.lifecycle_max_results.LifecycleMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_health.types.service_lifecycle.ServiceLifecycle]":
        _token = next_token
        while True:
            _response = await self.describe_service_lifecycle(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("service_lifecycles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disable_health_service_access_for_organization(
        self, *, config_overrides: Optional[AsyncHealthClientConfig] = None
    ) -> None:
        """<p>Disables Health from working with Organizations. To call this operation, you must sign in to the organization's management account. For more information, see <a href="https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html">Aggregating Health events</a> in the <i>Health User Guide</i>.</p> <p>This operation doesn't remove the service-linked role from the management account in your organization. You must use the IAM console, API, or Command Line Interface (CLI) to remove the service-linked role. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role">Deleting a Service-Linked Role</a> in the <i>IAM User Guide</i>.</p> <note> <p>You can also disable the organizational feature by using the Organizations <a href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html">DisableAWSServiceAccess</a> API operation. After you call this operation, Health stops aggregating events for all other Amazon Web Services accounts in your organization. If you call the Health API operations for organizational view, Health returns an error. Health continues to aggregate health events for your Amazon Web Services account.</p> </note>

        Raises:
            capo_health.errors.concurrent_modification_exception.ConcurrentModificationException: <p> <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html">EnableHealthServiceAccessForOrganization</a> is already in progress. Wait for the action to complete before trying again. To get the current status, use the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeHealthServiceStatusForOrganization.html">DescribeHealthServiceStatusForOrganization</a> operation.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import capo_health._operations.aws_health_20160804.disable_health_service_access_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.disable_health_service_access_for_organization.async_disable_health_service_access_for_organization(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_health_service_access_for_organization(
        self, *, config_overrides: Optional[AsyncHealthClientConfig] = None
    ) -> None:
        """<p>Enables Health to work with Organizations. You can use the organizational view feature to aggregate events from all Amazon Web Services accounts in your organization in a centralized location. </p> <p>This operation also creates a service-linked role for the management account in the organization. </p> <note> <p>To call this operation, you must meet the following requirements:</p> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan from <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a> to use the Health API. If you call the Health API from an Amazon Web Services account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, you receive a <code>SubscriptionRequiredException</code> error.</p> </li> <li> <p>You must have permission to call this operation from the organization's management account. For example IAM policies, see <a href="https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html">Health identity-based policy examples</a>.</p> </li> </ul> </note> <p>If you don't have the required support plan, you can instead use the Health console to enable the organizational view feature. For more information, see <a href="https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html">Aggregating Health events</a> in the <i>Health User Guide</i>.</p>

        Raises:
            capo_health.errors.concurrent_modification_exception.ConcurrentModificationException: <p> <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html">EnableHealthServiceAccessForOrganization</a> is already in progress. Wait for the action to complete before trying again. To get the current status, use the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeHealthServiceStatusForOrganization.html">DescribeHealthServiceStatusForOrganization</a> operation.</p>
            capo_health.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import capo_health._operations.aws_health_20160804.enable_health_service_access_for_organization

            (
                output,
                http_response,
            ) = await capo_health._operations.aws_health_20160804.enable_health_service_access_for_organization.async_enable_health_service_access_for_organization(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

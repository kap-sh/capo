"""Generated from Smithy shape ``com.amazonaws.pi#PerformanceInsightsv20180227``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pi._auth._signers
import capo_pi._auth._sigv4
from capo_pi._auth._identity import Credentials
from capo_pi._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pi._auth._zapros_handler import AuthMiddleware
from capo_pi._pagination import resolve_path as _resolve_path
from capo_pi._services._aws_config import aaws_config
from capo_pi._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pi.types.accept_language
    import capo_pi.types.additional_metrics_list
    import capo_pi.types.amazon_resource_name
    import capo_pi.types.analysis_report_id
    import capo_pi.types.authorized_actions_list
    import capo_pi.types.boolean
    import capo_pi.types.create_performance_analysis_report_request
    import capo_pi.types.create_performance_analysis_report_response
    import capo_pi.types.delete_performance_analysis_report_request
    import capo_pi.types.delete_performance_analysis_report_response
    import capo_pi.types.describe_dimension_keys_request
    import capo_pi.types.describe_dimension_keys_response
    import capo_pi.types.dimension_group
    import capo_pi.types.dimensions_metric_list
    import capo_pi.types.get_dimension_key_details_request
    import capo_pi.types.get_dimension_key_details_response
    import capo_pi.types.get_performance_analysis_report_request
    import capo_pi.types.get_performance_analysis_report_response
    import capo_pi.types.get_resource_metadata_request
    import capo_pi.types.get_resource_metadata_response
    import capo_pi.types.get_resource_metrics_request
    import capo_pi.types.get_resource_metrics_response
    import capo_pi.types.identifier_string
    import capo_pi.types.integer
    import capo_pi.types.iso_timestamp
    import capo_pi.types.list_available_resource_dimensions_request
    import capo_pi.types.list_available_resource_dimensions_response
    import capo_pi.types.list_available_resource_metrics_request
    import capo_pi.types.list_available_resource_metrics_response
    import capo_pi.types.list_performance_analysis_report_recommendations_request
    import capo_pi.types.list_performance_analysis_report_recommendations_response
    import capo_pi.types.list_performance_analysis_reports_request
    import capo_pi.types.list_performance_analysis_reports_response
    import capo_pi.types.list_tags_for_resource_request
    import capo_pi.types.list_tags_for_resource_response
    import capo_pi.types.max_results
    import capo_pi.types.metric_query_filter_map
    import capo_pi.types.metric_query_list
    import capo_pi.types.metric_type_list
    import capo_pi.types.next_token
    import capo_pi.types.period_alignment
    import capo_pi.types.recommendation
    import capo_pi.types.recommendation_id_list
    import capo_pi.types.request_string
    import capo_pi.types.requested_dimension_list
    import capo_pi.types.service_type
    import capo_pi.types.tag_key_list
    import capo_pi.types.tag_list
    import capo_pi.types.tag_resource_request
    import capo_pi.types.tag_resource_response
    import capo_pi.types.text_format
    import capo_pi.types.untag_resource_request
    import capo_pi.types.untag_resource_response


class AsyncPIClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPIClient:
    """A client for the ``PI`` service.

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
        self._config = AsyncPIClientConfig(
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
        self, config_overrides: Optional[AsyncPIClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPIClientConfig = config_overrides or {}
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

    async def create_performance_analysis_report(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        start_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        end_time: Optional["capo_pi.types.iso_timestamp.ISOTimestamp"] = None,
        tags: Optional["capo_pi.types.tag_list.TagList"] = None,
    ) -> "capo_pi.types.create_performance_analysis_report_response.CreatePerformanceAnalysisReportResponse":
        """<p>Creates a new performance analysis report for a specific time period for the DB instance.</p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights will return metrics. Valid value is <code>RDS</code>.</p>
            identifier: <p>An immutable, Amazon Web Services Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.</p> <p>To use an Amazon RDS instance as a data source, you specify its <code>DbiResourceId</code> value. For example, specify <code>db-ADECBTYHKTSAUMUZQYPDS2GW4A</code>.</p>
            start_time: <p>The start time defined for the analysis report.</p>
            end_time: <p>The end time defined for the analysis report.</p>
            tags: <p>The metadata assigned to the analysis report consisting of a key-value pair.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.create_performance_analysis_report_request.CreatePerformanceAnalysisReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.create_performance_analysis_report_response.CreatePerformanceAnalysisReportResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.create_performance_analysis_report

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.create_performance_analysis_report.async_create_performance_analysis_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.create_performance_analysis_report_request.CreatePerformanceAnalysisReportRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "start_time": start_time,
        }
        if end_time is not None:
            input_["end_time"] = end_time
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_performance_analysis_report(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        analysis_report_id: "capo_pi.types.analysis_report_id.AnalysisReportId",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
    ) -> "capo_pi.types.delete_performance_analysis_report_response.DeletePerformanceAnalysisReportResponse":
        """<p>Deletes a performance analysis report.</p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights will return metrics. Valid value is <code>RDS</code>.</p>
            identifier: <p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>
            analysis_report_id: <p>The unique identifier of the analysis report for deletion.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.delete_performance_analysis_report_request.DeletePerformanceAnalysisReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.delete_performance_analysis_report_response.DeletePerformanceAnalysisReportResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.delete_performance_analysis_report

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.delete_performance_analysis_report.async_delete_performance_analysis_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.delete_performance_analysis_report_request.DeletePerformanceAnalysisReportRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "analysis_report_id": analysis_report_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dimension_keys(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        start_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        end_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        metric: "capo_pi.types.request_string.RequestString",
        group_by: "capo_pi.types.dimension_group.DimensionGroup",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        period_in_seconds: Optional["capo_pi.types.integer.Integer"] = None,
        additional_metrics: Optional[
            "capo_pi.types.additional_metrics_list.AdditionalMetricsList"
        ] = None,
        partition_by: Optional["capo_pi.types.dimension_group.DimensionGroup"] = None,
        filter: Optional[
            "capo_pi.types.metric_query_filter_map.MetricQueryFilterMap"
        ] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
    ) -> "capo_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse":
        """<p>For a specific time period, retrieve the top <code>N</code> dimension keys for a metric. </p> <note> <p>Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.</p> </note>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights will return metrics. Valid values are as follows:</p> <ul> <li> <p> <code>RDS</code> </p> </li> <li> <p> <code>DOCDB</code> </p> </li> </ul>
            identifier: <p>An immutable, Amazon Web Services Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.</p> <p>To use an Amazon RDS instance as a data source, you specify its <code>DbiResourceId</code> value. For example, specify <code>db-FAIHNTYBKTGAUSUZQYPDS2GW4A</code>. </p>
            start_time: <p>The date and time specifying the beginning of the requested time series data. You must specify a <code>StartTime</code> within the past 7 days. The value specified is <i>inclusive</i>, which means that data points equal to or greater than <code>StartTime</code> are returned. </p> <p>The value for <code>StartTime</code> must be earlier than the value for <code>EndTime</code>. </p>
            end_time: <p>The date and time specifying the end of the requested time series data. The value specified is <i>exclusive</i>, which means that data points less than (but not equal to) <code>EndTime</code> are returned.</p> <p>The value for <code>EndTime</code> must be later than the value for <code>StartTime</code>.</p>
            metric: <p>The name of a Performance Insights metric to be measured.</p> <p>Valid values for <code>Metric</code> are:</p> <ul> <li> <p> <code>db.load.avg</code> - A scaled representation of the number of active sessions for the database engine. </p> </li> <li> <p> <code>db.sampledload.avg</code> - The raw number of active sessions for the database engine. </p> </li> </ul> <p>If the number of active sessions is less than an internal Performance Insights threshold, <code>db.load.avg</code> and <code>db.sampledload.avg</code> are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with <code>db.load.avg</code> showing the scaled values, <code>db.sampledload.avg</code> showing the raw values, and <code>db.sampledload.avg</code> less than <code>db.load.avg</code>. For most use cases, you can query <code>db.load.avg</code> only. </p>
            period_in_seconds: <p>The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are: </p> <ul> <li> <p> <code>1</code> (one second)</p> </li> <li> <p> <code>60</code> (one minute)</p> </li> <li> <p> <code>300</code> (five minutes)</p> </li> <li> <p> <code>3600</code> (one hour)</p> </li> <li> <p> <code>86400</code> (twenty-four hours)</p> </li> </ul> <p>If you don't specify <code>PeriodInSeconds</code>, then Performance Insights chooses a value for you, with a goal of returning roughly 100-200 data points in the response. </p>
            group_by: <p>A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights returns all dimensions within this group, unless you provide the names of specific dimensions within this group. You can also request that Performance Insights return a limited number of values for a dimension. </p>
            additional_metrics: <p>Additional metrics for the top <code>N</code> dimension keys. If the specified dimension group in the <code>GroupBy</code> parameter is <code>db.sql_tokenized</code>, you can specify per-SQL metrics to get the values for the top <code>N</code> SQL digests. The response syntax is as follows: <code>"AdditionalMetrics" : { "<i>string</i>" : "<i>string</i>" }</code>.</p> <p>The only supported statistic function is <code>.avg</code>.</p>
            partition_by: <p>For each dimension specified in <code>GroupBy</code>, specify a secondary dimension to further subdivide the partition keys in the response. </p>
            filter: <p>One or more filters to apply in the request. Restrictions:</p> <ul> <li> <p>Any number of filters by the same dimension, as specified in the <code>GroupBy</code> or <code>Partition</code> parameters.</p> </li> <li> <p>A single filter for any other dimension in this dimension group.</p> </li> </ul> <note> <p>The <code>db.sql.db_id</code> filter isn't available for RDS for SQL Server DB instances.</p> </note>
            max_results: <p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxRecords</code> value, a pagination token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.describe_dimension_keys_request.DescribeDimensionKeysRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.describe_dimension_keys

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.describe_dimension_keys.async_describe_dimension_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.describe_dimension_keys_request.DescribeDimensionKeysRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "start_time": start_time,
            "end_time": end_time,
            "metric": metric,
            "group_by": group_by,
        }
        if period_in_seconds is not None:
            input_["period_in_seconds"] = period_in_seconds
        if additional_metrics is not None:
            input_["additional_metrics"] = additional_metrics
        if partition_by is not None:
            input_["partition_by"] = partition_by
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

    async def iter_describe_dimension_keys(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        start_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        end_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        metric: "capo_pi.types.request_string.RequestString",
        group_by: "capo_pi.types.dimension_group.DimensionGroup",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        period_in_seconds: Optional["capo_pi.types.integer.Integer"] = None,
        additional_metrics: Optional[
            "capo_pi.types.additional_metrics_list.AdditionalMetricsList"
        ] = None,
        partition_by: Optional["capo_pi.types.dimension_group.DimensionGroup"] = None,
        filter: Optional[
            "capo_pi.types.metric_query_filter_map.MetricQueryFilterMap"
        ] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse]":
        _token = next_token
        while True:
            _response = await self.describe_dimension_keys(
                service_type,
                identifier,
                start_time,
                end_time,
                metric,
                group_by,
                config_overrides=config_overrides,
                period_in_seconds=period_in_seconds,
                additional_metrics=additional_metrics,
                partition_by=partition_by,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_dimension_key_details(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        group: "capo_pi.types.request_string.RequestString",
        group_identifier: "capo_pi.types.request_string.RequestString",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        requested_dimensions: Optional[
            "capo_pi.types.requested_dimension_list.RequestedDimensionList"
        ] = None,
    ) -> "capo_pi.types.get_dimension_key_details_response.GetDimensionKeyDetailsResponse":
        """<p>Get the attributes of the specified dimension group for a DB instance or data source. For example, if you specify a SQL ID, <code>GetDimensionKeyDetails</code> retrieves the full text of the dimension <code>db.sql.statement</code> associated with this ID. This operation is useful because <code>GetResourceMetrics</code> and <code>DescribeDimensionKeys</code> don't support retrieval of large SQL statement text, lock snapshots, and execution plans.</p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns data. The only valid value is <code>RDS</code>.</p>
            identifier: <p>The ID for a data source from which to gather dimension data. This ID must be immutable and unique within an Amazon Web Services Region. When a DB instance is the data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>. </p>
            group: <p>The name of the dimension group. Performance Insights searches the specified group for the dimension group ID. The following group name values are valid:</p> <ul> <li> <p> <code>db.execution_plan</code> (Amazon RDS and Aurora only)</p> </li> <li> <p> <code>db.lock_snapshot</code> (Aurora only)</p> </li> <li> <p> <code>db.query</code> (Amazon DocumentDB only)</p> </li> <li> <p> <code>db.sql</code> (Amazon RDS and Aurora only)</p> </li> </ul>
            group_identifier: <p>The ID of the dimension group from which to retrieve dimension details. For dimension group <code>db.sql</code>, the group ID is <code>db.sql.id</code>. The following group ID values are valid:</p> <ul> <li> <p> <code>db.execution_plan.id</code> for dimension group <code>db.execution_plan</code> (Aurora and RDS only)</p> </li> <li> <p> <code>db.sql.id</code> for dimension group <code>db.sql</code> (Aurora and RDS only)</p> </li> <li> <p> <code>db.query.id</code> for dimension group <code>db.query</code> (DocumentDB only)</p> </li> <li> <p>For the dimension group <code>db.lock_snapshot</code>, the <code>GroupIdentifier</code> is the epoch timestamp when Performance Insights captured the snapshot, in seconds. You can retrieve this value with the <code>GetResourceMetrics</code> operation for a 1 second period.</p> </li> </ul>
            requested_dimensions: <p>A list of dimensions to retrieve the detail data for within the given dimension group. If you don't specify this parameter, Performance Insights returns all dimension data within the specified dimension group. Specify dimension names for the following dimension groups:</p> <ul> <li> <p> <code>db.execution_plan</code> - Specify the dimension name <code>db.execution_plan.raw_plan</code> or the short dimension name <code>raw_plan</code> (Amazon RDS and Aurora only)</p> </li> <li> <p> <code>db.lock_snapshot</code> - Specify the dimension name <code>db.lock_snapshot.lock_trees</code> or the short dimension name <code>lock_trees</code>. (Aurora only)</p> </li> <li> <p> <code>db.sql</code> - Specify either the full dimension name <code>db.sql.statement</code> or the short dimension name <code>statement</code> (Aurora and RDS only).</p> </li> <li> <p> <code>db.query</code> - Specify either the full dimension name <code>db.query.statement</code> or the short dimension name <code>statement</code> (DocumentDB only).</p> </li> </ul>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.get_dimension_key_details_request.GetDimensionKeyDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.get_dimension_key_details_response.GetDimensionKeyDetailsResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.get_dimension_key_details

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.get_dimension_key_details.async_get_dimension_key_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.get_dimension_key_details_request.GetDimensionKeyDetailsRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "group": group,
            "group_identifier": group_identifier,
        }
        if requested_dimensions is not None:
            input_["requested_dimensions"] = requested_dimensions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_performance_analysis_report(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        analysis_report_id: "capo_pi.types.analysis_report_id.AnalysisReportId",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        text_format: Optional["capo_pi.types.text_format.TextFormat"] = None,
        accept_language: Optional[
            "capo_pi.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_pi.types.get_performance_analysis_report_response.GetPerformanceAnalysisReportResponse":
        """<p>Retrieves the report including the report ID, status, time details, and the insights with recommendations. The report status can be <code>RUNNING</code>, <code>SUCCEEDED</code>, or <code>FAILED</code>. The insights include the <code>description</code> and <code>recommendation</code> fields. </p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights will return metrics. Valid value is <code>RDS</code>.</p>
            identifier: <p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>
            analysis_report_id: <p>A unique identifier of the created analysis report. For example, <code>report-12345678901234567</code> </p>
            text_format: <p>Indicates the text format in the report. The options are <code>PLAIN_TEXT</code> or <code>MARKDOWN</code>. The default value is <code>plain text</code>.</p>
            accept_language: <p>The text language in the report. The default language is <code>EN_US</code> (English). </p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.get_performance_analysis_report_request.GetPerformanceAnalysisReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.get_performance_analysis_report_response.GetPerformanceAnalysisReportResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.get_performance_analysis_report

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.get_performance_analysis_report.async_get_performance_analysis_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.get_performance_analysis_report_request.GetPerformanceAnalysisReportRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "analysis_report_id": analysis_report_id,
        }
        if text_format is not None:
            input_["text_format"] = text_format
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_metadata(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
    ) -> "capo_pi.types.get_resource_metadata_response.GetResourceMetadataResponse":
        """<p>Retrieve the metadata for different features. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance. </p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns metrics.</p>
            identifier: <p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>. </p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.get_resource_metadata_request.GetResourceMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.get_resource_metadata_response.GetResourceMetadataResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.get_resource_metadata

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.get_resource_metadata.async_get_resource_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.get_resource_metadata_request.GetResourceMetadataRequest = {
            "service_type": service_type,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_metrics(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        metric_queries: "capo_pi.types.metric_query_list.MetricQueryList",
        start_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        end_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        period_in_seconds: Optional["capo_pi.types.integer.Integer"] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        period_alignment: Optional[
            "capo_pi.types.period_alignment.PeriodAlignment"
        ] = None,
    ) -> "capo_pi.types.get_resource_metrics_response.GetResourceMetricsResponse":
        """<p>Retrieve Performance Insights metrics for a set of data sources over a time period. You can provide specific dimension groups and dimensions, and provide filtering criteria for each group. You must specify an aggregate function for each metric.</p> <note> <p>Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.</p> </note>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns metrics. Valid values are as follows:</p> <ul> <li> <p> <code>RDS</code> </p> </li> <li> <p> <code>DOCDB</code> </p> </li> </ul>
            identifier: <p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>
            metric_queries: <p>An array of one or more queries to perform. Each query must specify a Performance Insights metric and specify an aggregate function, and you can provide filtering criteria. You must append the aggregate function to the metric. For example, to find the average for the metric <code>db.load</code> you must use <code>db.load.avg</code>. Valid values for aggregate functions include <code>.avg</code>, <code>.min</code>, <code>.max</code>, and <code>.sum</code>.</p>
            start_time: <p>The date and time specifying the beginning of the requested time series query range. You can't specify a <code>StartTime</code> that is earlier than 7 days ago. By default, Performance Insights has 7 days of retention, but you can extend this range up to 2 years. The value specified is <i>inclusive</i>. Thus, the command returns data points equal to or greater than <code>StartTime</code>.</p> <p>The value for <code>StartTime</code> must be earlier than the value for <code>EndTime</code>.</p>
            end_time: <p>The date and time specifying the end of the requested time series query range. The value specified is <i>exclusive</i>. Thus, the command returns data points less than (but not equal to) <code>EndTime</code>.</p> <p>The value for <code>EndTime</code> must be later than the value for <code>StartTime</code>.</p>
            period_in_seconds: <p>The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:</p> <ul> <li> <p> <code>1</code> (one second)</p> </li> <li> <p> <code>60</code> (one minute)</p> </li> <li> <p> <code>300</code> (five minutes)</p> </li> <li> <p> <code>3600</code> (one hour)</p> </li> <li> <p> <code>86400</code> (twenty-four hours)</p> </li> </ul> <p>If you don't specify <code>PeriodInSeconds</code>, then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.</p>
            max_results: <p>The maximum number of items to return in the response.</p>
            next_token: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>.</p>
            period_alignment: <p>The returned timestamp which is the start or end time of the time periods. The default value is <code>END_TIME</code>.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.get_resource_metrics_request.GetResourceMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.get_resource_metrics_response.GetResourceMetricsResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.get_resource_metrics

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.get_resource_metrics.async_get_resource_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.get_resource_metrics_request.GetResourceMetricsRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "metric_queries": metric_queries,
            "start_time": start_time,
            "end_time": end_time,
        }
        if period_in_seconds is not None:
            input_["period_in_seconds"] = period_in_seconds
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if period_alignment is not None:
            input_["period_alignment"] = period_alignment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_resource_metrics(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        metric_queries: "capo_pi.types.metric_query_list.MetricQueryList",
        start_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        end_time: "capo_pi.types.iso_timestamp.ISOTimestamp",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        period_in_seconds: Optional["capo_pi.types.integer.Integer"] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        period_alignment: Optional[
            "capo_pi.types.period_alignment.PeriodAlignment"
        ] = None,
    ) -> "AsyncIterator[capo_pi.types.get_resource_metrics_response.GetResourceMetricsResponse]":
        _token = next_token
        while True:
            _response = await self.get_resource_metrics(
                service_type,
                identifier,
                metric_queries,
                start_time,
                end_time,
                config_overrides=config_overrides,
                period_in_seconds=period_in_seconds,
                max_results=max_results,
                next_token=_token,
                period_alignment=period_alignment,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_available_resource_dimensions(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        metrics: "capo_pi.types.dimensions_metric_list.DimensionsMetricList",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        authorized_actions: Optional[
            "capo_pi.types.authorized_actions_list.AuthorizedActionsList"
        ] = None,
    ) -> "capo_pi.types.list_available_resource_dimensions_response.ListAvailableResourceDimensionsResponse":
        """<p>Retrieve the dimensions that can be queried for each specified metric type on a specified DB instance.</p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns metrics.</p>
            identifier: <p>An immutable identifier for a data source that is unique within an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VWZ</code>. </p>
            metrics: <p>The types of metrics for which to retrieve dimensions. Valid values include <code>db.load</code>.</p>
            max_results: <p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxRecords</code> value, a pagination token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>. </p>
            authorized_actions: <p>The actions to discover the dimensions you are authorized to access. If you specify multiple actions, then the response will contain the dimensions common for all the actions.</p> <p>When you don't specify this request parameter or provide an empty list, the response contains all the available dimensions for the target database engine whether or not you are authorized to access them.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.list_available_resource_dimensions_request.ListAvailableResourceDimensionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.list_available_resource_dimensions_response.ListAvailableResourceDimensionsResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.list_available_resource_dimensions

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.list_available_resource_dimensions.async_list_available_resource_dimensions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.list_available_resource_dimensions_request.ListAvailableResourceDimensionsRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "metrics": metrics,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if authorized_actions is not None:
            input_["authorized_actions"] = authorized_actions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_available_resource_dimensions(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        metrics: "capo_pi.types.dimensions_metric_list.DimensionsMetricList",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        authorized_actions: Optional[
            "capo_pi.types.authorized_actions_list.AuthorizedActionsList"
        ] = None,
    ) -> "AsyncIterator[capo_pi.types.list_available_resource_dimensions_response.ListAvailableResourceDimensionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_available_resource_dimensions(
                service_type,
                identifier,
                metrics,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                authorized_actions=authorized_actions,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_available_resource_metrics(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        metric_types: "capo_pi.types.metric_type_list.MetricTypeList",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
    ) -> "capo_pi.types.list_available_resource_metrics_response.ListAvailableResourceMetricsResponse":
        """<p>Retrieve metrics of the specified types that can be queried for a specified DB instance. </p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns metrics.</p>
            identifier: <p>An immutable identifier for a data source that is unique within an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VWZ</code>. </p>
            metric_types: <p>The types of metrics to return in the response. Valid values in the array include the following:</p> <ul> <li> <p> <code>os</code> (OS counter metrics) - All engines</p> </li> <li> <p> <code>db</code> (DB load metrics) - All engines except for Amazon DocumentDB</p> </li> <li> <p> <code>db.sql.stats</code> (per-SQL metrics) - All engines except for Amazon DocumentDB</p> </li> <li> <p> <code>db.sql_tokenized.stats</code> (per-SQL digest metrics) - All engines except for Amazon DocumentDB</p> </li> </ul>
            next_token: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>. </p>
            max_results: <p>The maximum number of items to return. If the <code>MaxRecords</code> value is less than the number of existing items, the response includes a pagination token. </p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.list_available_resource_metrics_request.ListAvailableResourceMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.list_available_resource_metrics_response.ListAvailableResourceMetricsResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.list_available_resource_metrics

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.list_available_resource_metrics.async_list_available_resource_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.list_available_resource_metrics_request.ListAvailableResourceMetricsRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "metric_types": metric_types,
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

    async def iter_list_available_resource_metrics(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        metric_types: "capo_pi.types.metric_type_list.MetricTypeList",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_pi.types.list_available_resource_metrics_response.ListAvailableResourceMetricsResponse]":
        _token = next_token
        while True:
            _response = await self.list_available_resource_metrics(
                service_type,
                identifier,
                metric_types,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_performance_analysis_report_recommendations(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        analysis_report_id: "capo_pi.types.analysis_report_id.AnalysisReportId",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        recommendation_ids: Optional[
            "capo_pi.types.recommendation_id_list.RecommendationIdList"
        ] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
    ) -> "capo_pi.types.list_performance_analysis_report_recommendations_response.ListPerformanceAnalysisReportRecommendationsResponse":
        """<p>Retrieves recommendations for a performance analysis report.</p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>
            identifier: <p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>
            analysis_report_id: <p>A unique identifier of the created analysis report. For example, <code>report-12345678901234567</code> </p>
            recommendation_ids: <p>A list of recommendation identifiers to filter the results.</p>
            max_results: <p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxResults</code> value, a pagination token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.list_performance_analysis_report_recommendations_request.ListPerformanceAnalysisReportRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.list_performance_analysis_report_recommendations_response.ListPerformanceAnalysisReportRecommendationsResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.list_performance_analysis_report_recommendations

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.list_performance_analysis_report_recommendations.async_list_performance_analysis_report_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.list_performance_analysis_report_recommendations_request.ListPerformanceAnalysisReportRecommendationsRequest = {
            "service_type": service_type,
            "identifier": identifier,
            "analysis_report_id": analysis_report_id,
        }
        if recommendation_ids is not None:
            input_["recommendation_ids"] = recommendation_ids
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

    async def iter_list_performance_analysis_report_recommendations(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        analysis_report_id: "capo_pi.types.analysis_report_id.AnalysisReportId",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        recommendation_ids: Optional[
            "capo_pi.types.recommendation_id_list.RecommendationIdList"
        ] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_pi.types.recommendation.Recommendation]":
        _token = next_token
        while True:
            _response = await self.list_performance_analysis_report_recommendations(
                service_type,
                identifier,
                analysis_report_id,
                config_overrides=config_overrides,
                recommendation_ids=recommendation_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommendations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_performance_analysis_reports(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        list_tags: Optional["capo_pi.types.boolean.Boolean"] = None,
    ) -> "capo_pi.types.list_performance_analysis_reports_response.ListPerformanceAnalysisReportsResponse":
        """<p>Lists all the analysis reports created for the DB instance. The reports are sorted based on the start time of each report.</p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>
            identifier: <p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>
            next_token: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>
            max_results: <p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxResults</code> value, a pagination token is included in the response so that the remaining results can be retrieved. </p>
            list_tags: <p>Specifies whether or not to include the list of tags in the response.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.list_performance_analysis_reports_request.ListPerformanceAnalysisReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.list_performance_analysis_reports_response.ListPerformanceAnalysisReportsResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.list_performance_analysis_reports

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.list_performance_analysis_reports.async_list_performance_analysis_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.list_performance_analysis_reports_request.ListPerformanceAnalysisReportsRequest = {
            "service_type": service_type,
            "identifier": identifier,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_tags is not None:
            input_["list_tags"] = list_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_performance_analysis_reports(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        identifier: "capo_pi.types.identifier_string.IdentifierString",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
        next_token: Optional["capo_pi.types.next_token.NextToken"] = None,
        max_results: Optional["capo_pi.types.max_results.MaxResults"] = None,
        list_tags: Optional["capo_pi.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[capo_pi.types.list_performance_analysis_reports_response.ListPerformanceAnalysisReportsResponse]":
        _token = next_token
        while True:
            _response = await self.list_performance_analysis_reports(
                service_type,
                identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                list_tags=list_tags,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        service_type: "capo_pi.types.service_type.ServiceType",
        resource_arn: "capo_pi.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
    ) -> "capo_pi.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves all the metadata tags associated with Amazon RDS Performance Insights resource.</p>

        Args:
            service_type: <p>List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>
            resource_arn: <p>Lists all the tags for the Amazon RDS Performance Insights resource. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "service_type": service_type,
            "resource_arn": resource_arn,
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
        service_type: "capo_pi.types.service_type.ServiceType",
        resource_arn: "capo_pi.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_pi.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
    ) -> "capo_pi.types.tag_resource_response.TagResourceResponse":
        """<p>Adds metadata tags to the Amazon RDS Performance Insights resource.</p>

        Args:
            service_type: <p>The Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>
            resource_arn: <p>The Amazon RDS Performance Insights resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>
            tags: <p>The metadata assigned to an Amazon RDS resource consisting of a key-value pair.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.tag_resource

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.tag_resource_request.TagResourceRequest = {
            "service_type": service_type,
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
        service_type: "capo_pi.types.service_type.ServiceType",
        resource_arn: "capo_pi.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_pi.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPIClientConfig] = None,
    ) -> "capo_pi.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes the metadata tags from the Amazon RDS Performance Insights resource.</p>

        Args:
            service_type: <p>List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>
            resource_arn: <p>The Amazon RDS Performance Insights resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>
            tag_keys: <p>The metadata assigned to an Amazon RDS Performance Insights resource consisting of a key-value pair.</p>

        Raises:
            capo_pi.errors.internal_service_error.InternalServiceError: <p>The request failed due to an unknown error.</p>
            capo_pi.errors.invalid_argument_exception.InvalidArgumentException: <p>One of the arguments provided is invalid for this request.</p>
            capo_pi.errors.not_authorized_exception.NotAuthorizedException: <p>The user is not authorized to perform this request.</p>
            capo_pi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pi.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pi.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_pi._operations.performance_insightsv20180227.untag_resource

            (
                output,
                http_response,
            ) = await capo_pi._operations.performance_insightsv20180227.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pi.types.untag_resource_request.UntagResourceRequest = {
            "service_type": service_type,
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

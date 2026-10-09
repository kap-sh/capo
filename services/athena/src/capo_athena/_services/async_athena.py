"""Generated from Smithy shape ``com.amazonaws.athena#AmazonAthena``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_athena._auth._signers
import capo_athena._auth._sigv4
from capo_athena._auth._identity import Credentials
from capo_athena._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_athena._auth._zapros_handler import AuthMiddleware
from capo_athena._pagination import resolve_path as _resolve_path
from capo_athena._services._aws_config import aaws_config
from capo_athena._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_athena.types.amazon_resource_name
    import capo_athena.types.batch_get_named_query_input
    import capo_athena.types.batch_get_named_query_output
    import capo_athena.types.batch_get_prepared_statement_input
    import capo_athena.types.batch_get_prepared_statement_output
    import capo_athena.types.batch_get_query_execution_input
    import capo_athena.types.batch_get_query_execution_output
    import capo_athena.types.boolean
    import capo_athena.types.boxed_boolean
    import capo_athena.types.calculation_configuration
    import capo_athena.types.calculation_execution_id
    import capo_athena.types.calculation_execution_state
    import capo_athena.types.cancel_capacity_reservation_input
    import capo_athena.types.cancel_capacity_reservation_output
    import capo_athena.types.capacity_assignments_list
    import capo_athena.types.capacity_reservation_name
    import capo_athena.types.catalog_name_string
    import capo_athena.types.client_request_token
    import capo_athena.types.code_block
    import capo_athena.types.create_capacity_reservation_input
    import capo_athena.types.create_capacity_reservation_output
    import capo_athena.types.create_data_catalog_input
    import capo_athena.types.create_data_catalog_output
    import capo_athena.types.create_named_query_input
    import capo_athena.types.create_named_query_output
    import capo_athena.types.create_notebook_input
    import capo_athena.types.create_notebook_output
    import capo_athena.types.create_prepared_statement_input
    import capo_athena.types.create_prepared_statement_output
    import capo_athena.types.create_presigned_notebook_url_request
    import capo_athena.types.create_presigned_notebook_url_response
    import capo_athena.types.create_work_group_input
    import capo_athena.types.create_work_group_output
    import capo_athena.types.data_catalog_summary
    import capo_athena.types.data_catalog_type
    import capo_athena.types.database
    import capo_athena.types.database_string
    import capo_athena.types.delete_capacity_reservation_input
    import capo_athena.types.delete_capacity_reservation_output
    import capo_athena.types.delete_data_catalog_input
    import capo_athena.types.delete_data_catalog_output
    import capo_athena.types.delete_named_query_input
    import capo_athena.types.delete_named_query_output
    import capo_athena.types.delete_notebook_input
    import capo_athena.types.delete_notebook_output
    import capo_athena.types.delete_prepared_statement_input
    import capo_athena.types.delete_prepared_statement_output
    import capo_athena.types.delete_work_group_input
    import capo_athena.types.delete_work_group_output
    import capo_athena.types.description_string
    import capo_athena.types.engine_configuration
    import capo_athena.types.execution_parameters
    import capo_athena.types.executor_state
    import capo_athena.types.export_notebook_input
    import capo_athena.types.export_notebook_output
    import capo_athena.types.expression_string
    import capo_athena.types.filter_definition
    import capo_athena.types.get_calculation_execution_code_request
    import capo_athena.types.get_calculation_execution_code_response
    import capo_athena.types.get_calculation_execution_request
    import capo_athena.types.get_calculation_execution_response
    import capo_athena.types.get_calculation_execution_status_request
    import capo_athena.types.get_calculation_execution_status_response
    import capo_athena.types.get_capacity_assignment_configuration_input
    import capo_athena.types.get_capacity_assignment_configuration_output
    import capo_athena.types.get_capacity_reservation_input
    import capo_athena.types.get_capacity_reservation_output
    import capo_athena.types.get_data_catalog_input
    import capo_athena.types.get_data_catalog_output
    import capo_athena.types.get_database_input
    import capo_athena.types.get_database_output
    import capo_athena.types.get_named_query_input
    import capo_athena.types.get_named_query_output
    import capo_athena.types.get_notebook_metadata_input
    import capo_athena.types.get_notebook_metadata_output
    import capo_athena.types.get_prepared_statement_input
    import capo_athena.types.get_prepared_statement_output
    import capo_athena.types.get_query_execution_input
    import capo_athena.types.get_query_execution_output
    import capo_athena.types.get_query_results_input
    import capo_athena.types.get_query_results_output
    import capo_athena.types.get_query_runtime_statistics_input
    import capo_athena.types.get_query_runtime_statistics_output
    import capo_athena.types.get_resource_dashboard_request
    import capo_athena.types.get_resource_dashboard_response
    import capo_athena.types.get_session_endpoint_request
    import capo_athena.types.get_session_endpoint_response
    import capo_athena.types.get_session_request
    import capo_athena.types.get_session_response
    import capo_athena.types.get_session_status_request
    import capo_athena.types.get_session_status_response
    import capo_athena.types.get_table_metadata_input
    import capo_athena.types.get_table_metadata_output
    import capo_athena.types.get_work_group_input
    import capo_athena.types.get_work_group_output
    import capo_athena.types.idempotency_token
    import capo_athena.types.import_notebook_input
    import capo_athena.types.import_notebook_output
    import capo_athena.types.list_application_dpu_sizes_input
    import capo_athena.types.list_application_dpu_sizes_output
    import capo_athena.types.list_calculation_executions_request
    import capo_athena.types.list_calculation_executions_response
    import capo_athena.types.list_capacity_reservations_input
    import capo_athena.types.list_capacity_reservations_output
    import capo_athena.types.list_data_catalogs_input
    import capo_athena.types.list_data_catalogs_output
    import capo_athena.types.list_databases_input
    import capo_athena.types.list_databases_output
    import capo_athena.types.list_engine_versions_input
    import capo_athena.types.list_engine_versions_output
    import capo_athena.types.list_executors_request
    import capo_athena.types.list_executors_response
    import capo_athena.types.list_named_queries_input
    import capo_athena.types.list_named_queries_output
    import capo_athena.types.list_notebook_metadata_input
    import capo_athena.types.list_notebook_metadata_output
    import capo_athena.types.list_notebook_sessions_request
    import capo_athena.types.list_notebook_sessions_response
    import capo_athena.types.list_prepared_statements_input
    import capo_athena.types.list_prepared_statements_output
    import capo_athena.types.list_query_executions_input
    import capo_athena.types.list_query_executions_output
    import capo_athena.types.list_sessions_request
    import capo_athena.types.list_sessions_response
    import capo_athena.types.list_table_metadata_input
    import capo_athena.types.list_table_metadata_output
    import capo_athena.types.list_tags_for_resource_input
    import capo_athena.types.list_tags_for_resource_output
    import capo_athena.types.list_work_groups_input
    import capo_athena.types.list_work_groups_output
    import capo_athena.types.max_application_dpu_sizes_count
    import capo_athena.types.max_calculations_count
    import capo_athena.types.max_capacity_reservations_count
    import capo_athena.types.max_data_catalogs_count
    import capo_athena.types.max_databases_count
    import capo_athena.types.max_engine_versions_count
    import capo_athena.types.max_list_executors_count
    import capo_athena.types.max_named_queries_count
    import capo_athena.types.max_notebooks_count
    import capo_athena.types.max_prepared_statements_count
    import capo_athena.types.max_query_executions_count
    import capo_athena.types.max_query_results
    import capo_athena.types.max_sessions_count
    import capo_athena.types.max_table_metadata_count
    import capo_athena.types.max_tags_count
    import capo_athena.types.max_work_groups_count
    import capo_athena.types.monitoring_configuration
    import capo_athena.types.name_string
    import capo_athena.types.named_query_description_string
    import capo_athena.types.named_query_id
    import capo_athena.types.named_query_id_list
    import capo_athena.types.notebook_id
    import capo_athena.types.notebook_name
    import capo_athena.types.notebook_type
    import capo_athena.types.parameters_map
    import capo_athena.types.payload
    import capo_athena.types.prepared_statement_name_list
    import capo_athena.types.put_capacity_assignment_configuration_input
    import capo_athena.types.put_capacity_assignment_configuration_output
    import capo_athena.types.query_execution_context
    import capo_athena.types.query_execution_id
    import capo_athena.types.query_execution_id_list
    import capo_athena.types.query_result_type
    import capo_athena.types.query_string
    import capo_athena.types.result_configuration
    import capo_athena.types.result_reuse_configuration
    import capo_athena.types.role_arn
    import capo_athena.types.s3_uri
    import capo_athena.types.session_id
    import capo_athena.types.session_idle_timeout_in_minutes
    import capo_athena.types.session_manager_token
    import capo_athena.types.session_state
    import capo_athena.types.start_calculation_execution_request
    import capo_athena.types.start_calculation_execution_response
    import capo_athena.types.start_query_execution_input
    import capo_athena.types.start_query_execution_output
    import capo_athena.types.start_session_request
    import capo_athena.types.start_session_response
    import capo_athena.types.statement_name
    import capo_athena.types.stop_calculation_execution_request
    import capo_athena.types.stop_calculation_execution_response
    import capo_athena.types.stop_query_execution_input
    import capo_athena.types.stop_query_execution_output
    import capo_athena.types.table_metadata
    import capo_athena.types.tag
    import capo_athena.types.tag_key_list
    import capo_athena.types.tag_list
    import capo_athena.types.tag_resource_input
    import capo_athena.types.tag_resource_output
    import capo_athena.types.target_dpus_integer
    import capo_athena.types.terminate_session_request
    import capo_athena.types.terminate_session_response
    import capo_athena.types.token
    import capo_athena.types.untag_resource_input
    import capo_athena.types.untag_resource_output
    import capo_athena.types.update_capacity_reservation_input
    import capo_athena.types.update_capacity_reservation_output
    import capo_athena.types.update_data_catalog_input
    import capo_athena.types.update_data_catalog_output
    import capo_athena.types.update_named_query_input
    import capo_athena.types.update_named_query_output
    import capo_athena.types.update_notebook_input
    import capo_athena.types.update_notebook_metadata_input
    import capo_athena.types.update_notebook_metadata_output
    import capo_athena.types.update_notebook_output
    import capo_athena.types.update_prepared_statement_input
    import capo_athena.types.update_prepared_statement_output
    import capo_athena.types.update_work_group_input
    import capo_athena.types.update_work_group_output
    import capo_athena.types.work_group_configuration
    import capo_athena.types.work_group_configuration_updates
    import capo_athena.types.work_group_description_string
    import capo_athena.types.work_group_name
    import capo_athena.types.work_group_state


class AsyncAthenaClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncAthenaClient:
    """A client for the ``Athena`` service.

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
        self._config = AsyncAthenaClientConfig(
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
        self, config_overrides: Optional[AsyncAthenaClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAthenaClientConfig = config_overrides or {}
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

    async def batch_get_named_query(
        self,
        named_query_ids: "capo_athena.types.named_query_id_list.NamedQueryIdList",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.batch_get_named_query_output.BatchGetNamedQueryOutput":
        """<p>Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Requires you to have access to the workgroup in which the queries were saved. Use <a>ListNamedQueriesInput</a> to get the list of named query IDs in the specified workgroup. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under <a>UnprocessedNamedQueryId</a>. Named queries differ from executed queries. Use <a>BatchGetQueryExecutionInput</a> to get details about each unique query execution, and <a>ListQueryExecutionsInput</a> to get a list of query execution IDs.</p>

        Args:
            named_query_ids: <p>An array of query IDs.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.batch_get_named_query_input.BatchGetNamedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.batch_get_named_query_output.BatchGetNamedQueryOutput"
        ]:
            import capo_athena._operations.amazon_athena.batch_get_named_query

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.batch_get_named_query.async_batch_get_named_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.batch_get_named_query_input.BatchGetNamedQueryInput = {
            "named_query_ids": named_query_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_prepared_statement(
        self,
        prepared_statement_names: "capo_athena.types.prepared_statement_name_list.PreparedStatementNameList",
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput":
        """<p>Returns the details of a single prepared statement or a list of up to 256 prepared statements for the array of prepared statement names that you provide. Requires you to have access to the workgroup to which the prepared statements belong. If a prepared statement cannot be retrieved for the name specified, the statement is listed in <code>UnprocessedPreparedStatementNames</code>.</p>

        Args:
            prepared_statement_names: <p>A list of prepared statement names to return.</p>
            work_group: <p>The name of the workgroup to which the prepared statements belong.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.batch_get_prepared_statement_input.BatchGetPreparedStatementInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.batch_get_prepared_statement_output.BatchGetPreparedStatementOutput"
        ]:
            import capo_athena._operations.amazon_athena.batch_get_prepared_statement

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.batch_get_prepared_statement.async_batch_get_prepared_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.batch_get_prepared_statement_input.BatchGetPreparedStatementInput = {
            "prepared_statement_names": prepared_statement_names,
            "work_group": work_group,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_query_execution(
        self,
        query_execution_ids: "capo_athena.types.query_execution_id_list.QueryExecutionIdList",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.batch_get_query_execution_output.BatchGetQueryExecutionOutput":
        """<p>Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. Requires you to have access to the workgroup in which the queries ran. To get a list of query execution IDs, use <a>ListQueryExecutionsInput$WorkGroup</a>. Query executions differ from named (saved) queries. Use <a>BatchGetNamedQueryInput</a> to get details about named queries.</p>

        Args:
            query_execution_ids: <p>An array of query execution IDs.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.batch_get_query_execution_input.BatchGetQueryExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.batch_get_query_execution_output.BatchGetQueryExecutionOutput"
        ]:
            import capo_athena._operations.amazon_athena.batch_get_query_execution

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.batch_get_query_execution.async_batch_get_query_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.batch_get_query_execution_input.BatchGetQueryExecutionInput = {
            "query_execution_ids": query_execution_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_capacity_reservation(
        self,
        name: "capo_athena.types.capacity_reservation_name.CapacityReservationName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.cancel_capacity_reservation_output.CancelCapacityReservationOutput":
        """<p>Cancels the capacity reservation with the specified name. Cancelled reservations remain in your account and will be deleted 45 days after cancellation. During the 45 days, you cannot re-purpose or reuse a reservation that has been cancelled, but you can refer to its tags and view it for historical reference. </p>

        Args:
            name: <p>The name of the capacity reservation to cancel.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.cancel_capacity_reservation_input.CancelCapacityReservationInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.cancel_capacity_reservation_output.CancelCapacityReservationOutput"
        ]:
            import capo_athena._operations.amazon_athena.cancel_capacity_reservation

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.cancel_capacity_reservation.async_cancel_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.cancel_capacity_reservation_input.CancelCapacityReservationInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_capacity_reservation(
        self,
        target_dpus: "capo_athena.types.target_dpus_integer.TargetDpusInteger",
        name: "capo_athena.types.capacity_reservation_name.CapacityReservationName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        tags: Optional["capo_athena.types.tag_list.TagList"] = None,
    ) -> "capo_athena.types.create_capacity_reservation_output.CreateCapacityReservationOutput":
        """<p>Creates a capacity reservation with the specified name and number of requested data processing units.</p>

        Args:
            target_dpus: <p>The number of requested data processing units.</p>
            name: <p>The name of the capacity reservation to create.</p>
            tags: <p>The tags for the capacity reservation.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.create_capacity_reservation_input.CreateCapacityReservationInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.create_capacity_reservation_output.CreateCapacityReservationOutput"
        ]:
            import capo_athena._operations.amazon_athena.create_capacity_reservation

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.create_capacity_reservation.async_create_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.create_capacity_reservation_input.CreateCapacityReservationInput = {
            "target_dpus": target_dpus,
            "name": name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_catalog(
        self,
        name: "capo_athena.types.catalog_name_string.CatalogNameString",
        type: "capo_athena.types.data_catalog_type.DataCatalogType",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.description_string.DescriptionString"
        ] = None,
        parameters: Optional["capo_athena.types.parameters_map.ParametersMap"] = None,
        tags: Optional["capo_athena.types.tag_list.TagList"] = None,
    ) -> "capo_athena.types.create_data_catalog_output.CreateDataCatalogOutput":
        r"""<p>Creates (registers) a data catalog with the specified name and properties. Catalogs created are visible to all users of the same Amazon Web Services account.</p> <p>For a <code>FEDERATED</code> catalog, this API operation creates the following resources.</p> <ul> <li> <p>CFN Stack Name with a maximum length of 128 characters and prefix <code>athenafederatedcatalog-CATALOG_NAME_SANITIZED</code> with length 23 characters.</p> </li> <li> <p>Lambda Function Name with a maximum length of 64 characters and prefix <code>athenafederatedcatalog_CATALOG_NAME_SANITIZED</code> with length 23 characters.</p> </li> <li> <p>Glue Connection Name with a maximum length of 255 characters and a prefix <code>athenafederatedcatalog_CATALOG_NAME_SANITIZED</code> with length 23 characters. </p> </li> </ul>

        Args:
            name: <p>The name of the data catalog to create. The catalog name must be unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.</p> <p>For <code>FEDERATED</code> type the catalog name has following considerations and limits:</p> <ul> <li> <p>The catalog name allows special characters such as <code>_ , @ , \ , - </code>. These characters are replaced with a hyphen (-) when creating the CFN Stack Name and with an underscore (_) when creating the Lambda Function and Glue Connection Name.</p> </li> <li> <p>The catalog name has a theoretical limit of 128 characters. However, since we use it to create other resources that allow less characters and we prepend a prefix to it, the actual catalog name limit for <code>FEDERATED</code> catalog is 64 - 23 = 41 characters.</p> </li> </ul>
            type: <p>The type of data catalog to create: <code>LAMBDA</code> for a federated catalog, <code>GLUE</code> for an Glue Data Catalog, and <code>HIVE</code> for an external Apache Hive metastore. <code>FEDERATED</code> is a federated catalog for which Athena creates the connection and the Lambda function for you based on the parameters that you pass.</p> <p>For <code>FEDERATED</code> type, we do not support IAM identity center.</p>
            description: <p>A description of the data catalog to be created.</p>
            parameters: <p>Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. </p> <ul> <li> <p>For the <code>HIVE</code> data catalog type, use the following syntax. The <code>metadata-function</code> parameter is required. <code>The sdk-version</code> parameter is optional and defaults to the currently supported version.</p> <p> <code>metadata-function=<i>lambda_arn</i>, sdk-version=<i>version_number</i> </code> </p> </li> <li> <p>For the <code>LAMBDA</code> data catalog type, use one of the following sets of required parameters, but not both.</p> <ul> <li> <p>If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.</p> <p> <code>metadata-function=<i>lambda_arn</i>, record-function=<i>lambda_arn</i> </code> </p> </li> <li> <p> If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.</p> <p> <code>function=<i>lambda_arn</i> </code> </p> </li> </ul> </li> <li> <p>The <code>GLUE</code> type takes a catalog ID parameter and is required. The <code> <i>catalog_id</i> </code> is the account ID of the Amazon Web Services account to which the Glue Data Catalog belongs.</p> <p> <code>catalog-id=<i>catalog_id</i> </code> </p> <ul> <li> <p>The <code>GLUE</code> data catalog type also applies to the default <code>AwsDataCatalog</code> that already exists in your account, of which you can have only one and cannot modify.</p> </li> </ul> </li> <li> <p>The <code>FEDERATED</code> data catalog type uses one of the following parameters, but not both. Use <code>connection-arn</code> for an existing Glue connection. Use <code>connection-type</code> and <code>connection-properties</code> to specify the configuration setting for a new connection.</p> <ul> <li> <p> <code>connection-arn:<i><glue_connection_arn_to_reuse></i> </code> </p> </li> <li> <p> <code>lambda-role-arn</code> (optional): The execution role to use for the Lambda function. If not provided, one is created.</p> </li> <li> <p> <code>connection-type:MYSQL|REDSHIFT|...., connection-properties:"<i><json_string></i>"</code> </p> <p>For <i> <code><json_string></code> </i>, use escaped JSON text, as in the following example.</p> <p> <code>"{\"spill_bucket\":\"my_spill\",\"spill_prefix\":\"athena-spill\",\"host\":\"abc12345.snowflakecomputing.com\",\"port\":\"1234\",\"warehouse\":\"DEV_WH\",\"database\":\"TEST\",\"schema\":\"PUBLIC\",\"SecretArn\":\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\"}"</code> </p> </li> </ul> </li> </ul>
            tags: <p>A list of comma separated tags to add to the data catalog that is created. All the resources that are created by the <code>CreateDataCatalog</code> API operation with <code>FEDERATED</code> type will have the tag <code>federated_athena_datacatalog="true"</code>. This includes the CFN Stack, Glue Connection, Athena DataCatalog, and all the resources created as part of the CFN Stack (Lambda Function, IAM policies/roles).</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.create_data_catalog_input.CreateDataCatalogInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.create_data_catalog_output.CreateDataCatalogOutput"
        ]:
            import capo_athena._operations.amazon_athena.create_data_catalog

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.create_data_catalog.async_create_data_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.create_data_catalog_input.CreateDataCatalogInput = {
            "name": name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_named_query(
        self,
        name: "capo_athena.types.name_string.NameString",
        database: "capo_athena.types.database_string.DatabaseString",
        query_string: "capo_athena.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.description_string.DescriptionString"
        ] = None,
        client_request_token: Optional[
            "capo_athena.types.idempotency_token.IdempotencyToken"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.create_named_query_output.CreateNamedQueryOutput":
        """<p>Creates a named query in the specified workgroup. Requires that you have access to the workgroup.</p>

        Args:
            name: <p>The query name.</p>
            description: <p>The query description.</p>
            database: <p>The database to which the query belongs.</p>
            query_string: <p>The contents of the query with all query statements.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another <code>CreateNamedQuery</code> request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the <code>QueryString</code>, an error is returned.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>
            work_group: <p>The name of the workgroup in which the named query is being created.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.create_named_query_input.CreateNamedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.create_named_query_output.CreateNamedQueryOutput"
        ]:
            import capo_athena._operations.amazon_athena.create_named_query

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.create_named_query.async_create_named_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.create_named_query_input.CreateNamedQueryInput = {
            "name": name,
            "database": database,
            "query_string": query_string,
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_notebook(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        name: "capo_athena.types.notebook_name.NotebookName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        client_request_token: Optional[
            "capo_athena.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_athena.types.create_notebook_output.CreateNotebookOutput":
        """<p>Creates an empty <code>ipynb</code> file in the specified Apache Spark enabled workgroup. Throws an error if a file in the workgroup with the same name already exists.</p>

        Args:
            work_group: <p>The name of the Spark enabled workgroup in which the notebook will be created.</p>
            name: <p>The name of the <code>ipynb</code> file to be created in the Spark workgroup, without the <code>.ipynb</code> extension.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.create_notebook_input.CreateNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.create_notebook_output.CreateNotebookOutput"
        ]:
            import capo_athena._operations.amazon_athena.create_notebook

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.create_notebook.async_create_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.create_notebook_input.CreateNotebookInput = {
            "work_group": work_group,
            "name": name,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_prepared_statement(
        self,
        statement_name: "capo_athena.types.statement_name.StatementName",
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        query_statement: "capo_athena.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.description_string.DescriptionString"
        ] = None,
    ) -> "capo_athena.types.create_prepared_statement_output.CreatePreparedStatementOutput":
        """<p>Creates a prepared statement for use with SQL queries in Athena.</p>

        Args:
            statement_name: <p>The name of the prepared statement.</p>
            work_group: <p>The name of the workgroup to which the prepared statement belongs.</p>
            query_statement: <p>The query string for the prepared statement.</p>
            description: <p>The description of the prepared statement.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.create_prepared_statement_input.CreatePreparedStatementInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.create_prepared_statement_output.CreatePreparedStatementOutput"
        ]:
            import capo_athena._operations.amazon_athena.create_prepared_statement

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.create_prepared_statement.async_create_prepared_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.create_prepared_statement_input.CreatePreparedStatementInput = {
            "statement_name": statement_name,
            "work_group": work_group,
            "query_statement": query_statement,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_presigned_notebook_url(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.create_presigned_notebook_url_response.CreatePresignedNotebookUrlResponse":
        """<p>Gets an authentication token and the URL at which the notebook can be accessed. During programmatic access, <code>CreatePresignedNotebookUrl</code> must be called every 10 minutes to refresh the authentication token. For information about granting programmatic access, see <a href="https://docs.aws.amazon.com/athena/latest/ug/setting-up.html#setting-up-grant-programmatic-access">Grant programmatic access</a>.</p>

        Args:
            session_id: <p>The session ID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.create_presigned_notebook_url_request.CreatePresignedNotebookUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.create_presigned_notebook_url_response.CreatePresignedNotebookUrlResponse"
        ]:
            import capo_athena._operations.amazon_athena.create_presigned_notebook_url

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.create_presigned_notebook_url.async_create_presigned_notebook_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.create_presigned_notebook_url_request.CreatePresignedNotebookUrlRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_work_group(
        self,
        name: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        configuration: Optional[
            "capo_athena.types.work_group_configuration.WorkGroupConfiguration"
        ] = None,
        description: Optional[
            "capo_athena.types.work_group_description_string.WorkGroupDescriptionString"
        ] = None,
        tags: Optional["capo_athena.types.tag_list.TagList"] = None,
    ) -> "capo_athena.types.create_work_group_output.CreateWorkGroupOutput":
        """<p>Creates a workgroup with the specified name. A workgroup can be an Apache Spark enabled workgroup or an Athena SQL workgroup.</p>

        Args:
            name: <p>The workgroup name.</p>
            configuration: <p>Contains configuration information for creating an Athena SQL workgroup or Spark enabled Athena workgroup. Athena SQL workgroup configuration includes the location in Amazon S3 where query and calculation results are stored, the encryption configuration, if any, used for encrypting query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, the limit for the amount of bytes scanned (cutoff) per query, if it is specified, and whether workgroup's settings (specified with <code>EnforceWorkGroupConfiguration</code>) in the <code>WorkGroupConfiguration</code> override client-side settings. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>
            description: <p>The workgroup description.</p>
            tags: <p>A list of comma separated tags to add to the workgroup that is created.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.create_work_group_input.CreateWorkGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.create_work_group_output.CreateWorkGroupOutput"
        ]:
            import capo_athena._operations.amazon_athena.create_work_group

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.create_work_group.async_create_work_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.create_work_group_input.CreateWorkGroupInput = {
            "name": name
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_capacity_reservation(
        self,
        name: "capo_athena.types.capacity_reservation_name.CapacityReservationName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.delete_capacity_reservation_output.DeleteCapacityReservationOutput":
        """<p>Deletes a cancelled capacity reservation. A reservation must be cancelled before it can be deleted. A deleted reservation is immediately removed from your account and can no longer be referenced, including by its ARN. A deleted reservation cannot be called by <code>GetCapacityReservation</code>, and deleted reservations do not appear in the output of <code>ListCapacityReservations</code>.</p>

        Args:
            name: <p>The name of the capacity reservation to delete.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.delete_capacity_reservation_input.DeleteCapacityReservationInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.delete_capacity_reservation_output.DeleteCapacityReservationOutput"
        ]:
            import capo_athena._operations.amazon_athena.delete_capacity_reservation

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.delete_capacity_reservation.async_delete_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.delete_capacity_reservation_input.DeleteCapacityReservationInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_catalog(
        self,
        name: "capo_athena.types.catalog_name_string.CatalogNameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        delete_catalog_only: Optional["capo_athena.types.boolean.Boolean"] = None,
    ) -> "capo_athena.types.delete_data_catalog_output.DeleteDataCatalogOutput":
        """<p>Deletes a data catalog.</p>

        Args:
            name: <p>The name of the data catalog to delete.</p>
            delete_catalog_only: <p>Deletes the Athena Data Catalog. You can only use this with the <code>FEDERATED</code> catalogs. You usually perform this before registering the connector with Glue Data Catalog. After deletion, you will have to manage the Glue Connection and Lambda function. </p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.delete_data_catalog_input.DeleteDataCatalogInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.delete_data_catalog_output.DeleteDataCatalogOutput"
        ]:
            import capo_athena._operations.amazon_athena.delete_data_catalog

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.delete_data_catalog.async_delete_data_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.delete_data_catalog_input.DeleteDataCatalogInput = {
            "name": name
        }
        if delete_catalog_only is not None:
            input_["delete_catalog_only"] = delete_catalog_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_named_query(
        self,
        named_query_id: "capo_athena.types.named_query_id.NamedQueryId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.delete_named_query_output.DeleteNamedQueryOutput":
        """<p>Deletes the named query if you have access to the workgroup in which the query was saved.</p>

        Args:
            named_query_id: <p>The unique ID of the query to delete.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.delete_named_query_input.DeleteNamedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.delete_named_query_output.DeleteNamedQueryOutput"
        ]:
            import capo_athena._operations.amazon_athena.delete_named_query

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.delete_named_query.async_delete_named_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.delete_named_query_input.DeleteNamedQueryInput = {
            "named_query_id": named_query_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_notebook(
        self,
        notebook_id: "capo_athena.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.delete_notebook_output.DeleteNotebookOutput":
        """<p>Deletes the specified notebook.</p>

        Args:
            notebook_id: <p>The ID of the notebook to delete.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.delete_notebook_input.DeleteNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.delete_notebook_output.DeleteNotebookOutput"
        ]:
            import capo_athena._operations.amazon_athena.delete_notebook

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.delete_notebook.async_delete_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.delete_notebook_input.DeleteNotebookInput = {
            "notebook_id": notebook_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_prepared_statement(
        self,
        statement_name: "capo_athena.types.statement_name.StatementName",
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.delete_prepared_statement_output.DeletePreparedStatementOutput":
        """<p>Deletes the prepared statement with the specified name from the specified workgroup.</p>

        Args:
            statement_name: <p>The name of the prepared statement to delete.</p>
            work_group: <p>The workgroup to which the statement to be deleted belongs.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.delete_prepared_statement_input.DeletePreparedStatementInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.delete_prepared_statement_output.DeletePreparedStatementOutput"
        ]:
            import capo_athena._operations.amazon_athena.delete_prepared_statement

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.delete_prepared_statement.async_delete_prepared_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.delete_prepared_statement_input.DeletePreparedStatementInput = {
            "statement_name": statement_name,
            "work_group": work_group,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_work_group(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        recursive_delete_option: Optional[
            "capo_athena.types.boxed_boolean.BoxedBoolean"
        ] = None,
    ) -> "capo_athena.types.delete_work_group_output.DeleteWorkGroupOutput":
        """<p>Deletes the workgroup with the specified name. The primary workgroup cannot be deleted.</p>

        Args:
            work_group: <p>The unique name of the workgroup to delete.</p>
            recursive_delete_option: <p>The option to delete the workgroup and its contents even if the workgroup contains any named queries, query executions, or notebooks.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.delete_work_group_input.DeleteWorkGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.delete_work_group_output.DeleteWorkGroupOutput"
        ]:
            import capo_athena._operations.amazon_athena.delete_work_group

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.delete_work_group.async_delete_work_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.delete_work_group_input.DeleteWorkGroupInput = {
            "work_group": work_group
        }
        if recursive_delete_option is not None:
            input_["recursive_delete_option"] = recursive_delete_option

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_notebook(
        self,
        notebook_id: "capo_athena.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.export_notebook_output.ExportNotebookOutput":
        """<p>Exports the specified notebook and its metadata.</p>

        Args:
            notebook_id: <p>The ID of the notebook to export.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.export_notebook_input.ExportNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.export_notebook_output.ExportNotebookOutput"
        ]:
            import capo_athena._operations.amazon_athena.export_notebook

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.export_notebook.async_export_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.export_notebook_input.ExportNotebookInput = {
            "notebook_id": notebook_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_calculation_execution(
        self,
        calculation_execution_id: "capo_athena.types.calculation_execution_id.CalculationExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_calculation_execution_response.GetCalculationExecutionResponse":
        """<p>Describes a previously submitted calculation execution.</p>

        Args:
            calculation_execution_id: <p>The calculation execution UUID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_calculation_execution_request.GetCalculationExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_calculation_execution_response.GetCalculationExecutionResponse"
        ]:
            import capo_athena._operations.amazon_athena.get_calculation_execution

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_calculation_execution.async_get_calculation_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_calculation_execution_request.GetCalculationExecutionRequest = {
            "calculation_execution_id": calculation_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_calculation_execution_code(
        self,
        calculation_execution_id: "capo_athena.types.calculation_execution_id.CalculationExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_calculation_execution_code_response.GetCalculationExecutionCodeResponse":
        """<p>Retrieves the unencrypted code that was executed for the calculation.</p>

        Args:
            calculation_execution_id: <p>The calculation execution UUID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_calculation_execution_code_request.GetCalculationExecutionCodeRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_calculation_execution_code_response.GetCalculationExecutionCodeResponse"
        ]:
            import capo_athena._operations.amazon_athena.get_calculation_execution_code

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_calculation_execution_code.async_get_calculation_execution_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_calculation_execution_code_request.GetCalculationExecutionCodeRequest = {
            "calculation_execution_id": calculation_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_calculation_execution_status(
        self,
        calculation_execution_id: "capo_athena.types.calculation_execution_id.CalculationExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_calculation_execution_status_response.GetCalculationExecutionStatusResponse":
        """<p>Gets the status of a current calculation.</p>

        Args:
            calculation_execution_id: <p>The calculation execution UUID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_calculation_execution_status_request.GetCalculationExecutionStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_calculation_execution_status_response.GetCalculationExecutionStatusResponse"
        ]:
            import capo_athena._operations.amazon_athena.get_calculation_execution_status

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_calculation_execution_status.async_get_calculation_execution_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_calculation_execution_status_request.GetCalculationExecutionStatusRequest = {
            "calculation_execution_id": calculation_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_capacity_assignment_configuration(
        self,
        capacity_reservation_name: "capo_athena.types.capacity_reservation_name.CapacityReservationName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_capacity_assignment_configuration_output.GetCapacityAssignmentConfigurationOutput":
        """<p>Gets the capacity assignment configuration for a capacity reservation, if one exists.</p>

        Args:
            capacity_reservation_name: <p>The name of the capacity reservation to retrieve the capacity assignment configuration for.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_capacity_assignment_configuration_input.GetCapacityAssignmentConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_capacity_assignment_configuration_output.GetCapacityAssignmentConfigurationOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_capacity_assignment_configuration

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_capacity_assignment_configuration.async_get_capacity_assignment_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_capacity_assignment_configuration_input.GetCapacityAssignmentConfigurationInput = {
            "capacity_reservation_name": capacity_reservation_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_capacity_reservation(
        self,
        name: "capo_athena.types.capacity_reservation_name.CapacityReservationName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> (
        "capo_athena.types.get_capacity_reservation_output.GetCapacityReservationOutput"
    ):
        """<p>Returns information about the capacity reservation with the specified name.</p>

        Args:
            name: <p>The name of the capacity reservation.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_capacity_reservation_input.GetCapacityReservationInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_capacity_reservation_output.GetCapacityReservationOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_capacity_reservation

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_capacity_reservation.async_get_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_capacity_reservation_input.GetCapacityReservationInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_database(
        self,
        catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString",
        database_name: "capo_athena.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.get_database_output.GetDatabaseOutput":
        """<p>Returns a database object for the specified database and data catalog.</p>

        Args:
            catalog_name: <p>The name of the data catalog that contains the database to return.</p>
            database_name: <p>The name of the database to return.</p>
            work_group: <p>The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled Glue Data Catalog.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.metadata_exception.MetadataException: <p>An exception that Athena received when it called a custom metastore. Occurs if the error is not caused by user input (<code>InvalidRequestException</code>) or from the Athena platform (<code>InternalServerException</code>). For example, if a user-created Lambda function is missing permissions, the Lambda <code>4XX</code> exception is returned in a <code>MetadataException</code>.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_database_input.GetDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_database_output.GetDatabaseOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_database

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_database.async_get_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_database_input.GetDatabaseInput = {
            "catalog_name": catalog_name,
            "database_name": database_name,
        }
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_catalog(
        self,
        name: "capo_athena.types.catalog_name_string.CatalogNameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.get_data_catalog_output.GetDataCatalogOutput":
        """<p>Returns the specified data catalog.</p>

        Args:
            name: <p>The name of the data catalog to return.</p>
            work_group: <p>The name of the workgroup. Required if making an IAM Identity Center request.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_data_catalog_input.GetDataCatalogInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_data_catalog_output.GetDataCatalogOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_data_catalog

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_data_catalog.async_get_data_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_data_catalog_input.GetDataCatalogInput = {
            "name": name
        }
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_named_query(
        self,
        named_query_id: "capo_athena.types.named_query_id.NamedQueryId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_named_query_output.GetNamedQueryOutput":
        """<p>Returns information about a single query. Requires that you have access to the workgroup in which the query was saved.</p>

        Args:
            named_query_id: <p>The unique ID of the query. Use <a>ListNamedQueries</a> to get query IDs.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_named_query_input.GetNamedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_named_query_output.GetNamedQueryOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_named_query

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_named_query.async_get_named_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_named_query_input.GetNamedQueryInput = {
            "named_query_id": named_query_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_notebook_metadata(
        self,
        notebook_id: "capo_athena.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_notebook_metadata_output.GetNotebookMetadataOutput":
        """<p>Retrieves notebook metadata for the specified notebook ID.</p>

        Args:
            notebook_id: <p>The ID of the notebook whose metadata is to be retrieved.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_notebook_metadata_input.GetNotebookMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_notebook_metadata_output.GetNotebookMetadataOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_notebook_metadata

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_notebook_metadata.async_get_notebook_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_notebook_metadata_input.GetNotebookMetadataInput = {
            "notebook_id": notebook_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_prepared_statement(
        self,
        statement_name: "capo_athena.types.statement_name.StatementName",
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_prepared_statement_output.GetPreparedStatementOutput":
        """<p>Retrieves the prepared statement with the specified name from the specified workgroup.</p>

        Args:
            statement_name: <p>The name of the prepared statement to retrieve.</p>
            work_group: <p>The workgroup to which the statement to be retrieved belongs.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_prepared_statement_input.GetPreparedStatementInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_prepared_statement_output.GetPreparedStatementOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_prepared_statement

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_prepared_statement.async_get_prepared_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_prepared_statement_input.GetPreparedStatementInput = {
            "statement_name": statement_name,
            "work_group": work_group,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_query_execution(
        self,
        query_execution_id: "capo_athena.types.query_execution_id.QueryExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_query_execution_output.GetQueryExecutionOutput":
        """<p>Returns information about a single execution of a query if you have access to the workgroup in which the query ran. Each time a query executes, information about the query execution is saved with a unique ID.</p>

        Args:
            query_execution_id: <p>The unique ID of the query execution.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_query_execution_input.GetQueryExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_query_execution_output.GetQueryExecutionOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_query_execution

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_query_execution.async_get_query_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_query_execution_input.GetQueryExecutionInput = {
            "query_execution_id": query_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_query_results(
        self,
        query_execution_id: "capo_athena.types.query_execution_id.QueryExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_query_results.MaxQueryResults"
        ] = None,
        query_result_type: Optional[
            "capo_athena.types.query_result_type.QueryResultType"
        ] = None,
    ) -> "capo_athena.types.get_query_results_output.GetQueryResultsOutput":
        """<p>Streams the results of a single query execution specified by <code>QueryExecutionId</code> from the Athena query results location in Amazon S3. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/querying.html">Working with query results, recent queries, and output files</a> in the <i>Amazon Athena User Guide</i>. This request does not execute the query but returns results. Use <a>StartQueryExecution</a> to run a query.</p> <p>To stream query results successfully, the IAM principal with permission to call <code>GetQueryResults</code> also must have permissions to the Amazon S3 <code>GetObject</code> action for the Athena query results location.</p> <important> <p>IAM principals with permission to the Amazon S3 <code>GetObject</code> action for the query results location are able to retrieve query results from Amazon S3 even if permission to the <code>GetQueryResults</code> action is denied. To restrict user or role access, ensure that Amazon S3 permissions to the Athena query location are denied.</p> </important>

        Args:
            query_execution_id: <p>The unique ID of the query execution.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>
            max_results: <p>The maximum number of results (rows) to return in this request.</p>
            query_result_type: <p> When you set this to <code>DATA_ROWS</code> or empty, <code>GetQueryResults</code> returns the query results in rows. If set to <code>DATA_MANIFEST</code>, it returns the manifest file in rows. Only the query types <code>CREATE TABLE AS SELECT</code>, <code>UNLOAD</code>, and <code>INSERT</code> can generate a manifest file. If you use <code>DATA_MANIFEST</code> for other query types, the query will fail. </p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_query_results_input.GetQueryResultsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_query_results_output.GetQueryResultsOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_query_results

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_query_results.async_get_query_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_query_results_input.GetQueryResultsInput = {
            "query_execution_id": query_execution_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if query_result_type is not None:
            input_["query_result_type"] = query_result_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_query_results(
        self,
        query_execution_id: "capo_athena.types.query_execution_id.QueryExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_query_results.MaxQueryResults"
        ] = None,
        query_result_type: Optional[
            "capo_athena.types.query_result_type.QueryResultType"
        ] = None,
    ) -> "AsyncIterator[capo_athena.types.get_query_results_output.GetQueryResultsOutput]":
        _token = next_token
        while True:
            _response = await self.get_query_results(
                query_execution_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                query_result_type=query_result_type,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_query_runtime_statistics(
        self,
        query_execution_id: "capo_athena.types.query_execution_id.QueryExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_query_runtime_statistics_output.GetQueryRuntimeStatisticsOutput":
        """<p>Returns query execution runtime statistics related to a single execution of a query if you have access to the workgroup in which the query ran. Statistics from the <code>Timeline</code> section of the response object are available as soon as <a>QueryExecutionStatus$State</a> is in a SUCCEEDED or FAILED state. The remaining non-timeline statistics in the response (like stage-level input and output row count and data size) are updated asynchronously and may not be available immediately after a query completes or, in some cases, may not be returned. The non-timeline statistics are also not included when a query has row-level filters defined in Lake Formation.</p>

        Args:
            query_execution_id: <p>The unique ID of the query execution.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_query_runtime_statistics_input.GetQueryRuntimeStatisticsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_query_runtime_statistics_output.GetQueryRuntimeStatisticsOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_query_runtime_statistics

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_query_runtime_statistics.async_get_query_runtime_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_query_runtime_statistics_input.GetQueryRuntimeStatisticsInput = {
            "query_execution_id": query_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_dashboard(
        self,
        resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> (
        "capo_athena.types.get_resource_dashboard_response.GetResourceDashboardResponse"
    ):
        """<p>Gets the Live UI/Persistence UI for a session.</p>

        Args:
            resource_arn: <p>The The Amazon Resource Name (ARN) for a session.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_resource_dashboard_request.GetResourceDashboardRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_resource_dashboard_response.GetResourceDashboardResponse"
        ]:
            import capo_athena._operations.amazon_athena.get_resource_dashboard

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_resource_dashboard.async_get_resource_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_resource_dashboard_request.GetResourceDashboardRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_session_response.GetSessionResponse":
        """<p>Gets the full details of a previously created session, including the session status and configuration.</p>

        Args:
            session_id: <p>The session ID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_session_response.GetSessionResponse"
        ]:
            import capo_athena._operations.amazon_athena.get_session

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_session_request.GetSessionRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session_endpoint(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_session_endpoint_response.GetSessionEndpointResponse":
        """<p>Gets a connection endpoint and authentication token for a given session Id.</p>

        Args:
            session_id: <p>The session ID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_session_endpoint_request.GetSessionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_session_endpoint_response.GetSessionEndpointResponse"
        ]:
            import capo_athena._operations.amazon_athena.get_session_endpoint

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_session_endpoint.async_get_session_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_session_endpoint_request.GetSessionEndpointRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session_status(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_session_status_response.GetSessionStatusResponse":
        """<p>Gets the current status of a session.</p>

        Args:
            session_id: <p>The session ID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_session_status_request.GetSessionStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_session_status_response.GetSessionStatusResponse"
        ]:
            import capo_athena._operations.amazon_athena.get_session_status

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_session_status.async_get_session_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_session_status_request.GetSessionStatusRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_metadata(
        self,
        catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString",
        database_name: "capo_athena.types.name_string.NameString",
        table_name: "capo_athena.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.get_table_metadata_output.GetTableMetadataOutput":
        """<p>Returns table metadata for the specified catalog, database, and table.</p>

        Args:
            catalog_name: <p>The name of the data catalog that contains the database and table metadata to return.</p>
            database_name: <p>The name of the database that contains the table metadata to return.</p>
            table_name: <p>The name of the table for which metadata is returned.</p>
            work_group: <p>The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled Glue Data Catalog.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.metadata_exception.MetadataException: <p>An exception that Athena received when it called a custom metastore. Occurs if the error is not caused by user input (<code>InvalidRequestException</code>) or from the Athena platform (<code>InternalServerException</code>). For example, if a user-created Lambda function is missing permissions, the Lambda <code>4XX</code> exception is returned in a <code>MetadataException</code>.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_table_metadata_input.GetTableMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_table_metadata_output.GetTableMetadataOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_table_metadata

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_table_metadata.async_get_table_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_table_metadata_input.GetTableMetadataInput = {
            "catalog_name": catalog_name,
            "database_name": database_name,
            "table_name": table_name,
        }
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_work_group(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.get_work_group_output.GetWorkGroupOutput":
        """<p>Returns information about the workgroup with the specified name.</p>

        Args:
            work_group: <p>The name of the workgroup.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.get_work_group_input.GetWorkGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.get_work_group_output.GetWorkGroupOutput"
        ]:
            import capo_athena._operations.amazon_athena.get_work_group

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.get_work_group.async_get_work_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.get_work_group_input.GetWorkGroupInput = {
            "work_group": work_group
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_notebook(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        name: "capo_athena.types.notebook_name.NotebookName",
        type: "capo_athena.types.notebook_type.NotebookType",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        payload: Optional["capo_athena.types.payload.Payload"] = None,
        notebook_s3_location_uri: Optional["capo_athena.types.s3_uri.S3Uri"] = None,
        client_request_token: Optional[
            "capo_athena.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_athena.types.import_notebook_output.ImportNotebookOutput":
        """<p>Imports a single <code>ipynb</code> file to a Spark enabled workgroup. To import the notebook, the request must specify a value for either <code>Payload</code> or <code>NoteBookS3LocationUri</code>. If neither is specified or both are specified, an <code>InvalidRequestException</code> occurs. The maximum file size that can be imported is 10 megabytes. If an <code>ipynb</code> file with the same name already exists in the workgroup, throws an error.</p>

        Args:
            work_group: <p>The name of the Spark enabled workgroup to import the notebook to.</p>
            name: <p>The name of the notebook to import.</p>
            payload: <p>The notebook content to be imported. The payload must be in <code>ipynb</code> format.</p>
            type: <p>The notebook content type. Currently, the only valid type is <code>IPYNB</code>.</p>
            notebook_s3_location_uri: <p>A URI that specifies the Amazon S3 location of a notebook file in <code>ipynb</code> format.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to import the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.import_notebook_input.ImportNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.import_notebook_output.ImportNotebookOutput"
        ]:
            import capo_athena._operations.amazon_athena.import_notebook

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.import_notebook.async_import_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.import_notebook_input.ImportNotebookInput = {
            "work_group": work_group,
            "name": name,
            "type": type,
        }
        if payload is not None:
            input_["payload"] = payload
        if notebook_s3_location_uri is not None:
            input_["notebook_s3_location_uri"] = notebook_s3_location_uri
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_application_dpu_sizes(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        max_results: Optional[
            "capo_athena.types.max_application_dpu_sizes_count.MaxApplicationDPUSizesCount"
        ] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
    ) -> "capo_athena.types.list_application_dpu_sizes_output.ListApplicationDPUSizesOutput":
        """<p>Returns the supported DPU sizes for the supported application runtimes (for example, <code>Athena notebook version 1</code>). </p>

        Args:
            max_results: <p>Specifies the maximum number of results to return.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_application_dpu_sizes_input.ListApplicationDPUSizesInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_application_dpu_sizes_output.ListApplicationDPUSizesOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_application_dpu_sizes

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_application_dpu_sizes.async_list_application_dpu_sizes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_application_dpu_sizes_input.ListApplicationDPUSizesInput = {}
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

    async def iter_list_application_dpu_sizes(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        max_results: Optional[
            "capo_athena.types.max_application_dpu_sizes_count.MaxApplicationDPUSizesCount"
        ] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_athena.types.list_application_dpu_sizes_output.ListApplicationDPUSizesOutput]":
        _token = next_token
        while True:
            _response = await self.list_application_dpu_sizes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_calculation_executions(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        state_filter: Optional[
            "capo_athena.types.calculation_execution_state.CalculationExecutionState"
        ] = None,
        max_results: Optional[
            "capo_athena.types.max_calculations_count.MaxCalculationsCount"
        ] = None,
        next_token: Optional[
            "capo_athena.types.session_manager_token.SessionManagerToken"
        ] = None,
    ) -> "capo_athena.types.list_calculation_executions_response.ListCalculationExecutionsResponse":
        """<p>Lists the calculations that have been submitted to a session in descending order. Newer calculations are listed first; older calculations are listed later.</p>

        Args:
            session_id: <p>The session ID.</p>
            state_filter: <p>A filter for a specific calculation execution state. A description of each state follows.</p> <p> <code>CREATING</code> - The calculation is in the process of being created.</p> <p> <code>CREATED</code> - The calculation has been created and is ready to run.</p> <p> <code>QUEUED</code> - The calculation has been queued for processing.</p> <p> <code>RUNNING</code> - The calculation is running.</p> <p> <code>CANCELING</code> - A request to cancel the calculation has been received and the system is working to stop it.</p> <p> <code>CANCELED</code> - The calculation is no longer running as the result of a cancel request.</p> <p> <code>COMPLETED</code> - The calculation has completed without error.</p> <p> <code>FAILED</code> - The calculation failed and is no longer running.</p>
            max_results: <p>The maximum number of calculation executions to return.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_calculation_executions_request.ListCalculationExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_calculation_executions_response.ListCalculationExecutionsResponse"
        ]:
            import capo_athena._operations.amazon_athena.list_calculation_executions

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_calculation_executions.async_list_calculation_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_calculation_executions_request.ListCalculationExecutionsRequest = {
            "session_id": session_id
        }
        if state_filter is not None:
            input_["state_filter"] = state_filter
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

    async def iter_list_calculation_executions(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        state_filter: Optional[
            "capo_athena.types.calculation_execution_state.CalculationExecutionState"
        ] = None,
        max_results: Optional[
            "capo_athena.types.max_calculations_count.MaxCalculationsCount"
        ] = None,
        next_token: Optional[
            "capo_athena.types.session_manager_token.SessionManagerToken"
        ] = None,
    ) -> "AsyncIterator[capo_athena.types.list_calculation_executions_response.ListCalculationExecutionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_calculation_executions(
                session_id,
                config_overrides=config_overrides,
                state_filter=state_filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_capacity_reservations(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_capacity_reservations_count.MaxCapacityReservationsCount"
        ] = None,
    ) -> "capo_athena.types.list_capacity_reservations_output.ListCapacityReservationsOutput":
        """<p>Lists the capacity reservations for the current account.</p>

        Args:
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated.</p>
            max_results: <p>Specifies the maximum number of results to return.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_capacity_reservations_input.ListCapacityReservationsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_capacity_reservations_output.ListCapacityReservationsOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_capacity_reservations

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_capacity_reservations.async_list_capacity_reservations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_capacity_reservations_input.ListCapacityReservationsInput = {}
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

    async def iter_list_capacity_reservations(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_capacity_reservations_count.MaxCapacityReservationsCount"
        ] = None,
    ) -> "AsyncIterator[capo_athena.types.list_capacity_reservations_output.ListCapacityReservationsOutput]":
        _token = next_token
        while True:
            _response = await self.list_capacity_reservations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_databases(
        self,
        catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_databases_count.MaxDatabasesCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.list_databases_output.ListDatabasesOutput":
        """<p>Lists the databases in the specified data catalog.</p>

        Args:
            catalog_name: <p>The name of the data catalog that contains the databases to return.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>
            max_results: <p>Specifies the maximum number of results to return.</p>
            work_group: <p>The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled Glue Data Catalog.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.metadata_exception.MetadataException: <p>An exception that Athena received when it called a custom metastore. Occurs if the error is not caused by user input (<code>InvalidRequestException</code>) or from the Athena platform (<code>InternalServerException</code>). For example, if a user-created Lambda function is missing permissions, the Lambda <code>4XX</code> exception is returned in a <code>MetadataException</code>.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_databases_input.ListDatabasesInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_databases_output.ListDatabasesOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_databases

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_databases.async_list_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_databases_input.ListDatabasesInput = {
            "catalog_name": catalog_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_databases(
        self,
        catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_databases_count.MaxDatabasesCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "AsyncIterator[capo_athena.types.database.Database]":
        _token = next_token
        while True:
            _response = await self.list_databases(
                catalog_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                work_group=work_group,
            )
            _page = _resolve_path(_response, ("database_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_catalogs(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_data_catalogs_count.MaxDataCatalogsCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.list_data_catalogs_output.ListDataCatalogsOutput":
        """<p>Lists the data catalogs in the current Amazon Web Services account.</p> <note> <p>In the Athena console, data catalogs are listed as "data sources" on the <b>Data sources</b> page under the <b>Data source name</b> column.</p> </note>

        Args:
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the NextToken from the response object of the previous page call.</p>
            max_results: <p>Specifies the maximum number of data catalogs to return.</p>
            work_group: <p>The name of the workgroup. Required if making an IAM Identity Center request.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_data_catalogs_input.ListDataCatalogsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_data_catalogs_output.ListDataCatalogsOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_data_catalogs

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_data_catalogs.async_list_data_catalogs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_data_catalogs_input.ListDataCatalogsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_data_catalogs(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_data_catalogs_count.MaxDataCatalogsCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "AsyncIterator[capo_athena.types.data_catalog_summary.DataCatalogSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_catalogs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                work_group=work_group,
            )
            _page = _resolve_path(_response, ("data_catalogs_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_engine_versions_count.MaxEngineVersionsCount"
        ] = None,
    ) -> "capo_athena.types.list_engine_versions_output.ListEngineVersionsOutput":
        """<p>Returns a list of engine versions that are available to choose from, including the Auto option.</p>

        Args:
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>
            max_results: <p>The maximum number of engine versions to return in this request.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_engine_versions_input.ListEngineVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_engine_versions_output.ListEngineVersionsOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_engine_versions

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_engine_versions.async_list_engine_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_engine_versions_input.ListEngineVersionsInput = {}
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

    async def iter_list_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_engine_versions_count.MaxEngineVersionsCount"
        ] = None,
    ) -> "AsyncIterator[capo_athena.types.list_engine_versions_output.ListEngineVersionsOutput]":
        _token = next_token
        while True:
            _response = await self.list_engine_versions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_executors(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        executor_state_filter: Optional[
            "capo_athena.types.executor_state.ExecutorState"
        ] = None,
        max_results: Optional[
            "capo_athena.types.max_list_executors_count.MaxListExecutorsCount"
        ] = None,
        next_token: Optional[
            "capo_athena.types.session_manager_token.SessionManagerToken"
        ] = None,
    ) -> "capo_athena.types.list_executors_response.ListExecutorsResponse":
        """<p>Lists, in descending order, the executors that joined a session. Newer executors are listed first; older executors are listed later. The result can be optionally filtered by state.</p>

        Args:
            session_id: <p>The session ID.</p>
            executor_state_filter: <p>A filter for a specific executor state. A description of each state follows.</p> <p> <code>CREATING</code> - The executor is being started, including acquiring resources.</p> <p> <code>CREATED</code> - The executor has been started.</p> <p> <code>REGISTERED</code> - The executor has been registered.</p> <p> <code>TERMINATING</code> - The executor is in the process of shutting down.</p> <p> <code>TERMINATED</code> - The executor is no longer running.</p> <p> <code>FAILED</code> - Due to a failure, the executor is no longer running.</p>
            max_results: <p>The maximum number of executors to return.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_executors_request.ListExecutorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_executors_response.ListExecutorsResponse"
        ]:
            import capo_athena._operations.amazon_athena.list_executors

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_executors.async_list_executors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_executors_request.ListExecutorsRequest = {
            "session_id": session_id
        }
        if executor_state_filter is not None:
            input_["executor_state_filter"] = executor_state_filter
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

    async def iter_list_executors(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        executor_state_filter: Optional[
            "capo_athena.types.executor_state.ExecutorState"
        ] = None,
        max_results: Optional[
            "capo_athena.types.max_list_executors_count.MaxListExecutorsCount"
        ] = None,
        next_token: Optional[
            "capo_athena.types.session_manager_token.SessionManagerToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_athena.types.list_executors_response.ListExecutorsResponse]"
    ):
        _token = next_token
        while True:
            _response = await self.list_executors(
                session_id,
                config_overrides=config_overrides,
                executor_state_filter=executor_state_filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_named_queries(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_named_queries_count.MaxNamedQueriesCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.list_named_queries_output.ListNamedQueriesOutput":
        """<p>Provides a list of available query IDs only for queries saved in the specified workgroup. Requires that you have access to the specified workgroup. If a workgroup is not specified, lists the saved queries for the primary workgroup.</p>

        Args:
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>
            max_results: <p>The maximum number of queries to return in this request.</p>
            work_group: <p>The name of the workgroup from which the named queries are being returned. If a workgroup is not specified, the saved queries for the primary workgroup are returned.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_named_queries_input.ListNamedQueriesInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_named_queries_output.ListNamedQueriesOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_named_queries

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_named_queries.async_list_named_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_named_queries_input.ListNamedQueriesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_named_queries(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_named_queries_count.MaxNamedQueriesCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "AsyncIterator[capo_athena.types.list_named_queries_output.ListNamedQueriesOutput]":
        _token = next_token
        while True:
            _response = await self.list_named_queries(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                work_group=work_group,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_notebook_metadata(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        filters: Optional[
            "capo_athena.types.filter_definition.FilterDefinition"
        ] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_notebooks_count.MaxNotebooksCount"
        ] = None,
    ) -> "capo_athena.types.list_notebook_metadata_output.ListNotebookMetadataOutput":
        """<p>Displays the notebook files for the specified workgroup in paginated format.</p>

        Args:
            filters: <p>Search filter string.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated.</p>
            max_results: <p>Specifies the maximum number of results to return.</p>
            work_group: <p>The name of the Spark enabled workgroup to retrieve notebook metadata for.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_notebook_metadata_input.ListNotebookMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_notebook_metadata_output.ListNotebookMetadataOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_notebook_metadata

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_notebook_metadata.async_list_notebook_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_notebook_metadata_input.ListNotebookMetadataInput = {
            "work_group": work_group
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

    async def list_notebook_sessions(
        self,
        notebook_id: "capo_athena.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        max_results: Optional[
            "capo_athena.types.max_sessions_count.MaxSessionsCount"
        ] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
    ) -> (
        "capo_athena.types.list_notebook_sessions_response.ListNotebookSessionsResponse"
    ):
        """<p>Lists, in descending order, the sessions that have been created in a notebook that are in an active state like <code>CREATING</code>, <code>CREATED</code>, <code>IDLE</code> or <code>BUSY</code>. Newer sessions are listed first; older sessions are listed later.</p>

        Args:
            notebook_id: <p>The ID of the notebook to list sessions for.</p>
            max_results: <p>The maximum number of notebook sessions to return.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_notebook_sessions_request.ListNotebookSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_notebook_sessions_response.ListNotebookSessionsResponse"
        ]:
            import capo_athena._operations.amazon_athena.list_notebook_sessions

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_notebook_sessions.async_list_notebook_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_notebook_sessions_request.ListNotebookSessionsRequest = {
            "notebook_id": notebook_id
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

    async def list_prepared_statements(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_prepared_statements_count.MaxPreparedStatementsCount"
        ] = None,
    ) -> (
        "capo_athena.types.list_prepared_statements_output.ListPreparedStatementsOutput"
    ):
        """<p>Lists the prepared statements in the specified workgroup.</p>

        Args:
            work_group: <p>The workgroup to list the prepared statements for.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_prepared_statements_input.ListPreparedStatementsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_prepared_statements_output.ListPreparedStatementsOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_prepared_statements

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_prepared_statements.async_list_prepared_statements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_prepared_statements_input.ListPreparedStatementsInput = {
            "work_group": work_group
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

    async def iter_list_prepared_statements(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_prepared_statements_count.MaxPreparedStatementsCount"
        ] = None,
    ) -> "AsyncIterator[capo_athena.types.list_prepared_statements_output.ListPreparedStatementsOutput]":
        _token = next_token
        while True:
            _response = await self.list_prepared_statements(
                work_group,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_query_executions(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_query_executions_count.MaxQueryExecutionsCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.list_query_executions_output.ListQueryExecutionsOutput":
        """<p>Provides a list of available query execution IDs for the queries in the specified workgroup. Athena keeps a query history for 45 days. If a workgroup is not specified, returns a list of query execution IDs for the primary workgroup. Requires you to have access to the workgroup in which the queries ran.</p>

        Args:
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>
            max_results: <p>The maximum number of query executions to return in this request.</p>
            work_group: <p>The name of the workgroup from which queries are being returned. If a workgroup is not specified, a list of available query execution IDs for the queries in the primary workgroup is returned.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_query_executions_input.ListQueryExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_query_executions_output.ListQueryExecutionsOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_query_executions

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_query_executions.async_list_query_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_query_executions_input.ListQueryExecutionsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_query_executions(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_query_executions_count.MaxQueryExecutionsCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "AsyncIterator[capo_athena.types.list_query_executions_output.ListQueryExecutionsOutput]":
        _token = next_token
        while True:
            _response = await self.list_query_executions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                work_group=work_group,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sessions(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        state_filter: Optional["capo_athena.types.session_state.SessionState"] = None,
        max_results: Optional[
            "capo_athena.types.max_sessions_count.MaxSessionsCount"
        ] = None,
        next_token: Optional[
            "capo_athena.types.session_manager_token.SessionManagerToken"
        ] = None,
    ) -> "capo_athena.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists the sessions in a workgroup that are in an active state like <code>CREATING</code>, <code>CREATED</code>, <code>IDLE</code>, or <code>BUSY</code>. Newer sessions are listed first; older sessions are listed later.</p>

        Args:
            work_group: <p>The workgroup to which the session belongs.</p>
            state_filter: <p>A filter for a specific session state. A description of each state follows.</p> <p> <code>CREATING</code> - The session is being started, including acquiring resources.</p> <p> <code>CREATED</code> - The session has been started.</p> <p> <code>IDLE</code> - The session is able to accept a calculation.</p> <p> <code>BUSY</code> - The session is processing another task and is unable to accept a calculation.</p> <p> <code>TERMINATING</code> - The session is in the process of shutting down.</p> <p> <code>TERMINATED</code> - The session and its resources are no longer running.</p> <p> <code>DEGRADED</code> - The session has no healthy coordinators.</p> <p> <code>FAILED</code> - Due to a failure, the session and its resources are no longer running.</p>
            max_results: <p>The maximum number of sessions to return.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_athena._operations.amazon_athena.list_sessions

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_sessions_request.ListSessionsRequest = {
            "work_group": work_group
        }
        if state_filter is not None:
            input_["state_filter"] = state_filter
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

    async def iter_list_sessions(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        state_filter: Optional["capo_athena.types.session_state.SessionState"] = None,
        max_results: Optional[
            "capo_athena.types.max_sessions_count.MaxSessionsCount"
        ] = None,
        next_token: Optional[
            "capo_athena.types.session_manager_token.SessionManagerToken"
        ] = None,
    ) -> "AsyncIterator[capo_athena.types.list_sessions_response.ListSessionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_sessions(
                work_group,
                config_overrides=config_overrides,
                state_filter=state_filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_table_metadata(
        self,
        catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString",
        database_name: "capo_athena.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        expression: Optional[
            "capo_athena.types.expression_string.ExpressionString"
        ] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_table_metadata_count.MaxTableMetadataCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "capo_athena.types.list_table_metadata_output.ListTableMetadataOutput":
        """<p>Lists the metadata for the tables in the specified data catalog database.</p>

        Args:
            catalog_name: <p>The name of the data catalog for which table metadata should be returned.</p>
            database_name: <p>The name of the database for which table metadata should be returned.</p>
            expression: <p>A regex filter that pattern-matches table names. If no expression is supplied, metadata for all tables are listed.</p>
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the NextToken from the response object of the previous page call.</p>
            max_results: <p>Specifies the maximum number of results to return.</p>
            work_group: <p>The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled Glue Data Catalog.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.metadata_exception.MetadataException: <p>An exception that Athena received when it called a custom metastore. Occurs if the error is not caused by user input (<code>InvalidRequestException</code>) or from the Athena platform (<code>InternalServerException</code>). For example, if a user-created Lambda function is missing permissions, the Lambda <code>4XX</code> exception is returned in a <code>MetadataException</code>.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_table_metadata_input.ListTableMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_table_metadata_output.ListTableMetadataOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_table_metadata

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_table_metadata.async_list_table_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_table_metadata_input.ListTableMetadataInput = {
            "catalog_name": catalog_name,
            "database_name": database_name,
        }
        if expression is not None:
            input_["expression"] = expression
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if work_group is not None:
            input_["work_group"] = work_group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_table_metadata(
        self,
        catalog_name: "capo_athena.types.catalog_name_string.CatalogNameString",
        database_name: "capo_athena.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        expression: Optional[
            "capo_athena.types.expression_string.ExpressionString"
        ] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_table_metadata_count.MaxTableMetadataCount"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
    ) -> "AsyncIterator[capo_athena.types.table_metadata.TableMetadata]":
        _token = next_token
        while True:
            _response = await self.list_table_metadata(
                catalog_name,
                database_name,
                config_overrides=config_overrides,
                expression=expression,
                next_token=_token,
                max_results=max_results,
                work_group=work_group,
            )
            _page = _resolve_path(_response, ("table_metadata_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional["capo_athena.types.max_tags_count.MaxTagsCount"] = None,
    ) -> "capo_athena.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with an Athena resource.</p>

        Args:
            resource_arn: <p>Lists the tags for the resource with the specified ARN.</p>
            next_token: <p>The token for the next set of results, or null if there are no additional results for this request, where the request lists the tags for the resource with the specified ARN.</p>
            max_results: <p>The maximum number of results to be returned per request that lists the tags for the resource.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
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

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional["capo_athena.types.max_tags_count.MaxTagsCount"] = None,
    ) -> "AsyncIterator[capo_athena.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_work_groups(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_work_groups_count.MaxWorkGroupsCount"
        ] = None,
    ) -> "capo_athena.types.list_work_groups_output.ListWorkGroupsOutput":
        """<p>Lists available workgroups for the account.</p>

        Args:
            next_token: <p>A token generated by the Athena service that specifies where to continue pagination if a previous request was truncated. To obtain the next set of pages, pass in the <code>NextToken</code> from the response object of the previous page call.</p>
            max_results: <p>The maximum number of workgroups to return in this request.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.list_work_groups_input.ListWorkGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.list_work_groups_output.ListWorkGroupsOutput"
        ]:
            import capo_athena._operations.amazon_athena.list_work_groups

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.list_work_groups.async_list_work_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.list_work_groups_input.ListWorkGroupsInput = {}
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

    async def iter_list_work_groups(
        self,
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        next_token: Optional["capo_athena.types.token.Token"] = None,
        max_results: Optional[
            "capo_athena.types.max_work_groups_count.MaxWorkGroupsCount"
        ] = None,
    ) -> (
        "AsyncIterator[capo_athena.types.list_work_groups_output.ListWorkGroupsOutput]"
    ):
        _token = next_token
        while True:
            _response = await self.list_work_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_capacity_assignment_configuration(
        self,
        capacity_reservation_name: "capo_athena.types.capacity_reservation_name.CapacityReservationName",
        capacity_assignments: "capo_athena.types.capacity_assignments_list.CapacityAssignmentsList",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.put_capacity_assignment_configuration_output.PutCapacityAssignmentConfigurationOutput":
        """<p>Puts a new capacity assignment configuration for a specified capacity reservation. If a capacity assignment configuration already exists for the capacity reservation, replaces the existing capacity assignment configuration.</p>

        Args:
            capacity_reservation_name: <p>The name of the capacity reservation to put a capacity assignment configuration for.</p>
            capacity_assignments: <p>The list of assignments for the capacity assignment configuration.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.put_capacity_assignment_configuration_input.PutCapacityAssignmentConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.put_capacity_assignment_configuration_output.PutCapacityAssignmentConfigurationOutput"
        ]:
            import capo_athena._operations.amazon_athena.put_capacity_assignment_configuration

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.put_capacity_assignment_configuration.async_put_capacity_assignment_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.put_capacity_assignment_configuration_input.PutCapacityAssignmentConfigurationInput = {
            "capacity_reservation_name": capacity_reservation_name,
            "capacity_assignments": capacity_assignments,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_calculation_execution(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.description_string.DescriptionString"
        ] = None,
        calculation_configuration: Optional[
            "capo_athena.types.calculation_configuration.CalculationConfiguration"
        ] = None,
        code_block: Optional["capo_athena.types.code_block.CodeBlock"] = None,
        client_request_token: Optional[
            "capo_athena.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_athena.types.start_calculation_execution_response.StartCalculationExecutionResponse":
        """<p>Submits calculations for execution within a session. You can supply the code to run as an inline code block within the request.</p> <note> <p>The request syntax requires the <a>StartCalculationExecutionRequest$CodeBlock</a> parameter or the <a>CalculationConfiguration$CodeBlock</a> parameter, but not both. Because <a>CalculationConfiguration$CodeBlock</a> is deprecated, use the <a>StartCalculationExecutionRequest$CodeBlock</a> parameter instead.</p> </note>

        Args:
            session_id: <p>The session ID.</p>
            description: <p>A description of the calculation.</p>
            calculation_configuration: <p>Contains configuration information for the calculation.</p>
            code_block: <p>A string that contains the code of the calculation. Use this parameter instead of <a>CalculationConfiguration$CodeBlock</a>, which is deprecated.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to create the calculation is idempotent (executes only once). If another <code>StartCalculationExecutionRequest</code> is received, the same response is returned and another calculation is not created. If a parameter has changed, an error is returned.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.start_calculation_execution_request.StartCalculationExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.start_calculation_execution_response.StartCalculationExecutionResponse"
        ]:
            import capo_athena._operations.amazon_athena.start_calculation_execution

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.start_calculation_execution.async_start_calculation_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.start_calculation_execution_request.StartCalculationExecutionRequest = {
            "session_id": session_id
        }
        if description is not None:
            input_["description"] = description
        if calculation_configuration is not None:
            input_["calculation_configuration"] = calculation_configuration
        if code_block is not None:
            input_["code_block"] = code_block
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_query_execution(
        self,
        query_string: "capo_athena.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        client_request_token: Optional[
            "capo_athena.types.idempotency_token.IdempotencyToken"
        ] = None,
        query_execution_context: Optional[
            "capo_athena.types.query_execution_context.QueryExecutionContext"
        ] = None,
        result_configuration: Optional[
            "capo_athena.types.result_configuration.ResultConfiguration"
        ] = None,
        work_group: Optional["capo_athena.types.work_group_name.WorkGroupName"] = None,
        execution_parameters: Optional[
            "capo_athena.types.execution_parameters.ExecutionParameters"
        ] = None,
        result_reuse_configuration: Optional[
            "capo_athena.types.result_reuse_configuration.ResultReuseConfiguration"
        ] = None,
        engine_configuration: Optional[
            "capo_athena.types.engine_configuration.EngineConfiguration"
        ] = None,
    ) -> "capo_athena.types.start_query_execution_output.StartQueryExecutionOutput":
        """<p>Runs the SQL query statements contained in the <code>Query</code>. Requires you to have access to the workgroup in which the query ran. Running queries against an external catalog requires <a>GetDataCatalog</a> permission to the catalog. For code samples using the Amazon Web Services SDK for Java, see <a href="http://docs.aws.amazon.com/athena/latest/ug/code-samples.html">Examples and Code Samples</a> in the <i>Amazon Athena User Guide</i>.</p>

        Args:
            query_string: <p>The SQL query statements to be executed.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another <code>StartQueryExecution</code> request is received, the same response is returned and another query is not created. An error is returned if a parameter, such as <code>QueryString</code>, has changed. A call to <code>StartQueryExecution</code> that uses a previous client request token returns the same <code>QueryExecutionId</code> even if the requester doesn't have permission on the tables specified in <code>QueryString</code>.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>
            query_execution_context: <p>The database within which the query executes.</p>
            result_configuration: <p>Specifies information about where and how to save the results of the query execution. If the query runs in a workgroup, then workgroup's settings may override query settings. This affects the query results location. The workgroup settings override is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>
            work_group: <p>The name of the workgroup in which the query is being started.</p>
            execution_parameters: <p>A list of values for the parameters in a query. The values are applied sequentially to the parameters in the query in the order in which the parameters occur.</p>
            result_reuse_configuration: <p>Specifies the query result reuse behavior for the query.</p>
            engine_configuration: <p>The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).</p> <p>To specify minimum and maximum DPU values for Capacity Reservations queries, the workgroup containing <code>EngineConfiguration</code> should have the following values: The name of the <code>Classifications</code> should be <code>athena-query-engine-properties</code>, with the only allowed properties as <code>max-dpu-count</code> and <code>min-dpu-count</code>.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.start_query_execution_input.StartQueryExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.start_query_execution_output.StartQueryExecutionOutput"
        ]:
            import capo_athena._operations.amazon_athena.start_query_execution

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.start_query_execution.async_start_query_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.start_query_execution_input.StartQueryExecutionInput = {
            "query_string": query_string
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if query_execution_context is not None:
            input_["query_execution_context"] = query_execution_context
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if work_group is not None:
            input_["work_group"] = work_group
        if execution_parameters is not None:
            input_["execution_parameters"] = execution_parameters
        if result_reuse_configuration is not None:
            input_["result_reuse_configuration"] = result_reuse_configuration
        if engine_configuration is not None:
            input_["engine_configuration"] = engine_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_session(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        engine_configuration: "capo_athena.types.engine_configuration.EngineConfiguration",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.description_string.DescriptionString"
        ] = None,
        execution_role: Optional["capo_athena.types.role_arn.RoleArn"] = None,
        monitoring_configuration: Optional[
            "capo_athena.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
        notebook_version: Optional["capo_athena.types.name_string.NameString"] = None,
        session_idle_timeout_in_minutes: Optional[
            "capo_athena.types.session_idle_timeout_in_minutes.SessionIdleTimeoutInMinutes"
        ] = None,
        client_request_token: Optional[
            "capo_athena.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_athena.types.tag_list.TagList"] = None,
        copy_work_group_tags: Optional[
            "capo_athena.types.boxed_boolean.BoxedBoolean"
        ] = None,
    ) -> "capo_athena.types.start_session_response.StartSessionResponse":
        """<p>Creates a session for running calculations within a workgroup. The session is ready when it reaches an <code>IDLE</code> state.</p>

        Args:
            description: <p>The session description.</p>
            work_group: <p>The workgroup to which the session belongs.</p>
            engine_configuration: <p>Contains engine data processing unit (DPU) configuration settings and parameter mappings.</p>
            execution_role: <p>The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.</p>
            monitoring_configuration: <p>Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.</p>
            notebook_version: <p>The notebook version. This value is supplied automatically for notebook sessions in the Athena console and is not required for programmatic session access. The only valid notebook version is <code>Athena notebook version 1</code>. If you specify a value for <code>NotebookVersion</code>, you must also specify a value for <code>NotebookId</code>. See <a>EngineConfiguration$AdditionalConfigs</a>.</p>
            session_idle_timeout_in_minutes: <p>The idle timeout in minutes for the session.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to create the session is idempotent (executes only once). If another <code>StartSessionRequest</code> is received, the same response is returned and another session is not created. If a parameter has changed, an error is returned.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>
            tags: <p>A list of comma separated tags to add to the session that is created.</p>
            copy_work_group_tags: <p>Copies the tags from the Workgroup to the Session when.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.session_already_exists_exception.SessionAlreadyExistsException: <p>The specified session already exists.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.start_session_request.StartSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.start_session_response.StartSessionResponse"
        ]:
            import capo_athena._operations.amazon_athena.start_session

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.start_session.async_start_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.start_session_request.StartSessionRequest = {
            "work_group": work_group,
            "engine_configuration": engine_configuration,
        }
        if description is not None:
            input_["description"] = description
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if monitoring_configuration is not None:
            input_["monitoring_configuration"] = monitoring_configuration
        if notebook_version is not None:
            input_["notebook_version"] = notebook_version
        if session_idle_timeout_in_minutes is not None:
            input_["session_idle_timeout_in_minutes"] = session_idle_timeout_in_minutes
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if copy_work_group_tags is not None:
            input_["copy_work_group_tags"] = copy_work_group_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_calculation_execution(
        self,
        calculation_execution_id: "capo_athena.types.calculation_execution_id.CalculationExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.stop_calculation_execution_response.StopCalculationExecutionResponse":
        """<p>Requests the cancellation of a calculation. A <code>StopCalculationExecution</code> call on a calculation that is already in a terminal state (for example, <code>STOPPED</code>, <code>FAILED</code>, or <code>COMPLETED</code>) succeeds but has no effect.</p> <note> <p>Cancelling a calculation is done on a best effort basis. If a calculation cannot be cancelled, you can be charged for its completion. If you are concerned about being charged for a calculation that cannot be cancelled, consider terminating the session in which the calculation is running.</p> </note>

        Args:
            calculation_execution_id: <p>The calculation execution UUID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.stop_calculation_execution_request.StopCalculationExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.stop_calculation_execution_response.StopCalculationExecutionResponse"
        ]:
            import capo_athena._operations.amazon_athena.stop_calculation_execution

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.stop_calculation_execution.async_stop_calculation_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.stop_calculation_execution_request.StopCalculationExecutionRequest = {
            "calculation_execution_id": calculation_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_query_execution(
        self,
        query_execution_id: "capo_athena.types.query_execution_id.QueryExecutionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.stop_query_execution_output.StopQueryExecutionOutput":
        """<p>Stops a query execution. Requires you to have access to the workgroup in which the query ran.</p>

        Args:
            query_execution_id: <p>The unique ID of the query execution to stop.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.stop_query_execution_input.StopQueryExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.stop_query_execution_output.StopQueryExecutionOutput"
        ]:
            import capo_athena._operations.amazon_athena.stop_query_execution

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.stop_query_execution.async_stop_query_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.stop_query_execution_input.StopQueryExecutionInput = {
            "query_execution_id": query_execution_id
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
        resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_athena.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.tag_resource_output.TagResourceOutput":
        """<p>Adds one or more tags to an Athena resource. A tag is a label that you assign to a resource. Each tag consists of a key and an optional value, both of which you define. For example, you can use tags to categorize Athena workgroups, data catalogs, or capacity reservations by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter the resources in your account. For best practices, see <a href="https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html">Tagging Best Practices</a>. Tag keys can be from 1 to 128 UTF-8 Unicode characters, and tag values can be from 0 to 256 UTF-8 Unicode characters. Tags can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource. If you specify more than one tag, separate them by commas.</p>

        Args:
            resource_arn: <p>Specifies the ARN of the Athena resource to which tags are to be added.</p>
            tags: <p>A collection of one or more tags, separated by commas, to be added to an Athena resource.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_athena._operations.amazon_athena.tag_resource

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.tag_resource_input.TagResourceInput = {
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

    async def terminate_session(
        self,
        session_id: "capo_athena.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.terminate_session_response.TerminateSessionResponse":
        """<p>Terminates an active session. A <code>TerminateSession</code> call on a session that is already inactive (for example, in a <code>FAILED</code>, <code>TERMINATED</code> or <code>TERMINATING</code> state) succeeds but has no effect. Calculations running in the session when <code>TerminateSession</code> is called are forcefully stopped, but may display as <code>FAILED</code> instead of <code>STOPPED</code>.</p>

        Args:
            session_id: <p>The session ID.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.terminate_session_request.TerminateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.terminate_session_response.TerminateSessionResponse"
        ]:
            import capo_athena._operations.amazon_athena.terminate_session

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.terminate_session.async_terminate_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.terminate_session_request.TerminateSessionRequest = {
            "session_id": session_id
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
        resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_athena.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from an Athena resource.</p>

        Args:
            resource_arn: <p>Specifies the ARN of the resource from which tags are to be removed.</p>
            tag_keys: <p>A comma-separated list of one or more tag keys whose tags are to be removed from the specified resource.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_athena._operations.amazon_athena.untag_resource

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.untag_resource_input.UntagResourceInput = {
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

    async def update_capacity_reservation(
        self,
        target_dpus: "capo_athena.types.target_dpus_integer.TargetDpusInteger",
        name: "capo_athena.types.capacity_reservation_name.CapacityReservationName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
    ) -> "capo_athena.types.update_capacity_reservation_output.UpdateCapacityReservationOutput":
        """<p>Updates the number of requested data processing units for the capacity reservation with the specified name.</p>

        Args:
            target_dpus: <p>The new number of requested data processing units.</p>
            name: <p>The name of the capacity reservation.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.update_capacity_reservation_input.UpdateCapacityReservationInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.update_capacity_reservation_output.UpdateCapacityReservationOutput"
        ]:
            import capo_athena._operations.amazon_athena.update_capacity_reservation

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.update_capacity_reservation.async_update_capacity_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.update_capacity_reservation_input.UpdateCapacityReservationInput = {
            "target_dpus": target_dpus,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_catalog(
        self,
        name: "capo_athena.types.catalog_name_string.CatalogNameString",
        type: "capo_athena.types.data_catalog_type.DataCatalogType",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.description_string.DescriptionString"
        ] = None,
        parameters: Optional["capo_athena.types.parameters_map.ParametersMap"] = None,
    ) -> "capo_athena.types.update_data_catalog_output.UpdateDataCatalogOutput":
        """<p>Updates the data catalog that has the specified name.</p>

        Args:
            name: <p>The name of the data catalog to update. The catalog name must be unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.</p>
            type: <p>Specifies the type of data catalog to update. Specify <code>LAMBDA</code> for a federated catalog, <code>HIVE</code> for an external hive metastore, or <code>GLUE</code> for an Glue Data Catalog.</p>
            description: <p>New or modified text that describes the data catalog.</p>
            parameters: <p>Specifies the Lambda function or functions to use for updating the data catalog. This is a mapping whose values depend on the catalog type. </p> <ul> <li> <p>For the <code>HIVE</code> data catalog type, use the following syntax. The <code>metadata-function</code> parameter is required. <code>The sdk-version</code> parameter is optional and defaults to the currently supported version.</p> <p> <code>metadata-function=<i>lambda_arn</i>, sdk-version=<i>version_number</i> </code> </p> </li> <li> <p>For the <code>LAMBDA</code> data catalog type, use one of the following sets of required parameters, but not both.</p> <ul> <li> <p>If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.</p> <p> <code>metadata-function=<i>lambda_arn</i>, record-function=<i>lambda_arn</i> </code> </p> </li> <li> <p> If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.</p> <p> <code>function=<i>lambda_arn</i> </code> </p> </li> </ul> </li> </ul>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.update_data_catalog_input.UpdateDataCatalogInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.update_data_catalog_output.UpdateDataCatalogOutput"
        ]:
            import capo_athena._operations.amazon_athena.update_data_catalog

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.update_data_catalog.async_update_data_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.update_data_catalog_input.UpdateDataCatalogInput = {
            "name": name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_named_query(
        self,
        named_query_id: "capo_athena.types.named_query_id.NamedQueryId",
        name: "capo_athena.types.name_string.NameString",
        query_string: "capo_athena.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.named_query_description_string.NamedQueryDescriptionString"
        ] = None,
    ) -> "capo_athena.types.update_named_query_output.UpdateNamedQueryOutput":
        """<p>Updates a <a>NamedQuery</a> object. The database or workgroup cannot be updated.</p>

        Args:
            named_query_id: <p>The unique identifier (UUID) of the query.</p>
            name: <p>The name of the query.</p>
            description: <p>The query description.</p>
            query_string: <p>The contents of the query with all query statements.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.update_named_query_input.UpdateNamedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.update_named_query_output.UpdateNamedQueryOutput"
        ]:
            import capo_athena._operations.amazon_athena.update_named_query

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.update_named_query.async_update_named_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.update_named_query_input.UpdateNamedQueryInput = {
            "named_query_id": named_query_id,
            "name": name,
            "query_string": query_string,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_notebook(
        self,
        notebook_id: "capo_athena.types.notebook_id.NotebookId",
        payload: "capo_athena.types.payload.Payload",
        type: "capo_athena.types.notebook_type.NotebookType",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        session_id: Optional["capo_athena.types.session_id.SessionId"] = None,
        client_request_token: Optional[
            "capo_athena.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_athena.types.update_notebook_output.UpdateNotebookOutput":
        """<p>Updates the contents of a Spark notebook.</p>

        Args:
            notebook_id: <p>The ID of the notebook to update.</p>
            payload: <p>The updated content for the notebook.</p>
            type: <p>The notebook content type. Currently, the only valid type is <code>IPYNB</code>.</p>
            session_id: <p>The active notebook session ID. Required if the notebook has an active session.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.update_notebook_input.UpdateNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.update_notebook_output.UpdateNotebookOutput"
        ]:
            import capo_athena._operations.amazon_athena.update_notebook

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.update_notebook.async_update_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.update_notebook_input.UpdateNotebookInput = {
            "notebook_id": notebook_id,
            "payload": payload,
            "type": type,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_notebook_metadata(
        self,
        notebook_id: "capo_athena.types.notebook_id.NotebookId",
        name: "capo_athena.types.notebook_name.NotebookName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        client_request_token: Optional[
            "capo_athena.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> (
        "capo_athena.types.update_notebook_metadata_output.UpdateNotebookMetadataOutput"
    ):
        """<p>Updates the metadata for a notebook.</p>

        Args:
            notebook_id: <p>The ID of the notebook to update the metadata for.</p>
            client_request_token: <p>A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>
            name: <p>The name to update the notebook to.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.too_many_requests_exception.TooManyRequestsException: <p>Indicates that the request was throttled.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.update_notebook_metadata_input.UpdateNotebookMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.update_notebook_metadata_output.UpdateNotebookMetadataOutput"
        ]:
            import capo_athena._operations.amazon_athena.update_notebook_metadata

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.update_notebook_metadata.async_update_notebook_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.update_notebook_metadata_input.UpdateNotebookMetadataInput = {
            "notebook_id": notebook_id,
            "name": name,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_prepared_statement(
        self,
        statement_name: "capo_athena.types.statement_name.StatementName",
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        query_statement: "capo_athena.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.description_string.DescriptionString"
        ] = None,
    ) -> "capo_athena.types.update_prepared_statement_output.UpdatePreparedStatementOutput":
        """<p>Updates a prepared statement.</p>

        Args:
            statement_name: <p>The name of the prepared statement.</p>
            work_group: <p>The workgroup for the prepared statement.</p>
            query_statement: <p>The query string for the prepared statement.</p>
            description: <p>The description of the prepared statement.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource, such as a workgroup, was not found.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.update_prepared_statement_input.UpdatePreparedStatementInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.update_prepared_statement_output.UpdatePreparedStatementOutput"
        ]:
            import capo_athena._operations.amazon_athena.update_prepared_statement

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.update_prepared_statement.async_update_prepared_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.update_prepared_statement_input.UpdatePreparedStatementInput = {
            "statement_name": statement_name,
            "work_group": work_group,
            "query_statement": query_statement,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_work_group(
        self,
        work_group: "capo_athena.types.work_group_name.WorkGroupName",
        *,
        config_overrides: Optional[AsyncAthenaClientConfig] = None,
        description: Optional[
            "capo_athena.types.work_group_description_string.WorkGroupDescriptionString"
        ] = None,
        configuration_updates: Optional[
            "capo_athena.types.work_group_configuration_updates.WorkGroupConfigurationUpdates"
        ] = None,
        state: Optional["capo_athena.types.work_group_state.WorkGroupState"] = None,
    ) -> "capo_athena.types.update_work_group_output.UpdateWorkGroupOutput":
        """<p>Updates the workgroup with the specified name. The workgroup's name cannot be changed. Only <code>ConfigurationUpdates</code> can be specified.</p>

        Args:
            work_group: <p>The specified workgroup that will be updated.</p>
            description: <p>The workgroup description.</p>
            configuration_updates: <p>Contains configuration updates for an Athena SQL workgroup.</p>
            state: <p>The workgroup state that will be updated for the given workgroup.</p>

        Raises:
            capo_athena.errors.internal_server_exception.InternalServerException: <p>Indicates a platform issue, which may be due to a transient condition or outage.</p>
            capo_athena.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.</p>
            capo_athena.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_athena.types.update_work_group_input.UpdateWorkGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_athena.types.update_work_group_output.UpdateWorkGroupOutput"
        ]:
            import capo_athena._operations.amazon_athena.update_work_group

            (
                output,
                http_response,
            ) = await capo_athena._operations.amazon_athena.update_work_group.async_update_work_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_athena.types.update_work_group_input.UpdateWorkGroupInput = {
            "work_group": work_group
        }
        if description is not None:
            input_["description"] = description
        if configuration_updates is not None:
            input_["configuration_updates"] = configuration_updates
        if state is not None:
            input_["state"] = state

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

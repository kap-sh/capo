"""Generated from Smithy shape ``com.amazonaws.neptunegraph#AmazonNeptuneGraph``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_neptune_graph._auth._signers
import capo_neptune_graph._auth._sigv4
from capo_neptune_graph._auth._identity import Credentials
from capo_neptune_graph._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_neptune_graph._auth._zapros_handler import AuthMiddleware
from capo_neptune_graph._pagination import resolve_path as _resolve_path
from capo_neptune_graph._resources.amazon_neptune_graph.graph_resource import (
    AsyncGraphResource,
)
from capo_neptune_graph._resources.amazon_neptune_graph.private_graph_endpoint_resource import (
    AsyncPrivateGraphEndpointResource,
)
from capo_neptune_graph._resources.amazon_neptune_graph.snapshot_resource import (
    AsyncSnapshotResource,
)
from capo_neptune_graph._resources.amazon_neptune_graph.task_resource import (
    AsyncTaskResource,
)
from capo_neptune_graph._services._aws_config import aaws_config
from capo_neptune_graph._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_neptune_graph.types.arn
    import capo_neptune_graph.types.blank_node_handling
    import capo_neptune_graph.types.cancel_export_task_input
    import capo_neptune_graph.types.cancel_export_task_output
    import capo_neptune_graph.types.cancel_import_task_input
    import capo_neptune_graph.types.cancel_import_task_output
    import capo_neptune_graph.types.cancel_query_input
    import capo_neptune_graph.types.create_graph_input
    import capo_neptune_graph.types.create_graph_output
    import capo_neptune_graph.types.create_graph_snapshot_input
    import capo_neptune_graph.types.create_graph_snapshot_output
    import capo_neptune_graph.types.create_graph_using_import_task_input
    import capo_neptune_graph.types.create_graph_using_import_task_output
    import capo_neptune_graph.types.create_private_graph_endpoint_input
    import capo_neptune_graph.types.create_private_graph_endpoint_output
    import capo_neptune_graph.types.delete_graph_input
    import capo_neptune_graph.types.delete_graph_output
    import capo_neptune_graph.types.delete_graph_snapshot_input
    import capo_neptune_graph.types.delete_graph_snapshot_output
    import capo_neptune_graph.types.delete_private_graph_endpoint_input
    import capo_neptune_graph.types.delete_private_graph_endpoint_output
    import capo_neptune_graph.types.document_valued_map
    import capo_neptune_graph.types.execute_query_input
    import capo_neptune_graph.types.execute_query_output
    import capo_neptune_graph.types.explain_mode
    import capo_neptune_graph.types.export_filter
    import capo_neptune_graph.types.export_format
    import capo_neptune_graph.types.export_task_id
    import capo_neptune_graph.types.export_task_summary
    import capo_neptune_graph.types.format
    import capo_neptune_graph.types.get_export_task_input
    import capo_neptune_graph.types.get_export_task_output
    import capo_neptune_graph.types.get_graph_input
    import capo_neptune_graph.types.get_graph_output
    import capo_neptune_graph.types.get_graph_snapshot_input
    import capo_neptune_graph.types.get_graph_snapshot_output
    import capo_neptune_graph.types.get_graph_summary_input
    import capo_neptune_graph.types.get_graph_summary_output
    import capo_neptune_graph.types.get_import_task_input
    import capo_neptune_graph.types.get_import_task_output
    import capo_neptune_graph.types.get_private_graph_endpoint_input
    import capo_neptune_graph.types.get_private_graph_endpoint_output
    import capo_neptune_graph.types.get_query_input
    import capo_neptune_graph.types.get_query_output
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.graph_name
    import capo_neptune_graph.types.graph_snapshot_summary
    import capo_neptune_graph.types.graph_summary
    import capo_neptune_graph.types.graph_summary_mode
    import capo_neptune_graph.types.import_options
    import capo_neptune_graph.types.import_task_summary
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.list_export_tasks_input
    import capo_neptune_graph.types.list_export_tasks_output
    import capo_neptune_graph.types.list_graph_snapshots_input
    import capo_neptune_graph.types.list_graph_snapshots_output
    import capo_neptune_graph.types.list_graphs_input
    import capo_neptune_graph.types.list_graphs_output
    import capo_neptune_graph.types.list_import_tasks_input
    import capo_neptune_graph.types.list_import_tasks_output
    import capo_neptune_graph.types.list_private_graph_endpoints_input
    import capo_neptune_graph.types.list_private_graph_endpoints_output
    import capo_neptune_graph.types.list_queries_input
    import capo_neptune_graph.types.list_queries_output
    import capo_neptune_graph.types.list_tags_for_resource_input
    import capo_neptune_graph.types.list_tags_for_resource_output
    import capo_neptune_graph.types.max_results
    import capo_neptune_graph.types.pagination_token
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.plan_cache_type
    import capo_neptune_graph.types.private_graph_endpoint_summary
    import capo_neptune_graph.types.provisioned_memory
    import capo_neptune_graph.types.query_language
    import capo_neptune_graph.types.query_state_input
    import capo_neptune_graph.types.replica_count
    import capo_neptune_graph.types.reset_graph_input
    import capo_neptune_graph.types.reset_graph_output
    import capo_neptune_graph.types.restore_graph_from_snapshot_input
    import capo_neptune_graph.types.restore_graph_from_snapshot_output
    import capo_neptune_graph.types.role_arn
    import capo_neptune_graph.types.security_group_ids
    import capo_neptune_graph.types.snapshot_identifier
    import capo_neptune_graph.types.snapshot_name
    import capo_neptune_graph.types.start_export_task_input
    import capo_neptune_graph.types.start_export_task_output
    import capo_neptune_graph.types.start_graph_input
    import capo_neptune_graph.types.start_graph_output
    import capo_neptune_graph.types.start_import_task_input
    import capo_neptune_graph.types.start_import_task_output
    import capo_neptune_graph.types.stop_graph_input
    import capo_neptune_graph.types.stop_graph_output
    import capo_neptune_graph.types.subnet_ids
    import capo_neptune_graph.types.tag_key_list
    import capo_neptune_graph.types.tag_map
    import capo_neptune_graph.types.tag_resource_input
    import capo_neptune_graph.types.tag_resource_output
    import capo_neptune_graph.types.task_id
    import capo_neptune_graph.types.untag_resource_input
    import capo_neptune_graph.types.untag_resource_output
    import capo_neptune_graph.types.update_graph_input
    import capo_neptune_graph.types.update_graph_output
    import capo_neptune_graph.types.vector_search_configuration
    import capo_neptune_graph.types.vpc_id


class AsyncNeptuneGraphClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    use_dual_stack: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncNeptuneGraphClient:
    """A client for the ``NeptuneGraph`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
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
        use_fips: bool | None = None,
        use_dual_stack: bool | None = None,
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
        self._config = AsyncNeptuneGraphClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "use_dual_stack": use_dual_stack,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.graph_resource = AsyncGraphResource(self)
        self.private_graph_endpoint_resource = AsyncPrivateGraphEndpointResource(self)
        self.snapshot_resource = AsyncSnapshotResource(self)
        self.task_resource = AsyncTaskResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNeptuneGraphClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def cancel_query(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> None:
        """<p>Cancels a specified query.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            query_id: <p>The unique identifier of the query to cancel.</p>

        Raises:
            capo_neptune_graph.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.cancel_query_input.CancelQueryInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune_graph._operations.amazon_neptune_graph.cancel_query

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.cancel_query.async_cancel_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.cancel_query_input.CancelQueryInput = {
            "graph_identifier": graph_identifier,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def execute_query(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        query_string: str,
        language: "capo_neptune_graph.types.query_language.QueryLanguage",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        parameters: Optional[
            "capo_neptune_graph.types.document_valued_map.DocumentValuedMap"
        ] = None,
        plan_cache: Optional[
            "capo_neptune_graph.types.plan_cache_type.PlanCacheType"
        ] = None,
        explain_mode: Optional[
            "capo_neptune_graph.types.explain_mode.ExplainMode"
        ] = None,
        query_timeout_milliseconds: Optional[int] = None,
    ) -> "AsyncGenerator[capo_neptune_graph.types.execute_query_output.ExecuteQueryOutput]":
        """<p>Execute an openCypher query.</p> <p> When invoking this operation in a Neptune Analytics cluster, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query: </p> <ul> <li> <p>neptune-graph:ReadDataViaQuery</p> </li> <li> <p>neptune-graph:WriteDataViaQuery</p> </li> <li> <p>neptune-graph:DeleteDataViaQuery</p> </li> </ul>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            query_string: <p>The query string to be executed.</p>
            language: <p>The query language the query is written in. Currently only openCypher is supported.</p>
            parameters: <p>The data parameters the query can use in JSON format. For example: {"name": "john", "age": 20}. (optional) </p>
            plan_cache: <p>Query plan cache is a feature that saves the query plan and reuses it on successive executions of the same query. This reduces query latency, and works for both <code>READ</code> and <code>UPDATE</code> queries. The plan cache is an LRU cache with a 5 minute TTL and a capacity of 1000.</p>
            explain_mode: <p>The explain mode parameter returns a query explain instead of the actual query results. A query explain can be used to gather insights about the query execution such as planning decisions, time spent on each operator, solutions flowing etc.</p>
            query_timeout_milliseconds: <p>Specifies the query timeout duration, in milliseconds. (optional)</p>

        Raises:
            capo_neptune_graph.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.unprocessable_exception.UnprocessableException: <p>Request cannot be processed due to known reasons. Eg. partition full.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.execute_query_input.ExecuteQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.execute_query_output.ExecuteQueryOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.execute_query

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.execute_query.async_execute_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.execute_query_input.ExecuteQueryInput = {
            "graph_identifier": graph_identifier,
            "query_string": query_string,
            "language": language,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if plan_cache is not None:
            input_["plan_cache"] = plan_cache
        if explain_mode is not None:
            input_["explain_mode"] = explain_mode
        if query_timeout_milliseconds is not None:
            input_["query_timeout_milliseconds"] = query_timeout_milliseconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def get_graph_summary(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        mode: Optional[
            "capo_neptune_graph.types.graph_summary_mode.GraphSummaryMode"
        ] = None,
    ) -> "capo_neptune_graph.types.get_graph_summary_output.GetGraphSummaryOutput":
        """<p>Gets a graph summary for a property graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            mode: <p>The summary mode can take one of two values: <code>basic</code> (the default), and <code>detailed</code>.</p>

        Raises:
            capo_neptune_graph.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_graph_summary_input.GetGraphSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_graph_summary_output.GetGraphSummaryOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_graph_summary

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_graph_summary.async_get_graph_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_graph_summary_input.GetGraphSummaryInput = {
            "graph_identifier": graph_identifier
        }
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_query(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_query_output.GetQueryOutput":
        """<p>Retrieves the status of a specified query.</p> <note> <p> When invoking this operation in a Neptune Analytics cluster, the IAM user or role making the request must have the <code>neptune-graph:GetQueryStatus</code> IAM action attached. </p> </note>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            query_id: <p>The ID of the query in question.</p>

        Raises:
            capo_neptune_graph.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_query_input.GetQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_query_output.GetQueryOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_query

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_query.async_get_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_query_input.GetQueryInput = {
            "graph_identifier": graph_identifier,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_queries(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        max_results: int,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        state: Optional[
            "capo_neptune_graph.types.query_state_input.QueryStateInput"
        ] = None,
    ) -> "capo_neptune_graph.types.list_queries_output.ListQueriesOutput":
        """<p>Lists active openCypher queries.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            max_results: <p>The maximum number of results to be fetched by the API.</p>
            state: <p>Filtered list of queries based on state.</p>

        Raises:
            capo_neptune_graph.errors.access_denied_exception.AccessDeniedException: <p>Raised in case of an authentication or authorization failure.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_queries_input.ListQueriesInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_queries_output.ListQueriesOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_queries

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_queries.async_list_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_queries_input.ListQueriesInput = {
            "graph_identifier": graph_identifier,
            "max_results": max_results,
        }
        if state is not None:
            input_["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_neptune_graph.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists tags associated with a specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_neptune_graph.types.arn.Arn",
        tags: "capo_neptune_graph.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.tag_resource_output.TagResourceOutput":
        r"""<p>Adds tags to the specified resource.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags need to be added.</p>
            tags: <p>The tags to be assigned to the Neptune Analytics resource.</p> <p>The tags are metadata that are specified as a list of key-value pairs:</p> <p> <b>Key</b> (string) – A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length. It can't be prefixed with <code>aws:</code> and can only contain the set of Unicode characters specified by this Java regular expression: <code>"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")</code>.</p> <p> <b>Value</b> (string) – A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length. It can't be prefixed with <code>aws:</code> and can only contain the set of Unicode characters specified by this Java regular expression: <code>"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")</code>.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.tag_resource

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_neptune_graph.types.arn.Arn",
        tag_keys: "capo_neptune_graph.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>ARN of the resource whose tag needs to be removed.</p>
            tag_keys: <p>Tag keys for the tags to be removed.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.untag_resource

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.untag_resource_input.UntagResourceInput = {
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

    async def create_graph(
        self,
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        provisioned_memory: "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
        public_connectivity: Optional[bool] = None,
        kms_key_identifier: Optional[
            "capo_neptune_graph.types.kms_key_arn.KmsKeyArn"
        ] = None,
        vector_search_configuration: Optional[
            "capo_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
        ] = None,
        replica_count: Optional[
            "capo_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.create_graph_output.CreateGraphOutput":
        """<p>Creates a new Neptune Analytics graph.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data in the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default = 1.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.create_graph_input.CreateGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.create_graph_output.CreateGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.create_graph.async_create_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.create_graph_input.CreateGraphInput = {
            "graph_name": graph_name,
            "provisioned_memory": provisioned_memory,
        }
        if tags is not None:
            input_["tags"] = tags
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if vector_search_configuration is not None:
            input_["vector_search_configuration"] = vector_search_configuration
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.delete_graph_output.DeleteGraphOutput":
        """<p>Deletes the specified graph. Graphs cannot be deleted if delete-protection is enabled.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph is deleted. If <code>true</code> is specified, no graph snapshot is created. If <code>false</code> is specified, a graph snapshot is created before the graph is deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.delete_graph_input.DeleteGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.delete_graph_output.DeleteGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.delete_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.delete_graph.async_delete_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.delete_graph_input.DeleteGraphInput = {
            "graph_identifier": graph_identifier,
            "skip_snapshot": skip_snapshot,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_graph_output.GetGraphOutput":
        """<p>Gets information about a specified graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_graph_input.GetGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_graph_output.GetGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_graph.async_get_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_graph_input.GetGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_graphs(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "capo_neptune_graph.types.list_graphs_output.ListGraphsOutput":
        """<p>Lists available Neptune Analytics graphs.</p>

        Args:
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_graphs_input.ListGraphsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_graphs_output.ListGraphsOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_graphs

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_graphs.async_list_graphs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_graphs_input.ListGraphsInput = {}
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

    async def iter_list_graphs(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_neptune_graph.types.graph_summary.GraphSummary]":
        _token = next_token
        while True:
            _response = await self.list_graphs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("graphs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reset_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.reset_graph_output.ResetGraphOutput":
        """<p>Empties the data from a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>ID of the graph to reset.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph data is deleted. If set to <code>true</code>, no graph snapshot is created. If set to <code>false</code>, a graph snapshot is created before the data is deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.reset_graph_input.ResetGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.reset_graph_output.ResetGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.reset_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.reset_graph.async_reset_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.reset_graph_input.ResetGraphInput = {
            "graph_identifier": graph_identifier,
            "skip_snapshot": skip_snapshot,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_graph_from_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
        replica_count: Optional[
            "capo_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        public_connectivity: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput":
        """<p>Restores a graph from a snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot in question.</p>
            graph_name: <p>A name for the new Neptune Analytics graph to be created from the snapshot.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>
            tags: <p>Adds metadata tags to the snapshot. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default =1</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot.async_restore_graph_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput = {
            "snapshot_identifier": snapshot_identifier,
            "graph_name": graph_name,
        }
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.start_graph_output.StartGraphOutput":
        """<p>Starts the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.start_graph_input.StartGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.start_graph_output.StartGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.start_graph.async_start_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.start_graph_input.StartGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.stop_graph_output.StopGraphOutput":
        """<p>Stops the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.stop_graph_input.StopGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.stop_graph_output.StopGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.stop_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.stop_graph.async_stop_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.stop_graph_input.StopGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        public_connectivity: Optional[bool] = None,
        provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.update_graph_output.UpdateGraphOutput":
        """<p>Updates the configuration of a specified Neptune Analytics graph</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.update_graph_input.UpdateGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.update_graph_output.UpdateGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.update_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.update_graph.async_update_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.update_graph_input.UpdateGraphInput = {
            "graph_identifier": graph_identifier
        }
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_private_graph_endpoint(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        vpc_id: Optional["capo_neptune_graph.types.vpc_id.VpcId"] = None,
        subnet_ids: Optional["capo_neptune_graph.types.subnet_ids.SubnetIds"] = None,
        vpc_security_group_ids: Optional[
            "capo_neptune_graph.types.security_group_ids.SecurityGroupIds"
        ] = None,
    ) -> "capo_neptune_graph.types.create_private_graph_endpoint_output.CreatePrivateGraphEndpointOutput":
        """<p>Create a private graph endpoint to allow private access to the graph from within a VPC. You can attach security groups to the private graph endpoint.</p> <note> <p>VPC endpoint charges apply.</p> </note>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p> The VPC in which the private graph endpoint needs to be created.</p>
            subnet_ids: <p>Subnets in which private graph endpoint ENIs are created.</p>
            vpc_security_group_ids: <p>Security groups to be attached to the private graph endpoint.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.create_private_graph_endpoint_input.CreatePrivateGraphEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.create_private_graph_endpoint_output.CreatePrivateGraphEndpointOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_private_graph_endpoint

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.create_private_graph_endpoint.async_create_private_graph_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.create_private_graph_endpoint_input.CreatePrivateGraphEndpointInput = {
            "graph_identifier": graph_identifier
        }
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_private_graph_endpoint(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        vpc_id: "capo_neptune_graph.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.delete_private_graph_endpoint_output.DeletePrivateGraphEndpointOutput":
        """<p>Deletes a private graph endpoint.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p>The ID of the VPC where the private endpoint is located.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.delete_private_graph_endpoint_input.DeletePrivateGraphEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.delete_private_graph_endpoint_output.DeletePrivateGraphEndpointOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.delete_private_graph_endpoint

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.delete_private_graph_endpoint.async_delete_private_graph_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.delete_private_graph_endpoint_input.DeletePrivateGraphEndpointInput = {
            "graph_identifier": graph_identifier,
            "vpc_id": vpc_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_private_graph_endpoint(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        vpc_id: "capo_neptune_graph.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_private_graph_endpoint_output.GetPrivateGraphEndpointOutput":
        """<p>Retrieves information about a specified private endpoint.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p>The ID of the VPC where the private endpoint is located.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_private_graph_endpoint_input.GetPrivateGraphEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_private_graph_endpoint_output.GetPrivateGraphEndpointOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_private_graph_endpoint

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_private_graph_endpoint.async_get_private_graph_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_private_graph_endpoint_input.GetPrivateGraphEndpointInput = {
            "graph_identifier": graph_identifier,
            "vpc_id": vpc_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_private_graph_endpoints(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "capo_neptune_graph.types.list_private_graph_endpoints_output.ListPrivateGraphEndpointsOutput":
        """<p>Lists private endpoints for a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_private_graph_endpoints_input.ListPrivateGraphEndpointsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_private_graph_endpoints_output.ListPrivateGraphEndpointsOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_private_graph_endpoints

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_private_graph_endpoints.async_list_private_graph_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_private_graph_endpoints_input.ListPrivateGraphEndpointsInput = {
            "graph_identifier": graph_identifier
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

    async def iter_list_private_graph_endpoints(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_neptune_graph.types.private_graph_endpoint_summary.PrivateGraphEndpointSummary]":
        _token = next_token
        while True:
            _response = await self.list_private_graph_endpoints(
                graph_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("private_graph_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_graph_snapshot(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        snapshot_name: "capo_neptune_graph.types.snapshot_name.SnapshotName",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
    ) -> "capo_neptune_graph.types.create_graph_snapshot_output.CreateGraphSnapshotOutput":
        """<p>Creates a snapshot of the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            snapshot_name: <p>The snapshot name. For example: <code>my-snapshot-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.create_graph_snapshot_input.CreateGraphSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.create_graph_snapshot_output.CreateGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.create_graph_snapshot.async_create_graph_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.create_graph_snapshot_input.CreateGraphSnapshotInput = {
            "graph_identifier": graph_identifier,
            "snapshot_name": snapshot_name,
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

    async def delete_graph_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.delete_graph_snapshot_output.DeleteGraphSnapshotOutput":
        """<p>Deletes the specified graph snapshot.</p>

        Args:
            snapshot_identifier: <p>ID of the graph snapshot to be deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.delete_graph_snapshot_input.DeleteGraphSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.delete_graph_snapshot_output.DeleteGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.delete_graph_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.delete_graph_snapshot.async_delete_graph_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.delete_graph_snapshot_input.DeleteGraphSnapshotInput = {
            "snapshot_identifier": snapshot_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_graph_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_graph_snapshot_output.GetGraphSnapshotOutput":
        """<p>Retrieves a specified graph snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot to retrieve.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_graph_snapshot_input.GetGraphSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_graph_snapshot_output.GetGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_graph_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_graph_snapshot.async_get_graph_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_graph_snapshot_input.GetGraphSnapshotInput = {
            "snapshot_identifier": snapshot_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_graph_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_neptune_graph.types.list_graph_snapshots_output.ListGraphSnapshotsOutput"
    ):
        """<p>Lists available snapshots of a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_graph_snapshots_input.ListGraphSnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_graph_snapshots_output.ListGraphSnapshotsOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_graph_snapshots

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_graph_snapshots.async_list_graph_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_graph_snapshots_input.ListGraphSnapshotsInput = {}
        if graph_identifier is not None:
            input_["graph_identifier"] = graph_identifier
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

    async def iter_list_graph_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_neptune_graph.types.graph_snapshot_summary.GraphSnapshotSummary]":
        _token = next_token
        while True:
            _response = await self.list_graph_snapshots(
                config_overrides=config_overrides,
                graph_identifier=graph_identifier,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("graph_snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_export_task(
        self,
        task_identifier: "capo_neptune_graph.types.export_task_id.ExportTaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.cancel_export_task_output.CancelExportTaskOutput":
        """<p>Cancel the specified export task.</p>

        Args:
            task_identifier: <p>The unique identifier of the export task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.cancel_export_task_input.CancelExportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.cancel_export_task_output.CancelExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.cancel_export_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.cancel_export_task.async_cancel_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.cancel_export_task_input.CancelExportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_import_task(
        self,
        task_identifier: "capo_neptune_graph.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.cancel_import_task_output.CancelImportTaskOutput":
        """<p>Deletes the specified import task.</p>

        Args:
            task_identifier: <p>The unique identifier of the import task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.cancel_import_task_input.CancelImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.cancel_import_task_output.CancelImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.cancel_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.cancel_import_task.async_cancel_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.cancel_import_task_input.CancelImportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_graph_using_import_task(
        self,
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        source: str,
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
        public_connectivity: Optional[bool] = None,
        kms_key_identifier: Optional[
            "capo_neptune_graph.types.kms_key_arn.KmsKeyArn"
        ] = None,
        vector_search_configuration: Optional[
            "capo_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
        ] = None,
        replica_count: Optional[
            "capo_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        deletion_protection: Optional[bool] = None,
        import_options: Optional[
            "capo_neptune_graph.types.import_options.ImportOptions"
        ] = None,
        max_provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        min_provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        fail_on_error: Optional[bool] = None,
        format: Optional["capo_neptune_graph.types.format.Format"] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        blank_node_handling: Optional[
            "capo_neptune_graph.types.blank_node_handling.BlankNodeHandling"
        ] = None,
    ) -> "capo_neptune_graph.types.create_graph_using_import_task_output.CreateGraphUsingImportTaskOutput":
        """<p>Creates a new Neptune Analytics graph and imports data into it, either from Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune database snapshot.</p> <p>The data can be loaded from files in S3 that in either the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a> or the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data imported into the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535 </p>
            replica_count: <p>The number of replicas in other AZs to provision on the new graph after import. Default = 1, Min = 0, Max = 2.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            import_options: <p>Contains options for controlling the import process. For example, if the <code>failOnError</code> key is set to <code>false</code>, the import skips problem data and attempts to continue (whereas if set to <code>true</code>, the default, or if omitted, the import operation halts immediately when an error is encountered.</p>
            max_provisioned_memory: <p>The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 1024, or the approved upper limit for your account.</p> <p> If both the minimum and maximum values are specified, the final <code>provisioned-memory</code> will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.</p>
            min_provisioned_memory: <p>The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 16</p>
            fail_on_error: <p>If set to <code>true</code>, the task halts when an import error is encountered. If set to <code>false</code>, the task skips the data that caused the error and continues if possible.</p>
            source: <p>A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>
            format: <p>Specifies the format of S3 data to be imported. Valid values are <code>CSV</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a>, <code>OPEN_CYPHER</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>, or <code>ntriples</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html">RDF n-triples</a> format.</p>
            parquet_type: <p>The parquet type of the import task.</p>
            blank_node_handling: <p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling">Handling RDF values</a>.</p>
            role_arn: <p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.create_graph_using_import_task_input.CreateGraphUsingImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.create_graph_using_import_task_output.CreateGraphUsingImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph_using_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.create_graph_using_import_task.async_create_graph_using_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.create_graph_using_import_task_input.CreateGraphUsingImportTaskInput = {
            "graph_name": graph_name,
            "source": source,
            "role_arn": role_arn,
        }
        if tags is not None:
            input_["tags"] = tags
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if vector_search_configuration is not None:
            input_["vector_search_configuration"] = vector_search_configuration
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if import_options is not None:
            input_["import_options"] = import_options
        if max_provisioned_memory is not None:
            input_["max_provisioned_memory"] = max_provisioned_memory
        if min_provisioned_memory is not None:
            input_["min_provisioned_memory"] = min_provisioned_memory
        if fail_on_error is not None:
            input_["fail_on_error"] = fail_on_error
        if format is not None:
            input_["format"] = format
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if blank_node_handling is not None:
            input_["blank_node_handling"] = blank_node_handling

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_export_task(
        self,
        task_identifier: "capo_neptune_graph.types.export_task_id.ExportTaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_export_task_output.GetExportTaskOutput":
        """<p>Retrieves a specified export task.</p>

        Args:
            task_identifier: <p>The unique identifier of the export task.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_export_task_input.GetExportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_export_task_output.GetExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_export_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_export_task.async_get_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_export_task_input.GetExportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import_task(
        self,
        task_identifier: "capo_neptune_graph.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_import_task_output.GetImportTaskOutput":
        """<p>Retrieves a specified import task.</p>

        Args:
            task_identifier: <p>The unique identifier of the import task.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_import_task_input.GetImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_import_task_output.GetImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_import_task.async_get_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_import_task_input.GetImportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_export_tasks(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "capo_neptune_graph.types.list_export_tasks_output.ListExportTasksOutput":
        """<p>Retrieves a list of export tasks.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate input.</p>
            max_results: <p>The maximum number of export tasks to return.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_export_tasks_input.ListExportTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_export_tasks_output.ListExportTasksOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_export_tasks

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_export_tasks.async_list_export_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_export_tasks_input.ListExportTasksInput = {}
        if graph_identifier is not None:
            input_["graph_identifier"] = graph_identifier
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

    async def iter_list_export_tasks(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_neptune_graph.types.export_task_summary.ExportTaskSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_export_tasks(
                config_overrides=config_overrides,
                graph_identifier=graph_identifier,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_import_tasks(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "capo_neptune_graph.types.list_import_tasks_output.ListImportTasksOutput":
        """<p>Lists import tasks.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph. When provided, the service returns only import tasks associated with this graph. If not specified, the service returns all import tasks.</p>
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_import_tasks_input.ListImportTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_import_tasks_output.ListImportTasksOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_import_tasks

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_import_tasks.async_list_import_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_import_tasks_input.ListImportTasksInput = {}
        if graph_identifier is not None:
            input_["graph_identifier"] = graph_identifier
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

    async def iter_list_import_tasks(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_neptune_graph.types.import_task_summary.ImportTaskSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_import_tasks(
                config_overrides=config_overrides,
                graph_identifier=graph_identifier,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_export_task(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
        format: "capo_neptune_graph.types.export_format.ExportFormat",
        destination: str,
        kms_key_identifier: "capo_neptune_graph.types.kms_key_arn.KmsKeyArn",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        export_filter: Optional[
            "capo_neptune_graph.types.export_filter.ExportFilter"
        ] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
    ) -> "capo_neptune_graph.types.start_export_task_output.StartExportTaskOutput":
        """<p>Export data from an existing Neptune Analytics graph to Amazon S3. The graph state should be <code>AVAILABLE</code>.</p>

        Args:
            graph_identifier: <p>The source graph identifier of the export task.</p>
            role_arn: <p>The ARN of the IAM role that will allow data to be exported to the destination.</p>
            format: <p>The format of the export task.</p>
            destination: <p>The Amazon S3 URI where data will be exported to.</p>
            kms_key_identifier: <p>The KMS key identifier of the export task.</p>
            parquet_type: <p>The parquet type of the export task.</p>
            export_filter: <p>The export filter of the export task.</p>
            tags: <p>Tags to be applied to the export task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.start_export_task_input.StartExportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.start_export_task_output.StartExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_export_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.start_export_task.async_start_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.start_export_task_input.StartExportTaskInput = {
            "graph_identifier": graph_identifier,
            "role_arn": role_arn,
            "format": format,
            "destination": destination,
            "kms_key_identifier": kms_key_identifier,
        }
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if export_filter is not None:
            input_["export_filter"] = export_filter
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import_task(
        self,
        source: str,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        import_options: Optional[
            "capo_neptune_graph.types.import_options.ImportOptions"
        ] = None,
        fail_on_error: Optional[bool] = None,
        format: Optional["capo_neptune_graph.types.format.Format"] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        blank_node_handling: Optional[
            "capo_neptune_graph.types.blank_node_handling.BlankNodeHandling"
        ] = None,
    ) -> "capo_neptune_graph.types.start_import_task_output.StartImportTaskOutput":
        """<p>Import data into existing Neptune Analytics graph from Amazon Simple Storage Service (S3). The graph needs to be empty and in the AVAILABLE state.</p>

        Args:
            fail_on_error: <p>If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.</p>
            source: <p>A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>
            format: <p>Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identifies the openCypher load format.</p>
            parquet_type: <p>The parquet type of the import task.</p>
            blank_node_handling: <p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling">Handling RDF values</a>.</p>
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            role_arn: <p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.start_import_task_input.StartImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.start_import_task_output.StartImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.start_import_task.async_start_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune_graph.types.start_import_task_input.StartImportTaskInput = {
            "source": source,
            "graph_identifier": graph_identifier,
            "role_arn": role_arn,
        }
        if import_options is not None:
            input_["import_options"] = import_options
        if fail_on_error is not None:
            input_["fail_on_error"] = fail_on_error
        if format is not None:
            input_["format"] = format
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if blank_node_handling is not None:
            input_["blank_node_handling"] = blank_node_handling

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

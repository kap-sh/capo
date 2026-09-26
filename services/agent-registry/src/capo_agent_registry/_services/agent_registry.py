"""Generated from Smithy shape ``com.amazonaws.agentregistry#AgentRegistry``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_agent_registry._auth._signers
import capo_agent_registry._auth._sigv4
from capo_agent_registry._auth._identity import Credentials
from capo_agent_registry._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_agent_registry._auth._zapros_handler import AuthMiddleware
from capo_agent_registry._pagination import resolve_path as _resolve_path
from capo_agent_registry._services._aws_config import aws_config
from capo_agent_registry._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_agent_registry.types.batch_get_discoverable_registry_record_request
    import capo_agent_registry.types.batch_get_discoverable_registry_record_response
    import capo_agent_registry.types.discoverable_registry_record_summary
    import capo_agent_registry.types.list_discoverable_registry_records_request
    import capo_agent_registry.types.list_discoverable_registry_records_response
    import capo_agent_registry.types.metadata_filter_expression
    import capo_agent_registry.types.registry_id_list
    import capo_agent_registry.types.registry_identifier
    import capo_agent_registry.types.registry_record_filter_list
    import capo_agent_registry.types.registry_records_entry_list
    import capo_agent_registry.types.search_discoverable_registry_records_request
    import capo_agent_registry.types.search_discoverable_registry_records_response
    import capo_agent_registry.types.search_query


class AgentRegistryClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AgentRegistryClient:
    """A client for the ``AgentRegistry`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AgentRegistryClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AgentRegistryClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AgentRegistryClientConfig = config_overrides or {}
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
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_get_discoverable_registry_record(
        self,
        entries: "capo_agent_registry.types.registry_records_entry_list.RegistryRecordsEntryList",
        *,
        config_overrides: Optional[AgentRegistryClientConfig] = None,
    ) -> "capo_agent_registry.types.batch_get_discoverable_registry_record_response.BatchGetDiscoverableRegistryRecordResponse":
        """<p> Retrieves multiple discoverable registry records by ID from a single registry. Records that cannot be retrieved are reported individually in the <code>errors</code> list rather than failing the entire request.</p>

        Args:
            entries: <p> The registry-scoped groups of record IDs to retrieve. Currently, you can specify exactly one entry.</p>

        Raises:
            capo_agent_registry.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry.errors.unauthorized_exception.UnauthorizedException: <p>The request could not be authenticated.</p>
            capo_agent_registry.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry.types.batch_get_discoverable_registry_record_request.BatchGetDiscoverableRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_agent_registry.types.batch_get_discoverable_registry_record_response.BatchGetDiscoverableRegistryRecordResponse"
        ]:
            import capo_agent_registry._operations.agent_registry.batch_get_discoverable_registry_record

            output, http_response = (
                capo_agent_registry._operations.agent_registry.batch_get_discoverable_registry_record.batch_get_discoverable_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry.types.batch_get_discoverable_registry_record_request.BatchGetDiscoverableRegistryRecordRequest = {
            "entries": entries
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_discoverable_registry_records(
        self,
        registry_id: "capo_agent_registry.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_agent_registry.types.registry_record_filter_list.RegistryRecordFilterList"
        ] = None,
    ) -> "capo_agent_registry.types.list_discoverable_registry_records_response.ListDiscoverableRegistryRecordsResponse":
        """<p> Lists the discoverable registry records in a registry. You can optionally filter and paginate the results.</p>

        Args:
            registry_id: <p> The identifier of the registry whose discoverable records are listed. You can provide either the full Amazon Resource Name (ARN) or the registry ID.</p>
            max_results: <p> The maximum number of records to return in a single page. Valid values are 1 through 100.</p>
            next_token: <p> The pagination token returned by a previous request. Use this value to retrieve the next page of results.</p>
            filters: <p> The filters to apply to the discoverable registry record list.</p>

        Raises:
            capo_agent_registry.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry.errors.unauthorized_exception.UnauthorizedException: <p>The request could not be authenticated.</p>
            capo_agent_registry.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry.types.list_discoverable_registry_records_request.ListDiscoverableRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_agent_registry.types.list_discoverable_registry_records_response.ListDiscoverableRegistryRecordsResponse"
        ]:
            import capo_agent_registry._operations.agent_registry.list_discoverable_registry_records

            output, http_response = (
                capo_agent_registry._operations.agent_registry.list_discoverable_registry_records.list_discoverable_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry.types.list_discoverable_registry_records_request.ListDiscoverableRegistryRecordsRequest = {
            "registry_id": registry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_discoverable_registry_records(
        self,
        registry_id: "capo_agent_registry.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_agent_registry.types.registry_record_filter_list.RegistryRecordFilterList"
        ] = None,
    ) -> "Iterator[capo_agent_registry.types.discoverable_registry_record_summary.DiscoverableRegistryRecordSummary]":
        _token = next_token
        while True:
            _response = self.list_discoverable_registry_records(
                registry_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("registry_records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_discoverable_registry_records(
        self,
        search_query: "capo_agent_registry.types.search_query.SearchQuery",
        registry_ids: "capo_agent_registry.types.registry_id_list.RegistryIdList",
        *,
        config_overrides: Optional[AgentRegistryClientConfig] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_agent_registry.types.metadata_filter_expression.MetadataFilterExpression"
        ] = None,
    ) -> "capo_agent_registry.types.search_discoverable_registry_records_response.SearchDiscoverableRegistryRecordsResponse":
        """<p> Searches the discoverable registry records in a registry using a natural language query. Returns metadata for the matching records ordered by relevance.</p>

        Args:
            search_query: <p> The natural language query to search for matching registry records.</p>
            registry_ids: <p> The registry identifiers to search within. Currently, you must specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the registry ID.</p>
            max_results: <p> The maximum number of results to return. Valid values are 1 through 20. The default value is 10.</p>
            filters: <p> An optional structured JSON metadata filter that narrows the search results. Supports the field-level operators <code>$eq</code>, <code>$ne</code>, and <code>$in</code>, and the logical operators <code>$and</code> and <code>$or</code> on filterable fields.</p>

        Raises:
            capo_agent_registry.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry.errors.unauthorized_exception.UnauthorizedException: <p>The request could not be authenticated.</p>
            capo_agent_registry.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry.types.search_discoverable_registry_records_request.SearchDiscoverableRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_agent_registry.types.search_discoverable_registry_records_response.SearchDiscoverableRegistryRecordsResponse"
        ]:
            import capo_agent_registry._operations.agent_registry.search_discoverable_registry_records

            output, http_response = (
                capo_agent_registry._operations.agent_registry.search_discoverable_registry_records.search_discoverable_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_agent_registry.types.search_discoverable_registry_records_request.SearchDiscoverableRegistryRecordsRequest = {
            "search_query": search_query,
            "registry_ids": registry_ids,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

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

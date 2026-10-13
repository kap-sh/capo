from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_controlcatalog._auth._signers
import capo_controlcatalog._auth._sigv4
from capo_controlcatalog._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_controlcatalog.types.list_objectives_request
    import capo_controlcatalog.types.list_objectives_response
    import capo_controlcatalog.types.max_list_objectives_results
    import capo_controlcatalog.types.objective_filter
    import capo_controlcatalog.types.objective_summary
    import capo_controlcatalog.types.pagination_token
    from capo_controlcatalog._services.async_control_catalog import (
        AsyncControlCatalogClient,
        AsyncControlCatalogClientConfig,
    )
    from capo_controlcatalog._services.control_catalog import (
        ControlCatalogClient,
        ControlCatalogClientConfig,
    )


class ObjectiveResource:
    def __init__(self, service: ControlCatalogClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_objectives_results.MaxListObjectivesResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        objective_filter: Optional[
            "capo_controlcatalog.types.objective_filter.ObjectiveFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_objectives_response.ListObjectivesResponse":
        """<p>Returns a paginated list of objectives from the Control Catalog.</p> <p>You can apply an optional filter to see the objectives that belong to a specific domain. If you don’t provide a filter, the operation returns all objectives. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            objective_filter: <p>An optional filter that narrows the results to a specific domain.</p> <p>This filter allows you to specify one domain ARN at a time. Passing multiple ARNs in the <code>ObjectiveFilter</code> isn’t supported.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.list_objectives_request.ListObjectivesRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.list_objectives_response.ListObjectivesResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_objectives

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.list_objectives.list_objectives(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListObjectives")
        )
        input_: capo_controlcatalog.types.list_objectives_request.ListObjectivesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if objective_filter is not None:
            input_["objective_filter"] = objective_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncObjectiveResource:
    def __init__(self, service: AsyncControlCatalogClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_objectives_results.MaxListObjectivesResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        objective_filter: Optional[
            "capo_controlcatalog.types.objective_filter.ObjectiveFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_objectives_response.ListObjectivesResponse":
        """<p>Returns a paginated list of objectives from the Control Catalog.</p> <p>You can apply an optional filter to see the objectives that belong to a specific domain. If you don’t provide a filter, the operation returns all objectives. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            objective_filter: <p>An optional filter that narrows the results to a specific domain.</p> <p>This filter allows you to specify one domain ARN at a time. Passing multiple ARNs in the <code>ObjectiveFilter</code> isn’t supported.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controlcatalog.types.list_objectives_request.ListObjectivesRequest]",
        ) -> AsyncOperationResponse[
            "capo_controlcatalog.types.list_objectives_response.ListObjectivesResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_objectives

            (
                output,
                http_response,
            ) = await capo_controlcatalog._operations.control_catalog.list_objectives.async_list_objectives(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListObjectives")
        )
        input_: capo_controlcatalog.types.list_objectives_request.ListObjectivesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if objective_filter is not None:
            input_["objective_filter"] = objective_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

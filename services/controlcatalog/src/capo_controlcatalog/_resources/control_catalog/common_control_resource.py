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
    import capo_controlcatalog.types.common_control_filter
    import capo_controlcatalog.types.common_control_summary
    import capo_controlcatalog.types.list_common_controls_request
    import capo_controlcatalog.types.list_common_controls_response
    import capo_controlcatalog.types.max_list_common_controls_results
    import capo_controlcatalog.types.pagination_token
    from capo_controlcatalog._services.async_control_catalog import (
        AsyncControlCatalogClient,
        AsyncControlCatalogClientConfig,
    )
    from capo_controlcatalog._services.control_catalog import (
        ControlCatalogClient,
        ControlCatalogClientConfig,
    )


class CommonControlResource:
    def __init__(self, service: ControlCatalogClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_common_controls_results.MaxListCommonControlsResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        common_control_filter: Optional[
            "capo_controlcatalog.types.common_control_filter.CommonControlFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse":
        """<p>Returns a paginated list of common controls from the Amazon Web Services Control Catalog.</p> <p>You can apply an optional filter to see common controls that have a specific objective. If you don’t provide a filter, the operation returns all common controls. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            common_control_filter: <p>An optional filter that narrows the results to a specific objective.</p> <p>This filter allows you to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_common_controls

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.list_common_controls.list_common_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCommonControls")
        )
        input_: capo_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if common_control_filter is not None:
            input_["common_control_filter"] = common_control_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCommonControlResource:
    def __init__(self, service: AsyncControlCatalogClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_common_controls_results.MaxListCommonControlsResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        common_control_filter: Optional[
            "capo_controlcatalog.types.common_control_filter.CommonControlFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse":
        """<p>Returns a paginated list of common controls from the Amazon Web Services Control Catalog.</p> <p>You can apply an optional filter to see common controls that have a specific objective. If you don’t provide a filter, the operation returns all common controls. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            common_control_filter: <p>An optional filter that narrows the results to a specific objective.</p> <p>This filter allows you to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest]",
        ) -> AsyncOperationResponse[
            "capo_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_common_controls

            (
                output,
                http_response,
            ) = await capo_controlcatalog._operations.control_catalog.list_common_controls.async_list_common_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCommonControls")
        )
        input_: capo_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if common_control_filter is not None:
            input_["common_control_filter"] = common_control_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

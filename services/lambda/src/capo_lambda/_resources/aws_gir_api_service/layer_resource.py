from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.architecture
    import capo_lambda.types.list_layers_request
    import capo_lambda.types.list_layers_response
    import capo_lambda.types.max_layer_list_items
    import capo_lambda.types.runtime
    import capo_lambda.types.string
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class LayerResource:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        compatible_architecture: Optional[
            "capo_lambda.types.architecture.Architecture"
        ] = None,
        compatible_runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
    ) -> "capo_lambda.types.list_layers_response.ListLayersResponse":
        """<p>Lists <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html">Lambda layers</a> and shows information about the latest version of each. Specify a <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">runtime identifier</a> to list only layers that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layers that are compatible with that <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architecture</a>.</p>

        Args:
            compatible_architecture: <p>The compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architecture</a>.</p>
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported">Supported runtimes</a>.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of layers to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the layers that are compatible with your function's runtime
            The following example returns information about layers that are compatible with the Python 3.7 runtime.

            >>> client.list(compatible_runtime='python3.7')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_layers_request.ListLayersRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_layers_response.ListLayersResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_layers

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_layers.list_layers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_layers_request.ListLayersRequest = {}
        if compatible_architecture is not None:
            input_["compatible_architecture"] = compatible_architecture
        if compatible_runtime is not None:
            input_["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLayerResource:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        compatible_architecture: Optional[
            "capo_lambda.types.architecture.Architecture"
        ] = None,
        compatible_runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_layer_list_items.MaxLayerListItems"
        ] = None,
    ) -> "capo_lambda.types.list_layers_response.ListLayersResponse":
        """<p>Lists <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html">Lambda layers</a> and shows information about the latest version of each. Specify a <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">runtime identifier</a> to list only layers that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layers that are compatible with that <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architecture</a>.</p>

        Args:
            compatible_architecture: <p>The compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architecture</a>.</p>
            compatible_runtime: <p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported">Supported runtimes</a>.</p>
            marker: <p>A pagination token returned by a previous call.</p>
            max_items: <p>The maximum number of layers to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the layers that are compatible with your function's runtime
            The following example returns information about layers that are compatible with the Python 3.7 runtime.

            >>> await client.list(compatible_runtime='python3.7')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_layers_request.ListLayersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_layers_response.ListLayersResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_layers

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_layers.async_list_layers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_layers_request.ListLayersRequest = {}
        if compatible_architecture is not None:
            input_["compatible_architecture"] = compatible_architecture
        if compatible_runtime is not None:
            input_["compatible_runtime"] = compatible_runtime
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_nova_act._auth._signers
import capo_nova_act._auth._sigv4
from capo_nova_act._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_nova_act.types.list_models_request
    import capo_nova_act.types.list_models_response
    from capo_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from capo_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class ModelResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def list(
        self,
        client_compatibility_version: int,
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.list_models_response.ListModelsResponse":
        """<p>Lists all available AI models that can be used for workflow execution, including their status and compatibility information.</p>

        Args:
            client_compatibility_version: <p>The client compatibility version to filter models by compatibility.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_models_request.ListModelsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_models_response.ListModelsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_models

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_models.list_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListModels")
        )
        input_: capo_nova_act.types.list_models_request.ListModelsRequest = {
            "client_compatibility_version": client_compatibility_version
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncModelResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def list(
        self,
        client_compatibility_version: int,
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "capo_nova_act.types.list_models_response.ListModelsResponse":
        """<p>Lists all available AI models that can be used for workflow execution, including their status and compatibility information.</p>

        Args:
            client_compatibility_version: <p>The client compatibility version to filter models by compatibility.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.list_models_request.ListModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.list_models_response.ListModelsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_models

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.list_models.async_list_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListModels")
        )
        input_: capo_nova_act.types.list_models_request.ListModelsRequest = {
            "client_compatibility_version": client_compatibility_version
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_migrationhuborchestrator._auth._signers
import capo_migrationhuborchestrator._auth._sigv4
from capo_migrationhuborchestrator._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.list_plugins_request
    import capo_migrationhuborchestrator.types.list_plugins_response
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.plugin_summary
    from capo_migrationhuborchestrator._services.async_migration_hub_orchestrator import (
        AsyncMigrationHubOrchestratorClient,
        AsyncMigrationHubOrchestratorClientConfig,
    )
    from capo_migrationhuborchestrator._services.migration_hub_orchestrator import (
        MigrationHubOrchestratorClient,
        MigrationHubOrchestratorClientConfig,
    )


class Plugin:
    def __init__(self, service: MigrationHubOrchestratorClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
    ):
        """<p>List AWS Migration Hub Orchestrator plugins.</p>

        Args:
            max_results: <p>The maximum number of plugins that can be returned.</p>
            next_token: <p>The pagination token.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest]",
        ) -> OperationResponse[
            "capo_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins

            output, http_response = (
                capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins.list_plugins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPlugins")
        )
        input_: capo_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest = {}
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


class AsyncPlugin:
    def __init__(self, service: AsyncMigrationHubOrchestratorClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
        max_results: Optional[
            "capo_migrationhuborchestrator.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_migrationhuborchestrator.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
    ):
        """<p>List AWS Migration Hub Orchestrator plugins.</p>

        Args:
            max_results: <p>The maximum number of plugins that can be returned.</p>
            next_token: <p>The pagination token.</p>

        Raises:
            capo_migrationhuborchestrator.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_migrationhuborchestrator.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_plugins_response.ListPluginsResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_plugins.async_list_plugins(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPlugins")
        )
        input_: capo_migrationhuborchestrator.types.list_plugins_request.ListPluginsRequest = {}
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

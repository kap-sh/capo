from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_amplifyuibuilder._auth._signers
import capo_amplifyuibuilder._auth._sigv4
from capo_amplifyuibuilder._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.create_theme_data
    import capo_amplifyuibuilder.types.create_theme_request
    import capo_amplifyuibuilder.types.create_theme_response
    import capo_amplifyuibuilder.types.delete_theme_request
    import capo_amplifyuibuilder.types.export_themes_request
    import capo_amplifyuibuilder.types.export_themes_response
    import capo_amplifyuibuilder.types.get_theme_request
    import capo_amplifyuibuilder.types.get_theme_response
    import capo_amplifyuibuilder.types.list_entity_limit
    import capo_amplifyuibuilder.types.list_themes_request
    import capo_amplifyuibuilder.types.list_themes_response
    import capo_amplifyuibuilder.types.theme
    import capo_amplifyuibuilder.types.theme_summary
    import capo_amplifyuibuilder.types.update_theme_data
    import capo_amplifyuibuilder.types.update_theme_request
    import capo_amplifyuibuilder.types.update_theme_response
    import capo_amplifyuibuilder.types.uuid
    from capo_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from capo_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class ThemeResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: str,
        environment_name: str,
        theme_to_create: "capo_amplifyuibuilder.types.create_theme_data.CreateThemeData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.create_theme_response.CreateThemeResponse":
        """<p>Creates a theme to apply to the components in an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            theme_to_create: <p>Represents the configuration of the theme to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.create_theme_request.CreateThemeRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.create_theme_response.CreateThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_theme

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.create_theme.create_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateTheme")
        )
        input_: capo_amplifyuibuilder.types.create_theme_request.CreateThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "theme_to_create": theme_to_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_theme_response.GetThemeResponse":
        """<p>Returns an existing theme for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.get_theme_request.GetThemeRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.get_theme_response.GetThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_theme

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.get_theme.get_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTheme")
        )
        input_: capo_amplifyuibuilder.types.get_theme_request.GetThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        updated_theme: "capo_amplifyuibuilder.types.update_theme_data.UpdateThemeData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse":
        """<p>Updates an existing theme.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>
            client_token: <p>The unique client token.</p>
            updated_theme: <p>The configuration of the updated theme.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_theme

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.update_theme.update_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateTheme")
        )
        input_: capo_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_theme": updated_theme,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Deletes a theme from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the theme to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest]",
        ) -> OperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_theme

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.delete_theme.delete_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteTheme")
        )
        input_: capo_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "capo_amplifyuibuilder.types.list_themes_response.ListThemesResponse":
        """<p>Retrieves a list of themes for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of theme results to return in the response.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.list_themes_request.ListThemesRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.list_themes_response.ListThemesResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_themes

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.list_themes.list_themes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListThemes")
        )
        input_: capo_amplifyuibuilder.types.list_themes_request.ListThemesRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_themes_response.ExportThemesResponse":
        """<p>Exports theme configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export the themes to.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.export_themes_request.ExportThemesRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.export_themes_response.ExportThemesResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_themes

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.export_themes.export_themes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportThemes")
        )
        input_: capo_amplifyuibuilder.types.export_themes_request.ExportThemesRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncThemeResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: str,
        environment_name: str,
        theme_to_create: "capo_amplifyuibuilder.types.create_theme_data.CreateThemeData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.create_theme_response.CreateThemeResponse":
        """<p>Creates a theme to apply to the components in an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            theme_to_create: <p>Represents the configuration of the theme to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.create_theme_request.CreateThemeRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.create_theme_response.CreateThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.create_theme.async_create_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateTheme")
        )
        input_: capo_amplifyuibuilder.types.create_theme_request.CreateThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "theme_to_create": theme_to_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_theme_response.GetThemeResponse":
        """<p>Returns an existing theme for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_theme_request.GetThemeRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_theme_response.GetThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_theme.async_get_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTheme")
        )
        input_: capo_amplifyuibuilder.types.get_theme_request.GetThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        updated_theme: "capo_amplifyuibuilder.types.update_theme_data.UpdateThemeData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse":
        """<p>Updates an existing theme.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>
            client_token: <p>The unique client token.</p>
            updated_theme: <p>The configuration of the updated theme.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.update_theme.async_update_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateTheme")
        )
        input_: capo_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_theme": updated_theme,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Deletes a theme from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the theme to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.delete_theme.async_delete_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteTheme")
        )
        input_: capo_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "capo_amplifyuibuilder.types.list_themes_response.ListThemesResponse":
        """<p>Retrieves a list of themes for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of theme results to return in the response.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_themes_request.ListThemesRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_themes_response.ListThemesResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_themes

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_themes.async_list_themes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListThemes")
        )
        input_: capo_amplifyuibuilder.types.list_themes_request.ListThemesRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
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

    async def export_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_themes_response.ExportThemesResponse":
        """<p>Exports theme configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export the themes to.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.export_themes_request.ExportThemesRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.export_themes_response.ExportThemesResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_themes

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.export_themes.async_export_themes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportThemes")
        )
        input_: capo_amplifyuibuilder.types.export_themes_request.ExportThemesRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

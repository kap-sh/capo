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
    import capo_amplifyuibuilder.types.component
    import capo_amplifyuibuilder.types.component_summary
    import capo_amplifyuibuilder.types.create_component_data
    import capo_amplifyuibuilder.types.create_component_request
    import capo_amplifyuibuilder.types.create_component_response
    import capo_amplifyuibuilder.types.delete_component_request
    import capo_amplifyuibuilder.types.export_components_request
    import capo_amplifyuibuilder.types.export_components_response
    import capo_amplifyuibuilder.types.get_component_request
    import capo_amplifyuibuilder.types.get_component_response
    import capo_amplifyuibuilder.types.list_components_request
    import capo_amplifyuibuilder.types.list_components_response
    import capo_amplifyuibuilder.types.list_entity_limit
    import capo_amplifyuibuilder.types.update_component_data
    import capo_amplifyuibuilder.types.update_component_request
    import capo_amplifyuibuilder.types.update_component_response
    import capo_amplifyuibuilder.types.uuid
    from capo_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from capo_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class ComponentResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: str,
        environment_name: str,
        component_to_create: "capo_amplifyuibuilder.types.create_component_data.CreateComponentData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
    ):
        """<p>Creates a new component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the component.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            component_to_create: <p>Represents the configuration of the component to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.create_component_request.CreateComponentRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_component

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.create_component.create_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateComponent")
        )
        input_: capo_amplifyuibuilder.types.create_component_request.CreateComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "component_to_create": component_to_create,
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
    ) -> "capo_amplifyuibuilder.types.get_component_response.GetComponentResponse":
        """<p>Returns an existing component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the component.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.get_component_request.GetComponentRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.get_component_response.GetComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_component

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.get_component.get_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetComponent")
        )
        input_: capo_amplifyuibuilder.types.get_component_request.GetComponentRequest = {
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
        updated_component: "capo_amplifyuibuilder.types.update_component_data.UpdateComponentData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
    ):
        """<p>Updates an existing component.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the component.</p>
            client_token: <p>The unique client token.</p>
            updated_component: <p>The configuration of the updated component.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.update_component_request.UpdateComponentRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_component

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.update_component.update_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateComponent")
        )
        input_: capo_amplifyuibuilder.types.update_component_request.UpdateComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_component": updated_component,
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
        """<p>Deletes a component from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the component to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the component to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest]",
        ) -> OperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_component

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.delete_component.delete_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteComponent")
        )
        input_: capo_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest = {
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
    ) -> "capo_amplifyuibuilder.types.list_components_response.ListComponentsResponse":
        """<p>Retrieves a list of components for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of components to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.list_components_request.ListComponentsRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.list_components_response.ListComponentsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_components

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.list_components.list_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListComponents")
        )
        input_: capo_amplifyuibuilder.types.list_components_request.ListComponentsRequest = {
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

    def export_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_components_response.ExportComponentsResponse":
        """<p>Exports component configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export components to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.export_components_request.ExportComponentsRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.export_components_response.ExportComponentsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_components

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.export_components.export_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportComponents")
        )
        input_: capo_amplifyuibuilder.types.export_components_request.ExportComponentsRequest = {
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


class AsyncComponentResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: str,
        environment_name: str,
        component_to_create: "capo_amplifyuibuilder.types.create_component_data.CreateComponentData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
    ):
        """<p>Creates a new component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the component.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            component_to_create: <p>Represents the configuration of the component to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.create_component_request.CreateComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.create_component.async_create_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateComponent")
        )
        input_: capo_amplifyuibuilder.types.create_component_request.CreateComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "component_to_create": component_to_create,
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
    ) -> "capo_amplifyuibuilder.types.get_component_response.GetComponentResponse":
        """<p>Returns an existing component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the component.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_component_request.GetComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_component_response.GetComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_component.async_get_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetComponent")
        )
        input_: capo_amplifyuibuilder.types.get_component_request.GetComponentRequest = {
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
        updated_component: "capo_amplifyuibuilder.types.update_component_data.UpdateComponentData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
    ):
        """<p>Updates an existing component.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the component.</p>
            client_token: <p>The unique client token.</p>
            updated_component: <p>The configuration of the updated component.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.update_component_request.UpdateComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.update_component.async_update_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateComponent")
        )
        input_: capo_amplifyuibuilder.types.update_component_request.UpdateComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_component": updated_component,
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
        """<p>Deletes a component from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the component to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the component to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.delete_component.async_delete_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteComponent")
        )
        input_: capo_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest = {
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
    ) -> "capo_amplifyuibuilder.types.list_components_response.ListComponentsResponse":
        """<p>Retrieves a list of components for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of components to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_components_request.ListComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_components_response.ListComponentsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_components

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListComponents")
        )
        input_: capo_amplifyuibuilder.types.list_components_request.ListComponentsRequest = {
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

    async def export_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_components_response.ExportComponentsResponse":
        """<p>Exports component configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export components to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.export_components_request.ExportComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.export_components_response.ExportComponentsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_components

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.export_components.async_export_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportComponents")
        )
        input_: capo_amplifyuibuilder.types.export_components_request.ExportComponentsRequest = {
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

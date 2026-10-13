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
    import capo_amplifyuibuilder.types.create_form_data
    import capo_amplifyuibuilder.types.create_form_request
    import capo_amplifyuibuilder.types.create_form_response
    import capo_amplifyuibuilder.types.delete_form_request
    import capo_amplifyuibuilder.types.export_forms_request
    import capo_amplifyuibuilder.types.export_forms_response
    import capo_amplifyuibuilder.types.form
    import capo_amplifyuibuilder.types.form_summary
    import capo_amplifyuibuilder.types.get_form_request
    import capo_amplifyuibuilder.types.get_form_response
    import capo_amplifyuibuilder.types.list_entity_limit
    import capo_amplifyuibuilder.types.list_forms_request
    import capo_amplifyuibuilder.types.list_forms_response
    import capo_amplifyuibuilder.types.update_form_data
    import capo_amplifyuibuilder.types.update_form_request
    import capo_amplifyuibuilder.types.update_form_response
    import capo_amplifyuibuilder.types.uuid
    from capo_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from capo_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class FormResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: str,
        environment_name: str,
        form_to_create: "capo_amplifyuibuilder.types.create_form_data.CreateFormData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.create_form_response.CreateFormResponse":
        """<p>Creates a new form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the form.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            form_to_create: <p>Represents the configuration of the form to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.create_form_request.CreateFormRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.create_form_response.CreateFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_form

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.create_form.create_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateForm")
        )
        input_: capo_amplifyuibuilder.types.create_form_request.CreateFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "form_to_create": form_to_create,
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
    ) -> "capo_amplifyuibuilder.types.get_form_response.GetFormResponse":
        """<p>Returns an existing form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the form.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.get_form_request.GetFormRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.get_form_response.GetFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_form

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.get_form.get_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetForm")
        )
        input_: capo_amplifyuibuilder.types.get_form_request.GetFormRequest = {
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
        updated_form: "capo_amplifyuibuilder.types.update_form_data.UpdateFormData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.update_form_response.UpdateFormResponse":
        """<p>Updates an existing form.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the form.</p>
            client_token: <p>The unique client token.</p>
            updated_form: <p>The request accepts the following data in JSON format.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.update_form_request.UpdateFormRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.update_form_response.UpdateFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_form

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.update_form.update_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateForm")
        )
        input_: capo_amplifyuibuilder.types.update_form_request.UpdateFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_form": updated_form,
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
        """<p>Deletes a form from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the form to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the form to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.delete_form_request.DeleteFormRequest]",
        ) -> OperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_form

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.delete_form.delete_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteForm")
        )
        input_: capo_amplifyuibuilder.types.delete_form_request.DeleteFormRequest = {
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
    ) -> "capo_amplifyuibuilder.types.list_forms_response.ListFormsResponse":
        """<p>Retrieves a list of forms for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of forms to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.list_forms_request.ListFormsRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.list_forms_response.ListFormsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_forms

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.list_forms.list_forms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListForms")
        )
        input_: capo_amplifyuibuilder.types.list_forms_request.ListFormsRequest = {
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

    def export_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_forms_response.ExportFormsResponse":
        """<p>Exports form configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export forms to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.export_forms_request.ExportFormsRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.export_forms_response.ExportFormsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_forms

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.export_forms.export_forms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportForms")
        )
        input_: capo_amplifyuibuilder.types.export_forms_request.ExportFormsRequest = {
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


class AsyncFormResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: str,
        environment_name: str,
        form_to_create: "capo_amplifyuibuilder.types.create_form_data.CreateFormData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.create_form_response.CreateFormResponse":
        """<p>Creates a new form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the form.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            form_to_create: <p>Represents the configuration of the form to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.create_form_request.CreateFormRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.create_form_response.CreateFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.create_form.async_create_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateForm")
        )
        input_: capo_amplifyuibuilder.types.create_form_request.CreateFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "form_to_create": form_to_create,
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
    ) -> "capo_amplifyuibuilder.types.get_form_response.GetFormResponse":
        """<p>Returns an existing form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the form.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_form_request.GetFormRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_form_response.GetFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_form.async_get_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetForm")
        )
        input_: capo_amplifyuibuilder.types.get_form_request.GetFormRequest = {
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
        updated_form: "capo_amplifyuibuilder.types.update_form_data.UpdateFormData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.update_form_response.UpdateFormResponse":
        """<p>Updates an existing form.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the form.</p>
            client_token: <p>The unique client token.</p>
            updated_form: <p>The request accepts the following data in JSON format.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.update_form_request.UpdateFormRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.update_form_response.UpdateFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.update_form.async_update_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateForm")
        )
        input_: capo_amplifyuibuilder.types.update_form_request.UpdateFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_form": updated_form,
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
        """<p>Deletes a form from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the form to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the form to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.delete_form_request.DeleteFormRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.delete_form.async_delete_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteForm")
        )
        input_: capo_amplifyuibuilder.types.delete_form_request.DeleteFormRequest = {
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
    ) -> "capo_amplifyuibuilder.types.list_forms_response.ListFormsResponse":
        """<p>Retrieves a list of forms for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of forms to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_forms_request.ListFormsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_forms_response.ListFormsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_forms

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_forms.async_list_forms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListForms")
        )
        input_: capo_amplifyuibuilder.types.list_forms_request.ListFormsRequest = {
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

    async def export_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_forms_response.ExportFormsResponse":
        """<p>Exports form configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export forms to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.export_forms_request.ExportFormsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.export_forms_response.ExportFormsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_forms

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.export_forms.async_export_forms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportForms")
        )
        input_: capo_amplifyuibuilder.types.export_forms_request.ExportFormsRequest = {
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

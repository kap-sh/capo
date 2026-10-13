from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_codecatalyst._auth._signers
import capo_codecatalyst._auth._sigv4
from capo_codecatalyst._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_codecatalyst.types.delete_space_request
    import capo_codecatalyst.types.delete_space_response
    import capo_codecatalyst.types.dev_environment_summary
    import capo_codecatalyst.types.filters
    import capo_codecatalyst.types.get_space_request
    import capo_codecatalyst.types.get_space_response
    import capo_codecatalyst.types.list_dev_environments_request
    import capo_codecatalyst.types.list_dev_environments_response
    import capo_codecatalyst.types.list_spaces_request
    import capo_codecatalyst.types.list_spaces_response
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.space_description
    import capo_codecatalyst.types.space_summary
    import capo_codecatalyst.types.update_space_request
    import capo_codecatalyst.types.update_space_response
    from capo_codecatalyst._services.async_code_catalyst import (
        AsyncCodeCatalystClient,
        AsyncCodeCatalystClientConfig,
    )
    from capo_codecatalyst._services.code_catalyst import (
        CodeCatalystClient,
        CodeCatalystClientConfig,
    )


class Space:
    def __init__(self, service: CodeCatalystClient) -> None:
        self._service = service

    def read(
        self,
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_space_response.GetSpaceResponse":
        """<p>Returns information about an space.</p>

        Args:
            name: <p>The name of the space.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.get_space_request.GetSpaceRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_space_response.GetSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_space

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_space.get_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSpace")
        )
        input_: capo_codecatalyst.types.get_space_request.GetSpaceRequest = {
            "name": name
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
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        description: Optional[
            "capo_codecatalyst.types.space_description.SpaceDescription"
        ] = None,
    ) -> "capo_codecatalyst.types.update_space_response.UpdateSpaceResponse":
        """<p>Changes one or more values for a space.</p>

        Args:
            name: <p>The name of the space.</p>
            description: <p>The description of the space.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.update_space_request.UpdateSpaceRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.update_space_response.UpdateSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.update_space

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.update_space.update_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSpace")
        )
        input_: capo_codecatalyst.types.update_space_request.UpdateSpaceRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.delete_space_response.DeleteSpaceResponse":
        """<p>Deletes a space.</p> <important> <p>Deleting a space cannot be undone. Additionally, since space names must be unique across Amazon CodeCatalyst, you cannot reuse names of deleted spaces.</p> </important>

        Args:
            name: <p>The name of the space. To retrieve a list of space names, use <a>ListSpaces</a>.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.delete_space_request.DeleteSpaceRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.delete_space_response.DeleteSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_space

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.delete_space.delete_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSpace")
        )
        input_: capo_codecatalyst.types.delete_space_request.DeleteSpaceRequest = {
            "name": name
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
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_codecatalyst.types.list_spaces_response.ListSpacesResponse":
        """<p>Retrieves a list of spaces.</p>

        Args:
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.list_spaces_request.ListSpacesRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_spaces_response.ListSpacesResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_spaces

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_spaces.list_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSpaces")
        )
        input_: capo_codecatalyst.types.list_spaces_request.ListSpacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_dev_environments(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        project_name: Optional["capo_codecatalyst.types.name_string.NameString"] = None,
        filters: Optional["capo_codecatalyst.types.filters.Filters"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse":
        """<p>Retrieves a list of Dev Environments in a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            filters: <p>Information about filters to apply to narrow the results returned in the list.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_dev_environments

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_dev_environments.list_dev_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDevEnvironments")
        )
        input_: capo_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest = {
            "space_name": space_name
        }
        if project_name is not None:
            input_["project_name"] = project_name
        if filters is not None:
            input_["filters"] = filters
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


class AsyncSpace:
    def __init__(self, service: AsyncCodeCatalystClient) -> None:
        self._service = service

    async def read(
        self,
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_space_response.GetSpaceResponse":
        """<p>Returns information about an space.</p>

        Args:
            name: <p>The name of the space.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.get_space_request.GetSpaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.get_space_response.GetSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_space

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.get_space.async_get_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSpace")
        )
        input_: capo_codecatalyst.types.get_space_request.GetSpaceRequest = {
            "name": name
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
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        description: Optional[
            "capo_codecatalyst.types.space_description.SpaceDescription"
        ] = None,
    ) -> "capo_codecatalyst.types.update_space_response.UpdateSpaceResponse":
        """<p>Changes one or more values for a space.</p>

        Args:
            name: <p>The name of the space.</p>
            description: <p>The description of the space.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.update_space_request.UpdateSpaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.update_space_response.UpdateSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.update_space

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.update_space.async_update_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSpace")
        )
        input_: capo_codecatalyst.types.update_space_request.UpdateSpaceRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.delete_space_response.DeleteSpaceResponse":
        """<p>Deletes a space.</p> <important> <p>Deleting a space cannot be undone. Additionally, since space names must be unique across Amazon CodeCatalyst, you cannot reuse names of deleted spaces.</p> </important>

        Args:
            name: <p>The name of the space. To retrieve a list of space names, use <a>ListSpaces</a>.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.delete_space_request.DeleteSpaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.delete_space_response.DeleteSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_space

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.delete_space.async_delete_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSpace")
        )
        input_: capo_codecatalyst.types.delete_space_request.DeleteSpaceRequest = {
            "name": name
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
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_codecatalyst.types.list_spaces_response.ListSpacesResponse":
        """<p>Retrieves a list of spaces.</p>

        Args:
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.list_spaces_request.ListSpacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.list_spaces_response.ListSpacesResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_spaces

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.list_spaces.async_list_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSpaces")
        )
        input_: capo_codecatalyst.types.list_spaces_request.ListSpacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_dev_environments(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        project_name: Optional["capo_codecatalyst.types.name_string.NameString"] = None,
        filters: Optional["capo_codecatalyst.types.filters.Filters"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse":
        """<p>Retrieves a list of Dev Environments in a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            filters: <p>Information about filters to apply to narrow the results returned in the list.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_dev_environments

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.list_dev_environments.async_list_dev_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDevEnvironments")
        )
        input_: capo_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest = {
            "space_name": space_name
        }
        if project_name is not None:
            input_["project_name"] = project_name
        if filters is not None:
            input_["filters"] = filters
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

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_cleanrooms._auth._signers
import capo_cleanrooms._auth._sigv4
from capo_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_cleanrooms.types.create_privacy_budget_template_input
    import capo_cleanrooms.types.create_privacy_budget_template_output
    import capo_cleanrooms.types.delete_privacy_budget_template_input
    import capo_cleanrooms.types.delete_privacy_budget_template_output
    import capo_cleanrooms.types.get_privacy_budget_template_input
    import capo_cleanrooms.types.get_privacy_budget_template_output
    import capo_cleanrooms.types.list_privacy_budget_templates_input
    import capo_cleanrooms.types.list_privacy_budget_templates_output
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.privacy_budget_template_auto_refresh
    import capo_cleanrooms.types.privacy_budget_template_identifier
    import capo_cleanrooms.types.privacy_budget_template_parameters_input
    import capo_cleanrooms.types.privacy_budget_template_summary
    import capo_cleanrooms.types.privacy_budget_template_update_parameters
    import capo_cleanrooms.types.privacy_budget_type
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.update_privacy_budget_template_input
    import capo_cleanrooms.types.update_privacy_budget_template_output
    from capo_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from capo_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class PrivacyBudgetTemplateResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        parameters: "capo_cleanrooms.types.privacy_budget_template_parameters_input.PrivacyBudgetTemplateParametersInput",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        auto_refresh: Optional[
            "capo_cleanrooms.types.privacy_budget_template_auto_refresh.PrivacyBudgetTemplateAutoRefresh"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_privacy_budget_template_output.CreatePrivacyBudgetTemplateOutput":
        """<p>Creates a privacy budget template for a specified collaboration. Each collaboration can have only one privacy budget template. If you need to change the privacy budget template, use the <a>UpdatePrivacyBudgetTemplate</a> operation.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is created in the collaboration that this membership belongs to. Accepts a membership ID.</p>
            auto_refresh: <p>How often the privacy budget refreshes.</p> <important> <p>If you plan to regularly bring new data into the collaboration, you can use <code>CALENDAR_MONTH</code> to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queries across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.</p> </important>
            privacy_budget_type: <p>Specifies the type of the privacy budget template.</p>
            parameters: <p>Specifies your parameters for the privacy budget template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.create_privacy_budget_template_input.CreatePrivacyBudgetTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.create_privacy_budget_template_output.CreatePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_privacy_budget_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_privacy_budget_template.create_privacy_budget_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.create_privacy_budget_template_input.CreatePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_type": privacy_budget_type,
            "parameters": parameters,
        }
        if auto_refresh is not None:
            input_["auto_refresh"] = auto_refresh
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_privacy_budget_template_output.GetPrivacyBudgetTemplateOutput":
        """<p>Returns details for a specified privacy budget template.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.get_privacy_budget_template_input.GetPrivacyBudgetTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.get_privacy_budget_template_output.GetPrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_privacy_budget_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_privacy_budget_template.get_privacy_budget_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.get_privacy_budget_template_input.GetPrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        parameters: Optional[
            "capo_cleanrooms.types.privacy_budget_template_update_parameters.PrivacyBudgetTemplateUpdateParameters"
        ] = None,
    ) -> "capo_cleanrooms.types.update_privacy_budget_template_output.UpdatePrivacyBudgetTemplateOutput":
        """<p>Updates the privacy budget template for the specified collaboration.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is updated in the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template that you want to update.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget template.</p>
            parameters: <p>Specifies the epsilon and noise parameters for the privacy budget template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.update_privacy_budget_template_input.UpdatePrivacyBudgetTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.update_privacy_budget_template_output.UpdatePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_privacy_budget_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_privacy_budget_template.update_privacy_budget_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.update_privacy_budget_template_input.UpdatePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_privacy_budget_template_output.DeletePrivacyBudgetTemplateOutput":
        """<p>Deletes a privacy budget template for a specified collaboration.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is deleted from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.delete_privacy_budget_template_input.DeletePrivacyBudgetTemplateInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.delete_privacy_budget_template_output.DeletePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_privacy_budget_template

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_privacy_budget_template.delete_privacy_budget_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.delete_privacy_budget_template_input.DeletePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_privacy_budget_templates_output.ListPrivacyBudgetTemplatesOutput":
        """<p>Returns detailed information about the privacy budget templates in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget templates are retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanrooms.types.list_privacy_budget_templates_input.ListPrivacyBudgetTemplatesInput]",
        ) -> OperationResponse[
            "capo_cleanrooms.types.list_privacy_budget_templates_output.ListPrivacyBudgetTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budget_templates

            output, http_response = (
                capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budget_templates.list_privacy_budget_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPrivacyBudgetTemplates")
        )
        input_: capo_cleanrooms.types.list_privacy_budget_templates_input.ListPrivacyBudgetTemplatesInput = {
            "membership_identifier": membership_identifier
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


class AsyncPrivacyBudgetTemplateResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        parameters: "capo_cleanrooms.types.privacy_budget_template_parameters_input.PrivacyBudgetTemplateParametersInput",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        auto_refresh: Optional[
            "capo_cleanrooms.types.privacy_budget_template_auto_refresh.PrivacyBudgetTemplateAutoRefresh"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_privacy_budget_template_output.CreatePrivacyBudgetTemplateOutput":
        """<p>Creates a privacy budget template for a specified collaboration. Each collaboration can have only one privacy budget template. If you need to change the privacy budget template, use the <a>UpdatePrivacyBudgetTemplate</a> operation.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is created in the collaboration that this membership belongs to. Accepts a membership ID.</p>
            auto_refresh: <p>How often the privacy budget refreshes.</p> <important> <p>If you plan to regularly bring new data into the collaboration, you can use <code>CALENDAR_MONTH</code> to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queries across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.</p> </important>
            privacy_budget_type: <p>Specifies the type of the privacy budget template.</p>
            parameters: <p>Specifies your parameters for the privacy budget template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_privacy_budget_template_input.CreatePrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_privacy_budget_template_output.CreatePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_privacy_budget_template.async_create_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.create_privacy_budget_template_input.CreatePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_type": privacy_budget_type,
            "parameters": parameters,
        }
        if auto_refresh is not None:
            input_["auto_refresh"] = auto_refresh
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_privacy_budget_template_output.GetPrivacyBudgetTemplateOutput":
        """<p>Returns details for a specified privacy budget template.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_privacy_budget_template_input.GetPrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_privacy_budget_template_output.GetPrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_privacy_budget_template.async_get_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.get_privacy_budget_template_input.GetPrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        parameters: Optional[
            "capo_cleanrooms.types.privacy_budget_template_update_parameters.PrivacyBudgetTemplateUpdateParameters"
        ] = None,
    ) -> "capo_cleanrooms.types.update_privacy_budget_template_output.UpdatePrivacyBudgetTemplateOutput":
        """<p>Updates the privacy budget template for the specified collaboration.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is updated in the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template that you want to update.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget template.</p>
            parameters: <p>Specifies the epsilon and noise parameters for the privacy budget template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_privacy_budget_template_input.UpdatePrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_privacy_budget_template_output.UpdatePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_privacy_budget_template.async_update_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.update_privacy_budget_template_input.UpdatePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_privacy_budget_template_output.DeletePrivacyBudgetTemplateOutput":
        """<p>Deletes a privacy budget template for a specified collaboration.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is deleted from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_privacy_budget_template_input.DeletePrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_privacy_budget_template_output.DeletePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_privacy_budget_template.async_delete_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePrivacyBudgetTemplate")
        )
        input_: capo_cleanrooms.types.delete_privacy_budget_template_input.DeletePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
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
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_privacy_budget_templates_output.ListPrivacyBudgetTemplatesOutput":
        """<p>Returns detailed information about the privacy budget templates in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget templates are retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_privacy_budget_templates_input.ListPrivacyBudgetTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_privacy_budget_templates_output.ListPrivacyBudgetTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budget_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budget_templates.async_list_privacy_budget_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPrivacyBudgetTemplates")
        )
        input_: capo_cleanrooms.types.list_privacy_budget_templates_input.ListPrivacyBudgetTemplatesInput = {
            "membership_identifier": membership_identifier
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

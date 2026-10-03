from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_connectcases._auth._signers
import capo_connectcases._auth._sigv4
from capo_connectcases._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_connectcases.types.create_template_request
    import capo_connectcases.types.create_template_response
    import capo_connectcases.types.delete_template_request
    import capo_connectcases.types.delete_template_response
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.get_template_request
    import capo_connectcases.types.get_template_response
    import capo_connectcases.types.layout_configuration
    import capo_connectcases.types.list_templates_request
    import capo_connectcases.types.list_templates_response
    import capo_connectcases.types.max_results
    import capo_connectcases.types.next_token
    import capo_connectcases.types.required_field_list
    import capo_connectcases.types.tag_propagation_configuration_list
    import capo_connectcases.types.template_case_rule_list
    import capo_connectcases.types.template_description
    import capo_connectcases.types.template_id
    import capo_connectcases.types.template_name
    import capo_connectcases.types.template_status
    import capo_connectcases.types.template_status_filters
    import capo_connectcases.types.update_template_request
    import capo_connectcases.types.update_template_response
    from capo_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from capo_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class Template:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.template_name.TemplateName",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.template_description.TemplateDescription"
        ] = None,
        layout_configuration: Optional[
            "capo_connectcases.types.layout_configuration.LayoutConfiguration"
        ] = None,
        required_fields: Optional[
            "capo_connectcases.types.required_field_list.RequiredFieldList"
        ] = None,
        status: Optional[
            "capo_connectcases.types.template_status.TemplateStatus"
        ] = None,
        rules: Optional[
            "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
        ] = None,
        tag_propagation_configurations: Optional[
            "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
        ] = None,
    ) -> "capo_connectcases.types.create_template_response.CreateTemplateResponse":
        """<p>Creates a template in the Cases domain. This template is used to define the case object model (that is, to define what data can be captured on cases) in a Cases domain. A template must have a unique name within a domain, and it must reference existing field IDs and layout IDs. Additionally, multiple fields with same IDs are not allowed within the same Template. A template can be either Active or Inactive, as indicated by its status. Inactive templates cannot be used to create cases.</p> <p> Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>A name for the template. It must be unique per domain.</p>
            description: <p>A brief description of the template.</p>
            layout_configuration: <p>Configuration of layouts associated to the template.</p>
            required_fields: <p>A list of fields that must contain a value for a case to be successfully created with this template.</p>
            status: <p>The status of the template.</p>
            rules: <p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template. </p>
            tag_propagation_configurations: <p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.create_template_request.CreateTemplateRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_template

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.create_template.create_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_template_request.CreateTemplateRequest = {
            "domain_id": domain_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if layout_configuration is not None:
            input_["layout_configuration"] = layout_configuration
        if required_fields is not None:
            input_["required_fields"] = required_fields
        if status is not None:
            input_["status"] = status
        if rules is not None:
            input_["rules"] = rules
        if tag_propagation_configurations is not None:
            input_["tag_propagation_configurations"] = tag_propagation_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_template_response.GetTemplateResponse":
        """<p>Returns the details for the requested template. Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.get_template_request.GetTemplateRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.get_template_response.GetTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_template

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.get_template.get_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.get_template_request.GetTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
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
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.template_name.TemplateName"] = None,
        description: Optional[
            "capo_connectcases.types.template_description.TemplateDescription"
        ] = None,
        layout_configuration: Optional[
            "capo_connectcases.types.layout_configuration.LayoutConfiguration"
        ] = None,
        required_fields: Optional[
            "capo_connectcases.types.required_field_list.RequiredFieldList"
        ] = None,
        status: Optional[
            "capo_connectcases.types.template_status.TemplateStatus"
        ] = None,
        rules: Optional[
            "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
        ] = None,
        tag_propagation_configurations: Optional[
            "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
        ] = None,
    ) -> "capo_connectcases.types.update_template_response.UpdateTemplateResponse":
        """<p>Updates the attributes of an existing template. The template attributes that can be modified include <code>name</code>, <code>description</code>, <code>layoutConfiguration</code>, <code>requiredFields</code>, and <code>status</code>. At least one of these attributes must not be null. If a null value is provided for a given attribute, that attribute is ignored and its current value is preserved.</p> <p>Other template APIs are:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier for the template.</p>
            name: <p>The name of the template. It must be unique per domain.</p>
            description: <p>A brief description of the template.</p>
            layout_configuration: <p>Configuration of layouts associated to the template.</p>
            required_fields: <p>A list of fields that must contain a value for a case to be successfully created with this template.</p>
            status: <p>The status of the template.</p>
            rules: <p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template.</p>
            tag_propagation_configurations: <p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.update_template_request.UpdateTemplateRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.update_template_response.UpdateTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_template

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.update_template.update_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.update_template_request.UpdateTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if layout_configuration is not None:
            input_["layout_configuration"] = layout_configuration
        if required_fields is not None:
            input_["required_fields"] = required_fields
        if status is not None:
            input_["status"] = status
        if rules is not None:
            input_["rules"] = rules
        if tag_propagation_configurations is not None:
            input_["tag_propagation_configurations"] = tag_propagation_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_template_response.DeleteTemplateResponse":
        """<p>Deletes a cases template. You can delete up to 100 templates per domain.</p> <p>After a cases template is deleted:</p> <ul> <li> <p>You can still retrieve the template by calling <code>GetTemplate</code>.</p> </li> <li> <p>You cannot update the template. </p> </li> <li> <p>You cannot create a case by using the deleted template.</p> </li> <li> <p>Deleted templates are not included in the <code>ListTemplates</code> response.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            template_id: <p>A unique identifier of a template.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.delete_template_request.DeleteTemplateRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.delete_template_response.DeleteTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_template

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.delete_template.delete_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_template_request.DeleteTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
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
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        status: Optional[
            "capo_connectcases.types.template_status_filters.TemplateStatusFilters"
        ] = None,
    ) -> "capo_connectcases.types.list_templates_response.ListTemplatesResponse":
        """<p>Lists all of the templates in a Cases domain. Each list item is a condensed summary object of the template. </p> <p> Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            status: <p>A list of status values to filter on.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.list_templates_request.ListTemplatesRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_templates

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.list_templates.list_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_templates_request.ListTemplatesRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTemplate:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.template_description.TemplateDescription"
        ] = None,
        layout_configuration: Optional[
            "capo_connectcases.types.layout_configuration.LayoutConfiguration"
        ] = None,
        required_fields: Optional[
            "capo_connectcases.types.required_field_list.RequiredFieldList"
        ] = None,
        status: Optional[
            "capo_connectcases.types.template_status.TemplateStatus"
        ] = None,
        rules: Optional[
            "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
        ] = None,
        tag_propagation_configurations: Optional[
            "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
        ] = None,
    ) -> "capo_connectcases.types.create_template_response.CreateTemplateResponse":
        """<p>Creates a template in the Cases domain. This template is used to define the case object model (that is, to define what data can be captured on cases) in a Cases domain. A template must have a unique name within a domain, and it must reference existing field IDs and layout IDs. Additionally, multiple fields with same IDs are not allowed within the same Template. A template can be either Active or Inactive, as indicated by its status. Inactive templates cannot be used to create cases.</p> <p> Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>A name for the template. It must be unique per domain.</p>
            description: <p>A brief description of the template.</p>
            layout_configuration: <p>Configuration of layouts associated to the template.</p>
            required_fields: <p>A list of fields that must contain a value for a case to be successfully created with this template.</p>
            status: <p>The status of the template.</p>
            rules: <p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template. </p>
            tag_propagation_configurations: <p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_template_request.CreateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_template.async_create_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_template_request.CreateTemplateRequest = {
            "domain_id": domain_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if layout_configuration is not None:
            input_["layout_configuration"] = layout_configuration
        if required_fields is not None:
            input_["required_fields"] = required_fields
        if status is not None:
            input_["status"] = status
        if rules is not None:
            input_["rules"] = rules
        if tag_propagation_configurations is not None:
            input_["tag_propagation_configurations"] = tag_propagation_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_template_response.GetTemplateResponse":
        """<p>Returns the details for the requested template. Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_template_request.GetTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_template_response.GetTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_template.async_get_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.get_template_request.GetTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
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
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.template_name.TemplateName"] = None,
        description: Optional[
            "capo_connectcases.types.template_description.TemplateDescription"
        ] = None,
        layout_configuration: Optional[
            "capo_connectcases.types.layout_configuration.LayoutConfiguration"
        ] = None,
        required_fields: Optional[
            "capo_connectcases.types.required_field_list.RequiredFieldList"
        ] = None,
        status: Optional[
            "capo_connectcases.types.template_status.TemplateStatus"
        ] = None,
        rules: Optional[
            "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
        ] = None,
        tag_propagation_configurations: Optional[
            "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
        ] = None,
    ) -> "capo_connectcases.types.update_template_response.UpdateTemplateResponse":
        """<p>Updates the attributes of an existing template. The template attributes that can be modified include <code>name</code>, <code>description</code>, <code>layoutConfiguration</code>, <code>requiredFields</code>, and <code>status</code>. At least one of these attributes must not be null. If a null value is provided for a given attribute, that attribute is ignored and its current value is preserved.</p> <p>Other template APIs are:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier for the template.</p>
            name: <p>The name of the template. It must be unique per domain.</p>
            description: <p>A brief description of the template.</p>
            layout_configuration: <p>Configuration of layouts associated to the template.</p>
            required_fields: <p>A list of fields that must contain a value for a case to be successfully created with this template.</p>
            status: <p>The status of the template.</p>
            rules: <p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template.</p>
            tag_propagation_configurations: <p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_template_request.UpdateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_template_response.UpdateTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_template.async_update_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.update_template_request.UpdateTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if layout_configuration is not None:
            input_["layout_configuration"] = layout_configuration
        if required_fields is not None:
            input_["required_fields"] = required_fields
        if status is not None:
            input_["status"] = status
        if rules is not None:
            input_["rules"] = rules
        if tag_propagation_configurations is not None:
            input_["tag_propagation_configurations"] = tag_propagation_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_template_response.DeleteTemplateResponse":
        """<p>Deletes a cases template. You can delete up to 100 templates per domain.</p> <p>After a cases template is deleted:</p> <ul> <li> <p>You can still retrieve the template by calling <code>GetTemplate</code>.</p> </li> <li> <p>You cannot update the template. </p> </li> <li> <p>You cannot create a case by using the deleted template.</p> </li> <li> <p>Deleted templates are not included in the <code>ListTemplates</code> response.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            template_id: <p>A unique identifier of a template.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_template_request.DeleteTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_template_response.DeleteTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_template.async_delete_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_template_request.DeleteTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
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
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        status: Optional[
            "capo_connectcases.types.template_status_filters.TemplateStatusFilters"
        ] = None,
    ) -> "capo_connectcases.types.list_templates_response.ListTemplatesResponse":
        """<p>Lists all of the templates in a Cases domain. Each list item is a condensed summary object of the template. </p> <p> Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            status: <p>A list of status values to filter on.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_templates_request.ListTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_templates

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_templates_request.ListTemplatesRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

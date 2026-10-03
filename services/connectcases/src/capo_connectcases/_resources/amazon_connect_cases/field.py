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
    import capo_connectcases.types.batch_get_field_identifier_list
    import capo_connectcases.types.batch_get_field_request
    import capo_connectcases.types.batch_get_field_response
    import capo_connectcases.types.batch_put_field_options_request
    import capo_connectcases.types.batch_put_field_options_response
    import capo_connectcases.types.create_field_request
    import capo_connectcases.types.create_field_response
    import capo_connectcases.types.delete_field_request
    import capo_connectcases.types.delete_field_response
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_attributes
    import capo_connectcases.types.field_description
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_name
    import capo_connectcases.types.field_options_list
    import capo_connectcases.types.field_type
    import capo_connectcases.types.list_field_options_request
    import capo_connectcases.types.list_field_options_response
    import capo_connectcases.types.list_fields_request
    import capo_connectcases.types.list_fields_response
    import capo_connectcases.types.max_results
    import capo_connectcases.types.next_token
    import capo_connectcases.types.update_field_request
    import capo_connectcases.types.update_field_response
    import capo_connectcases.types.values_list
    from capo_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from capo_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class Field:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.field_name.FieldName",
        type: "capo_connectcases.types.field_type.FieldType",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.field_description.FieldDescription"
        ] = None,
        attributes: Optional[
            "capo_connectcases.types.field_attributes.FieldAttributes"
        ] = None,
    ) -> "capo_connectcases.types.create_field_response.CreateFieldResponse":
        """<p>Creates a field in the Cases domain. This field is used to define the case object model (that is, defines what data can be captured on cases) in a Cases domain. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>The name of the field.</p>
            type: <p>Defines the data type, some system constraints, and default display of the field.</p>
            description: <p>The description of the field.</p>
            attributes: <p>Union of field attributes.</p>

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
            req: "OperationRequest[capo_connectcases.types.create_field_request.CreateFieldRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.create_field_response.CreateFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_field

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.create_field.create_field(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_field_request.CreateFieldRequest = {
            "domain_id": domain_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if attributes is not None:
            input_["attributes"] = attributes

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
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.field_name.FieldName"] = None,
        description: Optional[
            "capo_connectcases.types.field_description.FieldDescription"
        ] = None,
        attributes: Optional[
            "capo_connectcases.types.field_attributes.FieldAttributes"
        ] = None,
    ) -> "capo_connectcases.types.update_field_response.UpdateFieldResponse":
        """<p>Updates the properties of an existing field. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            name: <p>The name of the field.</p>
            description: <p>The description of a field.</p>
            attributes: <p>Union of field attributes.</p>

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
            req: "OperationRequest[capo_connectcases.types.update_field_request.UpdateFieldRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.update_field_response.UpdateFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_field

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.update_field.update_field(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.update_field_request.UpdateFieldRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if attributes is not None:
            input_["attributes"] = attributes

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
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_field_response.DeleteFieldResponse":
        """<p>Deletes a field from a cases template.</p> <p>After a field is deleted:</p> <ul> <li> <p>You can still retrieve the field by calling <code>BatchGetField</code>.</p> </li> <li> <p>You cannot update a deleted field by calling <code>UpdateField</code>; it throws a <code>ValidationException</code>.</p> </li> <li> <p>Deleted fields are not included in the <code>ListFields</code> response.</p> </li> <li> <p>Calling <code>CreateCase</code> with a deleted field throws a <code>ValidationException</code> denoting which field identifiers in the request have been deleted.</p> </li> <li> <p>Calling <code>GetCase</code> with a deleted field identifier returns the deleted field's value if one exists.</p> </li> <li> <p>Calling <code>UpdateCase</code> with a deleted field ID throws a <code>ValidationException</code> if the case does not already contain a value for the deleted field. Otherwise it succeeds, allowing you to update or remove (using <code>emptyValue: {}</code>) the field's value from the case.</p> </li> <li> <p> <code>GetTemplate</code> does not return field IDs for deleted fields.</p> </li> <li> <p> <code>GetLayout</code> does not return field IDs for deleted fields.</p> </li> <li> <p>Calling <code>SearchCases</code> with the deleted field ID as a filter returns any cases that have a value for the deleted field that matches the filter criteria.</p> </li> <li> <p>Calling <code>SearchCases</code> with a <code>searchTerm</code> value that matches a deleted field's value on a case returns the case in the response.</p> </li> <li> <p>Calling <code>BatchPutFieldOptions</code> with a deleted field ID throw a <code>ValidationException</code>.</p> </li> <li> <p>Calling <code>GetCaseEventConfiguration</code> does not return field IDs for deleted fields.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            field_id: <p>Unique identifier of the field.</p>

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
            req: "OperationRequest[capo_connectcases.types.delete_field_request.DeleteFieldRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.delete_field_response.DeleteFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_field

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.delete_field.delete_field(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_field_request.DeleteFieldRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
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
    ) -> "capo_connectcases.types.list_fields_response.ListFieldsResponse":
        """<p>Lists all fields in a Cases domain.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.list_fields_request.ListFieldsRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.list_fields_response.ListFieldsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_fields

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.list_fields.list_fields(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_fields_request.ListFieldsRequest = {
            "domain_id": domain_id
        }
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

    def batch_put_field_options(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        options: "capo_connectcases.types.field_options_list.FieldOptionsList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.batch_put_field_options_response.BatchPutFieldOptionsResponse":
        """<p>Creates and updates a set of field options for a single select field in a Cases domain.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            options: <p>A list of <code>FieldOption</code> objects.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.batch_put_field_options_request.BatchPutFieldOptionsRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.batch_put_field_options_response.BatchPutFieldOptionsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_put_field_options

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.batch_put_field_options.batch_put_field_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_put_field_options_request.BatchPutFieldOptionsRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
            "options": options,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_field_options(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        values: Optional["capo_connectcases.types.values_list.ValuesList"] = None,
    ) -> "capo_connectcases.types.list_field_options_response.ListFieldOptionsResponse":
        """<p>Lists all of the field options for a field identifier in the domain. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            values: <p>A list of <code>FieldOption</code> values to filter on for <code>ListFieldOptions</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.list_field_options_request.ListFieldOptionsRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.list_field_options_response.ListFieldOptionsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_field_options

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.list_field_options.list_field_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_field_options_request.ListFieldOptionsRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if values is not None:
            input_["values"] = values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_field(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        fields: "capo_connectcases.types.batch_get_field_identifier_list.BatchGetFieldIdentifierList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.batch_get_field_response.BatchGetFieldResponse":
        """<p>Returns the description for the list of fields in the request parameters. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectcases.types.batch_get_field_request.BatchGetFieldRequest]",
        ) -> OperationResponse[
            "capo_connectcases.types.batch_get_field_response.BatchGetFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_get_field

            output, http_response = (
                capo_connectcases._operations.amazon_connect_cases.batch_get_field.batch_get_field(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_get_field_request.BatchGetFieldRequest = {
            "domain_id": domain_id,
            "fields": fields,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncField:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.field_name.FieldName",
        type: "capo_connectcases.types.field_type.FieldType",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.field_description.FieldDescription"
        ] = None,
        attributes: Optional[
            "capo_connectcases.types.field_attributes.FieldAttributes"
        ] = None,
    ) -> "capo_connectcases.types.create_field_response.CreateFieldResponse":
        """<p>Creates a field in the Cases domain. This field is used to define the case object model (that is, defines what data can be captured on cases) in a Cases domain. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>The name of the field.</p>
            type: <p>Defines the data type, some system constraints, and default display of the field.</p>
            description: <p>The description of the field.</p>
            attributes: <p>Union of field attributes.</p>

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
            req: "AsyncOperationRequest[capo_connectcases.types.create_field_request.CreateFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_field_response.CreateFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_field.async_create_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.create_field_request.CreateFieldRequest = {
            "domain_id": domain_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if attributes is not None:
            input_["attributes"] = attributes

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
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.field_name.FieldName"] = None,
        description: Optional[
            "capo_connectcases.types.field_description.FieldDescription"
        ] = None,
        attributes: Optional[
            "capo_connectcases.types.field_attributes.FieldAttributes"
        ] = None,
    ) -> "capo_connectcases.types.update_field_response.UpdateFieldResponse":
        """<p>Updates the properties of an existing field. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            name: <p>The name of the field.</p>
            description: <p>The description of a field.</p>
            attributes: <p>Union of field attributes.</p>

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
            req: "AsyncOperationRequest[capo_connectcases.types.update_field_request.UpdateFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_field_response.UpdateFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_field.async_update_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.update_field_request.UpdateFieldRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if attributes is not None:
            input_["attributes"] = attributes

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
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_field_response.DeleteFieldResponse":
        """<p>Deletes a field from a cases template.</p> <p>After a field is deleted:</p> <ul> <li> <p>You can still retrieve the field by calling <code>BatchGetField</code>.</p> </li> <li> <p>You cannot update a deleted field by calling <code>UpdateField</code>; it throws a <code>ValidationException</code>.</p> </li> <li> <p>Deleted fields are not included in the <code>ListFields</code> response.</p> </li> <li> <p>Calling <code>CreateCase</code> with a deleted field throws a <code>ValidationException</code> denoting which field identifiers in the request have been deleted.</p> </li> <li> <p>Calling <code>GetCase</code> with a deleted field identifier returns the deleted field's value if one exists.</p> </li> <li> <p>Calling <code>UpdateCase</code> with a deleted field ID throws a <code>ValidationException</code> if the case does not already contain a value for the deleted field. Otherwise it succeeds, allowing you to update or remove (using <code>emptyValue: {}</code>) the field's value from the case.</p> </li> <li> <p> <code>GetTemplate</code> does not return field IDs for deleted fields.</p> </li> <li> <p> <code>GetLayout</code> does not return field IDs for deleted fields.</p> </li> <li> <p>Calling <code>SearchCases</code> with the deleted field ID as a filter returns any cases that have a value for the deleted field that matches the filter criteria.</p> </li> <li> <p>Calling <code>SearchCases</code> with a <code>searchTerm</code> value that matches a deleted field's value on a case returns the case in the response.</p> </li> <li> <p>Calling <code>BatchPutFieldOptions</code> with a deleted field ID throw a <code>ValidationException</code>.</p> </li> <li> <p>Calling <code>GetCaseEventConfiguration</code> does not return field IDs for deleted fields.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            field_id: <p>Unique identifier of the field.</p>

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
            req: "AsyncOperationRequest[capo_connectcases.types.delete_field_request.DeleteFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_field_response.DeleteFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_field.async_delete_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_field_request.DeleteFieldRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
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
    ) -> "capo_connectcases.types.list_fields_response.ListFieldsResponse":
        """<p>Lists all fields in a Cases domain.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_fields_request.ListFieldsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_fields_response.ListFieldsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_fields

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_fields.async_list_fields(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_fields_request.ListFieldsRequest = {
            "domain_id": domain_id
        }
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

    async def batch_put_field_options(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        options: "capo_connectcases.types.field_options_list.FieldOptionsList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.batch_put_field_options_response.BatchPutFieldOptionsResponse":
        """<p>Creates and updates a set of field options for a single select field in a Cases domain.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            options: <p>A list of <code>FieldOption</code> objects.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_put_field_options_request.BatchPutFieldOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_put_field_options_response.BatchPutFieldOptionsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_put_field_options

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_put_field_options.async_batch_put_field_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_put_field_options_request.BatchPutFieldOptionsRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
            "options": options,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_field_options(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        values: Optional["capo_connectcases.types.values_list.ValuesList"] = None,
    ) -> "capo_connectcases.types.list_field_options_response.ListFieldOptionsResponse":
        """<p>Lists all of the field options for a field identifier in the domain. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            values: <p>A list of <code>FieldOption</code> values to filter on for <code>ListFieldOptions</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_field_options_request.ListFieldOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_field_options_response.ListFieldOptionsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_field_options

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_field_options.async_list_field_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.list_field_options_request.ListFieldOptionsRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if values is not None:
            input_["values"] = values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_field(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        fields: "capo_connectcases.types.batch_get_field_identifier_list.BatchGetFieldIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.batch_get_field_response.BatchGetFieldResponse":
        """<p>Returns the description for the list of fields in the request parameters. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_get_field_request.BatchGetFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_get_field_response.BatchGetFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_get_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_get_field.async_batch_get_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_get_field_request.BatchGetFieldRequest = {
            "domain_id": domain_id,
            "fields": fields,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

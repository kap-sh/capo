from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.create_form_type_input
    import capo_datazone.types.create_form_type_output
    import capo_datazone.types.delete_form_type_input
    import capo_datazone.types.delete_form_type_output
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.form_type_name
    import capo_datazone.types.form_type_status
    import capo_datazone.types.get_form_type_input
    import capo_datazone.types.get_form_type_output
    import capo_datazone.types.model
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class FormType:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.form_type_name.FormTypeName",
        model: "capo_datazone.types.model.Model",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.form_type_status.FormTypeStatus"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
    ) -> "capo_datazone.types.create_form_type_output.CreateFormTypeOutput":
        """<p>Creates a metadata form type.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain must exist and be in an <code>ENABLED</code> state. </p> </li> <li> <p>The owning project must exist and be accessible.</p> </li> <li> <p>The name must be unique within the domain.</p> </li> </ul> <p>For custom form types, to indicate that a field should be searchable, annotate it with <code>@amazon.datazone#searchable</code>. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. To indicate that a field should be indexed for lexical search (which disables semantic search but supports stemmed and partial matches), annotate it with <code>@amazon.datazone#searchable(modes:["LEXICAL"])</code>. To indicate that a field should be indexed for technical identifier search (for more information on technical identifier search, see: <a href="https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/">https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/</a>), annotate it with <code>@amazon.datazone#searchable(modes:["TECHNICAL"])</code>.</p> <p>To denote that a field will store glossary term ids (which are filterable via the Search/SearchListings APIs), annotate it with <code>@amazon.datazone#glossaryterm("${GLOSSARY_ID}")</code>, where <code>${GLOSSARY_ID}</code> is the id of the glossary that the glossary terms stored in the field belong to. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this metadata form type is created.</p>
            name: <p>The name of this Amazon DataZone metadata form type.</p>
            model: <p>The model of this Amazon DataZone metadata form type.</p>
            owning_project_identifier: <p>The ID of the Amazon DataZone project that owns this metadata form type.</p>
            status: <p>The status of this Amazon DataZone metadata form type.</p>
            description: <p>The description of this Amazon DataZone metadata form type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.create_form_type_input.CreateFormTypeInput]",
        ) -> OperationResponse[
            "capo_datazone.types.create_form_type_output.CreateFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.create_form_type

            output, http_response = (
                capo_datazone._operations.data_zone.create_form_type.create_form_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.create_form_type_input.CreateFormTypeInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "model": model,
            "owning_project_identifier": owning_project_identifier,
        }
        if status is not None:
            input_["status"] = status
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_form_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        form_type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_form_type_output.DeleteFormTypeOutput":
        """<p>Deletes and metadata form type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The form type must exist in the domain. </p> </li> <li> <p>The form type must not be in use by any asset types or assets.</p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>User must have delete permissions on the form type.</p> </li> <li> <p>Any dependencies (such as linked asset types) must be removed first.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata form type is deleted.</p>
            form_type_identifier: <p>The ID of the metadata form type that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_form_type_input.DeleteFormTypeInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_form_type_output.DeleteFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_form_type

            output, http_response = (
                capo_datazone._operations.data_zone.delete_form_type.delete_form_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.delete_form_type_input.DeleteFormTypeInput = {
            "domain_identifier": domain_identifier,
            "form_type_identifier": form_type_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_form_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        form_type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_form_type_output.GetFormTypeOutput":
        """<p>Gets a metadata form type in Amazon DataZone.</p> <p>Form types define the structure and validation rules for collecting metadata about assets in Amazon DataZone. They act as templates that ensure consistent metadata capture across similar types of assets, while allowing for customization to meet specific organizational needs. Form types can include required fields, validation rules, and dependencies, helping maintain high-quality metadata that makes data assets more discoverable and usable.</p> <ul> <li> <p>The form type with the specified identifier must exist in the given domain. </p> </li> <li> <p>The domain must be valid and active.</p> </li> <li> <p>User must have permission on the form type.</p> </li> <li> <p>The form type should not be deleted or in an invalid state.</p> </li> </ul> <p>One use case for this API is to determine whether a form field is indexed for search. </p> <p>A searchable field will be annotated with <code>@amazon.datazone#searchable</code>. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. If a field is indexed technical identifier search, it will be annotated with <code>@amazon.datazone#searchable(modes:["TECHNICAL"])</code>. If a field is indexed for lexical search (supports stemmed and prefix matches but not semantic matches), it will be annotated with <code>@amazon.datazone#searchable(modes:["LEXICAL"])</code>.</p> <p>A field storing glossary term IDs (which is filterable) will be annotated with <code>@amazon.datazone#glossaryterm("${glossaryId}")</code>. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this metadata form type exists.</p>
            form_type_identifier: <p>The ID of the metadata form type.</p>
            revision: <p>The revision of this metadata form type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_form_type_input.GetFormTypeInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_form_type_output.GetFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.get_form_type

            output, http_response = (
                capo_datazone._operations.data_zone.get_form_type.get_form_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.get_form_type_input.GetFormTypeInput = {
            "domain_identifier": domain_identifier,
            "form_type_identifier": form_type_identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFormType:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.form_type_name.FormTypeName",
        model: "capo_datazone.types.model.Model",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.form_type_status.FormTypeStatus"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
    ) -> "capo_datazone.types.create_form_type_output.CreateFormTypeOutput":
        """<p>Creates a metadata form type.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain must exist and be in an <code>ENABLED</code> state. </p> </li> <li> <p>The owning project must exist and be accessible.</p> </li> <li> <p>The name must be unique within the domain.</p> </li> </ul> <p>For custom form types, to indicate that a field should be searchable, annotate it with <code>@amazon.datazone#searchable</code>. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. To indicate that a field should be indexed for lexical search (which disables semantic search but supports stemmed and partial matches), annotate it with <code>@amazon.datazone#searchable(modes:["LEXICAL"])</code>. To indicate that a field should be indexed for technical identifier search (for more information on technical identifier search, see: <a href="https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/">https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/</a>), annotate it with <code>@amazon.datazone#searchable(modes:["TECHNICAL"])</code>.</p> <p>To denote that a field will store glossary term ids (which are filterable via the Search/SearchListings APIs), annotate it with <code>@amazon.datazone#glossaryterm("${GLOSSARY_ID}")</code>, where <code>${GLOSSARY_ID}</code> is the id of the glossary that the glossary terms stored in the field belong to. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this metadata form type is created.</p>
            name: <p>The name of this Amazon DataZone metadata form type.</p>
            model: <p>The model of this Amazon DataZone metadata form type.</p>
            owning_project_identifier: <p>The ID of the Amazon DataZone project that owns this metadata form type.</p>
            status: <p>The status of this Amazon DataZone metadata form type.</p>
            description: <p>The description of this Amazon DataZone metadata form type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_form_type_input.CreateFormTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_form_type_output.CreateFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.create_form_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_form_type.async_create_form_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.create_form_type_input.CreateFormTypeInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "model": model,
            "owning_project_identifier": owning_project_identifier,
        }
        if status is not None:
            input_["status"] = status
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_form_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        form_type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_form_type_output.DeleteFormTypeOutput":
        """<p>Deletes and metadata form type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The form type must exist in the domain. </p> </li> <li> <p>The form type must not be in use by any asset types or assets.</p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>User must have delete permissions on the form type.</p> </li> <li> <p>Any dependencies (such as linked asset types) must be removed first.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata form type is deleted.</p>
            form_type_identifier: <p>The ID of the metadata form type that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_form_type_input.DeleteFormTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_form_type_output.DeleteFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_form_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_form_type.async_delete_form_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.delete_form_type_input.DeleteFormTypeInput = {
            "domain_identifier": domain_identifier,
            "form_type_identifier": form_type_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_form_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        form_type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_form_type_output.GetFormTypeOutput":
        """<p>Gets a metadata form type in Amazon DataZone.</p> <p>Form types define the structure and validation rules for collecting metadata about assets in Amazon DataZone. They act as templates that ensure consistent metadata capture across similar types of assets, while allowing for customization to meet specific organizational needs. Form types can include required fields, validation rules, and dependencies, helping maintain high-quality metadata that makes data assets more discoverable and usable.</p> <ul> <li> <p>The form type with the specified identifier must exist in the given domain. </p> </li> <li> <p>The domain must be valid and active.</p> </li> <li> <p>User must have permission on the form type.</p> </li> <li> <p>The form type should not be deleted or in an invalid state.</p> </li> </ul> <p>One use case for this API is to determine whether a form field is indexed for search. </p> <p>A searchable field will be annotated with <code>@amazon.datazone#searchable</code>. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. If a field is indexed technical identifier search, it will be annotated with <code>@amazon.datazone#searchable(modes:["TECHNICAL"])</code>. If a field is indexed for lexical search (supports stemmed and prefix matches but not semantic matches), it will be annotated with <code>@amazon.datazone#searchable(modes:["LEXICAL"])</code>.</p> <p>A field storing glossary term IDs (which is filterable) will be annotated with <code>@amazon.datazone#glossaryterm("${glossaryId}")</code>. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this metadata form type exists.</p>
            form_type_identifier: <p>The ID of the metadata form type.</p>
            revision: <p>The revision of this metadata form type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_form_type_input.GetFormTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_form_type_output.GetFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.get_form_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_form_type.async_get_form_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.get_form_type_input.GetFormTypeInput = {
            "domain_identifier": domain_identifier,
            "form_type_identifier": form_type_identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

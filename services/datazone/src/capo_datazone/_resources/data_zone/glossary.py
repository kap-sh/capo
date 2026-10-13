from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.create_glossary_input
    import capo_datazone.types.create_glossary_output
    import capo_datazone.types.delete_glossary_input
    import capo_datazone.types.delete_glossary_output
    import capo_datazone.types.domain_id
    import capo_datazone.types.get_glossary_input
    import capo_datazone.types.get_glossary_output
    import capo_datazone.types.glossary_description
    import capo_datazone.types.glossary_id
    import capo_datazone.types.glossary_name
    import capo_datazone.types.glossary_status
    import capo_datazone.types.glossary_usage_restrictions
    import capo_datazone.types.project_id
    import capo_datazone.types.update_glossary_input
    import capo_datazone.types.update_glossary_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class Glossary:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.glossary_name.GlossaryName",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[
            "capo_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional["capo_datazone.types.glossary_status.GlossaryStatus"] = None,
        usage_restrictions: Optional[
            "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_glossary_output.CreateGlossaryOutput":
        """<p>Creates an Amazon DataZone business glossary.</p> <p>Specifies that this is a create glossary policy.</p> <p>A glossary serves as the central repository for business terminology and definitions within an organization. It helps establish and maintain a common language across different departments and teams, reducing miscommunication and ensuring consistent interpretation of business concepts. Glossaries can include hierarchical relationships between terms, cross-references, and links to actual data assets, making them invaluable for both business users and technical teams trying to understand and use data correctly.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist and be in an active state. </p> </li> <li> <p>Owning project must exist and be accessible by the caller.</p> </li> <li> <p>The glossary name must be unique within the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>
            name: <p>The name of this business glossary.</p>
            owning_project_identifier: <p>The ID of the project that currently owns business glossary.</p>
            description: <p>The description of this business glossary.</p>
            status: <p>The status of this business glossary.</p>
            usage_restrictions: <p>The usage restriction of the restricted glossary.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

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
            req: "OperationRequest[capo_datazone.types.create_glossary_input.CreateGlossaryInput]",
        ) -> OperationResponse[
            "capo_datazone.types.create_glossary_output.CreateGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.create_glossary

            output, http_response = (
                capo_datazone._operations.data_zone.create_glossary.create_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_glossary_input.CreateGlossaryInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_glossary_input

            return capo_datazone.types.create_glossary_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_glossary_output.CreateGlossaryOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_glossary_output

            return capo_datazone.types.create_glossary_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateGlossary",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.create_glossary_input.CreateGlossaryInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "owning_project_identifier": owning_project_identifier,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if usage_restrictions is not None:
            input_["usage_restrictions"] = usage_restrictions
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_glossary_output.GetGlossaryOutput":
        """<p>Gets a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The specified glossary ID must exist and be associated with the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:GetGlossary</code> permission on the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary exists.</p>
            identifier: <p>The ID of the business glossary.</p>

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
            req: "OperationRequest[capo_datazone.types.get_glossary_input.GetGlossaryInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_glossary_output.GetGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.get_glossary

            output, http_response = (
                capo_datazone._operations.data_zone.get_glossary.get_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_glossary_output.GetGlossaryOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_glossary_output

            return capo_datazone.types.get_glossary_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetGlossary", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_glossary_input.GetGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.glossary_name.GlossaryName"] = None,
        description: Optional[
            "capo_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional["capo_datazone.types.glossary_status.GlossaryStatus"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput":
        """<p>Updates the business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must exist in the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:UpdateGlossary</code> permission to update it.</p> </li> <li> <p>When updating the name, the new name must be unique within the domain.</p> </li> <li> <p>The glossary must not be deleted or in a terminal state.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>
            identifier: <p>The identifier of the business glossary to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

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
            req: "OperationRequest[capo_datazone.types.update_glossary_input.UpdateGlossaryInput]",
        ) -> OperationResponse[
            "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.update_glossary

            output, http_response = (
                capo_datazone._operations.data_zone.update_glossary.update_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.update_glossary_input.UpdateGlossaryInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_glossary_input

            return capo_datazone.types.update_glossary_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_glossary_output

            return capo_datazone.types.update_glossary_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateGlossary",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.update_glossary_input.UpdateGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_glossary_output.DeleteGlossaryOutput":
        """<p>Deletes a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must be in DISABLED state. </p> </li> <li> <p>The glossary must not have any glossary terms associated with it.</p> </li> <li> <p>The glossary must exist in the specified domain.</p> </li> <li> <p>The caller must have the <code>datazone:DeleteGlossary</code> permission in the domain and glossary.</p> </li> <li> <p>Glossary should not be linked to any active metadata forms.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary is deleted.</p>
            identifier: <p>The ID of the business glossary that is deleted.</p>

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
            req: "OperationRequest[capo_datazone.types.delete_glossary_input.DeleteGlossaryInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_glossary_output.DeleteGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_glossary

            output, http_response = (
                capo_datazone._operations.data_zone.delete_glossary.delete_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGlossary")
        )
        input_: capo_datazone.types.delete_glossary_input.DeleteGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGlossary:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.glossary_name.GlossaryName",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "capo_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional["capo_datazone.types.glossary_status.GlossaryStatus"] = None,
        usage_restrictions: Optional[
            "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_glossary_output.CreateGlossaryOutput":
        """<p>Creates an Amazon DataZone business glossary.</p> <p>Specifies that this is a create glossary policy.</p> <p>A glossary serves as the central repository for business terminology and definitions within an organization. It helps establish and maintain a common language across different departments and teams, reducing miscommunication and ensuring consistent interpretation of business concepts. Glossaries can include hierarchical relationships between terms, cross-references, and links to actual data assets, making them invaluable for both business users and technical teams trying to understand and use data correctly.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist and be in an active state. </p> </li> <li> <p>Owning project must exist and be accessible by the caller.</p> </li> <li> <p>The glossary name must be unique within the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>
            name: <p>The name of this business glossary.</p>
            owning_project_identifier: <p>The ID of the project that currently owns business glossary.</p>
            description: <p>The description of this business glossary.</p>
            status: <p>The status of this business glossary.</p>
            usage_restrictions: <p>The usage restriction of the restricted glossary.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.create_glossary_input.CreateGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_glossary_output.CreateGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.create_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_glossary.async_create_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.create_glossary_input.CreateGlossaryInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_glossary_input

            return capo_datazone.types.create_glossary_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.create_glossary_output.CreateGlossaryOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.create_glossary_output

            return capo_datazone.types.create_glossary_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateGlossary",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.create_glossary_input.CreateGlossaryInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "owning_project_identifier": owning_project_identifier,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if usage_restrictions is not None:
            input_["usage_restrictions"] = usage_restrictions
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_glossary_output.GetGlossaryOutput":
        """<p>Gets a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The specified glossary ID must exist and be associated with the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:GetGlossary</code> permission on the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary exists.</p>
            identifier: <p>The ID of the business glossary.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.get_glossary_input.GetGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_glossary_output.GetGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.get_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_glossary.async_get_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_glossary_output.GetGlossaryOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_glossary_output

            return capo_datazone.types.get_glossary_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetGlossary", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_glossary_input.GetGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.glossary_name.GlossaryName"] = None,
        description: Optional[
            "capo_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional["capo_datazone.types.glossary_status.GlossaryStatus"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput":
        """<p>Updates the business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must exist in the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:UpdateGlossary</code> permission to update it.</p> </li> <li> <p>When updating the name, the new name must be unique within the domain.</p> </li> <li> <p>The glossary must not be deleted or in a terminal state.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>
            identifier: <p>The identifier of the business glossary to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.update_glossary_input.UpdateGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.update_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_glossary.async_update_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_datazone.types.update_glossary_input.UpdateGlossaryInput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_glossary_input

            return capo_datazone.types.update_glossary_input.redact_sensitive(input_)

        def _redact_output(
            output: "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.update_glossary_output

            return capo_datazone.types.update_glossary_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateGlossary",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_datazone.types.update_glossary_input.UpdateGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_glossary_output.DeleteGlossaryOutput":
        """<p>Deletes a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must be in DISABLED state. </p> </li> <li> <p>The glossary must not have any glossary terms associated with it.</p> </li> <li> <p>The glossary must exist in the specified domain.</p> </li> <li> <p>The caller must have the <code>datazone:DeleteGlossary</code> permission in the domain and glossary.</p> </li> <li> <p>Glossary should not be linked to any active metadata forms.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary is deleted.</p>
            identifier: <p>The ID of the business glossary that is deleted.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.delete_glossary_input.DeleteGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_glossary_output.DeleteGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_glossary.async_delete_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGlossary")
        )
        input_: capo_datazone.types.delete_glossary_input.DeleteGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

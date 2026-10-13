from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

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
    import capo_datazone.types.cancel_metadata_generation_run_input
    import capo_datazone.types.cancel_metadata_generation_run_output
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_id
    import capo_datazone.types.get_metadata_generation_run_input
    import capo_datazone.types.get_metadata_generation_run_output
    import capo_datazone.types.list_metadata_generation_runs_input
    import capo_datazone.types.list_metadata_generation_runs_output
    import capo_datazone.types.max_results
    import capo_datazone.types.metadata_generation_run_identifier
    import capo_datazone.types.metadata_generation_run_item
    import capo_datazone.types.metadata_generation_run_status
    import capo_datazone.types.metadata_generation_run_target
    import capo_datazone.types.metadata_generation_run_type
    import capo_datazone.types.metadata_generation_run_types
    import capo_datazone.types.pagination_token
    import capo_datazone.types.project_id
    import capo_datazone.types.start_metadata_generation_run_input
    import capo_datazone.types.start_metadata_generation_run_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class MetadataGenerationRun:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        target: "capo_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        types: Optional[
            "capo_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput":
        """<p>Starts the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must be created and belong to the specified domain and project. </p> </li> <li> <p>Asset type must be supported for metadata generation (e.g., Amazon Web Services Glue table).</p> </li> <li> <p>Asset must have a structured schema with valid rows and columns.</p> </li> <li> <p>Valid values for --type: BUSINESS_DESCRIPTIONS, BUSINESS_NAMES, BUSINESS_GLOSSARY_ASSOCIATIONS.</p> </li> <li> <p>The user must have permission to run metadata generation in the domain/project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to start a metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>
            types: <p>The types of the metadata generation run.</p>
            target: <p>The asset for which you want to start a metadata generation run.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
            owning_project_identifier: <p>The ID of the project that owns the asset for which you want to start a metadata generation run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_metadata_generation_run

            output, http_response = (
                capo_datazone._operations.data_zone.start_metadata_generation_run.start_metadata_generation_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartMetadataGenerationRun")
        )
        input_: capo_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput = {
            "domain_identifier": domain_identifier,
            "target": target,
            "owning_project_identifier": owning_project_identifier,
        }
        if type is not None:
            input_["type"] = type
        if types is not None:
            input_["types"] = types
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
        identifier: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
    ) -> "capo_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput":
        """<p>Gets a metadata generation run in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain and run identifier. </p> </li> <li> <p>The metadata generation run must exist.</p> </li> <li> <p>User must have read access to the metadata run.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>
            identifier: <p>The identifier of the metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>

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
            req: "OperationRequest[capo_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_metadata_generation_run

            output, http_response = (
                capo_datazone._operations.data_zone.get_metadata_generation_run.get_metadata_generation_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMetadataGenerationRun")
        )
        input_: capo_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if type is not None:
            input_["type"] = type

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
        identifier: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput":
        """<p>Cancels the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>The run must exist and be in a cancelable status (e.g., SUBMITTED, IN_PROGRESS). </p> </li> <li> <p>Runs in SUCCEEDED status cannot be cancelled.</p> </li> <li> <p>User must have access to the run and cancel permissions.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata generation run is to be cancelled.</p>
            identifier: <p>The ID of the metadata generation run.</p>

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
            req: "OperationRequest[capo_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.cancel_metadata_generation_run

            output, http_response = (
                capo_datazone._operations.data_zone.cancel_metadata_generation_run.cancel_metadata_generation_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelMetadataGenerationRun")
        )
        input_: capo_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput = {
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

    def list(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
        ] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        target_identifier: Optional["capo_datazone.types.entity_id.EntityId"] = None,
    ) -> "capo_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput":
        """<p>Lists all metadata generation runs.</p> <p>Metadata generation runs represent automated processes that leverage AI/ML capabilities to create or enhance asset metadata at scale. This feature helps organizations maintain comprehensive and consistent metadata across large numbers of assets without manual intervention. It can automatically generate business descriptions, tags, and other metadata elements, significantly reducing the time and effort required for metadata management while improving consistency and completeness.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain identifier. </p> </li> <li> <p>User must have access to metadata generation runs in the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to list metadata generation runs.</p>
            status: <p>The status of the metadata generation runs.</p>
            type: <p>The type of the metadata generation runs.</p>
            next_token: <p>When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            max_results: <p>The maximum number of metadata generation runs to return in a single call to ListMetadataGenerationRuns. When the number of metadata generation runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            target_identifier: <p>The target ID for which you want to list metadata generation runs.</p>

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
            req: "OperationRequest[capo_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput]",
        ) -> OperationResponse[
            "capo_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_metadata_generation_runs

            output, http_response = (
                capo_datazone._operations.data_zone.list_metadata_generation_runs.list_metadata_generation_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMetadataGenerationRuns")
        )
        input_: capo_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput = {
            "domain_identifier": domain_identifier
        }
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMetadataGenerationRun:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        target: "capo_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        types: Optional[
            "capo_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput":
        """<p>Starts the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must be created and belong to the specified domain and project. </p> </li> <li> <p>Asset type must be supported for metadata generation (e.g., Amazon Web Services Glue table).</p> </li> <li> <p>Asset must have a structured schema with valid rows and columns.</p> </li> <li> <p>Valid values for --type: BUSINESS_DESCRIPTIONS, BUSINESS_NAMES, BUSINESS_GLOSSARY_ASSOCIATIONS.</p> </li> <li> <p>The user must have permission to run metadata generation in the domain/project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to start a metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>
            types: <p>The types of the metadata generation run.</p>
            target: <p>The asset for which you want to start a metadata generation run.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
            owning_project_identifier: <p>The ID of the project that owns the asset for which you want to start a metadata generation run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_metadata_generation_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_metadata_generation_run.async_start_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartMetadataGenerationRun")
        )
        input_: capo_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput = {
            "domain_identifier": domain_identifier,
            "target": target,
            "owning_project_identifier": owning_project_identifier,
        }
        if type is not None:
            input_["type"] = type
        if types is not None:
            input_["types"] = types
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
        identifier: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
    ) -> "capo_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput":
        """<p>Gets a metadata generation run in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain and run identifier. </p> </li> <li> <p>The metadata generation run must exist.</p> </li> <li> <p>User must have read access to the metadata run.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>
            identifier: <p>The identifier of the metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_metadata_generation_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_metadata_generation_run.async_get_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMetadataGenerationRun")
        )
        input_: capo_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if type is not None:
            input_["type"] = type

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
        identifier: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput":
        """<p>Cancels the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>The run must exist and be in a cancelable status (e.g., SUBMITTED, IN_PROGRESS). </p> </li> <li> <p>Runs in SUCCEEDED status cannot be cancelled.</p> </li> <li> <p>User must have access to the run and cancel permissions.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata generation run is to be cancelled.</p>
            identifier: <p>The ID of the metadata generation run.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.cancel_metadata_generation_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.cancel_metadata_generation_run.async_cancel_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelMetadataGenerationRun")
        )
        input_: capo_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput = {
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

    async def list(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
        ] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        target_identifier: Optional["capo_datazone.types.entity_id.EntityId"] = None,
    ) -> "capo_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput":
        """<p>Lists all metadata generation runs.</p> <p>Metadata generation runs represent automated processes that leverage AI/ML capabilities to create or enhance asset metadata at scale. This feature helps organizations maintain comprehensive and consistent metadata across large numbers of assets without manual intervention. It can automatically generate business descriptions, tags, and other metadata elements, significantly reducing the time and effort required for metadata management while improving consistency and completeness.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain identifier. </p> </li> <li> <p>User must have access to metadata generation runs in the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to list metadata generation runs.</p>
            status: <p>The status of the metadata generation runs.</p>
            type: <p>The type of the metadata generation runs.</p>
            next_token: <p>When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            max_results: <p>The maximum number of metadata generation runs to return in a single call to ListMetadataGenerationRuns. When the number of metadata generation runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            target_identifier: <p>The target ID for which you want to list metadata generation runs.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_metadata_generation_runs

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_metadata_generation_runs.async_list_metadata_generation_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMetadataGenerationRuns")
        )
        input_: capo_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput = {
            "domain_identifier": domain_identifier
        }
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

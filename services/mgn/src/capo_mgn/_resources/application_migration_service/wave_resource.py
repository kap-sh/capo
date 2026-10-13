from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_i_ds
    import capo_mgn.types.archive_wave_request
    import capo_mgn.types.associate_applications_request
    import capo_mgn.types.associate_applications_response
    import capo_mgn.types.create_wave_request
    import capo_mgn.types.delete_wave_request
    import capo_mgn.types.delete_wave_response
    import capo_mgn.types.disassociate_applications_request
    import capo_mgn.types.disassociate_applications_response
    import capo_mgn.types.list_waves_request
    import capo_mgn.types.list_waves_request_filters
    import capo_mgn.types.list_waves_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.tags_map
    import capo_mgn.types.unarchive_wave_request
    import capo_mgn.types.update_wave_request
    import capo_mgn.types.wave
    import capo_mgn.types.wave_description
    import capo_mgn.types.wave_id
    import capo_mgn.types.wave_name
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class WaveResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_mgn.types.wave_name.WaveName",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional["capo_mgn.types.wave_description.WaveDescription"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Create wave.</p>

        Args:
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            tags: <p>Wave tags.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_wave_request.CreateWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.create_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_wave.create_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_wave_request.CreateWaveRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_wave_request

            return capo_mgn.types.create_wave_request.redact_sensitive(input_)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateWave", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.create_wave_request.CreateWaveRequest = {"name": name}
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_wave_response.DeleteWaveResponse":
        """<p>Delete wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_wave_request.DeleteWaveRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_wave_response.DeleteWaveResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_wave.delete_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWave")
        )
        input_: capo_mgn.types.delete_wave_request.DeleteWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_waves_request_filters.ListWavesRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_waves_response.ListWavesResponse":
        """<p>Retrieves all waves or multiple waves by ID.</p>

        Args:
            filters: <p>Waves list filters.</p>
            max_results: <p>Maximum results to return when listing waves.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Request account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_waves_request.ListWavesRequest]",
        ) -> OperationResponse["capo_mgn.types.list_waves_response.ListWavesResponse"]:
            import capo_mgn._operations.application_migration_service.list_waves

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_waves.list_waves(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_waves_response.ListWavesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_waves_response

            return capo_mgn.types.list_waves_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListWaves", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_waves_request.ListWavesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def archive_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Archive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.archive_wave_request.ArchiveWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.archive_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.archive_wave.archive_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ArchiveWave", redact_output=_redact_output),
        )
        input_: capo_mgn.types.archive_wave_request.ArchiveWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_applications(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        application_i_ds: "capo_mgn.types.application_i_ds.ApplicationIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.associate_applications_response.AssociateApplicationsResponse":
        """<p>Associate applications to wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.associate_applications_request.AssociateApplicationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.associate_applications_response.AssociateApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.associate_applications

            output, http_response = (
                capo_mgn._operations.application_migration_service.associate_applications.associate_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateApplications")
        )
        input_: capo_mgn.types.associate_applications_request.AssociateApplicationsRequest = {
            "wave_id": wave_id,
            "application_i_ds": application_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_applications(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        application_i_ds: "capo_mgn.types.application_i_ds.ApplicationIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse":
        """<p>Disassociate applications from wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.disassociate_applications

            output, http_response = (
                capo_mgn._operations.application_migration_service.disassociate_applications.disassociate_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateApplications")
        )
        input_: capo_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest = {
            "wave_id": wave_id,
            "application_i_ds": application_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def unarchive_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Unarchive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.unarchive_wave_request.UnarchiveWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.unarchive_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.unarchive_wave.unarchive_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UnarchiveWave", redact_output=_redact_output),
        )
        input_: capo_mgn.types.unarchive_wave_request.UnarchiveWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.wave_name.WaveName"] = None,
        description: Optional["capo_mgn.types.wave_description.WaveDescription"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Update wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_wave_request.UpdateWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.update_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_wave.update_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateWave", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_wave_request.UpdateWaveRequest = {
            "wave_id": wave_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWaveResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_mgn.types.wave_name.WaveName",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        description: Optional["capo_mgn.types.wave_description.WaveDescription"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Create wave.</p>

        Args:
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            tags: <p>Wave tags.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.create_wave_request.CreateWaveRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.create_wave

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.create_wave.async_create_wave(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_wave_request.CreateWaveRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_wave_request

            return capo_mgn.types.create_wave_request.redact_sensitive(input_)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateWave", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.create_wave_request.CreateWaveRequest = {"name": name}
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_wave_response.DeleteWaveResponse":
        """<p>Delete wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_wave_request.DeleteWaveRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.delete_wave_response.DeleteWaveResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_wave

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_wave.async_delete_wave(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWave")
        )
        input_: capo_mgn.types.delete_wave_request.DeleteWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_waves_request_filters.ListWavesRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_waves_response.ListWavesResponse":
        """<p>Retrieves all waves or multiple waves by ID.</p>

        Args:
            filters: <p>Waves list filters.</p>
            max_results: <p>Maximum results to return when listing waves.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Request account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_waves_request.ListWavesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_waves_response.ListWavesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_waves

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_waves.async_list_waves(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_waves_response.ListWavesResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_waves_response

            return capo_mgn.types.list_waves_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListWaves", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_waves_request.ListWavesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def archive_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Archive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.archive_wave_request.ArchiveWaveRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.archive_wave

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.archive_wave.async_archive_wave(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ArchiveWave", redact_output=_redact_output),
        )
        input_: capo_mgn.types.archive_wave_request.ArchiveWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_applications(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        application_i_ds: "capo_mgn.types.application_i_ds.ApplicationIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.associate_applications_response.AssociateApplicationsResponse":
        """<p>Associate applications to wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.associate_applications_request.AssociateApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.associate_applications_response.AssociateApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.associate_applications

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.associate_applications.async_associate_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateApplications")
        )
        input_: capo_mgn.types.associate_applications_request.AssociateApplicationsRequest = {
            "wave_id": wave_id,
            "application_i_ds": application_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_applications(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        application_i_ds: "capo_mgn.types.application_i_ds.ApplicationIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse":
        """<p>Disassociate applications from wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.disassociate_applications

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.disassociate_applications.async_disassociate_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateApplications")
        )
        input_: capo_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest = {
            "wave_id": wave_id,
            "application_i_ds": application_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unarchive_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Unarchive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.unarchive_wave_request.UnarchiveWaveRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.unarchive_wave

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.unarchive_wave.async_unarchive_wave(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UnarchiveWave", redact_output=_redact_output),
        )
        input_: capo_mgn.types.unarchive_wave_request.UnarchiveWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional["capo_mgn.types.wave_name.WaveName"] = None,
        description: Optional["capo_mgn.types.wave_description.WaveDescription"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Update wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_wave_request.UpdateWaveRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.update_wave

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_wave.async_update_wave(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(output: "capo_mgn.types.wave.Wave") -> dict[str, Any]:
            import capo_mgn.types.wave

            return capo_mgn.types.wave.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateWave", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_wave_request.UpdateWaveRequest = {
            "wave_id": wave_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

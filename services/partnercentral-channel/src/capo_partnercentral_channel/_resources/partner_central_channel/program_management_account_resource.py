from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_partnercentral_channel._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.account_id_list
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.create_program_management_account_request
    import capo_partnercentral_channel.types.create_program_management_account_response
    import capo_partnercentral_channel.types.delete_program_management_account_request
    import capo_partnercentral_channel.types.delete_program_management_account_response
    import capo_partnercentral_channel.types.list_program_management_accounts_request
    import capo_partnercentral_channel.types.list_program_management_accounts_response
    import capo_partnercentral_channel.types.list_program_management_accounts_sort_base
    import capo_partnercentral_channel.types.next_token
    import capo_partnercentral_channel.types.program
    import capo_partnercentral_channel.types.program_list
    import capo_partnercentral_channel.types.program_management_account_display_name
    import capo_partnercentral_channel.types.program_management_account_display_name_list
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.program_management_account_status_list
    import capo_partnercentral_channel.types.program_management_account_summary
    import capo_partnercentral_channel.types.revision
    import capo_partnercentral_channel.types.tag_list
    import capo_partnercentral_channel.types.update_program_management_account_request
    import capo_partnercentral_channel.types.update_program_management_account_response
    from capo_partnercentral_channel._services.async_partner_central_channel import (
        AsyncPartnerCentralChannelClient,
        AsyncPartnerCentralChannelClientConfig,
    )
    from capo_partnercentral_channel._services.partner_central_channel import (
        PartnerCentralChannelClient,
        PartnerCentralChannelClientConfig,
    )


class ProgramManagementAccountResource:
    def __init__(self, service: PartnerCentralChannelClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        program: "capo_partnercentral_channel.types.program.Program",
        display_name: "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName",
        account_id: "capo_partnercentral_channel.types.account_id.AccountId",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse":
        """<p>Creates a new program management account for managing partner relationships.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            program: <p>The program type for the management account.</p>
            display_name: <p>A human-readable name for the program management account.</p>
            account_id: <p>The AWS account ID to associate with the program management account.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the program management account.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateProgramManagementAccount

            >>> client.create(catalog='AWS', program='SOLUTION_PROVIDER', display_name='TestDisplayName', account_id='111122223333', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.create_program_management_account

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.create_program_management_account.create_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateProgramManagementAccount")
        )
        input_: capo_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest = {
            "catalog": catalog,
            "program": program,
            "display_name": display_name,
            "account_id": account_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "capo_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
        ] = None,
    ) -> "capo_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse":
        """<p>Updates the properties of a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to update.</p>
            revision: <p>The current revision number of the program management account.</p>
            display_name: <p>The new display name for the program management account.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateProgramManagementAccount

            >>> client.update(catalog='AWS', identifier='pma-u8ic702rtzng8', revision='3', display_name='TestDisplayName')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.update_program_management_account

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.update_program_management_account.update_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateProgramManagementAccount")
        )
        input_: capo_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse":
        """<p>Deletes a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for DeleteProgramManagementAccount

            >>> client.delete(catalog='AWS', identifier='pma-u8ic702rtzng8', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.delete_program_management_account

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.delete_program_management_account.delete_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteProgramManagementAccount")
        )
        input_: capo_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest = {
            "catalog": catalog,
            "identifier": identifier,
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

    def list(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.program_management_account_display_name_list.ProgramManagementAccountDisplayNameList"
        ] = None,
        programs: Optional[
            "capo_partnercentral_channel.types.program_list.ProgramList"
        ] = None,
        account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        statuses: Optional[
            "capo_partnercentral_channel.types.program_management_account_status_list.ProgramManagementAccountStatusList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_program_management_accounts_sort_base.ListProgramManagementAccountsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse":
        """<p>Lists program management accounts based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter accounts.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            display_names: <p>Filter by display names.</p>
            programs: <p>Filter by program types.</p>
            account_ids: <p>Filter by AWS account IDs.</p>
            statuses: <p>Filter by program management account statuses.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListProgramManagementAccounts

            >>> client.list(catalog='AWS', max_results=20, programs=['SOLUTION_PROVIDER'], display_names=['TestDisplayName'], account_ids=['111122223333'], statuses=['PENDING'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'})
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts.list_program_management_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListProgramManagementAccounts")
        )
        input_: capo_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if display_names is not None:
            input_["display_names"] = display_names
        if programs is not None:
            input_["programs"] = programs
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if statuses is not None:
            input_["statuses"] = statuses
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncProgramManagementAccountResource:
    def __init__(self, service: AsyncPartnerCentralChannelClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        program: "capo_partnercentral_channel.types.program.Program",
        display_name: "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName",
        account_id: "capo_partnercentral_channel.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse":
        """<p>Creates a new program management account for managing partner relationships.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            program: <p>The program type for the management account.</p>
            display_name: <p>A human-readable name for the program management account.</p>
            account_id: <p>The AWS account ID to associate with the program management account.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the program management account.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateProgramManagementAccount

            >>> await client.create(catalog='AWS', program='SOLUTION_PROVIDER', display_name='TestDisplayName', account_id='111122223333', client_token='clientToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.create_program_management_account

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.create_program_management_account.async_create_program_management_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateProgramManagementAccount")
        )
        input_: capo_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest = {
            "catalog": catalog,
            "program": program,
            "display_name": display_name,
            "account_id": account_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "capo_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
        ] = None,
    ) -> "capo_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse":
        """<p>Updates the properties of a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to update.</p>
            revision: <p>The current revision number of the program management account.</p>
            display_name: <p>The new display name for the program management account.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateProgramManagementAccount

            >>> await client.update(catalog='AWS', identifier='pma-u8ic702rtzng8', revision='3', display_name='TestDisplayName')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.update_program_management_account

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.update_program_management_account.async_update_program_management_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateProgramManagementAccount")
        )
        input_: capo_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse":
        """<p>Deletes a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for DeleteProgramManagementAccount

            >>> await client.delete(catalog='AWS', identifier='pma-u8ic702rtzng8', client_token='clientToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.delete_program_management_account

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.delete_program_management_account.async_delete_program_management_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteProgramManagementAccount")
        )
        input_: capo_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest = {
            "catalog": catalog,
            "identifier": identifier,
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

    async def list(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.program_management_account_display_name_list.ProgramManagementAccountDisplayNameList"
        ] = None,
        programs: Optional[
            "capo_partnercentral_channel.types.program_list.ProgramList"
        ] = None,
        account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        statuses: Optional[
            "capo_partnercentral_channel.types.program_management_account_status_list.ProgramManagementAccountStatusList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_program_management_accounts_sort_base.ListProgramManagementAccountsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse":
        """<p>Lists program management accounts based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter accounts.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            display_names: <p>Filter by display names.</p>
            programs: <p>Filter by program types.</p>
            account_ids: <p>Filter by AWS account IDs.</p>
            statuses: <p>Filter by program management account statuses.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListProgramManagementAccounts

            >>> await client.list(catalog='AWS', max_results=20, programs=['SOLUTION_PROVIDER'], display_names=['TestDisplayName'], account_ids=['111122223333'], statuses=['PENDING'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts

            (
                output,
                http_response,
            ) = await capo_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts.async_list_program_management_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListProgramManagementAccounts")
        )
        input_: capo_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if display_names is not None:
            input_["display_names"] = display_names
        if programs is not None:
            input_["programs"] = programs
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if statuses is not None:
            input_["statuses"] = statuses
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

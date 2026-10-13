from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_securityagent._auth._signers
import capo_securityagent._auth._sigv4
from capo_securityagent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_securityagent.types.create_security_requirement_pack_input
    import capo_securityagent.types.create_security_requirement_pack_output
    import capo_securityagent.types.delete_security_requirement_pack_input
    import capo_securityagent.types.delete_security_requirement_pack_output
    import capo_securityagent.types.get_security_requirement_pack_input
    import capo_securityagent.types.get_security_requirement_pack_output
    import capo_securityagent.types.kms_key_id
    import capo_securityagent.types.list_security_requirement_pack_filter
    import capo_securityagent.types.list_security_requirement_packs_input
    import capo_securityagent.types.list_security_requirement_packs_output
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token
    import capo_securityagent.types.security_requirement_pack_id
    import capo_securityagent.types.security_requirement_pack_name
    import capo_securityagent.types.security_requirement_pack_status
    import capo_securityagent.types.security_requirement_pack_summary
    import capo_securityagent.types.tag_map
    import capo_securityagent.types.update_security_requirement_pack_input
    import capo_securityagent.types.update_security_requirement_pack_output
    from capo_securityagent._services.async_security_agent import (
        AsyncSecurityAgentClient,
        AsyncSecurityAgentClientConfig,
    )
    from capo_securityagent._services.security_agent import (
        SecurityAgentClient,
        SecurityAgentClientConfig,
    )


class SecurityRequirementPackResource:
    def __init__(self, service: SecurityAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        description: Optional[str] = None,
        status: Optional[
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
        ] = None,
        kms_key_id: Optional["capo_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> "capo_securityagent.types.create_security_requirement_pack_output.CreateSecurityRequirementPackOutput":
        """<p>Creates a customer managed security requirement pack.</p>

        Args:
            name: <p>The name of the security requirement pack.</p>
            description: <p>A description of the security requirement pack.</p>
            status: <p>The status of the pack. Defaults to ENABLED if not provided.</p>
            kms_key_id: <p>The identifier of the AWS KMS key used to encrypt pack contents.</p>
            tags: <p>The tags to associate with the security requirement pack.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota. Review your current usage and request a quota increase if needed.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.create_security_requirement_pack_input.CreateSecurityRequirementPackInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.create_security_requirement_pack_output.CreateSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_security_requirement_pack

            output, http_response = (
                capo_securityagent._operations.security_agent.create_security_requirement_pack.create_security_requirement_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateSecurityRequirementPack")
        )
        input_: capo_securityagent.types.create_security_requirement_pack_input.CreateSecurityRequirementPackInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_security_requirement_pack_output.GetSecurityRequirementPackOutput":
        """<p>Retrieves information about a security requirement pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.get_security_requirement_pack_input.GetSecurityRequirementPackInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.get_security_requirement_pack_output.GetSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.get_security_requirement_pack

            output, http_response = (
                capo_securityagent._operations.security_agent.get_security_requirement_pack.get_security_requirement_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSecurityRequirementPack")
        )
        input_: capo_securityagent.types.get_security_requirement_pack_input.GetSecurityRequirementPackInput = {
            "pack_id": pack_id
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
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        name: Optional[
            "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName"
        ] = None,
        description: Optional[str] = None,
        status: Optional[
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
        ] = None,
    ) -> "capo_securityagent.types.update_security_requirement_pack_output.UpdateSecurityRequirementPackOutput":
        """<p>Updates a security requirement pack. For customer managed packs, both metadata and status can be updated. For AWS managed packs, only status can be updated.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to update.</p>
            name: <p>The updated name of the security requirement pack.</p>
            description: <p>The updated description of the security requirement pack.</p>
            status: <p>The updated status of the security requirement pack.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.update_security_requirement_pack_input.UpdateSecurityRequirementPackInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.update_security_requirement_pack_output.UpdateSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_security_requirement_pack

            output, http_response = (
                capo_securityagent._operations.security_agent.update_security_requirement_pack.update_security_requirement_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSecurityRequirementPack")
        )
        input_: capo_securityagent.types.update_security_requirement_pack_input.UpdateSecurityRequirementPackInput = {
            "pack_id": pack_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_security_requirement_pack_output.DeleteSecurityRequirementPackOutput":
        """<p>Deletes a customer managed security requirement pack and all its associated security requirements.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.delete_security_requirement_pack_input.DeleteSecurityRequirementPackInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.delete_security_requirement_pack_output.DeleteSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_security_requirement_pack

            output, http_response = (
                capo_securityagent._operations.security_agent.delete_security_requirement_pack.delete_security_requirement_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSecurityRequirementPack")
        )
        input_: capo_securityagent.types.delete_security_requirement_pack_input.DeleteSecurityRequirementPackInput = {
            "pack_id": pack_id
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
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.list_security_requirement_pack_filter.ListSecurityRequirementPackFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_security_requirement_packs_output.ListSecurityRequirementPacksOutput":
        """<p>Lists all security requirement packs in the caller's account.</p>

        Args:
            filter: <p>The filter criteria for listing security requirement packs.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single request.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.list_security_requirement_packs_input.ListSecurityRequirementPacksInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.list_security_requirement_packs_output.ListSecurityRequirementPacksOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_security_requirement_packs

            output, http_response = (
                capo_securityagent._operations.security_agent.list_security_requirement_packs.list_security_requirement_packs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSecurityRequirementPacks")
        )
        input_: capo_securityagent.types.list_security_requirement_packs_input.ListSecurityRequirementPacksInput = {}
        if filter is not None:
            input_["filter"] = filter
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


class AsyncSecurityRequirementPackResource:
    def __init__(self, service: AsyncSecurityAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        description: Optional[str] = None,
        status: Optional[
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
        ] = None,
        kms_key_id: Optional["capo_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> "capo_securityagent.types.create_security_requirement_pack_output.CreateSecurityRequirementPackOutput":
        """<p>Creates a customer managed security requirement pack.</p>

        Args:
            name: <p>The name of the security requirement pack.</p>
            description: <p>A description of the security requirement pack.</p>
            status: <p>The status of the pack. Defaults to ENABLED if not provided.</p>
            kms_key_id: <p>The identifier of the AWS KMS key used to encrypt pack contents.</p>
            tags: <p>The tags to associate with the security requirement pack.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota. Review your current usage and request a quota increase if needed.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_security_requirement_pack_input.CreateSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_security_requirement_pack_output.CreateSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_security_requirement_pack.async_create_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateSecurityRequirementPack")
        )
        input_: capo_securityagent.types.create_security_requirement_pack_input.CreateSecurityRequirementPackInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_security_requirement_pack_output.GetSecurityRequirementPackOutput":
        """<p>Retrieves information about a security requirement pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.get_security_requirement_pack_input.GetSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.get_security_requirement_pack_output.GetSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.get_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.get_security_requirement_pack.async_get_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSecurityRequirementPack")
        )
        input_: capo_securityagent.types.get_security_requirement_pack_input.GetSecurityRequirementPackInput = {
            "pack_id": pack_id
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
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        name: Optional[
            "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName"
        ] = None,
        description: Optional[str] = None,
        status: Optional[
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
        ] = None,
    ) -> "capo_securityagent.types.update_security_requirement_pack_output.UpdateSecurityRequirementPackOutput":
        """<p>Updates a security requirement pack. For customer managed packs, both metadata and status can be updated. For AWS managed packs, only status can be updated.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to update.</p>
            name: <p>The updated name of the security requirement pack.</p>
            description: <p>The updated description of the security requirement pack.</p>
            status: <p>The updated status of the security requirement pack.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_security_requirement_pack_input.UpdateSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_security_requirement_pack_output.UpdateSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_security_requirement_pack.async_update_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSecurityRequirementPack")
        )
        input_: capo_securityagent.types.update_security_requirement_pack_input.UpdateSecurityRequirementPackInput = {
            "pack_id": pack_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_security_requirement_pack_output.DeleteSecurityRequirementPackOutput":
        """<p>Deletes a customer managed security requirement pack and all its associated security requirements.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_security_requirement_pack_input.DeleteSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_security_requirement_pack_output.DeleteSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_security_requirement_pack.async_delete_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSecurityRequirementPack")
        )
        input_: capo_securityagent.types.delete_security_requirement_pack_input.DeleteSecurityRequirementPackInput = {
            "pack_id": pack_id
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
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.list_security_requirement_pack_filter.ListSecurityRequirementPackFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_security_requirement_packs_output.ListSecurityRequirementPacksOutput":
        """<p>Lists all security requirement packs in the caller's account.</p>

        Args:
            filter: <p>The filter criteria for listing security requirement packs.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single request.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_security_requirement_packs_input.ListSecurityRequirementPacksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_security_requirement_packs_output.ListSecurityRequirementPacksOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_security_requirement_packs

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_security_requirement_packs.async_list_security_requirement_packs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSecurityRequirementPacks")
        )
        input_: capo_securityagent.types.list_security_requirement_packs_input.ListSecurityRequirementPacksInput = {}
        if filter is not None:
            input_["filter"] = filter
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

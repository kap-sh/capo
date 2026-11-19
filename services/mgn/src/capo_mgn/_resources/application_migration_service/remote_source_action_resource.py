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
    import capo_mgn.types.create_remote_source_action_request
    import capo_mgn.types.create_remote_source_action_response
    import capo_mgn.types.delete_remote_source_action_request
    import capo_mgn.types.delete_remote_source_action_response
    import capo_mgn.types.list_remote_source_actions_request
    import capo_mgn.types.list_remote_source_actions_request_filters
    import capo_mgn.types.list_remote_source_actions_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.remote_source_action
    import capo_mgn.types.remote_source_action_description
    import capo_mgn.types.remote_source_action_id
    import capo_mgn.types.remote_source_action_name
    import capo_mgn.types.remote_source_action_operating_system
    import capo_mgn.types.remote_source_action_timeout_seconds
    import capo_mgn.types.ssm_parameter_store_parameter_name
    import capo_mgn.types.tags_map
    import capo_mgn.types.update_remote_source_action_request
    import capo_mgn.types.update_remote_source_action_response
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class RemoteSourceActionResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_mgn.types.remote_source_action_name.RemoteSourceActionName",
        ssm_parameter_name: "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional[
            "capo_mgn.types.remote_source_action_description.RemoteSourceActionDescription"
        ] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.remote_source_action_timeout_seconds.RemoteSourceActionTimeoutSeconds"
        ] = None,
        operating_system: Optional[
            "capo_mgn.types.remote_source_action_operating_system.RemoteSourceActionOperatingSystem"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.create_remote_source_action_response.CreateRemoteSourceActionResponse":
        """<p>Creates a source action, which references a script in AWS Systems Manager Parameter Store that Application Migration Service runs on source environment.</p>

        Args:
            name: <p>The name of the source action.</p>
            description: <p>A description of the source action.</p>
            ssm_parameter_name: <p>AWS Systems Manager Parameter Store parameter name.</p>
            timeout_seconds: <p>The maximum time, in seconds, that the script can run on each source server.</p>
            operating_system: <p>The operating system of the source servers that the script runs on. Set to <code>linux</code> or <code>windows</code> to run the script only on source servers with that operating system, or <code>all</code> to run it on both.</p>
            tags: <p>Tags to assign to the source action.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_remote_source_action_request.CreateRemoteSourceActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.create_remote_source_action_response.CreateRemoteSourceActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.create_remote_source_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_remote_source_action.create_remote_source_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_remote_source_action_request.CreateRemoteSourceActionRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_remote_source_action_request

            return capo_mgn.types.create_remote_source_action_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.create_remote_source_action_response.CreateRemoteSourceActionResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_remote_source_action_response

            return capo_mgn.types.create_remote_source_action_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRemoteSourceAction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_remote_source_action_request.CreateRemoteSourceActionRequest = {
            "name": name,
            "ssm_parameter_name": ssm_parameter_name,
        }
        if description is not None:
            input_["description"] = description
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if operating_system is not None:
            input_["operating_system"] = operating_system
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

    def update(
        self,
        remote_source_action_id: "capo_mgn.types.remote_source_action_id.RemoteSourceActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional[
            "capo_mgn.types.remote_source_action_name.RemoteSourceActionName"
        ] = None,
        description: Optional[
            "capo_mgn.types.remote_source_action_description.RemoteSourceActionDescription"
        ] = None,
        ssm_parameter_name: Optional[
            "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName"
        ] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.remote_source_action_timeout_seconds.RemoteSourceActionTimeoutSeconds"
        ] = None,
        operating_system: Optional[
            "capo_mgn.types.remote_source_action_operating_system.RemoteSourceActionOperatingSystem"
        ] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.update_remote_source_action_response.UpdateRemoteSourceActionResponse":
        """<p>Updates a source action.</p>

        Args:
            remote_source_action_id: <p>The unique identifier of the source action to update.</p>
            name: <p>The updated name of the source action.</p>
            description: <p>The updated description of the source action.</p>
            ssm_parameter_name: <p>AWS Systems Manager Parameter Store parameter name.</p>
            timeout_seconds: <p>The updated maximum time, in seconds, that the script can run on each source server.</p>
            operating_system: <p>The updated operating system of the source servers that the script runs on. Set to <code>linux</code> or <code>windows</code> to run the script only on source servers with that operating system, or <code>all</code> to run it on both.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_remote_source_action_request.UpdateRemoteSourceActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.update_remote_source_action_response.UpdateRemoteSourceActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.update_remote_source_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_remote_source_action.update_remote_source_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.update_remote_source_action_response.UpdateRemoteSourceActionResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.update_remote_source_action_response

            return capo_mgn.types.update_remote_source_action_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateRemoteSourceAction", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_remote_source_action_request.UpdateRemoteSourceActionRequest = {
            "remote_source_action_id": remote_source_action_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if ssm_parameter_name is not None:
            input_["ssm_parameter_name"] = ssm_parameter_name
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if operating_system is not None:
            input_["operating_system"] = operating_system
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
        remote_source_action_id: "capo_mgn.types.remote_source_action_id.RemoteSourceActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_remote_source_action_response.DeleteRemoteSourceActionResponse":
        """<p>Deletes a source action. This operation also deletes the invocation results of the source action.</p>

        Args:
            remote_source_action_id: <p>The unique identifier of the source action to delete.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_remote_source_action_request.DeleteRemoteSourceActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_remote_source_action_response.DeleteRemoteSourceActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_remote_source_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_remote_source_action.delete_remote_source_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRemoteSourceAction")
        )
        input_: capo_mgn.types.delete_remote_source_action_request.DeleteRemoteSourceActionRequest = {
            "remote_source_action_id": remote_source_action_id
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
            "capo_mgn.types.list_remote_source_actions_request_filters.ListRemoteSourceActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_remote_source_actions_response.ListRemoteSourceActionsResponse":
        """<p>Lists the source actions in the account, with optional filtering.</p>

        Args:
            filters: <p>Filters to apply when listing source actions.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_remote_source_actions_request.ListRemoteSourceActionsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_remote_source_actions_response.ListRemoteSourceActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_remote_source_actions

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_remote_source_actions.list_remote_source_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_remote_source_actions_response.ListRemoteSourceActionsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_remote_source_actions_response

            return capo_mgn.types.list_remote_source_actions_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListRemoteSourceActions", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_remote_source_actions_request.ListRemoteSourceActionsRequest = {}
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


class AsyncRemoteSourceActionResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_mgn.types.remote_source_action_name.RemoteSourceActionName",
        ssm_parameter_name: "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        description: Optional[
            "capo_mgn.types.remote_source_action_description.RemoteSourceActionDescription"
        ] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.remote_source_action_timeout_seconds.RemoteSourceActionTimeoutSeconds"
        ] = None,
        operating_system: Optional[
            "capo_mgn.types.remote_source_action_operating_system.RemoteSourceActionOperatingSystem"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.create_remote_source_action_response.CreateRemoteSourceActionResponse":
        """<p>Creates a source action, which references a script in AWS Systems Manager Parameter Store that Application Migration Service runs on source environment.</p>

        Args:
            name: <p>The name of the source action.</p>
            description: <p>A description of the source action.</p>
            ssm_parameter_name: <p>AWS Systems Manager Parameter Store parameter name.</p>
            timeout_seconds: <p>The maximum time, in seconds, that the script can run on each source server.</p>
            operating_system: <p>The operating system of the source servers that the script runs on. Set to <code>linux</code> or <code>windows</code> to run the script only on source servers with that operating system, or <code>all</code> to run it on both.</p>
            tags: <p>Tags to assign to the source action.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.create_remote_source_action_request.CreateRemoteSourceActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.create_remote_source_action_response.CreateRemoteSourceActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.create_remote_source_action

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.create_remote_source_action.async_create_remote_source_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_remote_source_action_request.CreateRemoteSourceActionRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_remote_source_action_request

            return capo_mgn.types.create_remote_source_action_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_mgn.types.create_remote_source_action_response.CreateRemoteSourceActionResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_remote_source_action_response

            return capo_mgn.types.create_remote_source_action_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRemoteSourceAction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_remote_source_action_request.CreateRemoteSourceActionRequest = {
            "name": name,
            "ssm_parameter_name": ssm_parameter_name,
        }
        if description is not None:
            input_["description"] = description
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if operating_system is not None:
            input_["operating_system"] = operating_system
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

    async def update(
        self,
        remote_source_action_id: "capo_mgn.types.remote_source_action_id.RemoteSourceActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional[
            "capo_mgn.types.remote_source_action_name.RemoteSourceActionName"
        ] = None,
        description: Optional[
            "capo_mgn.types.remote_source_action_description.RemoteSourceActionDescription"
        ] = None,
        ssm_parameter_name: Optional[
            "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName"
        ] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.remote_source_action_timeout_seconds.RemoteSourceActionTimeoutSeconds"
        ] = None,
        operating_system: Optional[
            "capo_mgn.types.remote_source_action_operating_system.RemoteSourceActionOperatingSystem"
        ] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.update_remote_source_action_response.UpdateRemoteSourceActionResponse":
        """<p>Updates a source action.</p>

        Args:
            remote_source_action_id: <p>The unique identifier of the source action to update.</p>
            name: <p>The updated name of the source action.</p>
            description: <p>The updated description of the source action.</p>
            ssm_parameter_name: <p>AWS Systems Manager Parameter Store parameter name.</p>
            timeout_seconds: <p>The updated maximum time, in seconds, that the script can run on each source server.</p>
            operating_system: <p>The updated operating system of the source servers that the script runs on. Set to <code>linux</code> or <code>windows</code> to run the script only on source servers with that operating system, or <code>all</code> to run it on both.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_remote_source_action_request.UpdateRemoteSourceActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.update_remote_source_action_response.UpdateRemoteSourceActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.update_remote_source_action

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_remote_source_action.async_update_remote_source_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.update_remote_source_action_response.UpdateRemoteSourceActionResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.update_remote_source_action_response

            return capo_mgn.types.update_remote_source_action_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateRemoteSourceAction", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_remote_source_action_request.UpdateRemoteSourceActionRequest = {
            "remote_source_action_id": remote_source_action_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if ssm_parameter_name is not None:
            input_["ssm_parameter_name"] = ssm_parameter_name
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if operating_system is not None:
            input_["operating_system"] = operating_system
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
        remote_source_action_id: "capo_mgn.types.remote_source_action_id.RemoteSourceActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_remote_source_action_response.DeleteRemoteSourceActionResponse":
        """<p>Deletes a source action. This operation also deletes the invocation results of the source action.</p>

        Args:
            remote_source_action_id: <p>The unique identifier of the source action to delete.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_remote_source_action_request.DeleteRemoteSourceActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.delete_remote_source_action_response.DeleteRemoteSourceActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_remote_source_action

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_remote_source_action.async_delete_remote_source_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRemoteSourceAction")
        )
        input_: capo_mgn.types.delete_remote_source_action_request.DeleteRemoteSourceActionRequest = {
            "remote_source_action_id": remote_source_action_id
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
            "capo_mgn.types.list_remote_source_actions_request_filters.ListRemoteSourceActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_remote_source_actions_response.ListRemoteSourceActionsResponse":
        """<p>Lists the source actions in the account, with optional filtering.</p>

        Args:
            filters: <p>Filters to apply when listing source actions.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_remote_source_actions_request.ListRemoteSourceActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_remote_source_actions_response.ListRemoteSourceActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_remote_source_actions

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_remote_source_actions.async_list_remote_source_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_remote_source_actions_response.ListRemoteSourceActionsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_remote_source_actions_response

            return capo_mgn.types.list_remote_source_actions_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListRemoteSourceActions", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_remote_source_actions_request.ListRemoteSourceActionsRequest = {}
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

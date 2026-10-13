from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.create_run_group_request
    import capo_omics.types.create_run_group_response
    import capo_omics.types.delete_run_group_request
    import capo_omics.types.get_run_group_request
    import capo_omics.types.get_run_group_response
    import capo_omics.types.list_run_groups_request
    import capo_omics.types.list_run_groups_response
    import capo_omics.types.run_group_id
    import capo_omics.types.run_group_list_item
    import capo_omics.types.run_group_list_token
    import capo_omics.types.run_group_name
    import capo_omics.types.run_group_request_id
    import capo_omics.types.tag_map
    import capo_omics.types.update_run_group_request
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class RunGroupResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        request_id: "capo_omics.types.run_group_request_id.RunGroupRequestId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        max_cpus: Optional[int] = None,
        max_runs: Optional[int] = None,
        max_duration: Optional[int] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        max_gpus: Optional[int] = None,
    ) -> "capo_omics.types.create_run_group_response.CreateRunGroupResponse":
        """<p>Creates a run group to limit the compute resources for the runs that are added to the group. Returns an ARN, ID, and tags for the run group.</p>

        Args:
            name: <p>A name for the group.</p>
            max_cpus: <p>The maximum number of CPUs that can run concurrently across all active runs in the run group.</p>
            max_runs: <p>The maximum number of runs that can be running at the same time.</p>
            max_duration: <p>The maximum time for each run (in minutes). If a run exceeds the maximum run time, the run fails automatically.</p>
            tags: <p>Tags for the group.</p>
            request_id: <p>To ensure that requests don't run multiple times, specify a unique ID for each request.</p>
            max_gpus: <p>The maximum number of GPUs that can run concurrently across all active runs in the run group.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.create_run_group_request.CreateRunGroupRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_run_group_response.CreateRunGroupResponse"
        ]:
            import capo_omics._operations.omics.create_run_group

            output, http_response = (
                capo_omics._operations.omics.create_run_group.create_run_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRunGroup")
        )
        input_: capo_omics.types.create_run_group_request.CreateRunGroupRequest = {
            "request_id": request_id
        }
        if name is not None:
            input_["name"] = name
        if max_cpus is not None:
            input_["max_cpus"] = max_cpus
        if max_runs is not None:
            input_["max_runs"] = max_runs
        if max_duration is not None:
            input_["max_duration"] = max_duration
        if tags is not None:
            input_["tags"] = tags
        if max_gpus is not None:
            input_["max_gpus"] = max_gpus

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_run_group_response.GetRunGroupResponse":
        """<p>Gets information about a run group and returns its metadata.</p>

        Args:
            id: <p>The group's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_run_group_request.GetRunGroupRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_run_group_response.GetRunGroupResponse"
        ]:
            import capo_omics._operations.omics.get_run_group

            output, http_response = (
                capo_omics._operations.omics.get_run_group.get_run_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRunGroup")
        )
        input_: capo_omics.types.get_run_group_request.GetRunGroupRequest = {"id": id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        max_cpus: Optional[int] = None,
        max_runs: Optional[int] = None,
        max_duration: Optional[int] = None,
        max_gpus: Optional[int] = None,
    ) -> None:
        """<p>Updates the settings of a run group and returns a response with no body if the operation is successful.</p> <p>You can update the following settings with <code>UpdateRunGroup</code>:</p> <ul> <li> <p>Maximum number of CPUs</p> </li> <li> <p>Run time (measured in minutes)</p> </li> <li> <p>Number of GPUs</p> </li> <li> <p>Number of concurrent runs</p> </li> <li> <p>Group name</p> </li> </ul> <p>To confirm that the settings have been successfully updated, use the <code>ListRunGroups</code> or <code>GetRunGroup</code> API operations to verify that the desired changes have been made.</p>

        Args:
            id: <p>The group's ID.</p>
            name: <p>A name for the group.</p>
            max_cpus: <p>The maximum number of CPUs to use.</p>
            max_runs: <p>The maximum number of concurrent runs for the group.</p>
            max_duration: <p>A maximum run time for the group in minutes.</p>
            max_gpus: <p>The maximum GPUs that can be used by a run group.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.update_run_group_request.UpdateRunGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.update_run_group

            output, http_response = (
                capo_omics._operations.omics.update_run_group.update_run_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRunGroup")
        )
        input_: capo_omics.types.update_run_group_request.UpdateRunGroupRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if max_cpus is not None:
            input_["max_cpus"] = max_cpus
        if max_runs is not None:
            input_["max_runs"] = max_runs
        if max_duration is not None:
            input_["max_duration"] = max_duration
        if max_gpus is not None:
            input_["max_gpus"] = max_gpus

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run group and returns a response with no body if the operation is successful.</p> <p>To verify that the run group is deleted:</p> <ul> <li> <p>Use <code>ListRunGroups</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetRunGroup</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The run group's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_run_group_request.DeleteRunGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.delete_run_group

            output, http_response = (
                capo_omics._operations.omics.delete_run_group.delete_run_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRunGroup")
        )
        input_: capo_omics.types.delete_run_group_request.DeleteRunGroupRequest = {
            "id": id
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
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        starting_token: Optional[
            "capo_omics.types.run_group_list_token.RunGroupListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_run_groups_response.ListRunGroupsResponse":
        """<p>Retrieves a list of all run groups and returns the metadata for each run group.</p>

        Args:
            name: <p>The run groups' name.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of run groups to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_run_groups_request.ListRunGroupsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_run_groups_response.ListRunGroupsResponse"
        ]:
            import capo_omics._operations.omics.list_run_groups

            output, http_response = (
                capo_omics._operations.omics.list_run_groups.list_run_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRunGroups")
        )
        input_: capo_omics.types.list_run_groups_request.ListRunGroupsRequest = {}
        if name is not None:
            input_["name"] = name
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRunGroupResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        request_id: "capo_omics.types.run_group_request_id.RunGroupRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        max_cpus: Optional[int] = None,
        max_runs: Optional[int] = None,
        max_duration: Optional[int] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        max_gpus: Optional[int] = None,
    ) -> "capo_omics.types.create_run_group_response.CreateRunGroupResponse":
        """<p>Creates a run group to limit the compute resources for the runs that are added to the group. Returns an ARN, ID, and tags for the run group.</p>

        Args:
            name: <p>A name for the group.</p>
            max_cpus: <p>The maximum number of CPUs that can run concurrently across all active runs in the run group.</p>
            max_runs: <p>The maximum number of runs that can be running at the same time.</p>
            max_duration: <p>The maximum time for each run (in minutes). If a run exceeds the maximum run time, the run fails automatically.</p>
            tags: <p>Tags for the group.</p>
            request_id: <p>To ensure that requests don't run multiple times, specify a unique ID for each request.</p>
            max_gpus: <p>The maximum number of GPUs that can run concurrently across all active runs in the run group.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_run_group_request.CreateRunGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_run_group_response.CreateRunGroupResponse"
        ]:
            import capo_omics._operations.omics.create_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_run_group.async_create_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRunGroup")
        )
        input_: capo_omics.types.create_run_group_request.CreateRunGroupRequest = {
            "request_id": request_id
        }
        if name is not None:
            input_["name"] = name
        if max_cpus is not None:
            input_["max_cpus"] = max_cpus
        if max_runs is not None:
            input_["max_runs"] = max_runs
        if max_duration is not None:
            input_["max_duration"] = max_duration
        if tags is not None:
            input_["tags"] = tags
        if max_gpus is not None:
            input_["max_gpus"] = max_gpus

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_run_group_response.GetRunGroupResponse":
        """<p>Gets information about a run group and returns its metadata.</p>

        Args:
            id: <p>The group's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_run_group_request.GetRunGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_run_group_response.GetRunGroupResponse"
        ]:
            import capo_omics._operations.omics.get_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_run_group.async_get_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRunGroup")
        )
        input_: capo_omics.types.get_run_group_request.GetRunGroupRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        max_cpus: Optional[int] = None,
        max_runs: Optional[int] = None,
        max_duration: Optional[int] = None,
        max_gpus: Optional[int] = None,
    ) -> None:
        """<p>Updates the settings of a run group and returns a response with no body if the operation is successful.</p> <p>You can update the following settings with <code>UpdateRunGroup</code>:</p> <ul> <li> <p>Maximum number of CPUs</p> </li> <li> <p>Run time (measured in minutes)</p> </li> <li> <p>Number of GPUs</p> </li> <li> <p>Number of concurrent runs</p> </li> <li> <p>Group name</p> </li> </ul> <p>To confirm that the settings have been successfully updated, use the <code>ListRunGroups</code> or <code>GetRunGroup</code> API operations to verify that the desired changes have been made.</p>

        Args:
            id: <p>The group's ID.</p>
            name: <p>A name for the group.</p>
            max_cpus: <p>The maximum number of CPUs to use.</p>
            max_runs: <p>The maximum number of concurrent runs for the group.</p>
            max_duration: <p>A maximum run time for the group in minutes.</p>
            max_gpus: <p>The maximum GPUs that can be used by a run group.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_run_group_request.UpdateRunGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.update_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_run_group.async_update_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRunGroup")
        )
        input_: capo_omics.types.update_run_group_request.UpdateRunGroupRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if max_cpus is not None:
            input_["max_cpus"] = max_cpus
        if max_runs is not None:
            input_["max_runs"] = max_runs
        if max_duration is not None:
            input_["max_duration"] = max_duration
        if max_gpus is not None:
            input_["max_gpus"] = max_gpus

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_omics.types.run_group_id.RunGroupId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run group and returns a response with no body if the operation is successful.</p> <p>To verify that the run group is deleted:</p> <ul> <li> <p>Use <code>ListRunGroups</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetRunGroup</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The run group's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_run_group_request.DeleteRunGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_run_group

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_run_group.async_delete_run_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRunGroup")
        )
        input_: capo_omics.types.delete_run_group_request.DeleteRunGroupRequest = {
            "id": id
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
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_group_name.RunGroupName"] = None,
        starting_token: Optional[
            "capo_omics.types.run_group_list_token.RunGroupListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_run_groups_response.ListRunGroupsResponse":
        """<p>Retrieves a list of all run groups and returns the metadata for each run group.</p>

        Args:
            name: <p>The run groups' name.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of run groups to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_run_groups_request.ListRunGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_run_groups_response.ListRunGroupsResponse"
        ]:
            import capo_omics._operations.omics.list_run_groups

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_run_groups.async_list_run_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRunGroups")
        )
        input_: capo_omics.types.list_run_groups_request.ListRunGroupsRequest = {}
        if name is not None:
            input_["name"] = name
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

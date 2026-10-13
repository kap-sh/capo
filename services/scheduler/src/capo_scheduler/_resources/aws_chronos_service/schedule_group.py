from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_scheduler._auth._signers
import capo_scheduler._auth._sigv4
from capo_scheduler._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_scheduler.types.client_token
    import capo_scheduler.types.create_schedule_group_input
    import capo_scheduler.types.create_schedule_group_output
    import capo_scheduler.types.delete_schedule_group_input
    import capo_scheduler.types.delete_schedule_group_output
    import capo_scheduler.types.get_schedule_group_input
    import capo_scheduler.types.get_schedule_group_output
    import capo_scheduler.types.list_schedule_groups_input
    import capo_scheduler.types.list_schedule_groups_output
    import capo_scheduler.types.max_results
    import capo_scheduler.types.next_token
    import capo_scheduler.types.schedule_group_name
    import capo_scheduler.types.schedule_group_name_prefix
    import capo_scheduler.types.schedule_group_summary
    import capo_scheduler.types.tag_list
    from capo_scheduler._services.async_scheduler import (
        AsyncSchedulerClient,
        AsyncSchedulerClientConfig,
    )
    from capo_scheduler._services.scheduler import (
        SchedulerClient,
        SchedulerClientConfig,
    )


class ScheduleGroup:
    def __init__(self, service: SchedulerClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        tags: Optional["capo_scheduler.types.tag_list.TagList"] = None,
        client_token: Optional["capo_scheduler.types.client_token.ClientToken"] = None,
    ) -> "capo_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput":
        """<p>Creates the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group that you are creating.</p>
            tags: <p>The list of tags to associate with the schedule group.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.create_schedule_group

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.create_schedule_group.create_schedule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateScheduleGroup")
        )
        input_: capo_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput = {
            "name": name
        }
        if tags is not None:
            input_["tags"] = tags
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
        name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
    ) -> "capo_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput":
        """<p>Retrieves the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group to retrieve.</p>

        Raises:
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.get_schedule_group_input.GetScheduleGroupInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.get_schedule_group

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.get_schedule_group.get_schedule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetScheduleGroup")
        )
        input_: capo_scheduler.types.get_schedule_group_input.GetScheduleGroupInput = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        client_token: Optional["capo_scheduler.types.client_token.ClientToken"] = None,
    ) -> "capo_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput":
        """<p>Deletes the specified schedule group. Deleting a schedule group results in EventBridge Scheduler deleting all schedules associated with the group. When you delete a group, it remains in a <code>DELETING</code> state until all of its associated schedules are deleted. Schedules associated with the group that are set to run while the schedule group is in the process of being deleted might continue to invoke their targets until the schedule group and its associated schedules are deleted.</p> <note> <p> This operation is eventually consistent. </p> </note>

        Args:
            name: <p>The name of the schedule group to delete.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.delete_schedule_group

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.delete_schedule_group.delete_schedule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteScheduleGroup")
        )
        input_: capo_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput = {
            "name": name
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
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        name_prefix: Optional[
            "capo_scheduler.types.schedule_group_name_prefix.ScheduleGroupNamePrefix"
        ] = None,
        next_token: Optional["capo_scheduler.types.next_token.NextToken"] = None,
        max_results: Optional["capo_scheduler.types.max_results.MaxResults"] = None,
    ) -> "capo_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput":
        """<p>Returns a paginated list of your schedule groups.</p>

        Args:
            name_prefix: <p>The name prefix that you can use to return a filtered list of your schedule groups.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            max_results: <p>If specified, limits the number of results returned by this operation. The operation also returns a <code>NextToken</code> which you can use in a subsequent operation to retrieve the next set of results.</p>

        Raises:
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.list_schedule_groups

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.list_schedule_groups.list_schedule_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListScheduleGroups")
        )
        input_: capo_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput = {}
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
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


class AsyncScheduleGroup:
    def __init__(self, service: AsyncSchedulerClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
        tags: Optional["capo_scheduler.types.tag_list.TagList"] = None,
        client_token: Optional["capo_scheduler.types.client_token.ClientToken"] = None,
    ) -> "capo_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput":
        """<p>Creates the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group that you are creating.</p>
            tags: <p>The list of tags to associate with the schedule group.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.create_schedule_group

            (
                output,
                http_response,
            ) = await capo_scheduler._operations.aws_chronos_service.create_schedule_group.async_create_schedule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateScheduleGroup")
        )
        input_: capo_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput = {
            "name": name
        }
        if tags is not None:
            input_["tags"] = tags
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
        name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
    ) -> "capo_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput":
        """<p>Retrieves the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group to retrieve.</p>

        Raises:
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_scheduler.types.get_schedule_group_input.GetScheduleGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.get_schedule_group

            (
                output,
                http_response,
            ) = await capo_scheduler._operations.aws_chronos_service.get_schedule_group.async_get_schedule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetScheduleGroup")
        )
        input_: capo_scheduler.types.get_schedule_group_input.GetScheduleGroupInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
        client_token: Optional["capo_scheduler.types.client_token.ClientToken"] = None,
    ) -> "capo_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput":
        """<p>Deletes the specified schedule group. Deleting a schedule group results in EventBridge Scheduler deleting all schedules associated with the group. When you delete a group, it remains in a <code>DELETING</code> state until all of its associated schedules are deleted. Schedules associated with the group that are set to run while the schedule group is in the process of being deleted might continue to invoke their targets until the schedule group and its associated schedules are deleted.</p> <note> <p> This operation is eventually consistent. </p> </note>

        Args:
            name: <p>The name of the schedule group to delete.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.delete_schedule_group

            (
                output,
                http_response,
            ) = await capo_scheduler._operations.aws_chronos_service.delete_schedule_group.async_delete_schedule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteScheduleGroup")
        )
        input_: capo_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput = {
            "name": name
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
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
        name_prefix: Optional[
            "capo_scheduler.types.schedule_group_name_prefix.ScheduleGroupNamePrefix"
        ] = None,
        next_token: Optional["capo_scheduler.types.next_token.NextToken"] = None,
        max_results: Optional["capo_scheduler.types.max_results.MaxResults"] = None,
    ) -> "capo_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput":
        """<p>Returns a paginated list of your schedule groups.</p>

        Args:
            name_prefix: <p>The name prefix that you can use to return a filtered list of your schedule groups.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            max_results: <p>If specified, limits the number of results returned by this operation. The operation also returns a <code>NextToken</code> which you can use in a subsequent operation to retrieve the next set of results.</p>

        Raises:
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.list_schedule_groups

            (
                output,
                http_response,
            ) = await capo_scheduler._operations.aws_chronos_service.list_schedule_groups.async_list_schedule_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListScheduleGroups")
        )
        input_: capo_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput = {}
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
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

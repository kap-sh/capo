from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional

from capo_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.create_scheduled_action_request
    import capo_redshift_serverless.types.create_scheduled_action_response
    import capo_redshift_serverless.types.delete_scheduled_action_request
    import capo_redshift_serverless.types.delete_scheduled_action_response
    import capo_redshift_serverless.types.get_scheduled_action_request
    import capo_redshift_serverless.types.get_scheduled_action_response
    import capo_redshift_serverless.types.iam_role_arn
    import capo_redshift_serverless.types.list_scheduled_actions_request
    import capo_redshift_serverless.types.list_scheduled_actions_response
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.pagination_token
    import capo_redshift_serverless.types.schedule
    import capo_redshift_serverless.types.scheduled_action_association
    import capo_redshift_serverless.types.scheduled_action_name
    import capo_redshift_serverless.types.target_action
    import capo_redshift_serverless.types.update_scheduled_action_request
    import capo_redshift_serverless.types.update_scheduled_action_response
    from capo_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from capo_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class ScheduledActionResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def create_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        target_action: "capo_redshift_serverless.types.target_action.TargetAction",
        schedule: "capo_redshift_serverless.types.schedule.Schedule",
        role_arn: "capo_redshift_serverless.types.iam_role_arn.IamRoleArn",
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        enabled: Optional[bool] = None,
        scheduled_action_description: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_redshift_serverless.types.create_scheduled_action_response.CreateScheduledActionResponse":
        """<p>Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the <code>CreateSnapshot</code> API operation.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action.</p>
            schedule: <p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>
            role_arn: <p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>
            namespace_name: <p>The name of the namespace for which to create a scheduled action.</p>
            enabled: <p>Indicates whether the schedule is enabled. If false, the scheduled action does not trigger. For more information about <code>state</code> of the scheduled action, see <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ScheduledAction.html">ScheduledAction</a>.</p>
            scheduled_action_description: <p>The description of the scheduled action.</p>
            start_time: <p>The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.</p>
            end_time: <p>The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.create_scheduled_action_request.CreateScheduledActionRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.create_scheduled_action_response.CreateScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_scheduled_action

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.create_scheduled_action.create_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_scheduled_action_request.CreateScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name,
            "target_action": target_action,
            "schedule": schedule,
            "role_arn": role_arn,
            "namespace_name": namespace_name,
        }
        if enabled is not None:
            input_["enabled"] = enabled
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_scheduled_action_response.DeleteScheduledActionResponse":
        """<p>Deletes a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to delete.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.delete_scheduled_action_request.DeleteScheduledActionRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.delete_scheduled_action_response.DeleteScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_scheduled_action

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.delete_scheduled_action.delete_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_scheduled_action_request.DeleteScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_scheduled_action_response.GetScheduledActionResponse":
        """<p>Returns information about a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.get_scheduled_action_request.GetScheduledActionRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.get_scheduled_action_response.GetScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_scheduled_action

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.get_scheduled_action.get_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_scheduled_action_request.GetScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_scheduled_actions(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
    ) -> "capo_redshift_serverless.types.list_scheduled_actions_response.ListScheduledActionsResponse":
        """<p>Returns a list of scheduled actions. You can use the flags to filter the list of returned scheduled actions.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. Use <code>nextToken</code> to display the next page of results.</p>
            namespace_name: <p>The name of namespace associated with the scheduled action to retrieve.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_scheduled_actions_request.ListScheduledActionsRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_scheduled_actions_response.ListScheduledActionsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_scheduled_actions

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_scheduled_actions.list_scheduled_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_scheduled_actions_request.ListScheduledActionsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        target_action: Optional[
            "capo_redshift_serverless.types.target_action.TargetAction"
        ] = None,
        schedule: Optional["capo_redshift_serverless.types.schedule.Schedule"] = None,
        role_arn: Optional[
            "capo_redshift_serverless.types.iam_role_arn.IamRoleArn"
        ] = None,
        enabled: Optional[bool] = None,
        scheduled_action_description: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_redshift_serverless.types.update_scheduled_action_response.UpdateScheduledActionResponse":
        """<p>Updates a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to update to.</p>
            schedule: <p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>
            role_arn: <p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>
            enabled: <p>Specifies whether to enable the scheduled action.</p>
            scheduled_action_description: <p>The descripion of the scheduled action to update to.</p>
            start_time: <p>The start time in UTC of the scheduled action to update to.</p>
            end_time: <p>The end time in UTC of the scheduled action to update.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.update_scheduled_action_request.UpdateScheduledActionRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.update_scheduled_action_response.UpdateScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_scheduled_action

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.update_scheduled_action.update_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_scheduled_action_request.UpdateScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }
        if target_action is not None:
            input_["target_action"] = target_action
        if schedule is not None:
            input_["schedule"] = schedule
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if enabled is not None:
            input_["enabled"] = enabled
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncScheduledActionResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def create_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        target_action: "capo_redshift_serverless.types.target_action.TargetAction",
        schedule: "capo_redshift_serverless.types.schedule.Schedule",
        role_arn: "capo_redshift_serverless.types.iam_role_arn.IamRoleArn",
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        enabled: Optional[bool] = None,
        scheduled_action_description: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_redshift_serverless.types.create_scheduled_action_response.CreateScheduledActionResponse":
        """<p>Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the <code>CreateSnapshot</code> API operation.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action.</p>
            schedule: <p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>
            role_arn: <p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>
            namespace_name: <p>The name of the namespace for which to create a scheduled action.</p>
            enabled: <p>Indicates whether the schedule is enabled. If false, the scheduled action does not trigger. For more information about <code>state</code> of the scheduled action, see <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ScheduledAction.html">ScheduledAction</a>.</p>
            scheduled_action_description: <p>The description of the scheduled action.</p>
            start_time: <p>The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.</p>
            end_time: <p>The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_scheduled_action_request.CreateScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_scheduled_action_response.CreateScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_scheduled_action.async_create_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_scheduled_action_request.CreateScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name,
            "target_action": target_action,
            "schedule": schedule,
            "role_arn": role_arn,
            "namespace_name": namespace_name,
        }
        if enabled is not None:
            input_["enabled"] = enabled
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_scheduled_action_response.DeleteScheduledActionResponse":
        """<p>Deletes a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to delete.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_scheduled_action_request.DeleteScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_scheduled_action_response.DeleteScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_scheduled_action.async_delete_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_scheduled_action_request.DeleteScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_scheduled_action_response.GetScheduledActionResponse":
        """<p>Returns information about a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_scheduled_action_request.GetScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_scheduled_action_response.GetScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_scheduled_action.async_get_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_scheduled_action_request.GetScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_scheduled_actions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
    ) -> "capo_redshift_serverless.types.list_scheduled_actions_response.ListScheduledActionsResponse":
        """<p>Returns a list of scheduled actions. You can use the flags to filter the list of returned scheduled actions.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. Use <code>nextToken</code> to display the next page of results.</p>
            namespace_name: <p>The name of namespace associated with the scheduled action to retrieve.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_scheduled_actions_request.ListScheduledActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_scheduled_actions_response.ListScheduledActionsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_scheduled_actions

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_scheduled_actions.async_list_scheduled_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_scheduled_actions_request.ListScheduledActionsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        target_action: Optional[
            "capo_redshift_serverless.types.target_action.TargetAction"
        ] = None,
        schedule: Optional["capo_redshift_serverless.types.schedule.Schedule"] = None,
        role_arn: Optional[
            "capo_redshift_serverless.types.iam_role_arn.IamRoleArn"
        ] = None,
        enabled: Optional[bool] = None,
        scheduled_action_description: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_redshift_serverless.types.update_scheduled_action_response.UpdateScheduledActionResponse":
        """<p>Updates a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to update to.</p>
            schedule: <p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>
            role_arn: <p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>
            enabled: <p>Specifies whether to enable the scheduled action.</p>
            scheduled_action_description: <p>The descripion of the scheduled action to update to.</p>
            start_time: <p>The start time in UTC of the scheduled action to update to.</p>
            end_time: <p>The end time in UTC of the scheduled action to update.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_scheduled_action_request.UpdateScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_scheduled_action_response.UpdateScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_scheduled_action.async_update_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_scheduled_action_request.UpdateScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }
        if target_action is not None:
            input_["target_action"] = target_action
        if schedule is not None:
            input_["schedule"] = schedule
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if enabled is not None:
            input_["enabled"] = enabled
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

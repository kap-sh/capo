"""Generated from Smithy shape ``com.amazonaws.scheduler#AWSChronosService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_scheduler._auth._signers
import capo_scheduler._auth._sigv4
from capo_scheduler._auth._identity import Credentials
from capo_scheduler._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_scheduler._auth._zapros_handler import AuthMiddleware
from capo_scheduler._pagination import resolve_path as _resolve_path
from capo_scheduler._resources.aws_chronos_service.schedule import Schedule
from capo_scheduler._resources.aws_chronos_service.schedule_group import ScheduleGroup
from capo_scheduler._services._aws_config import aws_config
from capo_scheduler._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_scheduler.types.action_after_completion
    import capo_scheduler.types.client_token
    import capo_scheduler.types.create_schedule_group_input
    import capo_scheduler.types.create_schedule_group_output
    import capo_scheduler.types.create_schedule_input
    import capo_scheduler.types.create_schedule_output
    import capo_scheduler.types.delete_schedule_group_input
    import capo_scheduler.types.delete_schedule_group_output
    import capo_scheduler.types.delete_schedule_input
    import capo_scheduler.types.delete_schedule_output
    import capo_scheduler.types.description
    import capo_scheduler.types.end_date
    import capo_scheduler.types.flexible_time_window
    import capo_scheduler.types.get_schedule_group_input
    import capo_scheduler.types.get_schedule_group_output
    import capo_scheduler.types.get_schedule_input
    import capo_scheduler.types.get_schedule_output
    import capo_scheduler.types.kms_key_arn
    import capo_scheduler.types.list_schedule_groups_input
    import capo_scheduler.types.list_schedule_groups_output
    import capo_scheduler.types.list_schedules_input
    import capo_scheduler.types.list_schedules_output
    import capo_scheduler.types.list_tags_for_resource_input
    import capo_scheduler.types.list_tags_for_resource_output
    import capo_scheduler.types.max_results
    import capo_scheduler.types.name
    import capo_scheduler.types.name_prefix
    import capo_scheduler.types.next_token
    import capo_scheduler.types.schedule_expression
    import capo_scheduler.types.schedule_expression_timezone
    import capo_scheduler.types.schedule_group_name
    import capo_scheduler.types.schedule_group_name_prefix
    import capo_scheduler.types.schedule_group_summary
    import capo_scheduler.types.schedule_state
    import capo_scheduler.types.schedule_summary
    import capo_scheduler.types.start_date
    import capo_scheduler.types.tag_key_list
    import capo_scheduler.types.tag_list
    import capo_scheduler.types.tag_resource_arn
    import capo_scheduler.types.tag_resource_input
    import capo_scheduler.types.tag_resource_output
    import capo_scheduler.types.target
    import capo_scheduler.types.untag_resource_input
    import capo_scheduler.types.untag_resource_output
    import capo_scheduler.types.update_schedule_input
    import capo_scheduler.types.update_schedule_output


class SchedulerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SchedulerClient:
    """A client for the ``Scheduler`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = SchedulerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.schedule = Schedule(self)
        self.schedule_group = ScheduleGroup(self)

    def operation_options(
        self, config_overrides: Optional[SchedulerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SchedulerClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_scheduler.types.tag_resource_arn.TagResourceArn",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
    ) -> "capo_scheduler.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with the Scheduler resource.</p>

        Args:
            resource_arn: <p>The ARN of the EventBridge Scheduler resource for which you want to view tags.</p>

        Raises:
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.list_tags_for_resource

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_scheduler.types.tag_resource_arn.TagResourceArn",
        tags: "capo_scheduler.types.tag_list.TagList",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
    ) -> "capo_scheduler.types.tag_resource_output.TagResourceOutput":
        """<p>Assigns one or more tags (key-value pairs) to the specified EventBridge Scheduler resource. You can only assign tags to schedule groups.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the schedule group that you are adding tags to.</p>
            tags: <p>The list of tags to associate with the schedule group.</p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.tag_resource

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_scheduler.types.tag_resource_arn.TagResourceArn",
        tag_keys: "capo_scheduler.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
    ) -> "capo_scheduler.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from the specified EventBridge Scheduler schedule group.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the schedule group from which you are removing tags.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.untag_resource

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_schedule(
        self,
        name: "capo_scheduler.types.name.Name",
        schedule_expression: "capo_scheduler.types.schedule_expression.ScheduleExpression",
        target: "capo_scheduler.types.target.Target",
        flexible_time_window: "capo_scheduler.types.flexible_time_window.FlexibleTimeWindow",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        group_name: Optional[
            "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
        ] = None,
        start_date: Optional["capo_scheduler.types.start_date.StartDate"] = None,
        end_date: Optional["capo_scheduler.types.end_date.EndDate"] = None,
        description: Optional["capo_scheduler.types.description.Description"] = None,
        schedule_expression_timezone: Optional[
            "capo_scheduler.types.schedule_expression_timezone.ScheduleExpressionTimezone"
        ] = None,
        state: Optional["capo_scheduler.types.schedule_state.ScheduleState"] = None,
        kms_key_arn: Optional["capo_scheduler.types.kms_key_arn.KmsKeyArn"] = None,
        client_token: Optional["capo_scheduler.types.client_token.ClientToken"] = None,
        action_after_completion: Optional[
            "capo_scheduler.types.action_after_completion.ActionAfterCompletion"
        ] = None,
    ) -> "capo_scheduler.types.create_schedule_output.CreateScheduleOutput":
        """<p>Creates the specified schedule.</p>

        Args:
            name: <p>The name of the schedule that you are creating.</p>
            group_name: <p>The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.</p>
            schedule_expression: <p> The expression that defines when the schedule runs. The following formats are supported. </p> <ul> <li> <p> <code>at</code> expression - <code>at(yyyy-mm-ddThh:mm:ss)</code> </p> </li> <li> <p> <code>rate</code> expression - <code>rate(value unit)</code> </p> </li> <li> <p> <code>cron</code> expression - <code>cron(fields)</code> </p> </li> </ul> <p> You can use <code>at</code> expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use <code>rate</code> and <code>cron</code> expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month. </p> <p> A <code>cron</code> expression consists of six fields separated by white spaces: <code>(minutes hours day_of_month month day_of_week year)</code>. </p> <p> A <code>rate</code> expression consists of a <i>value</i> as a positive integer, and a <i>unit</i> with the following options: <code>minute</code> | <code>minutes</code> | <code>hour</code> | <code>hours</code> | <code>day</code> | <code>days</code> </p> <p> For more information and examples, see <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">Schedule types on EventBridge Scheduler</a> in the <i>EventBridge Scheduler User Guide</i>. </p>
            start_date: <p>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the <code>StartDate</code> you specify. EventBridge Scheduler ignores <code>StartDate</code> for one-time schedules.</p>
            end_date: <p>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the <code>EndDate</code> you specify. EventBridge Scheduler ignores <code>EndDate</code> for one-time schedules.</p>
            description: <p>The description you specify for the schedule.</p>
            schedule_expression_timezone: <p>The timezone in which the scheduling expression is evaluated.</p>
            state: <p>Specifies whether the schedule is enabled or disabled.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) for the customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.</p>
            target: <p>The schedule's target.</p>
            flexible_time_window: <p>Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>
            action_after_completion: <p>Specifies the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target.</p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.create_schedule_input.CreateScheduleInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.create_schedule_output.CreateScheduleOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.create_schedule

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.create_schedule.create_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.create_schedule_input.CreateScheduleInput = {
            "name": name,
            "schedule_expression": schedule_expression,
            "target": target,
            "flexible_time_window": flexible_time_window,
        }
        if group_name is not None:
            input_["group_name"] = group_name
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if description is not None:
            input_["description"] = description
        if schedule_expression_timezone is not None:
            input_["schedule_expression_timezone"] = schedule_expression_timezone
        if state is not None:
            input_["state"] = state
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if action_after_completion is not None:
            input_["action_after_completion"] = action_after_completion

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_schedule(
        self,
        name: "capo_scheduler.types.name.Name",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        group_name: Optional[
            "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
        ] = None,
    ) -> "capo_scheduler.types.get_schedule_output.GetScheduleOutput":
        """<p>Retrieves the specified schedule.</p>

        Args:
            name: <p>The name of the schedule to retrieve.</p>
            group_name: <p>The name of the schedule group associated with this schedule. If you omit this, EventBridge Scheduler assumes that the schedule is associated with the default group.</p>

        Raises:
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.get_schedule_input.GetScheduleInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.get_schedule_output.GetScheduleOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.get_schedule

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.get_schedule.get_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.get_schedule_input.GetScheduleInput = {
            "name": name
        }
        if group_name is not None:
            input_["group_name"] = group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_schedule(
        self,
        name: "capo_scheduler.types.name.Name",
        schedule_expression: "capo_scheduler.types.schedule_expression.ScheduleExpression",
        target: "capo_scheduler.types.target.Target",
        flexible_time_window: "capo_scheduler.types.flexible_time_window.FlexibleTimeWindow",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        group_name: Optional[
            "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
        ] = None,
        start_date: Optional["capo_scheduler.types.start_date.StartDate"] = None,
        end_date: Optional["capo_scheduler.types.end_date.EndDate"] = None,
        description: Optional["capo_scheduler.types.description.Description"] = None,
        schedule_expression_timezone: Optional[
            "capo_scheduler.types.schedule_expression_timezone.ScheduleExpressionTimezone"
        ] = None,
        state: Optional["capo_scheduler.types.schedule_state.ScheduleState"] = None,
        kms_key_arn: Optional["capo_scheduler.types.kms_key_arn.KmsKeyArn"] = None,
        client_token: Optional["capo_scheduler.types.client_token.ClientToken"] = None,
        action_after_completion: Optional[
            "capo_scheduler.types.action_after_completion.ActionAfterCompletion"
        ] = None,
    ) -> "capo_scheduler.types.update_schedule_output.UpdateScheduleOutput":
        """<p> Updates the specified schedule. When you call <code>UpdateSchedule</code>, EventBridge Scheduler uses all values, including empty values, specified in the request and overrides the existing schedule. This is by design. This means that if you do not set an optional field in your request, that field will be set to its system-default value after the update. </p> <p> Before calling this operation, we recommend that you call the <code>GetSchedule</code> API operation and make a note of all optional parameters for your <code>UpdateSchedule</code> call. </p>

        Args:
            name: <p>The name of the schedule that you are updating.</p>
            group_name: <p>The name of the schedule group with which the schedule is associated. You must provide this value in order for EventBridge Scheduler to find the schedule you want to update. If you omit this value, EventBridge Scheduler assumes the group is associated to the default group.</p>
            schedule_expression: <p> The expression that defines when the schedule runs. The following formats are supported. </p> <ul> <li> <p> <code>at</code> expression - <code>at(yyyy-mm-ddThh:mm:ss)</code> </p> </li> <li> <p> <code>rate</code> expression - <code>rate(value unit)</code> </p> </li> <li> <p> <code>cron</code> expression - <code>cron(fields)</code> </p> </li> </ul> <p> You can use <code>at</code> expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use <code>rate</code> and <code>cron</code> expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month. </p> <p> A <code>cron</code> expression consists of six fields separated by white spaces: <code>(minutes hours day_of_month month day_of_week year)</code>. </p> <p> A <code>rate</code> expression consists of a <i>value</i> as a positive integer, and a <i>unit</i> with the following options: <code>minute</code> | <code>minutes</code> | <code>hour</code> | <code>hours</code> | <code>day</code> | <code>days</code> </p> <p> For more information and examples, see <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">Schedule types on EventBridge Scheduler</a> in the <i>EventBridge Scheduler User Guide</i>. </p>
            start_date: <p>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the <code>StartDate</code> you specify. EventBridge Scheduler ignores <code>StartDate</code> for one-time schedules.</p>
            end_date: <p>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the <code>EndDate</code> you specify. EventBridge Scheduler ignores <code>EndDate</code> for one-time schedules.</p>
            description: <p>The description you specify for the schedule.</p>
            schedule_expression_timezone: <p>The timezone in which the scheduling expression is evaluated.</p>
            state: <p>Specifies whether the schedule is enabled or disabled.</p>
            kms_key_arn: <p>The ARN for the customer managed KMS key that that you want EventBridge Scheduler to use to encrypt and decrypt your data.</p>
            target: <p>The schedule target. You can use this operation to change the target that your schedule invokes.</p>
            flexible_time_window: <p>Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>
            action_after_completion: <p>Specifies the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target.</p>

        Raises:
            capo_scheduler.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.update_schedule_input.UpdateScheduleInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.update_schedule_output.UpdateScheduleOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.update_schedule

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.update_schedule.update_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.update_schedule_input.UpdateScheduleInput = {
            "name": name,
            "schedule_expression": schedule_expression,
            "target": target,
            "flexible_time_window": flexible_time_window,
        }
        if group_name is not None:
            input_["group_name"] = group_name
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if description is not None:
            input_["description"] = description
        if schedule_expression_timezone is not None:
            input_["schedule_expression_timezone"] = schedule_expression_timezone
        if state is not None:
            input_["state"] = state
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if action_after_completion is not None:
            input_["action_after_completion"] = action_after_completion

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_schedule(
        self,
        name: "capo_scheduler.types.name.Name",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        group_name: Optional[
            "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
        ] = None,
        client_token: Optional["capo_scheduler.types.client_token.ClientToken"] = None,
    ) -> "capo_scheduler.types.delete_schedule_output.DeleteScheduleOutput":
        """<p>Deletes the specified schedule.</p>

        Args:
            name: <p>The name of the schedule to delete.</p>
            group_name: <p>The name of the schedule group associated with this schedule. If you omit this, the default schedule group is used.</p>
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
            req: "OperationRequest[capo_scheduler.types.delete_schedule_input.DeleteScheduleInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.delete_schedule_output.DeleteScheduleOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.delete_schedule

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.delete_schedule.delete_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.delete_schedule_input.DeleteScheduleInput = {
            "name": name
        }
        if group_name is not None:
            input_["group_name"] = group_name
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

    def list_schedules(
        self,
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        group_name: Optional[
            "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
        ] = None,
        name_prefix: Optional["capo_scheduler.types.name_prefix.NamePrefix"] = None,
        state: Optional["capo_scheduler.types.schedule_state.ScheduleState"] = None,
        next_token: Optional["capo_scheduler.types.next_token.NextToken"] = None,
        max_results: Optional["capo_scheduler.types.max_results.MaxResults"] = None,
    ) -> "capo_scheduler.types.list_schedules_output.ListSchedulesOutput":
        """<p>Returns a paginated list of your EventBridge Scheduler schedules.</p>

        Args:
            group_name: <p>If specified, only lists the schedules whose associated schedule group matches the given filter.</p>
            name_prefix: <p>Schedule name prefix to return the filtered list of resources.</p>
            state: <p>If specified, only lists the schedules whose current state matches the given filter.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            max_results: <p>If specified, limits the number of results returned by this operation. The operation also returns a <code>NextToken</code> which you can use in a subsequent operation to retrieve the next set of results.</p>

        Raises:
            capo_scheduler.errors.internal_server_exception.InternalServerException: <p>Unexpected error encountered while processing the request.</p>
            capo_scheduler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_scheduler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_scheduler.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_scheduler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_scheduler.types.list_schedules_input.ListSchedulesInput]",
        ) -> OperationResponse[
            "capo_scheduler.types.list_schedules_output.ListSchedulesOutput"
        ]:
            import capo_scheduler._operations.aws_chronos_service.list_schedules

            output, http_response = (
                capo_scheduler._operations.aws_chronos_service.list_schedules.list_schedules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_scheduler.types.list_schedules_input.ListSchedulesInput = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if state is not None:
            input_["state"] = state
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

    def iter_list_schedules(
        self,
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        group_name: Optional[
            "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
        ] = None,
        name_prefix: Optional["capo_scheduler.types.name_prefix.NamePrefix"] = None,
        state: Optional["capo_scheduler.types.schedule_state.ScheduleState"] = None,
        next_token: Optional["capo_scheduler.types.next_token.NextToken"] = None,
        max_results: Optional["capo_scheduler.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_scheduler.types.schedule_summary.ScheduleSummary]":
        _token = next_token
        while True:
            _response = self.list_schedules(
                config_overrides=config_overrides,
                group_name=group_name,
                name_prefix=name_prefix,
                state=state,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("schedules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_schedule_group(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_schedule_group(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_schedule_group(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_schedule_groups(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_schedule_groups(
        self,
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        name_prefix: Optional[
            "capo_scheduler.types.schedule_group_name_prefix.ScheduleGroupNamePrefix"
        ] = None,
        next_token: Optional["capo_scheduler.types.next_token.NextToken"] = None,
        max_results: Optional["capo_scheduler.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_scheduler.types.schedule_group_summary.ScheduleGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_schedule_groups(
                config_overrides=config_overrides,
                name_prefix=name_prefix,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("schedule_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

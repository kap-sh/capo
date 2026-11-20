"""Generated from Smithy shape ``com.amazonaws.connectscheduling#AmazonConnectScheduling``."""

import datetime
import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_connectscheduling._auth._signers
import capo_connectscheduling._auth._sigv4
from capo_connectscheduling._auth._identity import Credentials
from capo_connectscheduling._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_connectscheduling._auth._zapros_handler import AuthMiddleware
from capo_connectscheduling._services._aws_config import aws_config
from capo_connectscheduling._services._pipeline import (
    Interceptor,
    OperationLogging,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    ThreadSafeRateLimiter,
    ThreadSafeRetryQuota,
    execute_pipeline,
    log_operation,
    rate_limit,
    retry,
)

if TYPE_CHECKING:
    import capo_connectscheduling.types.approval_type
    import capo_connectscheduling.types.approve_time_off_request
    import capo_connectscheduling.types.approve_time_off_response
    import capo_connectscheduling.types.cancel_time_off_request
    import capo_connectscheduling.types.cancel_time_off_response
    import capo_connectscheduling.types.client_token
    import capo_connectscheduling.types.create_time_off_request
    import capo_connectscheduling.types.create_time_off_response
    import capo_connectscheduling.types.description
    import capo_connectscheduling.types.duration
    import capo_connectscheduling.types.get_time_off_request
    import capo_connectscheduling.types.get_time_off_response
    import capo_connectscheduling.types.instance_id_or_arn
    import capo_connectscheduling.types.put_time_off_balance_request
    import capo_connectscheduling.types.put_time_off_balance_response
    import capo_connectscheduling.types.reject_time_off_request
    import capo_connectscheduling.types.reject_time_off_response
    import capo_connectscheduling.types.rule_failure_action
    import capo_connectscheduling.types.shift_activity_id_or_arn
    import capo_connectscheduling.types.time_off_id
    import capo_connectscheduling.types.user_id_or_arn


class ConnectSchedulingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ConnectSchedulingClient:
    """A client for the ``ConnectScheduling`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        retry_mode: Literal["standard", "adaptive"] | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = Client(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = ThreadSafeRetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = ThreadSafeRateLimiter()
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
                Client(raw_handler)
            )
        self._config = ConnectSchedulingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[ConnectSchedulingClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ConnectSchedulingClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(log_operation(operation_logging))
        interceptors_.append(retry())
        interceptors_.append(rate_limit())
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def approve_time_off(
        self,
        instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn",
        user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn",
        time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId",
        *,
        config_overrides: Optional[ConnectSchedulingClientConfig] = None,
        description: Optional[
            "capo_connectscheduling.types.description.Description"
        ] = None,
        rule_failure_action: Optional[
            "capo_connectscheduling.types.rule_failure_action.RuleFailureAction"
        ] = None,
    ) -> (
        "capo_connectscheduling.types.approve_time_off_response.ApproveTimeOffResponse"
    ):
        """<p>Approves a time off request. Evaluates agent time off balances and group time off allowances before approving. <code>RuleFailureAction</code> controls what happens when these evaluations fail. The request is rejected with <code>CONFLICTING_TIME_OFF_REQUEST</code> if it overlaps another time off request for the user that is <code>APPROVED</code> or being approved.</p> <p>The time off request is processed asynchronously, so a successful call doesn't indicate the final status. Read the resulting status with <code>GetTimeOff</code> or from the time off state-change events.</p> <p>Approving an <code>APPROVED</code> request succeeds without a change. Approving a <code>REJECTED</code> request evaluates the rules again, so it can end <code>APPROVED</code> or <code>REJECTED</code>, and repeating the call can give a different result. Check the status with <code>GetTimeOff</code> before you retry.</p> <p>Returns <code>ConflictException</code> if the request is <code>PENDING</code> or <code>CANCELLED</code>. <code>PENDING</code> means Connect Customer is still processing the request asynchronously. Wait until <code>GetTimeOff</code> returns a status other than <code>PENDING</code>, and then retry.</p> <important> <p>When the approval succeeds, Connect Customer cancels any overtime or voluntary time off activity that overlaps the approved window.</p> </important> <note> <p>Connect Customer doesn't check whether the principal that calls this operation supervises the user. The staffing group's approval settings also don't apply. IAM permissions are the only control. If you allow a principal to call this operation, that principal can send <code>RuleFailureAction</code> <code>OVERRIDE</code> and approve a request past failed rules. Grant permission for this operation only to principals that you trust to override time off rules.</p> </note>

        Args:
            instance_id: <p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>
            user_id: <p>The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.</p>
            time_off_id: <p>The unique identifier of the time off request to approve. If the time off request doesn't belong to <code>UserId</code>, the operation returns <code>ResourceNotFoundException</code>.</p>
            description: <p>A description recorded with the approval. <code>GetTimeOff</code> doesn't return it.</p>
            rule_failure_action: <p>Controls what happens when a configured rule fails. <code>REJECT</code>, the default, records an <code>ERROR</code> and leaves the request <code>REJECTED</code>. <code>OVERRIDE</code> records a <code>WARNING</code> and approves the request, like the <i>Override time off rules</i> option in the Connect Customer admin website. <code>OVERRIDE</code> never waives <code>CONFLICTING_TIME_OFF_REQUEST</code>.</p>

        Raises:
            capo_connectscheduling.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_connectscheduling.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict with the current state of the resource.</p>
            capo_connectscheduling.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an error or failure with the service.</p>
            capo_connectscheduling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_connectscheduling.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectscheduling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_connectscheduling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To approve a time off request past a failed rule
            The following example approves a time off request with RuleFailureAction OVERRIDE, so a failed rule is recorded as a WARNING instead of rejecting the request.

            >>> client.approve_time_off(instance_id='12345678-1234-1234-1234-123456789012', user_id='87654321-4321-4321-4321-210987654321', time_off_id='abcdef12-3456-7890-abcd-ef1234567890', description='Approved with coverage from the evening shift', rule_failure_action='OVERRIDE')
        """

        def _handler(
            req: "OperationRequest[capo_connectscheduling.types.approve_time_off_request.ApproveTimeOffRequest]",
        ) -> OperationResponse[
            "capo_connectscheduling.types.approve_time_off_response.ApproveTimeOffResponse"
        ]:
            import capo_connectscheduling._operations.amazon_connect_scheduling.approve_time_off

            output, http_response = (
                capo_connectscheduling._operations.amazon_connect_scheduling.approve_time_off.approve_time_off(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectscheduling.types.approve_time_off_request.ApproveTimeOffRequest",
        ) -> dict[str, Any]:
            import capo_connectscheduling.types.approve_time_off_request

            return (
                capo_connectscheduling.types.approve_time_off_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("ApproveTimeOff", redact_input=_redact_input),
        )
        input_: capo_connectscheduling.types.approve_time_off_request.ApproveTimeOffRequest = {
            "instance_id": instance_id,
            "user_id": user_id,
            "time_off_id": time_off_id,
        }
        if description is not None:
            input_["description"] = description
        if rule_failure_action is not None:
            input_["rule_failure_action"] = rule_failure_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_time_off(
        self,
        instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn",
        user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn",
        time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId",
        *,
        config_overrides: Optional[ConnectSchedulingClientConfig] = None,
        description: Optional[
            "capo_connectscheduling.types.description.Description"
        ] = None,
    ) -> "capo_connectscheduling.types.cancel_time_off_response.CancelTimeOffResponse":
        """<p>Cancels a time off request.</p> <p>Cancelling a <code>CANCELLED</code> request succeeds without a change. Returns <code>ConflictException</code> if the request is <code>PENDING</code>, which means Connect Customer is still processing the request asynchronously. Wait until <code>GetTimeOff</code> returns a status other than <code>PENDING</code>, and then retry.</p>

        Args:
            instance_id: <p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>
            user_id: <p>The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.</p>
            time_off_id: <p>The unique identifier of the time off request to cancel. If the time off request doesn't belong to <code>UserId</code>, the operation returns <code>ResourceNotFoundException</code>.</p>
            description: <p>A description recorded with the cancellation. It replaces the description of the time off request. If you omit it, the request's description is removed.</p>

        Raises:
            capo_connectscheduling.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_connectscheduling.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict with the current state of the resource.</p>
            capo_connectscheduling.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an error or failure with the service.</p>
            capo_connectscheduling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_connectscheduling.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectscheduling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_connectscheduling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel a time off request
            The following example cancels a time off request and records the reason on the cancellation.

            >>> client.cancel_time_off(instance_id='12345678-1234-1234-1234-123456789012', user_id='87654321-4321-4321-4321-210987654321', time_off_id='abcdef12-3456-7890-abcd-ef1234567890', description='Plans changed')
        """

        def _handler(
            req: "OperationRequest[capo_connectscheduling.types.cancel_time_off_request.CancelTimeOffRequest]",
        ) -> OperationResponse[
            "capo_connectscheduling.types.cancel_time_off_response.CancelTimeOffResponse"
        ]:
            import capo_connectscheduling._operations.amazon_connect_scheduling.cancel_time_off

            output, http_response = (
                capo_connectscheduling._operations.amazon_connect_scheduling.cancel_time_off.cancel_time_off(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectscheduling.types.cancel_time_off_request.CancelTimeOffRequest",
        ) -> dict[str, Any]:
            import capo_connectscheduling.types.cancel_time_off_request

            return (
                capo_connectscheduling.types.cancel_time_off_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CancelTimeOff", redact_input=_redact_input),
        )
        input_: capo_connectscheduling.types.cancel_time_off_request.CancelTimeOffRequest = {
            "instance_id": instance_id,
            "user_id": user_id,
            "time_off_id": time_off_id,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_time_off(
        self,
        instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn",
        user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn",
        shift_activity_id: "capo_connectscheduling.types.shift_activity_id_or_arn.ShiftActivityIdOrArn",
        start_at: datetime.datetime,
        end_at: datetime.datetime,
        approval_type: "capo_connectscheduling.types.approval_type.ApprovalType",
        *,
        config_overrides: Optional[ConnectSchedulingClientConfig] = None,
        description: Optional[
            "capo_connectscheduling.types.description.Description"
        ] = None,
        rule_failure_action: Optional[
            "capo_connectscheduling.types.rule_failure_action.RuleFailureAction"
        ] = None,
        client_token: Optional[
            "capo_connectscheduling.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_connectscheduling.types.create_time_off_response.CreateTimeOffResponse":
        """<p>Creates a time off request for a user. You don't provide a status, because Connect Customer owns the request lifecycle. To get the decided status, call <code>GetTimeOff</code> or use the time off state-change events.</p> <p> <code>ApprovalType</code> controls who approves the request. You can specify one of the following values:</p> <ul> <li> <p> <code>AWAIT_APPROVAL</code>: the request waits in <code>AWAITING_APPROVAL</code> until you call <code>ApproveTimeOff</code> or <code>RejectTimeOff</code>. Rule evaluation and the overlap check run at approval, not at creation. A waiting request doesn't reserve its window, so another request for the same window can be approved first.</p> </li> <li> <p> <code>AUTOMATIC</code>: Connect Customer evaluates the rules (time off balances and group allowances) and decides the request. The request can be <code>PENDING</code> while Connect Customer decides, and then ends <code>APPROVED</code> or <code>REJECTED</code>. If it overlaps another time off request for the user, the requested time off ends <code>REJECTED</code> with <code>CONFLICTING_TIME_OFF_REQUEST</code>. It also ends <code>REJECTED</code> if it overlaps overtime or voluntary time off. If the whole window is in the past, Connect Customer records failed rules as <code>WARNING</code> and doesn't reject the request, whatever the <code>RuleFailureAction</code>.</p> </li> </ul> <p>The staffing group's <i>Supervisor approval needed</i> setting doesn't apply to this operation. <code>ApprovalType</code> alone decides whether the request waits for approval. The operation fails with <code>ValidationException</code> on <code>UserId</code> in the following cases:</p> <ul> <li> <p>The user isn't in a staffing group, or the staffing group isn't associated with a forecast group.</p> </li> <li> <p>Time off isn't <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-to.html">enabled</a> for the user's staffing group, or the user's staff rules don't allow time off.</p> </li> </ul> <p>To change the dates of a request, cancel it with <code>CancelTimeOff</code> and create a new request. The new request has a new <code>TimeOffId</code>.</p> <note> <p>Connect Customer doesn't check whether the principal that calls this operation supervises the user. The staffing group's approval settings also don't apply. IAM permissions are the only control. If you allow a principal to call this operation, that principal can send <code>ApprovalType</code> <code>AUTOMATIC</code> with <code>RuleFailureAction</code> <code>OVERRIDE</code> and approve a request past failed rules. Grant permission for this operation only to principals that you trust to override time off rules.</p> </note> <p>For information about time off in the Connect Customer admin website, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/scheduling-time-off.html">Time off management</a> in the <i>Connect Customer Administrator Guide</i>.</p>

        Args:
            instance_id: <p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>
            user_id: <p>The identifier of the user who the time off request is for. This can be the ID or the ARN of the user.</p>
            shift_activity_id: <p>The identifier of the shift activity that defines the type of time off being requested. This can be the ID or the ARN of the shift activity. It must be a time off activity. Activities that aren't set as <i>Requestable</i> are accepted.</p>
            start_at: <p>The start of the time off window, inclusive. It must be no earlier than one year before the current date. Connect Customer stores the value as sent, to the millisecond.</p>
            end_at: <p>The end of the time off window, exclusive. It must be after <code>StartAt</code> and no later than 24 months after the current date. Connect Customer stores the value as sent, to the millisecond.</p>
            description: <p>A description recorded on the time off request. If you omit it, the request has no description.</p>
            approval_type: <p>Controls who approves the request. <code>AWAIT_APPROVAL</code> waits for an <code>ApproveTimeOff</code> or <code>RejectTimeOff</code> call. <code>AUTOMATIC</code> has Connect Customer decide the request. For details, see <code>CreateTimeOff</code>.</p>
            rule_failure_action: <p>Controls what happens when a configured rule fails. <code>REJECT</code>, the default, records an <code>ERROR</code> and ends the request <code>REJECTED</code>, unless the whole window is in the past. <code>OVERRIDE</code> records a <code>WARNING</code> and ends the request <code>APPROVED</code>, like the <i>Override time off rules</i> option in the Connect Customer admin website. <code>OVERRIDE</code> requires <code>AUTOMATIC</code>. With <code>AWAIT_APPROVAL</code>, <code>OVERRIDE</code> fails with <code>ValidationException</code>. Set it on <code>ApproveTimeOff</code> instead. <code>OVERRIDE</code> never waives <code>CONFLICTING_TIME_OFF_REQUEST</code>.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, Connect Customer returns the result of that request and doesn't create another time off request. If you don't provide a token, the AWS SDK populates this field. If you reuse a client token with a different request body, the request fails with <code>ValidationException</code>. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>

        Raises:
            capo_connectscheduling.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_connectscheduling.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict with the current state of the resource.</p>
            capo_connectscheduling.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an error or failure with the service.</p>
            capo_connectscheduling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_connectscheduling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_connectscheduling.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectscheduling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_connectscheduling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a time off request that waits for approval
            The following example creates a time off request for one day. The request is created in AWAITING_APPROVAL until an ApproveTimeOff or RejectTimeOff call decides it.

            >>> client.create_time_off(instance_id='12345678-1234-1234-1234-123456789012', user_id='87654321-4321-4321-4321-210987654321', shift_activity_id='11112222-3333-4444-5555-666677778888', start_at=1795424400, end_at=1795453200, description='Family event', approval_type='AWAIT_APPROVAL')
        """

        def _handler(
            req: "OperationRequest[capo_connectscheduling.types.create_time_off_request.CreateTimeOffRequest]",
        ) -> OperationResponse[
            "capo_connectscheduling.types.create_time_off_response.CreateTimeOffResponse"
        ]:
            import capo_connectscheduling._operations.amazon_connect_scheduling.create_time_off

            output, http_response = (
                capo_connectscheduling._operations.amazon_connect_scheduling.create_time_off.create_time_off(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectscheduling.types.create_time_off_request.CreateTimeOffRequest",
        ) -> dict[str, Any]:
            import capo_connectscheduling.types.create_time_off_request

            return (
                capo_connectscheduling.types.create_time_off_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateTimeOff", redact_input=_redact_input),
        )
        input_: capo_connectscheduling.types.create_time_off_request.CreateTimeOffRequest = {
            "instance_id": instance_id,
            "user_id": user_id,
            "shift_activity_id": shift_activity_id,
            "start_at": start_at,
            "end_at": end_at,
            "approval_type": approval_type,
        }
        if description is not None:
            input_["description"] = description
        if rule_failure_action is not None:
            input_["rule_failure_action"] = rule_failure_action
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

    def get_time_off(
        self,
        instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn",
        user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn",
        time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId",
        *,
        config_overrides: Optional[ConnectSchedulingClientConfig] = None,
    ) -> "capo_connectscheduling.types.get_time_off_response.GetTimeOffResponse":
        """<p>Returns a time off request, including its current status and validation results.</p>

        Args:
            instance_id: <p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>
            user_id: <p>The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.</p>
            time_off_id: <p>The identifier of the time off request. If the time off request doesn't belong to <code>UserId</code>, the operation returns <code>ResourceNotFoundException</code>.</p>

        Raises:
            capo_connectscheduling.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_connectscheduling.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an error or failure with the service.</p>
            capo_connectscheduling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_connectscheduling.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectscheduling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_connectscheduling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a time off request
            The following example gets a time off request that was approved past a failed group allowance rule, which is reported as a WARNING.

            >>> client.get_time_off(instance_id='12345678-1234-1234-1234-123456789012', user_id='87654321-4321-4321-4321-210987654321', time_off_id='abcdef12-3456-7890-abcd-ef1234567890')
        """

        def _handler(
            req: "OperationRequest[capo_connectscheduling.types.get_time_off_request.GetTimeOffRequest]",
        ) -> OperationResponse[
            "capo_connectscheduling.types.get_time_off_response.GetTimeOffResponse"
        ]:
            import capo_connectscheduling._operations.amazon_connect_scheduling.get_time_off

            output, http_response = (
                capo_connectscheduling._operations.amazon_connect_scheduling.get_time_off.get_time_off(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_connectscheduling.types.get_time_off_response.GetTimeOffResponse",
        ) -> dict[str, Any]:
            import capo_connectscheduling.types.get_time_off_response

            return capo_connectscheduling.types.get_time_off_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetTimeOff", redact_output=_redact_output),
        )
        input_: capo_connectscheduling.types.get_time_off_request.GetTimeOffRequest = {
            "instance_id": instance_id,
            "user_id": user_id,
            "time_off_id": time_off_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_time_off_balance(
        self,
        instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn",
        user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn",
        shift_activity_id: "capo_connectscheduling.types.shift_activity_id_or_arn.ShiftActivityIdOrArn",
        balance: "capo_connectscheduling.types.duration.Duration",
        *,
        config_overrides: Optional[ConnectSchedulingClientConfig] = None,
    ) -> "capo_connectscheduling.types.put_time_off_balance_response.PutTimeOffBalanceResponse":
        """<p>Sets the time off balance for one user and shift activity. The value replaces the existing balance rather than adjusting it, so you can safely retry the call. This operation can't remove a balance. To remove one, upload a blank balance in the Connect Customer admin website. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/upload-timeoff-balance.html">Import an agent's time off balance</a> in the <i>Connect Customer Administrator Guide</i>.</p>

        Args:
            instance_id: <p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>
            user_id: <p>The identifier of the user whose balance is being updated. This can be the ID or the ARN of the user.</p>
            shift_activity_id: <p>The identifier of the shift activity that the balance applies to. This can be the ID or the ARN of the shift activity.</p>
            balance: <p>The new time off balance for the user and activity. It replaces the existing balance.</p>

        Raises:
            capo_connectscheduling.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_connectscheduling.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict with the current state of the resource.</p>
            capo_connectscheduling.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an error or failure with the service.</p>
            capo_connectscheduling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_connectscheduling.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectscheduling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_connectscheduling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set a user's time off balance
            The following example sets a user's balance for one time off activity to 80 hours, replacing any existing balance.

            >>> client.put_time_off_balance(instance_id='12345678-1234-1234-1234-123456789012', user_id='87654321-4321-4321-4321-210987654321', shift_activity_id='11112222-3333-4444-5555-666677778888', balance={'Value': 80, 'Unit': 'HOURS'})
        """

        def _handler(
            req: "OperationRequest[capo_connectscheduling.types.put_time_off_balance_request.PutTimeOffBalanceRequest]",
        ) -> OperationResponse[
            "capo_connectscheduling.types.put_time_off_balance_response.PutTimeOffBalanceResponse"
        ]:
            import capo_connectscheduling._operations.amazon_connect_scheduling.put_time_off_balance

            output, http_response = (
                capo_connectscheduling._operations.amazon_connect_scheduling.put_time_off_balance.put_time_off_balance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("PutTimeOffBalance")
        )
        input_: capo_connectscheduling.types.put_time_off_balance_request.PutTimeOffBalanceRequest = {
            "instance_id": instance_id,
            "user_id": user_id,
            "shift_activity_id": shift_activity_id,
            "balance": balance,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_time_off(
        self,
        instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn",
        user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn",
        time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId",
        *,
        config_overrides: Optional[ConnectSchedulingClientConfig] = None,
        description: Optional[
            "capo_connectscheduling.types.description.Description"
        ] = None,
    ) -> "capo_connectscheduling.types.reject_time_off_response.RejectTimeOffResponse":
        """<p>Rejects a time off request.</p> <p>Rejecting a <code>REJECTED</code> request succeeds without a change. Returns <code>ConflictException</code> if the request is <code>PENDING</code> or <code>CANCELLED</code>. <code>PENDING</code> means Connect Customer is still processing the request asynchronously. Wait until <code>GetTimeOff</code> returns a status other than <code>PENDING</code>, and then retry.</p>

        Args:
            instance_id: <p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>
            user_id: <p>The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.</p>
            time_off_id: <p>The unique identifier of the time off request to reject. If the time off request doesn't belong to <code>UserId</code>, the operation returns <code>ResourceNotFoundException</code>.</p>
            description: <p>A description recorded with the rejection, such as the reason. <code>GetTimeOff</code> doesn't return it.</p>

        Raises:
            capo_connectscheduling.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_connectscheduling.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict with the current state of the resource.</p>
            capo_connectscheduling.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an error or failure with the service.</p>
            capo_connectscheduling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_connectscheduling.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectscheduling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_connectscheduling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To reject a time off request
            The following example rejects a time off request and records the reason on the rejection.

            >>> client.reject_time_off(instance_id='12345678-1234-1234-1234-123456789012', user_id='87654321-4321-4321-4321-210987654321', time_off_id='abcdef12-3456-7890-abcd-ef1234567890', description='Not enough coverage for this shift')
        """

        def _handler(
            req: "OperationRequest[capo_connectscheduling.types.reject_time_off_request.RejectTimeOffRequest]",
        ) -> OperationResponse[
            "capo_connectscheduling.types.reject_time_off_response.RejectTimeOffResponse"
        ]:
            import capo_connectscheduling._operations.amazon_connect_scheduling.reject_time_off

            output, http_response = (
                capo_connectscheduling._operations.amazon_connect_scheduling.reject_time_off.reject_time_off(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_connectscheduling.types.reject_time_off_request.RejectTimeOffRequest",
        ) -> dict[str, Any]:
            import capo_connectscheduling.types.reject_time_off_request

            return (
                capo_connectscheduling.types.reject_time_off_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("RejectTimeOff", redact_input=_redact_input),
        )
        input_: capo_connectscheduling.types.reject_time_off_request.RejectTimeOffRequest = {
            "instance_id": instance_id,
            "user_id": user_id,
            "time_off_id": time_off_id,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

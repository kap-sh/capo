"""Generated from Smithy shape ``com.amazonaws.mturk#MTurkRequesterServiceV20170117``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mturk._auth._signers
import capo_mturk._auth._sigv4
from capo_mturk._auth._identity import Credentials
from capo_mturk._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mturk._auth._zapros_handler import AuthMiddleware
from capo_mturk._pagination import resolve_path as _resolve_path
from capo_mturk._services._aws_config import aws_config
from capo_mturk._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mturk.types.accept_qualification_request_request
    import capo_mturk.types.accept_qualification_request_response
    import capo_mturk.types.approve_assignment_request
    import capo_mturk.types.approve_assignment_response
    import capo_mturk.types.assignment_status_list
    import capo_mturk.types.associate_qualification_with_worker_request
    import capo_mturk.types.associate_qualification_with_worker_response
    import capo_mturk.types.boolean
    import capo_mturk.types.create_additional_assignments_for_hit_request
    import capo_mturk.types.create_additional_assignments_for_hit_response
    import capo_mturk.types.create_hit_request
    import capo_mturk.types.create_hit_response
    import capo_mturk.types.create_hit_type_request
    import capo_mturk.types.create_hit_type_response
    import capo_mturk.types.create_hit_with_hit_type_request
    import capo_mturk.types.create_hit_with_hit_type_response
    import capo_mturk.types.create_qualification_type_request
    import capo_mturk.types.create_qualification_type_response
    import capo_mturk.types.create_worker_block_request
    import capo_mturk.types.create_worker_block_response
    import capo_mturk.types.currency_amount
    import capo_mturk.types.customer_id
    import capo_mturk.types.customer_id_list
    import capo_mturk.types.delete_hit_request
    import capo_mturk.types.delete_hit_response
    import capo_mturk.types.delete_qualification_type_request
    import capo_mturk.types.delete_qualification_type_response
    import capo_mturk.types.delete_worker_block_request
    import capo_mturk.types.delete_worker_block_response
    import capo_mturk.types.disassociate_qualification_from_worker_request
    import capo_mturk.types.disassociate_qualification_from_worker_response
    import capo_mturk.types.entity_id
    import capo_mturk.types.event_type
    import capo_mturk.types.get_account_balance_request
    import capo_mturk.types.get_account_balance_response
    import capo_mturk.types.get_assignment_request
    import capo_mturk.types.get_assignment_response
    import capo_mturk.types.get_file_upload_url_request
    import capo_mturk.types.get_file_upload_url_response
    import capo_mturk.types.get_hit_request
    import capo_mturk.types.get_hit_response
    import capo_mturk.types.get_qualification_score_request
    import capo_mturk.types.get_qualification_score_response
    import capo_mturk.types.get_qualification_type_request
    import capo_mturk.types.get_qualification_type_response
    import capo_mturk.types.hit_layout_parameter_list
    import capo_mturk.types.idempotency_token
    import capo_mturk.types.integer
    import capo_mturk.types.list_assignments_for_hit_request
    import capo_mturk.types.list_assignments_for_hit_response
    import capo_mturk.types.list_bonus_payments_request
    import capo_mturk.types.list_bonus_payments_response
    import capo_mturk.types.list_hi_ts_for_qualification_type_request
    import capo_mturk.types.list_hi_ts_for_qualification_type_response
    import capo_mturk.types.list_hi_ts_request
    import capo_mturk.types.list_hi_ts_response
    import capo_mturk.types.list_qualification_requests_request
    import capo_mturk.types.list_qualification_requests_response
    import capo_mturk.types.list_qualification_types_request
    import capo_mturk.types.list_qualification_types_response
    import capo_mturk.types.list_review_policy_results_for_hit_request
    import capo_mturk.types.list_review_policy_results_for_hit_response
    import capo_mturk.types.list_reviewable_hi_ts_request
    import capo_mturk.types.list_reviewable_hi_ts_response
    import capo_mturk.types.list_worker_blocks_request
    import capo_mturk.types.list_worker_blocks_response
    import capo_mturk.types.list_workers_with_qualification_type_request
    import capo_mturk.types.list_workers_with_qualification_type_response
    import capo_mturk.types.long
    import capo_mturk.types.notification_specification
    import capo_mturk.types.notify_workers_request
    import capo_mturk.types.notify_workers_response
    import capo_mturk.types.pagination_token
    import capo_mturk.types.qualification_requirement_list
    import capo_mturk.types.qualification_status
    import capo_mturk.types.qualification_type_status
    import capo_mturk.types.reject_assignment_request
    import capo_mturk.types.reject_assignment_response
    import capo_mturk.types.reject_qualification_request_request
    import capo_mturk.types.reject_qualification_request_response
    import capo_mturk.types.result_size
    import capo_mturk.types.review_policy
    import capo_mturk.types.review_policy_level_list
    import capo_mturk.types.reviewable_hit_status
    import capo_mturk.types.send_bonus_request
    import capo_mturk.types.send_bonus_response
    import capo_mturk.types.send_test_event_notification_request
    import capo_mturk.types.send_test_event_notification_response
    import capo_mturk.types.string
    import capo_mturk.types.timestamp
    import capo_mturk.types.update_expiration_for_hit_request
    import capo_mturk.types.update_expiration_for_hit_response
    import capo_mturk.types.update_hit_review_status_request
    import capo_mturk.types.update_hit_review_status_response
    import capo_mturk.types.update_hit_type_of_hit_request
    import capo_mturk.types.update_hit_type_of_hit_response
    import capo_mturk.types.update_notification_settings_request
    import capo_mturk.types.update_notification_settings_response
    import capo_mturk.types.update_qualification_type_request
    import capo_mturk.types.update_qualification_type_response


class MTurkClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MTurkClient:
    """A client for the ``MTurk`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        anonymous: bool | None = None,
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
        self._config = MTurkClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MTurkClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MTurkClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def accept_qualification_request(
        self,
        qualification_request_id: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        integer_value: Optional["capo_mturk.types.integer.Integer"] = None,
    ) -> "capo_mturk.types.accept_qualification_request_response.AcceptQualificationRequestResponse":
        """<p> The <code>AcceptQualificationRequest</code> operation approves a Worker's request for a Qualification. </p> <p> Only the owner of the Qualification type can grant a Qualification request for that type. </p> <p> A successful request for the <code>AcceptQualificationRequest</code> operation returns with no errors and an empty body. </p>

        Args:
            qualification_request_id: <p>The ID of the Qualification request, as returned by the <code>GetQualificationRequests</code> operation.</p>
            integer_value: <p> The value of the Qualification. You can omit this value if you are using the presence or absence of the Qualification as the basis for a HIT requirement. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.accept_qualification_request_request.AcceptQualificationRequestRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.accept_qualification_request_response.AcceptQualificationRequestResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.accept_qualification_request

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.accept_qualification_request.accept_qualification_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.accept_qualification_request_request.AcceptQualificationRequestRequest = {
            "qualification_request_id": qualification_request_id
        }
        if integer_value is not None:
            input_["integer_value"] = integer_value

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def approve_assignment(
        self,
        assignment_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        requester_feedback: Optional["capo_mturk.types.string.String"] = None,
        override_rejection: Optional["capo_mturk.types.boolean.Boolean"] = None,
    ) -> "capo_mturk.types.approve_assignment_response.ApproveAssignmentResponse":
        """<p> The <code>ApproveAssignment</code> operation approves the results of a completed assignment. </p> <p> Approving an assignment initiates two payments from the Requester's Amazon.com account </p> <ul> <li> <p> The Worker who submitted the results is paid the reward specified in the HIT. </p> </li> <li> <p> Amazon Mechanical Turk fees are debited. </p> </li> </ul> <p> If the Requester's account does not have adequate funds for these payments, the call to ApproveAssignment returns an exception, and the approval is not processed. You can include an optional feedback message with the approval, which the Worker can see in the Status section of the web site. </p> <p> You can also call this operation for assignments that were previous rejected and approve them by explicitly overriding the previous rejection. This only works on rejected assignments that were submitted within the previous 30 days and only if the assignment's related HIT has not been deleted. </p>

        Args:
            assignment_id: <p> The ID of the assignment. The assignment must correspond to a HIT created by the Requester. </p>
            requester_feedback: <p> A message for the Worker, which the Worker can see in the Status section of the web site. </p>
            override_rejection: <p> A flag indicating that an assignment should be approved even if it was previously rejected. Defaults to <code>False</code>. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.approve_assignment_request.ApproveAssignmentRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.approve_assignment_response.ApproveAssignmentResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.approve_assignment

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.approve_assignment.approve_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.approve_assignment_request.ApproveAssignmentRequest = {
            "assignment_id": assignment_id
        }
        if requester_feedback is not None:
            input_["requester_feedback"] = requester_feedback
        if override_rejection is not None:
            input_["override_rejection"] = override_rejection

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_qualification_with_worker(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        worker_id: "capo_mturk.types.customer_id.CustomerId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        integer_value: Optional["capo_mturk.types.integer.Integer"] = None,
        send_notification: Optional["capo_mturk.types.boolean.Boolean"] = None,
    ) -> "capo_mturk.types.associate_qualification_with_worker_response.AssociateQualificationWithWorkerResponse":
        """<p> The <code>AssociateQualificationWithWorker</code> operation gives a Worker a Qualification. <code>AssociateQualificationWithWorker</code> does not require that the Worker submit a Qualification request. It gives the Qualification directly to the Worker. </p> <p> You can only assign a Qualification of a Qualification type that you created (using the <code>CreateQualificationType</code> operation). </p> <note> <p> Note: <code>AssociateQualificationWithWorker</code> does not affect any pending Qualification requests for the Qualification by the Worker. If you assign a Qualification to a Worker, then later grant a Qualification request made by the Worker, the granting of the request may modify the Qualification score. To resolve a pending Qualification request without affecting the Qualification the Worker already has, reject the request with the <code>RejectQualificationRequest</code> operation. </p> </note>

        Args:
            qualification_type_id: <p>The ID of the Qualification type to use for the assigned Qualification.</p>
            worker_id: <p> The ID of the Worker to whom the Qualification is being assigned. Worker IDs are included with submitted HIT assignments and Qualification requests. </p>
            integer_value: <p>The value of the Qualification to assign.</p>
            send_notification: <p> Specifies whether to send a notification email message to the Worker saying that the qualification was assigned to the Worker. Note: this is true by default. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.associate_qualification_with_worker_request.AssociateQualificationWithWorkerRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.associate_qualification_with_worker_response.AssociateQualificationWithWorkerResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.associate_qualification_with_worker

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.associate_qualification_with_worker.associate_qualification_with_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.associate_qualification_with_worker_request.AssociateQualificationWithWorkerRequest = {
            "qualification_type_id": qualification_type_id,
            "worker_id": worker_id,
        }
        if integer_value is not None:
            input_["integer_value"] = integer_value
        if send_notification is not None:
            input_["send_notification"] = send_notification

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_additional_assignments_for_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        number_of_additional_assignments: "capo_mturk.types.integer.Integer",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        unique_request_token: Optional[
            "capo_mturk.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_mturk.types.create_additional_assignments_for_hit_response.CreateAdditionalAssignmentsForHITResponse":
        """<p> The <code>CreateAdditionalAssignmentsForHIT</code> operation increases the maximum number of assignments of an existing HIT. </p> <p> To extend the maximum number of assignments, specify the number of additional assignments.</p> <note> <ul> <li> <p>HITs created with fewer than 10 assignments cannot be extended to have 10 or more assignments. Attempting to add assignments in a way that brings the total number of assignments for a HIT from fewer than 10 assignments to 10 or more assignments will result in an <code>AWS.MechanicalTurk.InvalidMaximumAssignmentsIncrease</code> exception.</p> </li> <li> <p>HITs that were created before July 22, 2015 cannot be extended. Attempting to extend HITs that were created before July 22, 2015 will result in an <code>AWS.MechanicalTurk.HITTooOldForExtension</code> exception. </p> </li> </ul> </note>

        Args:
            hit_id: <p>The ID of the HIT to extend.</p>
            number_of_additional_assignments: <p>The number of additional assignments to request for this HIT.</p>
            unique_request_token: <p> A unique identifier for this request, which allows you to retry the call on error without extending the HIT multiple times. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the extend HIT already exists in the system from a previous call using the same <code>UniqueRequestToken</code>, subsequent calls will return an error with a message containing the request ID. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.create_additional_assignments_for_hit_request.CreateAdditionalAssignmentsForHITRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.create_additional_assignments_for_hit_response.CreateAdditionalAssignmentsForHITResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.create_additional_assignments_for_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.create_additional_assignments_for_hit.create_additional_assignments_for_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.create_additional_assignments_for_hit_request.CreateAdditionalAssignmentsForHITRequest = {
            "hit_id": hit_id,
            "number_of_additional_assignments": number_of_additional_assignments,
        }
        if unique_request_token is not None:
            input_["unique_request_token"] = unique_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_hit(
        self,
        lifetime_in_seconds: "capo_mturk.types.long.Long",
        assignment_duration_in_seconds: "capo_mturk.types.long.Long",
        reward: "capo_mturk.types.currency_amount.CurrencyAmount",
        title: "capo_mturk.types.string.String",
        description: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        max_assignments: Optional["capo_mturk.types.integer.Integer"] = None,
        auto_approval_delay_in_seconds: Optional["capo_mturk.types.long.Long"] = None,
        keywords: Optional["capo_mturk.types.string.String"] = None,
        question: Optional["capo_mturk.types.string.String"] = None,
        requester_annotation: Optional["capo_mturk.types.string.String"] = None,
        qualification_requirements: Optional[
            "capo_mturk.types.qualification_requirement_list.QualificationRequirementList"
        ] = None,
        unique_request_token: Optional[
            "capo_mturk.types.idempotency_token.IdempotencyToken"
        ] = None,
        assignment_review_policy: Optional[
            "capo_mturk.types.review_policy.ReviewPolicy"
        ] = None,
        hit_review_policy: Optional[
            "capo_mturk.types.review_policy.ReviewPolicy"
        ] = None,
        hit_layout_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        hit_layout_parameters: Optional[
            "capo_mturk.types.hit_layout_parameter_list.HITLayoutParameterList"
        ] = None,
    ) -> "capo_mturk.types.create_hit_response.CreateHITResponse":
        """<p>The <code>CreateHIT</code> operation creates a new Human Intelligence Task (HIT). The new HIT is made available for Workers to find and accept on the Amazon Mechanical Turk website. </p> <p> This operation allows you to specify a new HIT by passing in values for the properties of the HIT, such as its title, reward amount and number of assignments. When you pass these values to <code>CreateHIT</code>, a new HIT is created for you, with a new <code>HITTypeID</code>. The HITTypeID can be used to create additional HITs in the future without needing to specify common parameters such as the title, description and reward amount each time.</p> <p> An alternative way to create HITs is to first generate a HITTypeID using the <code>CreateHITType</code> operation and then call the <code>CreateHITWithHITType</code> operation. This is the recommended best practice for Requesters who are creating large numbers of HITs. </p> <p>CreateHIT also supports several ways to provide question data: by providing a value for the <code>Question</code> parameter that fully specifies the contents of the HIT, or by providing a <code>HitLayoutId</code> and associated <code>HitLayoutParameters</code>. </p> <note> <p> If a HIT is created with 10 or more maximum assignments, there is an additional fee. For more information, see <a href="https://requester.mturk.com/pricing">Amazon Mechanical Turk Pricing</a>.</p> </note>

        Args:
            max_assignments: <p> The number of times the HIT can be accepted and completed before the HIT becomes unavailable. </p>
            auto_approval_delay_in_seconds: <p> The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered Approved automatically unless the Requester explicitly rejects it. </p>
            lifetime_in_seconds: <p> An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted. </p>
            assignment_duration_in_seconds: <p> The amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept. </p>
            reward: <p> The amount of money the Requester will pay a Worker for successfully completing the HIT. </p>
            title: <p> The title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned. </p>
            keywords: <p> One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs. </p>
            description: <p> A general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it. </p>
            question: <p> The data the person completing the HIT uses to produce the results. </p> <p> Constraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace. </p> <p>Either a Question parameter or a HITLayoutId parameter must be provided.</p>
            requester_annotation: <p> An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester's application that corresponds with the HIT. </p> <p> The RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester. </p> <p> The RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped. </p>
            qualification_requirements: <p> Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the <code>ActionsGuarded</code> field on each <code>QualificationRequirement</code> structure. </p>
            unique_request_token: <p> A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId. </p> <note> <p> Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs. </p> </note>
            assignment_review_policy: <p> The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy. </p>
            hit_review_policy: <p> The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy. </p>
            hit_layout_id: <p> The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters. </p> <p> Constraints: Either a Question parameter or a HITLayoutId parameter must be provided. </p>
            hit_layout_parameters: <p> If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.create_hit_request.CreateHITRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.create_hit_response.CreateHITResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.create_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.create_hit.create_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.create_hit_request.CreateHITRequest = {
            "lifetime_in_seconds": lifetime_in_seconds,
            "assignment_duration_in_seconds": assignment_duration_in_seconds,
            "reward": reward,
            "title": title,
            "description": description,
        }
        if max_assignments is not None:
            input_["max_assignments"] = max_assignments
        if auto_approval_delay_in_seconds is not None:
            input_["auto_approval_delay_in_seconds"] = auto_approval_delay_in_seconds
        if keywords is not None:
            input_["keywords"] = keywords
        if question is not None:
            input_["question"] = question
        if requester_annotation is not None:
            input_["requester_annotation"] = requester_annotation
        if qualification_requirements is not None:
            input_["qualification_requirements"] = qualification_requirements
        if unique_request_token is not None:
            input_["unique_request_token"] = unique_request_token
        if assignment_review_policy is not None:
            input_["assignment_review_policy"] = assignment_review_policy
        if hit_review_policy is not None:
            input_["hit_review_policy"] = hit_review_policy
        if hit_layout_id is not None:
            input_["hit_layout_id"] = hit_layout_id
        if hit_layout_parameters is not None:
            input_["hit_layout_parameters"] = hit_layout_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_hit_type(
        self,
        assignment_duration_in_seconds: "capo_mturk.types.long.Long",
        reward: "capo_mturk.types.currency_amount.CurrencyAmount",
        title: "capo_mturk.types.string.String",
        description: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        auto_approval_delay_in_seconds: Optional["capo_mturk.types.long.Long"] = None,
        keywords: Optional["capo_mturk.types.string.String"] = None,
        qualification_requirements: Optional[
            "capo_mturk.types.qualification_requirement_list.QualificationRequirementList"
        ] = None,
    ) -> "capo_mturk.types.create_hit_type_response.CreateHITTypeResponse":
        """<p> The <code>CreateHITType</code> operation creates a new HIT type. This operation allows you to define a standard set of HIT properties to use when creating HITs. If you register a HIT type with values that match an existing HIT type, the HIT type ID of the existing type will be returned. </p>

        Args:
            auto_approval_delay_in_seconds: <p> The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered Approved automatically unless the Requester explicitly rejects it. </p>
            assignment_duration_in_seconds: <p> The amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept. </p>
            reward: <p> The amount of money the Requester will pay a Worker for successfully completing the HIT. </p>
            title: <p> The title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned. </p>
            keywords: <p> One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs. </p>
            description: <p> A general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it. </p>
            qualification_requirements: <p> Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the <code>ActionsGuarded</code> field on each <code>QualificationRequirement</code> structure. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.create_hit_type_request.CreateHITTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.create_hit_type_response.CreateHITTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.create_hit_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.create_hit_type.create_hit_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.create_hit_type_request.CreateHITTypeRequest = {
            "assignment_duration_in_seconds": assignment_duration_in_seconds,
            "reward": reward,
            "title": title,
            "description": description,
        }
        if auto_approval_delay_in_seconds is not None:
            input_["auto_approval_delay_in_seconds"] = auto_approval_delay_in_seconds
        if keywords is not None:
            input_["keywords"] = keywords
        if qualification_requirements is not None:
            input_["qualification_requirements"] = qualification_requirements

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_hit_with_hit_type(
        self,
        hit_type_id: "capo_mturk.types.entity_id.EntityId",
        lifetime_in_seconds: "capo_mturk.types.long.Long",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        max_assignments: Optional["capo_mturk.types.integer.Integer"] = None,
        question: Optional["capo_mturk.types.string.String"] = None,
        requester_annotation: Optional["capo_mturk.types.string.String"] = None,
        unique_request_token: Optional[
            "capo_mturk.types.idempotency_token.IdempotencyToken"
        ] = None,
        assignment_review_policy: Optional[
            "capo_mturk.types.review_policy.ReviewPolicy"
        ] = None,
        hit_review_policy: Optional[
            "capo_mturk.types.review_policy.ReviewPolicy"
        ] = None,
        hit_layout_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        hit_layout_parameters: Optional[
            "capo_mturk.types.hit_layout_parameter_list.HITLayoutParameterList"
        ] = None,
    ) -> "capo_mturk.types.create_hit_with_hit_type_response.CreateHITWithHITTypeResponse":
        """<p> The <code>CreateHITWithHITType</code> operation creates a new Human Intelligence Task (HIT) using an existing HITTypeID generated by the <code>CreateHITType</code> operation. </p> <p> This is an alternative way to create HITs from the <code>CreateHIT</code> operation. This is the recommended best practice for Requesters who are creating large numbers of HITs. </p> <p>CreateHITWithHITType also supports several ways to provide question data: by providing a value for the <code>Question</code> parameter that fully specifies the contents of the HIT, or by providing a <code>HitLayoutId</code> and associated <code>HitLayoutParameters</code>. </p> <note> <p> If a HIT is created with 10 or more maximum assignments, there is an additional fee. For more information, see <a href="https://requester.mturk.com/pricing">Amazon Mechanical Turk Pricing</a>. </p> </note>

        Args:
            hit_type_id: <p>The HIT type ID you want to create this HIT with.</p>
            max_assignments: <p> The number of times the HIT can be accepted and completed before the HIT becomes unavailable. </p>
            lifetime_in_seconds: <p> An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted. </p>
            question: <p> The data the person completing the HIT uses to produce the results. </p> <p> Constraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace. </p> <p>Either a Question parameter or a HITLayoutId parameter must be provided.</p>
            requester_annotation: <p> An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester's application that corresponds with the HIT. </p> <p> The RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester. </p> <p> The RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped. </p>
            unique_request_token: <p> A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId. </p> <note> <p> Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs. </p> </note>
            assignment_review_policy: <p> The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy. </p>
            hit_review_policy: <p> The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy. </p>
            hit_layout_id: <p> The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters. </p> <p> Constraints: Either a Question parameter or a HITLayoutId parameter must be provided. </p>
            hit_layout_parameters: <p> If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.create_hit_with_hit_type_request.CreateHITWithHITTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.create_hit_with_hit_type_response.CreateHITWithHITTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.create_hit_with_hit_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.create_hit_with_hit_type.create_hit_with_hit_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.create_hit_with_hit_type_request.CreateHITWithHITTypeRequest = {
            "hit_type_id": hit_type_id,
            "lifetime_in_seconds": lifetime_in_seconds,
        }
        if max_assignments is not None:
            input_["max_assignments"] = max_assignments
        if question is not None:
            input_["question"] = question
        if requester_annotation is not None:
            input_["requester_annotation"] = requester_annotation
        if unique_request_token is not None:
            input_["unique_request_token"] = unique_request_token
        if assignment_review_policy is not None:
            input_["assignment_review_policy"] = assignment_review_policy
        if hit_review_policy is not None:
            input_["hit_review_policy"] = hit_review_policy
        if hit_layout_id is not None:
            input_["hit_layout_id"] = hit_layout_id
        if hit_layout_parameters is not None:
            input_["hit_layout_parameters"] = hit_layout_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_qualification_type(
        self,
        name: "capo_mturk.types.string.String",
        description: "capo_mturk.types.string.String",
        qualification_type_status: "capo_mturk.types.qualification_type_status.QualificationTypeStatus",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        keywords: Optional["capo_mturk.types.string.String"] = None,
        retry_delay_in_seconds: Optional["capo_mturk.types.long.Long"] = None,
        test: Optional["capo_mturk.types.string.String"] = None,
        answer_key: Optional["capo_mturk.types.string.String"] = None,
        test_duration_in_seconds: Optional["capo_mturk.types.long.Long"] = None,
        auto_granted: Optional["capo_mturk.types.boolean.Boolean"] = None,
        auto_granted_value: Optional["capo_mturk.types.integer.Integer"] = None,
    ) -> "capo_mturk.types.create_qualification_type_response.CreateQualificationTypeResponse":
        """<p> The <code>CreateQualificationType</code> operation creates a new Qualification type, which is represented by a <code>QualificationType</code> data structure. </p>

        Args:
            name: <p> The name you give to the Qualification type. The type name is used to represent the Qualification to Workers, and to find the type using a Qualification type search. It must be unique across all of your Qualification types.</p>
            keywords: <p>One or more words or phrases that describe the Qualification type, separated by commas. The keywords of a type make the type easier to find during a search.</p>
            description: <p>A long description for the Qualification type. On the Amazon Mechanical Turk website, the long description is displayed when a Worker examines a Qualification type.</p>
            qualification_type_status: <p>The initial status of the Qualification type.</p> <p>Constraints: Valid values are: Active | Inactive</p>
            retry_delay_in_seconds: <p>The number of seconds that a Worker must wait after requesting a Qualification of the Qualification type before the worker can retry the Qualification request.</p> <p>Constraints: None. If not specified, retries are disabled and Workers can request a Qualification of this type only once, even if the Worker has not been granted the Qualification. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must delete existing retry-enabled Qualification type and then create a new Qualification type with retries disabled.</p>
            test: <p> The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, <code>TestDurationInSeconds</code> must also be specified. </p> <p>Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.</p> <p>Constraints: None. If not specified, the Worker may request the Qualification without answering any questions.</p>
            answer_key: <p>The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.</p> <p>Constraints: Must not be longer than 65535 bytes.</p> <p>Constraints: None. If not specified, you must process Qualification requests manually.</p>
            test_duration_in_seconds: <p>The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.</p>
            auto_granted: <p>Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.</p> <p>Constraints: If the Test parameter is specified, this parameter cannot be true.</p>
            auto_granted_value: <p>The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.create_qualification_type_request.CreateQualificationTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.create_qualification_type_response.CreateQualificationTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.create_qualification_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.create_qualification_type.create_qualification_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.create_qualification_type_request.CreateQualificationTypeRequest = {
            "name": name,
            "description": description,
            "qualification_type_status": qualification_type_status,
        }
        if keywords is not None:
            input_["keywords"] = keywords
        if retry_delay_in_seconds is not None:
            input_["retry_delay_in_seconds"] = retry_delay_in_seconds
        if test is not None:
            input_["test"] = test
        if answer_key is not None:
            input_["answer_key"] = answer_key
        if test_duration_in_seconds is not None:
            input_["test_duration_in_seconds"] = test_duration_in_seconds
        if auto_granted is not None:
            input_["auto_granted"] = auto_granted
        if auto_granted_value is not None:
            input_["auto_granted_value"] = auto_granted_value

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_worker_block(
        self,
        worker_id: "capo_mturk.types.customer_id.CustomerId",
        reason: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.create_worker_block_response.CreateWorkerBlockResponse":
        """<p>The <code>CreateWorkerBlock</code> operation allows you to prevent a Worker from working on your HITs. For example, you can block a Worker who is producing poor quality work. You can block up to 100,000 Workers.</p>

        Args:
            worker_id: <p>The ID of the Worker to block.</p>
            reason: <p>A message explaining the reason for blocking the Worker. This parameter enables you to keep track of your Workers. The Worker does not see this message.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.create_worker_block_request.CreateWorkerBlockRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.create_worker_block_response.CreateWorkerBlockResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.create_worker_block

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.create_worker_block.create_worker_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.create_worker_block_request.CreateWorkerBlockRequest = {
            "worker_id": worker_id,
            "reason": reason,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.delete_hit_response.DeleteHITResponse":
        """<p> The <code>DeleteHIT</code> operation is used to delete HIT that is no longer needed. Only the Requester who created the HIT can delete it. </p> <p> You can only dispose of HITs that are in the <code>Reviewable</code> state, with all of their submitted assignments already either approved or rejected. If you call the DeleteHIT operation on a HIT that is not in the <code>Reviewable</code> state (for example, that has not expired, or still has active assignments), or on a HIT that is Reviewable but without all of its submitted assignments already approved or rejected, the service will return an error. </p> <note> <ul> <li> <p> HITs are automatically disposed of after 120 days. </p> </li> <li> <p> After you dispose of a HIT, you can no longer approve the HIT's rejected assignments. </p> </li> <li> <p> Disposed HITs are not returned in results for the ListHITs operation. </p> </li> <li> <p> Disposing HITs can improve the performance of operations such as ListReviewableHITs and ListHITs. </p> </li> </ul> </note>

        Args:
            hit_id: <p>The ID of the HIT to be deleted.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.delete_hit_request.DeleteHITRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.delete_hit_response.DeleteHITResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.delete_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.delete_hit.delete_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.delete_hit_request.DeleteHITRequest = {
            "hit_id": hit_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_qualification_type(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.delete_qualification_type_response.DeleteQualificationTypeResponse":
        """<p> The <code>DeleteQualificationType</code> deletes a Qualification type and deletes any HIT types that are associated with the Qualification type. </p> <p>This operation does not revoke Qualifications already assigned to Workers because the Qualifications might be needed for active HITs. If there are any pending requests for the Qualification type, Amazon Mechanical Turk rejects those requests. After you delete a Qualification type, you can no longer use it to create HITs or HIT types.</p> <note> <p>DeleteQualificationType must wait for all the HITs that use the deleted Qualification type to be deleted before completing. It may take up to 48 hours before DeleteQualificationType completes and the unique name of the Qualification type is available for reuse with CreateQualificationType.</p> </note>

        Args:
            qualification_type_id: <p>The ID of the QualificationType to dispose.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.delete_qualification_type_request.DeleteQualificationTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.delete_qualification_type_response.DeleteQualificationTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.delete_qualification_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.delete_qualification_type.delete_qualification_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.delete_qualification_type_request.DeleteQualificationTypeRequest = {
            "qualification_type_id": qualification_type_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_worker_block(
        self,
        worker_id: "capo_mturk.types.customer_id.CustomerId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        reason: Optional["capo_mturk.types.string.String"] = None,
    ) -> "capo_mturk.types.delete_worker_block_response.DeleteWorkerBlockResponse":
        """<p>The <code>DeleteWorkerBlock</code> operation allows you to reinstate a blocked Worker to work on your HITs. This operation reverses the effects of the CreateWorkerBlock operation. You need the Worker ID to use this operation. If the Worker ID is missing or invalid, this operation fails and returns the message “WorkerId is invalid.” If the specified Worker is not blocked, this operation returns successfully.</p>

        Args:
            worker_id: <p>The ID of the Worker to unblock.</p>
            reason: <p>A message that explains the reason for unblocking the Worker. The Worker does not see this message.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.delete_worker_block_request.DeleteWorkerBlockRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.delete_worker_block_response.DeleteWorkerBlockResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.delete_worker_block

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.delete_worker_block.delete_worker_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.delete_worker_block_request.DeleteWorkerBlockRequest = {
            "worker_id": worker_id
        }
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_qualification_from_worker(
        self,
        worker_id: "capo_mturk.types.customer_id.CustomerId",
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        reason: Optional["capo_mturk.types.string.String"] = None,
    ) -> "capo_mturk.types.disassociate_qualification_from_worker_response.DisassociateQualificationFromWorkerResponse":
        """<p> The <code>DisassociateQualificationFromWorker</code> revokes a previously granted Qualification from a user. </p> <p> You can provide a text message explaining why the Qualification was revoked. The user who had the Qualification can see this message. </p>

        Args:
            worker_id: <p>The ID of the Worker who possesses the Qualification to be revoked.</p>
            qualification_type_id: <p>The ID of the Qualification type of the Qualification to be revoked.</p>
            reason: <p>A text message that explains why the Qualification was revoked. The user who had the Qualification sees this message.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.disassociate_qualification_from_worker_request.DisassociateQualificationFromWorkerRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.disassociate_qualification_from_worker_response.DisassociateQualificationFromWorkerResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.disassociate_qualification_from_worker

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.disassociate_qualification_from_worker.disassociate_qualification_from_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.disassociate_qualification_from_worker_request.DisassociateQualificationFromWorkerRequest = {
            "worker_id": worker_id,
            "qualification_type_id": qualification_type_id,
        }
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_balance(
        self, *, config_overrides: Optional[MTurkClientConfig] = None
    ) -> "capo_mturk.types.get_account_balance_response.GetAccountBalanceResponse":
        """<p>The <code>GetAccountBalance</code> operation retrieves the Prepaid HITs balance in your Amazon Mechanical Turk account if you are a Prepaid Requester. Alternatively, this operation will retrieve the remaining available AWS Billing usage if you have enabled AWS Billing. Note: If you have enabled AWS Billing and still have a remaining Prepaid HITs balance, this balance can be viewed on the My Account page in the Requester console.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.get_account_balance_request.GetAccountBalanceRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.get_account_balance_response.GetAccountBalanceResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.get_account_balance

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.get_account_balance.get_account_balance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.get_account_balance_request.GetAccountBalanceRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_assignment(
        self,
        assignment_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.get_assignment_response.GetAssignmentResponse":
        """<p> The <code>GetAssignment</code> operation retrieves the details of the specified Assignment. </p>

        Args:
            assignment_id: <p>The ID of the Assignment to be retrieved.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.get_assignment_request.GetAssignmentRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.get_assignment_response.GetAssignmentResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.get_assignment

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.get_assignment.get_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.get_assignment_request.GetAssignmentRequest = {
            "assignment_id": assignment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_file_upload_url(
        self,
        assignment_id: "capo_mturk.types.entity_id.EntityId",
        question_identifier: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.get_file_upload_url_response.GetFileUploadURLResponse":
        """<p> The <code>GetFileUploadURL</code> operation generates and returns a temporary URL. You use the temporary URL to retrieve a file uploaded by a Worker as an answer to a FileUploadAnswer question for a HIT. The temporary URL is generated the instant the GetFileUploadURL operation is called, and is valid for 60 seconds. You can get a temporary file upload URL any time until the HIT is disposed. After the HIT is disposed, any uploaded files are deleted, and cannot be retrieved. Pending Deprecation on December 12, 2017. The Answer Specification structure will no longer support the <code>FileUploadAnswer</code> element to be used for the QuestionForm data structure. Instead, we recommend that Requesters who want to create HITs asking Workers to upload files to use Amazon S3. </p>

        Args:
            assignment_id: <p>The ID of the assignment that contains the question with a FileUploadAnswer.</p>
            question_identifier: <p>The identifier of the question with a FileUploadAnswer, as specified in the QuestionForm of the HIT.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.get_file_upload_url_request.GetFileUploadURLRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.get_file_upload_url_response.GetFileUploadURLResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.get_file_upload_url

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.get_file_upload_url.get_file_upload_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.get_file_upload_url_request.GetFileUploadURLRequest = {
            "assignment_id": assignment_id,
            "question_identifier": question_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.get_hit_response.GetHITResponse":
        """<p> The <code>GetHIT</code> operation retrieves the details of the specified HIT. </p>

        Args:
            hit_id: <p>The ID of the HIT to be retrieved.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.get_hit_request.GetHITRequest]",
        ) -> OperationResponse["capo_mturk.types.get_hit_response.GetHITResponse"]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.get_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.get_hit.get_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.get_hit_request.GetHITRequest = {"hit_id": hit_id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_qualification_score(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        worker_id: "capo_mturk.types.customer_id.CustomerId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.get_qualification_score_response.GetQualificationScoreResponse":
        """<p> The <code>GetQualificationScore</code> operation returns the value of a Worker's Qualification for a given Qualification type. </p> <p> To get a Worker's Qualification, you must know the Worker's ID. The Worker's ID is included in the assignment data returned by the <code>ListAssignmentsForHIT</code> operation. </p> <p>Only the owner of a Qualification type can query the value of a Worker's Qualification of that type.</p>

        Args:
            qualification_type_id: <p>The ID of the QualificationType.</p>
            worker_id: <p>The ID of the Worker whose Qualification is being updated.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.get_qualification_score_request.GetQualificationScoreRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.get_qualification_score_response.GetQualificationScoreResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.get_qualification_score

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.get_qualification_score.get_qualification_score(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.get_qualification_score_request.GetQualificationScoreRequest = {
            "qualification_type_id": qualification_type_id,
            "worker_id": worker_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_qualification_type(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> (
        "capo_mturk.types.get_qualification_type_response.GetQualificationTypeResponse"
    ):
        """<p> The <code>GetQualificationType</code>operation retrieves information about a Qualification type using its ID. </p>

        Args:
            qualification_type_id: <p>The ID of the QualificationType.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.get_qualification_type_request.GetQualificationTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.get_qualification_type_response.GetQualificationTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.get_qualification_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.get_qualification_type.get_qualification_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.get_qualification_type_request.GetQualificationTypeRequest = {
            "qualification_type_id": qualification_type_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_assignments_for_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
        assignment_statuses: Optional[
            "capo_mturk.types.assignment_status_list.AssignmentStatusList"
        ] = None,
    ) -> "capo_mturk.types.list_assignments_for_hit_response.ListAssignmentsForHITResponse":
        """<p> The <code>ListAssignmentsForHIT</code> operation retrieves completed assignments for a HIT. You can use this operation to retrieve the results for a HIT. </p> <p> You can get assignments for a HIT at any time, even if the HIT is not yet Reviewable. If a HIT requested multiple assignments, and has received some results but has not yet become Reviewable, you can still retrieve the partial results with this operation. </p> <p> Use the AssignmentStatus parameter to control which set of assignments for a HIT are returned. The ListAssignmentsForHIT operation can return submitted assignments awaiting approval, or it can return assignments that have already been approved or rejected. You can set AssignmentStatus=Approved,Rejected to get assignments that have already been approved and rejected together in one result set. </p> <p> Only the Requester who created the HIT can retrieve the assignments for that HIT. </p> <p> Results are sorted and divided into numbered pages and the operation returns a single page of results. You can use the parameters of the operation to control sorting and pagination. </p>

        Args:
            hit_id: <p>The ID of the HIT.</p>
            next_token: <p>Pagination token</p>
            assignment_statuses: <p>The status of the assignments to return: Submitted | Approved | Rejected</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_assignments_for_hit_request.ListAssignmentsForHITRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_assignments_for_hit_response.ListAssignmentsForHITResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_assignments_for_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_assignments_for_hit.list_assignments_for_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_assignments_for_hit_request.ListAssignmentsForHITRequest = {
            "hit_id": hit_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if assignment_statuses is not None:
            input_["assignment_statuses"] = assignment_statuses

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_assignments_for_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
        assignment_statuses: Optional[
            "capo_mturk.types.assignment_status_list.AssignmentStatusList"
        ] = None,
    ) -> "Iterator[capo_mturk.types.list_assignments_for_hit_response.ListAssignmentsForHITResponse]":
        _token = next_token
        while True:
            _response = self.list_assignments_for_hit(
                hit_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                assignment_statuses=assignment_statuses,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_bonus_payments(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        hit_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        assignment_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_bonus_payments_response.ListBonusPaymentsResponse":
        """<p> The <code>ListBonusPayments</code> operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment. </p>

        Args:
            hit_id: <p>The ID of the HIT associated with the bonus payments to retrieve. If not specified, all bonus payments for all assignments for the given HIT are returned. Either the HITId parameter or the AssignmentId parameter must be specified</p>
            assignment_id: <p>The ID of the assignment associated with the bonus payments to retrieve. If specified, only bonus payments for the given assignment are returned. Either the HITId parameter or the AssignmentId parameter must be specified</p>
            next_token: <p>Pagination token</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_bonus_payments_request.ListBonusPaymentsRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_bonus_payments_response.ListBonusPaymentsResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_bonus_payments

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_bonus_payments.list_bonus_payments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_bonus_payments_request.ListBonusPaymentsRequest = {}
        if hit_id is not None:
            input_["hit_id"] = hit_id
        if assignment_id is not None:
            input_["assignment_id"] = assignment_id
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

    def iter_list_bonus_payments(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        hit_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        assignment_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_bonus_payments_response.ListBonusPaymentsResponse]":
        _token = next_token
        while True:
            _response = self.list_bonus_payments(
                config_overrides=config_overrides,
                hit_id=hit_id,
                assignment_id=assignment_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_hi_ts(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_hi_ts_response.ListHITsResponse":
        """<p> The <code>ListHITs</code> operation returns all of a Requester's HITs. The operation returns HITs of any status, except for HITs that have been deleted of with the DeleteHIT operation or that have been auto-deleted. </p>

        Args:
            next_token: <p>Pagination token</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_hi_ts_request.ListHITsRequest]",
        ) -> OperationResponse["capo_mturk.types.list_hi_ts_response.ListHITsResponse"]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_hi_ts

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_hi_ts.list_hi_ts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_hi_ts_request.ListHITsRequest = {}
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

    def iter_list_hi_ts(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_hi_ts_response.ListHITsResponse]":
        _token = next_token
        while True:
            _response = self.list_hi_ts(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_hi_ts_for_qualification_type(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_hi_ts_for_qualification_type_response.ListHITsForQualificationTypeResponse":
        """<p> The <code>ListHITsForQualificationType</code> operation returns the HITs that use the given Qualification type for a Qualification requirement. The operation returns HITs of any status, except for HITs that have been deleted with the <code>DeleteHIT</code> operation or that have been auto-deleted. </p>

        Args:
            qualification_type_id: <p> The ID of the Qualification type to use when querying HITs. </p>
            next_token: <p>Pagination Token</p>
            max_results: <p> Limit the number of results returned. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_hi_ts_for_qualification_type_request.ListHITsForQualificationTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_hi_ts_for_qualification_type_response.ListHITsForQualificationTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_hi_ts_for_qualification_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_hi_ts_for_qualification_type.list_hi_ts_for_qualification_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_hi_ts_for_qualification_type_request.ListHITsForQualificationTypeRequest = {
            "qualification_type_id": qualification_type_id
        }
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

    def iter_list_hi_ts_for_qualification_type(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_hi_ts_for_qualification_type_response.ListHITsForQualificationTypeResponse]":
        _token = next_token
        while True:
            _response = self.list_hi_ts_for_qualification_type(
                qualification_type_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_qualification_requests(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        qualification_type_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_qualification_requests_response.ListQualificationRequestsResponse":
        """<p> The <code>ListQualificationRequests</code> operation retrieves requests for Qualifications of a particular Qualification type. The owner of the Qualification type calls this operation to poll for pending requests, and accepts them using the AcceptQualification operation. </p>

        Args:
            qualification_type_id: <p>The ID of the QualificationType.</p>
            max_results: <p> The maximum number of results to return in a single call. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_qualification_requests_request.ListQualificationRequestsRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_qualification_requests_response.ListQualificationRequestsResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_qualification_requests

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_qualification_requests.list_qualification_requests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_qualification_requests_request.ListQualificationRequestsRequest = {}
        if qualification_type_id is not None:
            input_["qualification_type_id"] = qualification_type_id
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

    def iter_list_qualification_requests(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        qualification_type_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_qualification_requests_response.ListQualificationRequestsResponse]":
        _token = next_token
        while True:
            _response = self.list_qualification_requests(
                config_overrides=config_overrides,
                qualification_type_id=qualification_type_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_qualification_types(
        self,
        must_be_requestable: "capo_mturk.types.boolean.Boolean",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        query: Optional["capo_mturk.types.string.String"] = None,
        must_be_owned_by_caller: Optional["capo_mturk.types.boolean.Boolean"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_qualification_types_response.ListQualificationTypesResponse":
        """<p> The <code>ListQualificationTypes</code> operation returns a list of Qualification types, filtered by an optional search term. </p>

        Args:
            query: <p> A text query against all of the searchable attributes of Qualification types. </p>
            must_be_requestable: <p>Specifies that only Qualification types that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test, are returned as results of the search. Some Qualification types, such as those assigned automatically by the system, cannot be requested directly by users. If false, all Qualification types, including those managed by the system, are considered. Valid values are True | False. </p>
            must_be_owned_by_caller: <p> Specifies that only Qualification types that the Requester created are returned. If false, the operation returns all Qualification types. </p>
            max_results: <p> The maximum number of results to return in a single call. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_qualification_types_request.ListQualificationTypesRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_qualification_types_response.ListQualificationTypesResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_qualification_types

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_qualification_types.list_qualification_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_qualification_types_request.ListQualificationTypesRequest = {
            "must_be_requestable": must_be_requestable
        }
        if query is not None:
            input_["query"] = query
        if must_be_owned_by_caller is not None:
            input_["must_be_owned_by_caller"] = must_be_owned_by_caller
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

    def iter_list_qualification_types(
        self,
        must_be_requestable: "capo_mturk.types.boolean.Boolean",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        query: Optional["capo_mturk.types.string.String"] = None,
        must_be_owned_by_caller: Optional["capo_mturk.types.boolean.Boolean"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_qualification_types_response.ListQualificationTypesResponse]":
        _token = next_token
        while True:
            _response = self.list_qualification_types(
                must_be_requestable,
                config_overrides=config_overrides,
                query=query,
                must_be_owned_by_caller=must_be_owned_by_caller,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_reviewable_hi_ts(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        hit_type_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        status: Optional[
            "capo_mturk.types.reviewable_hit_status.ReviewableHITStatus"
        ] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_reviewable_hi_ts_response.ListReviewableHITsResponse":
        """<p> The <code>ListReviewableHITs</code> operation retrieves the HITs with Status equal to Reviewable or Status equal to Reviewing that belong to the Requester calling the operation. </p>

        Args:
            hit_type_id: <p> The ID of the HIT type of the HITs to consider for the query. If not specified, all HITs for the Reviewer are considered </p>
            status: <p> Can be either <code>Reviewable</code> or <code>Reviewing</code>. Reviewable is the default value. </p>
            next_token: <p>Pagination Token</p>
            max_results: <p> Limit the number of results returned. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_reviewable_hi_ts_request.ListReviewableHITsRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_reviewable_hi_ts_response.ListReviewableHITsResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_reviewable_hi_ts

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_reviewable_hi_ts.list_reviewable_hi_ts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_reviewable_hi_ts_request.ListReviewableHITsRequest = {}
        if hit_type_id is not None:
            input_["hit_type_id"] = hit_type_id
        if status is not None:
            input_["status"] = status
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

    def iter_list_reviewable_hi_ts(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        hit_type_id: Optional["capo_mturk.types.entity_id.EntityId"] = None,
        status: Optional[
            "capo_mturk.types.reviewable_hit_status.ReviewableHITStatus"
        ] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_reviewable_hi_ts_response.ListReviewableHITsResponse]":
        _token = next_token
        while True:
            _response = self.list_reviewable_hi_ts(
                config_overrides=config_overrides,
                hit_type_id=hit_type_id,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_review_policy_results_for_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        policy_levels: Optional[
            "capo_mturk.types.review_policy_level_list.ReviewPolicyLevelList"
        ] = None,
        retrieve_actions: Optional["capo_mturk.types.boolean.Boolean"] = None,
        retrieve_results: Optional["capo_mturk.types.boolean.Boolean"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_review_policy_results_for_hit_response.ListReviewPolicyResultsForHITResponse":
        """<p> The <code>ListReviewPolicyResultsForHIT</code> operation retrieves the computed results and the actions taken in the course of executing your Review Policies for a given HIT. For information about how to specify Review Policies when you call CreateHIT, see Review Policies. The ListReviewPolicyResultsForHIT operation can return results for both Assignment-level and HIT-level review results. </p>

        Args:
            hit_id: <p>The unique identifier of the HIT to retrieve review results for.</p>
            policy_levels: <p> The Policy Level(s) to retrieve review results for - HIT or Assignment. If omitted, the default behavior is to retrieve all data for both policy levels. For a list of all the described policies, see Review Policies. </p>
            retrieve_actions: <p> Specify if the operation should retrieve a list of the actions taken executing the Review Policies and their outcomes. </p>
            retrieve_results: <p> Specify if the operation should retrieve a list of the results computed by the Review Policies. </p>
            next_token: <p>Pagination token</p>
            max_results: <p>Limit the number of results returned.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_review_policy_results_for_hit_request.ListReviewPolicyResultsForHITRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_review_policy_results_for_hit_response.ListReviewPolicyResultsForHITResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_review_policy_results_for_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_review_policy_results_for_hit.list_review_policy_results_for_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_review_policy_results_for_hit_request.ListReviewPolicyResultsForHITRequest = {
            "hit_id": hit_id
        }
        if policy_levels is not None:
            input_["policy_levels"] = policy_levels
        if retrieve_actions is not None:
            input_["retrieve_actions"] = retrieve_actions
        if retrieve_results is not None:
            input_["retrieve_results"] = retrieve_results
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

    def iter_list_review_policy_results_for_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        policy_levels: Optional[
            "capo_mturk.types.review_policy_level_list.ReviewPolicyLevelList"
        ] = None,
        retrieve_actions: Optional["capo_mturk.types.boolean.Boolean"] = None,
        retrieve_results: Optional["capo_mturk.types.boolean.Boolean"] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_review_policy_results_for_hit_response.ListReviewPolicyResultsForHITResponse]":
        _token = next_token
        while True:
            _response = self.list_review_policy_results_for_hit(
                hit_id,
                config_overrides=config_overrides,
                policy_levels=policy_levels,
                retrieve_actions=retrieve_actions,
                retrieve_results=retrieve_results,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_worker_blocks(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_worker_blocks_response.ListWorkerBlocksResponse":
        """<p>The <code>ListWorkersBlocks</code> operation retrieves a list of Workers who are blocked from working on your HITs.</p>

        Args:
            next_token: <p>Pagination token</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_worker_blocks_request.ListWorkerBlocksRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_worker_blocks_response.ListWorkerBlocksResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_worker_blocks

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_worker_blocks.list_worker_blocks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_worker_blocks_request.ListWorkerBlocksRequest = {}
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

    def iter_list_worker_blocks(
        self,
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_worker_blocks_response.ListWorkerBlocksResponse]":
        _token = next_token
        while True:
            _response = self.list_worker_blocks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_workers_with_qualification_type(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        status: Optional[
            "capo_mturk.types.qualification_status.QualificationStatus"
        ] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "capo_mturk.types.list_workers_with_qualification_type_response.ListWorkersWithQualificationTypeResponse":
        """<p> The <code>ListWorkersWithQualificationType</code> operation returns all of the Workers that have been associated with a given Qualification type. </p>

        Args:
            qualification_type_id: <p>The ID of the Qualification type of the Qualifications to return.</p>
            status: <p> The status of the Qualifications to return. Can be <code>Granted | Revoked</code>. </p>
            next_token: <p>Pagination Token</p>
            max_results: <p> Limit the number of results returned. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.list_workers_with_qualification_type_request.ListWorkersWithQualificationTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.list_workers_with_qualification_type_response.ListWorkersWithQualificationTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.list_workers_with_qualification_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.list_workers_with_qualification_type.list_workers_with_qualification_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.list_workers_with_qualification_type_request.ListWorkersWithQualificationTypeRequest = {
            "qualification_type_id": qualification_type_id
        }
        if status is not None:
            input_["status"] = status
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

    def iter_list_workers_with_qualification_type(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        status: Optional[
            "capo_mturk.types.qualification_status.QualificationStatus"
        ] = None,
        next_token: Optional[
            "capo_mturk.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_mturk.types.result_size.ResultSize"] = None,
    ) -> "Iterator[capo_mturk.types.list_workers_with_qualification_type_response.ListWorkersWithQualificationTypeResponse]":
        _token = next_token
        while True:
            _response = self.list_workers_with_qualification_type(
                qualification_type_id,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def notify_workers(
        self,
        subject: "capo_mturk.types.string.String",
        message_text: "capo_mturk.types.string.String",
        worker_ids: "capo_mturk.types.customer_id_list.CustomerIdList",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.notify_workers_response.NotifyWorkersResponse":
        """<p> The <code>NotifyWorkers</code> operation sends an email to one or more Workers that you specify with the Worker ID. You can specify up to 100 Worker IDs to send the same message with a single call to the NotifyWorkers operation. The NotifyWorkers operation will send a notification email to a Worker only if you have previously approved or rejected work from the Worker. </p>

        Args:
            subject: <p>The subject line of the email message to send. Can include up to 200 characters.</p>
            message_text: <p>The text of the email message to send. Can include up to 4,096 characters</p>
            worker_ids: <p>A list of Worker IDs you wish to notify. You can notify upto 100 Workers at a time.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.notify_workers_request.NotifyWorkersRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.notify_workers_response.NotifyWorkersResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.notify_workers

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.notify_workers.notify_workers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.notify_workers_request.NotifyWorkersRequest = {
            "subject": subject,
            "message_text": message_text,
            "worker_ids": worker_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_assignment(
        self,
        assignment_id: "capo_mturk.types.entity_id.EntityId",
        requester_feedback: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.reject_assignment_response.RejectAssignmentResponse":
        """<p> The <code>RejectAssignment</code> operation rejects the results of a completed assignment. </p> <p> You can include an optional feedback message with the rejection, which the Worker can see in the Status section of the web site. When you include a feedback message with the rejection, it helps the Worker understand why the assignment was rejected, and can improve the quality of the results the Worker submits in the future. </p> <p> Only the Requester who created the HIT can reject an assignment for the HIT. </p>

        Args:
            assignment_id: <p> The ID of the assignment. The assignment must correspond to a HIT created by the Requester. </p>
            requester_feedback: <p> A message for the Worker, which the Worker can see in the Status section of the web site. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.reject_assignment_request.RejectAssignmentRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.reject_assignment_response.RejectAssignmentResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.reject_assignment

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.reject_assignment.reject_assignment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.reject_assignment_request.RejectAssignmentRequest = {
            "assignment_id": assignment_id,
            "requester_feedback": requester_feedback,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_qualification_request(
        self,
        qualification_request_id: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        reason: Optional["capo_mturk.types.string.String"] = None,
    ) -> "capo_mturk.types.reject_qualification_request_response.RejectQualificationRequestResponse":
        """<p> The <code>RejectQualificationRequest</code> operation rejects a user's request for a Qualification. </p> <p> You can provide a text message explaining why the request was rejected. The Worker who made the request can see this message.</p>

        Args:
            qualification_request_id: <p> The ID of the Qualification request, as returned by the <code>ListQualificationRequests</code> operation. </p>
            reason: <p>A text message explaining why the request was rejected, to be shown to the Worker who made the request.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.reject_qualification_request_request.RejectQualificationRequestRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.reject_qualification_request_response.RejectQualificationRequestResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.reject_qualification_request

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.reject_qualification_request.reject_qualification_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.reject_qualification_request_request.RejectQualificationRequestRequest = {
            "qualification_request_id": qualification_request_id
        }
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_bonus(
        self,
        worker_id: "capo_mturk.types.customer_id.CustomerId",
        bonus_amount: "capo_mturk.types.currency_amount.CurrencyAmount",
        assignment_id: "capo_mturk.types.entity_id.EntityId",
        reason: "capo_mturk.types.string.String",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        unique_request_token: Optional[
            "capo_mturk.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_mturk.types.send_bonus_response.SendBonusResponse":
        """<p> The <code>SendBonus</code> operation issues a payment of money from your account to a Worker. This payment happens separately from the reward you pay to the Worker when you approve the Worker's assignment. The SendBonus operation requires the Worker's ID and the assignment ID as parameters to initiate payment of the bonus. You must include a message that explains the reason for the bonus payment, as the Worker may not be expecting the payment. Amazon Mechanical Turk collects a fee for bonus payments, similar to the HIT listing fee. This operation fails if your account does not have enough funds to pay for both the bonus and the fees. </p>

        Args:
            worker_id: <p>The ID of the Worker being paid the bonus.</p>
            bonus_amount: <p> The Bonus amount is a US Dollar amount specified using a string (for example, "5" represents $5.00 USD and "101.42" represents $101.42 USD). Do not include currency symbols or currency codes. </p>
            assignment_id: <p>The ID of the assignment for which this bonus is paid.</p>
            reason: <p>A message that explains the reason for the bonus payment. The Worker receiving the bonus can see this message.</p>
            unique_request_token: <p>A unique identifier for this request, which allows you to retry the call on error without granting multiple bonuses. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the bonus already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return an error with a message containing the request ID.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.send_bonus_request.SendBonusRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.send_bonus_response.SendBonusResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.send_bonus

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.send_bonus.send_bonus(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.send_bonus_request.SendBonusRequest = {
            "worker_id": worker_id,
            "bonus_amount": bonus_amount,
            "assignment_id": assignment_id,
            "reason": reason,
        }
        if unique_request_token is not None:
            input_["unique_request_token"] = unique_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_test_event_notification(
        self,
        notification: "capo_mturk.types.notification_specification.NotificationSpecification",
        test_event_type: "capo_mturk.types.event_type.EventType",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.send_test_event_notification_response.SendTestEventNotificationResponse":
        """<p> The <code>SendTestEventNotification</code> operation causes Amazon Mechanical Turk to send a notification message as if a HIT event occurred, according to the provided notification specification. This allows you to test notifications without setting up notifications for a real HIT type and trying to trigger them using the website. When you call this operation, the service attempts to send the test notification immediately. </p>

        Args:
            notification: <p> The notification specification to test. This value is identical to the value you would provide to the UpdateNotificationSettings operation when you establish the notification specification for a HIT type. </p>
            test_event_type: <p> The event to simulate to test the notification specification. This event is included in the test message even if the notification specification does not include the event type. The notification specification does not filter out the test event. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.send_test_event_notification_request.SendTestEventNotificationRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.send_test_event_notification_response.SendTestEventNotificationResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.send_test_event_notification

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.send_test_event_notification.send_test_event_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.send_test_event_notification_request.SendTestEventNotificationRequest = {
            "notification": notification,
            "test_event_type": test_event_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_expiration_for_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        expire_at: "capo_mturk.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.update_expiration_for_hit_response.UpdateExpirationForHITResponse":
        """<p> The <code>UpdateExpirationForHIT</code> operation allows you update the expiration time of a HIT. If you update it to a time in the past, the HIT will be immediately expired. </p>

        Args:
            hit_id: <p> The HIT to update. </p>
            expire_at: <p> The date and time at which you want the HIT to expire </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.update_expiration_for_hit_request.UpdateExpirationForHITRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.update_expiration_for_hit_response.UpdateExpirationForHITResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.update_expiration_for_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.update_expiration_for_hit.update_expiration_for_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.update_expiration_for_hit_request.UpdateExpirationForHITRequest = {
            "hit_id": hit_id,
            "expire_at": expire_at,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_hit_review_status(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        revert: Optional["capo_mturk.types.boolean.Boolean"] = None,
    ) -> "capo_mturk.types.update_hit_review_status_response.UpdateHITReviewStatusResponse":
        """<p> The <code>UpdateHITReviewStatus</code> operation updates the status of a HIT. If the status is Reviewable, this operation can update the status to Reviewing, or it can revert a Reviewing HIT back to the Reviewable status. </p>

        Args:
            hit_id: <p> The ID of the HIT to update. </p>
            revert: <p> Specifies how to update the HIT status. Default is <code>False</code>. </p> <ul> <li> <p> Setting this to false will only transition a HIT from <code>Reviewable</code> to <code>Reviewing</code> </p> </li> <li> <p> Setting this to true will only transition a HIT from <code>Reviewing</code> to <code>Reviewable</code> </p> </li> </ul>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.update_hit_review_status_request.UpdateHITReviewStatusRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.update_hit_review_status_response.UpdateHITReviewStatusResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.update_hit_review_status

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.update_hit_review_status.update_hit_review_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.update_hit_review_status_request.UpdateHITReviewStatusRequest = {
            "hit_id": hit_id
        }
        if revert is not None:
            input_["revert"] = revert

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_hit_type_of_hit(
        self,
        hit_id: "capo_mturk.types.entity_id.EntityId",
        hit_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
    ) -> "capo_mturk.types.update_hit_type_of_hit_response.UpdateHITTypeOfHITResponse":
        """<p> The <code>UpdateHITTypeOfHIT</code> operation allows you to change the HITType properties of a HIT. This operation disassociates the HIT from its old HITType properties and associates it with the new HITType properties. The HIT takes on the properties of the new HITType in place of the old ones. </p>

        Args:
            hit_id: <p>The HIT to update.</p>
            hit_type_id: <p>The ID of the new HIT type.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.update_hit_type_of_hit_request.UpdateHITTypeOfHITRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.update_hit_type_of_hit_response.UpdateHITTypeOfHITResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.update_hit_type_of_hit

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.update_hit_type_of_hit.update_hit_type_of_hit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.update_hit_type_of_hit_request.UpdateHITTypeOfHITRequest = {
            "hit_id": hit_id,
            "hit_type_id": hit_type_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_notification_settings(
        self,
        hit_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        notification: Optional[
            "capo_mturk.types.notification_specification.NotificationSpecification"
        ] = None,
        active: Optional["capo_mturk.types.boolean.Boolean"] = None,
    ) -> "capo_mturk.types.update_notification_settings_response.UpdateNotificationSettingsResponse":
        """<p> The <code>UpdateNotificationSettings</code> operation creates, updates, disables or re-enables notifications for a HIT type. If you call the UpdateNotificationSettings operation for a HIT type that already has a notification specification, the operation replaces the old specification with a new one. You can call the UpdateNotificationSettings operation to enable or disable notifications for the HIT type, without having to modify the notification specification itself by providing updates to the Active status without specifying a new notification specification. To change the Active status of a HIT type's notifications, the HIT type must already have a notification specification, or one must be provided in the same call to <code>UpdateNotificationSettings</code>. </p>

        Args:
            hit_type_id: <p> The ID of the HIT type whose notification specification is being updated. </p>
            notification: <p> The notification specification for the HIT type. </p>
            active: <p> Specifies whether notifications are sent for HITs of this HIT type, according to the notification specification. You must specify either the Notification parameter or the Active parameter for the call to UpdateNotificationSettings to succeed. </p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.update_notification_settings_request.UpdateNotificationSettingsRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.update_notification_settings_response.UpdateNotificationSettingsResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.update_notification_settings

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.update_notification_settings.update_notification_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.update_notification_settings_request.UpdateNotificationSettingsRequest = {
            "hit_type_id": hit_type_id
        }
        if notification is not None:
            input_["notification"] = notification
        if active is not None:
            input_["active"] = active

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_qualification_type(
        self,
        qualification_type_id: "capo_mturk.types.entity_id.EntityId",
        *,
        config_overrides: Optional[MTurkClientConfig] = None,
        description: Optional["capo_mturk.types.string.String"] = None,
        qualification_type_status: Optional[
            "capo_mturk.types.qualification_type_status.QualificationTypeStatus"
        ] = None,
        test: Optional["capo_mturk.types.string.String"] = None,
        answer_key: Optional["capo_mturk.types.string.String"] = None,
        test_duration_in_seconds: Optional["capo_mturk.types.long.Long"] = None,
        retry_delay_in_seconds: Optional["capo_mturk.types.long.Long"] = None,
        auto_granted: Optional["capo_mturk.types.boolean.Boolean"] = None,
        auto_granted_value: Optional["capo_mturk.types.integer.Integer"] = None,
    ) -> "capo_mturk.types.update_qualification_type_response.UpdateQualificationTypeResponse":
        """<p> The <code>UpdateQualificationType</code> operation modifies the attributes of an existing Qualification type, which is represented by a QualificationType data structure. Only the owner of a Qualification type can modify its attributes. </p> <p> Most attributes of a Qualification type can be changed after the type has been created. However, the Name and Keywords fields cannot be modified. The RetryDelayInSeconds parameter can be modified or added to change the delay or to enable retries, but RetryDelayInSeconds cannot be used to disable retries. </p> <p> You can use this operation to update the test for a Qualification type. The test is updated based on the values specified for the Test, TestDurationInSeconds and AnswerKey parameters. All three parameters specify the updated test. If you are updating the test for a type, you must specify the Test and TestDurationInSeconds parameters. The AnswerKey parameter is optional; omitting it specifies that the updated test does not have an answer key. </p> <p> If you omit the Test parameter, the test for the Qualification type is unchanged. There is no way to remove a test from a Qualification type that has one. If the type already has a test, you cannot update it to be AutoGranted. If the Qualification type does not have a test and one is provided by an update, the type will henceforth have a test. </p> <p> If you want to update the test duration or answer key for an existing test without changing the questions, you must specify a Test parameter with the original questions, along with the updated values. </p> <p> If you provide an updated Test but no AnswerKey, the new test will not have an answer key. Requests for such Qualifications must be granted manually. </p> <p> You can also update the AutoGranted and AutoGrantedValue attributes of the Qualification type.</p>

        Args:
            qualification_type_id: <p>The ID of the Qualification type to update.</p>
            description: <p>The new description of the Qualification type.</p>
            qualification_type_status: <p>The new status of the Qualification type - Active | Inactive</p>
            test: <p>The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, <code>TestDurationInSeconds</code> must also be specified.</p> <p>Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.</p> <p>Constraints: None. If not specified, the Worker may request the Qualification without answering any questions.</p>
            answer_key: <p>The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.</p>
            test_duration_in_seconds: <p>The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.</p>
            retry_delay_in_seconds: <p>The amount of time, in seconds, that Workers must wait after requesting a Qualification of the specified Qualification type before they can retry the Qualification request. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must dispose of the existing retry-enabled Qualification type using DisposeQualificationType and then create a new Qualification type with retries disabled using CreateQualificationType.</p>
            auto_granted: <p>Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.</p> <p>Constraints: If the Test parameter is specified, this parameter cannot be true.</p>
            auto_granted_value: <p>The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.</p>

        Raises:
            capo_mturk.errors.request_error.RequestError: <p>Your request is invalid.</p>
            capo_mturk.errors.service_fault.ServiceFault: <p>Amazon Mechanical Turk is temporarily unable to process your request. Try your call again.</p>
            capo_mturk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mturk.types.update_qualification_type_request.UpdateQualificationTypeRequest]",
        ) -> OperationResponse[
            "capo_mturk.types.update_qualification_type_response.UpdateQualificationTypeResponse"
        ]:
            import capo_mturk._operations.m_turk_requester_service_v20170117.update_qualification_type

            output, http_response = (
                capo_mturk._operations.m_turk_requester_service_v20170117.update_qualification_type.update_qualification_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mturk.types.update_qualification_type_request.UpdateQualificationTypeRequest = {
            "qualification_type_id": qualification_type_id
        }
        if description is not None:
            input_["description"] = description
        if qualification_type_status is not None:
            input_["qualification_type_status"] = qualification_type_status
        if test is not None:
            input_["test"] = test
        if answer_key is not None:
            input_["answer_key"] = answer_key
        if test_duration_in_seconds is not None:
            input_["test_duration_in_seconds"] = test_duration_in_seconds
        if retry_delay_in_seconds is not None:
            input_["retry_delay_in_seconds"] = retry_delay_in_seconds
        if auto_granted is not None:
            input_["auto_granted"] = auto_granted
        if auto_granted_value is not None:
            input_["auto_granted_value"] = auto_granted_value

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

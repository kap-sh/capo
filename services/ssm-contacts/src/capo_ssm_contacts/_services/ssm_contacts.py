"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#SSMContacts``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ssm_contacts._auth._signers
import capo_ssm_contacts._auth._sigv4
from capo_ssm_contacts._auth._identity import Credentials
from capo_ssm_contacts._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ssm_contacts._auth._zapros_handler import AuthMiddleware
from capo_ssm_contacts._pagination import resolve_path as _resolve_path
from capo_ssm_contacts._services._aws_config import aws_config
from capo_ssm_contacts._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ssm_contacts.types.accept_code
    import capo_ssm_contacts.types.accept_code_validation
    import capo_ssm_contacts.types.accept_page_request
    import capo_ssm_contacts.types.accept_page_result
    import capo_ssm_contacts.types.accept_type
    import capo_ssm_contacts.types.activate_contact_channel_request
    import capo_ssm_contacts.types.activate_contact_channel_result
    import capo_ssm_contacts.types.activation_code
    import capo_ssm_contacts.types.amazon_resource_name
    import capo_ssm_contacts.types.channel_name
    import capo_ssm_contacts.types.channel_type
    import capo_ssm_contacts.types.contact
    import capo_ssm_contacts.types.contact_alias
    import capo_ssm_contacts.types.contact_channel
    import capo_ssm_contacts.types.contact_channel_address
    import capo_ssm_contacts.types.contact_name
    import capo_ssm_contacts.types.contact_type
    import capo_ssm_contacts.types.content
    import capo_ssm_contacts.types.create_contact_channel_request
    import capo_ssm_contacts.types.create_contact_channel_result
    import capo_ssm_contacts.types.create_contact_request
    import capo_ssm_contacts.types.create_contact_result
    import capo_ssm_contacts.types.create_rotation_override_request
    import capo_ssm_contacts.types.create_rotation_override_result
    import capo_ssm_contacts.types.create_rotation_request
    import capo_ssm_contacts.types.create_rotation_result
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.deactivate_contact_channel_request
    import capo_ssm_contacts.types.deactivate_contact_channel_result
    import capo_ssm_contacts.types.defer_activation
    import capo_ssm_contacts.types.delete_contact_channel_request
    import capo_ssm_contacts.types.delete_contact_channel_result
    import capo_ssm_contacts.types.delete_contact_request
    import capo_ssm_contacts.types.delete_contact_result
    import capo_ssm_contacts.types.delete_rotation_override_request
    import capo_ssm_contacts.types.delete_rotation_override_result
    import capo_ssm_contacts.types.delete_rotation_request
    import capo_ssm_contacts.types.delete_rotation_result
    import capo_ssm_contacts.types.describe_engagement_request
    import capo_ssm_contacts.types.describe_engagement_result
    import capo_ssm_contacts.types.describe_page_request
    import capo_ssm_contacts.types.describe_page_result
    import capo_ssm_contacts.types.engagement
    import capo_ssm_contacts.types.get_contact_channel_request
    import capo_ssm_contacts.types.get_contact_channel_result
    import capo_ssm_contacts.types.get_contact_policy_request
    import capo_ssm_contacts.types.get_contact_policy_result
    import capo_ssm_contacts.types.get_contact_request
    import capo_ssm_contacts.types.get_contact_result
    import capo_ssm_contacts.types.get_rotation_override_request
    import capo_ssm_contacts.types.get_rotation_override_result
    import capo_ssm_contacts.types.get_rotation_request
    import capo_ssm_contacts.types.get_rotation_result
    import capo_ssm_contacts.types.idempotency_token
    import capo_ssm_contacts.types.incident_id
    import capo_ssm_contacts.types.list_contact_channels_request
    import capo_ssm_contacts.types.list_contact_channels_result
    import capo_ssm_contacts.types.list_contacts_request
    import capo_ssm_contacts.types.list_contacts_result
    import capo_ssm_contacts.types.list_engagements_request
    import capo_ssm_contacts.types.list_engagements_result
    import capo_ssm_contacts.types.list_page_receipts_request
    import capo_ssm_contacts.types.list_page_receipts_result
    import capo_ssm_contacts.types.list_page_resolutions_request
    import capo_ssm_contacts.types.list_page_resolutions_result
    import capo_ssm_contacts.types.list_pages_by_contact_request
    import capo_ssm_contacts.types.list_pages_by_contact_result
    import capo_ssm_contacts.types.list_pages_by_engagement_request
    import capo_ssm_contacts.types.list_pages_by_engagement_result
    import capo_ssm_contacts.types.list_preview_rotation_shifts_request
    import capo_ssm_contacts.types.list_preview_rotation_shifts_result
    import capo_ssm_contacts.types.list_rotation_overrides_request
    import capo_ssm_contacts.types.list_rotation_overrides_result
    import capo_ssm_contacts.types.list_rotation_shifts_request
    import capo_ssm_contacts.types.list_rotation_shifts_result
    import capo_ssm_contacts.types.list_rotations_request
    import capo_ssm_contacts.types.list_rotations_result
    import capo_ssm_contacts.types.list_tags_for_resource_request
    import capo_ssm_contacts.types.list_tags_for_resource_result
    import capo_ssm_contacts.types.max_results
    import capo_ssm_contacts.types.override_list
    import capo_ssm_contacts.types.page
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.plan
    import capo_ssm_contacts.types.policy
    import capo_ssm_contacts.types.public_content
    import capo_ssm_contacts.types.public_subject
    import capo_ssm_contacts.types.put_contact_policy_request
    import capo_ssm_contacts.types.put_contact_policy_result
    import capo_ssm_contacts.types.receipt
    import capo_ssm_contacts.types.receipt_info
    import capo_ssm_contacts.types.recurrence_settings
    import capo_ssm_contacts.types.resolution_contact
    import capo_ssm_contacts.types.rotation
    import capo_ssm_contacts.types.rotation_contacts_arn_list
    import capo_ssm_contacts.types.rotation_name
    import capo_ssm_contacts.types.rotation_override
    import capo_ssm_contacts.types.rotation_override_contacts_arn_list
    import capo_ssm_contacts.types.rotation_preview_member_list
    import capo_ssm_contacts.types.rotation_shift
    import capo_ssm_contacts.types.send_activation_code_request
    import capo_ssm_contacts.types.send_activation_code_result
    import capo_ssm_contacts.types.sender
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.start_engagement_request
    import capo_ssm_contacts.types.start_engagement_result
    import capo_ssm_contacts.types.stop_engagement_request
    import capo_ssm_contacts.types.stop_engagement_result
    import capo_ssm_contacts.types.stop_reason
    import capo_ssm_contacts.types.subject
    import capo_ssm_contacts.types.tag_key_list
    import capo_ssm_contacts.types.tag_resource_request
    import capo_ssm_contacts.types.tag_resource_result
    import capo_ssm_contacts.types.tags_list
    import capo_ssm_contacts.types.time_range
    import capo_ssm_contacts.types.time_zone_id
    import capo_ssm_contacts.types.untag_resource_request
    import capo_ssm_contacts.types.untag_resource_result
    import capo_ssm_contacts.types.update_contact_channel_request
    import capo_ssm_contacts.types.update_contact_channel_result
    import capo_ssm_contacts.types.update_contact_request
    import capo_ssm_contacts.types.update_contact_result
    import capo_ssm_contacts.types.update_rotation_request
    import capo_ssm_contacts.types.update_rotation_result
    import capo_ssm_contacts.types.uuid


class SSMContactsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SSMContactsClient:
    """A client for the ``SSMContacts`` service.

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
        self._config = SSMContactsClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[SSMContactsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SSMContactsClientConfig = config_overrides or {}
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

    def accept_page(
        self,
        page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        accept_type: "capo_ssm_contacts.types.accept_type.AcceptType",
        accept_code: "capo_ssm_contacts.types.accept_code.AcceptCode",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        contact_channel_id: Optional[
            "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
        ] = None,
        note: Optional["capo_ssm_contacts.types.receipt_info.ReceiptInfo"] = None,
        accept_code_validation: Optional[
            "capo_ssm_contacts.types.accept_code_validation.AcceptCodeValidation"
        ] = None,
    ) -> "capo_ssm_contacts.types.accept_page_result.AcceptPageResult":
        """<p>Used to acknowledge an engagement to a contact channel during an incident.</p>

        Args:
            page_id: <p>The Amazon Resource Name (ARN) of the engagement to a contact channel.</p>
            contact_channel_id: <p>The ARN of the contact channel.</p>
            accept_type: <p>The type indicates if the page was <code>DELIVERED</code> or <code>READ</code>.</p>
            note: <p>Information provided by the user when the user acknowledges the page.</p>
            accept_code: <p>A 6-digit code used to acknowledge the page.</p>
            accept_code_validation: <p>An optional field that Incident Manager uses to <code>ENFORCE</code> <code>AcceptCode</code> validation when acknowledging an page. Acknowledgement can occur by replying to a page, or when entering the AcceptCode in the console. Enforcing AcceptCode validation causes Incident Manager to verify that the code entered by the user matches the code sent by Incident Manager with the page.</p> <p>Incident Manager can also <code>IGNORE</code> <code>AcceptCode</code> validation. Ignoring <code>AcceptCode</code> validation causes Incident Manager to accept any value entered for the <code>AcceptCode</code>.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.accept_page_request.AcceptPageRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.accept_page_result.AcceptPageResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.accept_page

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.accept_page.accept_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.accept_page_request.AcceptPageRequest = {
            "page_id": page_id,
            "accept_type": accept_type,
            "accept_code": accept_code,
        }
        if contact_channel_id is not None:
            input_["contact_channel_id"] = contact_channel_id
        if note is not None:
            input_["note"] = note
        if accept_code_validation is not None:
            input_["accept_code_validation"] = accept_code_validation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def activate_contact_channel(
        self,
        contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        activation_code: "capo_ssm_contacts.types.activation_code.ActivationCode",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.activate_contact_channel_result.ActivateContactChannelResult":
        """<p>Activates a contact's contact channel. Incident Manager can't engage a contact until the contact channel has been activated.</p>

        Args:
            contact_channel_id: <p>The Amazon Resource Name (ARN) of the contact channel.</p>
            activation_code: <p>The code sent to the contact channel when it was created in the contact.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.activate_contact_channel_request.ActivateContactChannelRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.activate_contact_channel_result.ActivateContactChannelResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.activate_contact_channel

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.activate_contact_channel.activate_contact_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.activate_contact_channel_request.ActivateContactChannelRequest = {
            "contact_channel_id": contact_channel_id,
            "activation_code": activation_code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_contact(
        self,
        alias: "capo_ssm_contacts.types.contact_alias.ContactAlias",
        type: "capo_ssm_contacts.types.contact_type.ContactType",
        plan: "capo_ssm_contacts.types.plan.Plan",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        display_name: Optional[
            "capo_ssm_contacts.types.contact_name.ContactName"
        ] = None,
        tags: Optional["capo_ssm_contacts.types.tags_list.TagsList"] = None,
        idempotency_token: Optional[
            "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_ssm_contacts.types.create_contact_result.CreateContactResult":
        """<p>Contacts are either the contacts that Incident Manager engages during an incident or the escalation plans that Incident Manager uses to engage contacts in phases during an incident.</p>

        Args:
            alias: <p>The short name to quickly identify a contact or escalation plan. The contact alias must be unique and identifiable.</p>
            display_name: <p>The full name of the contact or escalation plan.</p>
            type: <p>The type of contact to create.</p> <ul> <li> <p> <code>PERSONAL</code>: A single, individual contact.</p> </li> <li> <p> <code>ESCALATION</code>: An escalation plan.</p> </li> <li> <p> <code>ONCALL_SCHEDULE</code>: An on-call schedule.</p> </li> </ul>
            plan: <p>A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.</p>
            tags: <p>Adds a tag to the target. You can only tag resources created in the first Region of your replication set.</p>
            idempotency_token: <p>A token ensuring that the operation is called only once with the specified details.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.create_contact_request.CreateContactRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.create_contact_result.CreateContactResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.create_contact

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.create_contact.create_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.create_contact_request.CreateContactRequest = {
            "alias": alias,
            "type": type,
            "plan": plan,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if tags is not None:
            input_["tags"] = tags
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_contact_channel(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        name: "capo_ssm_contacts.types.channel_name.ChannelName",
        type: "capo_ssm_contacts.types.channel_type.ChannelType",
        delivery_address: "capo_ssm_contacts.types.contact_channel_address.ContactChannelAddress",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        defer_activation: Optional[
            "capo_ssm_contacts.types.defer_activation.DeferActivation"
        ] = None,
        idempotency_token: Optional[
            "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_ssm_contacts.types.create_contact_channel_result.CreateContactChannelResult":
        """<p>A contact channel is the method that Incident Manager uses to engage your contact.</p>

        Args:
            contact_id: <p>The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.</p>
            name: <p>The name of the contact channel.</p>
            type: <p>Incident Manager supports three types of contact channels:</p> <ul> <li> <p> <code>SMS</code> </p> </li> <li> <p> <code>VOICE</code> </p> </li> <li> <p> <code>EMAIL</code> </p> </li> </ul>
            delivery_address: <p>The details that Incident Manager uses when trying to engage the contact channel. The format is dependent on the type of the contact channel. The following are the expected formats:</p> <ul> <li> <p>SMS - '+' followed by the country code and phone number</p> </li> <li> <p>VOICE - '+' followed by the country code and phone number</p> </li> <li> <p>EMAIL - any standard email format</p> </li> </ul>
            defer_activation: <p>If you want to activate the channel at a later time, you can choose to defer activation. Incident Manager can't engage your contact channel until it has been activated.</p>
            idempotency_token: <p>A token ensuring that the operation is called only once with the specified details.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.create_contact_channel_request.CreateContactChannelRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.create_contact_channel_result.CreateContactChannelResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.create_contact_channel

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.create_contact_channel.create_contact_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.create_contact_channel_request.CreateContactChannelRequest = {
            "contact_id": contact_id,
            "name": name,
            "type": type,
            "delivery_address": delivery_address,
        }
        if defer_activation is not None:
            input_["defer_activation"] = defer_activation
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_rotation(
        self,
        name: "capo_ssm_contacts.types.rotation_name.RotationName",
        contact_ids: "capo_ssm_contacts.types.rotation_contacts_arn_list.RotationContactsArnList",
        time_zone_id: "capo_ssm_contacts.types.time_zone_id.TimeZoneId",
        recurrence: "capo_ssm_contacts.types.recurrence_settings.RecurrenceSettings",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        start_time: Optional["capo_ssm_contacts.types.date_time.DateTime"] = None,
        tags: Optional["capo_ssm_contacts.types.tags_list.TagsList"] = None,
        idempotency_token: Optional[
            "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_ssm_contacts.types.create_rotation_result.CreateRotationResult":
        """<p>Creates a rotation in an on-call schedule.</p>

        Args:
            name: <p>The name of the rotation.</p>
            contact_ids: <p>The Amazon Resource Names (ARNs) of the contacts to add to the rotation.</p> <note> <p>Only the <code>PERSONAL</code> contact type is supported. The contact types <code>ESCALATION</code> and <code>ONCALL_SCHEDULE</code> are not supported for this operation. </p> </note> <p>The order that you list the contacts in is their shift order in the rotation schedule. To change the order of the contact's shifts, use the <a>UpdateRotation</a> operation.</p>
            start_time: <p>The date and time that the rotation goes into effect.</p>
            time_zone_id: <p>The time zone to base the rotation’s activity on in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the <a href="https://www.iana.org/time-zones">Time Zone Database</a> on the IANA website.</p> <note> <p>Designators for time zones that don’t support Daylight Savings Time rules, such as Pacific Standard Time (PST), are not supported.</p> </note>
            recurrence: <p>Information about the rule that specifies when a shift's team members rotate.</p>
            tags: <p>Optional metadata to assign to the rotation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html">Tagging Incident Manager resources</a> in the <i>Incident Manager User Guide</i>.</p>
            idempotency_token: <p>A token that ensures that the operation is called only once with the specified details.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.create_rotation_request.CreateRotationRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.create_rotation_result.CreateRotationResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.create_rotation

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.create_rotation.create_rotation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.create_rotation_request.CreateRotationRequest = {
            "name": name,
            "contact_ids": contact_ids,
            "time_zone_id": time_zone_id,
            "recurrence": recurrence,
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if tags is not None:
            input_["tags"] = tags
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_rotation_override(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        new_contact_ids: "capo_ssm_contacts.types.rotation_override_contacts_arn_list.RotationOverrideContactsArnList",
        start_time: "capo_ssm_contacts.types.date_time.DateTime",
        end_time: "capo_ssm_contacts.types.date_time.DateTime",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        idempotency_token: Optional[
            "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_ssm_contacts.types.create_rotation_override_result.CreateRotationOverrideResult":
        """<p>Creates an override for a rotation in an on-call schedule.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the rotation to create an override for.</p>
            new_contact_ids: <p>The Amazon Resource Names (ARNs) of the contacts to replace those in the current on-call rotation with.</p> <p>If you want to include any current team members in the override shift, you must include their ARNs in the new contact ID list.</p>
            start_time: <p>The date and time when the override goes into effect.</p>
            end_time: <p>The date and time when the override ends.</p>
            idempotency_token: <p>A token that ensures that the operation is called only once with the specified details.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.create_rotation_override_request.CreateRotationOverrideRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.create_rotation_override_result.CreateRotationOverrideResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.create_rotation_override

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.create_rotation_override.create_rotation_override(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.create_rotation_override_request.CreateRotationOverrideRequest = {
            "rotation_id": rotation_id,
            "new_contact_ids": new_contact_ids,
            "start_time": start_time,
            "end_time": end_time,
        }
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deactivate_contact_channel(
        self,
        contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.deactivate_contact_channel_result.DeactivateContactChannelResult":
        """<p>To no longer receive Incident Manager engagements to a contact channel, you can deactivate the channel.</p>

        Args:
            contact_channel_id: <p>The Amazon Resource Name (ARN) of the contact channel you're deactivating.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.deactivate_contact_channel_request.DeactivateContactChannelRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.deactivate_contact_channel_result.DeactivateContactChannelResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.deactivate_contact_channel

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.deactivate_contact_channel.deactivate_contact_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.deactivate_contact_channel_request.DeactivateContactChannelRequest = {
            "contact_channel_id": contact_channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_contact(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.delete_contact_result.DeleteContactResult":
        """<p>To remove a contact from Incident Manager, you can delete the contact. However, deleting a contact does not remove it from escalation plans and related response plans. Deleting an escalation plan also does not remove it from all related response plans. To modify an escalation plan, we recommend using the <a>UpdateContact</a> action to specify a different existing contact.</p>

        Args:
            contact_id: <p>The Amazon Resource Name (ARN) of the contact that you're deleting.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.delete_contact_request.DeleteContactRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.delete_contact_result.DeleteContactResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.delete_contact

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.delete_contact.delete_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.delete_contact_request.DeleteContactRequest = {
            "contact_id": contact_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_contact_channel(
        self,
        contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.delete_contact_channel_result.DeleteContactChannelResult":
        """<p>To stop receiving engagements on a contact channel, you can delete the channel from a contact. Deleting the contact channel does not remove it from the contact's engagement plan, but the stage that includes the channel will be ignored. If you delete the only contact channel for a contact, you'll no longer be able to engage that contact during an incident.</p>

        Args:
            contact_channel_id: <p>The Amazon Resource Name (ARN) of the contact channel.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.delete_contact_channel_request.DeleteContactChannelRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.delete_contact_channel_result.DeleteContactChannelResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.delete_contact_channel

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.delete_contact_channel.delete_contact_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.delete_contact_channel_request.DeleteContactChannelRequest = {
            "contact_channel_id": contact_channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rotation(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.delete_rotation_result.DeleteRotationResult":
        """<p>Deletes a rotation from the system. If a rotation belongs to more than one on-call schedule, this operation deletes it from all of them.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the on-call rotation to delete.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.delete_rotation_request.DeleteRotationRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.delete_rotation_result.DeleteRotationResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.delete_rotation

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.delete_rotation.delete_rotation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.delete_rotation_request.DeleteRotationRequest = {
            "rotation_id": rotation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rotation_override(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        rotation_override_id: "capo_ssm_contacts.types.uuid.Uuid",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.delete_rotation_override_result.DeleteRotationOverrideResult":
        """<p>Deletes an existing override for an on-call rotation.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the rotation that was overridden.</p>
            rotation_override_id: <p>The Amazon Resource Name (ARN) of the on-call rotation override to delete.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.delete_rotation_override_request.DeleteRotationOverrideRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.delete_rotation_override_result.DeleteRotationOverrideResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.delete_rotation_override

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.delete_rotation_override.delete_rotation_override(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.delete_rotation_override_request.DeleteRotationOverrideRequest = {
            "rotation_id": rotation_id,
            "rotation_override_id": rotation_override_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_engagement(
        self,
        engagement_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.describe_engagement_result.DescribeEngagementResult":
        """<p>Incident Manager uses engagements to engage contacts and escalation plans during an incident. Use this command to describe the engagement that occurred during an incident.</p>

        Args:
            engagement_id: <p>The Amazon Resource Name (ARN) of the engagement you want the details of.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.describe_engagement_request.DescribeEngagementRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.describe_engagement_result.DescribeEngagementResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.describe_engagement

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.describe_engagement.describe_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.describe_engagement_request.DescribeEngagementRequest = {
            "engagement_id": engagement_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_page(
        self,
        page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.describe_page_result.DescribePageResult":
        """<p>Lists details of the engagement to a contact channel.</p>

        Args:
            page_id: <p>The ID of the engagement to a contact channel.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.describe_page_request.DescribePageRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.describe_page_result.DescribePageResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.describe_page

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.describe_page.describe_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.describe_page_request.DescribePageRequest = {
            "page_id": page_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_contact(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.get_contact_result.GetContactResult":
        """<p>Retrieves information about the specified contact or escalation plan.</p>

        Args:
            contact_id: <p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.get_contact_request.GetContactRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.get_contact_result.GetContactResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.get_contact

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.get_contact.get_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.get_contact_request.GetContactRequest = {
            "contact_id": contact_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_contact_channel(
        self,
        contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.get_contact_channel_result.GetContactChannelResult":
        """<p>List details about a specific contact channel.</p>

        Args:
            contact_channel_id: <p>The Amazon Resource Name (ARN) of the contact channel you want information about.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.get_contact_channel_request.GetContactChannelRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.get_contact_channel_result.GetContactChannelResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.get_contact_channel

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.get_contact_channel.get_contact_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.get_contact_channel_request.GetContactChannelRequest = {
            "contact_channel_id": contact_channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_contact_policy(
        self,
        contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.get_contact_policy_result.GetContactPolicyResult":
        """<p>Retrieves the resource policies attached to the specified contact or escalation plan.</p>

        Args:
            contact_arn: <p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.get_contact_policy_request.GetContactPolicyRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.get_contact_policy_result.GetContactPolicyResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.get_contact_policy

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.get_contact_policy.get_contact_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.get_contact_policy_request.GetContactPolicyRequest = {
            "contact_arn": contact_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rotation(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.get_rotation_result.GetRotationResult":
        """<p>Retrieves information about an on-call rotation.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the on-call rotation to retrieve information about.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.get_rotation_request.GetRotationRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.get_rotation_result.GetRotationResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.get_rotation

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.get_rotation.get_rotation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.get_rotation_request.GetRotationRequest = {
            "rotation_id": rotation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rotation_override(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        rotation_override_id: "capo_ssm_contacts.types.uuid.Uuid",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> (
        "capo_ssm_contacts.types.get_rotation_override_result.GetRotationOverrideResult"
    ):
        """<p>Retrieves information about an override to an on-call rotation.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the overridden rotation to retrieve information about.</p>
            rotation_override_id: <p>The Amazon Resource Name (ARN) of the on-call rotation override to retrieve information about.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.get_rotation_override_request.GetRotationOverrideRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.get_rotation_override_result.GetRotationOverrideResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.get_rotation_override

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.get_rotation_override.get_rotation_override(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.get_rotation_override_request.GetRotationOverrideRequest = {
            "rotation_id": rotation_id,
            "rotation_override_id": rotation_override_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_contact_channels(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_ssm_contacts.types.list_contact_channels_result.ListContactChannelsResult"
    ):
        """<p>Lists all contact channels for the specified contact.</p>

        Args:
            contact_id: <p>The Amazon Resource Name (ARN) of the contact.</p>
            next_token: <p>The pagination token to continue to the next page of results.</p>
            max_results: <p>The maximum number of contact channels per page.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_contact_channels_request.ListContactChannelsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_contact_channels_result.ListContactChannelsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_contact_channels

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_contact_channels.list_contact_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_contact_channels_request.ListContactChannelsRequest = {
            "contact_id": contact_id
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

    def iter_list_contact_channels(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.contact_channel.ContactChannel]":
        _token = next_token
        while True:
            _response = self.list_contact_channels(
                contact_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("contact_channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_contacts(
        self,
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
        alias_prefix: Optional[
            "capo_ssm_contacts.types.contact_alias.ContactAlias"
        ] = None,
        type: Optional["capo_ssm_contacts.types.contact_type.ContactType"] = None,
    ) -> "capo_ssm_contacts.types.list_contacts_result.ListContactsResult":
        """<p>Lists all contacts and escalation plans in Incident Manager.</p>

        Args:
            next_token: <p>The pagination token to continue to the next page of results.</p>
            max_results: <p>The maximum number of contacts and escalation plans per page of results.</p>
            alias_prefix: <p>Used to list only contacts who's aliases start with the specified prefix.</p>
            type: <p>The type of contact.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_contacts_request.ListContactsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_contacts_result.ListContactsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_contacts

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_contacts.list_contacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_contacts_request.ListContactsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if alias_prefix is not None:
            input_["alias_prefix"] = alias_prefix
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_contacts(
        self,
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
        alias_prefix: Optional[
            "capo_ssm_contacts.types.contact_alias.ContactAlias"
        ] = None,
        type: Optional["capo_ssm_contacts.types.contact_type.ContactType"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.contact.Contact]":
        _token = next_token
        while True:
            _response = self.list_contacts(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                alias_prefix=alias_prefix,
                type=type,
            )
            _page = _resolve_path(_response, ("contacts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_engagements(
        self,
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
        incident_id: Optional["capo_ssm_contacts.types.incident_id.IncidentId"] = None,
        time_range_value: Optional[
            "capo_ssm_contacts.types.time_range.TimeRange"
        ] = None,
    ) -> "capo_ssm_contacts.types.list_engagements_result.ListEngagementsResult":
        """<p>Lists all engagements that have happened in an incident.</p>

        Args:
            next_token: <p>The pagination token to continue to the next page of results.</p>
            max_results: <p>The maximum number of engagements per page of results.</p>
            incident_id: <p>The Amazon Resource Name (ARN) of the incident you're listing engagements for.</p>
            time_range_value: <p>The time range to lists engagements for an incident.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_engagements_request.ListEngagementsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_engagements_result.ListEngagementsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_engagements

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_engagements.list_engagements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_engagements_request.ListEngagementsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if incident_id is not None:
            input_["incident_id"] = incident_id
        if time_range_value is not None:
            input_["time_range_value"] = time_range_value

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_engagements(
        self,
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
        incident_id: Optional["capo_ssm_contacts.types.incident_id.IncidentId"] = None,
        time_range_value: Optional[
            "capo_ssm_contacts.types.time_range.TimeRange"
        ] = None,
    ) -> "Iterator[capo_ssm_contacts.types.engagement.Engagement]":
        _token = next_token
        while True:
            _response = self.list_engagements(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                incident_id=incident_id,
                time_range_value=time_range_value,
            )
            _page = _resolve_path(_response, ("engagements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_page_receipts(
        self,
        page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_contacts.types.list_page_receipts_result.ListPageReceiptsResult":
        """<p>Lists all of the engagements to contact channels that have been acknowledged.</p>

        Args:
            page_id: <p>The Amazon Resource Name (ARN) of the engagement to a specific contact channel.</p>
            next_token: <p>The pagination token to continue to the next page of results.</p>
            max_results: <p>The maximum number of acknowledgements per page of results.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_page_receipts_request.ListPageReceiptsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_page_receipts_result.ListPageReceiptsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_page_receipts

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_page_receipts.list_page_receipts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_page_receipts_request.ListPageReceiptsRequest = {
            "page_id": page_id
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

    def iter_list_page_receipts(
        self,
        page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.receipt.Receipt]":
        _token = next_token
        while True:
            _response = self.list_page_receipts(
                page_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("receipts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_page_resolutions(
        self,
        page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_ssm_contacts.types.list_page_resolutions_result.ListPageResolutionsResult"
    ):
        """<p>Returns the resolution path of an engagement. For example, the escalation plan engaged in an incident might target an on-call schedule that includes several contacts in a rotation, but just one contact on-call when the incident starts. The resolution path indicates the hierarchy of <i>escalation plan > on-call schedule > contact</i>.</p>

        Args:
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>
            page_id: <p>The Amazon Resource Name (ARN) of the contact engaged for the incident.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_page_resolutions_request.ListPageResolutionsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_page_resolutions_result.ListPageResolutionsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_page_resolutions

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_page_resolutions.list_page_resolutions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_page_resolutions_request.ListPageResolutionsRequest = {
            "page_id": page_id
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_page_resolutions(
        self,
        page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_ssm_contacts.types.resolution_contact.ResolutionContact]":
        _token = next_token
        while True:
            _response = self.list_page_resolutions(
                page_id,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("page_resolutions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_pages_by_contact(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_ssm_contacts.types.list_pages_by_contact_result.ListPagesByContactResult"
    ):
        """<p>Lists the engagements to a contact's contact channels.</p>

        Args:
            contact_id: <p>The Amazon Resource Name (ARN) of the contact you are retrieving engagements for.</p>
            next_token: <p>The pagination token to continue to the next page of results.</p>
            max_results: <p>The maximum number of engagements to contact channels to list per page of results. </p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_pages_by_contact_request.ListPagesByContactRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_pages_by_contact_result.ListPagesByContactResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_pages_by_contact

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_pages_by_contact.list_pages_by_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_pages_by_contact_request.ListPagesByContactRequest = {
            "contact_id": contact_id
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

    def iter_list_pages_by_contact(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.page.Page]":
        _token = next_token
        while True:
            _response = self.list_pages_by_contact(
                contact_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("pages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_pages_by_engagement(
        self,
        engagement_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_contacts.types.list_pages_by_engagement_result.ListPagesByEngagementResult":
        """<p>Lists the engagements to contact channels that occurred by engaging a contact.</p>

        Args:
            engagement_id: <p>The Amazon Resource Name (ARN) of the engagement.</p>
            next_token: <p>The pagination token to continue to the next page of results.</p>
            max_results: <p>The maximum number of engagements to contact channels to list per page of results.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_pages_by_engagement_request.ListPagesByEngagementRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_pages_by_engagement_result.ListPagesByEngagementResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_pages_by_engagement

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_pages_by_engagement.list_pages_by_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_pages_by_engagement_request.ListPagesByEngagementRequest = {
            "engagement_id": engagement_id
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

    def iter_list_pages_by_engagement(
        self,
        engagement_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.page.Page]":
        _token = next_token
        while True:
            _response = self.list_pages_by_engagement(
                engagement_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("pages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_preview_rotation_shifts(
        self,
        end_time: "capo_ssm_contacts.types.date_time.DateTime",
        members: "capo_ssm_contacts.types.rotation_preview_member_list.RotationPreviewMemberList",
        time_zone_id: "capo_ssm_contacts.types.time_zone_id.TimeZoneId",
        recurrence: "capo_ssm_contacts.types.recurrence_settings.RecurrenceSettings",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        rotation_start_time: Optional[
            "capo_ssm_contacts.types.date_time.DateTime"
        ] = None,
        start_time: Optional["capo_ssm_contacts.types.date_time.DateTime"] = None,
        overrides: Optional[
            "capo_ssm_contacts.types.override_list.OverrideList"
        ] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_contacts.types.list_preview_rotation_shifts_result.ListPreviewRotationShiftsResult":
        """<p>Returns a list of shifts based on rotation configuration parameters.</p> <note> <p>The Incident Manager primarily uses this operation to populate the <b>Preview</b> calendar. It is not typically run by end users.</p> </note>

        Args:
            rotation_start_time: <p>The date and time a rotation would begin. The first shift is calculated from this date and time.</p>
            start_time: <p>Used to filter the range of calculated shifts before sending the response back to the user. </p>
            end_time: <p>The date and time a rotation shift would end.</p>
            members: <p>The contacts that would be assigned to a rotation.</p>
            time_zone_id: <p>The time zone the rotation’s activity would be based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". </p>
            recurrence: <p>Information about how long a rotation would last before restarting at the beginning of the shift order.</p>
            overrides: <p>Information about changes that would be made in a rotation override.</p>
            next_token: <p>A token to start the list. This token is used to get the next set of results.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that can be specified in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_preview_rotation_shifts_request.ListPreviewRotationShiftsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_preview_rotation_shifts_result.ListPreviewRotationShiftsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_preview_rotation_shifts

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_preview_rotation_shifts.list_preview_rotation_shifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_preview_rotation_shifts_request.ListPreviewRotationShiftsRequest = {
            "end_time": end_time,
            "members": members,
            "time_zone_id": time_zone_id,
            "recurrence": recurrence,
        }
        if rotation_start_time is not None:
            input_["rotation_start_time"] = rotation_start_time
        if start_time is not None:
            input_["start_time"] = start_time
        if overrides is not None:
            input_["overrides"] = overrides
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

    def iter_list_preview_rotation_shifts(
        self,
        end_time: "capo_ssm_contacts.types.date_time.DateTime",
        members: "capo_ssm_contacts.types.rotation_preview_member_list.RotationPreviewMemberList",
        time_zone_id: "capo_ssm_contacts.types.time_zone_id.TimeZoneId",
        recurrence: "capo_ssm_contacts.types.recurrence_settings.RecurrenceSettings",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        rotation_start_time: Optional[
            "capo_ssm_contacts.types.date_time.DateTime"
        ] = None,
        start_time: Optional["capo_ssm_contacts.types.date_time.DateTime"] = None,
        overrides: Optional[
            "capo_ssm_contacts.types.override_list.OverrideList"
        ] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.rotation_shift.RotationShift]":
        _token = next_token
        while True:
            _response = self.list_preview_rotation_shifts(
                end_time,
                members,
                time_zone_id,
                recurrence,
                config_overrides=config_overrides,
                rotation_start_time=rotation_start_time,
                start_time=start_time,
                overrides=overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("rotation_shifts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_rotation_overrides(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        start_time: "capo_ssm_contacts.types.date_time.DateTime",
        end_time: "capo_ssm_contacts.types.date_time.DateTime",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_contacts.types.list_rotation_overrides_result.ListRotationOverridesResult":
        """<p>Retrieves a list of overrides currently specified for an on-call rotation.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the rotation to retrieve information about.</p>
            start_time: <p>The date and time for the beginning of a time range for listing overrides.</p>
            end_time: <p>The date and time for the end of a time range for listing overrides.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_rotation_overrides_request.ListRotationOverridesRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_rotation_overrides_result.ListRotationOverridesResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_rotation_overrides

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_rotation_overrides.list_rotation_overrides(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_rotation_overrides_request.ListRotationOverridesRequest = {
            "rotation_id": rotation_id,
            "start_time": start_time,
            "end_time": end_time,
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

    def iter_list_rotation_overrides(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        start_time: "capo_ssm_contacts.types.date_time.DateTime",
        end_time: "capo_ssm_contacts.types.date_time.DateTime",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.rotation_override.RotationOverride]":
        _token = next_token
        while True:
            _response = self.list_rotation_overrides(
                rotation_id,
                start_time,
                end_time,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("rotation_overrides",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_rotations(
        self,
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        rotation_name_prefix: Optional[
            "capo_ssm_contacts.types.rotation_name.RotationName"
        ] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_contacts.types.list_rotations_result.ListRotationsResult":
        """<p>Retrieves a list of on-call rotations.</p>

        Args:
            rotation_name_prefix: <p>A filter to include rotations in list results based on their common prefix. For example, entering prod returns a list of all rotation names that begin with <code>prod</code>, such as <code>production</code> and <code>prod-1</code>.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_rotations_request.ListRotationsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_rotations_result.ListRotationsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_rotations

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_rotations.list_rotations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_rotations_request.ListRotationsRequest = {}
        if rotation_name_prefix is not None:
            input_["rotation_name_prefix"] = rotation_name_prefix
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

    def iter_list_rotations(
        self,
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        rotation_name_prefix: Optional[
            "capo_ssm_contacts.types.rotation_name.RotationName"
        ] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.rotation.Rotation]":
        _token = next_token
        while True:
            _response = self.list_rotations(
                config_overrides=config_overrides,
                rotation_name_prefix=rotation_name_prefix,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("rotations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_rotation_shifts(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        end_time: "capo_ssm_contacts.types.date_time.DateTime",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        start_time: Optional["capo_ssm_contacts.types.date_time.DateTime"] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm_contacts.types.list_rotation_shifts_result.ListRotationShiftsResult":
        """<p>Returns a list of shifts generated by an existing rotation in the system.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the rotation to retrieve shift information about. </p>
            start_time: <p>The date and time for the beginning of the time range to list shifts for.</p>
            end_time: <p>The date and time for the end of the time range to list shifts for.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_rotation_shifts_request.ListRotationShiftsRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_rotation_shifts_result.ListRotationShiftsResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_rotation_shifts

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_rotation_shifts.list_rotation_shifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_rotation_shifts_request.ListRotationShiftsRequest = {
            "rotation_id": rotation_id,
            "end_time": end_time,
        }
        if start_time is not None:
            input_["start_time"] = start_time
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

    def iter_list_rotation_shifts(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        end_time: "capo_ssm_contacts.types.date_time.DateTime",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        start_time: Optional["capo_ssm_contacts.types.date_time.DateTime"] = None,
        next_token: Optional[
            "capo_ssm_contacts.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_ssm_contacts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_ssm_contacts.types.rotation_shift.RotationShift]":
        _token = next_token
        while True:
            _response = self.list_rotation_shifts(
                rotation_id,
                end_time,
                config_overrides=config_overrides,
                start_time=start_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("rotation_shifts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_ssm_contacts.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.list_tags_for_resource_result.ListTagsForResourceResult":
        """<p>Lists the tags of a contact, escalation plan, rotation, or on-call schedule.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the contact, escalation plan, rotation, or on-call schedule.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.list_tags_for_resource

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_contact_policy(
        self,
        contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        policy: "capo_ssm_contacts.types.policy.Policy",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.put_contact_policy_result.PutContactPolicyResult":
        """<p>Adds a resource policy to the specified contact or escalation plan. The resource policy is used to share the contact or escalation plan using Resource Access Manager (RAM). For more information about cross-account sharing, see <a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/xa.html">Setting up cross-account functionality</a>.</p>

        Args:
            contact_arn: <p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>
            policy: <p>Details of the resource policy.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.put_contact_policy_request.PutContactPolicyRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.put_contact_policy_result.PutContactPolicyResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.put_contact_policy

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.put_contact_policy.put_contact_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.put_contact_policy_request.PutContactPolicyRequest = {
            "contact_arn": contact_arn,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_activation_code(
        self,
        contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.send_activation_code_result.SendActivationCodeResult":
        """<p>Sends an activation code to a contact channel. The contact can use this code to activate the contact channel in the console or with the <code>ActivateChannel</code> operation. Incident Manager can't engage a contact channel until it has been activated.</p>

        Args:
            contact_channel_id: <p>The Amazon Resource Name (ARN) of the contact channel.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.send_activation_code_request.SendActivationCodeRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.send_activation_code_result.SendActivationCodeResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.send_activation_code

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.send_activation_code.send_activation_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.send_activation_code_request.SendActivationCodeRequest = {
            "contact_channel_id": contact_channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_engagement(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        sender: "capo_ssm_contacts.types.sender.Sender",
        subject: "capo_ssm_contacts.types.subject.Subject",
        content: "capo_ssm_contacts.types.content.Content",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        public_subject: Optional[
            "capo_ssm_contacts.types.public_subject.PublicSubject"
        ] = None,
        public_content: Optional[
            "capo_ssm_contacts.types.public_content.PublicContent"
        ] = None,
        incident_id: Optional["capo_ssm_contacts.types.incident_id.IncidentId"] = None,
        idempotency_token: Optional[
            "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_ssm_contacts.types.start_engagement_result.StartEngagementResult":
        """<p>Starts an engagement to a contact or escalation plan. The engagement engages each contact specified in the incident.</p>

        Args:
            contact_id: <p>The Amazon Resource Name (ARN) of the contact being engaged.</p>
            sender: <p>The user that started the engagement.</p>
            subject: <p>The secure subject of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> or <code>EMAIL</code>.</p>
            content: <p>The secure content of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> or <code>EMAIL</code>.</p>
            public_subject: <p>The insecure subject of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>
            public_content: <p>The insecure content of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>
            incident_id: <p>The ARN of the incident that the engagement is part of.</p>
            idempotency_token: <p>A token ensuring that the operation is called only once with the specified details.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.start_engagement_request.StartEngagementRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.start_engagement_result.StartEngagementResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.start_engagement

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.start_engagement.start_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.start_engagement_request.StartEngagementRequest = {
            "contact_id": contact_id,
            "sender": sender,
            "subject": subject,
            "content": content,
        }
        if public_subject is not None:
            input_["public_subject"] = public_subject
        if public_content is not None:
            input_["public_content"] = public_content
        if incident_id is not None:
            input_["incident_id"] = incident_id
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_engagement(
        self,
        engagement_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        reason: Optional["capo_ssm_contacts.types.stop_reason.StopReason"] = None,
    ) -> "capo_ssm_contacts.types.stop_engagement_result.StopEngagementResult":
        """<p>Stops an engagement before it finishes the final stage of the escalation plan or engagement plan. Further contacts aren't engaged.</p>

        Args:
            engagement_id: <p>The Amazon Resource Name (ARN) of the engagement.</p>
            reason: <p>The reason that you're stopping the engagement.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.stop_engagement_request.StopEngagementRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.stop_engagement_result.StopEngagementResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.stop_engagement

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.stop_engagement.stop_engagement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.stop_engagement_request.StopEngagementRequest = {
            "engagement_id": engagement_id
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

    def tag_resource(
        self,
        resource_arn: "capo_ssm_contacts.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_ssm_contacts.types.tags_list.TagsList",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.tag_resource_result.TagResourceResult":
        """<p>Tags a contact or escalation plan. You can tag only contacts and escalation plans in the first region of your replication set.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>
            tags: <p>A list of tags that you are adding to the contact or escalation plan.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.tag_resource_result.TagResourceResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.tag_resource

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_ssm_contacts.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_ssm_contacts.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
    ) -> "capo_ssm_contacts.types.untag_resource_result.UntagResourceResult":
        """<p>Removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>
            tag_keys: <p>The key of the tag that you want to remove.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.untag_resource_result.UntagResourceResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.untag_resource

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.untag_resource_request.UntagResourceRequest = {
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

    def update_contact(
        self,
        contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        display_name: Optional[
            "capo_ssm_contacts.types.contact_name.ContactName"
        ] = None,
        plan: Optional["capo_ssm_contacts.types.plan.Plan"] = None,
    ) -> "capo_ssm_contacts.types.update_contact_result.UpdateContactResult":
        """<p>Updates the contact or escalation plan specified.</p>

        Args:
            contact_id: <p>The Amazon Resource Name (ARN) of the contact or escalation plan you're updating.</p>
            display_name: <p>The full name of the contact or escalation plan.</p>
            plan: <p>A list of stages. A contact has an engagement plan with stages for specified contact channels. An escalation plan uses these stages to contact specified contacts.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.update_contact_request.UpdateContactRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.update_contact_result.UpdateContactResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.update_contact

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.update_contact.update_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.update_contact_request.UpdateContactRequest = {
            "contact_id": contact_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if plan is not None:
            input_["plan"] = plan

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_contact_channel(
        self,
        contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        name: Optional["capo_ssm_contacts.types.channel_name.ChannelName"] = None,
        delivery_address: Optional[
            "capo_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
        ] = None,
    ) -> "capo_ssm_contacts.types.update_contact_channel_result.UpdateContactChannelResult":
        """<p>Updates a contact's contact channel.</p>

        Args:
            contact_channel_id: <p>The Amazon Resource Name (ARN) of the contact channel you want to update.</p>
            name: <p>The name of the contact channel.</p>
            delivery_address: <p>The details that Incident Manager uses when trying to engage the contact channel.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.data_encryption_exception.DataEncryptionException: <p>The operation failed to due an encryption key error.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.update_contact_channel_request.UpdateContactChannelRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.update_contact_channel_result.UpdateContactChannelResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.update_contact_channel

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.update_contact_channel.update_contact_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.update_contact_channel_request.UpdateContactChannelRequest = {
            "contact_channel_id": contact_channel_id
        }
        if name is not None:
            input_["name"] = name
        if delivery_address is not None:
            input_["delivery_address"] = delivery_address

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rotation(
        self,
        rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn",
        recurrence: "capo_ssm_contacts.types.recurrence_settings.RecurrenceSettings",
        *,
        config_overrides: Optional[SSMContactsClientConfig] = None,
        contact_ids: Optional[
            "capo_ssm_contacts.types.rotation_contacts_arn_list.RotationContactsArnList"
        ] = None,
        start_time: Optional["capo_ssm_contacts.types.date_time.DateTime"] = None,
        time_zone_id: Optional[
            "capo_ssm_contacts.types.time_zone_id.TimeZoneId"
        ] = None,
    ) -> "capo_ssm_contacts.types.update_rotation_result.UpdateRotationResult":
        """<p>Updates the information specified for an on-call rotation.</p>

        Args:
            rotation_id: <p>The Amazon Resource Name (ARN) of the rotation to update.</p>
            contact_ids: <p>The Amazon Resource Names (ARNs) of the contacts to include in the updated rotation. </p> <note> <p>Only the <code>PERSONAL</code> contact type is supported. The contact types <code>ESCALATION</code> and <code>ONCALL_SCHEDULE</code> are not supported for this operation. </p> </note> <p>The order in which you list the contacts is their shift order in the rotation schedule.</p>
            start_time: <p>The date and time the rotation goes into effect.</p>
            time_zone_id: <p>The time zone to base the updated rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the <a href="https://www.iana.org/time-zones">Time Zone Database</a> on the IANA website.</p> <note> <p>Designators for time zones that don’t support Daylight Savings Time Rules, such as Pacific Standard Time (PST), aren't supported.</p> </note>
            recurrence: <p>Information about how long the updated rotation lasts before restarting at the beginning of the shift order.</p>

        Raises:
            capo_ssm_contacts.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_contacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_contacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error occurred while processing the request.</p>
            capo_ssm_contacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource that doesn't exist.</p>
            capo_ssm_contacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_contacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_contacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_contacts.types.update_rotation_request.UpdateRotationRequest]",
        ) -> OperationResponse[
            "capo_ssm_contacts.types.update_rotation_result.UpdateRotationResult"
        ]:
            import capo_ssm_contacts._operations.ssm_contacts.update_rotation

            output, http_response = (
                capo_ssm_contacts._operations.ssm_contacts.update_rotation.update_rotation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_contacts.types.update_rotation_request.UpdateRotationRequest = {
            "rotation_id": rotation_id,
            "recurrence": recurrence,
        }
        if contact_ids is not None:
            input_["contact_ids"] = contact_ids
        if start_time is not None:
            input_["start_time"] = start_time
        if time_zone_id is not None:
            input_["time_zone_id"] = time_zone_id

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

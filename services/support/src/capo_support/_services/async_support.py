"""Generated from Smithy shape ``com.amazonaws.support#AWSSupport_20130415``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_support._auth._signers
import capo_support._auth._sigv4
from capo_support._auth._identity import Credentials
from capo_support._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_support._auth._zapros_handler import AuthMiddleware
from capo_support._pagination import resolve_path as _resolve_path
from capo_support._services._aws_config import aaws_config
from capo_support._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_support.types.add_attachments_to_set_request
    import capo_support.types.add_attachments_to_set_response
    import capo_support.types.add_communication_to_case_request
    import capo_support.types.add_communication_to_case_response
    import capo_support.types.after_time
    import capo_support.types.attachment_id
    import capo_support.types.attachment_set_id
    import capo_support.types.attachments
    import capo_support.types.before_time
    import capo_support.types.case_details
    import capo_support.types.case_id
    import capo_support.types.case_id_list
    import capo_support.types.category_code
    import capo_support.types.cc_email_address_list
    import capo_support.types.communication
    import capo_support.types.communication_body
    import capo_support.types.complete_attachment_upload_request
    import capo_support.types.complete_attachment_upload_response
    import capo_support.types.completed_upload_list
    import capo_support.types.create_case_request
    import capo_support.types.create_case_response
    import capo_support.types.describe_attachment_request
    import capo_support.types.describe_attachment_response
    import capo_support.types.describe_attachment_upload_status_request
    import capo_support.types.describe_attachment_upload_status_response
    import capo_support.types.describe_cases_request
    import capo_support.types.describe_cases_response
    import capo_support.types.describe_communications_request
    import capo_support.types.describe_communications_response
    import capo_support.types.describe_create_case_options_request
    import capo_support.types.describe_create_case_options_response
    import capo_support.types.describe_services_request
    import capo_support.types.describe_services_response
    import capo_support.types.describe_severity_levels_request
    import capo_support.types.describe_severity_levels_response
    import capo_support.types.describe_supported_languages_request
    import capo_support.types.describe_supported_languages_response
    import capo_support.types.describe_trusted_advisor_check_refresh_statuses_request
    import capo_support.types.describe_trusted_advisor_check_refresh_statuses_response
    import capo_support.types.describe_trusted_advisor_check_result_request
    import capo_support.types.describe_trusted_advisor_check_result_response
    import capo_support.types.describe_trusted_advisor_check_summaries_request
    import capo_support.types.describe_trusted_advisor_check_summaries_response
    import capo_support.types.describe_trusted_advisor_checks_request
    import capo_support.types.describe_trusted_advisor_checks_response
    import capo_support.types.display_id
    import capo_support.types.file_name
    import capo_support.types.file_size
    import capo_support.types.get_attachment_download_link_request
    import capo_support.types.get_attachment_download_link_response
    import capo_support.types.get_attachment_upload_links_request
    import capo_support.types.get_attachment_upload_links_response
    import capo_support.types.include_communications
    import capo_support.types.include_resolved_cases
    import capo_support.types.issue_type
    import capo_support.types.language
    import capo_support.types.max_results
    import capo_support.types.next_token
    import capo_support.types.nullable_boolean_type
    import capo_support.types.refresh_trusted_advisor_check_request
    import capo_support.types.refresh_trusted_advisor_check_response
    import capo_support.types.resolve_case_request
    import capo_support.types.resolve_case_response
    import capo_support.types.service_code2
    import capo_support.types.service_code_list
    import capo_support.types.severity_code
    import capo_support.types.string
    import capo_support.types.string_list
    import capo_support.types.subject
    import capo_support.types.upload_id
    import capo_support.types.upload_ids
    import capo_support.types.upload_range
    import capo_support.types.validated_category_code
    import capo_support.types.validated_issue_type_string
    import capo_support.types.validated_service_code


class AsyncSupportClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSupportClient:
    """A client for the ``Support`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncSupportClientConfig(
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
        self, config_overrides: Optional[AsyncSupportClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSupportClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def add_attachments_to_set(
        self,
        attachments: "capo_support.types.attachments.Attachments",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        attachment_set_id: Optional[
            "capo_support.types.attachment_set_id.AttachmentSetId"
        ] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> (
        "capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse"
    ):
        """<p>Adds one or more attachments to an attachment set. </p> <p>An attachment set is a temporary container for attachments that you add to a case or case communication. The set is available for 1 hour after it's created. The <code>expiryTime</code> returned in the response is when the set expires. </p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            attachment_set_id: <p>The ID of the attachment set. If an <code>attachmentSetId</code> is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an <code>attachmentSetId</code> is specified, the attachments are added to the specified set, if it exists.</p>
            attachments: <p>One or more attachments to add to the set. You can add up to three attachments per set. The size limit is 5 MB per attachment.</p> <p>In the <code>Attachment</code> object, use the <code>data</code> parameter to specify the contents of the attachment file. In the previous request syntax, the value for <code>data</code> appear as <code>blob</code>, which is represented as a base64-encoded string. The value for <code>fileName</code> is the name of the attachment, such as <code>troubleshoot-screenshot.png</code>.</p>
            dry_run: <p>Specifies whether to validate the request without actually adding the attachments. When set to <code>true</code>, the request is validated but no attachments are stored, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.attachment_limit_exceeded.AttachmentLimitExceeded: <p>The limit for the number of attachment sets created in a short period of time has been exceeded.</p>
            capo_support.errors.attachment_set_expired.AttachmentSetExpired: <p>The expiration time of the attachment set has passed. The set expires 1 hour after it is created.</p>
            capo_support.errors.attachment_set_id_not_found.AttachmentSetIdNotFound: <p>An attachment set with the specified ID could not be found.</p>
            capo_support.errors.attachment_set_size_limit_exceeded.AttachmentSetSizeLimitExceeded: <p>A limit for the size of an attachment set has been exceeded. The limits are three attachments and 5 MB per attachment.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.add_attachments_to_set_request.AddAttachmentsToSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse"
        ]:
            import capo_support._operations.aws_support_20130415.add_attachments_to_set

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.add_attachments_to_set.async_add_attachments_to_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.add_attachments_to_set_request.AddAttachmentsToSetRequest = {
            "attachments": attachments
        }
        if attachment_set_id is not None:
            input_["attachment_set_id"] = attachment_set_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_communication_to_case(
        self,
        communication_body: "capo_support.types.communication_body.CommunicationBody",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id: Optional["capo_support.types.case_id.CaseId"] = None,
        cc_email_addresses: Optional[
            "capo_support.types.cc_email_address_list.CcEmailAddressList"
        ] = None,
        attachment_set_id: Optional[
            "capo_support.types.attachment_set_id.AttachmentSetId"
        ] = None,
        upload_ids: Optional["capo_support.types.upload_ids.UploadIds"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.add_communication_to_case_response.AddCommunicationToCaseResponse":
        """<p>Adds additional customer communication to a Amazon Web Services Support case. Use the <code>caseId</code> parameter to identify the case to which to add communication. To list a set of email addresses to copy on the communication, use the <code>ccEmailAddresses</code> parameter. The <code>communicationBody</code> value contains the text of the communication.</p> <p>To attach files larger than 5 MB to the communication, use the <code>uploadIds</code> parameter.</p> <important> <p>Amazon Web Services Support automatically redacts sensitive information from support cases to protect your data. The following information is replaced with <code>[REDACTED_BY_Amazon Web Services]</code> and is not stored:</p> <ul> <li> <p>Amazon Web Services secret keys - The complete key is replaced. Example: <code>[REDACTED_BY_Amazon Web Services]</code> </p> </li> <li> <p>Private keys - The complete key is replaced. Example: <code>[REDACTED_BY_Amazon Web Services]</code> </p> </li> <li> <p>Credit card numbers - The number is redacted, but the last 4 digits remain. Example: <code>[REDACTED_BY_Amazon Web Services]-7016</code> </p> </li> </ul> <p>This sensitive information is never required by Amazon Web Services Support.</p> </important> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            case_id: <p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>
            communication_body: <p>The body of an email communication to add to the support case.</p>
            cc_email_addresses: <p>The email addresses in the CC line of an email to be added to the support case.</p>
            attachment_set_id: <p>The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling <a>AddAttachmentsToSet</a>. Each attachment in the set must be 5 MB or smaller. To attach files larger than 5 MB, use <code>uploadIds</code>.</p>
            upload_ids: <p>A list of upload IDs that identify attachments to add to the case. Each <code>uploadId</code> is returned by the <a>GetAttachmentUploadLinks</a> operation. The upload must reach the <code>attachment-ready</code> state by calling <a>CompleteAttachmentUpload</a> before it can be passed here. Use <code>uploadIds</code> to attach files of any supported size, including files larger than 5 MB.</p>
            dry_run: <p>Specifies whether to validate the request without actually adding the communication to the case. When set to <code>true</code>, the request is validated but the communication isn't added, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.attachment_set_expired.AttachmentSetExpired: <p>The expiration time of the attachment set has passed. The set expires 1 hour after it is created.</p>
            capo_support.errors.attachment_set_id_not_found.AttachmentSetIdNotFound: <p>An attachment set with the specified ID could not be found.</p>
            capo_support.errors.case_id_not_found.CaseIdNotFound: <p>The requested <code>caseId</code> couldn't be located.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.add_communication_to_case_request.AddCommunicationToCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.add_communication_to_case_response.AddCommunicationToCaseResponse"
        ]:
            import capo_support._operations.aws_support_20130415.add_communication_to_case

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.add_communication_to_case.async_add_communication_to_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.add_communication_to_case_request.AddCommunicationToCaseRequest = {
            "communication_body": communication_body
        }
        if case_id is not None:
            input_["case_id"] = case_id
        if cc_email_addresses is not None:
            input_["cc_email_addresses"] = cc_email_addresses
        if attachment_set_id is not None:
            input_["attachment_set_id"] = attachment_set_id
        if upload_ids is not None:
            input_["upload_ids"] = upload_ids
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def complete_attachment_upload(
        self,
        upload_id: "capo_support.types.upload_id.UploadId",
        completed_uploads: "capo_support.types.completed_upload_list.CompletedUploadList",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.complete_attachment_upload_response.CompleteAttachmentUploadResponse":
        """<p>Completes an attachment upload that was started with <a>GetAttachmentUploadLinks</a>. After you upload a part of the file to its presigned Amazon S3 URL, call <code>CompleteAttachmentUpload</code> with the <code>partIndex</code> and <code>eTag</code> of that part. You can include one part per call, or multiple parts in a single call. After <code>CompleteAttachmentUpload</code> has been called for every part of the file, the service processes the upload asynchronously. The <code>attachment-ready</code> status might not be reflected immediately. Use <a>DescribeAttachmentUploadStatus</a> to poll for the <code>uploadStatus</code> to become <code>attachment-ready</code> before passing the <code>uploadId</code> to <a>CreateCase</a> or <a>AddCommunicationToCase</a>.</p>

        Args:
            upload_id: <p>The identifier associated with the upload to complete.</p>
            completed_uploads: <p>The list of parts being reported as completed in this call. Each entry must contain the <code>partIndex</code> of an uploaded part and the <code>ETag</code> returned by Amazon S3 when that part was uploaded.</p>
            dry_run: <p>Specifies whether to validate the request without actually completing the upload. When set to <code>true</code>, the request is validated but the upload isn't finalized, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.upload_id_not_found.UploadIdNotFound: <p>The specified <code>uploadId</code> couldn't be located.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.complete_attachment_upload_request.CompleteAttachmentUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.complete_attachment_upload_response.CompleteAttachmentUploadResponse"
        ]:
            import capo_support._operations.aws_support_20130415.complete_attachment_upload

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.complete_attachment_upload.async_complete_attachment_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.complete_attachment_upload_request.CompleteAttachmentUploadRequest = {
            "upload_id": upload_id,
            "completed_uploads": completed_uploads,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_case(
        self,
        subject: "capo_support.types.subject.Subject",
        communication_body: "capo_support.types.communication_body.CommunicationBody",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        service_code: Optional["capo_support.types.service_code2.ServiceCode2"] = None,
        severity_code: Optional["capo_support.types.severity_code.SeverityCode"] = None,
        category_code: Optional["capo_support.types.category_code.CategoryCode"] = None,
        cc_email_addresses: Optional[
            "capo_support.types.cc_email_address_list.CcEmailAddressList"
        ] = None,
        language: Optional["capo_support.types.language.Language"] = None,
        issue_type: Optional["capo_support.types.issue_type.IssueType"] = None,
        attachment_set_id: Optional[
            "capo_support.types.attachment_set_id.AttachmentSetId"
        ] = None,
        upload_ids: Optional["capo_support.types.upload_ids.UploadIds"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.create_case_response.CreateCaseResponse":
        """<p>Creates a case in the Amazon Web Services Support Center. This operation is similar to how you create a case in the Amazon Web Services Support Center <a href="https://console.aws.amazon.com/support/home#/case/create">Create Case</a> page.</p> <p>The Amazon Web Services Support API doesn't support requesting service limit increases. You can submit a service limit increase in the following ways: </p> <ul> <li> <p>Submit a request from the Amazon Web Services Support Center <a href="https://console.aws.amazon.com/support/home#/case/create">Create Case</a> page.</p> </li> <li> <p>Use the Service Quotas <a href="https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html">RequestServiceQuotaIncrease</a> operation.</p> </li> </ul> <important> <p>Amazon Web Services Support automatically redacts sensitive information from support cases to protect your data. The following information is replaced with <code>[REDACTED_BY_Amazon Web Services]</code> and is not stored:</p> <ul> <li> <p>Amazon Web Services secret keys - The complete key is replaced. Example: <code>[REDACTED_BY_Amazon Web Services]</code> </p> </li> <li> <p>Private keys - The complete key is replaced. Example: <code>[REDACTED_BY_Amazon Web Services]</code> </p> </li> <li> <p>Credit card numbers - The number is redacted, but the last 4 digits remain. Example: <code>[REDACTED_BY_Amazon Web Services]-7016</code> </p> </li> </ul> <p>This sensitive information is never required by Amazon Web Services Support.</p> </important> <p>A successful <code>CreateCase</code> request returns a Amazon Web Services Support case number. You can use the <a>DescribeCases</a> operation and specify the case number to get existing Amazon Web Services Support cases. After you create a case, use the <a>AddCommunicationToCase</a> operation to add additional communication or attachments to an existing case.</p> <p>The <code>caseId</code> is separate from the <code>displayId</code> that appears in the <a href="https://console.aws.amazon.com/support">Amazon Web Services Support Center</a>. Use the <a>DescribeCases</a> operation to get the <code>displayId</code>.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            subject: <p>The title of the support case. The title appears in the <b>Subject</b> field on the Amazon Web Services Support Center <a href="https://console.aws.amazon.com/support/home#/case/create">Create Case</a> page.</p>
            service_code: <p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>
            severity_code: <p>A value that indicates the urgency of the case. This value determines the response time according to your service level agreement with Amazon Web Services Support. You can use the <a>DescribeSeverityLevels</a> operation to get the possible values for <code>severityCode</code>. </p> <p>For more information, see <a>SeverityLevel</a> and <a href="https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity">Choosing a Severity</a> in the <i>Amazon Web Services Support User Guide</i>.</p> <note> <p>The availability of severity levels depends on the support plan for the Amazon Web Services account.</p> </note>
            category_code: <p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>
            communication_body: <p>The communication body text that describes the issue. This text appears in the <b>Description</b> field on the Amazon Web Services Support Center <a href="https://console.aws.amazon.com/support/home#/case/create">Create Case</a> page.</p>
            cc_email_addresses: <p>A list of email addresses that Amazon Web Services Support copies on case correspondence. Amazon Web Services Support identifies the account that creates the case when you specify your Amazon Web Services credentials in an HTTP POST method or use the <a href="http://aws.amazon.com/tools/">Amazon Web Services SDKs</a>. </p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            issue_type: <p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>
            attachment_set_id: <p>The ID of a set of one or more attachments for the case. Create the set by using the <a>AddAttachmentsToSet</a> operation. Each attachment in the set must be 5 MB or smaller. To attach files larger than 5 MB, use <code>uploadIds</code>.</p>
            upload_ids: <p>A list of upload IDs that identify attachments to add to the case. Each <code>uploadId</code> is returned by the <a>GetAttachmentUploadLinks</a> operation. The upload must reach the <code>attachment-ready</code> state by calling <a>CompleteAttachmentUpload</a> before it can be passed here. Use <code>uploadIds</code> to attach files of any supported size, including files larger than 5 MB.</p>
            dry_run: <p>Specifies whether to validate the request without actually creating the case. When set to <code>true</code>, the request is validated but no case is created, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.attachment_set_expired.AttachmentSetExpired: <p>The expiration time of the attachment set has passed. The set expires 1 hour after it is created.</p>
            capo_support.errors.attachment_set_id_not_found.AttachmentSetIdNotFound: <p>An attachment set with the specified ID could not be found.</p>
            capo_support.errors.case_creation_limit_exceeded.CaseCreationLimitExceeded: <p>The case creation limit for the account has been exceeded.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.create_case_request.CreateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.create_case_response.CreateCaseResponse"
        ]:
            import capo_support._operations.aws_support_20130415.create_case

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.create_case.async_create_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.create_case_request.CreateCaseRequest = {
            "subject": subject,
            "communication_body": communication_body,
        }
        if service_code is not None:
            input_["service_code"] = service_code
        if severity_code is not None:
            input_["severity_code"] = severity_code
        if category_code is not None:
            input_["category_code"] = category_code
        if cc_email_addresses is not None:
            input_["cc_email_addresses"] = cc_email_addresses
        if language is not None:
            input_["language"] = language
        if issue_type is not None:
            input_["issue_type"] = issue_type
        if attachment_set_id is not None:
            input_["attachment_set_id"] = attachment_set_id
        if upload_ids is not None:
            input_["upload_ids"] = upload_ids
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_attachment(
        self,
        attachment_id: "capo_support.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_attachment_response.DescribeAttachmentResponse":
        """<p>Returns the attachment that has the specified ID. Attachments can include screenshots, error logs, or other files that describe your issue. Attachment IDs are generated by the case management system when you add an attachment to a case or case communication. Attachment IDs are returned in the <a>AttachmentDetails</a> objects that are returned by the <a>DescribeCommunications</a> operation.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <important> <p> <code>DescribeAttachment</code> can't return attachments larger than 5 MB. If the specified <code>attachmentId</code> refers to an attachment larger than 5 MB, the request fails with <code>InvalidParameterValueException</code>.</p> <p>To download an attachment of any size, including attachments larger than 5 MB, use <a>GetAttachmentDownloadLink</a>. <code>GetAttachmentDownloadLink</code> returns an Amazon S3 presigned URL that you can use to download the attachment directly.</p> </important>

        Args:
            attachment_id: <p>The ID of the attachment to return. Attachment IDs are returned by the <a>DescribeCommunications</a> operation.</p> <p>If the specified attachment is larger than 5 MB, this operation returns <code>InvalidParameterValueException</code>. To download attachments larger than 5 MB, use <a>GetAttachmentDownloadLink</a>.</p>
            dry_run: <p>Specifies whether to validate the request without actually retrieving the attachment. When set to <code>true</code>, the request is validated but no attachment content is returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.attachment_id_not_found.AttachmentIdNotFound: <p>An attachment with the specified ID could not be found.</p>
            capo_support.errors.describe_attachment_limit_exceeded.DescribeAttachmentLimitExceeded: <p>The limit for the number of <a>DescribeAttachment</a> requests in a short period of time has been exceeded.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_attachment_request.DescribeAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_attachment_response.DescribeAttachmentResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_attachment

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_attachment.async_describe_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_attachment_request.DescribeAttachmentRequest = {
            "attachment_id": attachment_id
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_attachment_upload_status(
        self,
        upload_id: "capo_support.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_attachment_upload_status_response.DescribeAttachmentUploadStatusResponse":
        """<p>Returns the current status, file name, and progress of a multipart attachment upload that was started with <a>GetAttachmentUploadLinks</a>. Use this operation to track where an upload is in the workflow. While parts are still being uploaded and reported through <a>CompleteAttachmentUpload</a>, the <code>uploadStatus</code> is <code>attachment-not-ready</code> and <code>uploadProgress</code> reports the total number of parts and how many have been completed so far. After every part has been reported and the service finishes processing the upload asynchronously, the <code>uploadStatus</code> becomes <code>attachment-ready</code> and the <code>uploadId</code> can be attached to a case through <a>CreateCase</a> or <a>AddCommunicationToCase</a>.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            upload_id: <p>The unique identifier for the upload. The <code>uploadId</code> is returned by <a>GetAttachmentUploadLinks</a> when you initiate the upload.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning upload status. When set to <code>true</code>, the request is validated but no status is returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.upload_id_not_found.UploadIdNotFound: <p>The specified <code>uploadId</code> couldn't be located.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_attachment_upload_status_request.DescribeAttachmentUploadStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_attachment_upload_status_response.DescribeAttachmentUploadStatusResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_attachment_upload_status

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_attachment_upload_status.async_describe_attachment_upload_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_attachment_upload_status_request.DescribeAttachmentUploadStatusRequest = {
            "upload_id": upload_id
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cases(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id_list: Optional["capo_support.types.case_id_list.CaseIdList"] = None,
        display_id: Optional["capo_support.types.display_id.DisplayId"] = None,
        after_time: Optional["capo_support.types.after_time.AfterTime"] = None,
        before_time: Optional["capo_support.types.before_time.BeforeTime"] = None,
        include_resolved_cases: Optional[
            "capo_support.types.include_resolved_cases.IncludeResolvedCases"
        ] = None,
        next_token: Optional["capo_support.types.next_token.NextToken"] = None,
        max_results: Optional["capo_support.types.max_results.MaxResults"] = None,
        language: Optional["capo_support.types.language.Language"] = None,
        include_communications: Optional[
            "capo_support.types.include_communications.IncludeCommunications"
        ] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_cases_response.DescribeCasesResponse":
        """<p>Returns a list of cases that you specify by passing one or more case IDs. You can use the <code>afterTime</code> and <code>beforeTime</code> parameters to filter the cases by date. You can set values for the <code>includeResolvedCases</code> and <code>includeCommunications</code> parameters to specify how much information to return.</p> <p>The response returns the following in JSON format:</p> <ul> <li> <p>One or more <a href="https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html">CaseDetails</a> data types.</p> </li> <li> <p>One or more <code>nextToken</code> values, which specify where to paginate the returned records represented by the <code>CaseDetails</code> objects.</p> </li> </ul> <p>Case data is available for 24 months after creation. If a case was created more than 24 months ago, a request might return an error.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <important> <p>Each <a>Communication</a> returned by this operation includes attachment information in two fields:</p> <ul> <li> <p> <code>attachmentSet</code>: returns only attachments that are 5 MB or smaller. Attachments larger than 5 MB are not included in this field.</p> </li> <li> <p> <code>attachments</code>: returns all attachments regardless of size.</p> </li> </ul> <p>Amazon Web Services recommends that you use the <code>attachments</code> field and download each attachment with <a>GetAttachmentDownloadLink</a>, which supports attachments of any size. The <code>attachmentSet</code> field and <a>DescribeAttachment</a> return only attachments that are 5 MB or smaller.</p> </important>

        Args:
            case_id_list: <p>A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.</p>
            display_id: <p>The ID displayed for a case in the Amazon Web Services Support Center user interface.</p>
            after_time: <p>The start date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>
            before_time: <p>The end date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>
            include_resolved_cases: <p>Specifies whether to include resolved support cases in the <code>DescribeCases</code> response. By default, resolved cases aren't included.</p>
            next_token: <p>A resumption point for pagination.</p>
            max_results: <p>The maximum number of results to return before paginating.</p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            include_communications: <p>Specifies whether to include communications in the <code>DescribeCases</code> response. By default, communications are included.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning case data. When set to <code>true</code>, the request is validated but no cases are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.case_id_not_found.CaseIdNotFound: <p>The requested <code>caseId</code> couldn't be located.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_cases_request.DescribeCasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_cases_response.DescribeCasesResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_cases

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_cases.async_describe_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_cases_request.DescribeCasesRequest = {}
        if case_id_list is not None:
            input_["case_id_list"] = case_id_list
        if display_id is not None:
            input_["display_id"] = display_id
        if after_time is not None:
            input_["after_time"] = after_time
        if before_time is not None:
            input_["before_time"] = before_time
        if include_resolved_cases is not None:
            input_["include_resolved_cases"] = include_resolved_cases
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if include_communications is not None:
            input_["include_communications"] = include_communications
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cases(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id_list: Optional["capo_support.types.case_id_list.CaseIdList"] = None,
        display_id: Optional["capo_support.types.display_id.DisplayId"] = None,
        after_time: Optional["capo_support.types.after_time.AfterTime"] = None,
        before_time: Optional["capo_support.types.before_time.BeforeTime"] = None,
        include_resolved_cases: Optional[
            "capo_support.types.include_resolved_cases.IncludeResolvedCases"
        ] = None,
        next_token: Optional["capo_support.types.next_token.NextToken"] = None,
        max_results: Optional["capo_support.types.max_results.MaxResults"] = None,
        language: Optional["capo_support.types.language.Language"] = None,
        include_communications: Optional[
            "capo_support.types.include_communications.IncludeCommunications"
        ] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "AsyncIterator[capo_support.types.case_details.CaseDetails]":
        _token = next_token
        while True:
            _response = await self.describe_cases(
                config_overrides=config_overrides,
                case_id_list=case_id_list,
                display_id=display_id,
                after_time=after_time,
                before_time=before_time,
                include_resolved_cases=include_resolved_cases,
                next_token=_token,
                max_results=max_results,
                language=language,
                include_communications=include_communications,
                dry_run=dry_run,
            )
            _page = _resolve_path(_response, ("cases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_communications(
        self,
        case_id: "capo_support.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        before_time: Optional["capo_support.types.before_time.BeforeTime"] = None,
        after_time: Optional["capo_support.types.after_time.AfterTime"] = None,
        next_token: Optional["capo_support.types.next_token.NextToken"] = None,
        max_results: Optional["capo_support.types.max_results.MaxResults"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_communications_response.DescribeCommunicationsResponse":
        """<p>Returns communications and attachments for one or more support cases. Use the <code>afterTime</code> and <code>beforeTime</code> parameters to filter by date. You can use the <code>caseId</code> parameter to restrict the results to a specific case.</p> <p>Case data is available for 24 months after creation. If a case was created more than 24 months ago, a request for data might cause an error.</p> <p>You can use the <code>maxResults</code> and <code>nextToken</code> parameters to control the pagination of the results. Set <code>maxResults</code> to the number of cases that you want to display on each page, and use <code>nextToken</code> to specify the resumption of pagination.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <important> <p>Each <a>Communication</a> returned by this operation includes attachment information in two fields:</p> <ul> <li> <p> <code>attachmentSet</code>: returns only attachments that are 5 MB or smaller. Attachments larger than 5 MB are not included in this field.</p> </li> <li> <p> <code>attachments</code>: returns all attachments regardless of size.</p> </li> </ul> <p>Amazon Web Services recommends that you use the <code>attachments</code> field and download each attachment with <a>GetAttachmentDownloadLink</a>, which supports attachments of any size. The <code>attachmentSet</code> field and <a>DescribeAttachment</a> return only attachments that are 5 MB or smaller.</p> </important>

        Args:
            case_id: <p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>
            before_time: <p>The end date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>
            after_time: <p>The start date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>
            next_token: <p>A resumption point for pagination.</p>
            max_results: <p>The maximum number of results to return before paginating.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning communications. When set to <code>true</code>, the request is validated but no communications are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.case_id_not_found.CaseIdNotFound: <p>The requested <code>caseId</code> couldn't be located.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_communications_request.DescribeCommunicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_communications_response.DescribeCommunicationsResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_communications

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_communications.async_describe_communications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_communications_request.DescribeCommunicationsRequest = {
            "case_id": case_id
        }
        if before_time is not None:
            input_["before_time"] = before_time
        if after_time is not None:
            input_["after_time"] = after_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_communications(
        self,
        case_id: "capo_support.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        before_time: Optional["capo_support.types.before_time.BeforeTime"] = None,
        after_time: Optional["capo_support.types.after_time.AfterTime"] = None,
        next_token: Optional["capo_support.types.next_token.NextToken"] = None,
        max_results: Optional["capo_support.types.max_results.MaxResults"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "AsyncIterator[capo_support.types.communication.Communication]":
        _token = next_token
        while True:
            _response = await self.describe_communications(
                case_id,
                config_overrides=config_overrides,
                before_time=before_time,
                after_time=after_time,
                next_token=_token,
                max_results=max_results,
                dry_run=dry_run,
            )
            _page = _resolve_path(_response, ("communications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_create_case_options(
        self,
        issue_type: "capo_support.types.issue_type.IssueType",
        service_code: "capo_support.types.service_code2.ServiceCode2",
        language: "capo_support.types.language.Language",
        category_code: "capo_support.types.category_code.CategoryCode",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_create_case_options_response.DescribeCreateCaseOptionsResponse":
        """<p>Returns a list of CreateCaseOption types along with the corresponding supported hours and language availability. You can specify the <code>language</code> <code>categoryCode</code>, <code>issueType</code> and <code>serviceCode</code> used to retrieve the CreateCaseOptions.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            issue_type: <p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>
            service_code: <p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            category_code: <p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning case option data. When set to <code>true</code>, the request is validated but no options are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.throttling_exception.ThrottlingException: <p> You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations. </p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_create_case_options_request.DescribeCreateCaseOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_create_case_options_response.DescribeCreateCaseOptionsResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_create_case_options

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_create_case_options.async_describe_create_case_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_create_case_options_request.DescribeCreateCaseOptionsRequest = {
            "issue_type": issue_type,
            "service_code": service_code,
            "language": language,
            "category_code": category_code,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_services(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        service_code_list: Optional[
            "capo_support.types.service_code_list.ServiceCodeList"
        ] = None,
        language: Optional["capo_support.types.language.Language"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_services_response.DescribeServicesResponse":
        """<p>Returns the current list of Amazon Web Services services and a list of service categories for each service. You then use service names and categories in your <a>CreateCase</a> requests. Each Amazon Web Services service has its own set of categories.</p> <p>The service codes and category codes correspond to the values that appear in the <b>Service</b> and <b>Category</b> lists on the Amazon Web Services Support Center <a href="https://console.aws.amazon.com/support/home#/case/create">Create Case</a> page. The values in those fields don't necessarily match the service codes and categories returned by the <code>DescribeServices</code> operation. Always use the service codes and categories that the <code>DescribeServices</code> operation returns, so that you have the most recent set of service and category codes.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            service_code_list: <p>A JSON-formatted list of service codes available for Amazon Web Services services.</p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning the list of services. When set to <code>true</code>, the request is validated but no services are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_services_request.DescribeServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_services_response.DescribeServicesResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_services

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_services.async_describe_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_services_request.DescribeServicesRequest = {}
        if service_code_list is not None:
            input_["service_code_list"] = service_code_list
        if language is not None:
            input_["language"] = language
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_severity_levels(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        language: Optional["capo_support.types.language.Language"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_severity_levels_response.DescribeSeverityLevelsResponse":
        """<p>Returns the list of severity levels that you can assign to a support case. The severity level for a case is also a field in the <a>CaseDetails</a> data type that you include for a <a>CreateCase</a> request.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning severity levels. When set to <code>true</code>, the request is validated but no severity levels are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_severity_levels_request.DescribeSeverityLevelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_severity_levels_response.DescribeSeverityLevelsResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_severity_levels

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_severity_levels.async_describe_severity_levels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_severity_levels_request.DescribeSeverityLevelsRequest = {}
        if language is not None:
            input_["language"] = language
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_supported_languages(
        self,
        issue_type: "capo_support.types.validated_issue_type_string.ValidatedIssueTypeString",
        service_code: "capo_support.types.validated_service_code.ValidatedServiceCode",
        category_code: "capo_support.types.validated_category_code.ValidatedCategoryCode",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.describe_supported_languages_response.DescribeSupportedLanguagesResponse":
        """<p>Returns a list of supported languages for a specified <code>categoryCode</code>, <code>issueType</code> and <code>serviceCode</code>. The returned supported languages will include a ISO 639-1 code for the <code>language</code>, and the language display name.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            issue_type: <p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>.</p>
            service_code: <p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>
            category_code: <p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning supported languages. When set to <code>true</code>, the request is validated but no languages are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.throttling_exception.ThrottlingException: <p> You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations. </p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_supported_languages_request.DescribeSupportedLanguagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_supported_languages_response.DescribeSupportedLanguagesResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_supported_languages

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_supported_languages.async_describe_supported_languages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_supported_languages_request.DescribeSupportedLanguagesRequest = {
            "issue_type": issue_type,
            "service_code": service_code,
            "category_code": category_code,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_trusted_advisor_check_refresh_statuses(
        self,
        check_ids: "capo_support.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "capo_support.types.describe_trusted_advisor_check_refresh_statuses_response.DescribeTrustedAdvisorCheckRefreshStatusesResponse":
        """<p>Returns the refresh status of the Trusted Advisor checks that have the specified check IDs. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>Some checks are refreshed automatically, and you can't return their refresh statuses by using the <code>DescribeTrustedAdvisorCheckRefreshStatuses</code> operation. If you call this operation for these checks, you might see an <code>InvalidParameterValue</code> error.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            check_ids: <p>The IDs of the Trusted Advisor checks to get the status.</p> <note> <p>If you specify the check ID of a check that is automatically refreshed, you might see an <code>InvalidParameterValue</code> error.</p> </note>

        Raises:
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.throttling_exception.ThrottlingException: <p> You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations. </p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_trusted_advisor_check_refresh_statuses_request.DescribeTrustedAdvisorCheckRefreshStatusesRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_trusted_advisor_check_refresh_statuses_response.DescribeTrustedAdvisorCheckRefreshStatusesResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_trusted_advisor_check_refresh_statuses

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_trusted_advisor_check_refresh_statuses.async_describe_trusted_advisor_check_refresh_statuses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_trusted_advisor_check_refresh_statuses_request.DescribeTrustedAdvisorCheckRefreshStatusesRequest = {
            "check_ids": check_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_trusted_advisor_check_result(
        self,
        check_id: "capo_support.types.string.String",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        language: Optional["capo_support.types.string.String"] = None,
    ) -> "capo_support.types.describe_trusted_advisor_check_result_response.DescribeTrustedAdvisorCheckResultResponse":
        """<p>Returns the results of the Trusted Advisor check that has the specified check ID. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>The response contains a <a>TrustedAdvisorCheckResult</a> object, which contains these three objects:</p> <ul> <li> <p> <a>TrustedAdvisorCategorySpecificSummary</a> </p> </li> <li> <p> <a>TrustedAdvisorResourceDetail</a> </p> </li> <li> <p> <a>TrustedAdvisorResourcesSummary</a> </p> </li> </ul> <p>In addition, the response contains these fields:</p> <ul> <li> <p> <b>status</b> - The alert status of the check can be <code>ok</code> (green), <code>warning</code> (yellow), <code>error</code> (red), or <code>not_available</code>.</p> </li> <li> <p> <b>timestamp</b> - The time of the last refresh of the check.</p> </li> <li> <p> <b>checkId</b> - The unique identifier for the check.</p> </li> </ul> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            check_id: <p>The unique identifier for the Trusted Advisor check.</p>
            language: <p>The ISO 639-1 code for the language that you want your check results to appear in.</p> <p>The Amazon Web Services Support API currently supports the following languages for Trusted Advisor:</p> <ul> <li> <p>Chinese, Simplified - <code>zh</code> </p> </li> <li> <p>Chinese, Traditional - <code>zh_TW</code> </p> </li> <li> <p>English - <code>en</code> </p> </li> <li> <p>French - <code>fr</code> </p> </li> <li> <p>German - <code>de</code> </p> </li> <li> <p>Indonesian - <code>id</code> </p> </li> <li> <p>Italian - <code>it</code> </p> </li> <li> <p>Japanese - <code>ja</code> </p> </li> <li> <p>Korean - <code>ko</code> </p> </li> <li> <p>Portuguese, Brazilian - <code>pt_BR</code> </p> </li> <li> <p>Spanish - <code>es</code> </p> </li> </ul>

        Raises:
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.throttling_exception.ThrottlingException: <p> You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations. </p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_trusted_advisor_check_result_request.DescribeTrustedAdvisorCheckResultRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_trusted_advisor_check_result_response.DescribeTrustedAdvisorCheckResultResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_trusted_advisor_check_result

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_trusted_advisor_check_result.async_describe_trusted_advisor_check_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_trusted_advisor_check_result_request.DescribeTrustedAdvisorCheckResultRequest = {
            "check_id": check_id
        }
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_trusted_advisor_checks(
        self,
        language: "capo_support.types.string.String",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "capo_support.types.describe_trusted_advisor_checks_response.DescribeTrustedAdvisorChecksResponse":
        """<p>Returns information about all available Trusted Advisor checks, including the name, ID, category, description, and metadata. You must specify a language code.</p> <p>The response contains a <a>TrustedAdvisorCheckDescription</a> object for each check. You must set the Amazon Web Services Region to us-east-1.</p> <note> <ul> <li> <p>You must have a Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> <li> <p>The names and descriptions for Trusted Advisor checks are subject to change. We recommend that you specify the check ID in your code to uniquely identify a check.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            language: <p>The ISO 639-1 code for the language that you want your checks to appear in.</p> <p>The Amazon Web Services Support API currently supports the following languages for Trusted Advisor:</p> <ul> <li> <p>Chinese, Simplified - <code>zh</code> </p> </li> <li> <p>Chinese, Traditional - <code>zh_TW</code> </p> </li> <li> <p>English - <code>en</code> </p> </li> <li> <p>French - <code>fr</code> </p> </li> <li> <p>German - <code>de</code> </p> </li> <li> <p>Indonesian - <code>id</code> </p> </li> <li> <p>Italian - <code>it</code> </p> </li> <li> <p>Japanese - <code>ja</code> </p> </li> <li> <p>Korean - <code>ko</code> </p> </li> <li> <p>Portuguese, Brazilian - <code>pt_BR</code> </p> </li> <li> <p>Spanish - <code>es</code> </p> </li> </ul>

        Raises:
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.throttling_exception.ThrottlingException: <p> You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations. </p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_trusted_advisor_checks_request.DescribeTrustedAdvisorChecksRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_trusted_advisor_checks_response.DescribeTrustedAdvisorChecksResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_trusted_advisor_checks

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_trusted_advisor_checks.async_describe_trusted_advisor_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_trusted_advisor_checks_request.DescribeTrustedAdvisorChecksRequest = {
            "language": language
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_trusted_advisor_check_summaries(
        self,
        check_ids: "capo_support.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "capo_support.types.describe_trusted_advisor_check_summaries_response.DescribeTrustedAdvisorCheckSummariesResponse":
        """<p>Returns the results for the Trusted Advisor check summaries for the check IDs that you specified. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>The response contains an array of <a>TrustedAdvisorCheckSummary</a> objects.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p> <p> <b>Understanding the Trusted Advisor Resources processed value</b> </p> <p>The <b>Resources processed</b> value, <code>resourcesProcessed</code>, usually shows both flagged resources (those with warnings or errors) and resources in good standing (ok status resources). However, some checks report flagged resources only. To understand what a specific check reports, review the detailed check information in the <a href="https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html">Trusted Advisor check reference</a>. If you see a <b>Green</b> criterion listed in the <b>Alert criteria</b>, then the check reports all resources. If there's no <b>Green</b> criterion listed in the <b>Alert criteria</b>, then the check reports only flagged resources. For example, the <a href="https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-ec2-reserved-instances-optimization">Amazon EC2 Reserved Instance optimization check (cX3c2R1chu)</a> doesn't list a <b>Green</b> criterion in the <b>Alert criteria</b>. So, this check only reports flagged resources.</p>

        Args:
            check_ids: <p>The IDs of the Trusted Advisor checks.</p>

        Raises:
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.throttling_exception.ThrottlingException: <p> You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations. </p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.describe_trusted_advisor_check_summaries_request.DescribeTrustedAdvisorCheckSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.describe_trusted_advisor_check_summaries_response.DescribeTrustedAdvisorCheckSummariesResponse"
        ]:
            import capo_support._operations.aws_support_20130415.describe_trusted_advisor_check_summaries

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.describe_trusted_advisor_check_summaries.async_describe_trusted_advisor_check_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.describe_trusted_advisor_check_summaries_request.DescribeTrustedAdvisorCheckSummariesRequest = {
            "check_ids": check_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_attachment_download_link(
        self,
        attachment_id: "capo_support.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.get_attachment_download_link_response.GetAttachmentDownloadLinkResponse":
        """<p>Returns a presigned download URL for an attachment that is associated with a case communication. The download link works for an attachment of any size, including attachments added through <code>AddAttachmentsToSet</code> and attachments uploaded through <a>GetAttachmentUploadLinks</a>. The download URL is time-limited and expires at the date and time indicated in the <code>downloadUrl</code> response field. Download the attachment from the URL before it expires.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            attachment_id: <p>The unique identifier of the attachment for which to retrieve a download link. Attachment IDs are returned in the <code>AttachmentDetails</code> objects in the <code>attachments</code> field of a <a>Communication</a> returned by <a>DescribeCommunications</a> or <a>DescribeCases</a>.</p>
            dry_run: <p>Specifies whether to validate the request without actually returning a download link. When set to <code>true</code>, the request is validated but no URL is returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.attachment_id_not_found.AttachmentIdNotFound: <p>An attachment with the specified ID could not be found.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.get_attachment_download_link_request.GetAttachmentDownloadLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.get_attachment_download_link_response.GetAttachmentDownloadLinkResponse"
        ]:
            import capo_support._operations.aws_support_20130415.get_attachment_download_link

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.get_attachment_download_link.async_get_attachment_download_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.get_attachment_download_link_request.GetAttachmentDownloadLinkRequest = {
            "attachment_id": attachment_id
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_attachment_upload_links(
        self,
        file_name: "capo_support.types.file_name.FileName",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        file_size_bytes: Optional["capo_support.types.file_size.FileSize"] = None,
        upload_id: Optional["capo_support.types.upload_id.UploadId"] = None,
        upload_range: Optional["capo_support.types.upload_range.UploadRange"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.get_attachment_upload_links_response.GetAttachmentUploadLinksResponse":
        """<p>Returns one or more presigned upload URLs for uploading a large file attachment to a support case by using a multipart upload workflow. The maximum file size that you can upload with this workflow is 150 MB, and parts can be up to 100 MB each. Initiate a new upload by providing <code>fileName</code> and <code>fileSizeBytes</code>; the response returns a unique <code>uploadId</code>, the part size, the total number of parts, and a list of presigned upload URLs for the requested range of parts. A maximum of 10 upload URLs are returned per call. To retrieve more upload URLs for an upload that's already in progress, call <code>GetAttachmentUploadLinks</code> again with the existing <code>uploadId</code> and a new <code>uploadRange</code>.</p> <p>Upload each part to its presigned URL by using HTTP <code>PUT</code> and capture the ETag from the response. After you upload all parts, call <a>CompleteAttachmentUpload</a> with the <code>uploadId</code> and the list of part indexes and ETags to finalize the upload. You can then attach the upload to a case by passing the <code>uploadId</code> in the <code>uploadIds</code> parameter of <a>CreateCase</a> or <a>AddCommunicationToCase</a>. To monitor progress before completion, call <a>DescribeAttachmentUploadStatus</a>.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            file_name: <p>The name of the file to upload, including the file extension. This value is required when you initiate a new upload.</p>
            file_size_bytes: <p>The total size of the file in bytes. The service uses this value to calculate the total number of parts and the size of each part. Required when you initiate a new upload (when <code>uploadId</code> isn't provided). Valid range: 1 to 157,286,400 bytes (approximately 150 MB).</p>
            upload_id: <p>The unique identifier of an in-progress multipart upload, returned by a previous call to <code>GetAttachmentUploadLinks</code>. Specify <code>uploadId</code> to retrieve additional presigned upload URLs for an upload that has already been initiated. Required when <code>fileSizeBytes</code> isn't provided. Length: 1 to 2,048 characters.</p>
            upload_range: <p>The range of part indexes for which to return presigned upload URLs. Use this parameter to page through the upload URLs for a large file across multiple calls. If you omit this parameter, the service determines the range to return.</p>
            dry_run: <p>Specifies whether to validate the request without actually generating upload URLs. When set to <code>true</code>, the request is validated but no URLs are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.upload_id_not_found.UploadIdNotFound: <p>The specified <code>uploadId</code> couldn't be located.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.get_attachment_upload_links_request.GetAttachmentUploadLinksRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.get_attachment_upload_links_response.GetAttachmentUploadLinksResponse"
        ]:
            import capo_support._operations.aws_support_20130415.get_attachment_upload_links

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.get_attachment_upload_links.async_get_attachment_upload_links(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.get_attachment_upload_links_request.GetAttachmentUploadLinksRequest = {
            "file_name": file_name
        }
        if file_size_bytes is not None:
            input_["file_size_bytes"] = file_size_bytes
        if upload_id is not None:
            input_["upload_id"] = upload_id
        if upload_range is not None:
            input_["upload_range"] = upload_range
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def refresh_trusted_advisor_check(
        self,
        check_id: "capo_support.types.string.String",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "capo_support.types.refresh_trusted_advisor_check_response.RefreshTrustedAdvisorCheckResponse":
        """<p>Refreshes the Trusted Advisor check that you specify using the check ID. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>Some checks are refreshed automatically. If you call the <code>RefreshTrustedAdvisorCheck</code> operation to refresh them, you might see the <code>InvalidParameterValue</code> error.</p> <p>The response contains a <a>TrustedAdvisorCheckRefreshStatus</a> object.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href="https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            check_id: <p>The unique identifier for the Trusted Advisor check to refresh.</p> <note> <p>Specifying the check ID of a check that is automatically refreshed causes an <code>InvalidParameterValue</code> error.</p> </note>

        Raises:
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.refresh_trusted_advisor_check_request.RefreshTrustedAdvisorCheckRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.refresh_trusted_advisor_check_response.RefreshTrustedAdvisorCheckResponse"
        ]:
            import capo_support._operations.aws_support_20130415.refresh_trusted_advisor_check

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.refresh_trusted_advisor_check.async_refresh_trusted_advisor_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.refresh_trusted_advisor_check_request.RefreshTrustedAdvisorCheckRequest = {
            "check_id": check_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resolve_case(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id: Optional["capo_support.types.case_id.CaseId"] = None,
        dry_run: Optional[
            "capo_support.types.nullable_boolean_type.NullableBooleanType"
        ] = None,
    ) -> "capo_support.types.resolve_case_response.ResolveCaseResponse":
        """<p>Resolves a support case. This operation takes a <code>caseId</code> and returns the initial and final state of the case.</p> <note> <ul> <li> <p>You must have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan to use the Amazon Web Services Support API. If you're in an Amazon Web Services Region that doesn't offer one of these Amazon Web Services Support plans, or if you haven't transitioned to one of these plans, you can use the Amazon Web Services Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.</p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have an Amazon Web Services Business Support+, Amazon Web Services Enterprise Support, or Amazon Web Services Unified Operations plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            case_id: <p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>
            dry_run: <p>Specifies whether to validate the request without actually resolving the case. When set to <code>true</code>, the request is validated but the case isn't resolved, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>

        Raises:
            capo_support.errors.case_id_not_found.CaseIdNotFound: <p>The requested <code>caseId</code> couldn't be located.</p>
            capo_support.errors.dry_run_operation_exception.DryRunOperationException: <p>The request was valid, but the operation wasn't performed because <code>dryRun</code> was set to <code>true</code>.</p>
            capo_support.errors.internal_server_error.InternalServerError: <p>An internal server error occurred.</p>
            capo_support.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_support.types.resolve_case_request.ResolveCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_support.types.resolve_case_response.ResolveCaseResponse"
        ]:
            import capo_support._operations.aws_support_20130415.resolve_case

            (
                output,
                http_response,
            ) = await capo_support._operations.aws_support_20130415.resolve_case.async_resolve_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_support.types.resolve_case_request.ResolveCaseRequest = {}
        if case_id is not None:
            input_["case_id"] = case_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()

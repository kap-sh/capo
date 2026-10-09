"""Generated from Smithy shape ``com.amazonaws.artifact#Artifact``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_artifact._auth._signers
import capo_artifact._auth._sigv4
from capo_artifact._auth._identity import Credentials
from capo_artifact._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_artifact._auth._zapros_handler import AuthMiddleware
from capo_artifact._pagination import resolve_path as _resolve_path
from capo_artifact._resources.artifact.account_settings_resource import (
    AccountSettingsResource,
)
from capo_artifact._resources.artifact.compliance_inquiry_resource import (
    ComplianceInquiryResource,
)
from capo_artifact._resources.artifact.customer_agreement_resource import (
    CustomerAgreementResource,
)
from capo_artifact._resources.artifact.report_resource import ReportResource
from capo_artifact._resources.artifact.term_resource import TermResource
from capo_artifact._services._aws_config import aws_config
from capo_artifact._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_artifact.types.create_compliance_inquiry_request
    import capo_artifact.types.create_compliance_inquiry_response
    import capo_artifact.types.customer_agreement_summary
    import capo_artifact.types.export_compliance_inquiry_request
    import capo_artifact.types.export_compliance_inquiry_response
    import capo_artifact.types.feedback_comment_attribute
    import capo_artifact.types.feedback_rating
    import capo_artifact.types.feedback_reason_code_list
    import capo_artifact.types.get_account_settings_request
    import capo_artifact.types.get_account_settings_response
    import capo_artifact.types.get_compliance_inquiry_metadata_request
    import capo_artifact.types.get_compliance_inquiry_metadata_response
    import capo_artifact.types.get_report_metadata_request
    import capo_artifact.types.get_report_metadata_response
    import capo_artifact.types.get_report_request
    import capo_artifact.types.get_report_response
    import capo_artifact.types.get_term_for_report_request
    import capo_artifact.types.get_term_for_report_response
    import capo_artifact.types.idempotent_client_token
    import capo_artifact.types.inquiry_content
    import capo_artifact.types.inquiry_id
    import capo_artifact.types.inquiry_name
    import capo_artifact.types.inquiry_summary
    import capo_artifact.types.inquiry_support_mode
    import capo_artifact.types.list_compliance_inquiries_request
    import capo_artifact.types.list_compliance_inquiries_response
    import capo_artifact.types.list_compliance_inquiry_queries_request
    import capo_artifact.types.list_compliance_inquiry_queries_response
    import capo_artifact.types.list_customer_agreements_request
    import capo_artifact.types.list_customer_agreements_response
    import capo_artifact.types.list_report_versions_request
    import capo_artifact.types.list_report_versions_response
    import capo_artifact.types.list_reports_request
    import capo_artifact.types.list_reports_response
    import capo_artifact.types.list_tags_for_resource_request
    import capo_artifact.types.list_tags_for_resource_response
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.max_results_attribute
    import capo_artifact.types.next_token_attribute
    import capo_artifact.types.notification_subscription_status
    import capo_artifact.types.put_account_settings_request
    import capo_artifact.types.put_account_settings_response
    import capo_artifact.types.put_compliance_inquiry_feedback_request
    import capo_artifact.types.put_compliance_inquiry_feedback_response
    import capo_artifact.types.query_identifiers_list
    import capo_artifact.types.query_summary
    import capo_artifact.types.report_id
    import capo_artifact.types.report_summary
    import capo_artifact.types.short_string_attribute
    import capo_artifact.types.tag_keys
    import capo_artifact.types.tag_resource_request
    import capo_artifact.types.tag_resource_response
    import capo_artifact.types.tags_map
    import capo_artifact.types.untag_resource_request
    import capo_artifact.types.untag_resource_response
    import capo_artifact.types.version_attribute


class ArtifactClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ArtifactClient:
    """A client for the ``Artifact`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = ArtifactClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.account_settings_resource = AccountSettingsResource(self)
        self.compliance_inquiry_resource = ComplianceInquiryResource(self)
        self.customer_agreement_resource = CustomerAgreementResource(self)
        self.report_resource = ReportResource(self)
        self.term_resource = TermResource(self)

    def operation_options(
        self, config_overrides: Optional[ArtifactClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ArtifactClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_artifact.types.long_string_attribute.LongStringAttribute",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
    ) -> "capo_artifact.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_artifact._operations.artifact.list_tags_for_resource

            output, http_response = (
                capo_artifact._operations.artifact.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_artifact.types.long_string_attribute.LongStringAttribute",
        tags: "capo_artifact.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
    ) -> "capo_artifact.types.tag_resource_response.TagResourceResponse":
        """<p>Add tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>Tags to add to the resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_artifact._operations.artifact.tag_resource

            output, http_response = (
                capo_artifact._operations.artifact.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_artifact.types.long_string_attribute.LongStringAttribute",
        tag_keys: "capo_artifact.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
    ) -> "capo_artifact.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Tag keys to remove from the resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_artifact._operations.artifact.untag_resource

            output, http_response = (
                capo_artifact._operations.artifact.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.untag_resource_request.UntagResourceRequest = {
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

    def get_account_settings(
        self, *, config_overrides: Optional[ArtifactClientConfig] = None
    ) -> "capo_artifact.types.get_account_settings_response.GetAccountSettingsResponse":
        """<p>Get the account settings for Artifact.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetAccountSettings operation
            Get the current account settings.

            >>> client.get_account_settings()
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import capo_artifact._operations.artifact.get_account_settings

            output, http_response = (
                capo_artifact._operations.artifact.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.get_account_settings_request.GetAccountSettingsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_account_settings(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        notification_subscription_status: Optional[
            "capo_artifact.types.notification_subscription_status.NotificationSubscriptionStatus"
        ] = None,
    ) -> "capo_artifact.types.put_account_settings_response.PutAccountSettingsResponse":
        """<p>Put the account settings for Artifact.</p>

        Args:
            notification_subscription_status: <p>Desired notification subscription status.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke PutAccountSettings operation
            Set the account settings.

            >>> client.put_account_settings(notification_subscription_status='SUBSCRIBED')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.put_account_settings_request.PutAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.put_account_settings_response.PutAccountSettingsResponse"
        ]:
            import capo_artifact._operations.artifact.put_account_settings

            output, http_response = (
                capo_artifact._operations.artifact.put_account_settings.put_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.put_account_settings_request.PutAccountSettingsRequest = {}
        if notification_subscription_status is not None:
            input_["notification_subscription_status"] = (
                notification_subscription_status
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_compliance_inquiry(
        self,
        name: "capo_artifact.types.inquiry_name.InquiryName",
        inquiry_content: "capo_artifact.types.inquiry_content.InquiryContent",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        client_token: Optional[
            "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
        ] = None,
        support_mode: Optional[
            "capo_artifact.types.inquiry_support_mode.InquirySupportMode"
        ] = None,
        tags: Optional["capo_artifact.types.tags_map.TagsMap"] = None,
    ) -> "capo_artifact.types.create_compliance_inquiry_response.CreateComplianceInquiryResponse":
        """<p>Create a new compliance inquiry.</p>

        Args:
            name: <p>Title of the inquiry.</p>
            inquiry_content: <p>Content for creating a compliance inquiry - either a single query or file content.</p>
            client_token: <p>Idempotency token for the request.</p>
            support_mode: <p>Support mode for inquiry processing. Only supported for file upload mode. Defaults to AI_ONLY if not specified.</p>
            tags: <p>Tags to associate with the compliance inquiry resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateComplianceInquiry operation
            Creates a compliance inquiry with a single text query.

            >>> client.create_compliance_inquiry(name='My Compliance Inquiry', inquiry_content={'query': 'Is my workload compliant with SOC 2?'}, client_token='unique-client-token-1234', support_mode='AI_ONLY')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.create_compliance_inquiry_response.CreateComplianceInquiryResponse"
        ]:
            import capo_artifact._operations.artifact.create_compliance_inquiry

            output, http_response = (
                capo_artifact._operations.artifact.create_compliance_inquiry.create_compliance_inquiry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.create_compliance_inquiry_request.CreateComplianceInquiryRequest = {
            "name": name,
            "inquiry_content": inquiry_content,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if support_mode is not None:
            input_["support_mode"] = support_mode
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_compliance_inquiry(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        query_identifiers: Optional[
            "capo_artifact.types.query_identifiers_list.QueryIdentifiersList"
        ] = None,
        include_citations: Optional[bool] = None,
    ) -> "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse":
        """<p>Export a compliance inquiry report.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>
            query_identifiers: <p>List of query identifiers to include in the export.</p>
            include_citations: <p>When true, include citations in the exported document.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ExportComplianceInquiry operation
            Exports a compliance inquiry report.

            >>> client.export_compliance_inquiry(compliance_inquiry_id='compliance-inquiry-abcdef0123456789', query_identifiers=[1, 2], include_citations=True)
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.export_compliance_inquiry_request.ExportComplianceInquiryRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.export_compliance_inquiry_response.ExportComplianceInquiryResponse"
        ]:
            import capo_artifact._operations.artifact.export_compliance_inquiry

            output, http_response = (
                capo_artifact._operations.artifact.export_compliance_inquiry.export_compliance_inquiry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.export_compliance_inquiry_request.ExportComplianceInquiryRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
        }
        if query_identifiers is not None:
            input_["query_identifiers"] = query_identifiers
        if include_citations is not None:
            input_["include_citations"] = include_citations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compliance_inquiry_metadata(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
    ) -> "capo_artifact.types.get_compliance_inquiry_metadata_response.GetComplianceInquiryMetadataResponse":
        """<p>Get the metadata for a single compliance inquiry.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetComplianceInquiryMetadata operation
            Gets metadata for a compliance inquiry.

            >>> client.get_compliance_inquiry_metadata(compliance_inquiry_id='compliance-inquiry-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_compliance_inquiry_metadata_request.GetComplianceInquiryMetadataRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_compliance_inquiry_metadata_response.GetComplianceInquiryMetadataResponse"
        ]:
            import capo_artifact._operations.artifact.get_compliance_inquiry_metadata

            output, http_response = (
                capo_artifact._operations.artifact.get_compliance_inquiry_metadata.get_compliance_inquiry_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.get_compliance_inquiry_metadata_request.GetComplianceInquiryMetadataRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_compliance_inquiries(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_compliance_inquiries_response.ListComplianceInquiriesResponse":
        """<p>List available compliance inquiries.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComplianceInquiries operation
            Lists all compliance inquiries.

            >>> client.list_compliance_inquiries(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_compliance_inquiries_request.ListComplianceInquiriesRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_compliance_inquiries_response.ListComplianceInquiriesResponse"
        ]:
            import capo_artifact._operations.artifact.list_compliance_inquiries

            output, http_response = (
                capo_artifact._operations.artifact.list_compliance_inquiries.list_compliance_inquiries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.list_compliance_inquiries_request.ListComplianceInquiriesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_compliance_inquiries(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "Iterator[capo_artifact.types.inquiry_summary.InquirySummary]":
        _token = next_token
        while True:
            _response = self.list_compliance_inquiries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("compliance_inquiries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_compliance_inquiry_queries(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_compliance_inquiry_queries_response.ListComplianceInquiryQueriesResponse":
        """<p>List queries within a compliance inquiry.</p>

        Args:
            compliance_inquiry_id: <p>Unique resource ID for the compliance inquiry.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComplianceInquiryQueries operation
            Lists queries within a compliance inquiry.

            >>> client.list_compliance_inquiry_queries(compliance_inquiry_id='compliance-inquiry-abcdef0123456789', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_compliance_inquiry_queries_request.ListComplianceInquiryQueriesRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_compliance_inquiry_queries_response.ListComplianceInquiryQueriesResponse"
        ]:
            import capo_artifact._operations.artifact.list_compliance_inquiry_queries

            output, http_response = (
                capo_artifact._operations.artifact.list_compliance_inquiry_queries.list_compliance_inquiry_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.list_compliance_inquiry_queries_request.ListComplianceInquiryQueriesRequest = {
            "compliance_inquiry_id": compliance_inquiry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_compliance_inquiry_queries(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "Iterator[capo_artifact.types.query_summary.QuerySummary]":
        _token = next_token
        while True:
            _response = self.list_compliance_inquiry_queries(
                compliance_inquiry_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("queries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_compliance_inquiry_feedback(
        self,
        compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId",
        rating: "capo_artifact.types.feedback_rating.FeedbackRating",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        query_identifier: Optional[int] = None,
        response_revision_id: Optional[int] = None,
        reason_codes: Optional[
            "capo_artifact.types.feedback_reason_code_list.FeedbackReasonCodeList"
        ] = None,
        comment: Optional[
            "capo_artifact.types.feedback_comment_attribute.FeedbackCommentAttribute"
        ] = None,
        client_token: Optional[
            "capo_artifact.types.idempotent_client_token.IdempotentClientToken"
        ] = None,
    ) -> "capo_artifact.types.put_compliance_inquiry_feedback_response.PutComplianceInquiryFeedbackResponse":
        """<p>Submits feedback on a compliance inquiry response.</p>

        Args:
            compliance_inquiry_id: <p>The unique identifier for the compliance inquiry.</p>
            query_identifier: <p>The sequential identifier of the query to provide feedback on.</p>
            rating: <p>The rating for the feedback. Valid values are THUMBS_UP and THUMBS_DOWN.</p>
            response_revision_id: <p>The response revision ID. Use this value to prevent submitting feedback on a stale response.</p>
            reason_codes: <p>The reason codes that describe why you rated the response. Valid values are OTHER, PARTIAL_RESPONSE, and IRRELEVANT_RESPONSE.</p>
            comment: <p>An optional comment for the feedback.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.put_compliance_inquiry_feedback_response.PutComplianceInquiryFeedbackResponse"
        ]:
            import capo_artifact._operations.artifact.put_compliance_inquiry_feedback

            output, http_response = (
                capo_artifact._operations.artifact.put_compliance_inquiry_feedback.put_compliance_inquiry_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.put_compliance_inquiry_feedback_request.PutComplianceInquiryFeedbackRequest = {
            "compliance_inquiry_id": compliance_inquiry_id,
            "rating": rating,
        }
        if query_identifier is not None:
            input_["query_identifier"] = query_identifier
        if response_revision_id is not None:
            input_["response_revision_id"] = response_revision_id
        if reason_codes is not None:
            input_["reason_codes"] = reason_codes
        if comment is not None:
            input_["comment"] = comment
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

    def list_customer_agreements(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse":
        """<p>List active customer-agreements applicable to calling identity.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCustomerAgreements operation
            The ListCustomerAgreements operation returns a collection of customer-agreement resources in the ACTIVE state for the calling credential.

            >>> client.list_customer_agreements()
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse"
        ]:
            import capo_artifact._operations.artifact.list_customer_agreements

            output, http_response = (
                capo_artifact._operations.artifact.list_customer_agreements.list_customer_agreements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_customer_agreements(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "Iterator[capo_artifact.types.customer_agreement_summary.CustomerAgreementSummary]":
        _token = next_token
        while True:
            _response = self.list_customer_agreements(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("customer_agreements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_report_metadata(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_report_metadata_response.GetReportMetadataResponse":
        """<p>Get the metadata for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetReportMetadata operation on the latest version of a specific report
            The GetReportMetadata operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> client.get_report_metadata(report_id='report-bqhUJF3FrQZsMJpb')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_report_metadata_request.GetReportMetadataRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_report_metadata_response.GetReportMetadataResponse"
        ]:
            import capo_artifact._operations.artifact.get_report_metadata

            output, http_response = (
                capo_artifact._operations.artifact.get_report_metadata.get_report_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.get_report_metadata_request.GetReportMetadataRequest = {
            "report_id": report_id
        }
        if report_version is not None:
            input_["report_version"] = report_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_reports(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_reports_response.ListReportsResponse":
        """<p>List available reports.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListReports operation
            The ListReports operation returns a collection of report resources.

            >>> client.list_reports()
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_reports_request.ListReportsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_reports_response.ListReportsResponse"
        ]:
            import capo_artifact._operations.artifact.list_reports

            output, http_response = (
                capo_artifact._operations.artifact.list_reports.list_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.list_reports_request.ListReportsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_reports(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "Iterator[capo_artifact.types.report_summary.ReportSummary]":
        _token = next_token
        while True:
            _response = self.list_reports(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_report(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        term_token: "capo_artifact.types.short_string_attribute.ShortStringAttribute",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_report_response.GetReportResponse":
        """<p>Get the content for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>
            term_token: <p>Unique download token provided by GetTermForReport API.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetReport operation on the latest version of a specific report
            The GetReport operation is invoked on a reportId and on a optional version.
                        Callers must provide a termToken, which is provided by the GetTermForReport
                        operation. If callers do not provide a version, it will default to the
                        report's latest version

            >>> client.get_report(report_id='report-abcdef0123456789', term_token='term-token-abcdefghijklm01234567890')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_report_request.GetReportRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_report_response.GetReportResponse"
        ]:
            import capo_artifact._operations.artifact.get_report

            output, http_response = (
                capo_artifact._operations.artifact.get_report.get_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.get_report_request.GetReportRequest = {
            "report_id": report_id,
            "term_token": term_token,
        }
        if report_version is not None:
            input_["report_version"] = report_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_term_for_report(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_term_for_report_response.GetTermForReportResponse":
        """<p>Get the Term content associated with a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetTermForReport operation on the latest version of a specific report
            The GetTermForReport operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> client.get_term_for_report(report_id='report-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_term_for_report_request.GetTermForReportRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_term_for_report_response.GetTermForReportResponse"
        ]:
            import capo_artifact._operations.artifact.get_term_for_report

            output, http_response = (
                capo_artifact._operations.artifact.get_term_for_report.get_term_for_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.get_term_for_report_request.GetTermForReportRequest = {
            "report_id": report_id
        }
        if report_version is not None:
            input_["report_version"] = report_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_report_versions(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_report_versions_response.ListReportVersionsResponse":
        """<p>List available report versions for a given report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListReportVersions operation
            The ListReportVersions operation returns a collection of report versions
                        for a given resource.

            >>> client.list_report_versions(report_id='report-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_report_versions_request.ListReportVersionsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_report_versions_response.ListReportVersionsResponse"
        ]:
            import capo_artifact._operations.artifact.list_report_versions

            output, http_response = (
                capo_artifact._operations.artifact.list_report_versions.list_report_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_artifact.types.list_report_versions_request.ListReportVersionsRequest = {
            "report_id": report_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_report_versions(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "Iterator[capo_artifact.types.report_summary.ReportSummary]":
        _token = next_token
        while True:
            _response = self.list_report_versions(
                report_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

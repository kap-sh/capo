"""Generated from Smithy shape ``com.amazonaws.securityir#SecurityIncidentResponse``."""

import datetime
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_security_ir._auth._signers
import capo_security_ir._auth._sigv4
from capo_security_ir._auth._identity import Credentials
from capo_security_ir._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_security_ir._auth._zapros_handler import AuthMiddleware
from capo_security_ir._pagination import resolve_path as _resolve_path
from capo_security_ir._resources.security_incident_response.case import Case
from capo_security_ir._resources.security_incident_response.membership import Membership
from capo_security_ir._services._aws_config import aws_config
from capo_security_ir._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_security_ir.types.arn
    import capo_security_ir.types.attachment_id
    import capo_security_ir.types.aws_account_ids
    import capo_security_ir.types.batch_get_member_account_details_request
    import capo_security_ir.types.batch_get_member_account_details_response
    import capo_security_ir.types.cancel_membership_request
    import capo_security_ir.types.cancel_membership_response
    import capo_security_ir.types.case_description
    import capo_security_ir.types.case_edit_item
    import capo_security_ir.types.case_id
    import capo_security_ir.types.case_metadata
    import capo_security_ir.types.case_title
    import capo_security_ir.types.close_case_request
    import capo_security_ir.types.close_case_response
    import capo_security_ir.types.comment_body
    import capo_security_ir.types.comment_id
    import capo_security_ir.types.content_length
    import capo_security_ir.types.create_case_comment_request
    import capo_security_ir.types.create_case_comment_response
    import capo_security_ir.types.create_case_request
    import capo_security_ir.types.create_case_response
    import capo_security_ir.types.create_membership_request
    import capo_security_ir.types.create_membership_response
    import capo_security_ir.types.engagement_type
    import capo_security_ir.types.feedback_comment
    import capo_security_ir.types.file_name
    import capo_security_ir.types.get_case_attachment_download_url_request
    import capo_security_ir.types.get_case_attachment_download_url_response
    import capo_security_ir.types.get_case_attachment_upload_url_request
    import capo_security_ir.types.get_case_attachment_upload_url_response
    import capo_security_ir.types.get_case_request
    import capo_security_ir.types.get_case_response
    import capo_security_ir.types.get_finding_metrics_request
    import capo_security_ir.types.get_finding_metrics_response
    import capo_security_ir.types.get_membership_request
    import capo_security_ir.types.get_membership_response
    import capo_security_ir.types.impacted_accounts
    import capo_security_ir.types.impacted_aws_region_list
    import capo_security_ir.types.impacted_services_list
    import capo_security_ir.types.incident_response_team
    import capo_security_ir.types.investigation_action
    import capo_security_ir.types.list_case_edits_request
    import capo_security_ir.types.list_case_edits_response
    import capo_security_ir.types.list_cases_item
    import capo_security_ir.types.list_cases_request
    import capo_security_ir.types.list_cases_response
    import capo_security_ir.types.list_comments_item
    import capo_security_ir.types.list_comments_request
    import capo_security_ir.types.list_comments_response
    import capo_security_ir.types.list_investigations_request
    import capo_security_ir.types.list_investigations_response
    import capo_security_ir.types.list_membership_item
    import capo_security_ir.types.list_memberships_request
    import capo_security_ir.types.list_memberships_response
    import capo_security_ir.types.list_tags_for_resource_input
    import capo_security_ir.types.list_tags_for_resource_output
    import capo_security_ir.types.membership_accounts_configurations_update
    import capo_security_ir.types.membership_id
    import capo_security_ir.types.membership_name
    import capo_security_ir.types.opt_in_features
    import capo_security_ir.types.resolver_type
    import capo_security_ir.types.result_id
    import capo_security_ir.types.self_managed_case_status
    import capo_security_ir.types.send_feedback_request
    import capo_security_ir.types.send_feedback_response
    import capo_security_ir.types.tag_keys
    import capo_security_ir.types.tag_map
    import capo_security_ir.types.tag_resource_input
    import capo_security_ir.types.tag_resource_output
    import capo_security_ir.types.threat_actor_ip_list
    import capo_security_ir.types.untag_resource_input
    import capo_security_ir.types.untag_resource_output
    import capo_security_ir.types.update_case_comment_request
    import capo_security_ir.types.update_case_comment_response
    import capo_security_ir.types.update_case_request
    import capo_security_ir.types.update_case_response
    import capo_security_ir.types.update_case_status_request
    import capo_security_ir.types.update_case_status_response
    import capo_security_ir.types.update_membership_request
    import capo_security_ir.types.update_membership_response
    import capo_security_ir.types.update_resolver_type_request
    import capo_security_ir.types.update_resolver_type_response
    import capo_security_ir.types.usefulness_rating
    import capo_security_ir.types.watchers


class SecurityIRClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SecurityIRClient:
    """A client for the ``SecurityIR`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = SecurityIRClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.case = Case(self)
        self.membership = Membership(self)

    def operation_options(
        self, config_overrides: Optional[SecurityIRClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SecurityIRClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_security_ir.types.arn.Arn",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> (
        "capo_security_ir.types.list_tags_for_resource_output.ListTagsForResourceOutput"
    ):
        """<p>Returns currently configured tags on a resource.</p>

        Args:
            resource_arn: <p>Required element for ListTagsForResource to provide the ARN to identify a specific resource.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListTagsForResource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_security_ir._operations.security_incident_response.list_tags_for_resource

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_security_ir.types.arn.Arn",
        tags: "capo_security_ir.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag(s) to a designated resource.</p>

        Args:
            resource_arn: <p>Required element for TagResource to identify the ARN for the resource to add a tag to.</p>
            tags: <p>Required element for ListTagsForResource to provide the content for a tag.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke TagResource

            >>> client.tag_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh', tags={'key': 'example-tag-key', 'value': 'example-tag-value'})
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_security_ir.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_security_ir._operations.security_incident_response.tag_resource

            output, http_response = (
                capo_security_ir._operations.security_incident_response.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_security_ir.types.arn.Arn",
        tag_keys: "capo_security_ir.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag(s) from a designate resource.</p>

        Args:
            resource_arn: <p>Required element for UnTagResource to identify the ARN for the resource to remove a tag from.</p>
            tag_keys: <p>Required element for UnTagResource to identify tag to remove.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UntagResource

            >>> client.untag_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh', tag_keys=['example-tag-key'])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_security_ir.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_security_ir._operations.security_incident_response.untag_resource

            output, http_response = (
                capo_security_ir._operations.security_incident_response.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.untag_resource_input.UntagResourceInput = {
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

    def create_case(
        self,
        resolver_type: "capo_security_ir.types.resolver_type.ResolverType",
        title: "capo_security_ir.types.case_title.CaseTitle",
        description: "capo_security_ir.types.case_description.CaseDescription",
        engagement_type: "capo_security_ir.types.engagement_type.EngagementType",
        reported_incident_start_date: datetime.datetime,
        impacted_accounts: "capo_security_ir.types.impacted_accounts.ImpactedAccounts",
        watchers: "capo_security_ir.types.watchers.Watchers",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
        threat_actor_ip_addresses: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        impacted_services: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_aws_regions: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        tags: Optional["capo_security_ir.types.tag_map.TagMap"] = None,
    ) -> "capo_security_ir.types.create_case_response.CreateCaseResponse":
        """<p>Creates a new case.</p>

        Args:
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            resolver_type: <p>Required element used in combination with CreateCase to identify the resolver type.</p>
            title: <p>Required element used in combination with CreateCase to provide a title for the new case.</p>
            description: <p>Required element used in combination with CreateCase</p> <p>to provide a description for the new case.</p>
            engagement_type: <p>Required element used in combination with CreateCase to provide an engagement type for the new cases. Available engagement types include Security Incident | Investigation </p>
            reported_incident_start_date: <p>Required element used in combination with CreateCase to provide an initial start date for the unauthorized activity. </p>
            impacted_accounts: <p>Required element used in combination with CreateCase to provide a list of impacted accounts.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            watchers: <p>Required element used in combination with CreateCase to provide a list of entities to receive notifications for case updates. </p>
            threat_actor_ip_addresses: <p>An optional element used in combination with CreateCase to provide a list of suspicious internet protocol addresses associated with unauthorized activity. </p>
            impacted_services: <p>An optional element used in combination with CreateCase to provide a list of services impacted.</p>
            impacted_aws_regions: <p>An optional element used in combination with CreateCase to provide a list of impacted regions.</p>
            tags: <p>An optional element used in combination with CreateCase to add customer specified tags to a case.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateCase

            >>> client.create_case(resolver_type='Self', title='My sample case', description='Case description', reported_incident_start_date='2023-03-27T15:32:01.789Z', engagement_type='Investigation', watchers=[{'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}, {'email': 'bob@example.com', 'name': 'Bob', 'jobTitle': 'CFO'}], impacted_accounts=['000000000000', '111111111111'], impacted_services=['Amazon EC2', 'Amazon EKS'], impacted_aws_regions=[{'region': 'ap-southeast-1'}], threat_actor_ip_addresses=[{'ipAddress': '192.168.192.168', 'userAgent': 'Browser'}])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.create_case_request.CreateCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.create_case_response.CreateCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.create_case.create_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.create_case_request.CreateCaseRequest = {
            "resolver_type": resolver_type,
            "title": title,
            "description": description,
            "engagement_type": engagement_type,
            "reported_incident_start_date": reported_incident_start_date,
            "impacted_accounts": impacted_accounts,
            "watchers": watchers,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if threat_actor_ip_addresses is not None:
            input_["threat_actor_ip_addresses"] = threat_actor_ip_addresses
        if impacted_services is not None:
            input_["impacted_services"] = impacted_services
        if impacted_aws_regions is not None:
            input_["impacted_aws_regions"] = impacted_aws_regions
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_case(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_case_response.GetCaseResponse":
        """<p>Returns the attributes of a case.</p>

        Args:
            case_id: <p>Required element for GetCase to identify the requested case ID.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCase

            >>> client.get_case(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_case_request.GetCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_case_response.GetCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_case.get_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.get_case_request.GetCaseRequest = {
            "case_id": case_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_case(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        title: Optional["capo_security_ir.types.case_title.CaseTitle"] = None,
        description: Optional[
            "capo_security_ir.types.case_description.CaseDescription"
        ] = None,
        reported_incident_start_date: Optional[datetime.datetime] = None,
        actual_incident_start_date: Optional[datetime.datetime] = None,
        engagement_type: Optional[
            "capo_security_ir.types.engagement_type.EngagementType"
        ] = None,
        watchers_to_add: Optional["capo_security_ir.types.watchers.Watchers"] = None,
        watchers_to_delete: Optional["capo_security_ir.types.watchers.Watchers"] = None,
        threat_actor_ip_addresses_to_add: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        threat_actor_ip_addresses_to_delete: Optional[
            "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
        ] = None,
        impacted_services_to_add: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_services_to_delete: Optional[
            "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
        ] = None,
        impacted_aws_regions_to_add: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        impacted_aws_regions_to_delete: Optional[
            "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
        ] = None,
        impacted_accounts_to_add: Optional[
            "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
        ] = None,
        impacted_accounts_to_delete: Optional[
            "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
        ] = None,
        case_metadata: Optional[
            "capo_security_ir.types.case_metadata.CaseMetadata"
        ] = None,
    ) -> "capo_security_ir.types.update_case_response.UpdateCaseResponse":
        """<p>Updates an existing case.</p>

        Args:
            case_id: <p>Required element for UpdateCase to identify the case ID for updates.</p>
            title: <p>Optional element for UpdateCase to provide content for the title field.</p>
            description: <p>Optional element for UpdateCase to provide content for the description field.</p>
            reported_incident_start_date: <p>Optional element for UpdateCase to provide content for the customer reported incident start date field. </p>
            actual_incident_start_date: <p>Optional element for UpdateCase to provide content for the incident start date field.</p>
            engagement_type: <p>Optional element for UpdateCase to provide content for the engagement type field. <code>Available engagement types include Security Incident | Investigation</code>. </p>
            watchers_to_add: <p>Optional element for UpdateCase to provide content to add additional watchers to a case.</p>
            watchers_to_delete: <p>Optional element for UpdateCase to provide content to remove existing watchers from a case.</p>
            threat_actor_ip_addresses_to_add: <p>Optional element for UpdateCase to provide content to add additional suspicious IP addresses related to a case. </p>
            threat_actor_ip_addresses_to_delete: <p>Optional element for UpdateCase to provide content to remove suspicious IP addresses from a case.</p>
            impacted_services_to_add: <p>Optional element for UpdateCase to provide content to add services impacted.</p>
            impacted_services_to_delete: <p>Optional element for UpdateCase to provide content to remove services impacted.</p>
            impacted_aws_regions_to_add: <p>Optional element for UpdateCase to provide content to add regions impacted.</p>
            impacted_aws_regions_to_delete: <p>Optional element for UpdateCase to provide content to remove regions impacted.</p>
            impacted_accounts_to_add: <p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            impacted_accounts_to_delete: <p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>
            case_metadata: <p>Update the case request with case metadata</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCase

            >>> client.update_case(case_id='8403556009', title='My sample case', description='Case description', reported_incident_start_date='2023-03-27T15:32:01.789Z', actual_incident_start_date='2023-03-25T15:32:01.789Z', engagement_type='Investigation', watchers_to_add=[{'email': 'Sam@example.com', 'name': 'Same', 'jobTitle': 'CEO'}], watchers_to_delete=[{'email': 'bob@example.com', 'name': 'Bob', 'jobTitle': 'CFO'}], threat_actor_ip_addresses_to_add=[{'ipAddress': '190.160.190.160', 'userAgent': 'Browser'}], threat_actor_ip_addresses_to_delete=[{'ipAddress': '192.168.192.168', 'userAgent': 'Browser'}], impacted_services_to_add=['Amazon EC2'], impacted_services_to_delete=['Amazon EKS'], impacted_aws_regions_to_add=[{'region': 'ap-southeast-1'}], impacted_aws_regions_to_delete=[{'region': 'us-east-1'}], impacted_accounts_to_add=['000000000000'], impacted_accounts_to_delete=['111111111111'])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_case_request.UpdateCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_case_response.UpdateCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_case.update_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.update_case_request.UpdateCaseRequest = {
            "case_id": case_id
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if reported_incident_start_date is not None:
            input_["reported_incident_start_date"] = reported_incident_start_date
        if actual_incident_start_date is not None:
            input_["actual_incident_start_date"] = actual_incident_start_date
        if engagement_type is not None:
            input_["engagement_type"] = engagement_type
        if watchers_to_add is not None:
            input_["watchers_to_add"] = watchers_to_add
        if watchers_to_delete is not None:
            input_["watchers_to_delete"] = watchers_to_delete
        if threat_actor_ip_addresses_to_add is not None:
            input_["threat_actor_ip_addresses_to_add"] = (
                threat_actor_ip_addresses_to_add
            )
        if threat_actor_ip_addresses_to_delete is not None:
            input_["threat_actor_ip_addresses_to_delete"] = (
                threat_actor_ip_addresses_to_delete
            )
        if impacted_services_to_add is not None:
            input_["impacted_services_to_add"] = impacted_services_to_add
        if impacted_services_to_delete is not None:
            input_["impacted_services_to_delete"] = impacted_services_to_delete
        if impacted_aws_regions_to_add is not None:
            input_["impacted_aws_regions_to_add"] = impacted_aws_regions_to_add
        if impacted_aws_regions_to_delete is not None:
            input_["impacted_aws_regions_to_delete"] = impacted_aws_regions_to_delete
        if impacted_accounts_to_add is not None:
            input_["impacted_accounts_to_add"] = impacted_accounts_to_add
        if impacted_accounts_to_delete is not None:
            input_["impacted_accounts_to_delete"] = impacted_accounts_to_delete
        if case_metadata is not None:
            input_["case_metadata"] = case_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cases(
        self,
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_cases_response.ListCasesResponse":
        """<p>Lists all cases the requester has access to.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListCases. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element for ListCases to limit the number of responses.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCases

            >>> client.list_cases(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_cases_request.ListCasesRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_cases_response.ListCasesResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_cases

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_cases.list_cases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.list_cases_request.ListCasesRequest = {}
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

    def iter_list_cases(
        self,
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_security_ir.types.list_cases_item.ListCasesItem]":
        _token = next_token
        while True:
            _response = self.list_cases(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def close_case(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.close_case_response.CloseCaseResponse":
        """<p>Closes an existing case.</p>

        Args:
            case_id: <p>Required element used in combination with CloseCase to identify the case ID to close.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CloseCase

            >>> client.close_case(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.close_case_request.CloseCaseRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.close_case_response.CloseCaseResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.close_case

            output, http_response = (
                capo_security_ir._operations.security_incident_response.close_case.close_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.close_case_request.CloseCaseRequest = {
            "case_id": case_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_case_comment(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        body: "capo_security_ir.types.comment_body.CommentBody",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_security_ir.types.create_case_comment_response.CreateCaseCommentResponse"
    ):
        """<p>Adds a comment to an existing case.</p>

        Args:
            case_id: <p>Required element used in combination with CreateCaseComment to specify a case ID.</p>
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            body: <p>Required element used in combination with CreateCaseComment to add content for the new comment.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateCaseComment

            >>> client.create_case_comment(case_id='8403556009', body='Case comment body.')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.create_case_comment_response.CreateCaseCommentResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_case_comment

            output, http_response = (
                capo_security_ir._operations.security_incident_response.create_case_comment.create_case_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.create_case_comment_request.CreateCaseCommentRequest = {
            "case_id": case_id,
            "body": body,
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

    def get_case_attachment_download_url(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        attachment_id: "capo_security_ir.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse":
        """<p>Returns a Pre-Signed URL for uploading attachments into a case.</p>

        Args:
            case_id: <p>Required element for GetCaseAttachmentDownloadUrl to identify the case ID for downloading an attachment from. </p>
            attachment_id: <p>Required element for GetCaseAttachmentDownloadUrl to identify the attachment ID for downloading an attachment. </p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCaseAttachmentDownloadUrl

            >>> client.get_case_attachment_download_url(case_id='8403556009', attachment_id='3C5A6B89-1DEF-4C2D-A5B6-123456789ABC')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_case_attachment_download_url_request.GetCaseAttachmentDownloadUrlRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_case_attachment_download_url_response.GetCaseAttachmentDownloadUrlResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case_attachment_download_url

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_case_attachment_download_url.get_case_attachment_download_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.get_case_attachment_download_url_request.GetCaseAttachmentDownloadUrlRequest = {
            "case_id": case_id,
            "attachment_id": attachment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_case_attachment_upload_url(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        file_name: "capo_security_ir.types.file_name.FileName",
        content_length: "capo_security_ir.types.content_length.ContentLength",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse":
        """<p>Uploads an attachment to a case.</p>

        Args:
            case_id: <p>Required element for GetCaseAttachmentUploadUrl to identify the case ID for uploading an attachment. </p>
            file_name: <p>Required element for GetCaseAttachmentUploadUrl to identify the file name of the attachment to upload. </p>
            content_length: <p>Required element for GetCaseAttachmentUploadUrl to identify the size of the file attachment.</p>
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetCaseAttachmentUploadUrl

            >>> client.get_case_attachment_upload_url(case_id='8403556009', file_name='TestFileName', content_length=1500)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_case_attachment_upload_url_response.GetCaseAttachmentUploadUrlResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_case_attachment_upload_url

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_case_attachment_upload_url.get_case_attachment_upload_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.get_case_attachment_upload_url_request.GetCaseAttachmentUploadUrlRequest = {
            "case_id": case_id,
            "file_name": file_name,
            "content_length": content_length,
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

    def list_case_edits(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_case_edits_response.ListCaseEditsResponse":
        """<p>Views the case history for edits made to a designated case.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListCaseEdits. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element to identify how many results to obtain. There is a maximum value of 25.</p>
            case_id: <p>Required element used with ListCaseEdits to identify the case to query.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListCaseEdits

            >>> client.list_case_edits(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_case_edits_request.ListCaseEditsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_case_edits_response.ListCaseEditsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_case_edits

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_case_edits.list_case_edits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.list_case_edits_request.ListCaseEditsRequest = {
            "case_id": case_id
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

    def iter_list_case_edits(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_security_ir.types.case_edit_item.CaseEditItem]":
        _token = next_token
        while True:
            _response = self.list_case_edits(
                case_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_comments(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_comments_response.ListCommentsResponse":
        """<p>Returns comments for a designated case.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListComments. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Optional element for ListComments to limit the number of responses.</p>
            case_id: <p>Required element for ListComments to designate the case to query.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListComments

            >>> client.list_comments(case_id='8403556009')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_comments_request.ListCommentsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_comments_response.ListCommentsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_comments

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_comments.list_comments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.list_comments_request.ListCommentsRequest = {
            "case_id": case_id
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

    def iter_list_comments(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_security_ir.types.list_comments_item.ListCommentsItem]":
        _token = next_token
        while True:
            _response = self.list_comments(
                case_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_investigations(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_security_ir.types.list_investigations_response.ListInvestigationsResponse"
    ):
        """<p>Investigation performed by an agent for a security incident...</p>

        Args:
            next_token: <p>Investigation performed by an agent for a security incident request</p>
            max_results: <p>Investigation performed by an agent for a security incident request, returning max results</p>
            case_id: <p>Investigation performed by an agent for a security incident per caseID</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListInvestigations with feedback examples

            >>> client.list_investigations(case_id='8403556009', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_investigations_request.ListInvestigationsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_investigations_response.ListInvestigationsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_investigations

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_investigations.list_investigations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.list_investigations_request.ListInvestigationsRequest = {
            "case_id": case_id
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

    def iter_list_investigations(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_security_ir.types.investigation_action.InvestigationAction]":
        _token = next_token
        while True:
            _response = self.list_investigations(
                case_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("investigation_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def send_feedback(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        result_id: "capo_security_ir.types.result_id.ResultId",
        usefulness: "capo_security_ir.types.usefulness_rating.UsefulnessRating",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        comment: Optional[
            "capo_security_ir.types.feedback_comment.FeedbackComment"
        ] = None,
    ) -> "capo_security_ir.types.send_feedback_response.SendFeedbackResponse":
        """<p>Send feedback based on response investigation action</p>

        Args:
            case_id: <p>Send feedback based on request caseID</p>
            result_id: <p>Send feedback based on request result ID</p>
            usefulness: <p>Required enum value indicating user assessment of result q.....</p>
            comment: <p>Send feedback based on request comments</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Send positive feedback for investigation result

            >>> client.send_feedback(case_id='8403556009', result_id='inv-polkjhyuty', usefulness='USEFUL', comment='The CloudTrail analysis was very helpful in identifying the root cause of the security incident.')
            Send negative feedback with detailed comment

            >>> client.send_feedback(case_id='8403556009', result_id='inv-irutjfhgjk', usefulness='NOT_USEFUL', comment="The investigation results were too generic and didn't provide actionable insights for our specific incident.")
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.send_feedback_request.SendFeedbackRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.send_feedback_response.SendFeedbackResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.send_feedback

            output, http_response = (
                capo_security_ir._operations.security_incident_response.send_feedback.send_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.send_feedback_request.SendFeedbackRequest = {
            "case_id": case_id,
            "result_id": result_id,
            "usefulness": usefulness,
        }
        if comment is not None:
            input_["comment"] = comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_case_comment(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        comment_id: "capo_security_ir.types.comment_id.CommentId",
        body: "capo_security_ir.types.comment_body.CommentBody",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> (
        "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse"
    ):
        """<p>Updates an existing case comment.</p>

        Args:
            case_id: <p>Required element for UpdateCaseComment to identify the case ID containing the comment to be updated. </p>
            comment_id: <p>Required element for UpdateCaseComment to identify the case ID to be updated.</p>
            body: <p>Required element for UpdateCaseComment to identify the content for the comment to be updated.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCaseComment

            >>> client.update_case_comment(case_id='8403556009', comment_id='000000', body='Updated case comment.')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_case_comment_response.UpdateCaseCommentResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case_comment

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_case_comment.update_case_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.update_case_comment_request.UpdateCaseCommentRequest = {
            "case_id": case_id,
            "comment_id": comment_id,
            "body": body,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_case_status(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        case_status: "capo_security_ir.types.self_managed_case_status.SelfManagedCaseStatus",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.update_case_status_response.UpdateCaseStatusResponse":
        """<p>Updates the state transitions for a designated cases.</p> <p> <b>Self-managed</b>: the following states are available for self-managed cases. </p> <ul> <li> <p>Submitted → Detection and Analysis</p> </li> <li> <p>Detection and Analysis → Containment, Eradication, and Recovery</p> </li> <li> <p>Detection and Analysis → Post-incident Activities</p> </li> <li> <p>Containment, Eradication, and Recovery → Detection and Analysis</p> </li> <li> <p>Containment, Eradication, and Recovery → Post-incident Activities</p> </li> <li> <p>Post-incident Activities → Containment, Eradication, and Recovery</p> </li> <li> <p>Post-incident Activities → Detection and Analysis</p> </li> <li> <p>Any → Closed</p> </li> </ul> <p> <b>AWS supported</b>: You must use the <code>CloseCase</code> API to close. </p>

        Args:
            case_id: <p>Required element for UpdateCaseStatus to identify the case to update.</p>
            case_status: <p>Required element for UpdateCaseStatus to identify the status for a case. Options include <code>Submitted | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities</code>. </p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateCaseStatus

            >>> client.update_case_status(case_id='8403556009', case_status='Post-incident Activities')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_case_status_request.UpdateCaseStatusRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_case_status_response.UpdateCaseStatusResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_case_status

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_case_status.update_case_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.update_case_status_request.UpdateCaseStatusRequest = {
            "case_id": case_id,
            "case_status": case_status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resolver_type(
        self,
        case_id: "capo_security_ir.types.case_id.CaseId",
        resolver_type: "capo_security_ir.types.resolver_type.ResolverType",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.update_resolver_type_response.UpdateResolverTypeResponse":
        """<p>Updates the resolver type for a case.</p> <important> <p>This is a one-way action and cannot be reversed.</p> </important>

        Args:
            case_id: <p>Required element for UpdateResolverType to identify the case to update.</p>
            resolver_type: <p>Required element for UpdateResolverType to identify the new resolver.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateResolverType

            >>> client.update_resolver_type(case_id='8403556009', resolver_type='AWS')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_resolver_type_request.UpdateResolverTypeRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_resolver_type_response.UpdateResolverTypeResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_resolver_type

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_resolver_type.update_resolver_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.update_resolver_type_request.UpdateResolverTypeRequest = {
            "case_id": case_id,
            "resolver_type": resolver_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_membership(
        self,
        membership_name: "capo_security_ir.types.membership_name.MembershipName",
        incident_response_team: "capo_security_ir.types.incident_response_team.IncidentResponseTeam",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        client_token: Optional[str] = None,
        opt_in_features: Optional[
            "capo_security_ir.types.opt_in_features.OptInFeatures"
        ] = None,
        tags: Optional["capo_security_ir.types.tag_map.TagMap"] = None,
        cover_entire_organization: Optional[bool] = None,
    ) -> "capo_security_ir.types.create_membership_response.CreateMembershipResponse":
        """<p>Creates a new membership.</p>

        Args:
            client_token: <note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>
            membership_name: <p>Required element used in combination with CreateMembership to create a name for the membership.</p>
            incident_response_team: <p>Required element used in combination with CreateMembership to add customer incident response team members and trusted partners to the membership. </p>
            opt_in_features: <p>Optional element to enable the monitoring and investigation opt-in features for the service.</p>
            tags: <p>Optional element for customer configured tags.</p>
            cover_entire_organization: <p>The <code>coverEntireOrganization</code> parameter is a boolean flag that determines whether the membership should be applied to the entire Amazon Web Services Organization. When set to true, the membership will be created for all accounts within the organization. When set to false, the membership will only be created for specified accounts. </p> <p>This parameter is optional. If not specified, the default value is false.</p> <ul> <li> <p>If set to <i>true</i>: The membership will automatically include all existing and future accounts in the Amazon Web Services Organization. </p> </li> <li> <p>If set to <i>false</i>: The membership will only apply to explicitly specified accounts. </p> </li> </ul>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateMembership

            >>> client.create_membership(membership_name='Example Membership Name.', incident_response_team=[{'name': 'Bob Jones', 'jobTitle': 'Security Responder', 'email': 'bob.jones@gmail.com'}, {'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}], opt_in_features=[{'featureName': 'Triage', 'isEnabled': True}])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.create_membership_request.CreateMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.create_membership_response.CreateMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.create_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.create_membership.create_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.create_membership_request.CreateMembershipRequest = {
            "membership_name": membership_name,
            "incident_response_team": incident_response_team,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if opt_in_features is not None:
            input_["opt_in_features"] = opt_in_features
        if tags is not None:
            input_["tags"] = tags
        if cover_entire_organization is not None:
            input_["cover_entire_organization"] = cover_entire_organization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_membership(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.get_membership_response.GetMembershipResponse":
        """<p>Returns the attributes of a membership.</p>

        Args:
            membership_id: <p>Required element for GetMembership to identify the membership ID to query.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetMembership

            >>> client.get_membership(membership_id='m-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_membership_request.GetMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_membership_response.GetMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_membership.get_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.get_membership_request.GetMembershipRequest = {
            "membership_id": membership_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_membership(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        membership_name: Optional[
            "capo_security_ir.types.membership_name.MembershipName"
        ] = None,
        incident_response_team: Optional[
            "capo_security_ir.types.incident_response_team.IncidentResponseTeam"
        ] = None,
        opt_in_features: Optional[
            "capo_security_ir.types.opt_in_features.OptInFeatures"
        ] = None,
        membership_accounts_configurations_update: Optional[
            "capo_security_ir.types.membership_accounts_configurations_update.MembershipAccountsConfigurationsUpdate"
        ] = None,
        undo_membership_cancellation: Optional[bool] = None,
    ) -> "capo_security_ir.types.update_membership_response.UpdateMembershipResponse":
        """<p>Updates membership configuration.</p>

        Args:
            membership_id: <p>Required element for UpdateMembership to identify the membership to update.</p>
            membership_name: <p>Optional element for UpdateMembership to update the membership name.</p>
            incident_response_team: <p>Optional element for UpdateMembership to update the membership name.</p>
            opt_in_features: <p>Optional element for UpdateMembership to enable or disable opt-in features for the service.</p>
            membership_accounts_configurations_update: <p>The <code>membershipAccountsConfigurationsUpdate</code> field in the <code>UpdateMembershipRequest</code> structure allows you to update the configuration settings for accounts within a membership. </p> <p>This field is optional and contains a structure of type <code>MembershipAccountsConfigurationsUpdate </code> that specifies the updated account configurations for the membership. </p>
            undo_membership_cancellation: <p>The <code>undoMembershipCancellation</code> parameter is a boolean flag that indicates whether to reverse a previously requested membership cancellation. When set to true, this will revoke the cancellation request and maintain the membership status. </p> <p>This parameter is optional and can be used in scenarios where you need to restore a membership that was marked for cancellation but hasn't been fully terminated yet. </p> <ul> <li> <p>If set to <code>true</code>, the cancellation request will be revoked </p> </li> <li> <p>If set to <code>false</code> the service will throw a ValidationException. </p> </li> </ul>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateMembership

            >>> client.update_membership(membership_id='m-abcd1234efgh', membership_name='New membership name', incident_response_team=[{'name': 'Bob Jones', 'jobTitle': 'Security Responder', 'email': 'bob.jones@gmail.com'}, {'email': 'alice@example.com', 'name': 'Alice', 'jobTitle': 'CEO'}], opt_in_features=[{'featureName': 'Triage', 'isEnabled': True}])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.update_membership_request.UpdateMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.update_membership_response.UpdateMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.update_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.update_membership.update_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.update_membership_request.UpdateMembershipRequest = {
            "membership_id": membership_id
        }
        if membership_name is not None:
            input_["membership_name"] = membership_name
        if incident_response_team is not None:
            input_["incident_response_team"] = incident_response_team
        if opt_in_features is not None:
            input_["opt_in_features"] = opt_in_features
        if membership_accounts_configurations_update is not None:
            input_["membership_accounts_configurations_update"] = (
                membership_accounts_configurations_update
            )
        if undo_membership_cancellation is not None:
            input_["undo_membership_cancellation"] = undo_membership_cancellation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_memberships(
        self,
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_security_ir.types.list_memberships_response.ListMembershipsResponse":
        """<p>Returns the memberships that the calling principal can access.</p>

        Args:
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListMemberships. When provided in this manner, the API fetches the next page of results. </p>
            max_results: <p>Request element for ListMemberships to limit the number of responses.</p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListMemberships

            >>> client.list_memberships(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.list_memberships_request.ListMembershipsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.list_memberships_response.ListMembershipsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.list_memberships

            output, http_response = (
                capo_security_ir._operations.security_incident_response.list_memberships.list_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.list_memberships_request.ListMembershipsRequest = {}
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

    def iter_list_memberships(
        self,
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_security_ir.types.list_membership_item.ListMembershipItem]":
        _token = next_token
        while True:
            _response = self.list_memberships(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def batch_get_member_account_details(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        account_ids: "capo_security_ir.types.aws_account_ids.AWSAccountIds",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.batch_get_member_account_details_response.BatchGetMemberAccountDetailsResponse":
        """<p>Provides information on whether the supplied account IDs are associated with a membership.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>

        Args:
            membership_id: <p>Required element used in combination with BatchGetMemberAccountDetails to identify the membership ID to query. </p>
            account_ids: <p>Optional element to query the membership relationship status to a provided list of account IDs.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke BatchGetMemberAccountDetails

            >>> client.batch_get_member_account_details(membership_id='m-abcd1234efgh', account_ids=['123412341234'])
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.batch_get_member_account_details_request.BatchGetMemberAccountDetailsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.batch_get_member_account_details_response.BatchGetMemberAccountDetailsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.batch_get_member_account_details

            output, http_response = (
                capo_security_ir._operations.security_incident_response.batch_get_member_account_details.batch_get_member_account_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.batch_get_member_account_details_request.BatchGetMemberAccountDetailsRequest = {
            "membership_id": membership_id,
            "account_ids": account_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_membership(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "capo_security_ir.types.cancel_membership_response.CancelMembershipResponse":
        """<p>Cancels an existing membership.</p>

        Args:
            membership_id: <p>Required element used in combination with CancelMembershipRequest to identify the membership ID to cancel. </p>

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CancelMembership

            >>> client.cancel_membership(membership_id='m-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.cancel_membership_request.CancelMembershipRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.cancel_membership_response.CancelMembershipResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.cancel_membership

            output, http_response = (
                capo_security_ir._operations.security_incident_response.cancel_membership.cancel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.cancel_membership_request.CancelMembershipRequest = {
            "membership_id": membership_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_finding_metrics(
        self,
        membership_id: "capo_security_ir.types.membership_id.MembershipId",
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> (
        "capo_security_ir.types.get_finding_metrics_response.GetFindingMetricsResponse"
    ):
        """Returns finding-lifecycle metrics for a membership over a date range.

        Args:
            membership_id: The membership ID to retrieve metrics for.
            start_date: The start of the day-aligned UTC window, inclusive.
            end_date: The end of the day-aligned UTC window, inclusive.

        Raises:
            capo_security_ir.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_security_ir.errors.conflict_exception.ConflictException: <p/>
            capo_security_ir.errors.internal_server_exception.InternalServerException: <p/>
            capo_security_ir.errors.invalid_token_exception.InvalidTokenException: <p/>
            capo_security_ir.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_security_ir.errors.security_incident_response_not_active_exception.SecurityIncidentResponseNotActiveException: <p/>
            capo_security_ir.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_security_ir.errors.throttling_exception.ThrottlingException: <p/>
            capo_security_ir.errors.validation_exception.ValidationException: <p/>
            capo_security_ir.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve finding-lifecycle metrics for a membership

            >>> client.get_finding_metrics(membership_id='m-a1b2c3d4e5f', start_date='2026-08-01T00:00:00Z', end_date='2026-08-18T00:00:00Z')
        """

        def _handler(
            req: "OperationRequest[capo_security_ir.types.get_finding_metrics_request.GetFindingMetricsRequest]",
        ) -> OperationResponse[
            "capo_security_ir.types.get_finding_metrics_response.GetFindingMetricsResponse"
        ]:
            import capo_security_ir._operations.security_incident_response.get_finding_metrics

            output, http_response = (
                capo_security_ir._operations.security_incident_response.get_finding_metrics.get_finding_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_security_ir.types.get_finding_metrics_request.GetFindingMetricsRequest = {
            "membership_id": membership_id,
            "start_date": start_date,
            "end_date": end_date,
        }

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

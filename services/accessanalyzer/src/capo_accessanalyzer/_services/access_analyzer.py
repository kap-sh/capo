"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccessAnalyzer``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_accessanalyzer._auth._signers
import capo_accessanalyzer._auth._sigv4
from capo_accessanalyzer._auth._identity import Credentials
from capo_accessanalyzer._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_accessanalyzer._auth._zapros_handler import AuthMiddleware
from capo_accessanalyzer._pagination import resolve_path as _resolve_path
from capo_accessanalyzer._resources.access_analyzer.analyzer import Analyzer
from capo_accessanalyzer._services._aws_config import aws_config
from capo_accessanalyzer._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_check_policy_document
    import capo_accessanalyzer.types.access_check_policy_type
    import capo_accessanalyzer.types.access_check_resource_type
    import capo_accessanalyzer.types.access_list
    import capo_accessanalyzer.types.access_preview_id
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.analyzer_configuration
    import capo_accessanalyzer.types.analyzer_name
    import capo_accessanalyzer.types.apply_archive_rule_request
    import capo_accessanalyzer.types.cancel_policy_generation_request
    import capo_accessanalyzer.types.cancel_policy_generation_response
    import capo_accessanalyzer.types.check_access_not_granted_request
    import capo_accessanalyzer.types.check_access_not_granted_response
    import capo_accessanalyzer.types.check_no_new_access_request
    import capo_accessanalyzer.types.check_no_new_access_response
    import capo_accessanalyzer.types.check_no_public_access_request
    import capo_accessanalyzer.types.check_no_public_access_response
    import capo_accessanalyzer.types.cloud_trail_details
    import capo_accessanalyzer.types.configurations_map
    import capo_accessanalyzer.types.create_access_preview_request
    import capo_accessanalyzer.types.create_access_preview_response
    import capo_accessanalyzer.types.create_analyzer_request
    import capo_accessanalyzer.types.create_analyzer_response
    import capo_accessanalyzer.types.create_archive_rule_request
    import capo_accessanalyzer.types.create_service_linked_analyzer_request
    import capo_accessanalyzer.types.create_service_linked_analyzer_response
    import capo_accessanalyzer.types.delete_analyzer_request
    import capo_accessanalyzer.types.delete_archive_rule_request
    import capo_accessanalyzer.types.delete_service_linked_analyzer_request
    import capo_accessanalyzer.types.filter_criteria_map
    import capo_accessanalyzer.types.finding_id
    import capo_accessanalyzer.types.finding_id_list
    import capo_accessanalyzer.types.finding_status_update
    import capo_accessanalyzer.types.generate_finding_recommendation_request
    import capo_accessanalyzer.types.get_access_preview_request
    import capo_accessanalyzer.types.get_access_preview_response
    import capo_accessanalyzer.types.get_analyzed_resource_request
    import capo_accessanalyzer.types.get_analyzed_resource_response
    import capo_accessanalyzer.types.get_analyzer_request
    import capo_accessanalyzer.types.get_analyzer_response
    import capo_accessanalyzer.types.get_archive_rule_request
    import capo_accessanalyzer.types.get_archive_rule_response
    import capo_accessanalyzer.types.get_finding_recommendation_request
    import capo_accessanalyzer.types.get_finding_recommendation_response
    import capo_accessanalyzer.types.get_finding_request
    import capo_accessanalyzer.types.get_finding_response
    import capo_accessanalyzer.types.get_finding_v2_request
    import capo_accessanalyzer.types.get_finding_v2_response
    import capo_accessanalyzer.types.get_findings_statistics_request
    import capo_accessanalyzer.types.get_findings_statistics_response
    import capo_accessanalyzer.types.get_generated_policy_request
    import capo_accessanalyzer.types.get_generated_policy_response
    import capo_accessanalyzer.types.inline_archive_rules_list
    import capo_accessanalyzer.types.job_id
    import capo_accessanalyzer.types.list_access_preview_findings_request
    import capo_accessanalyzer.types.list_access_preview_findings_response
    import capo_accessanalyzer.types.list_access_previews_request
    import capo_accessanalyzer.types.list_access_previews_response
    import capo_accessanalyzer.types.list_analyzed_resources_request
    import capo_accessanalyzer.types.list_analyzed_resources_response
    import capo_accessanalyzer.types.list_analyzers_request
    import capo_accessanalyzer.types.list_analyzers_response
    import capo_accessanalyzer.types.list_archive_rules_request
    import capo_accessanalyzer.types.list_archive_rules_response
    import capo_accessanalyzer.types.list_findings_request
    import capo_accessanalyzer.types.list_findings_response
    import capo_accessanalyzer.types.list_findings_v2_request
    import capo_accessanalyzer.types.list_findings_v2_response
    import capo_accessanalyzer.types.list_policy_generations_request
    import capo_accessanalyzer.types.list_policy_generations_response
    import capo_accessanalyzer.types.list_tags_for_resource_request
    import capo_accessanalyzer.types.list_tags_for_resource_response
    import capo_accessanalyzer.types.locale
    import capo_accessanalyzer.types.name
    import capo_accessanalyzer.types.policy_document
    import capo_accessanalyzer.types.policy_generation_details
    import capo_accessanalyzer.types.policy_type
    import capo_accessanalyzer.types.principal_arn
    import capo_accessanalyzer.types.recommended_step
    import capo_accessanalyzer.types.resource_arn
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.sort_criteria
    import capo_accessanalyzer.types.start_policy_generation_request
    import capo_accessanalyzer.types.start_policy_generation_response
    import capo_accessanalyzer.types.start_resource_scan_request
    import capo_accessanalyzer.types.tag_keys
    import capo_accessanalyzer.types.tag_resource_request
    import capo_accessanalyzer.types.tag_resource_response
    import capo_accessanalyzer.types.tags_map
    import capo_accessanalyzer.types.token
    import capo_accessanalyzer.types.type
    import capo_accessanalyzer.types.untag_resource_request
    import capo_accessanalyzer.types.untag_resource_response
    import capo_accessanalyzer.types.update_analyzer_request
    import capo_accessanalyzer.types.update_analyzer_response
    import capo_accessanalyzer.types.update_archive_rule_request
    import capo_accessanalyzer.types.update_findings_request
    import capo_accessanalyzer.types.validate_policy_request
    import capo_accessanalyzer.types.validate_policy_resource_type
    import capo_accessanalyzer.types.validate_policy_response


class AccessAnalyzerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AccessAnalyzerClient:
    """A client for the ``AccessAnalyzer`` service.

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
        self._config = AccessAnalyzerClientConfig(
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
        self.analyzer = Analyzer(self)

    def operation_options(
        self, config_overrides: Optional[AccessAnalyzerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AccessAnalyzerClientConfig = config_overrides or {}
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

    def apply_archive_rule(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        rule_name: "capo_accessanalyzer.types.name.Name",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Retroactively applies the archive rule to existing findings that meet the archive rule criteria.</p>

        Args:
            analyzer_arn: <p>The Amazon resource name (ARN) of the analyzer.</p>
            rule_name: <p>The name of the rule to apply.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.apply_archive_rule_request.ApplyArchiveRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.apply_archive_rule

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.apply_archive_rule.apply_archive_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.apply_archive_rule_request.ApplyArchiveRuleRequest = {
            "analyzer_arn": analyzer_arn,
            "rule_name": rule_name,
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

    def cancel_policy_generation(
        self,
        job_id: "capo_accessanalyzer.types.job_id.JobId",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.cancel_policy_generation_response.CancelPolicyGenerationResponse":
        """<p>Cancels the requested policy generation.</p>

        Args:
            job_id: <p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.cancel_policy_generation_request.CancelPolicyGenerationRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.cancel_policy_generation_response.CancelPolicyGenerationResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.cancel_policy_generation

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.cancel_policy_generation.cancel_policy_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.cancel_policy_generation_request.CancelPolicyGenerationRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def check_access_not_granted(
        self,
        policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument",
        access: "capo_accessanalyzer.types.access_list.AccessList",
        policy_type: "capo_accessanalyzer.types.access_check_policy_type.AccessCheckPolicyType",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.check_access_not_granted_response.CheckAccessNotGrantedResponse":
        """<p>Checks whether the specified access isn't allowed by a policy.</p>

        Args:
            policy_document: <p>The JSON policy document to use as the content for the policy.</p>
            access: <p>An access object containing the permissions that shouldn't be granted by the specified policy. If only actions are specified, IAM Access Analyzer checks for access to peform at least one of the actions on any resource in the policy. If only resources are specified, then IAM Access Analyzer checks for access to perform any action on at least one of the resources. If both actions and resources are specified, IAM Access Analyzer checks for access to perform at least one of the specified actions on at least one of the specified resources.</p>
            policy_type: <p>The type of policy. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.</p> <p>Resource policies grant permissions on Amazon Web Services resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.unprocessable_entity_exception.UnprocessableEntityException: <p>The specified entity could not be processed.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Passing check. Restrictive identity policy.

            >>> client.check_access_not_granted(access=[{'actions': ['s3:PutObject']}], policy_document='{"Version":"2012-10-17","Id":"123","Statement":[{"Sid":"AllowJohnDoe","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:user/JohnDoe"},"Action":"s3:GetObject","Resource":"*"}]}', policy_type='RESOURCE_POLICY')
            Passing check. Restrictive S3 Bucket resource policy.

            >>> client.check_access_not_granted(access=[{'resources': ['arn:aws:s3:::sensitive-bucket/*']}], policy_document='{"Version":"2012-10-17","Id":"123","Statement":[{"Sid":"AllowJohnDoe","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:user/JohnDoe"},"Action":"s3:PutObject","Resource":"arn:aws:s3:::non-sensitive-bucket/*"}]}', policy_type='RESOURCE_POLICY')
            Failing check. Permissive S3 Bucket resource policy.

            >>> client.check_access_not_granted(access=[{'resources': ['arn:aws:s3:::my-bucket/*']}], policy_document='{"Version":"2012-10-17","Id":"123","Statement":[{"Sid":"AllowJohnDoe","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:user/JohnDoe"},"Action":"s3:PutObject","Resource":"arn:aws:s3:::my-bucket/*"}]}', policy_type='RESOURCE_POLICY')
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.check_access_not_granted_request.CheckAccessNotGrantedRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.check_access_not_granted_response.CheckAccessNotGrantedResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.check_access_not_granted

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.check_access_not_granted.check_access_not_granted(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.check_access_not_granted_request.CheckAccessNotGrantedRequest = {
            "policy_document": policy_document,
            "access": access,
            "policy_type": policy_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def check_no_new_access(
        self,
        new_policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument",
        existing_policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument",
        policy_type: "capo_accessanalyzer.types.access_check_policy_type.AccessCheckPolicyType",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.check_no_new_access_response.CheckNoNewAccessResponse":
        """<p>Checks whether new access is allowed for an updated policy when compared to the existing policy.</p> <p>You can find examples for reference policies and learn how to set up and run a custom policy check for new access in the <a href="https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples">IAM Access Analyzer custom policy checks samples</a> repository on GitHub. The reference policies in this repository are meant to be passed to the <code>existingPolicyDocument</code> request parameter.</p>

        Args:
            new_policy_document: <p>The JSON policy document to use as the content for the updated policy.</p>
            existing_policy_document: <p>The JSON policy document to use as the content for the existing policy.</p>
            policy_type: <p>The type of policy to compare. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.</p> <p>Resource policies grant permissions on Amazon Web Services resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.unprocessable_entity_exception.UnprocessableEntityException: <p>The specified entity could not be processed.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.check_no_new_access_request.CheckNoNewAccessRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.check_no_new_access_response.CheckNoNewAccessResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.check_no_new_access

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.check_no_new_access.check_no_new_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.check_no_new_access_request.CheckNoNewAccessRequest = {
            "new_policy_document": new_policy_document,
            "existing_policy_document": existing_policy_document,
            "policy_type": policy_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def check_no_public_access(
        self,
        policy_document: "capo_accessanalyzer.types.access_check_policy_document.AccessCheckPolicyDocument",
        resource_type: "capo_accessanalyzer.types.access_check_resource_type.AccessCheckResourceType",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.check_no_public_access_response.CheckNoPublicAccessResponse":
        """<p>Checks whether a resource policy can grant public access to the specified resource type.</p>

        Args:
            policy_document: <p>The JSON policy document to evaluate for public access.</p>
            resource_type: <p>The type of resource to evaluate for public access. For example, to check for public access to Amazon S3 buckets, you can choose <code>AWS::S3::Bucket</code> for the resource type.</p> <p>For resource types not supported as valid values, IAM Access Analyzer will return an error.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.unprocessable_entity_exception.UnprocessableEntityException: <p>The specified entity could not be processed.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Passing check. S3 Bucket policy without public access.

            >>> client.check_no_public_access(policy_document='{"Version":"2012-10-17","Statement":[{"Sid":"Bob","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::111122223333:user/JohnDoe"},"Action":["s3:GetObject"]}]}', resource_type='AWS::S3::Bucket')
            Failing check. S3 Bucket policy with public access.

            >>> client.check_no_public_access(policy_document='{"Version":"2012-10-17","Statement":[{"Sid":"Bob","Effect":"Allow","Principal":"*","Action":["s3:GetObject"]}]}', resource_type='AWS::S3::Bucket')
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.check_no_public_access_request.CheckNoPublicAccessRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.check_no_public_access_response.CheckNoPublicAccessResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.check_no_public_access

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.check_no_public_access.check_no_public_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.check_no_public_access_request.CheckNoPublicAccessRequest = {
            "policy_document": policy_document,
            "resource_type": resource_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_access_preview(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        configurations: "capo_accessanalyzer.types.configurations_map.ConfigurationsMap",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_accessanalyzer.types.create_access_preview_response.CreateAccessPreviewResponse":
        """<p>Creates an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the account analyzer</a> used to generate the access preview. You can only create an access preview for analyzers with an <code>Account</code> type and <code>Active</code> status.</p>
            configurations: <p>Access control configuration for your resource that is used to generate the access preview. The access preview includes findings for external access allowed to the resource with the proposed access control configuration. The configuration must contain exactly one element.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quote met error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.create_access_preview_request.CreateAccessPreviewRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.create_access_preview_response.CreateAccessPreviewResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.create_access_preview

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.create_access_preview.create_access_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.create_access_preview_request.CreateAccessPreviewRequest = {
            "analyzer_arn": analyzer_arn,
            "configurations": configurations,
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

    def create_service_linked_analyzer(
        self,
        type: "capo_accessanalyzer.types.type.Type",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        archive_rules: Optional[
            "capo_accessanalyzer.types.inline_archive_rules_list.InlineArchiveRulesList"
        ] = None,
        client_token: Optional[str] = None,
        configuration: Optional[
            "capo_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
        ] = None,
    ) -> "capo_accessanalyzer.types.create_service_linked_analyzer_response.CreateServiceLinkedAnalyzerResponse":
        """<p>Creates a service-linked analyzer managed by an Amazon Web Services service. This operation can only be invoked by authorized Amazon Web Services services. Direct customer invocation returns <code>AccessDeniedException</code>.</p> <p>Service-linked analyzers enable Amazon Web Services services to create and manage analyzers on behalf of customers. The lifecycle of these analyzers is managed by the calling service.</p>

        Args:
            type: <p>The type of analyzer to create. Valid values are <code>ACCOUNT_UNUSED_ACCESS</code> and <code>ORGANIZATION_UNUSED_ACCESS</code>.</p>
            archive_rules: <p>Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.</p>
            client_token: <p>A client token.</p>
            configuration: <p>Specifies the configuration of the analyzer. The specified scope of unused access is used for the configuration.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quote met error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.create_service_linked_analyzer_request.CreateServiceLinkedAnalyzerRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.create_service_linked_analyzer_response.CreateServiceLinkedAnalyzerResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.create_service_linked_analyzer

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.create_service_linked_analyzer.create_service_linked_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.create_service_linked_analyzer_request.CreateServiceLinkedAnalyzerRequest = {
            "type": type
        }
        if archive_rules is not None:
            input_["archive_rules"] = archive_rules
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def generate_finding_recommendation(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        id: str,
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> None:
        """<p>Creates a recommendation for an unused permissions finding.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the finding recommendation.</p>
            id: <p>The unique ID for the finding recommendation.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successfully started generating finding recommendation

            >>> client.generate_finding_recommendation(analyzer_arn='arn:aws:access-analyzer:us-east-1:111122223333:analyzer/a', id='finding-id')
            Failed field validation for id value

            >>> client.generate_finding_recommendation(analyzer_arn='arn:aws:access-analyzer:us-east-1:111122223333:analyzer/a', id='!')
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.generate_finding_recommendation_request.GenerateFindingRecommendationRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.generate_finding_recommendation

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.generate_finding_recommendation.generate_finding_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.generate_finding_recommendation_request.GenerateFindingRecommendationRequest = {
            "analyzer_arn": analyzer_arn,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_access_preview(
        self,
        access_preview_id: "capo_accessanalyzer.types.access_preview_id.AccessPreviewId",
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> (
        "capo_accessanalyzer.types.get_access_preview_response.GetAccessPreviewResponse"
    ):
        """<p>Retrieves information about an access preview for the specified analyzer.</p>

        Args:
            access_preview_id: <p>The unique ID for the access preview.</p>
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the access preview.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_access_preview_request.GetAccessPreviewRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_access_preview_response.GetAccessPreviewResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_access_preview

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_access_preview.get_access_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_access_preview_request.GetAccessPreviewRequest = {
            "access_preview_id": access_preview_id,
            "analyzer_arn": analyzer_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_analyzed_resource(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        resource_arn: "capo_accessanalyzer.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.get_analyzed_resource_response.GetAnalyzedResourceResponse":
        """<p>Retrieves information about a resource that was analyzed.</p> <note> <p>This action is supported only for external access analyzers.</p> </note>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve information from.</p>
            resource_arn: <p>The ARN of the resource to retrieve information about.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_analyzed_resource_request.GetAnalyzedResourceRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_analyzed_resource_response.GetAnalyzedResourceResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_analyzed_resource

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_analyzed_resource.get_analyzed_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_analyzed_resource_request.GetAnalyzedResourceRequest = {
            "analyzer_arn": analyzer_arn,
            "resource_arn": resource_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_finding(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        id: "capo_accessanalyzer.types.finding_id.FindingId",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.get_finding_response.GetFindingResponse":
        """<p>Retrieves information about the specified finding. GetFinding and GetFindingV2 both use <code>access-analyzer:GetFinding</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>access-analyzer:GetFinding</code> action.</p> <note> <p>GetFinding is supported only for external access analyzers. You must use GetFindingV2 for internal and unused access analyzers.</p> </note>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> that generated the finding.</p>
            id: <p>The ID of the finding to retrieve.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_finding_request.GetFindingRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_finding_response.GetFindingResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_finding

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_finding.get_finding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_finding_request.GetFindingRequest = {
            "analyzer_arn": analyzer_arn,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_finding_recommendation(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        id: str,
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
    ) -> "capo_accessanalyzer.types.get_finding_recommendation_response.GetFindingRecommendationResponse":
        """<p>Retrieves information about a finding recommendation for the specified analyzer.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the finding recommendation.</p>
            id: <p>The unique ID for the finding recommendation.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token used for pagination of results returned.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successfully fetched finding recommendation

            >>> client.get_finding_recommendation(analyzer_arn='arn:aws:access-analyzer:us-east-1:111122223333:analyzer/a', id='finding-id', max_results=3, next_token='token')
            In progress finding recommendation

            >>> client.get_finding_recommendation(analyzer_arn='arn:aws:access-analyzer:us-east-1:111122223333:analyzer/a', id='finding-id', max_results=3)
            Failed finding recommendation

            >>> client.get_finding_recommendation(analyzer_arn='arn:aws:access-analyzer:us-east-1:111122223333:analyzer/a', id='finding-id', max_results=3)
            Failed field validation for id value

            >>> client.get_finding_recommendation(analyzer_arn='arn:aws:access-analyzer:us-east-1:111122223333:analyzer/a', id='!')
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_finding_recommendation_request.GetFindingRecommendationRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_finding_recommendation_response.GetFindingRecommendationResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_finding_recommendation

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_finding_recommendation.get_finding_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_finding_recommendation_request.GetFindingRecommendationRequest = {
            "analyzer_arn": analyzer_arn,
            "id": id,
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

    def iter_get_finding_recommendation(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        id: str,
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
    ) -> "Iterator[capo_accessanalyzer.types.recommended_step.RecommendedStep]":
        _token = next_token
        while True:
            _response = self.get_finding_recommendation(
                analyzer_arn,
                id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommended_steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_findings_statistics(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.get_findings_statistics_response.GetFindingsStatisticsResponse":
        """<p>Retrieves a list of aggregated finding statistics for an external access or unused access analyzer.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the statistics.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_findings_statistics_request.GetFindingsStatisticsRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_findings_statistics_response.GetFindingsStatisticsResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_findings_statistics

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_findings_statistics.get_findings_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_findings_statistics_request.GetFindingsStatisticsRequest = {
            "analyzer_arn": analyzer_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_finding_v2(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        id: "capo_accessanalyzer.types.finding_id.FindingId",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
    ) -> "capo_accessanalyzer.types.get_finding_v2_response.GetFindingV2Response":
        """<p>Retrieves information about the specified finding. GetFinding and GetFindingV2 both use <code>access-analyzer:GetFinding</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>access-analyzer:GetFinding</code> action.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> that generated the finding.</p>
            id: <p>The ID of the finding to retrieve.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token used for pagination of results returned.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_finding_v2_request.GetFindingV2Request]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_finding_v2_response.GetFindingV2Response"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_finding_v2

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_finding_v2.get_finding_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_finding_v2_request.GetFindingV2Request = {
            "analyzer_arn": analyzer_arn,
            "id": id,
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

    def get_generated_policy(
        self,
        job_id: "capo_accessanalyzer.types.job_id.JobId",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        include_resource_placeholders: Optional[bool] = None,
        include_service_level_template: Optional[bool] = None,
    ) -> "capo_accessanalyzer.types.get_generated_policy_response.GetGeneratedPolicyResponse":
        """<p>Retrieves the policy that was generated using <code>StartPolicyGeneration</code>. </p>

        Args:
            job_id: <p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>
            include_resource_placeholders: <p>The level of detail that you want to generate. You can specify whether to generate policies with placeholders for resource ARNs for actions that support resource level granularity in policies.</p> <p>For example, in the resource section of a policy, you can receive a placeholder such as <code>"Resource":"arn:aws:s3:::${BucketName}"</code> instead of <code>"*"</code>.</p>
            include_service_level_template: <p>The level of detail that you want to generate. You can specify whether to generate service-level policies. </p> <p>IAM Access Analyzer uses <code>iam:servicelastaccessed</code> to identify services that have been used recently to create this service-level template.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_generated_policy_request.GetGeneratedPolicyRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_generated_policy_response.GetGeneratedPolicyResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_generated_policy

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_generated_policy.get_generated_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_generated_policy_request.GetGeneratedPolicyRequest = {
            "job_id": job_id
        }
        if include_resource_placeholders is not None:
            input_["include_resource_placeholders"] = include_resource_placeholders
        if include_service_level_template is not None:
            input_["include_service_level_template"] = include_service_level_template

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_access_preview_findings(
        self,
        access_preview_id: "capo_accessanalyzer.types.access_preview_id.AccessPreviewId",
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        filter: Optional[
            "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
        ] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_accessanalyzer.types.list_access_preview_findings_response.ListAccessPreviewFindingsResponse":
        """<p>Retrieves a list of access preview findings generated by the specified access preview.</p>

        Args:
            access_preview_id: <p>The unique ID for the access preview.</p>
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the access.</p>
            filter: <p>Criteria to filter the returned findings.</p>
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_access_preview_findings_request.ListAccessPreviewFindingsRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_access_preview_findings_response.ListAccessPreviewFindingsResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_access_preview_findings

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_access_preview_findings.list_access_preview_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_access_preview_findings_request.ListAccessPreviewFindingsRequest = {
            "access_preview_id": access_preview_id,
            "analyzer_arn": analyzer_arn,
        }
        if filter is not None:
            input_["filter"] = filter
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

    def list_access_previews(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse":
        """<p>Retrieves a list of access previews for the specified analyzer.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the access preview.</p>
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_access_previews_request.ListAccessPreviewsRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_access_previews_response.ListAccessPreviewsResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_access_previews

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_access_previews.list_access_previews(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_access_previews_request.ListAccessPreviewsRequest = {
            "analyzer_arn": analyzer_arn
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

    def list_analyzed_resources(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        resource_type: Optional[
            "capo_accessanalyzer.types.resource_type.ResourceType"
        ] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_accessanalyzer.types.list_analyzed_resources_response.ListAnalyzedResourcesResponse":
        """<p>Retrieves a list of resources of the specified type that have been analyzed by the specified analyzer.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve a list of analyzed resources from.</p>
            resource_type: <p>The type of resource.</p>
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_analyzed_resources_request.ListAnalyzedResourcesRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_analyzed_resources_response.ListAnalyzedResourcesResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_analyzed_resources

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_analyzed_resources.list_analyzed_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_analyzed_resources_request.ListAnalyzedResourcesRequest = {
            "analyzer_arn": analyzer_arn
        }
        if resource_type is not None:
            input_["resource_type"] = resource_type
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

    def list_findings(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        filter: Optional[
            "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
        ] = None,
        sort: Optional["capo_accessanalyzer.types.sort_criteria.SortCriteria"] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_accessanalyzer.types.list_findings_response.ListFindingsResponse":
        """<p>Retrieves a list of findings generated by the specified analyzer. ListFindings and ListFindingsV2 both use <code>access-analyzer:ListFindings</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>access-analyzer:ListFindings</code> action.</p> <p>To learn about filter keys that you can use to retrieve a list of findings, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html">IAM Access Analyzer filter keys</a> in the <b>IAM User Guide</b>.</p> <note> <p>ListFindings is supported only for external access analyzers. You must use ListFindingsV2 for internal and unused access analyzers.</p> </note>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve findings from.</p>
            filter: <p>A filter to match for the findings to return.</p>
            sort: <p>The sort order for the findings returned.</p>
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_findings_request.ListFindingsRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_findings_response.ListFindingsResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_findings

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_findings.list_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_findings_request.ListFindingsRequest = {
            "analyzer_arn": analyzer_arn
        }
        if filter is not None:
            input_["filter"] = filter
        if sort is not None:
            input_["sort"] = sort
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

    def list_findings_v2(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        filter: Optional[
            "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        sort: Optional["capo_accessanalyzer.types.sort_criteria.SortCriteria"] = None,
    ) -> "capo_accessanalyzer.types.list_findings_v2_response.ListFindingsV2Response":
        """<p>Retrieves a list of findings generated by the specified analyzer. ListFindings and ListFindingsV2 both use <code>access-analyzer:ListFindings</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>access-analyzer:ListFindings</code> action.</p> <p>To learn about filter keys that you can use to retrieve a list of findings, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html">IAM Access Analyzer filter keys</a> in the <b>IAM User Guide</b>.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve findings from.</p>
            filter: <p>A filter to match for the findings to return.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token used for pagination of results returned.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_findings_v2_request.ListFindingsV2Request]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_findings_v2_response.ListFindingsV2Response"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_findings_v2

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_findings_v2.list_findings_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_findings_v2_request.ListFindingsV2Request = {
            "analyzer_arn": analyzer_arn
        }
        if filter is not None:
            input_["filter"] = filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_generations(
        self,
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        principal_arn: Optional[
            "capo_accessanalyzer.types.principal_arn.PrincipalArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
    ) -> "capo_accessanalyzer.types.list_policy_generations_response.ListPolicyGenerationsResponse":
        """<p>Lists all of the policy generations requested in the last seven days.</p>

        Args:
            principal_arn: <p>The ARN of the IAM entity (user or role) for which you are generating a policy. Use this with <code>ListGeneratedPolicies</code> to filter the results to only include results for a specific principal.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token used for pagination of results returned.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_policy_generations_request.ListPolicyGenerationsRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_policy_generations_response.ListPolicyGenerationsResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_policy_generations

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_policy_generations.list_policy_generations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_policy_generations_request.ListPolicyGenerationsRequest = {}
        if principal_arn is not None:
            input_["principal_arn"] = principal_arn
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

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags applied to the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to retrieve tags from.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_tags_for_resource

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_policy_generation(
        self,
        policy_generation_details: "capo_accessanalyzer.types.policy_generation_details.PolicyGenerationDetails",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        cloud_trail_details: Optional[
            "capo_accessanalyzer.types.cloud_trail_details.CloudTrailDetails"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_accessanalyzer.types.start_policy_generation_response.StartPolicyGenerationResponse":
        """<p>Starts the policy generation request.</p>

        Args:
            policy_generation_details: <p>Contains the ARN of the IAM entity (user or role) for which you are generating a policy.</p>
            cloud_trail_details: <p>A <code>CloudTrailDetails</code> object that contains details about a <code>Trail</code> that you want to analyze to generate policies.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quote met error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.start_policy_generation_request.StartPolicyGenerationRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.start_policy_generation_response.StartPolicyGenerationResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.start_policy_generation

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.start_policy_generation.start_policy_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.start_policy_generation_request.StartPolicyGenerationRequest = {
            "policy_generation_details": policy_generation_details
        }
        if cloud_trail_details is not None:
            input_["cloud_trail_details"] = cloud_trail_details
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

    def start_resource_scan(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        resource_arn: "capo_accessanalyzer.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        resource_owner_account: Optional[str] = None,
    ) -> None:
        """<p>Immediately starts a scan of the policies applied to the specified resource.</p> <note> <p>This action is supported only for external access analyzers.</p> </note>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to use to scan the policies applied to the specified resource.</p>
            resource_arn: <p>The ARN of the resource to scan.</p>
            resource_owner_account: <p>The Amazon Web Services account ID that owns the resource. For most Amazon Web Services resources, the owning account is the account in which the resource was created.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.start_resource_scan_request.StartResourceScanRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.start_resource_scan

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.start_resource_scan.start_resource_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.start_resource_scan_request.StartResourceScanRequest = {
            "analyzer_arn": analyzer_arn,
            "resource_arn": resource_arn,
        }
        if resource_owner_account is not None:
            input_["resource_owner_account"] = resource_owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_accessanalyzer.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to add the tag to.</p>
            tags: <p>The tags to add to the resource.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.tag_resource

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_accessanalyzer.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove the tag from.</p>
            tag_keys: <p>The key for the tag to add.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.untag_resource

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.untag_resource_request.UntagResourceRequest = {
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

    def update_findings(
        self,
        analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn",
        status: "capo_accessanalyzer.types.finding_status_update.FindingStatusUpdate",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        ids: Optional["capo_accessanalyzer.types.finding_id_list.FindingIdList"] = None,
        resource_arn: Optional[
            "capo_accessanalyzer.types.resource_arn.ResourceArn"
        ] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Updates the status for the specified findings.</p>

        Args:
            analyzer_arn: <p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> that generated the findings to update.</p>
            status: <p>The state represents the action to take to update the finding Status. Use <code>ARCHIVE</code> to change an Active finding to an Archived finding. Use <code>ACTIVE</code> to change an Archived finding to an Active finding.</p>
            ids: <p>The IDs of the findings to update.</p>
            resource_arn: <p>The ARN of the resource identified in the finding.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.update_findings_request.UpdateFindingsRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.update_findings

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.update_findings.update_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.update_findings_request.UpdateFindingsRequest = {
            "analyzer_arn": analyzer_arn,
            "status": status,
        }
        if ids is not None:
            input_["ids"] = ids
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
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

    def validate_policy(
        self,
        policy_document: "capo_accessanalyzer.types.policy_document.PolicyDocument",
        policy_type: "capo_accessanalyzer.types.policy_type.PolicyType",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        locale: Optional["capo_accessanalyzer.types.locale.Locale"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        validate_policy_resource_type: Optional[
            "capo_accessanalyzer.types.validate_policy_resource_type.ValidatePolicyResourceType"
        ] = None,
    ) -> "capo_accessanalyzer.types.validate_policy_response.ValidatePolicyResponse":
        """<p>Requests the validation of a policy and returns a list of findings. The findings help you identify issues and provide actionable recommendations to resolve the issue and enable you to author functional policies that meet security best practices. </p>

        Args:
            locale: <p>The locale to use for localizing the findings.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token used for pagination of results returned.</p>
            policy_document: <p>The JSON policy document to use as the content for the policy.</p>
            policy_type: <p>The type of policy to validate. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.</p> <p>Resource policies grant permissions on Amazon Web Services resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy. </p> <p>Service control policies (SCPs) are a type of organization policy attached to an Amazon Web Services organization, organizational unit (OU), or an account.</p>
            validate_policy_resource_type: <p>The type of resource to attach to your resource policy. Specify a value for the policy validation resource type only if the policy type is <code>RESOURCE_POLICY</code>. For example, to validate a resource policy to attach to an Amazon S3 bucket, you can choose <code>AWS::S3::Bucket</code> for the policy validation resource type.</p> <p>For resource types not supported as valid values, IAM Access Analyzer runs policy checks that apply to all resource policies. For example, to validate a resource policy to attach to a KMS key, do not specify a value for the policy validation resource type and IAM Access Analyzer will run policy checks that apply to all resource policies.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.validate_policy_request.ValidatePolicyRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.validate_policy_response.ValidatePolicyResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.validate_policy

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.validate_policy.validate_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.validate_policy_request.ValidatePolicyRequest = {
            "policy_document": policy_document,
            "policy_type": policy_type,
        }
        if locale is not None:
            input_["locale"] = locale
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if validate_policy_resource_type is not None:
            input_["validate_policy_resource_type"] = validate_policy_resource_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_analyzer(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        type: "capo_accessanalyzer.types.type.Type",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        archive_rules: Optional[
            "capo_accessanalyzer.types.inline_archive_rules_list.InlineArchiveRulesList"
        ] = None,
        tags: Optional["capo_accessanalyzer.types.tags_map.TagsMap"] = None,
        client_token: Optional[str] = None,
        configuration: Optional[
            "capo_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
        ] = None,
    ) -> "capo_accessanalyzer.types.create_analyzer_response.CreateAnalyzerResponse":
        """<p>Creates an analyzer for your account.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to create.</p>
            type: <p>The type of analyzer to create. You can create only one analyzer per account per Region. You can create up to 5 analyzers per organization per Region.</p>
            archive_rules: <p>Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.</p>
            tags: <p>An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, <code>_</code>, <code>.</code>, <code>/</code>, <code>=</code>, <code>+</code>, and <code>-</code>.</p> <p>For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with <code>aws:</code>.</p> <p>For the tag value, you can specify a value that is 0 to 256 characters in length.</p>
            client_token: <p>A client token.</p>
            configuration: <p>Specifies the configuration of the analyzer. If the analyzer is an unused access analyzer, the specified scope of unused access is used for the configuration. If the analyzer is an internal access analyzer, the specified internal access analysis rules are used for the configuration.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quote met error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.create_analyzer_request.CreateAnalyzerRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.create_analyzer_response.CreateAnalyzerResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.create_analyzer

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.create_analyzer.create_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.create_analyzer_request.CreateAnalyzerRequest = {
            "analyzer_name": analyzer_name,
            "type": type,
        }
        if archive_rules is not None:
            input_["archive_rules"] = archive_rules
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_analyzer(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.get_analyzer_response.GetAnalyzerResponse":
        """<p>Retrieves information about the specified analyzer.</p>

        Args:
            analyzer_name: <p>The name of the analyzer retrieved.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_analyzer_request.GetAnalyzerRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_analyzer_response.GetAnalyzerResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_analyzer

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_analyzer.get_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_analyzer_request.GetAnalyzerRequest = {
            "analyzer_name": analyzer_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_analyzer(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        configuration: Optional[
            "capo_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
        ] = None,
    ) -> "capo_accessanalyzer.types.update_analyzer_response.UpdateAnalyzerResponse":
        """<p>Modifies the configuration of an existing analyzer.</p> <note> <p>This action is not supported for external access analyzers.</p> </note>

        Args:
            analyzer_name: <p>The name of the analyzer to modify.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.update_analyzer_request.UpdateAnalyzerRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.update_analyzer_response.UpdateAnalyzerResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.update_analyzer

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.update_analyzer.update_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.update_analyzer_request.UpdateAnalyzerRequest = {
            "analyzer_name": analyzer_name
        }
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_analyzer(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Deletes the specified analyzer. When you delete an analyzer, IAM Access Analyzer is disabled for the account or organization in the current or specific Region. All findings that were generated by the analyzer are deleted. You cannot undo this action.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to delete.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.delete_analyzer_request.DeleteAnalyzerRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.delete_analyzer

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.delete_analyzer.delete_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.delete_analyzer_request.DeleteAnalyzerRequest = {
            "analyzer_name": analyzer_name
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

    def list_analyzers(
        self,
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
        type: Optional["capo_accessanalyzer.types.type.Type"] = None,
    ) -> "capo_accessanalyzer.types.list_analyzers_response.ListAnalyzersResponse":
        """<p>Retrieves a list of analyzers.</p>

        Args:
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            type: <p>The type of analyzer.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_analyzers_request.ListAnalyzersRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_analyzers_response.ListAnalyzersResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_analyzers

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_analyzers.list_analyzers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_analyzers_request.ListAnalyzersRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_linked_analyzer(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Deletes a service-linked analyzer. This operation can be invoked by both authorized Amazon Web Services services and customers.</p> <p>When invoked by a customer, IAM Access Analyzer performs a callback to the managing service to verify whether the analyzer is still in use and can be deleted. If the service indicates the analyzer is still in use, the deletion is rejected with <code>ConflictException</code>.</p>

        Args:
            analyzer_name: <p>The name of the service-linked analyzer to delete. Service-linked analyzer names follow the format <code>_AccessAnalyzerFor{ServiceName}-{Id}</code>.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.delete_service_linked_analyzer_request.DeleteServiceLinkedAnalyzerRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.delete_service_linked_analyzer

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.delete_service_linked_analyzer.delete_service_linked_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.delete_service_linked_analyzer_request.DeleteServiceLinkedAnalyzerRequest = {
            "analyzer_name": analyzer_name
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

    def create_archive_rule(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        rule_name: "capo_accessanalyzer.types.name.Name",
        filter: "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Creates an archive rule for the specified analyzer. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.</p> <p>To learn about filter keys that you can use to create an archive rule, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html">IAM Access Analyzer filter keys</a> in the <b>IAM User Guide</b>.</p>

        Args:
            analyzer_name: <p>The name of the created analyzer.</p>
            rule_name: <p>The name of the rule to create.</p>
            filter: <p>The criteria for the rule.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.conflict_exception.ConflictException: <p>A conflict exception error.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quote met error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.create_archive_rule_request.CreateArchiveRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.create_archive_rule

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.create_archive_rule.create_archive_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.create_archive_rule_request.CreateArchiveRuleRequest = {
            "analyzer_name": analyzer_name,
            "rule_name": rule_name,
            "filter": filter,
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

    def get_archive_rule(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        rule_name: "capo_accessanalyzer.types.name.Name",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "capo_accessanalyzer.types.get_archive_rule_response.GetArchiveRuleResponse":
        """<p>Retrieves information about an archive rule.</p> <p>To learn about filter keys that you can use to create an archive rule, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html">IAM Access Analyzer filter keys</a> in the <b>IAM User Guide</b>.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to retrieve rules from.</p>
            rule_name: <p>The name of the rule to retrieve.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.get_archive_rule_request.GetArchiveRuleRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.get_archive_rule_response.GetArchiveRuleResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.get_archive_rule

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.get_archive_rule.get_archive_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.get_archive_rule_request.GetArchiveRuleRequest = {
            "analyzer_name": analyzer_name,
            "rule_name": rule_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_archive_rule(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        rule_name: "capo_accessanalyzer.types.name.Name",
        filter: "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Updates the criteria and values for the specified archive rule.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to update the archive rules for.</p>
            rule_name: <p>The name of the rule to update.</p>
            filter: <p>A filter to match for the rules to update. Only rules that match the filter are updated.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.update_archive_rule_request.UpdateArchiveRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.update_archive_rule

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.update_archive_rule.update_archive_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.update_archive_rule_request.UpdateArchiveRuleRequest = {
            "analyzer_name": analyzer_name,
            "rule_name": rule_name,
            "filter": filter,
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

    def delete_archive_rule(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        rule_name: "capo_accessanalyzer.types.name.Name",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Deletes the specified archive rule.</p>

        Args:
            analyzer_name: <p>The name of the analyzer that associated with the archive rule to delete.</p>
            rule_name: <p>The name of the rule to delete.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.delete_archive_rule_request.DeleteArchiveRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_accessanalyzer._operations.access_analyzer.delete_archive_rule

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.delete_archive_rule.delete_archive_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.delete_archive_rule_request.DeleteArchiveRuleRequest = {
            "analyzer_name": analyzer_name,
            "rule_name": rule_name,
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

    def list_archive_rules(
        self,
        analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        next_token: Optional["capo_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_accessanalyzer.types.list_archive_rules_response.ListArchiveRulesResponse"
    ):
        """<p>Retrieves a list of archive rules created for the specified analyzer.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to retrieve rules from.</p>
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the request.</p>

        Raises:
            capo_accessanalyzer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_accessanalyzer.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_accessanalyzer.errors.throttling_exception.ThrottlingException: <p>Throttling limit exceeded error.</p>
            capo_accessanalyzer.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_accessanalyzer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_accessanalyzer.types.list_archive_rules_request.ListArchiveRulesRequest]",
        ) -> OperationResponse[
            "capo_accessanalyzer.types.list_archive_rules_response.ListArchiveRulesResponse"
        ]:
            import capo_accessanalyzer._operations.access_analyzer.list_archive_rules

            output, http_response = (
                capo_accessanalyzer._operations.access_analyzer.list_archive_rules.list_archive_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_accessanalyzer.types.list_archive_rules_request.ListArchiveRulesRequest = {
            "analyzer_name": analyzer_name
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

"""Generated from Smithy shape ``com.amazonaws.continuum#ContinuumControlPlane``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_continuum._auth._signers
import capo_continuum._auth._sigv4
from capo_continuum._auth._identity import Credentials
from capo_continuum._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_continuum._auth._zapros_handler import AuthMiddleware
from capo_continuum._pagination import resolve_path as _resolve_path
from capo_continuum._resources.continuum_control_plane.collector import Collector
from capo_continuum._resources.continuum_control_plane.environment import Environment
from capo_continuum._resources.continuum_control_plane.integration import Integration
from capo_continuum._services._aws_config import aws_config
from capo_continuum._services._pipeline import (
    Interceptor,
    OperationLogging,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    ThreadSafeRetryQuota,
    execute_pipeline,
    log_operation,
    retry,
)

if TYPE_CHECKING:
    import capo_continuum.types.associate_collector_input
    import capo_continuum.types.associate_collector_output
    import capo_continuum.types.associated_collector
    import capo_continuum.types.associated_environment
    import capo_continuum.types.association_client_token
    import capo_continuum.types.aws_account_id
    import capo_continuum.types.code_scan_summary
    import capo_continuum.types.collector_arn
    import capo_continuum.types.collector_client_token
    import capo_continuum.types.collector_id
    import capo_continuum.types.collector_name
    import capo_continuum.types.collector_type
    import capo_continuum.types.create_code_finding_input
    import capo_continuum.types.create_code_finding_output
    import capo_continuum.types.create_code_scan_input
    import capo_continuum.types.create_code_scan_output
    import capo_continuum.types.create_collector_input
    import capo_continuum.types.create_collector_output
    import capo_continuum.types.create_environment_configuration
    import capo_continuum.types.create_environment_input
    import capo_continuum.types.create_environment_output
    import capo_continuum.types.create_integration_input
    import capo_continuum.types.create_integration_output
    import capo_continuum.types.delete_collector_input
    import capo_continuum.types.delete_environment_input
    import capo_continuum.types.delete_integration_input
    import capo_continuum.types.disassociate_collector_input
    import capo_continuum.types.environment_arn
    import capo_continuum.types.environment_id
    import capo_continuum.types.environment_list_entry
    import capo_continuum.types.environment_name
    import capo_continuum.types.environment_source_role_arn
    import capo_continuum.types.finding_client_token
    import capo_continuum.types.finding_id
    import capo_continuum.types.finding_summary
    import capo_continuum.types.get_code_finding_input
    import capo_continuum.types.get_code_finding_output
    import capo_continuum.types.get_code_issue_artifact_input
    import capo_continuum.types.get_code_issue_artifact_output
    import capo_continuum.types.get_code_issue_input
    import capo_continuum.types.get_code_issue_output
    import capo_continuum.types.get_code_scan_input
    import capo_continuum.types.get_code_scan_output
    import capo_continuum.types.get_collector_data_access_authorization_input
    import capo_continuum.types.get_collector_data_access_authorization_output
    import capo_continuum.types.get_collector_input
    import capo_continuum.types.get_collector_output
    import capo_continuum.types.get_environment_input
    import capo_continuum.types.get_environment_output
    import capo_continuum.types.get_integration_input
    import capo_continuum.types.get_integration_output
    import capo_continuum.types.get_resource_policy_input
    import capo_continuum.types.get_resource_policy_output
    import capo_continuum.types.integration_authorization_provider_type
    import capo_continuum.types.integration_client_token
    import capo_continuum.types.integration_id
    import capo_continuum.types.integration_name
    import capo_continuum.types.integration_summary
    import capo_continuum.types.issue_artifact_id
    import capo_continuum.types.issue_artifact_item
    import capo_continuum.types.issue_artifact_type
    import capo_continuum.types.issue_id
    import capo_continuum.types.issue_summary
    import capo_continuum.types.kubernetes_cluster_role_configuration
    import capo_continuum.types.kubernetes_cluster_role_update
    import capo_continuum.types.list_associated_collectors_input
    import capo_continuum.types.list_associated_collectors_output
    import capo_continuum.types.list_associated_environments_input
    import capo_continuum.types.list_associated_environments_output
    import capo_continuum.types.list_code_findings_input
    import capo_continuum.types.list_code_findings_output
    import capo_continuum.types.list_code_issue_artifacts_input
    import capo_continuum.types.list_code_issue_artifacts_output
    import capo_continuum.types.list_code_issues_input
    import capo_continuum.types.list_code_issues_output
    import capo_continuum.types.list_code_scans_input
    import capo_continuum.types.list_code_scans_output
    import capo_continuum.types.list_collectors_input
    import capo_continuum.types.list_collectors_output
    import capo_continuum.types.list_environments_input
    import capo_continuum.types.list_environments_output
    import capo_continuum.types.list_integrations_input
    import capo_continuum.types.list_integrations_output
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token
    import capo_continuum.types.provider_configuration
    import capo_continuum.types.put_resource_policy_input
    import capo_continuum.types.put_resource_policy_output
    import capo_continuum.types.resource_policy_input_document
    import capo_continuum.types.resource_policy_revision_id
    import capo_continuum.types.resource_policy_target_arn
    import capo_continuum.types.scan_client_token
    import capo_continuum.types.scan_run_id
    import capo_continuum.types.start_integration_authorization_input
    import capo_continuum.types.start_integration_authorization_output
    import capo_continuum.types.update_collector_input
    import capo_continuum.types.update_collector_output
    import capo_continuum.types.update_environment_configuration
    import capo_continuum.types.update_environment_input
    import capo_continuum.types.update_environment_output
    import capo_continuum.types.update_integration_input
    import capo_continuum.types.update_integration_output
    import capo_continuum.types.update_provider_configuration


class ContinuumClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ContinuumClient:
    """A client for the ``Continuum`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = ContinuumClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.collector = Collector(self)
        self.environment = Environment(self)
        self.integration = Integration(self)

    def operation_options(
        self,
        config_overrides: Optional[ContinuumClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ContinuumClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(log_operation(operation_logging))
        interceptors_.append(retry())
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
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

    def get_resource_policy(
        self,
        arn: "capo_continuum.types.resource_policy_target_arn.ResourcePolicyTargetArn",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_resource_policy_output.GetResourcePolicyOutput":
        """Retrieves the resource policy attached to a Continuum resource.

        Args:
            arn: The ARN of a resource in the caller's account.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_resource_policy

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_continuum.types.get_resource_policy_output.GetResourcePolicyOutput",
        ) -> dict[str, Any]:
            import capo_continuum.types.get_resource_policy_output

            return capo_continuum.types.get_resource_policy_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetResourcePolicy", redact_output=_redact_output),
        )
        input_: capo_continuum.types.get_resource_policy_input.GetResourcePolicyInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        arn: "capo_continuum.types.resource_policy_target_arn.ResourcePolicyTargetArn",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        policy: Optional[
            "capo_continuum.types.resource_policy_input_document.ResourcePolicyInputDocument"
        ] = None,
        expected_revision_id: Optional[
            "capo_continuum.types.resource_policy_revision_id.ResourcePolicyRevisionId"
        ] = None,
    ) -> "capo_continuum.types.put_resource_policy_output.PutResourcePolicyOutput":
        """Creates or replaces the resource policy attached to a Continuum resource.

        Args:
            arn: The ARN of a resource in the caller's account.
            policy: Omit or supply an empty Statement array to clear resource-policy grants and store the canonical empty-statement policy. Cross-account access is denied; same-account access remains subject to identity policies. Use an explicit Deny statement to deny same-account principals too.
            expected_revision_id: Optional optimistic-concurrency token for the currently observed policy.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.put_resource_policy_input.PutResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_continuum.types.put_resource_policy_output.PutResourcePolicyOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.put_resource_policy

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.put_resource_policy_input.PutResourcePolicyInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.put_resource_policy_input

            return capo_continuum.types.put_resource_policy_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_continuum.types.put_resource_policy_output.PutResourcePolicyOutput",
        ) -> dict[str, Any]:
            import capo_continuum.types.put_resource_policy_output

            return capo_continuum.types.put_resource_policy_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "PutResourcePolicy",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_continuum.types.put_resource_policy_input.PutResourcePolicyInput = {
            "arn": arn
        }
        if policy is not None:
            input_["policy"] = policy
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_integration_authorization(
        self,
        provider_type: "capo_continuum.types.integration_authorization_provider_type.IntegrationAuthorizationProviderType",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        name: Optional["capo_continuum.types.integration_name.IntegrationName"] = None,
    ) -> "capo_continuum.types.start_integration_authorization_output.StartIntegrationAuthorizationOutput":
        """Starts an OAuth authorization for a new integration and returns the values the caller sends to the provider's authorization endpoint. The authorization belongs to the calling AWS account, can be redeemed once by CreateIntegration from that same account, and expires after ten minutes.

        Args:
            provider_type: The provider to authorize. Only GITHUB is supported.
            name: The name the integration will be created with. When specified, the request fails with ConflictException if an integration with this name already exists in the account, before the caller leaves for the provider. The name is only checked: it is not reserved, stored, or authorized. CreateIntegration requires its own name, checks it again, and may use a different one.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.start_integration_authorization_input.StartIntegrationAuthorizationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.start_integration_authorization_output.StartIntegrationAuthorizationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.start_integration_authorization

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.start_integration_authorization.start_integration_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_continuum.types.start_integration_authorization_output.StartIntegrationAuthorizationOutput",
        ) -> dict[str, Any]:
            import capo_continuum.types.start_integration_authorization_output

            return capo_continuum.types.start_integration_authorization_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "StartIntegrationAuthorization", redact_output=_redact_output
            ),
        )
        input_: capo_continuum.types.start_integration_authorization_input.StartIntegrationAuthorizationInput = {
            "provider_type": provider_type
        }
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_collector(
        self,
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        type: Optional["capo_continuum.types.collector_type.CollectorType"] = None,
        kubernetes_cluster_role: Optional[
            "capo_continuum.types.kubernetes_cluster_role_configuration.KubernetesClusterRoleConfiguration"
        ] = None,
        client_token: Optional[
            "capo_continuum.types.collector_client_token.CollectorClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_collector_output.CreateCollectorOutput":
        """Creates the Collector for the caller's account. Provisions an AWS Config service-linked recorder using the caller's federated access session and begins recording infrastructure changes.

        Args:
            type: Source to collect. Defaults to AWS_COLLECTOR when omitted.
            kubernetes_cluster_role: IAM role configuration used to collect Kubernetes cluster metadata. The authenticated caller must be allowed to pass its exact roleArn to Continuum.
            client_token: Caller-provided token that makes retried create requests return the original Collector rather than creating a duplicate.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_collector_input.CreateCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_collector_output.CreateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_collector.create_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.create_collector_input.CreateCollectorInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.create_collector_input

            return capo_continuum.types.create_collector_input.redact_sensitive(input_)

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateCollector", redact_input=_redact_input),
        )
        input_: capo_continuum.types.create_collector_input.CreateCollectorInput = {}
        if type is not None:
            input_["type"] = type
        if kubernetes_cluster_role is not None:
            input_["kubernetes_cluster_role"] = kubernetes_cluster_role
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

    def get_collector(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_collector_output.GetCollectorOutput":
        """Retrieves the current state of the Collector for the caller's account.

        Args:
            collector_id: The unique identifier of the Collector to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_collector_input.GetCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_collector_output.GetCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_collector.get_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCollector")
        )
        input_: capo_continuum.types.get_collector_input.GetCollectorInput = {
            "collector_id": collector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_collector(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        name: Optional["capo_continuum.types.collector_name.CollectorName"] = None,
        kubernetes_cluster_role: Optional[
            "capo_continuum.types.kubernetes_cluster_role_update.KubernetesClusterRoleUpdate"
        ] = None,
    ) -> "capo_continuum.types.update_collector_output.UpdateCollectorOutput":
        """Updates the customer-controlled mutable properties of a Collector. Only the name and Kubernetes cluster IAM role can be changed.

        Args:
            collector_id: The unique identifier of the Collector to update.
            name: The new customer-visible name.
            kubernetes_cluster_role: Atomic update to the IAM role configuration used to collect Kubernetes cluster metadata. The set variant requires a complete configuration; the authenticated caller must be allowed to pass its exact roleArn to Continuum. The remove variant clears both the role and external ID.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.update_collector_input.UpdateCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.update_collector_output.UpdateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.update_collector.update_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.update_collector_input.UpdateCollectorInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.update_collector_input

            return capo_continuum.types.update_collector_input.redact_sensitive(input_)

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("UpdateCollector", redact_input=_redact_input),
        )
        input_: capo_continuum.types.update_collector_input.UpdateCollectorInput = {
            "collector_id": collector_id
        }
        if name is not None:
            input_["name"] = name
        if kubernetes_cluster_role is not None:
            input_["kubernetes_cluster_role"] = kubernetes_cluster_role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_collector(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Deletes the Collector for the caller's account. The Collector first enters PENDING_DELETION, then the service removes its schedule, AWS Config service-linked recorder, versioned S3 bucket, KMS key, and persisted record.

        Args:
            collector_id: The unique identifier of the Collector to delete.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.delete_collector_input.DeleteCollectorInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.delete_collector.delete_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteCollector")
        )
        input_: capo_continuum.types.delete_collector_input.DeleteCollectorInput = {
            "collector_id": collector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_collectors(
        self, *, config_overrides: Optional[ContinuumClientConfig] = None
    ) -> "capo_continuum.types.list_collectors_output.ListCollectorsOutput":
        """Lists the Collectors owned by the authenticated caller's account, including a Collector whose deletion is in progress. A Collector that is still being created is omitted. The account-scoped Collector quota currently permits at most one result, so no result ordering applies.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_collectors_input.ListCollectorsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_collectors_output.ListCollectorsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_collectors

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_collectors.list_collectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListCollectors")
        )
        input_: capo_continuum.types.list_collectors_input.ListCollectorsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_collector_data_access_authorization(
        self,
        account_id: "capo_continuum.types.aws_account_id.AwsAccountId",
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        environment_arn: Optional[
            "capo_continuum.types.environment_arn.EnvironmentArn"
        ] = None,
    ) -> "capo_continuum.types.get_collector_data_access_authorization_output.GetCollectorDataAccessAuthorizationOutput":
        """Authorizes an Environment's access to a Collector's data. Continuum calls this operation with the Environment's Collector data-access role before it reads the Collector's inventory, so grant continuum:GetCollectorDataAccessAuthorization to that role and, for a Collector in another account, in the Collector's resource policy. The operation evaluates the action against the exact Collector ARN and the Collector's current resource policy using IAM and the caller's authenticated request context, with environmentArn as the continuum:EnvironmentArn condition key. A successful request returns HTTP 200 with no response members. If access is not granted, the operation returns AccessDeniedException without disclosing Collector existence, ownership, or the policy layer that denied access. The service does not reinterpret the policy using only an account ID.

        Args:
            account_id: The AWS account that owns the Collector.
            collector_id: The unique identifier of the Collector.
            environment_arn: The full ARN of the Environment requesting the Collector's data. The Environment must be in the caller's account. Continuum supplies this value as the continuum:EnvironmentArn condition key.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_collector_data_access_authorization_input.GetCollectorDataAccessAuthorizationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_collector_data_access_authorization_output.GetCollectorDataAccessAuthorizationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_collector_data_access_authorization

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_collector_data_access_authorization.get_collector_data_access_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCollectorDataAccessAuthorization")
        )
        input_: capo_continuum.types.get_collector_data_access_authorization_input.GetCollectorDataAccessAuthorizationInput = {
            "account_id": account_id,
            "collector_id": collector_id,
        }
        if environment_arn is not None:
            input_["environment_arn"] = environment_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_associated_environments(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_associated_environments_output.ListAssociatedEnvironmentsOutput":
        """Lists the Environments currently associated with one Collector in lexicographically ascending environmentArn order. The ARN identifies each Environment across accounts within the Collector's Region.

        Args:
            collector_id: The unique identifier of the Collector whose associations to list.
            max_results: Maximum number of Environment associations to return.
            next_token: Pagination token returned by a prior request.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_associated_environments_input.ListAssociatedEnvironmentsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_associated_environments_output.ListAssociatedEnvironmentsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_associated_environments

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_associated_environments.list_associated_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListAssociatedEnvironments")
        )
        input_: capo_continuum.types.list_associated_environments_input.ListAssociatedEnvironmentsInput = {
            "collector_id": collector_id
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

    def iter_list_associated_environments(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.associated_environment.AssociatedEnvironment]":
        _token = next_token
        while True:
            _response = self.list_associated_environments(
                collector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associated_environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_environment(
        self,
        name: "capo_continuum.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        configuration: Optional[
            "capo_continuum.types.create_environment_configuration.CreateEnvironmentConfiguration"
        ] = None,
    ) -> "capo_continuum.types.create_environment_output.CreateEnvironmentOutput":
        """Creates an environment and starts its validation and any requested provisioning. Storage provisioning and dependency checks may continue after the initial 201 response; use GetEnvironment to observe completion.

        Args:
            name: The customer-visible name of the environment.
            configuration: Type-specific configuration. Omission creates a code environment with the default operating policy and no sources.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_environment_input.CreateEnvironmentInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateEnvironment")
        )
        input_: capo_continuum.types.create_environment_input.CreateEnvironmentInput = {
            "name": name
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

    def get_environment(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_environment_output.GetEnvironmentOutput":
        """Retrieves the current state and configuration of an environment.

        Args:
            environment_id: The unique identifier of the environment to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_environment_input.GetEnvironmentInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetEnvironment")
        )
        input_: capo_continuum.types.get_environment_input.GetEnvironmentInput = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_environment(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        name: Optional["capo_continuum.types.environment_name.EnvironmentName"] = None,
        configuration: Optional[
            "capo_continuum.types.update_environment_configuration.UpdateEnvironmentConfiguration"
        ] = None,
    ) -> "capo_continuum.types.update_environment_output.UpdateEnvironmentOutput":
        """Updates the customer-controlled mutable properties of an environment. Only the name, the environment's S3 integration source and repository selections, its scan frequency, its network policy, and its patch creation policy can be changed.

        Args:
            environment_id: The unique identifier of the environment to update.
            name: The new customer-visible name.
            configuration: Type-specific configuration changes. Omission preserves the configuration.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> OperationResponse[
            "capo_continuum.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateEnvironment")
        )
        input_: capo_continuum.types.update_environment_input.UpdateEnvironmentInput = {
            "environment_id": environment_id
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Deletes an environment and its associated resources.

        Args:
            environment_id: The unique identifier of the environment to delete.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteEnvironment")
        )
        input_: capo_continuum.types.delete_environment_input.DeleteEnvironmentInput = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_environments(
        self,
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_environments_output.ListEnvironmentsOutput":
        """Lists all environments in your account in descending environmentId order. This complete-inventory operation intentionally has no response filters; see the input documentation for the API standards justification.

        Args:
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_environments_input.ListEnvironmentsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_environments

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListEnvironments")
        )
        input_: capo_continuum.types.list_environments_input.ListEnvironmentsInput = {}
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

    def iter_list_environments(
        self,
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.environment_list_entry.EnvironmentListEntry]":
        _token = next_token
        while True:
            _response = self.list_environments(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_collector(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        collector_arn: "capo_continuum.types.collector_arn.CollectorArn",
        collector_data_access_role_arn: "capo_continuum.types.environment_source_role_arn.EnvironmentSourceRoleArn",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.association_client_token.AssociationClientToken"
        ] = None,
    ) -> "capo_continuum.types.associate_collector_output.AssociateCollectorOutput":
        """Associates one Collector with this Environment and configures the customer role Continuum uses to authorize access to associated Collector data. The caller must have permission on the Environment and permission to pass the role. Continuum assumes the supplied role and calls GetCollectorDataAccessAuthorization on the requested Collector; only a successful authorization response permits the association. The caller does not need Collector data-access permission. The Environment retains its other Collector associations. Calling again with an existing association is safe and does not create a duplicate.

        Args:
            environment_id: The unique identifier of the Environment making the association.
            client_token: Caller-provided token that makes retried association requests idempotent. The first successful request binds the token to the complete Collector ARN, supplied role, and result for at least 24 hours. During that retry window, reusing it with a different request fails with ConflictException. A matching replay still requires the supplied role to have current Collector access. Once authorized, a matching replay returns the stored result without changing association state. Revocation can deny a replay; it does not remove the stored association or its original result.
            collector_arn: The ARN of the Collector to associate with this Environment.
            collector_data_access_role_arn: IAM role in the Environment account that Continuum assumes before authorizing access to associated Collector inventory. Every association, including a same-account association, requires this role. The supplied ARN replaces the Environment's previously stored role. The customer is responsible for granting the role access to every Collector that should contribute data.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.associate_collector_input.AssociateCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.associate_collector_output.AssociateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.associate_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.associate_collector.associate_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("AssociateCollector")
        )
        input_: capo_continuum.types.associate_collector_input.AssociateCollectorInput = {
            "environment_id": environment_id,
            "collector_arn": collector_arn,
            "collector_data_access_role_arn": collector_data_access_role_arn,
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

    def disassociate_collector(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        collector_arn: "capo_continuum.types.collector_arn.CollectorArn",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Removes one Collector association from this Environment, preserving its other associations. The stored Collector data-access role is cleared when no Collector associations remain. The Environment owner must have permission to disassociate. A current Collector access grant is not required, and the Collector does not need to remain active or present, so stale or revoked associations can be cleaned up.

        Args:
            environment_id: The unique identifier of the Environment whose associations are updated.
            collector_arn: The ARN of the Collector to disassociate from this Environment.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.disassociate_collector_input.DisassociateCollectorInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.disassociate_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.disassociate_collector.disassociate_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DisassociateCollector")
        )
        input_: capo_continuum.types.disassociate_collector_input.DisassociateCollectorInput = {
            "environment_id": environment_id,
            "collector_arn": collector_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_associated_collectors(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_associated_collectors_output.ListAssociatedCollectorsOutput":
        """Lists the Collectors currently associated with one Environment in ascending collectorId order. Each entry carries the Collector ARN, so a listed association can be passed straight to DisassociateCollector, including when the Collector belongs to another account. An association recorded before Continuum persisted the ARN is omitted from the response, because without the ARN it cannot be acted on.

        Args:
            environment_id: The unique identifier of the Environment whose associations to list.
            max_results: Maximum number of associated Collectors to return.
            next_token: Pagination token returned by a prior request.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_associated_collectors_input.ListAssociatedCollectorsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_associated_collectors_output.ListAssociatedCollectorsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_associated_collectors

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_associated_collectors.list_associated_collectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListAssociatedCollectors")
        )
        input_: capo_continuum.types.list_associated_collectors_input.ListAssociatedCollectorsInput = {
            "environment_id": environment_id
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

    def iter_list_associated_collectors(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.associated_collector.AssociatedCollector]":
        _token = next_token
        while True:
            _response = self.list_associated_collectors(
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associated_collectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_code_finding(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        ocsf_document: object,
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.finding_client_token.FindingClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_code_finding_output.CreateCodeFindingOutput":
        """Ingests a customer-supplied security finding into an environment. Continuum validates the document synchronously against the required overlay fields for the declared format; invalid documents are rejected with a ValidationException. The maximum accepted document size is 256 KB. The environment must have a source configured, and the finding must identify a code location so Continuum can tie it to a repository in the environment's build. Continuum assigns a findingId and stores the verbatim document. When no successful build yet contains the finding's repository, the finding stays SUBMITTED until the next successful build; if that build does not contain it either, the finding is DISCARDED with discardReason SOURCE_REPO_NOT_FOUND.

        Args:
            environment_id: The environment to ingest the finding into.
            ocsf_document: The OCSF finding document to ingest, verbatim. Must declare a class_uid Continuum supports (2002 Vulnerability Finding, or 2007 Application Security Posture Finding) and validate against the vendored OCSF JSON Schema for that class, including the Continuum overlay requirements that finding_info.uid be present and that vulnerabilities[0].affected_code[0].file identify the code location. With several repositories in the environment, the file path must begin with the repository name. Maximum size 256 KB. Stored verbatim and normalized into the typed Finding members returned by GetCodeFinding. GetCodeFinding does not return the document itself.
            client_token: Caller-provided idempotency token. A retry with the same token and an identical finding document replays the original result; the same token with different content is rejected.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_code_finding_input.CreateCodeFindingInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_code_finding_output.CreateCodeFindingOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_code_finding

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_code_finding.create_code_finding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateCodeFinding")
        )
        input_: capo_continuum.types.create_code_finding_input.CreateCodeFindingInput = {
            "environment_id": environment_id,
            "ocsf_document": ocsf_document,
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

    def get_code_finding(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        finding_id: "capo_continuum.types.finding_id.FindingId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_code_finding_output.GetCodeFindingOutput":
        """Retrieves the current state and details of a finding.

        Args:
            environment_id: The environment that owns the finding.
            finding_id: The unique identifier of the finding to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_code_finding_input.GetCodeFindingInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_code_finding_output.GetCodeFindingOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_code_finding

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_code_finding.get_code_finding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCodeFinding")
        )
        input_: capo_continuum.types.get_code_finding_input.GetCodeFindingInput = {
            "environment_id": environment_id,
            "finding_id": finding_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_code_findings(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_code_findings_output.ListCodeFindingsOutput":
        """Lists the findings in an environment in descending findingId order.

        Args:
            environment_id: The environment whose findings to list.
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_code_findings_input.ListCodeFindingsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_code_findings_output.ListCodeFindingsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_code_findings

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_code_findings.list_code_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListCodeFindings")
        )
        input_: capo_continuum.types.list_code_findings_input.ListCodeFindingsInput = {
            "environment_id": environment_id
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

    def iter_list_code_findings(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.finding_summary.FindingSummary]":
        _token = next_token
        while True:
            _response = self.list_code_findings(
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_code_issue(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        issue_id: "capo_continuum.types.issue_id.IssueId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_code_issue_output.GetCodeIssueOutput":
        """Retrieves the current state and details of an issue.

        Args:
            environment_id: The environment that owns the issue.
            issue_id: The unique identifier of the issue to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_code_issue_input.GetCodeIssueInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_code_issue_output.GetCodeIssueOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_code_issue

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_code_issue.get_code_issue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCodeIssue")
        )
        input_: capo_continuum.types.get_code_issue_input.GetCodeIssueInput = {
            "environment_id": environment_id,
            "issue_id": issue_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_code_issues(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_code_issues_output.ListCodeIssuesOutput":
        """Lists the issues in an environment in descending issueId order.

        Args:
            environment_id: The environment whose issues to list.
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_code_issues_input.ListCodeIssuesInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_code_issues_output.ListCodeIssuesOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_code_issues

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_code_issues.list_code_issues(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListCodeIssues")
        )
        input_: capo_continuum.types.list_code_issues_input.ListCodeIssuesInput = {
            "environment_id": environment_id
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

    def iter_list_code_issues(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.issue_summary.IssueSummary]":
        _token = next_token
        while True:
            _response = self.list_code_issues(
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_code_issue_artifact(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        issue_id: "capo_continuum.types.issue_id.IssueId",
        artifact_id: "capo_continuum.types.issue_artifact_id.IssueArtifactId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> (
        "capo_continuum.types.get_code_issue_artifact_output.GetCodeIssueArtifactOutput"
    ):
        """Retrieves one immutable artifact attached to an issue, including its content.

        Args:
            environment_id: The environment that owns the issue.
            issue_id: The issue the artifact is attached to.
            artifact_id: The unique identifier of the artifact to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_code_issue_artifact_input.GetCodeIssueArtifactInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_code_issue_artifact_output.GetCodeIssueArtifactOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_code_issue_artifact

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_code_issue_artifact.get_code_issue_artifact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCodeIssueArtifact")
        )
        input_: capo_continuum.types.get_code_issue_artifact_input.GetCodeIssueArtifactInput = {
            "environment_id": environment_id,
            "issue_id": issue_id,
            "artifact_id": artifact_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_code_issue_artifacts(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        issue_id: "capo_continuum.types.issue_id.IssueId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        artifact_type: Optional[
            "capo_continuum.types.issue_artifact_type.IssueArtifactType"
        ] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_code_issue_artifacts_output.ListCodeIssueArtifactsOutput":
        """Lists the artifacts attached to an issue in descending artifactId order. Content is returned by GetCodeIssueArtifact.

        Args:
            environment_id: The environment that owns the issue.
            issue_id: The issue whose artifacts to list.
            artifact_type: Optional filter for a semantic artifact category. Omit to list all artifacts attached to the issue.
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_code_issue_artifacts_input.ListCodeIssueArtifactsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_code_issue_artifacts_output.ListCodeIssueArtifactsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_code_issue_artifacts

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_code_issue_artifacts.list_code_issue_artifacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListCodeIssueArtifacts")
        )
        input_: capo_continuum.types.list_code_issue_artifacts_input.ListCodeIssueArtifactsInput = {
            "environment_id": environment_id,
            "issue_id": issue_id,
        }
        if artifact_type is not None:
            input_["artifact_type"] = artifact_type
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

    def iter_list_code_issue_artifacts(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        issue_id: "capo_continuum.types.issue_id.IssueId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        artifact_type: Optional[
            "capo_continuum.types.issue_artifact_type.IssueArtifactType"
        ] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.issue_artifact_item.IssueArtifactItem]":
        _token = next_token
        while True:
            _response = self.list_code_issue_artifacts(
                environment_id,
                issue_id,
                config_overrides=config_overrides,
                artifact_type=artifact_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_code_scan(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.scan_client_token.ScanClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_code_scan_output.CreateCodeScanOutput":
        """Creates an explicit scan request for one environment. CP creates durable work before any queue delivery occurs. Retrying a request that succeeded, with the same clientToken on the same environment, returns the original scan instead of starting another one. Token handling is not yet atomic: requests with the same token that run at the same time, or a retry after a request that failed partway through, can leave an additional scan, which may end in the FAILED state with a message that it was superseded. Deleting the environment makes its tokens unusable; a later request with one of them returns ResourceNotFoundException. Each environment can have a limited number of scans in progress at the same time. Once that limit is enforced, a request that would exceed it returns ServiceQuotaExceededException; wait for a scan to finish (ListCodeScans shows each scan's status), then retry.

        Args:
            environment_id: Environment to scan.
            client_token: An optional token identifying one scan request for this environment. SDKs generate a token when omitted. If a request reaches the service without a token, the service generates one for that request, so each request without a token starts a new scan. To retry a request after a lost response, supply the same token on the same environment; once a request with that token has succeeded, a retry returns the original scan. Concurrent requests with the same token, or a retry after a request that failed partway through, can leave an additional scan, which may end FAILED as superseded. A token is bound to its scan for as long as the service retains the scan's build record, with no shorter expiry. Deleting the environment makes the binding inaccessible: a later request with the token returns ResourceNotFoundException.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_code_scan_input.CreateCodeScanInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_code_scan_output.CreateCodeScanOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_code_scan

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_code_scan.create_code_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateCodeScan")
        )
        input_: capo_continuum.types.create_code_scan_input.CreateCodeScanInput = {
            "environment_id": environment_id
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

    def get_code_scan(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        scan_run_id: "capo_continuum.types.scan_run_id.ScanRunId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_code_scan_output.GetCodeScanOutput":
        """Retrieves one customer-visible environment scan.

        Args:
            environment_id: Environment that owns the scan.
            scan_run_id: Scan to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_code_scan_input.GetCodeScanInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_code_scan_output.GetCodeScanOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_code_scan

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_code_scan.get_code_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetCodeScan")
        )
        input_: capo_continuum.types.get_code_scan_input.GetCodeScanInput = {
            "environment_id": environment_id,
            "scan_run_id": scan_run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_code_scans(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_code_scans_output.ListCodeScansOutput":
        """Lists customer-visible scans for one environment in descending scanRunId order.

        Args:
            environment_id: Environment whose scans to list.
            max_results: Maximum number of scans to return.
            next_token: Pagination token returned by a prior request.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_code_scans_input.ListCodeScansInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_code_scans_output.ListCodeScansOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_code_scans

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_code_scans.list_code_scans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListCodeScans")
        )
        input_: capo_continuum.types.list_code_scans_input.ListCodeScansInput = {
            "environment_id": environment_id
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

    def iter_list_code_scans(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.code_scan_summary.CodeScanSummary]":
        _token = next_token
        while True:
            _response = self.list_code_scans(
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_integration(
        self,
        name: "capo_continuum.types.integration_name.IntegrationName",
        provider_configuration: "capo_continuum.types.provider_configuration.ProviderConfiguration",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.integration_client_token.IntegrationClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_integration_output.CreateIntegrationOutput":
        """Creates a new integration with an external source provider. Repeating an identical request with the same clientToken returns the original integrationId, integrationArn, and createdAt. Token records are retained for eight hours after success or terminal failure, including after the integration is deleted; replaying a deleted integration's token does not recreate it. An identical request with a retained terminal failure returns the recorded error. Reusing a token with different parameters returns ValidationException. A fresh token starts a new create attempt; if the name is already owned by another integration, ConflictException includes that integration's identifier. An attempt still in progress may return ThrottlingException with retryAfterSeconds set to 1; retry with the same token and identical parameters. GitHub authorization codes are single use. Retry an unresolved attempt with its original token and unchanged parameters first. If the service reports a terminal failure, an expired attempt, or a successful token exchange whose integration could not be saved, restart GitHub authorization with a fresh token and authorization code. The service does not checkpoint provider results for recovery by another request.

        Args:
            client_token: An optional token identifying one create attempt within the caller's account, Region, and operation. SDKs generate a token when omitted. If a request reaches the service without a token, the service generates one for that request. Each request without a token starts a new attempt. To replay an attempt, supply the same token and identical input. Authorized users and roles in the same account can retry an attempt this way. Token records are retained for eight hours after success or terminal failure, including after deletion of a successfully created integration. Different input with the same token returns ValidationException.
            name: The name for the integration.
            provider_configuration: The provider-specific configuration required to create the integration. Only one member may be specified.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_integration_input.CreateIntegrationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_integration.create_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.create_integration_input.CreateIntegrationInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.create_integration_input

            return capo_continuum.types.create_integration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateIntegration", redact_input=_redact_input),
        )
        input_: capo_continuum.types.create_integration_input.CreateIntegrationInput = {
            "name": name,
            "provider_configuration": provider_configuration,
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

    def get_integration(
        self,
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_integration_output.GetIntegrationOutput":
        """Retrieves information about an integration.

        Args:
            integration_id: The unique identifier of the integration to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_integration_input.GetIntegrationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_integration_output.GetIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetIntegration")
        )
        input_: capo_continuum.types.get_integration_input.GetIntegrationInput = {
            "integration_id": integration_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_integration(
        self,
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        provider_configuration: "capo_continuum.types.update_provider_configuration.UpdateProviderConfiguration",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.update_integration_output.UpdateIntegrationOutput":
        """Rotates the credentials used by an Amazon S3 integration. Only S3 integrations can be updated; GitHub integrations cannot be modified. The integration's name, provider type, and bucket remain fixed. The caller must have iam:PassRole permission for the supplied role, including when only the external ID changes. Continuum verifies that the role can be assumed with the requested external ID and can access the existing bucket before saving both credentials atomically. Omitting externalId preserves its current value. Repeating both current credentials leaves updatedAt unchanged, but still requires authorization and access validation.

        Args:
            integration_id: The unique identifier of the S3 integration to update.
            provider_configuration: The provider-specific changes to apply. The member must match the integration's provider type, and only S3 integrations can be updated.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.update_integration_input.UpdateIntegrationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.update_integration_output.UpdateIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.update_integration.update_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.update_integration_input.UpdateIntegrationInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.update_integration_input

            return capo_continuum.types.update_integration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("UpdateIntegration", redact_input=_redact_input),
        )
        input_: capo_continuum.types.update_integration_input.UpdateIntegrationInput = {
            "integration_id": integration_id,
            "provider_configuration": provider_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_integration(
        self,
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Deletes an integration and releases its name and account quota. Its retained CreateIntegration token receipt can still replay the original result without recreating the integration. Shared provider registrations are retained: deleting one integration does not remove provider access used by another integration. A fresh GitHub CreateIntegration attempt requires a fresh OAuth authorization code and a new clientToken.

        Args:
            integration_id: The unique identifier of the integration to delete.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteIntegration")
        )
        input_: capo_continuum.types.delete_integration_input.DeleteIntegrationInput = {
            "integration_id": integration_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_integrations(
        self,
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_integrations_output.ListIntegrationsOutput":
        """Lists the integrations in your account in descending integrationId order.

        Args:
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_integrations_input.ListIntegrationsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_integrations

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_integrations.list_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListIntegrations")
        )
        input_: capo_continuum.types.list_integrations_input.ListIntegrationsInput = {}
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

    def iter_list_integrations(
        self,
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_continuum.types.integration_summary.IntegrationSummary]":
        _token = next_token
        while True:
            _response = self.list_integrations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

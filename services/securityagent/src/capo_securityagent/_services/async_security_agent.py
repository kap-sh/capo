"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityAgent``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_securityagent._auth._signers
import capo_securityagent._auth._sigv4
from capo_securityagent._auth._identity import Credentials
from capo_securityagent._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_securityagent._auth._zapros_handler import AuthMiddleware
from capo_securityagent._pagination import resolve_path as _resolve_path
from capo_securityagent._resources.security_agent.agent_space_resource import (
    AsyncAgentSpaceResource,
)
from capo_securityagent._resources.security_agent.application_resource import (
    AsyncApplicationResource,
)
from capo_securityagent._resources.security_agent.integration_resource import (
    AsyncIntegrationResource,
)
from capo_securityagent._resources.security_agent.private_connection_resource import (
    AsyncPrivateConnectionResource,
)
from capo_securityagent._resources.security_agent.security_requirement_pack_resource import (
    AsyncSecurityRequirementPackResource,
)
from capo_securityagent._resources.security_agent.target_domain_resource import (
    AsyncTargetDomainResource,
)
from capo_securityagent._services._aws_config import aaws_config
from capo_securityagent._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_securityagent.types.actor_message
    import capo_securityagent.types.add_artifact_input
    import capo_securityagent.types.add_artifact_output
    import capo_securityagent.types.agent_name
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.agent_space_id_list
    import capo_securityagent.types.agent_space_summary
    import capo_securityagent.types.application_id
    import capo_securityagent.types.application_summary
    import capo_securityagent.types.artifact_id
    import capo_securityagent.types.artifact_ids
    import capo_securityagent.types.artifact_summary
    import capo_securityagent.types.artifact_type
    import capo_securityagent.types.assets
    import capo_securityagent.types.aws_resources
    import capo_securityagent.types.batch_create_security_requirements_input
    import capo_securityagent.types.batch_create_security_requirements_output
    import capo_securityagent.types.batch_delete_code_reviews_input
    import capo_securityagent.types.batch_delete_code_reviews_output
    import capo_securityagent.types.batch_delete_pentests_input
    import capo_securityagent.types.batch_delete_pentests_output
    import capo_securityagent.types.batch_delete_security_requirements_input
    import capo_securityagent.types.batch_delete_security_requirements_output
    import capo_securityagent.types.batch_delete_threat_models_input
    import capo_securityagent.types.batch_delete_threat_models_output
    import capo_securityagent.types.batch_get_agent_spaces_input
    import capo_securityagent.types.batch_get_agent_spaces_output
    import capo_securityagent.types.batch_get_artifact_metadata_input
    import capo_securityagent.types.batch_get_artifact_metadata_output
    import capo_securityagent.types.batch_get_code_review_job_tasks_input
    import capo_securityagent.types.batch_get_code_review_job_tasks_output
    import capo_securityagent.types.batch_get_code_review_jobs_input
    import capo_securityagent.types.batch_get_code_review_jobs_output
    import capo_securityagent.types.batch_get_code_reviews_input
    import capo_securityagent.types.batch_get_code_reviews_output
    import capo_securityagent.types.batch_get_findings_input
    import capo_securityagent.types.batch_get_findings_output
    import capo_securityagent.types.batch_get_pentest_job_tasks_input
    import capo_securityagent.types.batch_get_pentest_job_tasks_output
    import capo_securityagent.types.batch_get_pentest_jobs_input
    import capo_securityagent.types.batch_get_pentest_jobs_output
    import capo_securityagent.types.batch_get_pentests_input
    import capo_securityagent.types.batch_get_pentests_output
    import capo_securityagent.types.batch_get_security_requirements_input
    import capo_securityagent.types.batch_get_security_requirements_output
    import capo_securityagent.types.batch_get_target_domains_input
    import capo_securityagent.types.batch_get_target_domains_output
    import capo_securityagent.types.batch_get_threat_model_job_tasks_input
    import capo_securityagent.types.batch_get_threat_model_job_tasks_output
    import capo_securityagent.types.batch_get_threat_model_jobs_input
    import capo_securityagent.types.batch_get_threat_model_jobs_output
    import capo_securityagent.types.batch_get_threat_models_input
    import capo_securityagent.types.batch_get_threat_models_output
    import capo_securityagent.types.batch_get_threats_input
    import capo_securityagent.types.batch_get_threats_output
    import capo_securityagent.types.batch_update_security_requirements_input
    import capo_securityagent.types.batch_update_security_requirements_output
    import capo_securityagent.types.certificate_chain
    import capo_securityagent.types.ci_cd_configuration
    import capo_securityagent.types.client_id
    import capo_securityagent.types.client_secret
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.code_remediation_strategy
    import capo_securityagent.types.code_review_id_list
    import capo_securityagent.types.code_review_job_id_list
    import capo_securityagent.types.code_review_job_summary
    import capo_securityagent.types.code_review_job_task_summary
    import capo_securityagent.types.code_review_settings
    import capo_securityagent.types.code_review_summary
    import capo_securityagent.types.confidence_level
    import capo_securityagent.types.create_agent_space_input
    import capo_securityagent.types.create_agent_space_output
    import capo_securityagent.types.create_application_request
    import capo_securityagent.types.create_application_response
    import capo_securityagent.types.create_code_review_input
    import capo_securityagent.types.create_code_review_output
    import capo_securityagent.types.create_integration_input
    import capo_securityagent.types.create_integration_output
    import capo_securityagent.types.create_membership_request
    import capo_securityagent.types.create_membership_response
    import capo_securityagent.types.create_pentest_input
    import capo_securityagent.types.create_pentest_output
    import capo_securityagent.types.create_private_connection_input
    import capo_securityagent.types.create_private_connection_output
    import capo_securityagent.types.create_security_requirement_entry_list
    import capo_securityagent.types.create_security_requirement_pack_input
    import capo_securityagent.types.create_security_requirement_pack_output
    import capo_securityagent.types.create_target_domain_input
    import capo_securityagent.types.create_target_domain_output
    import capo_securityagent.types.create_threat_input
    import capo_securityagent.types.create_threat_model_input
    import capo_securityagent.types.create_threat_model_output
    import capo_securityagent.types.create_threat_output
    import capo_securityagent.types.default_kms_key_id
    import capo_securityagent.types.delete_agent_space_input
    import capo_securityagent.types.delete_agent_space_output
    import capo_securityagent.types.delete_application_request
    import capo_securityagent.types.delete_artifact_input
    import capo_securityagent.types.delete_artifact_output
    import capo_securityagent.types.delete_integration_input
    import capo_securityagent.types.delete_integration_output
    import capo_securityagent.types.delete_membership_request
    import capo_securityagent.types.delete_membership_response
    import capo_securityagent.types.delete_private_connection_input
    import capo_securityagent.types.delete_private_connection_output
    import capo_securityagent.types.delete_security_requirement_pack_input
    import capo_securityagent.types.delete_security_requirement_pack_output
    import capo_securityagent.types.delete_target_domain_input
    import capo_securityagent.types.delete_target_domain_output
    import capo_securityagent.types.describe_private_connection_input
    import capo_securityagent.types.describe_private_connection_output
    import capo_securityagent.types.diff_source
    import capo_securityagent.types.discovered_endpoint
    import capo_securityagent.types.document_list
    import capo_securityagent.types.domain_verification_method
    import capo_securityagent.types.finding_id_list
    import capo_securityagent.types.finding_status
    import capo_securityagent.types.finding_summary
    import capo_securityagent.types.get_application_request
    import capo_securityagent.types.get_application_response
    import capo_securityagent.types.get_artifact_input
    import capo_securityagent.types.get_artifact_output
    import capo_securityagent.types.get_integration_input
    import capo_securityagent.types.get_integration_output
    import capo_securityagent.types.get_security_requirement_pack_input
    import capo_securityagent.types.get_security_requirement_pack_output
    import capo_securityagent.types.id_c_instance_arn
    import capo_securityagent.types.import_security_requirements_input
    import capo_securityagent.types.import_security_requirements_output
    import capo_securityagent.types.import_source
    import capo_securityagent.types.initiate_provider_registration_input
    import capo_securityagent.types.initiate_provider_registration_output
    import capo_securityagent.types.integrated_resource_input_item_list
    import capo_securityagent.types.integrated_resource_summary
    import capo_securityagent.types.integration_filter
    import capo_securityagent.types.integration_id
    import capo_securityagent.types.integration_summary
    import capo_securityagent.types.job_type
    import capo_securityagent.types.kms_key_id
    import capo_securityagent.types.list_actor_messages_input
    import capo_securityagent.types.list_actor_messages_output
    import capo_securityagent.types.list_agent_spaces_input
    import capo_securityagent.types.list_agent_spaces_output
    import capo_securityagent.types.list_applications_request
    import capo_securityagent.types.list_applications_response
    import capo_securityagent.types.list_artifacts_input
    import capo_securityagent.types.list_artifacts_output
    import capo_securityagent.types.list_code_review_job_tasks_input
    import capo_securityagent.types.list_code_review_job_tasks_output
    import capo_securityagent.types.list_code_review_jobs_for_code_review_input
    import capo_securityagent.types.list_code_review_jobs_for_code_review_output
    import capo_securityagent.types.list_code_reviews_input
    import capo_securityagent.types.list_code_reviews_output
    import capo_securityagent.types.list_discovered_endpoints_input
    import capo_securityagent.types.list_discovered_endpoints_output
    import capo_securityagent.types.list_findings_input
    import capo_securityagent.types.list_findings_output
    import capo_securityagent.types.list_integrated_resources_input
    import capo_securityagent.types.list_integrated_resources_output
    import capo_securityagent.types.list_integrations_input
    import capo_securityagent.types.list_integrations_output
    import capo_securityagent.types.list_memberships_request
    import capo_securityagent.types.list_memberships_response
    import capo_securityagent.types.list_pentest_job_tasks_input
    import capo_securityagent.types.list_pentest_job_tasks_output
    import capo_securityagent.types.list_pentest_jobs_for_pentest_input
    import capo_securityagent.types.list_pentest_jobs_for_pentest_output
    import capo_securityagent.types.list_pentests_input
    import capo_securityagent.types.list_pentests_output
    import capo_securityagent.types.list_private_connections_input
    import capo_securityagent.types.list_private_connections_output
    import capo_securityagent.types.list_security_requirement_pack_filter
    import capo_securityagent.types.list_security_requirement_packs_input
    import capo_securityagent.types.list_security_requirement_packs_output
    import capo_securityagent.types.list_security_requirements_input
    import capo_securityagent.types.list_security_requirements_output
    import capo_securityagent.types.list_tags_for_resource_input
    import capo_securityagent.types.list_tags_for_resource_output
    import capo_securityagent.types.list_target_domains_input
    import capo_securityagent.types.list_target_domains_output
    import capo_securityagent.types.list_threat_model_job_tasks_input
    import capo_securityagent.types.list_threat_model_job_tasks_output
    import capo_securityagent.types.list_threat_model_jobs_input
    import capo_securityagent.types.list_threat_model_jobs_output
    import capo_securityagent.types.list_threat_models_input
    import capo_securityagent.types.list_threat_models_output
    import capo_securityagent.types.list_threats_input
    import capo_securityagent.types.list_threats_output
    import capo_securityagent.types.max_results
    import capo_securityagent.types.membership_config
    import capo_securityagent.types.membership_id
    import capo_securityagent.types.membership_summary
    import capo_securityagent.types.membership_type
    import capo_securityagent.types.membership_type_filter
    import capo_securityagent.types.network_traffic_config
    import capo_securityagent.types.next_token
    import capo_securityagent.types.pentest_id_list
    import capo_securityagent.types.pentest_job_id_list
    import capo_securityagent.types.pentest_job_summary
    import capo_securityagent.types.pentest_summary
    import capo_securityagent.types.private_connection_mode
    import capo_securityagent.types.private_connection_name
    import capo_securityagent.types.private_connection_summary
    import capo_securityagent.types.provider
    import capo_securityagent.types.provider_input
    import capo_securityagent.types.report_destination
    import capo_securityagent.types.report_filters
    import capo_securityagent.types.resource_arn
    import capo_securityagent.types.resource_type
    import capo_securityagent.types.risk_level
    import capo_securityagent.types.risk_type_list
    import capo_securityagent.types.role_arn
    import capo_securityagent.types.scope_change_list
    import capo_securityagent.types.security_requirement_name_list
    import capo_securityagent.types.security_requirement_pack_id
    import capo_securityagent.types.security_requirement_pack_name
    import capo_securityagent.types.security_requirement_pack_status
    import capo_securityagent.types.security_requirement_pack_summary
    import capo_securityagent.types.security_requirement_summary
    import capo_securityagent.types.service_role
    import capo_securityagent.types.skill_type_list
    import capo_securityagent.types.start_code_remediation_input
    import capo_securityagent.types.start_code_remediation_output
    import capo_securityagent.types.start_code_review_job_input
    import capo_securityagent.types.start_code_review_job_output
    import capo_securityagent.types.start_pentest_job_input
    import capo_securityagent.types.start_pentest_job_output
    import capo_securityagent.types.start_threat_model_job_input
    import capo_securityagent.types.start_threat_model_job_output
    import capo_securityagent.types.step_name
    import capo_securityagent.types.stop_code_review_job_input
    import capo_securityagent.types.stop_code_review_job_output
    import capo_securityagent.types.stop_pentest_job_input
    import capo_securityagent.types.stop_pentest_job_output
    import capo_securityagent.types.stop_threat_model_job_input
    import capo_securityagent.types.stop_threat_model_job_output
    import capo_securityagent.types.stride_category_list
    import capo_securityagent.types.string_list
    import capo_securityagent.types.tag_key_list
    import capo_securityagent.types.tag_map
    import capo_securityagent.types.tag_resource_input
    import capo_securityagent.types.tag_resource_output
    import capo_securityagent.types.target_domain_id
    import capo_securityagent.types.target_domain_id_list
    import capo_securityagent.types.target_domain_summary
    import capo_securityagent.types.target_url
    import capo_securityagent.types.task_id_list
    import capo_securityagent.types.task_summary
    import capo_securityagent.types.threat_anchor_shape
    import capo_securityagent.types.threat_evidence_list
    import capo_securityagent.types.threat_id_list
    import capo_securityagent.types.threat_model_id_list
    import capo_securityagent.types.threat_model_job_id_list
    import capo_securityagent.types.threat_model_job_summary
    import capo_securityagent.types.threat_model_job_task_summary
    import capo_securityagent.types.threat_model_summary
    import capo_securityagent.types.threat_severity
    import capo_securityagent.types.threat_status
    import capo_securityagent.types.threat_summary
    import capo_securityagent.types.untag_resource_input
    import capo_securityagent.types.untag_resource_output
    import capo_securityagent.types.update_agent_space_input
    import capo_securityagent.types.update_agent_space_output
    import capo_securityagent.types.update_application_request
    import capo_securityagent.types.update_application_response
    import capo_securityagent.types.update_code_review_input
    import capo_securityagent.types.update_code_review_output
    import capo_securityagent.types.update_finding_input
    import capo_securityagent.types.update_finding_output
    import capo_securityagent.types.update_integrated_resources_input
    import capo_securityagent.types.update_integrated_resources_output
    import capo_securityagent.types.update_integration_input
    import capo_securityagent.types.update_integration_output
    import capo_securityagent.types.update_pentest_input
    import capo_securityagent.types.update_pentest_output
    import capo_securityagent.types.update_private_connection_certificate_input
    import capo_securityagent.types.update_private_connection_certificate_output
    import capo_securityagent.types.update_security_requirement_entry_list
    import capo_securityagent.types.update_security_requirement_pack_input
    import capo_securityagent.types.update_security_requirement_pack_output
    import capo_securityagent.types.update_target_domain_input
    import capo_securityagent.types.update_target_domain_output
    import capo_securityagent.types.update_threat_input
    import capo_securityagent.types.update_threat_model_input
    import capo_securityagent.types.update_threat_model_output
    import capo_securityagent.types.update_threat_output
    import capo_securityagent.types.validation_mode
    import capo_securityagent.types.verify_target_domain_input
    import capo_securityagent.types.verify_target_domain_output
    import capo_securityagent.types.vpc_config
    import capo_securityagent.types.webhook_action


class AsyncSecurityAgentClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSecurityAgentClient:
    """A client for the ``SecurityAgent`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncSecurityAgentClientConfig(
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
        self.agent_space_resource = AsyncAgentSpaceResource(self)
        self.application_resource = AsyncApplicationResource(self)
        self.integration_resource = AsyncIntegrationResource(self)
        self.private_connection_resource = AsyncPrivateConnectionResource(self)
        self.security_requirement_pack_resource = AsyncSecurityRequirementPackResource(
            self
        )
        self.target_domain_resource = AsyncTargetDomainResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSecurityAgentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSecurityAgentClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def add_artifact(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_content: bytes,
        artifact_type: "capo_securityagent.types.artifact_type.ArtifactType",
        file_name: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.add_artifact_output.AddArtifactOutput":
        """<p>Uploads an artifact to an agent space. Artifacts provide additional context for security testing, such as architecture diagrams, API specifications, or configuration files.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to add the artifact to.</p>
            artifact_content: <p>The binary content of the artifact to upload.</p>
            artifact_type: <p>The file type of the artifact. Valid values include TXT, PNG, JPEG, MD, PDF, DOCX, DOC, JSON, and YAML.</p>
            file_name: <p>The file name of the artifact.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.add_artifact_input.AddArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.add_artifact_output.AddArtifactOutput"
        ]:
            import capo_securityagent._operations.security_agent.add_artifact

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.add_artifact.async_add_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.add_artifact_input.AddArtifactInput = {
            "agent_space_id": agent_space_id,
            "artifact_content": artifact_content,
            "artifact_type": artifact_type,
            "file_name": file_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_create_security_requirements(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        security_requirements: "capo_securityagent.types.create_security_requirement_entry_list.CreateSecurityRequirementEntryList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_create_security_requirements_output.BatchCreateSecurityRequirementsOutput":
        """<p>Batch creates security requirements in a customer managed pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to add requirements to.</p>
            security_requirements: <p>The list of security requirements to create.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota. Review your current usage and request a quota increase if needed.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_create_security_requirements_input.BatchCreateSecurityRequirementsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_create_security_requirements_output.BatchCreateSecurityRequirementsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_create_security_requirements

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_create_security_requirements.async_batch_create_security_requirements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_create_security_requirements_input.BatchCreateSecurityRequirementsInput = {
            "pack_id": pack_id,
            "security_requirements": security_requirements,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_code_reviews(
        self,
        code_review_ids: "capo_securityagent.types.code_review_id_list.CodeReviewIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_delete_code_reviews_output.BatchDeleteCodeReviewsOutput":
        """<p>Deletes one or more code reviews from an agent space.</p>

        Args:
            code_review_ids: <p>The list of code review identifiers to delete.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code reviews to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_delete_code_reviews_input.BatchDeleteCodeReviewsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_delete_code_reviews_output.BatchDeleteCodeReviewsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_delete_code_reviews

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_delete_code_reviews.async_batch_delete_code_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_delete_code_reviews_input.BatchDeleteCodeReviewsInput = {
            "code_review_ids": code_review_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_pentests(
        self,
        pentest_ids: "capo_securityagent.types.pentest_id_list.PentestIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_delete_pentests_output.BatchDeletePentestsOutput":
        """<p>Deletes one or more pentests from an agent space.</p>

        Args:
            pentest_ids: <p>The list of pentest identifiers to delete.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentests to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_delete_pentests_input.BatchDeletePentestsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_delete_pentests_output.BatchDeletePentestsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_delete_pentests

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_delete_pentests.async_batch_delete_pentests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_delete_pentests_input.BatchDeletePentestsInput = {
            "pentest_ids": pentest_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_security_requirements(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        security_requirement_names: "capo_securityagent.types.security_requirement_name_list.SecurityRequirementNameList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_delete_security_requirements_output.BatchDeleteSecurityRequirementsOutput":
        """<p>Batch deletes security requirements from a customer managed pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to remove requirements from.</p>
            security_requirement_names: <p>The list of security requirement names to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_delete_security_requirements_input.BatchDeleteSecurityRequirementsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_delete_security_requirements_output.BatchDeleteSecurityRequirementsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_delete_security_requirements

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_delete_security_requirements.async_batch_delete_security_requirements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_delete_security_requirements_input.BatchDeleteSecurityRequirementsInput = {
            "pack_id": pack_id,
            "security_requirement_names": security_requirement_names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_threat_models(
        self,
        threat_model_ids: "capo_securityagent.types.threat_model_id_list.ThreatModelIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_delete_threat_models_output.BatchDeleteThreatModelsOutput":
        """<p>Deletes one or more threat models from an agent space.</p>

        Args:
            threat_model_ids: <p>The list of threat model identifiers to delete.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the threat models to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_delete_threat_models_input.BatchDeleteThreatModelsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_delete_threat_models_output.BatchDeleteThreatModelsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_delete_threat_models

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_delete_threat_models.async_batch_delete_threat_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_delete_threat_models_input.BatchDeleteThreatModelsInput = {
            "threat_model_ids": threat_model_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_artifact_metadata(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_ids: "capo_securityagent.types.artifact_ids.ArtifactIds",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_artifact_metadata_output.BatchGetArtifactMetadataOutput":
        """<p>Retrieves metadata for one or more artifacts in an agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the artifacts.</p>
            artifact_ids: <p>The list of artifact identifiers to retrieve metadata for.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_artifact_metadata_input.BatchGetArtifactMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_artifact_metadata_output.BatchGetArtifactMetadataOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_artifact_metadata

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_artifact_metadata.async_batch_get_artifact_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_artifact_metadata_input.BatchGetArtifactMetadataInput = {
            "agent_space_id": agent_space_id,
            "artifact_ids": artifact_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_code_review_jobs(
        self,
        code_review_job_ids: "capo_securityagent.types.code_review_job_id_list.CodeReviewJobIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_code_review_jobs_output.BatchGetCodeReviewJobsOutput":
        """<p>Retrieves information about one or more code review jobs in an agent space.</p>

        Args:
            code_review_job_ids: <p>The list of code review job identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code review jobs.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_code_review_jobs_input.BatchGetCodeReviewJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_code_review_jobs_output.BatchGetCodeReviewJobsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_code_review_jobs

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_code_review_jobs.async_batch_get_code_review_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_code_review_jobs_input.BatchGetCodeReviewJobsInput = {
            "code_review_job_ids": code_review_job_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_code_review_job_tasks(
        self,
        agent_space_id: str,
        code_review_job_task_ids: "capo_securityagent.types.task_id_list.TaskIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_code_review_job_tasks_output.BatchGetCodeReviewJobTasksOutput":
        """<p>Retrieves information about one or more tasks within a code review job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the tasks.</p>
            code_review_job_task_ids: <p>The list of task identifiers to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_code_review_job_tasks_input.BatchGetCodeReviewJobTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_code_review_job_tasks_output.BatchGetCodeReviewJobTasksOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_code_review_job_tasks

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_code_review_job_tasks.async_batch_get_code_review_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_code_review_job_tasks_input.BatchGetCodeReviewJobTasksInput = {
            "agent_space_id": agent_space_id,
            "code_review_job_task_ids": code_review_job_task_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_code_reviews(
        self,
        code_review_ids: "capo_securityagent.types.code_review_id_list.CodeReviewIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_code_reviews_output.BatchGetCodeReviewsOutput":
        """<p>Retrieves information about one or more code reviews in an agent space.</p>

        Args:
            code_review_ids: <p>The list of code review identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code reviews.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_code_reviews_input.BatchGetCodeReviewsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_code_reviews_output.BatchGetCodeReviewsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_code_reviews

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_code_reviews.async_batch_get_code_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_code_reviews_input.BatchGetCodeReviewsInput = {
            "code_review_ids": code_review_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_findings(
        self,
        finding_ids: "capo_securityagent.types.finding_id_list.FindingIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_findings_output.BatchGetFindingsOutput":
        """<p>Retrieves information about one or more security findings in an agent space.</p>

        Args:
            finding_ids: <p>The list of finding identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the findings.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_findings_input.BatchGetFindingsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_findings_output.BatchGetFindingsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_findings

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_findings.async_batch_get_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_findings_input.BatchGetFindingsInput = {
            "finding_ids": finding_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_pentest_jobs(
        self,
        pentest_job_ids: "capo_securityagent.types.pentest_job_id_list.PentestJobIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_pentest_jobs_output.BatchGetPentestJobsOutput":
        """<p>Retrieves information about one or more pentest jobs in an agent space.</p>

        Args:
            pentest_job_ids: <p>The list of pentest job identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentest jobs.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_pentest_jobs_input.BatchGetPentestJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_pentest_jobs_output.BatchGetPentestJobsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_pentest_jobs

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_pentest_jobs.async_batch_get_pentest_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_pentest_jobs_input.BatchGetPentestJobsInput = {
            "pentest_job_ids": pentest_job_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_pentest_job_tasks(
        self,
        agent_space_id: str,
        task_ids: "capo_securityagent.types.task_id_list.TaskIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_pentest_job_tasks_output.BatchGetPentestJobTasksOutput":
        """<p>Retrieves information about one or more tasks within a pentest job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the tasks.</p>
            task_ids: <p>The list of task identifiers to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_pentest_job_tasks_input.BatchGetPentestJobTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_pentest_job_tasks_output.BatchGetPentestJobTasksOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_pentest_job_tasks

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_pentest_job_tasks.async_batch_get_pentest_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_pentest_job_tasks_input.BatchGetPentestJobTasksInput = {
            "agent_space_id": agent_space_id,
            "task_ids": task_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_pentests(
        self,
        pentest_ids: "capo_securityagent.types.pentest_id_list.PentestIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_pentests_output.BatchGetPentestsOutput":
        """<p>Retrieves information about one or more pentests in an agent space.</p>

        Args:
            pentest_ids: <p>The list of pentest identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentests.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_pentests_input.BatchGetPentestsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_pentests_output.BatchGetPentestsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_pentests

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_pentests.async_batch_get_pentests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_pentests_input.BatchGetPentestsInput = {
            "pentest_ids": pentest_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_security_requirements(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        security_requirement_names: "capo_securityagent.types.security_requirement_name_list.SecurityRequirementNameList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_security_requirements_output.BatchGetSecurityRequirementsOutput":
        """<p>Batch retrieves security requirements from a pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to retrieve requirements from.</p>
            security_requirement_names: <p>The list of security requirement names to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_security_requirements_input.BatchGetSecurityRequirementsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_security_requirements_output.BatchGetSecurityRequirementsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_security_requirements

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_security_requirements.async_batch_get_security_requirements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_security_requirements_input.BatchGetSecurityRequirementsInput = {
            "pack_id": pack_id,
            "security_requirement_names": security_requirement_names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_threat_model_jobs(
        self,
        threat_model_job_ids: "capo_securityagent.types.threat_model_job_id_list.ThreatModelJobIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_threat_model_jobs_output.BatchGetThreatModelJobsOutput":
        """<p>Retrieves information about one or more threat model jobs in an agent space.</p>

        Args:
            threat_model_job_ids: <p>The list of threat model job identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the threat model jobs.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_threat_model_jobs_input.BatchGetThreatModelJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_threat_model_jobs_output.BatchGetThreatModelJobsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_threat_model_jobs

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_threat_model_jobs.async_batch_get_threat_model_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_threat_model_jobs_input.BatchGetThreatModelJobsInput = {
            "threat_model_job_ids": threat_model_job_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_threat_model_job_tasks(
        self,
        agent_space_id: str,
        threat_model_job_task_ids: "capo_securityagent.types.task_id_list.TaskIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_threat_model_job_tasks_output.BatchGetThreatModelJobTasksOutput":
        """<p>Retrieves information about one or more tasks within a threat model job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the tasks.</p>
            threat_model_job_task_ids: <p>The list of task identifiers to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_threat_model_job_tasks_input.BatchGetThreatModelJobTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_threat_model_job_tasks_output.BatchGetThreatModelJobTasksOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_threat_model_job_tasks

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_threat_model_job_tasks.async_batch_get_threat_model_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_threat_model_job_tasks_input.BatchGetThreatModelJobTasksInput = {
            "agent_space_id": agent_space_id,
            "threat_model_job_task_ids": threat_model_job_task_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_threat_models(
        self,
        threat_model_ids: "capo_securityagent.types.threat_model_id_list.ThreatModelIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_threat_models_output.BatchGetThreatModelsOutput":
        """<p>Retrieves information about one or more threat models in an agent space.</p>

        Args:
            threat_model_ids: <p>The list of threat model identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the threat models.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_threat_models_input.BatchGetThreatModelsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_threat_models_output.BatchGetThreatModelsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_threat_models

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_threat_models.async_batch_get_threat_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_threat_models_input.BatchGetThreatModelsInput = {
            "threat_model_ids": threat_model_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_threats(
        self,
        threat_ids: "capo_securityagent.types.threat_id_list.ThreatIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_threats_output.BatchGetThreatsOutput":
        """<p>Retrieves information about one or more threats.</p>

        Args:
            threat_ids: <p>The list of threat identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_threats_input.BatchGetThreatsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_threats_output.BatchGetThreatsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_threats

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_threats.async_batch_get_threats(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_threats_input.BatchGetThreatsInput = {
            "threat_ids": threat_ids,
            "agent_space_id": agent_space_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_security_requirements(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        security_requirements: "capo_securityagent.types.update_security_requirement_entry_list.UpdateSecurityRequirementEntryList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_update_security_requirements_output.BatchUpdateSecurityRequirementsOutput":
        """<p>Batch updates security requirements within a customer managed pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack containing the requirements to update.</p>
            security_requirements: <p>The list of security requirement updates to apply.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_update_security_requirements_input.BatchUpdateSecurityRequirementsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_update_security_requirements_output.BatchUpdateSecurityRequirementsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_update_security_requirements

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_update_security_requirements.async_batch_update_security_requirements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_update_security_requirements_input.BatchUpdateSecurityRequirementsInput = {
            "pack_id": pack_id,
            "security_requirements": security_requirements,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_code_review(
        self,
        title: str,
        agent_space_id: str,
        assets: "capo_securityagent.types.assets.Assets",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        service_role: Optional[
            "capo_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "capo_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        code_remediation_strategy: Optional[
            "capo_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
        validation_mode: Optional[
            "capo_securityagent.types.validation_mode.ValidationMode"
        ] = None,
        max_task_hours: Optional[float] = None,
        report_destination: Optional[
            "capo_securityagent.types.report_destination.ReportDestination"
        ] = None,
        report_filters: Optional[
            "capo_securityagent.types.report_filters.ReportFilters"
        ] = None,
    ) -> "capo_securityagent.types.create_code_review_output.CreateCodeReviewOutput":
        """<p>Creates a new code review configuration in an agent space. A code review defines the parameters for automated security-focused code analysis.</p>

        Args:
            title: <p>The title of the code review.</p>
            agent_space_id: <p>The unique identifier of the agent space to create the code review in.</p>
            assets: <p>The assets to include in the code review, such as documents and source code.</p>
            service_role: <p>The IAM service role to use for the code review.</p>
            log_config: <p>The CloudWatch Logs configuration for the code review.</p>
            code_remediation_strategy: <p>The code remediation strategy for the code review. Valid values are AUTOMATIC and DISABLED.</p>
            validation_mode: <p>The validation mode for the code review. Valid values are SIMULATED and DISABLED.</p>
            max_task_hours: <p>The maximum number of billable task hours allowed for jobs started from this code review. Must be a positive number. If not set, jobs run to completion with no budget cap.</p>
            report_destination: <p>The destination for publishing scan reports to an integrated document provider.</p>
            report_filters: <p>The report-generation filters applied when the report is exported.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_code_review_input.CreateCodeReviewInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_code_review_output.CreateCodeReviewOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_code_review

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_code_review.async_create_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_code_review_input.CreateCodeReviewInput = {
            "title": title,
            "agent_space_id": agent_space_id,
            "assets": assets,
        }
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy
        if validation_mode is not None:
            input_["validation_mode"] = validation_mode
        if max_task_hours is not None:
            input_["max_task_hours"] = max_task_hours
        if report_destination is not None:
            input_["report_destination"] = report_destination
        if report_filters is not None:
            input_["report_filters"] = report_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_membership(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        membership_id: "capo_securityagent.types.membership_id.MembershipId",
        member_type: "capo_securityagent.types.membership_type.MembershipType",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        config: Optional[
            "capo_securityagent.types.membership_config.MembershipConfig"
        ] = None,
    ) -> "capo_securityagent.types.create_membership_response.CreateMembershipResponse":
        """<p>Creates a new membership, granting a user access to an agent space within an application.</p>

        Args:
            application_id: <p>The unique identifier of the application that contains the agent space.</p>
            agent_space_id: <p>The unique identifier of the agent space to grant access to.</p>
            membership_id: <p>The unique identifier for the membership.</p>
            member_type: <p>The type of member. Currently, only USER is supported.</p>
            config: <p>The configuration for the membership, such as the user role.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_membership_request.CreateMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_membership_response.CreateMembershipResponse"
        ]:
            import capo_securityagent._operations.security_agent.create_membership

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_membership.async_create_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_membership_request.CreateMembershipRequest = {
            "application_id": application_id,
            "agent_space_id": agent_space_id,
            "membership_id": membership_id,
            "member_type": member_type,
        }
        if config is not None:
            input_["config"] = config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_pentest(
        self,
        title: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        assets: Optional["capo_securityagent.types.assets.Assets"] = None,
        exclude_risk_types: Optional[
            "capo_securityagent.types.risk_type_list.RiskTypeList"
        ] = None,
        service_role: Optional[
            "capo_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "capo_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        vpc_config: Optional["capo_securityagent.types.vpc_config.VpcConfig"] = None,
        network_traffic_config: Optional[
            "capo_securityagent.types.network_traffic_config.NetworkTrafficConfig"
        ] = None,
        code_remediation_strategy: Optional[
            "capo_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
        disable_managed_skills: Optional[
            "capo_securityagent.types.skill_type_list.SkillTypeList"
        ] = None,
        max_task_hours: Optional[float] = None,
        report_destination: Optional[
            "capo_securityagent.types.report_destination.ReportDestination"
        ] = None,
        report_filters: Optional[
            "capo_securityagent.types.report_filters.ReportFilters"
        ] = None,
        cicd_configuration: Optional[
            "capo_securityagent.types.ci_cd_configuration.CiCdConfiguration"
        ] = None,
    ) -> "capo_securityagent.types.create_pentest_output.CreatePentestOutput":
        """<p>Creates a new pentest configuration in an agent space. A pentest defines the security test parameters, including target assets, risk type exclusions, and logging configuration.</p>

        Args:
            title: <p>The title of the pentest.</p>
            agent_space_id: <p>The unique identifier of the agent space to create the pentest in.</p>
            assets: <p>The assets to include in the pentest, such as endpoints, actors, documents, and source code.</p>
            exclude_risk_types: <p>The list of risk types to exclude from the pentest.</p>
            service_role: <p>The IAM service role to use for the pentest.</p>
            log_config: <p>The CloudWatch Logs configuration for the pentest.</p>
            vpc_config: <p>The VPC configuration for the pentest.</p>
            network_traffic_config: <p>The network traffic configuration for the pentest, including custom headers and traffic rules.</p>
            code_remediation_strategy: <p>The code remediation strategy for the pentest. Valid values are AUTOMATIC and DISABLED.</p>
            disable_managed_skills: <p>A list of managed skills to disable for this pentest. Valid values include FINDING_PERSONALIZATION and LOGIN_OPTIMIZATION.</p>
            max_task_hours: <p>The maximum number of billable task hours allowed for jobs started from this pentest. Must be a positive number. If not set, jobs run to completion with no budget cap.</p>
            report_destination: <p>The destination for publishing scan reports to an integrated document provider.</p>
            report_filters: <p>The report-generation filters applied when the report is exported.</p>
            cicd_configuration: <p>The CI/CD pentesting configuration to apply to the pentest.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_pentest_input.CreatePentestInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_pentest_output.CreatePentestOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_pentest

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_pentest.async_create_pentest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_pentest_input.CreatePentestInput = {
            "title": title,
            "agent_space_id": agent_space_id,
        }
        if assets is not None:
            input_["assets"] = assets
        if exclude_risk_types is not None:
            input_["exclude_risk_types"] = exclude_risk_types
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if network_traffic_config is not None:
            input_["network_traffic_config"] = network_traffic_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy
        if disable_managed_skills is not None:
            input_["disable_managed_skills"] = disable_managed_skills
        if max_task_hours is not None:
            input_["max_task_hours"] = max_task_hours
        if report_destination is not None:
            input_["report_destination"] = report_destination
        if report_filters is not None:
            input_["report_filters"] = report_filters
        if cicd_configuration is not None:
            input_["cicd_configuration"] = cicd_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_threat(
        self,
        agent_space_id: str,
        threat_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        title: Optional[str] = None,
        statement: Optional[str] = None,
        severity: Optional[
            "capo_securityagent.types.threat_severity.ThreatSeverity"
        ] = None,
        comments: Optional[str] = None,
        stride: Optional[
            "capo_securityagent.types.stride_category_list.StrideCategoryList"
        ] = None,
        threat_source: Optional[str] = None,
        prerequisites: Optional[str] = None,
        threat_action: Optional[str] = None,
        threat_impact: Optional[str] = None,
        impacted_goal: Optional[
            "capo_securityagent.types.string_list.StringList"
        ] = None,
        impacted_assets: Optional[
            "capo_securityagent.types.string_list.StringList"
        ] = None,
        anchor: Optional[
            "capo_securityagent.types.threat_anchor_shape.ThreatAnchorShape"
        ] = None,
        evidence: Optional[
            "capo_securityagent.types.threat_evidence_list.ThreatEvidenceList"
        ] = None,
        recommendation: Optional[str] = None,
    ) -> "capo_securityagent.types.create_threat_output.CreateThreatOutput":
        """<p>Creates a new threat under a threat model job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            threat_job_id: <p>The unique identifier of the threat model job the threat belongs to.</p>
            title: <p>A short title summarizing the threat.</p>
            statement: <p>The natural-language threat statement.</p>
            severity: <p>The severity level of the threat.</p>
            comments: <p>Optional customer comment on the threat.</p>
            stride: <p>The STRIDE categories applicable to this threat.</p>
            threat_source: <p>The actor or origin of the threat.</p>
            prerequisites: <p>The conditions required for the threat to be exploitable.</p>
            threat_action: <p>What the threat source can do.</p>
            threat_impact: <p>The direct consequence of the threat action.</p>
            impacted_goal: <p>The security goals affected by the threat.</p>
            impacted_assets: <p>The specific assets affected by the threat.</p>
            anchor: <p>The DFD element this threat is anchored to.</p>
            evidence: <p>The source code files supporting the threat.</p>
            recommendation: <p>The recommended mitigation guidance for this threat.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_threat_input.CreateThreatInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_threat_output.CreateThreatOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_threat

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_threat.async_create_threat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_threat_input.CreateThreatInput = {
            "agent_space_id": agent_space_id,
            "threat_job_id": threat_job_id,
        }
        if title is not None:
            input_["title"] = title
        if statement is not None:
            input_["statement"] = statement
        if severity is not None:
            input_["severity"] = severity
        if comments is not None:
            input_["comments"] = comments
        if stride is not None:
            input_["stride"] = stride
        if threat_source is not None:
            input_["threat_source"] = threat_source
        if prerequisites is not None:
            input_["prerequisites"] = prerequisites
        if threat_action is not None:
            input_["threat_action"] = threat_action
        if threat_impact is not None:
            input_["threat_impact"] = threat_impact
        if impacted_goal is not None:
            input_["impacted_goal"] = impacted_goal
        if impacted_assets is not None:
            input_["impacted_assets"] = impacted_assets
        if anchor is not None:
            input_["anchor"] = anchor
        if evidence is not None:
            input_["evidence"] = evidence
        if recommendation is not None:
            input_["recommendation"] = recommendation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_threat_model(
        self,
        title: str,
        agent_space_id: str,
        service_role: "capo_securityagent.types.service_role.ServiceRole",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        description: Optional[str] = None,
        assets: Optional["capo_securityagent.types.assets.Assets"] = None,
        scope_docs: Optional[
            "capo_securityagent.types.document_list.DocumentList"
        ] = None,
        log_config: Optional[
            "capo_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        report_destination: Optional[
            "capo_securityagent.types.report_destination.ReportDestination"
        ] = None,
    ) -> "capo_securityagent.types.create_threat_model_output.CreateThreatModelOutput":
        """<p>Creates a new threat model configuration in an agent space. A threat model defines the parameters for automated threat analysis.</p>

        Args:
            title: <p>The title of the threat model.</p>
            agent_space_id: <p>The unique identifier of the agent space to create the threat model in.</p>
            description: <p>A description of the application or system being threat modeled.</p>
            assets: <p>The assets to include in the threat model.</p>
            scope_docs: <p>The scoped documents for the agent to focus on during threat modeling.</p>
            service_role: <p>The IAM service role to use for the threat model.</p>
            log_config: <p>The CloudWatch Logs configuration for the threat model.</p>
            report_destination: <p>The destination for publishing scan reports to an integrated document provider.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_threat_model_input.CreateThreatModelInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_threat_model_output.CreateThreatModelOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_threat_model

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_threat_model.async_create_threat_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_threat_model_input.CreateThreatModelInput = {
            "title": title,
            "agent_space_id": agent_space_id,
            "service_role": service_role,
        }
        if description is not None:
            input_["description"] = description
        if assets is not None:
            input_["assets"] = assets
        if scope_docs is not None:
            input_["scope_docs"] = scope_docs
        if log_config is not None:
            input_["log_config"] = log_config
        if report_destination is not None:
            input_["report_destination"] = report_destination

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_artifact(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_id: "capo_securityagent.types.artifact_id.ArtifactId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_artifact_output.DeleteArtifactOutput":
        """<p>Deletes an artifact from an agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the artifact.</p>
            artifact_id: <p>The unique identifier of the artifact to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_artifact_input.DeleteArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_artifact_output.DeleteArtifactOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_artifact

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_artifact.async_delete_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_artifact_input.DeleteArtifactInput = {
            "agent_space_id": agent_space_id,
            "artifact_id": artifact_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_membership(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        membership_id: "capo_securityagent.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        member_type: Optional[
            "capo_securityagent.types.membership_type.MembershipType"
        ] = None,
    ) -> "capo_securityagent.types.delete_membership_response.DeleteMembershipResponse":
        """<p>Deletes a membership, revoking a user's access to an agent space.</p>

        Args:
            application_id: <p>The unique identifier of the application that contains the agent space.</p>
            agent_space_id: <p>The unique identifier of the agent space to revoke access from.</p>
            membership_id: <p>The unique identifier of the membership to delete.</p>
            member_type: <p>The type of member to remove.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_membership_request.DeleteMembershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_membership_response.DeleteMembershipResponse"
        ]:
            import capo_securityagent._operations.security_agent.delete_membership

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_membership.async_delete_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_membership_request.DeleteMembershipRequest = {
            "application_id": application_id,
            "agent_space_id": agent_space_id,
            "membership_id": membership_id,
        }
        if member_type is not None:
            input_["member_type"] = member_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_artifact(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_id: "capo_securityagent.types.artifact_id.ArtifactId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_artifact_output.GetArtifactOutput":
        """<p>Retrieves an artifact from an agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the artifact.</p>
            artifact_id: <p>The unique identifier of the artifact to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.get_artifact_input.GetArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.get_artifact_output.GetArtifactOutput"
        ]:
            import capo_securityagent._operations.security_agent.get_artifact

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.get_artifact.async_get_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.get_artifact_input.GetArtifactInput = {
            "agent_space_id": agent_space_id,
            "artifact_id": artifact_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_security_requirements(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        input: "capo_securityagent.types.import_source.ImportSource",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.import_security_requirements_output.ImportSecurityRequirementsOutput":
        """<p>Imports security requirements from uploaded documents into a customer managed security requirement pack. The import process asynchronously extracts and generates structured security requirements from the provided source files.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to import requirements into.</p>
            input: <p>The import source containing the documents to extract security requirements from.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota. Review your current usage and request a quota increase if needed.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.import_security_requirements_input.ImportSecurityRequirementsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.import_security_requirements_output.ImportSecurityRequirementsOutput"
        ]:
            import capo_securityagent._operations.security_agent.import_security_requirements

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.import_security_requirements.async_import_security_requirements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.import_security_requirements_input.ImportSecurityRequirementsInput = {
            "pack_id": pack_id,
            "input": input,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def initiate_provider_registration(
        self,
        provider: "capo_securityagent.types.provider.Provider",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        target_url: Optional["capo_securityagent.types.target_url.TargetUrl"] = None,
        organization_name: Optional[str] = None,
        client_id: Optional["capo_securityagent.types.client_id.ClientId"] = None,
        client_secret: Optional[
            "capo_securityagent.types.client_secret.ClientSecret"
        ] = None,
    ) -> "capo_securityagent.types.initiate_provider_registration_output.InitiateProviderRegistrationOutput":
        """<p>Initiates the OAuth registration flow with a third-party provider. Returns a redirect URL and CSRF state token for completing the authorization.</p>

        Args:
            provider: <p>The provider to initiate registration with.</p>
            target_url: <p>The HTTPS URL of a self-managed provider instance. Omit for SaaS providers.</p>
            organization_name: <p>The name of the organization to connect.</p>
            client_id: <p>The client ID of the OAuth application registered on your self-managed provider instance.</p>
            client_secret: <p>The client secret of the OAuth application registered on your self-managed provider instance.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.initiate_provider_registration_input.InitiateProviderRegistrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.initiate_provider_registration_output.InitiateProviderRegistrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.initiate_provider_registration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.initiate_provider_registration.async_initiate_provider_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.initiate_provider_registration_input.InitiateProviderRegistrationInput = {
            "provider": provider
        }
        if target_url is not None:
            input_["target_url"] = target_url
        if organization_name is not None:
            input_["organization_name"] = organization_name
        if client_id is not None:
            input_["client_id"] = client_id
        if client_secret is not None:
            input_["client_secret"] = client_secret

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_actor_messages(
        self,
        agent_space_id: str,
        pentest_id: str,
        actor_identifier: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_actor_messages_output.ListActorMessagesOutput":
        """<p>Returns a paginated list of the email MFA messages received for an actor at its server-generated email address, most recent first.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            agent_space_id: <p>The unique identifier of the agent space that owns the pentest.</p>
            pentest_id: <p>The unique identifier of the pentest that the actor belongs to.</p>
            actor_identifier: <p>The identifier of the actor whose messages to list. The identifier is case-insensitive.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_actor_messages_input.ListActorMessagesInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_actor_messages_output.ListActorMessagesOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_actor_messages

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_actor_messages.async_list_actor_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_actor_messages_input.ListActorMessagesInput = {
            "agent_space_id": agent_space_id,
            "pentest_id": pentest_id,
            "actor_identifier": actor_identifier,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_actor_messages(
        self,
        agent_space_id: str,
        pentest_id: str,
        actor_identifier: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.actor_message.ActorMessage]":
        _token = next_token
        while True:
            _response = await self.list_actor_messages(
                agent_space_id,
                pentest_id,
                actor_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("messages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_artifacts(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_artifacts_output.ListArtifactsOutput":
        """<p>Returns a paginated list of artifact summaries for the specified agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to list artifacts for.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_artifacts_input.ListArtifactsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_artifacts_output.ListArtifactsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_artifacts

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_artifacts.async_list_artifacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_artifacts_input.ListArtifactsInput = {
            "agent_space_id": agent_space_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_artifacts(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.artifact_summary.ArtifactSummary]":
        _token = next_token
        while True:
            _response = await self.list_artifacts(
                agent_space_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("artifact_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_code_review_jobs_for_code_review(
        self,
        code_review_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_code_review_jobs_for_code_review_output.ListCodeReviewJobsForCodeReviewOutput":
        """<p>Returns a paginated list of code review job summaries for the specified code review configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            code_review_id: <p>The unique identifier of the code review to list jobs for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_code_review_jobs_for_code_review_input.ListCodeReviewJobsForCodeReviewInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_code_review_jobs_for_code_review_output.ListCodeReviewJobsForCodeReviewOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_code_review_jobs_for_code_review

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_code_review_jobs_for_code_review.async_list_code_review_jobs_for_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_code_review_jobs_for_code_review_input.ListCodeReviewJobsForCodeReviewInput = {
            "code_review_id": code_review_id,
            "agent_space_id": agent_space_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_code_review_jobs_for_code_review(
        self,
        code_review_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.code_review_job_summary.CodeReviewJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_code_review_jobs_for_code_review(
                code_review_id,
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("code_review_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_code_review_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        code_review_job_id: Optional[str] = None,
        step_name: Optional["capo_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_code_review_job_tasks_output.ListCodeReviewJobTasksOutput":
        """<p>Returns a paginated list of task summaries for the specified code review job, optionally filtered by step name or category.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            code_review_job_id: <p>The unique identifier of the code review job to list tasks for.</p>
            step_name: <p>Filter tasks by step name.</p>
            category_name: <p>Filter tasks by category name.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_code_review_job_tasks_input.ListCodeReviewJobTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_code_review_job_tasks_output.ListCodeReviewJobTasksOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_code_review_job_tasks

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_code_review_job_tasks.async_list_code_review_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_code_review_job_tasks_input.ListCodeReviewJobTasksInput = {
            "agent_space_id": agent_space_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if code_review_job_id is not None:
            input_["code_review_job_id"] = code_review_job_id
        if step_name is not None:
            input_["step_name"] = step_name
        if category_name is not None:
            input_["category_name"] = category_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_code_review_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        code_review_job_id: Optional[str] = None,
        step_name: Optional["capo_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.code_review_job_task_summary.CodeReviewJobTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_code_review_job_tasks(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                code_review_job_id=code_review_job_id,
                step_name=step_name,
                category_name=category_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("code_review_job_task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_code_reviews(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_code_reviews_output.ListCodeReviewsOutput":
        """<p>Returns a paginated list of code review summaries for the specified agent space.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            agent_space_id: <p>The unique identifier of the agent space to list code reviews for.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_code_reviews_input.ListCodeReviewsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_code_reviews_output.ListCodeReviewsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_code_reviews

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_code_reviews.async_list_code_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_code_reviews_input.ListCodeReviewsInput = {
            "agent_space_id": agent_space_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_code_reviews(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[capo_securityagent.types.code_review_summary.CodeReviewSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_code_reviews(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("code_review_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_discovered_endpoints(
        self,
        pentest_job_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        prefix: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_discovered_endpoints_output.ListDiscoveredEndpointsOutput":
        """<p>Returns a paginated list of endpoints discovered during a pentest job execution.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to list discovered endpoints for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            prefix: <p>A prefix to filter discovered endpoints by URI.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_discovered_endpoints_input.ListDiscoveredEndpointsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_discovered_endpoints_output.ListDiscoveredEndpointsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_discovered_endpoints

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_discovered_endpoints.async_list_discovered_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_discovered_endpoints_input.ListDiscoveredEndpointsInput = {
            "pentest_job_id": pentest_job_id,
            "agent_space_id": agent_space_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if prefix is not None:
            input_["prefix"] = prefix
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_discovered_endpoints(
        self,
        pentest_job_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        prefix: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[capo_securityagent.types.discovered_endpoint.DiscoveredEndpoint]"
    ):
        _token = next_token
        while True:
            _response = await self.list_discovered_endpoints(
                pentest_job_id,
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                prefix=prefix,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("discovered_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_findings(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        pentest_job_id: Optional[str] = None,
        code_review_job_id: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        risk_type: Optional[str] = None,
        risk_level: Optional["capo_securityagent.types.risk_level.RiskLevel"] = None,
        status: Optional[
            "capo_securityagent.types.finding_status.FindingStatus"
        ] = None,
        confidence: Optional[
            "capo_securityagent.types.confidence_level.ConfidenceLevel"
        ] = None,
        name: Optional[str] = None,
    ) -> "capo_securityagent.types.list_findings_output.ListFindingsOutput":
        """<p>Lists the security findings for a pentest job.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to list findings for.</p>
            code_review_job_id: <p>The unique identifier of the code review job to list findings for. Mutually exclusive with pentestJobId.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            risk_type: <p>Filter findings by risk type.</p>
            risk_level: <p>Filter findings by risk level.</p>
            status: <p>Filter findings by status.</p>
            confidence: <p>Filter findings by confidence level.</p>
            name: <p>Filter findings by name.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_findings_input.ListFindingsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_findings_output.ListFindingsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_findings

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_findings.async_list_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_findings_input.ListFindingsInput = {
            "agent_space_id": agent_space_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if pentest_job_id is not None:
            input_["pentest_job_id"] = pentest_job_id
        if code_review_job_id is not None:
            input_["code_review_job_id"] = code_review_job_id
        if next_token is not None:
            input_["next_token"] = next_token
        if risk_type is not None:
            input_["risk_type"] = risk_type
        if risk_level is not None:
            input_["risk_level"] = risk_level
        if status is not None:
            input_["status"] = status
        if confidence is not None:
            input_["confidence"] = confidence
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_findings(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        pentest_job_id: Optional[str] = None,
        code_review_job_id: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        risk_type: Optional[str] = None,
        risk_level: Optional["capo_securityagent.types.risk_level.RiskLevel"] = None,
        status: Optional[
            "capo_securityagent.types.finding_status.FindingStatus"
        ] = None,
        confidence: Optional[
            "capo_securityagent.types.confidence_level.ConfidenceLevel"
        ] = None,
        name: Optional[str] = None,
    ) -> "AsyncIterator[capo_securityagent.types.finding_summary.FindingSummary]":
        _token = next_token
        while True:
            _response = await self.list_findings(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                pentest_job_id=pentest_job_id,
                code_review_job_id=code_review_job_id,
                next_token=_token,
                risk_type=risk_type,
                risk_level=risk_level,
                status=status,
                confidence=confidence,
                name=name,
            )
            _page = _resolve_path(_response, ("findings_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_integrated_resources(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        integration_id: Optional[
            "capo_securityagent.types.integration_id.IntegrationId"
        ] = None,
        resource_type: Optional[
            "capo_securityagent.types.resource_type.ResourceType"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_integrated_resources_output.ListIntegratedResourcesOutput":
        """<p>Lists the integrated resources for an agent space, optionally filtered by integration or resource type.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to list integrated resources for.</p>
            integration_id: <p>The unique identifier of the integration to filter by.</p>
            resource_type: <p>The type of resource to filter by.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_integrated_resources_input.ListIntegratedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_integrated_resources_output.ListIntegratedResourcesOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_integrated_resources

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_integrated_resources.async_list_integrated_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_integrated_resources_input.ListIntegratedResourcesInput = {
            "agent_space_id": agent_space_id
        }
        if integration_id is not None:
            input_["integration_id"] = integration_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_integrated_resources(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        integration_id: Optional[
            "capo_securityagent.types.integration_id.IntegrationId"
        ] = None,
        resource_type: Optional[
            "capo_securityagent.types.resource_type.ResourceType"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.integrated_resource_summary.IntegratedResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_integrated_resources(
                agent_space_id,
                config_overrides=config_overrides,
                integration_id=integration_id,
                resource_type=resource_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("integrated_resource_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_memberships(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        member_type: Optional[
            "capo_securityagent.types.membership_type_filter.MembershipTypeFilter"
        ] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_memberships_response.ListMembershipsResponse":
        """<p>Returns a paginated list of membership summaries for the specified agent space within an application.</p>

        Args:
            application_id: <p>The unique identifier of the application that contains the agent space.</p>
            agent_space_id: <p>The unique identifier of the agent space to list memberships for.</p>
            member_type: <p>Filter memberships by member type.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_memberships_request.ListMembershipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_memberships_response.ListMembershipsResponse"
        ]:
            import capo_securityagent._operations.security_agent.list_memberships

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_memberships.async_list_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_memberships_request.ListMembershipsRequest = {
            "application_id": application_id,
            "agent_space_id": agent_space_id,
        }
        if member_type is not None:
            input_["member_type"] = member_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_memberships(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        member_type: Optional[
            "capo_securityagent.types.membership_type_filter.MembershipTypeFilter"
        ] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.membership_summary.MembershipSummary]":
        _token = next_token
        while True:
            _response = await self.list_memberships(
                application_id,
                agent_space_id,
                config_overrides=config_overrides,
                member_type=member_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("membership_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pentest_jobs_for_pentest(
        self,
        pentest_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        job_type: Optional["capo_securityagent.types.job_type.JobType"] = None,
    ) -> "capo_securityagent.types.list_pentest_jobs_for_pentest_output.ListPentestJobsForPentestOutput":
        """<p>Returns a paginated list of pentest job summaries for the specified pentest configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_id: <p>The unique identifier of the pentest to list jobs for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            job_type: <p>Filters the returned pentest jobs to only those of the specified job type.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_pentest_jobs_for_pentest_input.ListPentestJobsForPentestInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_pentest_jobs_for_pentest_output.ListPentestJobsForPentestOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_pentest_jobs_for_pentest

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_pentest_jobs_for_pentest.async_list_pentest_jobs_for_pentest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_pentest_jobs_for_pentest_input.ListPentestJobsForPentestInput = {
            "pentest_id": pentest_id,
            "agent_space_id": agent_space_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if job_type is not None:
            input_["job_type"] = job_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_pentest_jobs_for_pentest(
        self,
        pentest_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        job_type: Optional["capo_securityagent.types.job_type.JobType"] = None,
    ) -> (
        "AsyncIterator[capo_securityagent.types.pentest_job_summary.PentestJobSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_pentest_jobs_for_pentest(
                pentest_id,
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                job_type=job_type,
            )
            _page = _resolve_path(_response, ("pentest_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pentest_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        pentest_job_id: Optional[str] = None,
        step_name: Optional["capo_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_pentest_job_tasks_output.ListPentestJobTasksOutput":
        """<p>Returns a paginated list of task summaries for the specified pentest job, optionally filtered by step name or category.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to list tasks for.</p>
            step_name: <p>Filter tasks by step name. Valid values include PREFLIGHT, STATIC_ANALYSIS, PENTEST, VALIDATION, and FINALIZING.</p>
            category_name: <p>Filter tasks by category name.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_pentest_job_tasks_input.ListPentestJobTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_pentest_job_tasks_output.ListPentestJobTasksOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_pentest_job_tasks

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_pentest_job_tasks.async_list_pentest_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_pentest_job_tasks_input.ListPentestJobTasksInput = {
            "agent_space_id": agent_space_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if pentest_job_id is not None:
            input_["pentest_job_id"] = pentest_job_id
        if step_name is not None:
            input_["step_name"] = step_name
        if category_name is not None:
            input_["category_name"] = category_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_pentest_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        pentest_job_id: Optional[str] = None,
        step_name: Optional["capo_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.task_summary.TaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_pentest_job_tasks(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                pentest_job_id=pentest_job_id,
                step_name=step_name,
                category_name=category_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pentests(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_pentests_output.ListPentestsOutput":
        """<p>Returns a paginated list of pentest summaries for the specified agent space.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            agent_space_id: <p>The unique identifier of the agent space to list pentests for.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_pentests_input.ListPentestsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_pentests_output.ListPentestsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_pentests

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_pentests.async_list_pentests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_pentests_input.ListPentestsInput = {
            "agent_space_id": agent_space_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_pentests(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.pentest_summary.PentestSummary]":
        _token = next_token
        while True:
            _response = await self.list_pentests(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pentest_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_security_requirements(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_security_requirements_output.ListSecurityRequirementsOutput":
        """<p>Lists security requirements within a pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to list requirements for.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single request.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_security_requirements_input.ListSecurityRequirementsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_security_requirements_output.ListSecurityRequirementsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_security_requirements

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_security_requirements.async_list_security_requirements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_security_requirements_input.ListSecurityRequirementsInput = {
            "pack_id": pack_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_security_requirements(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.security_requirement_summary.SecurityRequirementSummary]":
        _token = next_token
        while True:
            _response = await self.list_security_requirements(
                pack_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("security_requirement_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_securityagent.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns the tags associated with the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_threat_model_jobs(
        self,
        threat_model_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_threat_model_jobs_output.ListThreatModelJobsOutput":
        """<p>Returns a paginated list of threat model job summaries for the specified threat model.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            threat_model_id: <p>The unique identifier of the threat model to list jobs for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_threat_model_jobs_input.ListThreatModelJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_threat_model_jobs_output.ListThreatModelJobsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_threat_model_jobs

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_threat_model_jobs.async_list_threat_model_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_threat_model_jobs_input.ListThreatModelJobsInput = {
            "threat_model_id": threat_model_id,
            "agent_space_id": agent_space_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_threat_model_jobs(
        self,
        threat_model_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.threat_model_job_summary.ThreatModelJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_threat_model_jobs(
                threat_model_id,
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("threat_model_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_threat_model_job_tasks(
        self,
        agent_space_id: str,
        threat_model_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_threat_model_job_tasks_output.ListThreatModelJobTasksOutput":
        """<p>Returns a paginated list of task summaries for the specified threat model job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            threat_model_job_id: <p>The unique identifier of the threat model job to list tasks for.</p>
            next_token: <p>A token to use for paginating results that are returned in the response.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_threat_model_job_tasks_input.ListThreatModelJobTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_threat_model_job_tasks_output.ListThreatModelJobTasksOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_threat_model_job_tasks

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_threat_model_job_tasks.async_list_threat_model_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_threat_model_job_tasks_input.ListThreatModelJobTasksInput = {
            "agent_space_id": agent_space_id,
            "threat_model_job_id": threat_model_job_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_threat_model_job_tasks(
        self,
        agent_space_id: str,
        threat_model_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.threat_model_job_task_summary.ThreatModelJobTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_threat_model_job_tasks(
                agent_space_id,
                threat_model_job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("threat_model_job_task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_threat_models(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_threat_models_output.ListThreatModelsOutput":
        """<p>Returns a paginated list of threat model summaries for the specified agent space.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response.</p>
            agent_space_id: <p>The unique identifier of the agent space to list threat models for.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_threat_models_input.ListThreatModelsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_threat_models_output.ListThreatModelsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_threat_models

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_threat_models.async_list_threat_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_threat_models_input.ListThreatModelsInput = {
            "agent_space_id": agent_space_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_threat_models(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.threat_model_summary.ThreatModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_threat_models(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("threat_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_threats(
        self,
        threat_job_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_threats_output.ListThreatsOutput":
        """<p>Returns a paginated list of threats for a threat model job.</p>

        Args:
            threat_job_id: <p>The unique identifier of the threat model job to list threats for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_threats_input.ListThreatsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_threats_output.ListThreatsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_threats

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_threats.async_list_threats(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_threats_input.ListThreatsInput = {
            "threat_job_id": threat_job_id,
            "agent_space_id": agent_space_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_threats(
        self,
        threat_job_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.threat_summary.ThreatSummary]":
        _token = next_token
        while True:
            _response = await self.list_threats(
                threat_job_id,
                agent_space_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("threats",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_code_remediation(
        self,
        agent_space_id: str,
        finding_ids: "capo_securityagent.types.finding_id_list.FindingIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        pentest_job_id: Optional[str] = None,
        code_review_job_id: Optional[str] = None,
    ) -> "capo_securityagent.types.start_code_remediation_output.StartCodeRemediationOutput":
        """<p>Initiates code remediation for one or more security findings. This creates pull requests in integrated repositories to fix the identified vulnerabilities.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            pentest_job_id: <p>The unique identifier of the pentest job that produced the findings. Mutually exclusive with <code>codeReviewJobId</code>.</p>
            code_review_job_id: <p>The unique identifier of the code review job that produced the findings. Mutually exclusive with <code>pentestJobId</code>.</p>
            finding_ids: <p>The list of finding identifiers to initiate code remediation for.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.start_code_remediation_input.StartCodeRemediationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.start_code_remediation_output.StartCodeRemediationOutput"
        ]:
            import capo_securityagent._operations.security_agent.start_code_remediation

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.start_code_remediation.async_start_code_remediation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.start_code_remediation_input.StartCodeRemediationInput = {
            "agent_space_id": agent_space_id,
            "finding_ids": finding_ids,
        }
        if pentest_job_id is not None:
            input_["pentest_job_id"] = pentest_job_id
        if code_review_job_id is not None:
            input_["code_review_job_id"] = code_review_job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_code_review_job(
        self,
        agent_space_id: str,
        code_review_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        diff_source: Optional["capo_securityagent.types.diff_source.DiffSource"] = None,
    ) -> (
        "capo_securityagent.types.start_code_review_job_output.StartCodeReviewJobOutput"
    ):
        """<p>Starts a new code review job for a code review configuration. The job executes the security-focused code analysis defined in the code review.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            code_review_id: <p>The unique identifier of the code review to start a job for.</p>
            diff_source: <p>Source of the diff for a differential scan. When present, the job analyzes only the changed lines instead of performing a full scan.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.start_code_review_job_input.StartCodeReviewJobInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.start_code_review_job_output.StartCodeReviewJobOutput"
        ]:
            import capo_securityagent._operations.security_agent.start_code_review_job

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.start_code_review_job.async_start_code_review_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.start_code_review_job_input.StartCodeReviewJobInput = {
            "agent_space_id": agent_space_id,
            "code_review_id": code_review_id,
        }
        if diff_source is not None:
            input_["diff_source"] = diff_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_pentest_job(
        self,
        agent_space_id: str,
        pentest_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        job_type: Optional["capo_securityagent.types.job_type.JobType"] = None,
        selected_finding_ids: Optional[
            "capo_securityagent.types.string_list.StringList"
        ] = None,
        scope_changes: Optional[
            "capo_securityagent.types.scope_change_list.ScopeChangeList"
        ] = None,
    ) -> "capo_securityagent.types.start_pentest_job_output.StartPentestJobOutput":
        """<p>Starts a new pentest job for a pentest configuration. The job executes the security tests defined in the pentest.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            pentest_id: <p>The unique identifier of the pentest to start a job for.</p>
            job_type: <p>The type of pentest job to start. Valid values are FULL, REVALIDATION, and CICD. When set to REVALIDATION, the selectedFindingIds parameter is required. When set to CICD, the scopeChanges parameter defines the code changes to test.</p>
            selected_finding_ids: <p>The list of finding identifiers to revalidate. Required when jobType is REVALIDATION. Each finding must belong to the same agent space and pentest.</p>
            scope_changes: <p>The code changes that define the scope of a CI/CD pentest job. Provide this when starting a job with jobType CICD to test only the changes in the current pipeline run.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.start_pentest_job_input.StartPentestJobInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.start_pentest_job_output.StartPentestJobOutput"
        ]:
            import capo_securityagent._operations.security_agent.start_pentest_job

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.start_pentest_job.async_start_pentest_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.start_pentest_job_input.StartPentestJobInput = {
            "agent_space_id": agent_space_id,
            "pentest_id": pentest_id,
        }
        if job_type is not None:
            input_["job_type"] = job_type
        if selected_finding_ids is not None:
            input_["selected_finding_ids"] = selected_finding_ids
        if scope_changes is not None:
            input_["scope_changes"] = scope_changes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_threat_model_job(
        self,
        agent_space_id: str,
        threat_model_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.start_threat_model_job_output.StartThreatModelJobOutput":
        """<p>Starts a new threat model job for a threat model configuration.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            threat_model_id: <p>The unique identifier of the threat model to start a job for.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.start_threat_model_job_input.StartThreatModelJobInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.start_threat_model_job_output.StartThreatModelJobOutput"
        ]:
            import capo_securityagent._operations.security_agent.start_threat_model_job

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.start_threat_model_job.async_start_threat_model_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.start_threat_model_job_input.StartThreatModelJobInput = {
            "agent_space_id": agent_space_id,
            "threat_model_id": threat_model_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_code_review_job(
        self,
        agent_space_id: str,
        code_review_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.stop_code_review_job_output.StopCodeReviewJobOutput":
        """<p>Stops a running code review job. The job transitions to a stopping state and then to stopped after cleanup completes.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            code_review_job_id: <p>The unique identifier of the code review job to stop.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.stop_code_review_job_input.StopCodeReviewJobInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.stop_code_review_job_output.StopCodeReviewJobOutput"
        ]:
            import capo_securityagent._operations.security_agent.stop_code_review_job

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.stop_code_review_job.async_stop_code_review_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.stop_code_review_job_input.StopCodeReviewJobInput = {
            "agent_space_id": agent_space_id,
            "code_review_job_id": code_review_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_pentest_job(
        self,
        agent_space_id: str,
        pentest_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.stop_pentest_job_output.StopPentestJobOutput":
        """<p>Stops a running pentest job. The job transitions to a stopping state and then to stopped after cleanup completes.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to stop.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.stop_pentest_job_input.StopPentestJobInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.stop_pentest_job_output.StopPentestJobOutput"
        ]:
            import capo_securityagent._operations.security_agent.stop_pentest_job

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.stop_pentest_job.async_stop_pentest_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.stop_pentest_job_input.StopPentestJobInput = {
            "agent_space_id": agent_space_id,
            "pentest_job_id": pentest_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_threat_model_job(
        self,
        agent_space_id: str,
        threat_model_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> (
        "capo_securityagent.types.stop_threat_model_job_output.StopThreatModelJobOutput"
    ):
        """<p>Stops a running threat model job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            threat_model_job_id: <p>The unique identifier of the threat model job to stop.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.stop_threat_model_job_input.StopThreatModelJobInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.stop_threat_model_job_output.StopThreatModelJobOutput"
        ]:
            import capo_securityagent._operations.security_agent.stop_threat_model_job

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.stop_threat_model_job.async_stop_threat_model_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.stop_threat_model_job_input.StopThreatModelJobInput = {
            "agent_space_id": agent_space_id,
            "threat_model_job_id": threat_model_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_securityagent.types.resource_arn.ResourceArn",
        tags: "capo_securityagent.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.tag_resource_output.TagResourceOutput":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The tags to add to the resource.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_securityagent._operations.security_agent.tag_resource

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_securityagent.types.resource_arn.ResourceArn",
        tag_keys: "capo_securityagent.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_securityagent._operations.security_agent.untag_resource

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_code_review(
        self,
        code_review_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        title: Optional[str] = None,
        assets: Optional["capo_securityagent.types.assets.Assets"] = None,
        service_role: Optional[
            "capo_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "capo_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        code_remediation_strategy: Optional[
            "capo_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
        validation_mode: Optional[
            "capo_securityagent.types.validation_mode.ValidationMode"
        ] = None,
        max_task_hours: Optional[float] = None,
        report_destination: Optional[
            "capo_securityagent.types.report_destination.ReportDestination"
        ] = None,
        report_filters: Optional[
            "capo_securityagent.types.report_filters.ReportFilters"
        ] = None,
    ) -> "capo_securityagent.types.update_code_review_output.UpdateCodeReviewOutput":
        """<p>Updates an existing code review configuration.</p>

        Args:
            code_review_id: <p>The unique identifier of the code review to update.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code review.</p>
            title: <p>The updated title of the code review.</p>
            assets: <p>The updated assets for the code review.</p>
            service_role: <p>The updated IAM service role for the code review.</p>
            log_config: <p>The updated CloudWatch Logs configuration for the code review.</p>
            code_remediation_strategy: <p>The updated code remediation strategy for the code review.</p>
            validation_mode: <p>The updated validation mode for the code review. Valid values are SIMULATED and DISABLED.</p>
            max_task_hours: <p>The updated maximum number of billable task hours allowed for jobs started from this code review.</p>
            report_destination: <p>The destination for publishing scan reports to an integrated document provider.</p>
            report_filters: <p>The report-generation filters applied when the report is exported.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_code_review_input.UpdateCodeReviewInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_code_review_output.UpdateCodeReviewOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_code_review

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_code_review.async_update_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_code_review_input.UpdateCodeReviewInput = {
            "code_review_id": code_review_id,
            "agent_space_id": agent_space_id,
        }
        if title is not None:
            input_["title"] = title
        if assets is not None:
            input_["assets"] = assets
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy
        if validation_mode is not None:
            input_["validation_mode"] = validation_mode
        if max_task_hours is not None:
            input_["max_task_hours"] = max_task_hours
        if report_destination is not None:
            input_["report_destination"] = report_destination
        if report_filters is not None:
            input_["report_filters"] = report_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_finding(
        self,
        finding_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        risk_type: Optional[str] = None,
        risk_level: Optional["capo_securityagent.types.risk_level.RiskLevel"] = None,
        risk_score: Optional[str] = None,
        attack_script: Optional[str] = None,
        reasoning: Optional[str] = None,
        status: Optional[
            "capo_securityagent.types.finding_status.FindingStatus"
        ] = None,
        customer_note: Optional[str] = None,
    ) -> "capo_securityagent.types.update_finding_output.UpdateFindingOutput":
        """<p>Updates the status or risk level of a security finding.</p>

        Args:
            finding_id: <p>The unique identifier of the finding to update.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the finding.</p>
            name: <p>The updated name for the finding.</p>
            description: <p>The updated description for the finding.</p>
            risk_type: <p>The updated risk type for the finding.</p>
            risk_level: <p>The updated risk level for the finding.</p>
            risk_score: <p>The updated numerical risk score for the finding.</p>
            attack_script: <p>The updated attack script for the finding.</p>
            reasoning: <p>The updated reasoning for the finding.</p>
            status: <p>The updated status for the finding.</p>
            customer_note: <p>A customer-provided note on the finding.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_finding_input.UpdateFindingInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_finding_output.UpdateFindingOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_finding

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_finding.async_update_finding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_finding_input.UpdateFindingInput = {
            "finding_id": finding_id,
            "agent_space_id": agent_space_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if risk_type is not None:
            input_["risk_type"] = risk_type
        if risk_level is not None:
            input_["risk_level"] = risk_level
        if risk_score is not None:
            input_["risk_score"] = risk_score
        if attack_script is not None:
            input_["attack_script"] = attack_script
        if reasoning is not None:
            input_["reasoning"] = reasoning
        if status is not None:
            input_["status"] = status
        if customer_note is not None:
            input_["customer_note"] = customer_note

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_integrated_resources(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        items: "capo_securityagent.types.integrated_resource_input_item_list.IntegratedResourceInputItemList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.update_integrated_resources_output.UpdateIntegratedResourcesOutput":
        """<p>Updates the integrated resources for an agent space, including their capabilities.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            integration_id: <p>The unique identifier of the integration.</p>
            items: <p>The list of integrated resource items to update.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_integrated_resources_input.UpdateIntegratedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_integrated_resources_output.UpdateIntegratedResourcesOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_integrated_resources

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_integrated_resources.async_update_integrated_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_integrated_resources_input.UpdateIntegratedResourcesInput = {
            "agent_space_id": agent_space_id,
            "integration_id": integration_id,
            "items": items,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_pentest(
        self,
        pentest_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        title: Optional[str] = None,
        assets: Optional["capo_securityagent.types.assets.Assets"] = None,
        exclude_risk_types: Optional[
            "capo_securityagent.types.risk_type_list.RiskTypeList"
        ] = None,
        service_role: Optional[
            "capo_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "capo_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        vpc_config: Optional["capo_securityagent.types.vpc_config.VpcConfig"] = None,
        network_traffic_config: Optional[
            "capo_securityagent.types.network_traffic_config.NetworkTrafficConfig"
        ] = None,
        code_remediation_strategy: Optional[
            "capo_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
        disable_managed_skills: Optional[
            "capo_securityagent.types.skill_type_list.SkillTypeList"
        ] = None,
        max_task_hours: Optional[float] = None,
        report_destination: Optional[
            "capo_securityagent.types.report_destination.ReportDestination"
        ] = None,
        report_filters: Optional[
            "capo_securityagent.types.report_filters.ReportFilters"
        ] = None,
        cicd_configuration: Optional[
            "capo_securityagent.types.ci_cd_configuration.CiCdConfiguration"
        ] = None,
    ) -> "capo_securityagent.types.update_pentest_output.UpdatePentestOutput":
        """<p>Updates an existing pentest configuration.</p>

        Args:
            pentest_id: <p>The unique identifier of the pentest to update.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentest.</p>
            title: <p>The updated title of the pentest.</p>
            assets: <p>The updated assets for the pentest.</p>
            exclude_risk_types: <p>The updated list of risk types to exclude from the pentest.</p>
            service_role: <p>The updated IAM service role for the pentest.</p>
            log_config: <p>The updated CloudWatch Logs configuration for the pentest.</p>
            vpc_config: <p>The updated VPC configuration for the pentest.</p>
            network_traffic_config: <p>The updated network traffic configuration for the pentest.</p>
            code_remediation_strategy: <p>The updated code remediation strategy for the pentest.</p>
            disable_managed_skills: <p>The updated list of managed skills to disable for this pentest. Valid values include FINDING_PERSONALIZATION and LOGIN_OPTIMIZATION.</p>
            max_task_hours: <p>The updated maximum number of billable task hours allowed for jobs started from this pentest.</p>
            report_destination: <p>The destination for publishing scan reports to an integrated document provider.</p>
            report_filters: <p>The report-generation filters applied when the report is exported.</p>
            cicd_configuration: <p>The updated CI/CD pentesting configuration to apply to the pentest.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_pentest_input.UpdatePentestInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_pentest_output.UpdatePentestOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_pentest

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_pentest.async_update_pentest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_pentest_input.UpdatePentestInput = {
            "pentest_id": pentest_id,
            "agent_space_id": agent_space_id,
        }
        if title is not None:
            input_["title"] = title
        if assets is not None:
            input_["assets"] = assets
        if exclude_risk_types is not None:
            input_["exclude_risk_types"] = exclude_risk_types
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if network_traffic_config is not None:
            input_["network_traffic_config"] = network_traffic_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy
        if disable_managed_skills is not None:
            input_["disable_managed_skills"] = disable_managed_skills
        if max_task_hours is not None:
            input_["max_task_hours"] = max_task_hours
        if report_destination is not None:
            input_["report_destination"] = report_destination
        if report_filters is not None:
            input_["report_filters"] = report_filters
        if cicd_configuration is not None:
            input_["cicd_configuration"] = cicd_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_threat(
        self,
        threat_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        title: Optional[str] = None,
        status: Optional["capo_securityagent.types.threat_status.ThreatStatus"] = None,
        comments: Optional[str] = None,
        statement: Optional[str] = None,
        severity: Optional[
            "capo_securityagent.types.threat_severity.ThreatSeverity"
        ] = None,
        threat_source: Optional[str] = None,
        prerequisites: Optional[str] = None,
        threat_action: Optional[str] = None,
        threat_impact: Optional[str] = None,
        impacted_goal: Optional[
            "capo_securityagent.types.string_list.StringList"
        ] = None,
        impacted_assets: Optional[
            "capo_securityagent.types.string_list.StringList"
        ] = None,
        anchor: Optional[
            "capo_securityagent.types.threat_anchor_shape.ThreatAnchorShape"
        ] = None,
        evidence: Optional[
            "capo_securityagent.types.threat_evidence_list.ThreatEvidenceList"
        ] = None,
        recommendation: Optional[str] = None,
    ) -> "capo_securityagent.types.update_threat_output.UpdateThreatOutput":
        """<p>Updates a threat.</p>

        Args:
            threat_id: <p>The unique identifier of the threat to update.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            title: <p>A short title summarizing the threat.</p>
            status: <p>The updated status of the threat.</p>
            comments: <p>Optional customer comment.</p>
            statement: <p>The updated natural-language threat statement.</p>
            severity: <p>The updated severity level of the threat.</p>
            threat_source: <p>The updated actor or origin of the threat.</p>
            prerequisites: <p>The updated conditions required for the threat to be exploitable.</p>
            threat_action: <p>The updated description of what the threat source can do.</p>
            threat_impact: <p>The updated direct consequence of the threat action.</p>
            impacted_goal: <p>The updated security goals affected by the threat.</p>
            impacted_assets: <p>The updated list of specific assets affected by the threat.</p>
            anchor: <p>The updated DFD element this threat is anchored to.</p>
            evidence: <p>The updated source code files supporting the threat.</p>
            recommendation: <p>The updated recommended mitigation guidance for this threat.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_threat_input.UpdateThreatInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_threat_output.UpdateThreatOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_threat

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_threat.async_update_threat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_threat_input.UpdateThreatInput = {
            "threat_id": threat_id,
            "agent_space_id": agent_space_id,
        }
        if title is not None:
            input_["title"] = title
        if status is not None:
            input_["status"] = status
        if comments is not None:
            input_["comments"] = comments
        if statement is not None:
            input_["statement"] = statement
        if severity is not None:
            input_["severity"] = severity
        if threat_source is not None:
            input_["threat_source"] = threat_source
        if prerequisites is not None:
            input_["prerequisites"] = prerequisites
        if threat_action is not None:
            input_["threat_action"] = threat_action
        if threat_impact is not None:
            input_["threat_impact"] = threat_impact
        if impacted_goal is not None:
            input_["impacted_goal"] = impacted_goal
        if impacted_assets is not None:
            input_["impacted_assets"] = impacted_assets
        if anchor is not None:
            input_["anchor"] = anchor
        if evidence is not None:
            input_["evidence"] = evidence
        if recommendation is not None:
            input_["recommendation"] = recommendation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_threat_model(
        self,
        threat_model_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        assets: Optional["capo_securityagent.types.assets.Assets"] = None,
        scope_docs: Optional[
            "capo_securityagent.types.document_list.DocumentList"
        ] = None,
        service_role: Optional[
            "capo_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "capo_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        report_destination: Optional[
            "capo_securityagent.types.report_destination.ReportDestination"
        ] = None,
    ) -> "capo_securityagent.types.update_threat_model_output.UpdateThreatModelOutput":
        """<p>Updates an existing threat model configuration.</p>

        Args:
            threat_model_id: <p>The unique identifier of the threat model to update.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the threat model.</p>
            title: <p>The updated title of the threat model.</p>
            description: <p>The updated description of the application or system being threat modeled.</p>
            assets: <p>The updated assets for the threat model.</p>
            scope_docs: <p>The updated scoped documents for the agent to focus on during threat modeling.</p>
            service_role: <p>The updated IAM service role for the threat model.</p>
            log_config: <p>The updated CloudWatch Logs configuration for the threat model.</p>
            report_destination: <p>The destination for publishing scan reports to an integrated document provider.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_threat_model_input.UpdateThreatModelInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_threat_model_output.UpdateThreatModelOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_threat_model

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_threat_model.async_update_threat_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_threat_model_input.UpdateThreatModelInput = {
            "threat_model_id": threat_model_id,
            "agent_space_id": agent_space_id,
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if assets is not None:
            input_["assets"] = assets
        if scope_docs is not None:
            input_["scope_docs"] = scope_docs
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if report_destination is not None:
            input_["report_destination"] = report_destination

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_target_domain(
        self,
        target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> (
        "capo_securityagent.types.verify_target_domain_output.VerifyTargetDomainOutput"
    ):
        """<p>Initiates verification of a target domain. This checks whether the domain ownership verification token has been properly configured.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to verify.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.verify_target_domain_input.VerifyTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.verify_target_domain_output.VerifyTargetDomainOutput"
        ]:
            import capo_securityagent._operations.security_agent.verify_target_domain

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.verify_target_domain.async_verify_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.verify_target_domain_input.VerifyTargetDomainInput = {
            "target_domain_id": target_domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_agent_space(
        self,
        name: "capo_securityagent.types.agent_name.AgentName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        description: Optional[str] = None,
        aws_resources: Optional[
            "capo_securityagent.types.aws_resources.AWSResources"
        ] = None,
        target_domain_ids: Optional[
            "capo_securityagent.types.target_domain_id_list.TargetDomainIdList"
        ] = None,
        code_review_settings: Optional[
            "capo_securityagent.types.code_review_settings.CodeReviewSettings"
        ] = None,
        kms_key_id: Optional["capo_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> "capo_securityagent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new agent space. An agent space is a dedicated workspace for securing a specific application.</p>

        Args:
            name: <p>The name of the agent space.</p>
            description: <p>A description of the agent space.</p>
            aws_resources: <p>The AWS resources to associate with the agent space.</p>
            target_domain_ids: <p>The list of target domain identifiers to associate with the agent space.</p>
            code_review_settings: <p>The code review settings for the agent space.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data in the agent space.</p>
            tags: <p>The tags to associate with the agent space.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_agent_space

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_agent_space.async_create_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_agent_space_input.CreateAgentSpaceInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if aws_resources is not None:
            input_["aws_resources"] = aws_resources
        if target_domain_ids is not None:
            input_["target_domain_ids"] = target_domain_ids
        if code_review_settings is not None:
            input_["code_review_settings"] = code_review_settings
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent_space(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        name: Optional["capo_securityagent.types.agent_name.AgentName"] = None,
        description: Optional[str] = None,
        aws_resources: Optional[
            "capo_securityagent.types.aws_resources.AWSResources"
        ] = None,
        target_domain_ids: Optional[
            "capo_securityagent.types.target_domain_id_list.TargetDomainIdList"
        ] = None,
        code_review_settings: Optional[
            "capo_securityagent.types.code_review_settings.CodeReviewSettings"
        ] = None,
    ) -> "capo_securityagent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the configuration of an existing agent space, including its name, description, AWS resources, target domains, and code review settings.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to update.</p>
            name: <p>The updated name of the agent space.</p>
            description: <p>The updated description of the agent space.</p>
            aws_resources: <p>The updated AWS resources to associate with the agent space.</p>
            target_domain_ids: <p>The updated list of target domain identifiers to associate with the agent space.</p>
            code_review_settings: <p>The updated code review settings for the agent space.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_agent_space

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_agent_space.async_update_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_agent_space_input.UpdateAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if aws_resources is not None:
            input_["aws_resources"] = aws_resources
        if target_domain_ids is not None:
            input_["target_domain_ids"] = target_domain_ids
        if code_review_settings is not None:
            input_["code_review_settings"] = code_review_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent_space(
        self,
        agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an agent space and all of its associated resources, including pentests, findings, and artifacts.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_agent_space

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_agent_space.async_delete_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_agent_space_input.DeleteAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_spaces(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Returns a paginated list of agent space summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_agent_spaces

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_agent_spaces.async_list_agent_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_agent_spaces_input.ListAgentSpacesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_agent_spaces(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_securityagent.types.agent_space_summary.AgentSpaceSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_agent_spaces(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("agent_space_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_get_agent_spaces(
        self,
        agent_space_ids: "capo_securityagent.types.agent_space_id_list.AgentSpaceIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_agent_spaces_output.BatchGetAgentSpacesOutput":
        """<p>Retrieves information about one or more agent spaces.</p>

        Args:
            agent_space_ids: <p>The list of agent space identifiers to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_agent_spaces_input.BatchGetAgentSpacesInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_agent_spaces_output.BatchGetAgentSpacesOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_agent_spaces

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_agent_spaces.async_batch_get_agent_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_agent_spaces_input.BatchGetAgentSpacesInput = {
            "agent_space_ids": agent_space_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_application(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        idc_instance_arn: Optional[
            "capo_securityagent.types.id_c_instance_arn.IdCInstanceArn"
        ] = None,
        role_arn: Optional["capo_securityagent.types.role_arn.RoleArn"] = None,
        default_kms_key_id: Optional[
            "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
        ] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_securityagent.types.create_application_response.CreateApplicationResponse"
    ):
        """<p>Creates a new application. An application is the top-level organizational unit that supports IAM Identity Center integration.</p>

        Args:
            idc_instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance to associate with the application.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to associate with the application.</p>
            default_kms_key_id: <p>The identifier of the default AWS KMS key to use for encrypting data in the application.</p>
            tags: <p>The tags to associate with the application.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.create_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_application_request.CreateApplicationRequest = {}
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if default_kms_key_id is not None:
            input_["default_kms_key_id"] = default_kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_application_response.GetApplicationResponse":
        """<p>Retrieves information about an application.</p>

        Args:
            application_id: <p>The unique identifier of the application to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.get_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        role_arn: Optional["capo_securityagent.types.role_arn.RoleArn"] = None,
        default_kms_key_id: Optional[
            "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
        ] = None,
    ) -> (
        "capo_securityagent.types.update_application_response.UpdateApplicationResponse"
    ):
        """<p>Updates the configuration of an existing application, including the IAM role and default KMS key.</p>

        Args:
            application_id: <p>The unique identifier of the application to update.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the application.</p>
            default_kms_key_id: <p>The updated identifier of the default AWS KMS key for the application.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.update_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if default_kms_key_id is not None:
            input_["default_kms_key_id"] = default_kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> None:
        """<p>Deletes an application and its associated configuration, including IAM Identity Center settings.</p>

        Args:
            application_id: <p>The unique identifier of the application to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_securityagent._operations.security_agent.delete_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_applications_response.ListApplicationsResponse":
        """<p>Returns a paginated list of application summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_securityagent._operations.security_agent.list_applications

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_securityagent.types.application_summary.ApplicationSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_integration(
        self,
        provider: "capo_securityagent.types.provider.Provider",
        input: "capo_securityagent.types.provider_input.ProviderInput",
        integration_display_name: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        kms_key_id: Optional["capo_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
        private_connection_name: Optional[
            "capo_securityagent.types.private_connection_name.PrivateConnectionName"
        ] = None,
    ) -> "capo_securityagent.types.create_integration_output.CreateIntegrationOutput":
        """<p>Creates a new integration with a third-party provider, such as GitHub, for code review and remediation.</p>

        Args:
            provider: <p>The integration provider.</p>
            input: <p>The provider-specific input required to create the integration.</p>
            integration_display_name: <p>The display name for the integration.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data associated with the integration.</p>
            tags: <p>The tags to associate with the integration.</p>
            private_connection_name: <p>The name of an active private connection used to reach a self-hosted provider instance over private networking. Specify this when the instance is not publicly reachable.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_integration_input.CreateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_integration_input.CreateIntegrationInput = {
            "provider": provider,
            "input": input,
            "integration_display_name": integration_display_name,
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_integration(
        self,
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_integration_output.GetIntegrationOutput":
        """<p>Retrieves information about an integration.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.get_integration_input.GetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.get_integration_output.GetIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.get_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.get_integration.async_get_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.get_integration_input.GetIntegrationInput = {
            "integration_id": integration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_integration(
        self,
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        webhook_action: "capo_securityagent.types.webhook_action.WebhookAction",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.update_integration_output.UpdateIntegrationOutput":
        """<p>Creates an integration's webhook, or rotates the HMAC signing secret of an existing one. The secret is returned only once, in this response, and cannot be retrieved again.</p>

        Args:
            integration_id: <p>The ID of the integration whose webhook you want to create or rotate.</p>
            webhook_action: <p>The action to perform on the integration's webhook.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_integration_input.UpdateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_integration_output.UpdateIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_integration.async_update_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_integration_input.UpdateIntegrationInput = {
            "integration_id": integration_id,
            "webhook_action": webhook_action,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_integration(
        self,
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_integration_output.DeleteIntegrationOutput":
        """<p>Deletes an integration with a third-party provider.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_integration_output.DeleteIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_integration_input.DeleteIntegrationInput = {
            "integration_id": integration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_integrations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.integration_filter.IntegrationFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_integrations_output.ListIntegrationsOutput":
        """<p>Lists the integrations in your account, optionally filtered by provider or provider type.</p>

        Args:
            filter: <p>A filter to apply to the list of integrations.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_integrations_input.ListIntegrationsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_integrations

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_integrations.async_list_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_integrations_input.ListIntegrationsInput = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_integrations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.integration_filter.IntegrationFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_securityagent.types.integration_summary.IntegrationSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_integrations(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("integration_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_private_connection(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves the details of a private connection.</p>

        Args:
            private_connection_name: <p>The name of the private connection to describe.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.describe_private_connection

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.describe_private_connection.async_describe_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.describe_private_connection_input.DescribePrivateConnectionInput = {
            "private_connection_name": private_connection_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_private_connection(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a private connection.</p>

        Args:
            private_connection_name: <p>The name of the private connection to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_private_connection

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_private_connection.async_delete_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_private_connection_input.DeletePrivateConnectionInput = {
            "private_connection_name": private_connection_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_private_connections(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists the private connections in your account.</p>

        Args:
            max_results: <p>The maximum number of private connections to return in a single response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_private_connections

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_private_connections.async_list_private_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_private_connections_input.ListPrivateConnectionsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_private_connections(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.private_connection_summary.PrivateConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_private_connections(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("private_connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_private_connection(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        mode: "capo_securityagent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> "capo_securityagent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a private connection for reaching a self-hosted provider instance over private networking using Amazon VPC Lattice.</p>

        Args:
            private_connection_name: <p>A unique name for the private connection within your account.</p>
            mode: <p>The configuration for the private connection. Specify either a service-managed or a self-managed mode.</p>
            tags: <p>The tags to attach to the private connection.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_private_connection

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_private_connection.async_create_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput = {
            "private_connection_name": private_connection_name,
            "mode": mode,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_private_connection_certificate(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        certificate: "capo_securityagent.types.certificate_chain.CertificateChain",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a private connection. Certificates can be added or replaced but not removed.</p>

        Args:
            private_connection_name: <p>The name of the private connection to update.</p>
            certificate: <p>The PEM-encoded certificate chain for the private connection.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_private_connection_certificate

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_private_connection_certificate.async_update_private_connection_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {
            "private_connection_name": private_connection_name,
            "certificate": certificate,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_security_requirement_pack(
        self,
        name: "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        description: Optional[str] = None,
        status: Optional[
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
        ] = None,
        kms_key_id: Optional["capo_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> "capo_securityagent.types.create_security_requirement_pack_output.CreateSecurityRequirementPackOutput":
        """<p>Creates a customer managed security requirement pack.</p>

        Args:
            name: <p>The name of the security requirement pack.</p>
            description: <p>A description of the security requirement pack.</p>
            status: <p>The status of the pack. Defaults to ENABLED if not provided.</p>
            kms_key_id: <p>The identifier of the AWS KMS key used to encrypt pack contents.</p>
            tags: <p>The tags to associate with the security requirement pack.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota. Review your current usage and request a quota increase if needed.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_security_requirement_pack_input.CreateSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_security_requirement_pack_output.CreateSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_security_requirement_pack.async_create_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_security_requirement_pack_input.CreateSecurityRequirementPackInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_security_requirement_pack(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_security_requirement_pack_output.GetSecurityRequirementPackOutput":
        """<p>Retrieves information about a security requirement pack.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.get_security_requirement_pack_input.GetSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.get_security_requirement_pack_output.GetSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.get_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.get_security_requirement_pack.async_get_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.get_security_requirement_pack_input.GetSecurityRequirementPackInput = {
            "pack_id": pack_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_security_requirement_pack(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        name: Optional[
            "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName"
        ] = None,
        description: Optional[str] = None,
        status: Optional[
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
        ] = None,
    ) -> "capo_securityagent.types.update_security_requirement_pack_output.UpdateSecurityRequirementPackOutput":
        """<p>Updates a security requirement pack. For customer managed packs, both metadata and status can be updated. For AWS managed packs, only status can be updated.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to update.</p>
            name: <p>The updated name of the security requirement pack.</p>
            description: <p>The updated description of the security requirement pack.</p>
            status: <p>The updated status of the security requirement pack.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_security_requirement_pack_input.UpdateSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_security_requirement_pack_output.UpdateSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_security_requirement_pack.async_update_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_security_requirement_pack_input.UpdateSecurityRequirementPackInput = {
            "pack_id": pack_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_security_requirement_pack(
        self,
        pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_security_requirement_pack_output.DeleteSecurityRequirementPackOutput":
        """<p>Deletes a customer managed security requirement pack and all its associated security requirements.</p>

        Args:
            pack_id: <p>The unique identifier of the security requirement pack to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_security_requirement_pack_input.DeleteSecurityRequirementPackInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_security_requirement_pack_output.DeleteSecurityRequirementPackOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_security_requirement_pack

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_security_requirement_pack.async_delete_security_requirement_pack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_security_requirement_pack_input.DeleteSecurityRequirementPackInput = {
            "pack_id": pack_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_security_requirement_packs(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.list_security_requirement_pack_filter.ListSecurityRequirementPackFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_security_requirement_packs_output.ListSecurityRequirementPacksOutput":
        """<p>Lists all security requirement packs in the caller's account.</p>

        Args:
            filter: <p>The filter criteria for listing security requirement packs.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single request.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_security_requirement_packs_input.ListSecurityRequirementPacksInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_security_requirement_packs_output.ListSecurityRequirementPacksOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_security_requirement_packs

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_security_requirement_packs.async_list_security_requirement_packs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_security_requirement_packs_input.ListSecurityRequirementPacksInput = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_security_requirement_packs(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.list_security_requirement_pack_filter.ListSecurityRequirementPackFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.security_requirement_pack_summary.SecurityRequirementPackSummary]":
        _token = next_token
        while True:
            _response = await self.list_security_requirement_packs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("security_requirement_pack_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_target_domain(
        self,
        target_domain_name: str,
        verification_method: "capo_securityagent.types.domain_verification_method.DomainVerificationMethod",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_securityagent.types.create_target_domain_output.CreateTargetDomainOutput"
    ):
        """<p>Creates a new target domain for penetration testing. A target domain is a web domain that must be registered and verified before it can be tested.</p>

        Args:
            target_domain_name: <p>The domain name to register as a target domain.</p>
            verification_method: <p>The method to use for verifying domain ownership. Valid values are DNS_TXT, HTTP_ROUTE, and PRIVATE_VPC.</p>
            tags: <p>The tags to associate with the target domain.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_target_domain_input.CreateTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_target_domain_output.CreateTargetDomainOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_target_domain

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_target_domain.async_create_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.create_target_domain_input.CreateTargetDomainInput = {
            "target_domain_name": target_domain_name,
            "verification_method": verification_method,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_target_domain(
        self,
        target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId",
        verification_method: "capo_securityagent.types.domain_verification_method.DomainVerificationMethod",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> (
        "capo_securityagent.types.update_target_domain_output.UpdateTargetDomainOutput"
    ):
        """<p>Updates the verification method for a target domain.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to update.</p>
            verification_method: <p>The updated verification method for the target domain.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_target_domain_input.UpdateTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_target_domain_output.UpdateTargetDomainOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_target_domain

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_target_domain.async_update_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.update_target_domain_input.UpdateTargetDomainInput = {
            "target_domain_id": target_domain_id,
            "verification_method": verification_method,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_target_domain(
        self,
        target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> (
        "capo_securityagent.types.delete_target_domain_output.DeleteTargetDomainOutput"
    ):
        """<p>Deletes a target domain registration. After deletion, the domain can no longer be used for penetration testing.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_target_domain_input.DeleteTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_target_domain_output.DeleteTargetDomainOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_target_domain

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_target_domain.async_delete_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_target_domain_input.DeleteTargetDomainInput = {
            "target_domain_id": target_domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_target_domains(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_target_domains_output.ListTargetDomainsOutput":
        """<p>Returns a paginated list of target domain summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_target_domains_input.ListTargetDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_target_domains_output.ListTargetDomainsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_target_domains

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_target_domains.async_list_target_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.list_target_domains_input.ListTargetDomainsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_target_domains(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityagent.types.target_domain_summary.TargetDomainSummary]":
        _token = next_token
        while True:
            _response = await self.list_target_domains(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("target_domain_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_get_target_domains(
        self,
        target_domain_ids: "capo_securityagent.types.target_domain_id_list.TargetDomainIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.batch_get_target_domains_output.BatchGetTargetDomainsOutput":
        """<p>Retrieves information about one or more target domains.</p>

        Args:
            target_domain_ids: <p>The list of target domain identifiers to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.batch_get_target_domains_input.BatchGetTargetDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.batch_get_target_domains_output.BatchGetTargetDomainsOutput"
        ]:
            import capo_securityagent._operations.security_agent.batch_get_target_domains

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.batch_get_target_domains.async_batch_get_target_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityagent.types.batch_get_target_domains_input.BatchGetTargetDomainsInput = {
            "target_domain_ids": target_domain_ids
        }

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

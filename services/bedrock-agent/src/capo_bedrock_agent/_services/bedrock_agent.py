"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AmazonBedrockAgentBuildTimeLambda``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_bedrock_agent._auth._signers
import capo_bedrock_agent._auth._sigv4
from capo_bedrock_agent._auth._identity import Credentials
from capo_bedrock_agent._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_agent._auth._zapros_handler import AuthMiddleware
from capo_bedrock_agent._pagination import resolve_path as _resolve_path
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.action_group_resource import (
    ActionGroupResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.agent_collaborator_resource import (
    AgentCollaboratorResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.agent_resource import (
    AgentResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.alias_resource import (
    AliasResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.data_source_resource import (
    DataSourceResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.flow_resource import (
    FlowResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.ingestion_job_resource import (
    IngestionJobResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.knowledge_base_document_resource import (
    KnowledgeBaseDocumentResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.knowledge_base_resource import (
    KnowledgeBaseResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.prompt_resource import (
    PromptResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.tagging_resource import (
    TaggingResource,
)
from capo_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.version_resource import (
    VersionResource,
)
from capo_bedrock_agent._services._aws_config import aws_config
from capo_bedrock_agent._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_bedrock_agent.types.action_group_executor
    import capo_bedrock_agent.types.action_group_signature
    import capo_bedrock_agent.types.action_group_signature_params
    import capo_bedrock_agent.types.action_group_state
    import capo_bedrock_agent.types.action_group_summary
    import capo_bedrock_agent.types.agent_alias_id
    import capo_bedrock_agent.types.agent_alias_routing_configuration
    import capo_bedrock_agent.types.agent_alias_summary
    import capo_bedrock_agent.types.agent_collaboration
    import capo_bedrock_agent.types.agent_collaborator_summary
    import capo_bedrock_agent.types.agent_descriptor
    import capo_bedrock_agent.types.agent_knowledge_base_summary
    import capo_bedrock_agent.types.agent_role_arn
    import capo_bedrock_agent.types.agent_summary
    import capo_bedrock_agent.types.agent_version_summary
    import capo_bedrock_agent.types.alias_invocation_state
    import capo_bedrock_agent.types.api_schema
    import capo_bedrock_agent.types.associate_agent_collaborator_request
    import capo_bedrock_agent.types.associate_agent_collaborator_response
    import capo_bedrock_agent.types.associate_agent_knowledge_base_request
    import capo_bedrock_agent.types.associate_agent_knowledge_base_response
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.collaboration_instruction
    import capo_bedrock_agent.types.create_agent_action_group_request
    import capo_bedrock_agent.types.create_agent_action_group_response
    import capo_bedrock_agent.types.create_agent_alias_request
    import capo_bedrock_agent.types.create_agent_alias_response
    import capo_bedrock_agent.types.create_agent_request
    import capo_bedrock_agent.types.create_agent_response
    import capo_bedrock_agent.types.create_data_source_request
    import capo_bedrock_agent.types.create_data_source_response
    import capo_bedrock_agent.types.create_flow_alias_request
    import capo_bedrock_agent.types.create_flow_alias_response
    import capo_bedrock_agent.types.create_flow_request
    import capo_bedrock_agent.types.create_flow_response
    import capo_bedrock_agent.types.create_flow_version_request
    import capo_bedrock_agent.types.create_flow_version_response
    import capo_bedrock_agent.types.create_knowledge_base_request
    import capo_bedrock_agent.types.create_knowledge_base_response
    import capo_bedrock_agent.types.create_prompt_request
    import capo_bedrock_agent.types.create_prompt_response
    import capo_bedrock_agent.types.create_prompt_version_request
    import capo_bedrock_agent.types.create_prompt_version_response
    import capo_bedrock_agent.types.create_vpc_configuration_request
    import capo_bedrock_agent.types.create_vpc_configuration_response
    import capo_bedrock_agent.types.custom_orchestration
    import capo_bedrock_agent.types.data_deletion_policy
    import capo_bedrock_agent.types.data_source_configuration
    import capo_bedrock_agent.types.data_source_summary
    import capo_bedrock_agent.types.delete_agent_action_group_request
    import capo_bedrock_agent.types.delete_agent_action_group_response
    import capo_bedrock_agent.types.delete_agent_alias_request
    import capo_bedrock_agent.types.delete_agent_alias_response
    import capo_bedrock_agent.types.delete_agent_request
    import capo_bedrock_agent.types.delete_agent_response
    import capo_bedrock_agent.types.delete_agent_version_request
    import capo_bedrock_agent.types.delete_agent_version_response
    import capo_bedrock_agent.types.delete_data_source_request
    import capo_bedrock_agent.types.delete_data_source_response
    import capo_bedrock_agent.types.delete_flow_alias_request
    import capo_bedrock_agent.types.delete_flow_alias_response
    import capo_bedrock_agent.types.delete_flow_request
    import capo_bedrock_agent.types.delete_flow_response
    import capo_bedrock_agent.types.delete_flow_version_request
    import capo_bedrock_agent.types.delete_flow_version_response
    import capo_bedrock_agent.types.delete_knowledge_base_documents_request
    import capo_bedrock_agent.types.delete_knowledge_base_documents_response
    import capo_bedrock_agent.types.delete_knowledge_base_request
    import capo_bedrock_agent.types.delete_knowledge_base_response
    import capo_bedrock_agent.types.delete_prompt_request
    import capo_bedrock_agent.types.delete_prompt_response
    import capo_bedrock_agent.types.delete_resource_policy_request
    import capo_bedrock_agent.types.delete_resource_policy_response
    import capo_bedrock_agent.types.delete_vpc_configuration_request
    import capo_bedrock_agent.types.delete_vpc_configuration_response
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.disassociate_agent_collaborator_request
    import capo_bedrock_agent.types.disassociate_agent_collaborator_response
    import capo_bedrock_agent.types.disassociate_agent_knowledge_base_request
    import capo_bedrock_agent.types.disassociate_agent_knowledge_base_response
    import capo_bedrock_agent.types.document_identifiers
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.flow_alias_concurrency_configuration
    import capo_bedrock_agent.types.flow_alias_identifier
    import capo_bedrock_agent.types.flow_alias_routing_configuration
    import capo_bedrock_agent.types.flow_alias_summary
    import capo_bedrock_agent.types.flow_definition
    import capo_bedrock_agent.types.flow_description
    import capo_bedrock_agent.types.flow_execution_role_arn
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.flow_name
    import capo_bedrock_agent.types.flow_summary
    import capo_bedrock_agent.types.flow_version_summary
    import capo_bedrock_agent.types.function_schema
    import capo_bedrock_agent.types.get_agent_action_group_request
    import capo_bedrock_agent.types.get_agent_action_group_response
    import capo_bedrock_agent.types.get_agent_alias_request
    import capo_bedrock_agent.types.get_agent_alias_response
    import capo_bedrock_agent.types.get_agent_collaborator_request
    import capo_bedrock_agent.types.get_agent_collaborator_response
    import capo_bedrock_agent.types.get_agent_knowledge_base_request
    import capo_bedrock_agent.types.get_agent_knowledge_base_response
    import capo_bedrock_agent.types.get_agent_request
    import capo_bedrock_agent.types.get_agent_response
    import capo_bedrock_agent.types.get_agent_version_request
    import capo_bedrock_agent.types.get_agent_version_response
    import capo_bedrock_agent.types.get_data_source_request
    import capo_bedrock_agent.types.get_data_source_response
    import capo_bedrock_agent.types.get_flow_alias_request
    import capo_bedrock_agent.types.get_flow_alias_response
    import capo_bedrock_agent.types.get_flow_request
    import capo_bedrock_agent.types.get_flow_response
    import capo_bedrock_agent.types.get_flow_version_request
    import capo_bedrock_agent.types.get_flow_version_response
    import capo_bedrock_agent.types.get_ingestion_job_request
    import capo_bedrock_agent.types.get_ingestion_job_response
    import capo_bedrock_agent.types.get_knowledge_base_documents_request
    import capo_bedrock_agent.types.get_knowledge_base_documents_response
    import capo_bedrock_agent.types.get_knowledge_base_request
    import capo_bedrock_agent.types.get_knowledge_base_response
    import capo_bedrock_agent.types.get_prompt_request
    import capo_bedrock_agent.types.get_prompt_response
    import capo_bedrock_agent.types.get_resource_policy_request
    import capo_bedrock_agent.types.get_resource_policy_response
    import capo_bedrock_agent.types.get_vpc_configuration_request
    import capo_bedrock_agent.types.get_vpc_configuration_response
    import capo_bedrock_agent.types.guardrail_configuration
    import capo_bedrock_agent.types.host_header
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.included_data
    import capo_bedrock_agent.types.ingest_knowledge_base_documents_request
    import capo_bedrock_agent.types.ingest_knowledge_base_documents_response
    import capo_bedrock_agent.types.ingestion_job_filters
    import capo_bedrock_agent.types.ingestion_job_sort_by
    import capo_bedrock_agent.types.ingestion_job_summary
    import capo_bedrock_agent.types.instruction
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.knowledge_base_configuration
    import capo_bedrock_agent.types.knowledge_base_document_detail
    import capo_bedrock_agent.types.knowledge_base_documents
    import capo_bedrock_agent.types.knowledge_base_role_arn
    import capo_bedrock_agent.types.knowledge_base_state
    import capo_bedrock_agent.types.knowledge_base_summary
    import capo_bedrock_agent.types.list_agent_action_groups_request
    import capo_bedrock_agent.types.list_agent_action_groups_response
    import capo_bedrock_agent.types.list_agent_aliases_request
    import capo_bedrock_agent.types.list_agent_aliases_response
    import capo_bedrock_agent.types.list_agent_collaborators_request
    import capo_bedrock_agent.types.list_agent_collaborators_response
    import capo_bedrock_agent.types.list_agent_knowledge_bases_request
    import capo_bedrock_agent.types.list_agent_knowledge_bases_response
    import capo_bedrock_agent.types.list_agent_versions_request
    import capo_bedrock_agent.types.list_agent_versions_response
    import capo_bedrock_agent.types.list_agents_request
    import capo_bedrock_agent.types.list_agents_response
    import capo_bedrock_agent.types.list_data_sources_request
    import capo_bedrock_agent.types.list_data_sources_response
    import capo_bedrock_agent.types.list_flow_aliases_request
    import capo_bedrock_agent.types.list_flow_aliases_response
    import capo_bedrock_agent.types.list_flow_versions_request
    import capo_bedrock_agent.types.list_flow_versions_response
    import capo_bedrock_agent.types.list_flows_request
    import capo_bedrock_agent.types.list_flows_response
    import capo_bedrock_agent.types.list_ingestion_jobs_request
    import capo_bedrock_agent.types.list_ingestion_jobs_response
    import capo_bedrock_agent.types.list_knowledge_base_documents_request
    import capo_bedrock_agent.types.list_knowledge_base_documents_response
    import capo_bedrock_agent.types.list_knowledge_bases_request
    import capo_bedrock_agent.types.list_knowledge_bases_response
    import capo_bedrock_agent.types.list_prompts_request
    import capo_bedrock_agent.types.list_prompts_response
    import capo_bedrock_agent.types.list_tags_for_resource_request
    import capo_bedrock_agent.types.list_tags_for_resource_response
    import capo_bedrock_agent.types.list_vpc_configurations_request
    import capo_bedrock_agent.types.list_vpc_configurations_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.memory_configuration
    import capo_bedrock_agent.types.model_identifier
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.numerical_version
    import capo_bedrock_agent.types.orchestration_type
    import capo_bedrock_agent.types.port
    import capo_bedrock_agent.types.prepare_agent_request
    import capo_bedrock_agent.types.prepare_agent_response
    import capo_bedrock_agent.types.prepare_flow_request
    import capo_bedrock_agent.types.prepare_flow_response
    import capo_bedrock_agent.types.prompt_description
    import capo_bedrock_agent.types.prompt_identifier
    import capo_bedrock_agent.types.prompt_name
    import capo_bedrock_agent.types.prompt_override_configuration
    import capo_bedrock_agent.types.prompt_summary
    import capo_bedrock_agent.types.prompt_variant_list
    import capo_bedrock_agent.types.prompt_variant_name
    import capo_bedrock_agent.types.put_resource_policy_request
    import capo_bedrock_agent.types.put_resource_policy_response
    import capo_bedrock_agent.types.relay_conversation_history
    import capo_bedrock_agent.types.resource_arn
    import capo_bedrock_agent.types.resource_policy
    import capo_bedrock_agent.types.resource_target
    import capo_bedrock_agent.types.revision_id
    import capo_bedrock_agent.types.server_side_encryption_configuration
    import capo_bedrock_agent.types.session_ttl
    import capo_bedrock_agent.types.start_ingestion_job_request
    import capo_bedrock_agent.types.start_ingestion_job_response
    import capo_bedrock_agent.types.stop_ingestion_job_request
    import capo_bedrock_agent.types.stop_ingestion_job_response
    import capo_bedrock_agent.types.storage_configuration
    import capo_bedrock_agent.types.subnet_id_list
    import capo_bedrock_agent.types.tag_key_list
    import capo_bedrock_agent.types.tag_resource_request
    import capo_bedrock_agent.types.tag_resource_response
    import capo_bedrock_agent.types.taggable_resources_arn
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.tls_server_name
    import capo_bedrock_agent.types.untag_resource_request
    import capo_bedrock_agent.types.untag_resource_response
    import capo_bedrock_agent.types.update_agent_action_group_request
    import capo_bedrock_agent.types.update_agent_action_group_response
    import capo_bedrock_agent.types.update_agent_alias_request
    import capo_bedrock_agent.types.update_agent_alias_response
    import capo_bedrock_agent.types.update_agent_collaborator_request
    import capo_bedrock_agent.types.update_agent_collaborator_response
    import capo_bedrock_agent.types.update_agent_knowledge_base_request
    import capo_bedrock_agent.types.update_agent_knowledge_base_response
    import capo_bedrock_agent.types.update_agent_request
    import capo_bedrock_agent.types.update_agent_response
    import capo_bedrock_agent.types.update_data_source_request
    import capo_bedrock_agent.types.update_data_source_response
    import capo_bedrock_agent.types.update_flow_alias_request
    import capo_bedrock_agent.types.update_flow_alias_response
    import capo_bedrock_agent.types.update_flow_request
    import capo_bedrock_agent.types.update_flow_response
    import capo_bedrock_agent.types.update_knowledge_base_request
    import capo_bedrock_agent.types.update_knowledge_base_response
    import capo_bedrock_agent.types.update_prompt_request
    import capo_bedrock_agent.types.update_prompt_response
    import capo_bedrock_agent.types.validate_flow_definition_request
    import capo_bedrock_agent.types.validate_flow_definition_response
    import capo_bedrock_agent.types.vector_ingestion_configuration
    import capo_bedrock_agent.types.version
    import capo_bedrock_agent.types.vpc_configuration_description
    import capo_bedrock_agent.types.vpc_configuration_id
    import capo_bedrock_agent.types.vpc_configuration_name
    import capo_bedrock_agent.types.vpc_configuration_status
    import capo_bedrock_agent.types.vpc_configuration_summary
    import capo_bedrock_agent.types.vpc_id
    import capo_bedrock_agent.types.vpc_protocol
    import capo_bedrock_agent.types.vpc_resolution_mode


class BedrockAgentClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class BedrockAgentClient:
    """A client for the ``BedrockAgent`` service.

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
        self._config = BedrockAgentClientConfig(
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
        self.action_group_resource = ActionGroupResource(self)
        self.agent_collaborator_resource = AgentCollaboratorResource(self)
        self.agent_resource = AgentResource(self)
        self.alias_resource = AliasResource(self)
        self.data_source_resource = DataSourceResource(self)
        self.flow_resource = FlowResource(self)
        self.ingestion_job_resource = IngestionJobResource(self)
        self.knowledge_base_document_resource = KnowledgeBaseDocumentResource(self)
        self.knowledge_base_resource = KnowledgeBaseResource(self)
        self.prompt_resource = PromptResource(self)
        self.tagging_resource = TaggingResource(self)
        self.version_resource = VersionResource(self)

    def operation_options(
        self, config_overrides: Optional[BedrockAgentClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockAgentClientConfig = config_overrides or {}
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

    def create_vpc_configuration(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        vpc_id: "capo_bedrock_agent.types.vpc_id.VpcId",
        subnet_ids: "capo_bedrock_agent.types.subnet_id_list.SubnetIdList",
        resource_target: "capo_bedrock_agent.types.resource_target.ResourceTarget",
        port: "capo_bedrock_agent.types.port.Port",
        protocol: "capo_bedrock_agent.types.vpc_protocol.VpcProtocol",
        resolution_mode: "capo_bedrock_agent.types.vpc_resolution_mode.VpcResolutionMode",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        host_header: Optional["capo_bedrock_agent.types.host_header.HostHeader"] = None,
        tls_server_name: Optional[
            "capo_bedrock_agent.types.tls_server_name.TlsServerName"
        ] = None,
        name: Optional[
            "capo_bedrock_agent.types.vpc_configuration_name.VpcConfigurationName"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.vpc_configuration_description.VpcConfigurationDescription"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_vpc_configuration_response.CreateVpcConfigurationResponse":
        """<p>Creates a VPC configuration that lets a knowledge base connect to a resource in your private VPC. This operation is asynchronous: it returns a <code>vpcConfigurationId</code> with status <code>CREATING</code>. Poll <code>GetVpcConfiguration</code> until the status becomes <code>CREATED</code> or <code>CREATE_FAILED</code>.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to associate this VPC configuration with.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>
            vpc_id: <p>The identifier of the VPC that the knowledge base connects through to reach the resource.</p>
            subnet_ids: <p>The subnets, in the VPC identified by <code>vpcId</code>, that the knowledge base uses to connect to the resource.</p>
            resource_target: <p>The private IPv4 address or DNS name of the resource you want the knowledge base to reach. The target must be privately reachable from inside your VPC, such as an internal load balancer or a private IP. The following are not supported:</p> <ul> <li> <p>Internet-facing endpoints</p> </li> <li> <p>Loopback addresses</p> </li> <li> <p>Link-local addresses</p> </li> <li> <p>Wildcard addresses</p> </li> <li> <p>Multicast addresses</p> </li> <li> <p>IPv6 literals</p> </li> </ul>
            port: <p>The port on which to reach the resource.</p>
            protocol: <p>The protocol used to connect to the resource. Specify <code>HTTP</code> for plaintext or <code>HTTPS</code> for TLS. When you specify <code>HTTPS</code>, you must also provide <code>tlsServerName</code>.</p>
            resolution_mode: <p>Controls how a domain-name <code>resourceTarget</code> is resolved. This applies only when the target is a domain name; it has no effect for IP-address targets, which have no name to resolve. In all cases the resolved address must be reachable from inside your VPC. Valid values:</p> <ul> <li> <p> <code>IN_VPC</code> (default, recommended) – The target domain name is resolved privately, using the DNS resolvers of the VPC, such as private Route 53 hosted zones or on-premises DNS reachable from the VPC. Use this for targets that are private to your VPC, such as internal load balancers, private hosted-zone names, or on-premises hosts.</p> </li> <li> <p> <code>PUBLIC</code> – The target domain name is resolved against public DNS resolvers. Select this only when the target's domain name must be resolved through public DNS and the resulting address is still reachable from the VPC, an uncommon split-horizon configuration. If you are unsure, use <code>IN_VPC</code>.</p> </li> </ul>
            host_header: <p>An optional HTTP <code>Host</code> header value to send when invoking the resource. Set this only if your resource (or an upstream router or ingress) routes by the <code>Host</code> header and that host differs from the target. This setting is independent of <code>tlsServerName</code>.</p>
            tls_server_name: <p>The expected TLS server name. The service matches this value against the Subject Alternative Names on your resource's TLS certificate during invocation. This field is required when <code>protocol</code> is <code>HTTPS</code>. Set it to a hostname on your certificate, such as <code>app.internal.example.com</code>. You can use a single leftmost wildcard, such as <code>*.example.com</code>. The value must be a hostname without a port.</p>
            name: <p>An optional human-readable name for the VPC configuration. If you don't specify a name, the VPC configuration has no name.</p>
            description: <p>An optional description of the VPC configuration. If you don't specify a description, the VPC configuration has no description.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_vpc_configuration_request.CreateVpcConfigurationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_vpc_configuration_response.CreateVpcConfigurationResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_vpc_configuration

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_vpc_configuration.create_vpc_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_vpc_configuration_request.CreateVpcConfigurationRequest = {
            "knowledge_base_id": knowledge_base_id,
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "resource_target": resource_target,
            "port": port,
            "protocol": protocol,
            "resolution_mode": resolution_mode,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if host_header is not None:
            input_["host_header"] = host_header
        if tls_server_name is not None:
            input_["tls_server_name"] = tls_server_name
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        expected_revision_id: Optional[
            "capo_bedrock_agent.types.revision_id.RevisionId"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Removes the resource policy associated with a knowledge base. After deletion, other AWS accounts can no longer access the knowledge base using cross-account permissions.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the knowledge base to remove the resource policy from.</p>
            expected_revision_id: <p>The expected revision identifier of the resource policy. Use this to prevent conflicts when multiple users update the same policy concurrently.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_resource_policy

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_configuration(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        vpc_configuration_id: "capo_bedrock_agent.types.vpc_configuration_id.VpcConfigurationId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.delete_vpc_configuration_response.DeleteVpcConfigurationResponse":
        """<p>Deletes a VPC configuration. This operation is asynchronous: it returns status <code>DELETING</code>. Poll <code>GetVpcConfiguration</code> until it returns a <code>ResourceNotFoundException</code>, indicating the configuration is deleted. Delete requests are idempotent and safe to retry.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that owns the VPC configuration.</p>
            vpc_configuration_id: <p>The unique identifier of the VPC configuration to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_vpc_configuration_request.DeleteVpcConfigurationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_vpc_configuration_response.DeleteVpcConfigurationResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_vpc_configuration

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_vpc_configuration.delete_vpc_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_vpc_configuration_request.DeleteVpcConfigurationRequest = {
            "knowledge_base_id": knowledge_base_id,
            "vpc_configuration_id": vpc_configuration_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource policy associated with a knowledge base.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the knowledge base to retrieve the resource policy for.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_resource_policy

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vpc_configuration(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        vpc_configuration_id: "capo_bedrock_agent.types.vpc_configuration_id.VpcConfigurationId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_vpc_configuration_response.GetVpcConfigurationResponse":
        """<p>Returns the details and current status of a single VPC configuration. Use this operation to poll for the outcome of an asynchronous create or delete.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that owns the VPC configuration.</p>
            vpc_configuration_id: <p>The unique identifier of the VPC configuration to retrieve.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_vpc_configuration_request.GetVpcConfigurationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_vpc_configuration_response.GetVpcConfigurationResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_vpc_configuration

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_vpc_configuration.get_vpc_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_vpc_configuration_request.GetVpcConfigurationRequest = {
            "knowledge_base_id": knowledge_base_id,
            "vpc_configuration_id": vpc_configuration_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vpc_configurations(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        status_filter: Optional[
            "capo_bedrock_agent.types.vpc_configuration_status.VpcConfigurationStatus"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_vpc_configurations_response.ListVpcConfigurationsResponse":
        """<p>Returns a paginated list of the VPC configurations for a knowledge base. You can optionally filter by status. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base whose VPC configurations you want to list.</p>
            status_filter: <p>The status to filter the results by. Only VPC configurations with the specified status are returned.</p>
            max_results: <p>The maximum number of results to return in the response. If more results are available, the response returns a <code>nextToken</code>.</p>
            next_token: <p>A pagination token to retrieve the next page of results, returned in a previous response when more results are available.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_vpc_configurations_request.ListVpcConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_vpc_configurations_response.ListVpcConfigurationsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_vpc_configurations

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_vpc_configurations.list_vpc_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_vpc_configurations_request.ListVpcConfigurationsRequest = {
            "knowledge_base_id": knowledge_base_id
        }
        if status_filter is not None:
            input_["status_filter"] = status_filter
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

    def iter_list_vpc_configurations(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        status_filter: Optional[
            "capo_bedrock_agent.types.vpc_configuration_status.VpcConfigurationStatus"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.vpc_configuration_summary.VpcConfigurationSummary]":
        _token = next_token
        while True:
            _response = self.list_vpc_configurations(
                knowledge_base_id,
                config_overrides=config_overrides,
                status_filter=status_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_resource_policy(
        self,
        resource_arn: "capo_bedrock_agent.types.resource_arn.ResourceArn",
        policy: "capo_bedrock_agent.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        expected_revision_id: Optional[
            "capo_bedrock_agent.types.revision_id.RevisionId"
        ] = None,
    ) -> "capo_bedrock_agent.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Associates a resource policy with a knowledge base. A resource policy allows other AWS accounts to access the knowledge base. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-cross-account.html">Cross-account access for knowledge bases</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the knowledge base to attach the resource policy to.</p>
            policy: <p>The JSON-formatted resource policy to associate with the knowledge base.</p>
            expected_revision_id: <p>The expected revision identifier of the resource policy. Use this to prevent conflicts when multiple users update the same policy concurrently. Specify the <code>revisionId</code> from the most recent <code>GetResourcePolicy</code> or <code>PutResourcePolicy</code> response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.put_resource_policy

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_flow_definition(
        self,
        definition: "capo_bedrock_agent.types.flow_definition.FlowDefinition",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.validate_flow_definition_response.ValidateFlowDefinitionResponse":
        """<p>Validates the definition of a flow.</p>

        Args:
            definition: <p>The definition of a flow to validate.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.validate_flow_definition_request.ValidateFlowDefinitionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.validate_flow_definition_response.ValidateFlowDefinitionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.validate_flow_definition

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.validate_flow_definition.validate_flow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.validate_flow_definition_request.ValidateFlowDefinitionRequest = {
            "definition": definition
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        parent_action_group_signature: Optional[
            "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
        ] = None,
        parent_action_group_signature_params: Optional[
            "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
        ] = None,
        action_group_executor: Optional[
            "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
        ] = None,
        api_schema: Optional["capo_bedrock_agent.types.api_schema.APISchema"] = None,
        action_group_state: Optional[
            "capo_bedrock_agent.types.action_group_state.ActionGroupState"
        ] = None,
        function_schema: Optional[
            "capo_bedrock_agent.types.function_schema.FunctionSchema"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_agent_action_group_response.CreateAgentActionGroupResponse":
        """<p>Creates an action group for an agent. An action group represents the actions that an agent can carry out for the customer by defining the APIs that an agent can call and the logic for calling them.</p> <p>To allow your agent to request the user for additional information when trying to complete a task, add an action group with the <code>parentActionGroupSignature</code> field set to <code>AMAZON.UserInput</code>. </p> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, add an action group with the <code>parentActionGroupSignature</code> field set to <code>AMAZON.CodeInterpreter</code>. </p> <p>You must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields blank for this action group. During orchestration, if your agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html">Observation</a> reprompting the user for more information.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create the action group.</p>
            agent_version: <p>The version of the agent for which to create the action group.</p>
            action_group_name: <p>The name to give the action group.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the action group.</p>
            parent_action_group_signature: <p>Specify a built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul>
            parent_action_group_signature_params: <p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>
            action_group_executor: <p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.</p>
            api_schema: <p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>
            action_group_state: <p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>
            function_schema: <p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_agent_action_group_request.CreateAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_agent_action_group_response.CreateAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_action_group.create_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_action_group_request.CreateAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_name": action_group_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if parent_action_group_signature is not None:
            input_["parent_action_group_signature"] = parent_action_group_signature
        if parent_action_group_signature_params is not None:
            input_["parent_action_group_signature_params"] = (
                parent_action_group_signature_params
            )
        if action_group_executor is not None:
            input_["action_group_executor"] = action_group_executor
        if api_schema is not None:
            input_["api_schema"] = api_schema
        if action_group_state is not None:
            input_["action_group_state"] = action_group_state
        if function_schema is not None:
            input_["function_schema"] = function_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_action_group_response.DeleteAgentActionGroupResponse":
        """<p>Deletes an action group in an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the action group belongs to.</p>
            agent_version: <p>The version of the agent that the action group belongs to.</p>
            action_group_id: <p>The unique identifier of the action group to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_action_group_request.DeleteAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_action_group_response.DeleteAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_action_group.delete_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_action_group_request.DeleteAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_action_group_response.GetAgentActionGroupResponse":
        """<p>Gets information about an action group for an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the action group belongs to.</p>
            agent_version: <p>The version of the agent that the action group belongs to.</p>
            action_group_id: <p>The unique identifier of the action group for which to get information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_action_group_request.GetAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_action_group_response.GetAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_action_group.get_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_action_group_request.GetAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_action_groups(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_action_groups_response.ListAgentActionGroupsResponse":
        """<p>Lists the action groups for an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_action_groups_request.ListAgentActionGroupsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_action_groups_response.ListAgentActionGroupsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_action_groups

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_action_groups.list_agent_action_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_action_groups_request.ListAgentActionGroupsRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
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

    def iter_list_agent_action_groups(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.action_group_summary.ActionGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_agent_action_groups(
                agent_id,
                agent_version,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("action_group_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_agent_action_group(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        action_group_id: "capo_bedrock_agent.types.id.Id",
        action_group_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        parent_action_group_signature: Optional[
            "capo_bedrock_agent.types.action_group_signature.ActionGroupSignature"
        ] = None,
        parent_action_group_signature_params: Optional[
            "capo_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
        ] = None,
        action_group_executor: Optional[
            "capo_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
        ] = None,
        action_group_state: Optional[
            "capo_bedrock_agent.types.action_group_state.ActionGroupState"
        ] = None,
        api_schema: Optional["capo_bedrock_agent.types.api_schema.APISchema"] = None,
        function_schema: Optional[
            "capo_bedrock_agent.types.function_schema.FunctionSchema"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_action_group_response.UpdateAgentActionGroupResponse":
        """<p>Updates the configuration for an action group for an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to update the action group.</p>
            agent_version: <p>The unique identifier of the agent version for which to update the action group.</p>
            action_group_id: <p>The unique identifier of the action group.</p>
            action_group_name: <p>Specifies a new name for the action group.</p>
            description: <p>Specifies a new name for the action group.</p>
            parent_action_group_signature: <p>Update the built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul> <p>During orchestration, if your agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html">Observation</a> reprompting the user for more information.</p>
            parent_action_group_signature_params: <p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>
            action_group_executor: <p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.</p>
            action_group_state: <p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>
            api_schema: <p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html">Action group OpenAPI schemas</a>.</p>
            function_schema: <p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_action_group_request.UpdateAgentActionGroupRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_action_group_response.UpdateAgentActionGroupResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_action_group

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_action_group.update_agent_action_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_action_group_request.UpdateAgentActionGroupRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "action_group_id": action_group_id,
            "action_group_name": action_group_name,
        }
        if description is not None:
            input_["description"] = description
        if parent_action_group_signature is not None:
            input_["parent_action_group_signature"] = parent_action_group_signature
        if parent_action_group_signature_params is not None:
            input_["parent_action_group_signature_params"] = (
                parent_action_group_signature_params
            )
        if action_group_executor is not None:
            input_["action_group_executor"] = action_group_executor
        if action_group_state is not None:
            input_["action_group_state"] = action_group_state
        if api_schema is not None:
            input_["api_schema"] = api_schema
        if function_schema is not None:
            input_["function_schema"] = function_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "capo_bedrock_agent.types.name.Name",
        collaboration_instruction: "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse":
        """<p>Makes an agent a collaborator for another agent.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>An agent version.</p>
            agent_descriptor: <p>The alias of the collaborator agent.</p>
            collaborator_name: <p>A name for the collaborator.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator.associate_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "agent_descriptor": agent_descriptor,
            "collaborator_name": collaborator_name,
            "collaboration_instruction": collaboration_instruction,
        }
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history
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

    def disassociate_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse":
        """<p>Disassociates an agent collaborator.</p>

        Args:
            agent_id: <p>An agent ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator.disassociate_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse":
        """<p>Retrieves information about an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator.get_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_collaborators(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse":
        """<p>Retrieve a list of an agent's collaborators.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            max_results: <p>The maximum number of agent collaborators to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators.list_agent_collaborators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
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

    def iter_list_agent_collaborators(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.agent_collaborator_summary.AgentCollaboratorSummary]":
        _token = next_token
        while True:
            _response = self.list_agent_collaborators(
                agent_id,
                agent_version,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_collaborator_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "capo_bedrock_agent.types.name.Name",
        collaboration_instruction: "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse":
        """<p>Updates an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
            agent_descriptor: <p>An agent descriptor for the agent collaborator.</p>
            collaborator_name: <p>The collaborator's name.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator.update_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
            "agent_descriptor": agent_descriptor,
            "collaborator_name": collaborator_name,
            "collaboration_instruction": collaboration_instruction,
        }
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_agent(
        self,
        agent_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        instruction: Optional[
            "capo_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        agent_resource_role_arn: Optional[
            "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_agent_response.CreateAgentResponse":
        """<note> <p>Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore Amazon Bedrock AgentCore. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html">Amazon Bedrock Agents Classic availability change</a>.</p> </note> <p>Creates an agent that orchestrates interactions between foundation models, data sources, software applications, user conversations, and APIs to carry out tasks to help customers.</p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p> <code>agentResourceRoleArn</code> – The Amazon Resource Name (ARN) of the role with permissions to invoke API operations on an agent.</p> </li> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To enable your agent to retain conversational context across multiple sessions, include a <code>memoryConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-configure-memory.html">Configure memory</a>.</p> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p> </li> <li> <p>If your agent fails to be created, the response returns a list of <code>failureReasons</code> alongside a list of <code>recommendedActions</code> for you to troubleshoot.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul>

        Args:
            agent_name: <p>A name for the agent that you create.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            instruction: <p>Instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>A description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            tags: <p>Any tags that you want to attach to the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is created.</p>
            memory_configuration: <p> Contains the details of the memory configured for the agent.</p>
            agent_collaboration: <p>The agent's collaboration role.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_agent_request.CreateAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_agent_response.CreateAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent.create_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_request.CreateAgentRequest = {
            "agent_name": agent_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if agent_resource_role_arn is not None:
            input_["agent_resource_role_arn"] = agent_resource_role_arn
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if tags is not None:
            input_["tags"] = tags
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_response.DeleteAgentResponse":
        """<p>Deletes an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_request.DeleteAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_response.DeleteAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent.delete_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_request.DeleteAgentRequest = {
            "agent_id": agent_id
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_response.GetAgentResponse":
        """<p>Gets information about an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_request.GetAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_response.GetAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent.get_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_request.GetAgentRequest = {
            "agent_id": agent_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agents(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agents_response.ListAgentsResponse":
        """<p>Lists the agents belonging to an account and information about each agent.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agents_request.ListAgentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agents_response.ListAgentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agents.list_agents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agents_request.ListAgentsRequest = {}
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

    def iter_list_agents(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.agent_summary.AgentSummary]":
        _token = next_token
        while True:
            _response = self.list_agents(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def prepare_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse":
        """<p>Creates a <code>DRAFT</code> version of the agent that can be used for internal testing.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to create a <code>DRAFT</code> version.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.prepare_agent_response.PrepareAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_agent.prepare_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.prepare_agent_request.PrepareAgentRequest = {
            "agent_id": agent_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_agent(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_name: "capo_bedrock_agent.types.name.Name",
        agent_resource_role_arn: "capo_bedrock_agent.types.agent_role_arn.AgentRoleArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        instruction: Optional[
            "capo_bedrock_agent.types.instruction.Instruction"
        ] = None,
        foundation_model: Optional[
            "capo_bedrock_agent.types.model_identifier.ModelIdentifier"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent.types.custom_orchestration.CustomOrchestration"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent.types.session_ttl.SessionTTL"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent.types.memory_configuration.MemoryConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent.types.agent_collaboration.AgentCollaboration"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_response.UpdateAgentResponse":
        """<p>Updates the configuration of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_name: <p>Specifies a new name for the agent.</p>
            instruction: <p>Specifies new instructions that tell the agent what it should do and how it should interact with users.</p>
            foundation_model: <p>The identifier for the model that you want to be used for orchestration by the agent you create.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            description: <p>Specifies a new description of the agent.</p>
            orchestration_type: <p> Specifies the type of orchestration strategy for the agent. This is set to <code>DEFAULT</code> orchestration type, by default. </p>
            custom_orchestration: <p> Contains details of the custom orchestration configured for the agent. </p>
            idle_session_ttl_in_seconds: <p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>
            agent_resource_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key with which to encrypt the agent.</p>
            prompt_override_configuration: <p>Contains configurations to override prompts in different parts of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>
            guardrail_configuration: <p>The unique Guardrail configuration assigned to the agent when it is updated.</p>
            memory_configuration: <p>Specifies the new memory configuration for the agent. </p>
            agent_collaboration: <p>The agent's collaboration role.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_request.UpdateAgentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_response.UpdateAgentResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent.update_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_request.UpdateAgentRequest = {
            "agent_id": agent_id,
            "agent_name": agent_name,
            "agent_resource_role_arn": agent_resource_role_arn,
        }
        if instruction is not None:
            input_["instruction"] = instruction
        if foundation_model is not None:
            input_["foundation_model"] = foundation_model
        if description is not None:
            input_["description"] = description
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        routing_configuration: Optional[
            "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> (
        "capo_bedrock_agent.types.create_agent_alias_response.CreateAgentAliasResponse"
    ):
        """<p>Creates an alias of an agent that can be used to deploy the agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_alias_name: <p>The name of the alias.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the alias of the agent.</p>
            routing_configuration: <p>Contains details about the routing configuration of the alias.</p>
            tags: <p>Any tags that you want to attach to the alias of the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_agent_alias_request.CreateAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_agent_alias_response.CreateAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_agent_alias.create_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_agent_alias_request.CreateAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_name": agent_alias_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if routing_configuration is not None:
            input_["routing_configuration"] = routing_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.delete_agent_alias_response.DeleteAgentAliasResponse"
    ):
        """<p>Deletes an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the alias belongs to.</p>
            agent_alias_id: <p>The unique identifier of the alias to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_alias_request.DeleteAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_alias_response.DeleteAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_alias.delete_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_alias_request.DeleteAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_alias_response.GetAgentAliasResponse":
        """<p>Gets information about an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias to get information belongs.</p>
            agent_alias_id: <p>The unique identifier of the alias for which to get information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_alias_request.GetAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_alias_response.GetAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_alias.get_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_alias_request.GetAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_aliases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> (
        "capo_bedrock_agent.types.list_agent_aliases_response.ListAgentAliasesResponse"
    ):
        """<p>Lists the aliases of an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_aliases_request.ListAgentAliasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_aliases_response.ListAgentAliasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_aliases

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_aliases.list_agent_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_aliases_request.ListAgentAliasesRequest = {
            "agent_id": agent_id
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

    def iter_list_agent_aliases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.agent_alias_summary.AgentAliasSummary]":
        _token = next_token
        while True:
            _response = self.list_agent_aliases(
                agent_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_alias_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_agent_alias(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_alias_id: "capo_bedrock_agent.types.agent_alias_id.AgentAliasId",
        agent_alias_name: "capo_bedrock_agent.types.name.Name",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        routing_configuration: Optional[
            "capo_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
        ] = None,
        alias_invocation_state: Optional[
            "capo_bedrock_agent.types.alias_invocation_state.AliasInvocationState"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.update_agent_alias_response.UpdateAgentAliasResponse"
    ):
        """<p>Updates configurations for an alias of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_alias_id: <p>The unique identifier of the alias.</p>
            agent_alias_name: <p>Specifies a new name for the alias.</p>
            description: <p>Specifies a new description for the alias.</p>
            routing_configuration: <p>Contains details about the routing configuration of the alias.</p>
            alias_invocation_state: <p>The invocation state for the agent alias. To pause the agent alias, set the value to <code>REJECT_INVOCATIONS</code>. To start the agent alias running again, set the value to <code>ACCEPT_INVOCATIONS</code>. Use the <code>GetAgentAlias</code>, or <code>ListAgentAliases</code>, operation to get the invocation state of an agent alias.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_alias_request.UpdateAgentAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_alias_response.UpdateAgentAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_alias.update_agent_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_alias_request.UpdateAgentAliasRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "agent_alias_name": agent_alias_name,
        }
        if description is not None:
            input_["description"] = description
        if routing_configuration is not None:
            input_["routing_configuration"] = routing_configuration
        if alias_invocation_state is not None:
            input_["alias_invocation_state"] = alias_invocation_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        data_source_configuration: "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        data_deletion_policy: Optional[
            "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.create_data_source_response.CreateDataSourceResponse"
    ):
        """<p>Connects a knowledge base to a data source. You specify the configuration for the specific data source service in the <code>dataSourceConfiguration</code> field.</p> <important> <p>You can't change the <code>chunkingConfiguration</code> after you create the data source connector.</p> </important>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to which to add the data source.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            name: <p>The name of the data source.</p>
            description: <p>A description of the data source.</p>
            data_source_configuration: <p>The connection configuration for the data source.</p>
            data_deletion_policy: <p>The data deletion policy for the data source.</p> <p>You can set the data deletion policy to:</p> <ul> <li> <p>DELETE: Deletes all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b>, only the data. This flag is ignored if an Amazon Web Services account is deleted.</p> </li> <li> <p>RETAIN: Retains all data from your data source that’s converted into vector embeddings upon deletion of a knowledge base or data source resource. Note that the <b>vector store itself is not deleted</b> if you delete a knowledge base or data source resource.</p> </li> </ul> <note> <p>For managed knowledge bases, the only supported option is <code>DELETE</code>, which is also the default.</p> </note>
            server_side_encryption_configuration: <p>Contains details about the server-side encryption for the data source.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in the data source.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_data_source_request.CreateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_data_source_response.CreateDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_data_source.create_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_data_source_request.CreateDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "data_source_configuration": data_source_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if data_deletion_policy is not None:
            input_["data_deletion_policy"] = data_deletion_policy
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.delete_data_source_response.DeleteDataSourceResponse"
    ):
        """<p>Deletes a data source from a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base from which to delete the data source.</p>
            data_source_id: <p>The unique identifier of the data source to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_data_source_response.DeleteDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_data_source.delete_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_data_source_request.DeleteDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_data_source_response.GetDataSourceResponse":
        """<p>Gets information about a data source.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data source.</p>
            data_source_id: <p>The unique identifier of the data source.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_data_source_request.GetDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_data_source_response.GetDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_data_source.get_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_data_source_request.GetDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_sources(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_data_sources_response.ListDataSourcesResponse":
        """<p>Lists the data sources in a knowledge base and information about each one.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for which to return a list of information.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_data_sources

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_data_sources.list_data_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_data_sources_request.ListDataSourcesRequest = {
            "knowledge_base_id": knowledge_base_id
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

    def iter_list_data_sources(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.data_source_summary.DataSourceSummary]":
        _token = next_token
        while True:
            _response = self.list_data_sources(
                knowledge_base_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("data_source_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_data_source(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        data_source_configuration: "capo_bedrock_agent.types.data_source_configuration.DataSourceConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        data_deletion_policy: Optional[
            "capo_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
    ) -> (
        "capo_bedrock_agent.types.update_data_source_response.UpdateDataSourceResponse"
    ):
        """<p>Updates the configurations for a data source connector.</p> <important> <p>You can't change the <code>chunkingConfiguration</code> after you create the data source connector. Specify the existing <code>chunkingConfiguration</code>.</p> </important>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data source.</p>
            data_source_id: <p>The unique identifier of the data source.</p>
            name: <p>Specifies a new name for the data source.</p>
            description: <p>Specifies a new description for the data source.</p>
            data_source_configuration: <p>The connection configuration for the data source that you want to update.</p>
            data_deletion_policy: <p>The data deletion policy for the data source that you want to update.</p>
            server_side_encryption_configuration: <p>Contains details about server-side encryption of the data source.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in the data source.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_data_source_response.UpdateDataSourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_data_source

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_data_source.update_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_data_source_request.UpdateDataSourceRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "name": name,
            "data_source_configuration": data_source_configuration,
        }
        if description is not None:
            input_["description"] = description
        if data_deletion_policy is not None:
            input_["data_deletion_policy"] = data_deletion_policy
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_flow(
        self,
        name: "capo_bedrock_agent.types.flow_name.FlowName",
        execution_role_arn: "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.flow_description.FlowDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        definition: Optional[
            "capo_bedrock_agent.types.flow_definition.FlowDefinition"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_flow_response.CreateFlowResponse":
        """<p>Creates a prompt flow that you can use to send an input through various steps to yield an output. Configure nodes, each of which corresponds to a step of the flow, and create connections between the nodes to create paths to different outputs. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html">How it works</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html">Create a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the flow.</p>
            description: <p>A description for the flow.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>
            definition: <p>A definition of the nodes and connections between nodes in the flow.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_flow_request.CreateFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_flow_response.CreateFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow.create_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_flow_request.CreateFlowRequest = {
            "name": name,
            "execution_role_arn": execution_role_arn,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if definition is not None:
            input_["definition"] = definition
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_flow(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        included_data: Optional[
            "capo_bedrock_agent.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_flow_response.GetFlowResponse":
        """<p>Retrieves information about a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html">Manage a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            included_data: <p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_flow_request.GetFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_flow_response.GetFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow.get_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_flow_request.GetFlowRequest = {
            "flow_identifier": flow_identifier
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_flow(
        self,
        name: "capo_bedrock_agent.types.flow_name.FlowName",
        execution_role_arn: "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn",
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.flow_description.FlowDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        definition: Optional[
            "capo_bedrock_agent.types.flow_definition.FlowDefinition"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_flow_response.UpdateFlowResponse":
        """<p>Modifies a flow. Include both fields that you want to keep and fields that you want to change. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html">How it works</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html">Create a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the flow.</p>
            description: <p>A description for the flow.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>
            definition: <p>A definition of the nodes and the connections between the nodes in the flow.</p>
            flow_identifier: <p>The unique identifier of the flow.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_flow_request.UpdateFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_flow_response.UpdateFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow.update_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_flow_request.UpdateFlowRequest = {
            "name": name,
            "execution_role_arn": execution_role_arn,
            "flow_identifier": flow_identifier,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if definition is not None:
            input_["definition"] = definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_flow(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_flow_response.DeleteFlowResponse":
        """<p>Deletes a flow.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_flow_request.DeleteFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_flow_response.DeleteFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow.delete_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_flow_request.DeleteFlowRequest = {
            "flow_identifier": flow_identifier
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_flows(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_flows_response.ListFlowsResponse":
        """<p>Returns a list of flows and information about each flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html">Manage a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_flows_request.ListFlowsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_flows_response.ListFlowsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flows

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flows.list_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_flows_request.ListFlowsRequest = {}
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

    def iter_list_flows(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.flow_summary.FlowSummary]":
        _token = next_token
        while True:
            _response = self.list_flows(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("flow_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def prepare_flow(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.prepare_flow_response.PrepareFlowResponse":
        """<p>Prepares the <code>DRAFT</code> version of a flow so that it can be invoked. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html">Test a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.prepare_flow_request.PrepareFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.prepare_flow_response.PrepareFlowResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_flow

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.prepare_flow.prepare_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.prepare_flow_request.PrepareFlowRequest = {
            "flow_identifier": flow_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_flow_alias(
        self,
        name: "capo_bedrock_agent.types.name.Name",
        routing_configuration: "capo_bedrock_agent.types.flow_alias_routing_configuration.FlowAliasRoutingConfiguration",
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        concurrency_configuration: Optional[
            "capo_bedrock_agent.types.flow_alias_concurrency_configuration.FlowAliasConcurrencyConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_flow_alias_response.CreateFlowAliasResponse":
        """<p>Creates an alias of a flow for deployment. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html">Deploy a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the alias.</p>
            description: <p>A description for the alias.</p>
            routing_configuration: <p>Contains information about the version to which to map the alias.</p>
            concurrency_configuration: <p>The configuration that specifies how nodes in the flow are executed in parallel.</p>
            flow_identifier: <p>The unique identifier of the flow for which to create an alias.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the alias of the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_flow_alias_request.CreateFlowAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_flow_alias_response.CreateFlowAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow_alias.create_flow_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_flow_alias_request.CreateFlowAliasRequest = {
            "name": name,
            "routing_configuration": routing_configuration,
            "flow_identifier": flow_identifier,
        }
        if description is not None:
            input_["description"] = description
        if concurrency_configuration is not None:
            input_["concurrency_configuration"] = concurrency_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_flow_alias(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        alias_identifier: "capo_bedrock_agent.types.flow_alias_identifier.FlowAliasIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_flow_alias_response.GetFlowAliasResponse":
        """<p>Retrieves information about a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html">Deploy a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow that the alias belongs to.</p>
            alias_identifier: <p>The unique identifier of the alias for which to retrieve information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_flow_alias_request.GetFlowAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_flow_alias_response.GetFlowAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow_alias.get_flow_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_flow_alias_request.GetFlowAliasRequest = {
            "flow_identifier": flow_identifier,
            "alias_identifier": alias_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_flow_alias(
        self,
        name: "capo_bedrock_agent.types.name.Name",
        routing_configuration: "capo_bedrock_agent.types.flow_alias_routing_configuration.FlowAliasRoutingConfiguration",
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        alias_identifier: "capo_bedrock_agent.types.flow_alias_identifier.FlowAliasIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        concurrency_configuration: Optional[
            "capo_bedrock_agent.types.flow_alias_concurrency_configuration.FlowAliasConcurrencyConfiguration"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_flow_alias_response.UpdateFlowAliasResponse":
        """<p>Modifies the alias of a flow. Include both fields that you want to keep and ones that you want to change. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html">Deploy a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>The name of the alias.</p>
            description: <p>A description for the alias.</p>
            routing_configuration: <p>Contains information about the version to which to map the alias.</p>
            concurrency_configuration: <p>The configuration that specifies how nodes in the flow are executed in parallel.</p>
            flow_identifier: <p>The unique identifier of the flow.</p>
            alias_identifier: <p>The unique identifier of the alias.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_flow_alias_request.UpdateFlowAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_flow_alias_response.UpdateFlowAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_flow_alias.update_flow_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_flow_alias_request.UpdateFlowAliasRequest = {
            "name": name,
            "routing_configuration": routing_configuration,
            "flow_identifier": flow_identifier,
            "alias_identifier": alias_identifier,
        }
        if description is not None:
            input_["description"] = description
        if concurrency_configuration is not None:
            input_["concurrency_configuration"] = concurrency_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_flow_alias(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        alias_identifier: "capo_bedrock_agent.types.flow_alias_identifier.FlowAliasIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.delete_flow_alias_response.DeleteFlowAliasResponse":
        """<p>Deletes an alias of a flow.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow that the alias belongs to.</p>
            alias_identifier: <p>The unique identifier of the alias to be deleted.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_flow_alias_request.DeleteFlowAliasRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_flow_alias_response.DeleteFlowAliasResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow_alias

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow_alias.delete_flow_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_flow_alias_request.DeleteFlowAliasRequest = {
            "flow_identifier": flow_identifier,
            "alias_identifier": alias_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_flow_aliases(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_flow_aliases_response.ListFlowAliasesResponse":
        """<p>Returns a list of aliases for a flow.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow for which aliases are being returned.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_flow_aliases_request.ListFlowAliasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_flow_aliases_response.ListFlowAliasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flow_aliases

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flow_aliases.list_flow_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_flow_aliases_request.ListFlowAliasesRequest = {
            "flow_identifier": flow_identifier
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

    def iter_list_flow_aliases(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.flow_alias_summary.FlowAliasSummary]":
        _token = next_token
        while True:
            _response = self.list_flow_aliases(
                flow_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("flow_alias_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_flow_version(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.flow_description.FlowDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_flow_version_response.CreateFlowVersionResponse":
        """<p>Creates a version of the flow that you can deploy. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html">Deploy a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow that you want to create a version of.</p>
            description: <p>A description of the version of the flow.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_flow_version_request.CreateFlowVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_flow_version_response.CreateFlowVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_flow_version.create_flow_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_flow_version_request.CreateFlowVersionRequest = {
            "flow_identifier": flow_identifier
        }
        if description is not None:
            input_["description"] = description
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

    def get_flow_version(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        flow_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        included_data: Optional[
            "capo_bedrock_agent.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_flow_version_response.GetFlowVersionResponse":
        """<p>Retrieves information about a version of a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html">Deploy a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow for which to get information.</p>
            flow_version: <p>The version of the flow for which to get information.</p>
            included_data: <p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_flow_version_request.GetFlowVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_flow_version_response.GetFlowVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_flow_version.get_flow_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_flow_version_request.GetFlowVersionRequest = {
            "flow_identifier": flow_identifier,
            "flow_version": flow_version,
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_flow_version(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        flow_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_flow_version_response.DeleteFlowVersionResponse":
        """<p>Deletes a version of a flow.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow whose version that you want to delete</p>
            flow_version: <p>The version of the flow that you want to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_flow_version_request.DeleteFlowVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_flow_version_response.DeleteFlowVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_flow_version.delete_flow_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_flow_version_request.DeleteFlowVersionRequest = {
            "flow_identifier": flow_identifier,
            "flow_version": flow_version,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_flow_versions(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> (
        "capo_bedrock_agent.types.list_flow_versions_response.ListFlowVersionsResponse"
    ):
        """<p>Returns a list of information about each flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html">Deploy a flow in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_flow_versions_request.ListFlowVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_flow_versions_response.ListFlowVersionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flow_versions

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_flow_versions.list_flow_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_flow_versions_request.ListFlowVersionsRequest = {
            "flow_identifier": flow_identifier
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

    def iter_list_flow_versions(
        self,
        flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.flow_version_summary.FlowVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_flow_versions(
                flow_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("flow_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        ingestion_job_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse":
        """<p>Gets information about a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to get information on.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to get information on.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to get information on.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_ingestion_job_response.GetIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_ingestion_job.get_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_ingestion_job_request.GetIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "ingestion_job_id": ingestion_job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ingestion_jobs(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        filters: Optional[
            "capo_bedrock_agent.types.ingestion_job_filters.IngestionJobFilters"
        ] = None,
        sort_by: Optional[
            "capo_bedrock_agent.types.ingestion_job_sort_by.IngestionJobSortBy"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse":
        """<p>Lists the data ingestion jobs for a data source. The list also includes information about each job.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the list of data ingestion jobs.</p>
            data_source_id: <p>The unique identifier of the data source for the list of data ingestion jobs.</p>
            filters: <p>Contains information about the filters for filtering the data.</p>
            sort_by: <p>Contains details about how to sort the data.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_ingestion_jobs_response.ListIngestionJobsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_ingestion_jobs.list_ingestion_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_ingestion_jobs_request.ListIngestionJobsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    def iter_list_ingestion_jobs(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        filters: Optional[
            "capo_bedrock_agent.types.ingestion_job_filters.IngestionJobFilters"
        ] = None,
        sort_by: Optional[
            "capo_bedrock_agent.types.ingestion_job_sort_by.IngestionJobSortBy"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.ingestion_job_summary.IngestionJobSummary]":
        _token = next_token
        while True:
            _response = self.list_ingestion_jobs(
                knowledge_base_id,
                data_source_id,
                config_overrides=config_overrides,
                filters=filters,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ingestion_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
    ) -> "capo_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse":
        """<p>Begins a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job.</p>
            data_source_id: <p>The unique identifier of the data source you want to ingest into your knowledge base.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p>A description of the data ingestion job.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.start_ingestion_job_response.StartIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.start_ingestion_job.start_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.start_ingestion_job_request.StartIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_ingestion_job(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        ingestion_job_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
    ):
        """<p>Stops a currently running data ingestion job. You can send a <code>StartIngestionJob</code> request again to ingest the rest of your data when you are ready.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base for the data ingestion job you want to stop.</p>
            data_source_id: <p>The unique identifier of the data source for the data ingestion job you want to stop.</p>
            ingestion_job_id: <p>The unique identifier of the data ingestion job you want to stop.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.stop_ingestion_job_response.StopIngestionJobResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.stop_ingestion_job.stop_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.stop_ingestion_job_request.StopIngestionJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "ingestion_job_id": ingestion_job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        document_identifiers: "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse":
        """<p>Deletes documents from a data source and syncs the changes to the knowledge base that is connected to it. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents.delete_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_identifiers": document_identifiers,
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

    def get_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        document_identifiers: "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse":
        """<p>Retrieves specific documents from a data source that is connected to a knowledge base. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document for which to retrieve information.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents.get_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_identifiers": document_identifiers,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def ingest_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        documents: "capo_bedrock_agent.types.knowledge_base_documents.KnowledgeBaseDocuments",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse":
        """<p>Ingests documents directly into the knowledge base that is connected to the data source. The <code>dataSourceType</code> specified in the content for each document must match the type of the data source that you specify in the header. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to ingest the documents into.</p>
            data_source_id: <p>The unique identifier of the data source connected to the knowledge base that you're adding documents to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            documents: <p>A list of objects, each of which contains information about the documents to add.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents.ingest_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "documents": documents,
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

    def list_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse":
        """<p>Retrieves all the documents contained in a data source that is connected to a knowledge base. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents.list_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
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

    def iter_list_knowledge_base_documents(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        data_source_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.knowledge_base_document_detail.KnowledgeBaseDocumentDetail]":
        _token = next_token
        while True:
            _response = self.list_knowledge_base_documents(
                knowledge_base_id,
                data_source_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("document_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        description: "capo_bedrock_agent.types.description.Description",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        knowledge_base_state: Optional[
            "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
        ] = None,
    ) -> "capo_bedrock_agent.types.associate_agent_knowledge_base_response.AssociateAgentKnowledgeBaseResponse":
        """<p>Associates a knowledge base with an agent. If a knowledge base is associated and its <code>indexState</code> is set to <code>Enabled</code>, the agent queries the knowledge base for information to augment its response to the user.</p>

        Args:
            agent_id: <p>The unique identifier of the agent with which you want to associate the knowledge base.</p>
            agent_version: <p>The version of the agent with which you want to associate the knowledge base.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base to associate with the agent.</p>
            description: <p>A description of what the agent should use the knowledge base for.</p>
            knowledge_base_state: <p>Specifies whether to use the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.associate_agent_knowledge_base_request.AssociateAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.associate_agent_knowledge_base_response.AssociateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_knowledge_base.associate_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.associate_agent_knowledge_base_request.AssociateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
            "description": description,
        }
        if knowledge_base_state is not None:
            input_["knowledge_base_state"] = knowledge_base_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_knowledge_base(
        self,
        name: "capo_bedrock_agent.types.name.Name",
        role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn",
        knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        storage_configuration: Optional[
            "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_knowledge_base_response.CreateKnowledgeBaseResponse":
        """<p>Creates a knowledge base. A knowledge base contains your data sources so that Large Language Models (LLMs) can use your data. To create a knowledge base, you must first set up your data sources and configure a supported vector store. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowlege-base-prereq.html">Set up a knowledge base</a>.</p> <note> <p>To create a managed knowledge base, provide a <code>managedKnowledgeBaseConfiguration</code> during creation. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-build-managed.html">Build a managed knowledge base</a>.</p> </note> <ul> <li> <p>Provide the <code>name</code> and an optional <code>description</code>.</p> </li> <li> <p>Provide the Amazon Resource Name (ARN) with permissions to create a knowledge base in the <code>roleArn</code> field.</p> </li> <li> <p>For managed knowledge bases, set <code>embeddingModelType</code> to <code>MANAGED</code> to use the service-managed embedding model, or <code>CUSTOM</code> with an <code>embeddingModelArn</code> to use your own. To use your own KMS key for encryption, provide the ARN in <code>serverSideEncryptionConfiguration</code>. No vector store configuration is required for managed knowledge bases.</p> </li> <li> <p>For self-managed knowledge bases, provide the embedding model to use in the <code>embeddingModelArn</code> field in the <code>knowledgeBaseConfiguration</code> object.</p> </li> <li> <p>For self-managed knowledge bases, provide the configuration for your vector store in the <code>storageConfiguration</code> object.</p> <ul> <li> <p>For an Amazon OpenSearch Service database, use the <code>opensearchServerlessConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-oss.html">Create a vector store in Amazon OpenSearch Service</a>.</p> </li> <li> <p>For an Amazon Aurora database, use the <code>RdsConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html">Create a vector store in Amazon Aurora</a>.</p> </li> <li> <p>For a Pinecone database, use the <code>pineconeConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-pinecone.html">Create a vector store in Pinecone</a>.</p> </li> <li> <p>For a Redis Enterprise Cloud database, use the <code>redisEnterpriseCloudConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-redis.html">Create a vector store in Redis Enterprise Cloud</a>.</p> </li> </ul> </li> </ul>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            name: <p>A name for the knowledge base.</p>
            description: <p>A description of the knowledge base.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>
            knowledge_base_configuration: <p>Contains details about the embeddings model used for the knowledge base.</p>
            storage_configuration: <p>Contains details about the configuration of the vector database used for the knowledge base.</p>
            tags: <p>Specify the key-value pairs for the tags that you want to attach to your knowledge base in this object.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_knowledge_base_request.CreateKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_knowledge_base.create_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_knowledge_base_request.CreateKnowledgeBaseRequest = {
            "name": name,
            "role_arn": role_arn,
            "knowledge_base_configuration": knowledge_base_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse":
        """<p>Deletes a knowledge base. Before deleting a knowledge base, you should disassociate the knowledge base from any agents that it is associated with by making a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DisassociateAgentKnowledgeBase.html">DisassociateAgentKnowledgeBase</a> request.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to delete.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base.delete_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.disassociate_agent_knowledge_base_response.DisassociateAgentKnowledgeBaseResponse":
        """<p>Disassociates a knowledge base from an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent from which to disassociate the knowledge base.</p>
            agent_version: <p>The version of the agent from which to disassociate the knowledge base.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base to disassociate.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.disassociate_agent_knowledge_base_request.DisassociateAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.disassociate_agent_knowledge_base_response.DisassociateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_knowledge_base.disassociate_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.disassociate_agent_knowledge_base_request.DisassociateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_knowledge_base_response.GetAgentKnowledgeBaseResponse":
        """<p>Gets information about a knowledge base associated with an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent with which the knowledge base is associated.</p>
            agent_version: <p>The version of the agent with which the knowledge base is associated.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base associated with the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_knowledge_base_request.GetAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_knowledge_base_response.GetAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_knowledge_base.get_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_knowledge_base_request.GetAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "capo_bedrock_agent.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
    ):
        """<p>Gets information about a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base you want to get information on.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_knowledge_base_request.GetKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base.get_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_knowledge_base_request.GetKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_knowledge_bases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_knowledge_bases_response.ListAgentKnowledgeBasesResponse":
        """<p>Lists knowledge bases associated with an agent and information about each one.</p>

        Args:
            agent_id: <p>The unique identifier of the agent for which to return information about knowledge bases associated with it.</p>
            agent_version: <p>The version of the agent for which to return information about knowledge bases associated with it.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_knowledge_bases_request.ListAgentKnowledgeBasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_knowledge_bases_response.ListAgentKnowledgeBasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_knowledge_bases

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_knowledge_bases.list_agent_knowledge_bases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_knowledge_bases_request.ListAgentKnowledgeBasesRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
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

    def iter_list_agent_knowledge_bases(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.agent_knowledge_base_summary.AgentKnowledgeBaseSummary]":
        _token = next_token
        while True:
            _response = self.list_agent_knowledge_bases(
                agent_id,
                agent_version,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_knowledge_base_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_knowledge_bases_response.ListKnowledgeBasesResponse":
        """<p>Lists the knowledge bases in an account. The list also includesinformation about each knowledge base.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_knowledge_bases_request.ListKnowledgeBasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_knowledge_bases_response.ListKnowledgeBasesResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_bases

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_bases.list_knowledge_bases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_knowledge_bases_request.ListKnowledgeBasesRequest = {}
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

    def iter_list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_bedrock_agent.types.knowledge_base_summary.KnowledgeBaseSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_knowledge_bases(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("knowledge_base_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_agent_knowledge_base(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        knowledge_base_state: Optional[
            "capo_bedrock_agent.types.knowledge_base_state.KnowledgeBaseState"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_knowledge_base_response.UpdateAgentKnowledgeBaseResponse":
        """<p>Updates the configuration for a knowledge base that has been associated with an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent associated with the knowledge base that you want to update.</p>
            agent_version: <p>The version of the agent associated with the knowledge base that you want to update.</p>
            knowledge_base_id: <p>The unique identifier of the knowledge base that has been associated with an agent.</p>
            description: <p>Specifies a new description for the knowledge base associated with an agent.</p>
            knowledge_base_state: <p>Specifies whether the agent uses the knowledge base or not when sending an <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> request.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_knowledge_base_request.UpdateAgentKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_knowledge_base_response.UpdateAgentKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_knowledge_base.update_agent_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_agent_knowledge_base_request.UpdateAgentKnowledgeBaseRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "knowledge_base_id": knowledge_base_id,
        }
        if description is not None:
            input_["description"] = description
        if knowledge_base_state is not None:
            input_["knowledge_base_state"] = knowledge_base_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_knowledge_base(
        self,
        knowledge_base_id: "capo_bedrock_agent.types.id.Id",
        name: "capo_bedrock_agent.types.name.Name",
        role_arn: "capo_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn",
        knowledge_base_configuration: "capo_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.description.Description"
        ] = None,
        storage_configuration: Optional[
            "capo_bedrock_agent.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_knowledge_base_response.UpdateKnowledgeBaseResponse":
        """<p>Updates the configuration of a knowledge base with the fields that you specify. Because all fields will be overwritten, you must include the same values for fields that you want to keep the same.</p> <p>You can change the following fields:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>description</code> </p> </li> <li> <p> <code>roleArn</code> </p> </li> </ul> <p>You can't change the <code>knowledgeBaseConfiguration</code> or <code>storageConfiguration</code> fields, so you must specify the same configurations as when you created the knowledge base. You can send a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html">GetKnowledgeBase</a> request and copy the same configurations.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to update.</p>
            name: <p>Specifies a new name for the knowledge base.</p>
            description: <p>Specifies a new description for the knowledge base.</p>
            role_arn: <p>Specifies a different Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>
            knowledge_base_configuration: <p>Specifies the configuration for the embeddings model used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>
            storage_configuration: <p>Specifies the configuration for the vector store used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_knowledge_base_request.UpdateKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_knowledge_base_response.UpdateKnowledgeBaseResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_knowledge_base

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_knowledge_base.update_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_knowledge_base_request.UpdateKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "role_arn": role_arn,
            "knowledge_base_configuration": knowledge_base_configuration,
        }
        if description is not None:
            input_["description"] = description
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_prompt(
        self,
        name: "capo_bedrock_agent.types.prompt_name.PromptName",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "capo_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_prompt_response.CreatePromptResponse":
        """<p>Creates a prompt in your prompt library that you can add to a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management in Amazon Bedrock</a>, <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html">Create a prompt using Prompt management</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html">Prompt flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the prompt. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_prompt_request.CreatePromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_prompt_response.CreatePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt.create_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_prompt_request.CreatePromptRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_prompt(
        self,
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_version: Optional["capo_bedrock_agent.types.version.Version"] = None,
        included_data: Optional[
            "capo_bedrock_agent.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_prompt_response.GetPromptResponse":
        """<p>Retrieves information about the working draft (<code>DRAFT</code> version) of a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html">View information about prompts using Prompt management</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-view.html">View information about a version of your prompt</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt about which you want to retrieve information. Omit this field to return information about the working draft of the prompt.</p>
            included_data: <p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_prompt_request.GetPromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_prompt_response.GetPromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt.get_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_prompt_request.GetPromptRequest = {
            "prompt_identifier": prompt_identifier
        }
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_prompt(
        self,
        name: "capo_bedrock_agent.types.prompt_name.PromptName",
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "capo_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_prompt_response.UpdatePromptResponse":
        """<p>Modifies a prompt in your prompt library. Include both fields that you want to keep and fields that you want to replace. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management in Amazon Bedrock</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-edit">Edit prompts in your prompt library</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            prompt_identifier: <p>The unique identifier of the prompt.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_prompt_request.UpdatePromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_prompt_response.UpdatePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt.update_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_prompt_request.UpdatePromptRequest = {
            "name": name,
            "prompt_identifier": prompt_identifier,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_prompt(
        self,
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_version: Optional[
            "capo_bedrock_agent.types.numerical_version.NumericalVersion"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_prompt_response.DeletePromptResponse":
        """<p>Deletes a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-delete.html">Delete prompts from the Prompt management tool</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-delete.html">Delete a version of a prompt from the Prompt management tool</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt to delete. To delete the prompt, omit this field.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_prompt_request.DeletePromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_prompt_response.DeletePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt.delete_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_prompt_request.DeletePromptRequest = {
            "prompt_identifier": prompt_identifier
        }
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_prompts(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_identifier: Optional[
            "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_prompts_response.ListPromptsResponse":
        """<p>Returns either information about the working draft (<code>DRAFT</code> version) of each prompt in an account, or information about of all versions of a prompt, depending on whether you include the <code>promptIdentifier</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html">View information about prompts using Prompt management</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt for whose versions you want to return information. Omit this field to list information about all prompts in an account.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_prompts_request.ListPromptsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_prompts_response.ListPromptsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts.list_prompts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_prompts_request.ListPromptsRequest = {}
        if prompt_identifier is not None:
            input_["prompt_identifier"] = prompt_identifier
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

    def iter_list_prompts(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_identifier: Optional[
            "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.prompt_summary.PromptSummary]":
        _token = next_token
        while True:
            _response = self.list_prompts(
                config_overrides=config_overrides,
                prompt_identifier=prompt_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("prompt_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_prompt_version(
        self,
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse":
        """<p>Creates a static snapshot of your prompt that can be deployed to production. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html">Deploy prompts using Prompt management by creating versions</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt that you want to create a version of.</p>
            description: <p>A description for the version of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the version of the prompt. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version.create_prompt_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest = {
            "prompt_identifier": prompt_identifier
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for the resource you specify.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_tags_for_resource

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "capo_bedrock_agent.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.tag_resource_response.TagResourceResponse":
        """<p>Associate tags with a resource. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the Amazon Bedrock User Guide.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>An object containing key-value pairs that define the tags to attach to the resource.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.tag_resource

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "capo_bedrock_agent.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of keys of the tags to remove from the resource.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.untag_resource

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.untag_resource_request.UntagResourceRequest = {
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

    def delete_agent_version(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse":
        """<p>Deletes a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the version belongs to.</p>
            agent_version: <p>The version of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version.delete_agent_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_version(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse":
        """<p>Gets details about a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version.get_agent_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_versions(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse":
        """<p>Lists the versions of an agent and information about each version.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions.list_agent_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest = {
            "agent_id": agent_id
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

    def iter_list_agent_versions(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_bedrock_agent.types.agent_version_summary.AgentVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_agent_versions(
                agent_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()

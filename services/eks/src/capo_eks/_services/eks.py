"""Generated from Smithy shape ``com.amazonaws.eks#AWSWesleyFrontend``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_eks._auth._signers
import capo_eks._auth._sigv4
from capo_eks._auth._identity import Credentials
from capo_eks._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_eks._auth._zapros_handler import AuthMiddleware
from capo_eks._pagination import resolve_path as _resolve_path
from capo_eks._services._aws_config import aws_config
from capo_eks._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_eks.types.access_policy
    import capo_eks.types.access_scope
    import capo_eks.types.activate_certificate_authority_request
    import capo_eks.types.activate_certificate_authority_response
    import capo_eks.types.addon_info
    import capo_eks.types.addon_namespace_config_request
    import capo_eks.types.addon_pod_identity_associations_list
    import capo_eks.types.ami_types
    import capo_eks.types.associate_access_policy_request
    import capo_eks.types.associate_access_policy_response
    import capo_eks.types.associate_encryption_config_request
    import capo_eks.types.associate_encryption_config_response
    import capo_eks.types.associate_identity_provider_config_request
    import capo_eks.types.associate_identity_provider_config_response
    import capo_eks.types.associated_access_policy
    import capo_eks.types.boolean
    import capo_eks.types.boxed_boolean
    import capo_eks.types.boxed_integer
    import capo_eks.types.cancel_update_request
    import capo_eks.types.cancel_update_response
    import capo_eks.types.capability_configuration_request
    import capo_eks.types.capability_delete_propagation_policy
    import capo_eks.types.capability_summary
    import capo_eks.types.capability_type
    import capo_eks.types.capacity_types
    import capo_eks.types.certificate_authority_max_results
    import capo_eks.types.certificate_authority_summary
    import capo_eks.types.cluster_name
    import capo_eks.types.cluster_version_information
    import capo_eks.types.cluster_version_status
    import capo_eks.types.compute_config_request
    import capo_eks.types.connector_config_request
    import capo_eks.types.control_plane_scaling_config
    import capo_eks.types.create_access_config_request
    import capo_eks.types.create_access_entry_request
    import capo_eks.types.create_access_entry_response
    import capo_eks.types.create_addon_request
    import capo_eks.types.create_addon_response
    import capo_eks.types.create_capability_request
    import capo_eks.types.create_capability_response
    import capo_eks.types.create_certificate_authority_request
    import capo_eks.types.create_certificate_authority_response
    import capo_eks.types.create_cluster_request
    import capo_eks.types.create_cluster_response
    import capo_eks.types.create_eks_anywhere_subscription_request
    import capo_eks.types.create_eks_anywhere_subscription_response
    import capo_eks.types.create_fargate_profile_request
    import capo_eks.types.create_fargate_profile_response
    import capo_eks.types.create_nodegroup_request
    import capo_eks.types.create_nodegroup_response
    import capo_eks.types.create_pod_identity_association_request
    import capo_eks.types.create_pod_identity_association_response
    import capo_eks.types.delete_access_entry_request
    import capo_eks.types.delete_access_entry_response
    import capo_eks.types.delete_addon_request
    import capo_eks.types.delete_addon_response
    import capo_eks.types.delete_capability_request
    import capo_eks.types.delete_capability_response
    import capo_eks.types.delete_certificate_authority_request
    import capo_eks.types.delete_certificate_authority_response
    import capo_eks.types.delete_cluster_request
    import capo_eks.types.delete_cluster_response
    import capo_eks.types.delete_eks_anywhere_subscription_request
    import capo_eks.types.delete_eks_anywhere_subscription_response
    import capo_eks.types.delete_fargate_profile_request
    import capo_eks.types.delete_fargate_profile_response
    import capo_eks.types.delete_nodegroup_request
    import capo_eks.types.delete_nodegroup_response
    import capo_eks.types.delete_pod_identity_association_request
    import capo_eks.types.delete_pod_identity_association_response
    import capo_eks.types.deregister_cluster_request
    import capo_eks.types.deregister_cluster_response
    import capo_eks.types.describe_access_entry_request
    import capo_eks.types.describe_access_entry_response
    import capo_eks.types.describe_addon_configuration_request
    import capo_eks.types.describe_addon_configuration_response
    import capo_eks.types.describe_addon_request
    import capo_eks.types.describe_addon_response
    import capo_eks.types.describe_addon_versions_request
    import capo_eks.types.describe_addon_versions_request_max_results
    import capo_eks.types.describe_addon_versions_response
    import capo_eks.types.describe_capability_request
    import capo_eks.types.describe_capability_response
    import capo_eks.types.describe_certificate_authority_request
    import capo_eks.types.describe_certificate_authority_response
    import capo_eks.types.describe_cluster_request
    import capo_eks.types.describe_cluster_response
    import capo_eks.types.describe_cluster_version_max_results
    import capo_eks.types.describe_cluster_versions_request
    import capo_eks.types.describe_cluster_versions_response
    import capo_eks.types.describe_eks_anywhere_subscription_request
    import capo_eks.types.describe_eks_anywhere_subscription_response
    import capo_eks.types.describe_fargate_profile_request
    import capo_eks.types.describe_fargate_profile_response
    import capo_eks.types.describe_identity_provider_config_request
    import capo_eks.types.describe_identity_provider_config_response
    import capo_eks.types.describe_insight_request
    import capo_eks.types.describe_insight_response
    import capo_eks.types.describe_insights_refresh_request
    import capo_eks.types.describe_insights_refresh_response
    import capo_eks.types.describe_nodegroup_request
    import capo_eks.types.describe_nodegroup_response
    import capo_eks.types.describe_pod_identity_association_request
    import capo_eks.types.describe_pod_identity_association_response
    import capo_eks.types.describe_update_request
    import capo_eks.types.describe_update_response
    import capo_eks.types.disassociate_access_policy_request
    import capo_eks.types.disassociate_access_policy_response
    import capo_eks.types.disassociate_identity_provider_config_request
    import capo_eks.types.disassociate_identity_provider_config_response
    import capo_eks.types.eks_anywhere_subscription
    import capo_eks.types.eks_anywhere_subscription_license_type
    import capo_eks.types.eks_anywhere_subscription_name
    import capo_eks.types.eks_anywhere_subscription_status_values
    import capo_eks.types.eks_anywhere_subscription_term
    import capo_eks.types.encryption_config_list
    import capo_eks.types.fargate_profile_selectors
    import capo_eks.types.fargate_profiles_request_max_results
    import capo_eks.types.identity_provider_config
    import capo_eks.types.include_clusters_list
    import capo_eks.types.insight_summary
    import capo_eks.types.insights_filter
    import capo_eks.types.integer
    import capo_eks.types.kube_api_server_config_request
    import capo_eks.types.kube_controller_manager_config_request
    import capo_eks.types.kube_scheduler_config_request
    import capo_eks.types.kubernetes_network_config_request
    import capo_eks.types.labels_map
    import capo_eks.types.launch_template_specification
    import capo_eks.types.list_access_entries_request
    import capo_eks.types.list_access_entries_request_max_results
    import capo_eks.types.list_access_entries_response
    import capo_eks.types.list_access_policies_request
    import capo_eks.types.list_access_policies_request_max_results
    import capo_eks.types.list_access_policies_response
    import capo_eks.types.list_addons_request
    import capo_eks.types.list_addons_request_max_results
    import capo_eks.types.list_addons_response
    import capo_eks.types.list_associated_access_policies_request
    import capo_eks.types.list_associated_access_policies_request_max_results
    import capo_eks.types.list_associated_access_policies_response
    import capo_eks.types.list_capabilities_request
    import capo_eks.types.list_capabilities_request_max_results
    import capo_eks.types.list_capabilities_response
    import capo_eks.types.list_certificate_authorities_request
    import capo_eks.types.list_certificate_authorities_response
    import capo_eks.types.list_clusters_request
    import capo_eks.types.list_clusters_request_max_results
    import capo_eks.types.list_clusters_response
    import capo_eks.types.list_eks_anywhere_subscriptions_request
    import capo_eks.types.list_eks_anywhere_subscriptions_request_max_results
    import capo_eks.types.list_eks_anywhere_subscriptions_response
    import capo_eks.types.list_fargate_profiles_request
    import capo_eks.types.list_fargate_profiles_response
    import capo_eks.types.list_identity_provider_configs_request
    import capo_eks.types.list_identity_provider_configs_request_max_results
    import capo_eks.types.list_identity_provider_configs_response
    import capo_eks.types.list_insights_max_results
    import capo_eks.types.list_insights_request
    import capo_eks.types.list_insights_response
    import capo_eks.types.list_nodegroups_request
    import capo_eks.types.list_nodegroups_request_max_results
    import capo_eks.types.list_nodegroups_response
    import capo_eks.types.list_pod_identity_associations_max_results
    import capo_eks.types.list_pod_identity_associations_request
    import capo_eks.types.list_pod_identity_associations_response
    import capo_eks.types.list_tags_for_resource_request
    import capo_eks.types.list_tags_for_resource_response
    import capo_eks.types.list_updates_request
    import capo_eks.types.list_updates_request_max_results
    import capo_eks.types.list_updates_response
    import capo_eks.types.logging
    import capo_eks.types.node_repair_config
    import capo_eks.types.nodegroup_scaling_config
    import capo_eks.types.nodegroup_update_config
    import capo_eks.types.oidc_identity_provider_config_request
    import capo_eks.types.outpost_config_request
    import capo_eks.types.pod_identity_association_summary
    import capo_eks.types.register_cluster_request
    import capo_eks.types.register_cluster_response
    import capo_eks.types.remote_access_config
    import capo_eks.types.remote_network_config_request
    import capo_eks.types.resolve_conflicts
    import capo_eks.types.role_arn
    import capo_eks.types.rollback_config
    import capo_eks.types.start_insights_refresh_request
    import capo_eks.types.start_insights_refresh_response
    import capo_eks.types.storage_config_request
    import capo_eks.types.string
    import capo_eks.types.string_list
    import capo_eks.types.tag_key_list
    import capo_eks.types.tag_map
    import capo_eks.types.tag_resource_request
    import capo_eks.types.tag_resource_response
    import capo_eks.types.taints_list
    import capo_eks.types.untag_resource_request
    import capo_eks.types.untag_resource_response
    import capo_eks.types.update_access_config_request
    import capo_eks.types.update_access_entry_request
    import capo_eks.types.update_access_entry_response
    import capo_eks.types.update_addon_request
    import capo_eks.types.update_addon_response
    import capo_eks.types.update_capability_configuration
    import capo_eks.types.update_capability_request
    import capo_eks.types.update_capability_response
    import capo_eks.types.update_cluster_config_request
    import capo_eks.types.update_cluster_config_response
    import capo_eks.types.update_cluster_version_request
    import capo_eks.types.update_cluster_version_response
    import capo_eks.types.update_eks_anywhere_subscription_request
    import capo_eks.types.update_eks_anywhere_subscription_response
    import capo_eks.types.update_labels_payload
    import capo_eks.types.update_nodegroup_config_request
    import capo_eks.types.update_nodegroup_config_response
    import capo_eks.types.update_nodegroup_version_request
    import capo_eks.types.update_nodegroup_version_response
    import capo_eks.types.update_pod_identity_association_request
    import capo_eks.types.update_pod_identity_association_response
    import capo_eks.types.update_taints_payload
    import capo_eks.types.upgrade_policy_request
    import capo_eks.types.version_status
    import capo_eks.types.vpc_config_request
    import capo_eks.types.warm_pool_config
    import capo_eks.types.zonal_shift_config_request


class EKSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class EKSClient:
    """A client for the ``EKS`` service.

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
        self._config = EKSClientConfig(
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
        self, config_overrides: Optional[EKSClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EKSClientConfig = config_overrides or {}
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

    def activate_certificate_authority(
        self,
        cluster_name: "capo_eks.types.string.String",
        certificate_authority_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.activate_certificate_authority_response.ActivateCertificateAuthorityResponse":
        """<p>Activates a successor certificate authority (CA) as the signing certificate authority for your cluster, completing a CA rotation.</p> <p>When you activate a successor CA, Amazon EKS promotes it to be the cluster's signer (its <code>signingStatus</code> becomes <code>IN_USE</code>) and the outgoing CA is retired (<code>NOT_USED</code>). The outgoing CA remains in the cluster's trust bundle but no longer signs certificates. The successor CA you activate must already be present on the cluster and fully distributed (its <code>distributionStatus</code> must be <code>COMPLETE</code>). This is an asynchronous operation that returns an <code>update</code> object you can track with <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html"> <code>DescribeUpdate</code> </a>.</p> <p>Before you activate the successor CA, make sure the worker nodes you manage and your external clients have been updated to trust it, so they maintain connectivity to the API server after activation. For a limited period after activation, CA rollback is available to revert to the outgoing CA if needed. If you don't activate the successor CA yourself, Amazon EKS activates it automatically as the expiration deadline approaches. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/certificate-authority-rotation.html">Rotate the Amazon EKS cluster certificate authority</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            certificate_authority_id: <p>The ID of the certificate authority to activate as the cluster's signing certificate authority. This certificate authority must already exist on the cluster and have a <code>distributionStatus</code> of <code>COMPLETE</code>.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.activate_certificate_authority_request.ActivateCertificateAuthorityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.activate_certificate_authority_response.ActivateCertificateAuthorityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.activate_certificate_authority

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.activate_certificate_authority.activate_certificate_authority(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.activate_certificate_authority_request.ActivateCertificateAuthorityRequest = {
            "cluster_name": cluster_name,
            "certificate_authority_id": certificate_authority_id,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_access_policy(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        policy_arn: "capo_eks.types.string.String",
        access_scope: "capo_eks.types.access_scope.AccessScope",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> (
        "capo_eks.types.associate_access_policy_response.AssociateAccessPolicyResponse"
    ):
        """<p>Associates an access policy and its scope to an access entry. For more information about associating access policies, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html">Associating and disassociating access policies to and from access entries</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            principal_arn: <p>The Amazon Resource Name (ARN) of the IAM user or role for the <code>AccessEntry</code> that you're associating the access policy to. </p>
            policy_arn: <p>The ARN of the <code>AccessPolicy</code> that you're associating. For a list of ARNs, use <code>ListAccessPolicies</code>.</p>
            access_scope: <p>The scope for the <code>AccessPolicy</code>. You can scope access policies to an entire cluster or to specific Kubernetes namespaces.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.associate_access_policy_request.AssociateAccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_eks.types.associate_access_policy_response.AssociateAccessPolicyResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.associate_access_policy

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.associate_access_policy.associate_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.associate_access_policy_request.AssociateAccessPolicyRequest = {
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
            "policy_arn": policy_arn,
            "access_scope": access_scope,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_encryption_config(
        self,
        cluster_name: "capo_eks.types.string.String",
        encryption_config: "capo_eks.types.encryption_config_list.EncryptionConfigList",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.associate_encryption_config_response.AssociateEncryptionConfigResponse":
        """<p>Associates an encryption configuration to an existing cluster.</p> <p>Use this API to enable encryption on existing clusters that don't already have encryption enabled. This allows you to implement a defense-in-depth security strategy without migrating applications to new Amazon EKS clusters.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            encryption_config: <p>The configuration you are using for encryption.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.associate_encryption_config_request.AssociateEncryptionConfigRequest]",
        ) -> OperationResponse[
            "capo_eks.types.associate_encryption_config_response.AssociateEncryptionConfigResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.associate_encryption_config

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.associate_encryption_config.associate_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.associate_encryption_config_request.AssociateEncryptionConfigRequest = {
            "cluster_name": cluster_name,
            "encryption_config": encryption_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_identity_provider_config(
        self,
        cluster_name: "capo_eks.types.string.String",
        oidc: "capo_eks.types.oidc_identity_provider_config_request.OidcIdentityProviderConfigRequest",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.associate_identity_provider_config_response.AssociateIdentityProviderConfigResponse":
        """<p>Associates an identity provider configuration to a cluster.</p> <p>If you want to authenticate identities using an identity provider, you can create an identity provider configuration and associate it to your cluster. After configuring authentication to your cluster you can create Kubernetes <code>Role</code> and <code>ClusterRole</code> objects, assign permissions to them, and then bind them to the identities using Kubernetes <code>RoleBinding</code> and <code>ClusterRoleBinding</code> objects. For more information see <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/">Using RBAC Authorization</a> in the Kubernetes documentation.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            oidc: <p>An object representing an OpenID Connect (OIDC) identity provider configuration.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.associate_identity_provider_config_request.AssociateIdentityProviderConfigRequest]",
        ) -> OperationResponse[
            "capo_eks.types.associate_identity_provider_config_response.AssociateIdentityProviderConfigResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.associate_identity_provider_config

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.associate_identity_provider_config.associate_identity_provider_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.associate_identity_provider_config_request.AssociateIdentityProviderConfigRequest = {
            "cluster_name": cluster_name,
            "oidc": oidc,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_update(
        self,
        name: "capo_eks.types.string.String",
        update_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.cancel_update_response.CancelUpdateResponse":
        """<p>Cancels an in-progress update to an Amazon EKS cluster on a best-effort basis. Cancellation is only performed if the update can be cancelled. Currently, this is supported for <code>VersionRollback</code> update types on EKS Auto Mode clusters when nodes are rolling back.</p> <p>A successful cancellation stops the node rollback. After cancellation, nodes converge to the current cluster version honoring configured disruption controls. If the control plane rollback has already begun, the cancellation request fails.</p>

        Args:
            name: <p>The name of the Amazon EKS cluster associated with the update.</p>
            update_id: <p>The ID of the update to cancel.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.invalid_state_exception.InvalidStateException: <p>Amazon EKS detected upgrade readiness issues. Call the <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html"> <code>ListInsights</code> </a> API to view detected upgrade blocking issues. Pass the <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html#API_UpdateClusterVersion_RequestBody"> <code>force</code> </a> flag when updating to override upgrade readiness errors.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.cancel_update_request.CancelUpdateRequest]",
        ) -> OperationResponse[
            "capo_eks.types.cancel_update_response.CancelUpdateResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.cancel_update

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.cancel_update.cancel_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.cancel_update_request.CancelUpdateRequest = {
            "name": name,
            "update_id": update_id,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_access_entry(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        kubernetes_groups: Optional["capo_eks.types.string_list.StringList"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        username: Optional["capo_eks.types.string.String"] = None,
        type: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.create_access_entry_response.CreateAccessEntryResponse":
        """<p>Creates an access entry.</p> <p>An access entry allows an IAM principal to access your cluster. Access entries can replace the need to maintain entries in the <code>aws-auth</code> <code>ConfigMap</code> for authentication. You have the following options for authorizing an IAM principal to access Kubernetes objects on your cluster: Kubernetes role-based access control (RBAC), Amazon EKS, or both. Kubernetes RBAC authorization requires you to create and manage Kubernetes <code>Role</code>, <code>ClusterRole</code>, <code>RoleBinding</code>, and <code>ClusterRoleBinding</code> objects, in addition to managing access entries. If you use Amazon EKS authorization exclusively, you don't need to create and manage Kubernetes <code>Role</code>, <code>ClusterRole</code>, <code>RoleBinding</code>, and <code>ClusterRoleBinding</code> objects.</p> <p>For more information about access entries, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html">Access entries</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            principal_arn: <p>The ARN of the IAM principal for the <code>AccessEntry</code>. You can specify one ARN for each access entry. You can't specify the same ARN in more than one access entry. This value can't be changed after access entry creation.</p> <p>The valid principals differ depending on the type of the access entry in the <code>type</code> field. For <code>STANDARD</code> access entries, you can use every IAM principal type. For nodes (<code>EC2</code> (for EKS Auto Mode), <code>EC2_LINUX</code>, <code>EC2_WINDOWS</code>, <code>FARGATE_LINUX</code>, and <code>HYBRID_LINUX</code>), the only valid ARN is IAM roles. You can't use the STS session principal type with access entries because this is a temporary principal for each session and not a permanent identity that can be assigned permissions.</p> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp">IAM best practices</a> recommend using IAM roles with temporary credentials, rather than IAM users with long-term credentials. </p>
            kubernetes_groups: <p>The value for <code>name</code> that you've specified for <code>kind: Group</code> as a <code>subject</code> in a Kubernetes <code>RoleBinding</code> or <code>ClusterRoleBinding</code> object. Amazon EKS doesn't confirm that the value for <code>name</code> exists in any bindings on your cluster. You can specify one or more names.</p> <p>Kubernetes authorizes the <code>principalArn</code> of the access entry to access any cluster objects that you've specified in a Kubernetes <code>Role</code> or <code>ClusterRole</code> object that is also specified in a binding's <code>roleRef</code>. For more information about creating Kubernetes <code>RoleBinding</code>, <code>ClusterRoleBinding</code>, <code>Role</code>, or <code>ClusterRole</code> objects, see <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/">Using RBAC Authorization in the Kubernetes documentation</a>.</p> <p>If you want Amazon EKS to authorize the <code>principalArn</code> (instead of, or in addition to Kubernetes authorizing the <code>principalArn</code>), you can associate one or more access policies to the access entry using <code>AssociateAccessPolicy</code>. If you associate any access policies, the <code>principalARN</code> has all permissions assigned in the associated access policies and all permissions in any Kubernetes <code>Role</code> or <code>ClusterRole</code> objects that the group names are bound to.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            username: <p>The username to authenticate to Kubernetes with. We recommend not specifying a username and letting Amazon EKS specify it for you. For more information about the value Amazon EKS specifies for you, or constraints before specifying your own username, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#creating-access-entries">Creating access entries</a> in the <i>Amazon EKS User Guide</i>.</p>
            type: <p>The type of the new access entry. Valid values are <code>STANDARD</code>, <code>FARGATE_LINUX</code>, <code>EC2_LINUX</code>, <code>EC2_WINDOWS</code>, <code>EC2</code> (for EKS Auto Mode), <code>HYBRID_LINUX</code>, and <code>HYPERPOD_LINUX</code>. </p> <p>If the <code>principalArn</code> is for an IAM role that's used for self-managed Amazon EC2 nodes, specify <code>EC2_LINUX</code> or <code>EC2_WINDOWS</code>. Amazon EKS grants the necessary permissions to the node for you. If the <code>principalArn</code> is for any other purpose, specify <code>STANDARD</code>. If you don't specify a value, Amazon EKS sets the value to <code>STANDARD</code>. If you have the access mode of the cluster set to <code>API_AND_CONFIG_MAP</code>, it's unnecessary to create access entries for IAM roles used with Fargate profiles or managed Amazon EC2 nodes, because Amazon EKS creates entries in the <code>aws-auth</code> <code>ConfigMap</code> for the roles. You can't change this value once you've created the access entry.</p> <p>If you set the value to <code>EC2_LINUX</code> or <code>EC2_WINDOWS</code>, you can't specify values for <code>kubernetesGroups</code>, or associate an <code>AccessPolicy</code> to the access entry.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_access_entry_request.CreateAccessEntryRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_access_entry_response.CreateAccessEntryResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_access_entry

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_access_entry.create_access_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_access_entry_request.CreateAccessEntryRequest = {
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
        }
        if kubernetes_groups is not None:
            input_["kubernetes_groups"] = kubernetes_groups
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if username is not None:
            input_["username"] = username
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_addon(
        self,
        cluster_name: "capo_eks.types.cluster_name.ClusterName",
        addon_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        addon_version: Optional["capo_eks.types.string.String"] = None,
        service_account_role_arn: Optional["capo_eks.types.role_arn.RoleArn"] = None,
        resolve_conflicts: Optional[
            "capo_eks.types.resolve_conflicts.ResolveConflicts"
        ] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
        configuration_values: Optional["capo_eks.types.string.String"] = None,
        pod_identity_associations: Optional[
            "capo_eks.types.addon_pod_identity_associations_list.AddonPodIdentityAssociationsList"
        ] = None,
        namespace_config: Optional[
            "capo_eks.types.addon_namespace_config_request.AddonNamespaceConfigRequest"
        ] = None,
    ) -> "capo_eks.types.create_addon_response.CreateAddonResponse":
        """<p>Creates an Amazon EKS add-on.</p> <p>Amazon EKS add-ons help to automate the provisioning and lifecycle management of common operational software for Amazon EKS clusters. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html">Amazon EKS add-ons</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            addon_name: <p>The name of the add-on. The name must match one of the names returned by <code>DescribeAddonVersions</code>.</p>
            addon_version: <p>The version of the add-on. The version must match one of the versions returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html"> <code>DescribeAddonVersions</code> </a>.</p>
            service_account_role_arn: <p>The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-on's service account. The role must be assigned the IAM permissions required by the add-on. If you don't specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html">Amazon EKS node IAM role</a> in the <i>Amazon EKS User Guide</i>.</p> <note> <p>To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html">Enabling IAM roles for service accounts on your cluster</a> in the <i>Amazon EKS User Guide</i>.</p> </note>
            resolve_conflicts: <p>How to resolve field value conflicts for an Amazon EKS add-on. Conflicts are handled based on the value you choose:</p> <ul> <li> <p> <b>None</b> – If the self-managed version of the add-on is installed on your cluster, Amazon EKS doesn't change the value. Creation of the add-on might fail.</p> </li> <li> <p> <b>Overwrite</b> – If the self-managed version of the add-on is installed on your cluster and the Amazon EKS default value is different than the existing value, Amazon EKS changes the value to the Amazon EKS default value.</p> </li> <li> <p> <b>Preserve</b> – This is similar to the NONE option. If the self-managed version of the add-on is installed on your cluster Amazon EKS doesn't change the add-on resource properties. Creation of the add-on might fail if conflicts are detected. This option works differently during the update operation. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html"> <code>UpdateAddon</code> </a>.</p> </li> </ul> <p>If you don't currently have the self-managed version of the add-on installed on your cluster, the Amazon EKS add-on is installed. Amazon EKS sets all values to default values, regardless of the option that you specify.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            configuration_values: <p>The set of configuration values for the add-on that's created. The values that you provide are validated against the schema returned by <code>DescribeAddonConfiguration</code>.</p>
            pod_identity_associations: <p>An array of EKS Pod Identity associations to be created. Each association maps a Kubernetes service account to an IAM role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html">Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p>
            namespace_config: <p>The namespace configuration for the addon. If specified, this will override the default namespace for the addon.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_addon_request.CreateAddonRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_addon_response.CreateAddonResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_addon

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_addon.create_addon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_addon_request.CreateAddonRequest = {
            "cluster_name": cluster_name,
            "addon_name": addon_name,
        }
        if addon_version is not None:
            input_["addon_version"] = addon_version
        if service_account_role_arn is not None:
            input_["service_account_role_arn"] = service_account_role_arn
        if resolve_conflicts is not None:
            input_["resolve_conflicts"] = resolve_conflicts
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if configuration_values is not None:
            input_["configuration_values"] = configuration_values
        if pod_identity_associations is not None:
            input_["pod_identity_associations"] = pod_identity_associations
        if namespace_config is not None:
            input_["namespace_config"] = namespace_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_capability(
        self,
        capability_name: "capo_eks.types.string.String",
        cluster_name: "capo_eks.types.string.String",
        type: "capo_eks.types.capability_type.CapabilityType",
        role_arn: "capo_eks.types.string.String",
        delete_propagation_policy: "capo_eks.types.capability_delete_propagation_policy.CapabilityDeletePropagationPolicy",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        configuration: Optional[
            "capo_eks.types.capability_configuration_request.CapabilityConfigurationRequest"
        ] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
    ) -> "capo_eks.types.create_capability_response.CreateCapabilityResponse":
        """<p>Creates a managed capability resource for an Amazon EKS cluster.</p> <p>Capabilities provide fully managed capabilities to build and scale with Kubernetes. When you create a capability, Amazon EKSprovisions and manages the infrastructure required to run the capability outside of your cluster. This approach reduces operational overhead and preserves cluster resources.</p> <p>You can only create one Capability of each type on a given Amazon EKS cluster. Valid types are Argo CD for declarative GitOps deployment, Amazon Web Services Controllers for Kubernetes (ACK) for resource management, and Kube Resource Orchestrator (KRO) for Kubernetes custom resource orchestration.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/capabilities.html">EKS Capabilities</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            capability_name: <p>A unique name for the capability. The name must be unique within your cluster and can contain alphanumeric characters, hyphens, and underscores.</p>
            cluster_name: <p>The name of the Amazon EKS cluster where you want to create the capability.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is valid for 24 hours after creation. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.</p>
            type: <p>The type of capability to create. Valid values are:</p> <ul> <li> <p> <code>ACK</code> – Amazon Web Services Controllers for Kubernetes (ACK), which lets you manage resources directly from Kubernetes.</p> </li> <li> <p> <code>ARGOCD</code> – Argo CD for GitOps-based continuous delivery.</p> </li> <li> <p> <code>KRO</code> – Kube Resource Orchestrator (KRO) for composing and managing custom Kubernetes resources.</p> </li> </ul>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with Amazon Web Services services. This role must have a trust policy that allows the EKS service principal to assume it, and it must have the necessary permissions for the capability type you're creating.</p> <p>For ACK capabilities, the role needs permissions to manage the resources you want to control through Kubernetes. For Argo CD capabilities, the role needs permissions to access Git repositories and Secrets Manager. For KRO capabilities, the role needs permissions based on the resources you'll be orchestrating.</p>
            configuration: <p>The configuration settings for the capability. The structure of this object varies depending on the capability type. For Argo CD capabilities, you can configure IAM Identity CenterIAM; Identity Center integration, RBAC role mappings, and network access settings.</p>
            delete_propagation_policy: <p>Specifies how Kubernetes resources managed by the capability should be handled when the capability is deleted. Currently, the only supported value is <code>RETAIN</code> which retains all Kubernetes resources managed by the capability when the capability is deleted.</p> <p>Because resources are retained, all Kubernetes resources created by the capability should be deleted from the cluster before deleting the capability itself. After the capability is deleted, these resources become difficult to manage because the controller is no longer available.</p>

        Raises:
            capo_eks.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management</a> in the <i>IAM User Guide</i>. </p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_capability_request.CreateCapabilityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_capability_response.CreateCapabilityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_capability

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_capability.create_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_capability_request.CreateCapabilityRequest = {
            "capability_name": capability_name,
            "cluster_name": cluster_name,
            "type": type,
            "role_arn": role_arn,
            "delete_propagation_policy": delete_propagation_policy,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if configuration is not None:
            input_["configuration"] = configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_certificate_authority(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.create_certificate_authority_response.CreateCertificateAuthorityResponse":
        """<p>Appends a successor certificate authority (CA) to your cluster, beginning the CA rotation process.</p> <p>A cluster certificate authority is the root of trust for your cluster's control plane. It signs the certificates that secure communication between the Kubernetes API server and its clients, and its public certificate is distributed to your cluster's trust bundle so that worker nodes and clients can verify the API server's identity. Each cluster can have at most two certificate authorities at a time: the outgoing CA that's currently signing (its <code>signingStatus</code> is <code>IN_USE</code>) and one successor CA (<code>signingStatus</code> of <code>NOT_USED</code>) that you can later activate to complete the rotation.</p> <p>Appending a successor CA adds its public certificate to the cluster's trust bundle so that the cluster trusts both CAs simultaneously (the dual trust period), but it doesn't begin signing certificates. Amazon EKS then distributes the successor CA to the Amazon Web Services managed components in your cluster; you can track this through the CA's <code>distributionStatus</code>. The successor CA can't be activated until its <code>distributionStatus</code> is <code>COMPLETE</code>. To activate it as the cluster's signer, use <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ActivateCertificateAuthority.html"> <code>ActivateCertificateAuthority</code> </a>. This is an asynchronous operation that returns an <code>update</code> object. If you don't append a successor CA yourself, Amazon EKS appends one automatically before the outgoing CA approaches expiration.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/certificate-authority-rotation.html">Rotate the Amazon EKS cluster certificate authority</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_certificate_authority_request.CreateCertificateAuthorityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_certificate_authority_response.CreateCertificateAuthorityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_certificate_authority

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_certificate_authority.create_certificate_authority(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_certificate_authority_request.CreateCertificateAuthorityRequest = {
            "cluster_name": cluster_name
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cluster(
        self,
        name: "capo_eks.types.cluster_name.ClusterName",
        role_arn: "capo_eks.types.string.String",
        resources_vpc_config: "capo_eks.types.vpc_config_request.VpcConfigRequest",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        version: Optional["capo_eks.types.string.String"] = None,
        kubernetes_network_config: Optional[
            "capo_eks.types.kubernetes_network_config_request.KubernetesNetworkConfigRequest"
        ] = None,
        logging: Optional["capo_eks.types.logging.Logging"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
        encryption_config: Optional[
            "capo_eks.types.encryption_config_list.EncryptionConfigList"
        ] = None,
        outpost_config: Optional[
            "capo_eks.types.outpost_config_request.OutpostConfigRequest"
        ] = None,
        access_config: Optional[
            "capo_eks.types.create_access_config_request.CreateAccessConfigRequest"
        ] = None,
        bootstrap_self_managed_addons: Optional[
            "capo_eks.types.boxed_boolean.BoxedBoolean"
        ] = None,
        upgrade_policy: Optional[
            "capo_eks.types.upgrade_policy_request.UpgradePolicyRequest"
        ] = None,
        zonal_shift_config: Optional[
            "capo_eks.types.zonal_shift_config_request.ZonalShiftConfigRequest"
        ] = None,
        remote_network_config: Optional[
            "capo_eks.types.remote_network_config_request.RemoteNetworkConfigRequest"
        ] = None,
        compute_config: Optional[
            "capo_eks.types.compute_config_request.ComputeConfigRequest"
        ] = None,
        storage_config: Optional[
            "capo_eks.types.storage_config_request.StorageConfigRequest"
        ] = None,
        deletion_protection: Optional[
            "capo_eks.types.boxed_boolean.BoxedBoolean"
        ] = None,
        control_plane_scaling_config: Optional[
            "capo_eks.types.control_plane_scaling_config.ControlPlaneScalingConfig"
        ] = None,
        kube_api_server_config: Optional[
            "capo_eks.types.kube_api_server_config_request.KubeApiServerConfigRequest"
        ] = None,
        kube_scheduler_config: Optional[
            "capo_eks.types.kube_scheduler_config_request.KubeSchedulerConfigRequest"
        ] = None,
        kube_controller_manager_config: Optional[
            "capo_eks.types.kube_controller_manager_config_request.KubeControllerManagerConfigRequest"
        ] = None,
    ) -> "capo_eks.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates an Amazon EKS control plane.</p> <p>The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, such as <code>etcd</code> and the API server. The control plane runs in an account managed by Amazon Web Services, and the Kubernetes API is exposed by the Amazon EKS API server endpoint. Each Amazon EKS cluster control plane is single tenant and unique. It runs on its own set of Amazon EC2 instances.</p> <p>The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the nodes (for example, to support <code>kubectl exec</code>, <code>logs</code>, and <code>proxy</code> data flows).</p> <p>Amazon EKS nodes run in your Amazon Web Services account and connect to your cluster's control plane over the Kubernetes API server endpoint and a certificate file that is created for your cluster.</p> <p>You can use the <code>endpointPublicAccess</code> and <code>endpointPrivateAccess</code> parameters to enable or disable public and private access to your cluster's Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. The endpoint domain name and IP address family depends on the value of the <code>ipFamily</code> for the cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html">Amazon EKS Cluster Endpoint Access Control</a> in the <i> <i>Amazon EKS User Guide</i> </i>. </p> <p>You can use the <code>logging</code> parameter to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Cluster Control Plane Logs</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <note> <p>CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see <a href="http://aws.amazon.com/cloudwatch/pricing/">CloudWatch Pricing</a>.</p> </note> <p>In most cases, it takes several minutes to create a cluster. After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch nodes into your cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-auth.html">Allowing users to access your cluster</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html">Launching Amazon EKS nodes</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            name: <p>The unique name to give to your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can't be longer than 100 characters. The name must be unique within the Amazon Web Services Region and Amazon Web Services account that you're creating the cluster in.</p>
            version: <p>The desired Kubernetes version for your cluster. If you don't specify a value here, the default version available in Amazon EKS is used.</p> <note> <p>The default version might not be the latest version available.</p> </note>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to Amazon Web Services API operations on your behalf. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html">Amazon EKS Service IAM Role</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>
            resources_vpc_config: <p>The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the <i>Amazon EKS User Guide</i>. You must specify at least two subnets. You can specify up to five security groups. However, we recommend that you use a dedicated security group for your cluster control plane.</p>
            kubernetes_network_config: <p>The Kubernetes network configuration for the cluster.</p>
            logging: <p>Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs . By default, cluster control plane logs aren't exported to CloudWatch Logs . For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Cluster control plane logs</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <note> <p>CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see <a href="http://aws.amazon.com/cloudwatch/pricing/">CloudWatch Pricing</a>.</p> </note>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            encryption_config: <p>The encryption configuration for the cluster.</p>
            outpost_config: <p>An object representing the configuration of your local Amazon EKS cluster on an Amazon Web Services Outpost. Before creating a local cluster on an Outpost, review <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-overview.html">Local clusters for Amazon EKS on Amazon Web Services Outposts</a> in the <i>Amazon EKS User Guide</i>. This object isn't available for creating Amazon EKS clusters on the Amazon Web Services cloud.</p>
            access_config: <p>The access configuration for the cluster.</p>
            bootstrap_self_managed_addons: <p>If you set this value to <code>False</code> when creating a cluster, the default networking add-ons will not be installed.</p> <p>The default networking add-ons include <code>vpc-cni</code>, <code>coredns</code>, and <code>kube-proxy</code>.</p> <p>Use this option when you plan to install third-party alternative add-ons or self-manage the default networking add-ons.</p>
            upgrade_policy: <p>New clusters, by default, have extended support enabled. You can disable extended support when creating a cluster by setting this value to <code>STANDARD</code>.</p>
            zonal_shift_config: <p>Enable or disable ARC zonal shift for the cluster. If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.</p> <p>Zonal shift is a feature of Amazon Application Recovery Controller (ARC). ARC zonal shift is designed to be a temporary measure that allows you to move traffic for a resource away from an impaired AZ until the zonal shift expires or you cancel it. You can extend the zonal shift if necessary.</p> <p>You can start a zonal shift for an Amazon EKS cluster, or you can allow Amazon Web Services to do it for you by enabling <i>zonal autoshift</i>. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. Additionally, any ALB or NLB handling ingress traffic for applications in your Amazon EKS cluster will automatically route traffic to targets in the healthy AZs. For more information about zonal shift in EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html">Learn about Amazon Application Recovery Controller (ARC) Zonal Shift in Amazon EKS</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>
            remote_network_config: <p>The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.</p>
            compute_config: <p>Enable or disable the compute capability of EKS Auto Mode when creating your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your Amazon Web Services account</p>
            storage_config: <p>Enable or disable the block storage capability of EKS Auto Mode when creating your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your Amazon Web Services account.</p>
            deletion_protection: <p>Indicates whether to enable deletion protection for the cluster. When enabled, the cluster cannot be deleted unless deletion protection is first disabled. This helps prevent accidental cluster deletion. Default value is <code>false</code>.</p>
            control_plane_scaling_config: <p>The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.</p>
            kube_api_server_config: <p>The Kubernetes API server configuration for the new cluster.</p>
            kube_scheduler_config: <p>The Kubernetes scheduler configuration for the new cluster.</p>
            kube_controller_manager_config: <p>The Kubernetes controller manager configuration for the new cluster.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.unsupported_availability_zone_exception.UnsupportedAvailabilityZoneException: <p>At least one of your specified cluster subnets is in an Availability Zone that does not support Amazon EKS. The exception output specifies the supported Availability Zones for your account, from which you can choose subnets for your cluster.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new cluster
            The following example creates an Amazon EKS cluster called prod.

            >>> client.create_cluster(name='prod', version='1.10', role_arn='arn:aws:iam::012345678910:role/eks-service-role-AWSServiceRoleForAmazonEKS-J7ONKE3BQ4PI', resources_vpc_config={'subnetIds': ['subnet-6782e71e', 'subnet-e7e761ac'], 'securityGroupIds': ['sg-6979fe18']}, client_request_token='1d2129a1-3d38-460a-9756-e5b91fddb951')
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_cluster

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_cluster_request.CreateClusterRequest = {
            "name": name,
            "role_arn": role_arn,
            "resources_vpc_config": resources_vpc_config,
        }
        if version is not None:
            input_["version"] = version
        if kubernetes_network_config is not None:
            input_["kubernetes_network_config"] = kubernetes_network_config
        if logging is not None:
            input_["logging"] = logging
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if encryption_config is not None:
            input_["encryption_config"] = encryption_config
        if outpost_config is not None:
            input_["outpost_config"] = outpost_config
        if access_config is not None:
            input_["access_config"] = access_config
        if bootstrap_self_managed_addons is not None:
            input_["bootstrap_self_managed_addons"] = bootstrap_self_managed_addons
        if upgrade_policy is not None:
            input_["upgrade_policy"] = upgrade_policy
        if zonal_shift_config is not None:
            input_["zonal_shift_config"] = zonal_shift_config
        if remote_network_config is not None:
            input_["remote_network_config"] = remote_network_config
        if compute_config is not None:
            input_["compute_config"] = compute_config
        if storage_config is not None:
            input_["storage_config"] = storage_config
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if control_plane_scaling_config is not None:
            input_["control_plane_scaling_config"] = control_plane_scaling_config
        if kube_api_server_config is not None:
            input_["kube_api_server_config"] = kube_api_server_config
        if kube_scheduler_config is not None:
            input_["kube_scheduler_config"] = kube_scheduler_config
        if kube_controller_manager_config is not None:
            input_["kube_controller_manager_config"] = kube_controller_manager_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_eks_anywhere_subscription(
        self,
        name: "capo_eks.types.eks_anywhere_subscription_name.EksAnywhereSubscriptionName",
        term: "capo_eks.types.eks_anywhere_subscription_term.EksAnywhereSubscriptionTerm",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        license_quantity: Optional["capo_eks.types.integer.Integer"] = None,
        license_type: Optional[
            "capo_eks.types.eks_anywhere_subscription_license_type.EksAnywhereSubscriptionLicenseType"
        ] = None,
        auto_renew: Optional["capo_eks.types.boolean.Boolean"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
    ) -> "capo_eks.types.create_eks_anywhere_subscription_response.CreateEksAnywhereSubscriptionResponse":
        """<p>Creates an EKS Anywhere subscription. When a subscription is created, it is a contract agreement for the length of the term specified in the request. Licenses that are used to validate support are provisioned in Amazon Web Services License Manager and the caller account is granted access to EKS Anywhere Curated Packages.</p>

        Args:
            name: <p>The unique name for your subscription. It must be unique in your Amazon Web Services account in the Amazon Web Services Region you're creating the subscription in. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphabetic character and can't be longer than 100 characters.</p>
            term: <p>An object representing the term duration and term unit type of your subscription. This determines the term length of your subscription. Valid values are MONTHS for term unit and 12 or 36 for term duration, indicating a 12 month or 36 month subscription. This value cannot be changed after creating the subscription.</p>
            license_quantity: <p>The number of licenses to purchase with the subscription. Valid values are between 1 and 100. This value can't be changed after creating the subscription.</p>
            license_type: <p>The license type for all licenses in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster.</p>
            auto_renew: <p>A boolean indicating whether the subscription auto renews at the end of the term.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>The metadata for a subscription to assist with categorization and organization. Each tag consists of a key and an optional value. Subscription tags don't propagate to any other resources associated with the subscription.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_eks_anywhere_subscription_request.CreateEksAnywhereSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_eks_anywhere_subscription_response.CreateEksAnywhereSubscriptionResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_eks_anywhere_subscription

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_eks_anywhere_subscription.create_eks_anywhere_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_eks_anywhere_subscription_request.CreateEksAnywhereSubscriptionRequest = {
            "name": name,
            "term": term,
        }
        if license_quantity is not None:
            input_["license_quantity"] = license_quantity
        if license_type is not None:
            input_["license_type"] = license_type
        if auto_renew is not None:
            input_["auto_renew"] = auto_renew
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_fargate_profile(
        self,
        fargate_profile_name: "capo_eks.types.string.String",
        cluster_name: "capo_eks.types.string.String",
        pod_execution_role_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        subnets: Optional["capo_eks.types.string_list.StringList"] = None,
        selectors: Optional[
            "capo_eks.types.fargate_profile_selectors.FargateProfileSelectors"
        ] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
    ) -> "capo_eks.types.create_fargate_profile_response.CreateFargateProfileResponse":
        """<p>Creates an Fargate profile for your Amazon EKS cluster. You must have at least one Fargate profile in a cluster to be able to run pods on Fargate.</p> <p>The Fargate profile allows an administrator to declare which pods run on Fargate and specify which pods run on which Fargate profile. This declaration is done through the profile's selectors. Each profile can have up to five selectors that contain a namespace and labels. A namespace is required for every selector. The label field consists of multiple optional key-value pairs. Pods that match the selectors are scheduled on Fargate. If a to-be-scheduled pod matches any of the selectors in the Fargate profile, then that pod is run on Fargate.</p> <p>When you create a Fargate profile, you must specify a pod execution role to use with the pods that are scheduled with the profile. This role is added to the cluster's Kubernetes <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/">Role Based Access Control</a> (RBAC) for authorization so that the <code>kubelet</code> that is running on the Fargate infrastructure can register with your Amazon EKS cluster so that it can appear in your cluster as a node. The pod execution role also provides IAM permissions to the Fargate infrastructure to allow read access to Amazon ECR image repositories. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html">Pod Execution Role</a> in the <i>Amazon EKS User Guide</i>.</p> <p>Fargate profiles are immutable. However, you can create a new updated profile to replace an existing profile and then delete the original after the updated profile has finished creating.</p> <p>If any Fargate profiles in a cluster are in the <code>DELETING</code> status, you must wait for that Fargate profile to finish deleting before you can create any other profiles in that cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html">Fargate profile</a> in the <i>Amazon EKS User Guide</i>.</p>

        Args:
            fargate_profile_name: <p>The name of the Fargate profile.</p>
            cluster_name: <p>The name of your cluster.</p>
            pod_execution_role_arn: <p>The Amazon Resource Name (ARN) of the <code>Pod</code> execution role to use for a <code>Pod</code> that matches the selectors in the Fargate profile. The <code>Pod</code> execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html"> <code>Pod</code> execution role</a> in the <i>Amazon EKS User Guide</i>.</p>
            subnets: <p>The IDs of subnets to launch a <code>Pod</code> into. A <code>Pod</code> running on Fargate isn't assigned a public IP address, so only private subnets (with no direct route to an Internet Gateway) are accepted for this parameter.</p>
            selectors: <p>The selectors to match for a <code>Pod</code> to use this Fargate profile. Each selector must have an associated Kubernetes <code>namespace</code>. Optionally, you can also specify <code>labels</code> for a <code>namespace</code>. You may specify up to five selectors in a Fargate profile.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.unsupported_availability_zone_exception.UnsupportedAvailabilityZoneException: <p>At least one of your specified cluster subnets is in an Availability Zone that does not support Amazon EKS. The exception output specifies the supported Availability Zones for your account, from which you can choose subnets for your cluster.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_fargate_profile_request.CreateFargateProfileRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_fargate_profile_response.CreateFargateProfileResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_fargate_profile

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_fargate_profile.create_fargate_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_fargate_profile_request.CreateFargateProfileRequest = {
            "fargate_profile_name": fargate_profile_name,
            "cluster_name": cluster_name,
            "pod_execution_role_arn": pod_execution_role_arn,
        }
        if subnets is not None:
            input_["subnets"] = subnets
        if selectors is not None:
            input_["selectors"] = selectors
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_nodegroup(
        self,
        cluster_name: "capo_eks.types.string.String",
        nodegroup_name: "capo_eks.types.string.String",
        subnets: "capo_eks.types.string_list.StringList",
        node_role: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        scaling_config: Optional[
            "capo_eks.types.nodegroup_scaling_config.NodegroupScalingConfig"
        ] = None,
        disk_size: Optional["capo_eks.types.boxed_integer.BoxedInteger"] = None,
        instance_types: Optional["capo_eks.types.string_list.StringList"] = None,
        ami_type: Optional["capo_eks.types.ami_types.AMITypes"] = None,
        remote_access: Optional[
            "capo_eks.types.remote_access_config.RemoteAccessConfig"
        ] = None,
        labels: Optional["capo_eks.types.labels_map.labelsMap"] = None,
        taints: Optional["capo_eks.types.taints_list.taintsList"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        launch_template: Optional[
            "capo_eks.types.launch_template_specification.LaunchTemplateSpecification"
        ] = None,
        update_config: Optional[
            "capo_eks.types.nodegroup_update_config.NodegroupUpdateConfig"
        ] = None,
        node_repair_config: Optional[
            "capo_eks.types.node_repair_config.NodeRepairConfig"
        ] = None,
        capacity_type: Optional["capo_eks.types.capacity_types.CapacityTypes"] = None,
        version: Optional["capo_eks.types.string.String"] = None,
        release_version: Optional["capo_eks.types.string.String"] = None,
        warm_pool_config: Optional[
            "capo_eks.types.warm_pool_config.WarmPoolConfig"
        ] = None,
    ) -> "capo_eks.types.create_nodegroup_response.CreateNodegroupResponse":
        """<p>Creates a managed node group for an Amazon EKS cluster.</p> <p>You can only create a node group for your cluster that is equal to the current Kubernetes version for the cluster. All node groups are created with the latest AMI release version for the respective minor Kubernetes version of the cluster, unless you deploy a custom AMI using a launch template.</p> <p>For later updates, you will only be able to update a node group using a launch template only if it was originally deployed with a launch template. Additionally, the launch template ID or name must match what was used when the node group was created. You can update the launch template version with necessary changes. For more information about using launch templates, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a>.</p> <p>An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and associated Amazon EC2 instances that are managed by Amazon Web Services for an Amazon EKS cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html">Managed node groups</a> in the <i>Amazon EKS User Guide</i>.</p> <note> <p>Windows AMI types are only supported for commercial Amazon Web Services Regions that support Windows on Amazon EKS.</p> </note>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            nodegroup_name: <p>The unique name to give your node group.</p>
            scaling_config: <p>The scaling configuration details for the Auto Scaling group that is created for your node group.</p>
            disk_size: <p>The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB for Linux and Bottlerocket. The default disk size is 50 GiB for Windows. If you specify <code>launchTemplate</code>, then don't specify <code>diskSize</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            subnets: <p>The subnets to use for the Auto Scaling group that is created for your node group. If you specify <code>launchTemplate</code>, then don't specify <code> <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html">SubnetId</a> </code> in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            instance_types: <p>Specify the instance types for a node group. If you specify a GPU instance type, make sure to also specify an applicable GPU AMI type with the <code>amiType</code> parameter. If you specify <code>launchTemplate</code>, then you can specify zero or one instance type in your launch template <i>or</i> you can specify 0-20 instance types for <code>instanceTypes</code>. If however, you specify an instance type in your launch template <i>and</i> specify any <code>instanceTypes</code>, the node group deployment will fail. If you don't specify an instance type in a launch template or for <code>instanceTypes</code>, then <code>t3.medium</code> is used, by default. If you specify <code>Spot</code> for <code>capacityType</code>, then we recommend specifying multiple values for <code>instanceTypes</code>. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html#managed-node-group-capacity-types">Managed node group capacity types</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            ami_type: <p>The AMI type for your node group. If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>amiType</code>, or the node group deployment will fail. If your launch template uses a Windows custom AMI, then add <code>eks:kube-proxy-windows</code> to your Windows nodes <code>rolearn</code> in the <code>aws-auth</code> <code>ConfigMap</code>. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            remote_access: <p>The remote access configuration to use with your node group. For Linux, the protocol is SSH. For Windows, the protocol is RDP. If you specify <code>launchTemplate</code>, then don't specify <code>remoteAccess</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            node_role: <p>The Amazon Resource Name (ARN) of the IAM role to associate with your node group. The Amazon EKS worker node <code>kubelet</code> daemon makes calls to Amazon Web Services APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch nodes and register them into a cluster, you must create an IAM role for those nodes to use when they are launched. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html">Amazon EKS node IAM role</a> in the <i> <i>Amazon EKS User Guide</i> </i>. If you specify <code>launchTemplate</code>, then don't specify <code> <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html">IamInstanceProfile</a> </code> in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            labels: <p>The Kubernetes <code>labels</code> to apply to the nodes in the node group when they are created.</p>
            taints: <p>The Kubernetes taints to be applied to the nodes in the node group. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html">Node taints on managed node groups</a>.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            launch_template: <p>An object representing a node group's launch template specification. When using this object, don't directly specify <code>instanceTypes</code>, <code>diskSize</code>, or <code>remoteAccess</code>. You cannot later specify a different launch template ID or name than what was used to create the node group.</p> <p>Make sure that the launch template meets the requirements in <code>launchTemplateSpecification</code>. Also refer to <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            update_config: <p>The node group update configuration.</p>
            node_repair_config: <p>The node auto repair configuration for the node group.</p>
            capacity_type: <p>The capacity type for your node group.</p>
            version: <p>The Kubernetes version to use for your managed nodes. By default, the Kubernetes version of the cluster is used, and this is the only accepted specified value. If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>version</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            release_version: <p>The AMI version of the Amazon EKS optimized AMI to use with your node group. By default, the latest available AMI version for the node group's current Kubernetes version is used. For information about Linux versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html">Amazon EKS optimized Amazon Linux AMI versions</a> in the <i>Amazon EKS User Guide</i>. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html">Amazon EKS optimized Windows AMI versions</a> in the <i>Amazon EKS User Guide</i>.</p> <p>If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>releaseVersion</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            warm_pool_config: <p>The warm pool configuration for the node group. Warm pools maintain pre-initialized EC2 instances that can quickly join your cluster during scale-out events, improving application scaling performance and reducing costs.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_nodegroup_request.CreateNodegroupRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_nodegroup_response.CreateNodegroupResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_nodegroup

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_nodegroup.create_nodegroup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_nodegroup_request.CreateNodegroupRequest = {
            "cluster_name": cluster_name,
            "nodegroup_name": nodegroup_name,
            "subnets": subnets,
            "node_role": node_role,
        }
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if disk_size is not None:
            input_["disk_size"] = disk_size
        if instance_types is not None:
            input_["instance_types"] = instance_types
        if ami_type is not None:
            input_["ami_type"] = ami_type
        if remote_access is not None:
            input_["remote_access"] = remote_access
        if labels is not None:
            input_["labels"] = labels
        if taints is not None:
            input_["taints"] = taints
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if launch_template is not None:
            input_["launch_template"] = launch_template
        if update_config is not None:
            input_["update_config"] = update_config
        if node_repair_config is not None:
            input_["node_repair_config"] = node_repair_config
        if capacity_type is not None:
            input_["capacity_type"] = capacity_type
        if version is not None:
            input_["version"] = version
        if release_version is not None:
            input_["release_version"] = release_version
        if warm_pool_config is not None:
            input_["warm_pool_config"] = warm_pool_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_pod_identity_association(
        self,
        cluster_name: "capo_eks.types.string.String",
        namespace: "capo_eks.types.string.String",
        service_account: "capo_eks.types.string.String",
        role_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
        disable_session_tags: Optional[
            "capo_eks.types.boxed_boolean.BoxedBoolean"
        ] = None,
        target_role_arn: Optional["capo_eks.types.string.String"] = None,
        policy: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.create_pod_identity_association_response.CreatePodIdentityAssociationResponse":
        """<p>Creates an EKS Pod Identity association between a service account in an Amazon EKS cluster and an IAM role with <i>EKS Pod Identity</i>. Use EKS Pod Identity to give temporary IAM credentials to Pods and the credentials are rotated automatically.</p> <p>Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.</p> <p>If a Pod uses a service account that has an association, Amazon EKS sets environment variables in the containers of the Pod. The environment variables configure the Amazon Web Services SDKs, including the Command Line Interface, to use the EKS Pod Identity credentials.</p> <p>EKS Pod Identity is a simpler method than <i>IAM roles for service accounts</i>, as this method doesn't use OIDC identity providers. Additionally, you can configure a role for EKS Pod Identity once, and reuse it across clusters.</p> <p>Similar to Amazon Web Services IAM behavior, EKS Pod Identity associations are eventually consistent, and may take several seconds to be effective after the initial API call returns successfully. You must design your applications to account for these potential delays. We recommend that you don’t include association create/updates in the critical, high-availability code paths of your application. Instead, make changes in a separate initialization or setup routine that you run less frequently.</p> <p>You can set a <i>target IAM role</i> in the same or a different account for advanced scenarios. With a target role, EKS Pod Identity automatically performs two role assumptions in sequence: first assuming the role in the association that is in this account, then using those credentials to assume the target IAM role. This process provides your Pod with temporary credentials that have the permissions defined in the target role, allowing secure access to resources in another Amazon Web Services account.</p>

        Args:
            cluster_name: <p>The name of the cluster to create the EKS Pod Identity association in.</p>
            namespace: <p>The name of the Kubernetes namespace inside the cluster to create the EKS Pod Identity association in. The service account and the Pods that use the service account must be in this namespace.</p>
            service_account: <p>The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to associate with the service account. The EKS Pod Identity agent manages credentials to assume this role for applications in the containers in the Pods that use this service account.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource – 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length – 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length – 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            disable_session_tags: <p>Disable the automatic sessions tags that are appended by EKS Pod Identity.</p> <p>EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to Amazon Web Services resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags">List of session tags added by EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p> <p>Amazon Web Services compresses inline session policies, managed policy ARNs, and session tags into a packed binary format that has a separate limit. If you receive a <code>PackedPolicyTooLarge</code> error indicating the packed binary format has exceeded the size limit, you can attempt to reduce the size by disabling the session tags added by EKS Pod Identity.</p>
            target_role_arn: <p>The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.</p> <p>When you run applications on Amazon EKS, your application might need to access Amazon Web Services resources from a different role that exists in the same or different Amazon Web Services account. For example, your application running in “Account A” might need to access resources, such as Amazon S3 buckets in “Account B” or within “Account A” itself. You can create a association to access Amazon Web Services resources in “Account B” by creating two IAM roles: a role in “Account A” and a role in “Account B” (which can be the same or different account), each with the necessary trust and permission policies. After you provide these roles in the <i>IAM role</i> and <i>Target IAM role</i> fields, EKS will perform role chaining to ensure your application gets the required permissions. This means Role A will assume Role B, allowing your Pods to securely access resources like S3 buckets in the target account.</p>
            policy: <p>An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.</p> <p> <b>Important considerations</b> </p> <ul> <li> <p> <b>Session tags:</b> When using this policy, <code>disableSessionTags</code> must be set to <code>true</code>.</p> </li> <li> <p> <b>Target role permissions:</b> If you specify both a <code>TargetRoleArn</code> and a policy, the policy restrictions apply only to the target role's permissions, not to the initial role used for assuming the target role.</p> </li> </ul>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.create_pod_identity_association_request.CreatePodIdentityAssociationRequest]",
        ) -> OperationResponse[
            "capo_eks.types.create_pod_identity_association_response.CreatePodIdentityAssociationResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.create_pod_identity_association

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.create_pod_identity_association.create_pod_identity_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.create_pod_identity_association_request.CreatePodIdentityAssociationRequest = {
            "cluster_name": cluster_name,
            "namespace": namespace,
            "service_account": service_account,
            "role_arn": role_arn,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if disable_session_tags is not None:
            input_["disable_session_tags"] = disable_session_tags
        if target_role_arn is not None:
            input_["target_role_arn"] = target_role_arn
        if policy is not None:
            input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_access_entry(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.delete_access_entry_response.DeleteAccessEntryResponse":
        """<p>Deletes an access entry.</p> <p>Deleting an access entry of a type other than <code>Standard</code> can cause your cluster to function improperly. If you delete an access entry in error, you can recreate it.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            principal_arn: <p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>

        Raises:
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_access_entry_request.DeleteAccessEntryRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_access_entry_response.DeleteAccessEntryResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_access_entry

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_access_entry.delete_access_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_access_entry_request.DeleteAccessEntryRequest = {
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_addon(
        self,
        cluster_name: "capo_eks.types.cluster_name.ClusterName",
        addon_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        preserve: Optional["capo_eks.types.boolean.Boolean"] = None,
    ) -> "capo_eks.types.delete_addon_response.DeleteAddonResponse":
        """<p>Deletes an Amazon EKS add-on.</p> <p>When you remove an add-on, it's deleted from the cluster. You can always manually start an add-on on the cluster using the Kubernetes API.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            addon_name: <p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>.</p>
            preserve: <p>Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isn't removed.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_addon_request.DeleteAddonRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_addon_response.DeleteAddonResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_addon

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_addon.delete_addon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_addon_request.DeleteAddonRequest = {
            "cluster_name": cluster_name,
            "addon_name": addon_name,
        }
        if preserve is not None:
            input_["preserve"] = preserve

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_capability(
        self,
        cluster_name: "capo_eks.types.string.String",
        capability_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.delete_capability_response.DeleteCapabilityResponse":
        """<p>Deletes a managed capability from your Amazon EKS cluster. When you delete a capability, Amazon EKS removes the capability infrastructure but retains all resources that were managed by the capability.</p> <p>Before deleting a capability, you should delete all Kubernetes resources that were created by the capability. After the capability is deleted, these resources become difficult to manage because the controller that managed them is no longer available. To delete resources before removing the capability, use <code>kubectl delete</code> or remove them through your GitOps workflow.</p>

        Args:
            cluster_name: <p>The name of the Amazon EKS cluster that contains the capability you want to delete.</p>
            capability_name: <p>The name of the capability to delete.</p>

        Raises:
            capo_eks.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management</a> in the <i>IAM User Guide</i>. </p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_capability_request.DeleteCapabilityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_capability_response.DeleteCapabilityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_capability

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_capability.delete_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_capability_request.DeleteCapabilityRequest = {
            "cluster_name": cluster_name,
            "capability_name": capability_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_certificate_authority(
        self,
        cluster_name: "capo_eks.types.string.String",
        certificate_authority_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.delete_certificate_authority_response.DeleteCertificateAuthorityResponse":
        """<p>Deletes a certificate authority (CA) from your cluster.</p> <p>Deleting a certificate authority removes its public certificate from the cluster's trust bundle. You can't delete the certificate authority that's currently signing certificates for the cluster (its <code>signingStatus</code> is <code>IN_USE</code>) — to remove the outgoing CA, first activate the successor CA with <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ActivateCertificateAuthority.html"> <code>ActivateCertificateAuthority</code> </a>. Amazon EKS also protects a successor CA from deletion in certain cases to keep a valid rotation path — for example, a successor that Amazon EKS appended can't be deleted while it's the only successor on the cluster. This is an asynchronous operation that returns an <code>update</code> object.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            certificate_authority_id: <p>The ID of the certificate authority to delete. You can't delete the certificate authority that's currently signing certificates for the cluster.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_certificate_authority_request.DeleteCertificateAuthorityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_certificate_authority_response.DeleteCertificateAuthorityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_certificate_authority

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_certificate_authority.delete_certificate_authority(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_certificate_authority_request.DeleteCertificateAuthorityRequest = {
            "cluster_name": cluster_name,
            "certificate_authority_id": certificate_authority_id,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cluster(
        self,
        name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes an Amazon EKS cluster control plane.</p> <p>If you have active services and ingress resources in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html">Deleting a cluster</a> in the <i>Amazon EKS User Guide</i>.</p> <p>If you have managed node groups or Fargate profiles attached to the cluster, you must delete them first. For more information, see <code>DeleteNodgroup</code> and <code>DeleteFargateProfile</code>.</p>

        Args:
            name: <p>The name of the cluster to delete.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a cluster
            This example command deletes a cluster named `devel` in your default region.

            >>> client.delete_cluster(name='devel')
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_cluster

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_cluster_request.DeleteClusterRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_eks_anywhere_subscription(
        self,
        id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.delete_eks_anywhere_subscription_response.DeleteEksAnywhereSubscriptionResponse":
        """<p>Deletes an expired or inactive subscription. Deleting inactive subscriptions removes them from the Amazon Web Services Management Console view and from list/describe API responses. Subscriptions can only be cancelled within 7 days of creation and are cancelled by creating a ticket in the Amazon Web Services Support Center. </p>

        Args:
            id: <p>The ID of the subscription.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_eks_anywhere_subscription_request.DeleteEksAnywhereSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_eks_anywhere_subscription_response.DeleteEksAnywhereSubscriptionResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_eks_anywhere_subscription

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_eks_anywhere_subscription.delete_eks_anywhere_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_eks_anywhere_subscription_request.DeleteEksAnywhereSubscriptionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_fargate_profile(
        self,
        cluster_name: "capo_eks.types.string.String",
        fargate_profile_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.delete_fargate_profile_response.DeleteFargateProfileResponse":
        """<p>Deletes an Fargate profile.</p> <p>When you delete a Fargate profile, any <code>Pod</code> running on Fargate that was created with the profile is deleted. If the <code>Pod</code> matches another Fargate profile, then it is scheduled on Fargate with that profile. If it no longer matches any Fargate profiles, then it's not scheduled on Fargate and may remain in a pending state.</p> <p>Only one Fargate profile in a cluster can be in the <code>DELETING</code> status at a time. You must wait for a Fargate profile to finish deleting before you can delete any other profiles in that cluster.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            fargate_profile_name: <p>The name of the Fargate profile to delete.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_fargate_profile_request.DeleteFargateProfileRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_fargate_profile_response.DeleteFargateProfileResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_fargate_profile

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_fargate_profile.delete_fargate_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_fargate_profile_request.DeleteFargateProfileRequest = {
            "cluster_name": cluster_name,
            "fargate_profile_name": fargate_profile_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_nodegroup(
        self,
        cluster_name: "capo_eks.types.string.String",
        nodegroup_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.delete_nodegroup_response.DeleteNodegroupResponse":
        """<p>Deletes a managed node group.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            nodegroup_name: <p>The name of the node group to delete.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_nodegroup_request.DeleteNodegroupRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_nodegroup_response.DeleteNodegroupResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_nodegroup

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_nodegroup.delete_nodegroup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_nodegroup_request.DeleteNodegroupRequest = {
            "cluster_name": cluster_name,
            "nodegroup_name": nodegroup_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_pod_identity_association(
        self,
        cluster_name: "capo_eks.types.string.String",
        association_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.delete_pod_identity_association_response.DeletePodIdentityAssociationResponse":
        """<p>Deletes a EKS Pod Identity association.</p> <p>The temporary Amazon Web Services credentials from the previous IAM role session might still be valid until the session expiry. If you need to immediately revoke the temporary session credentials, then go to the role in the IAM console.</p>

        Args:
            cluster_name: <p>The cluster name that</p>
            association_id: <p>The ID of the association to be deleted.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.delete_pod_identity_association_request.DeletePodIdentityAssociationRequest]",
        ) -> OperationResponse[
            "capo_eks.types.delete_pod_identity_association_response.DeletePodIdentityAssociationResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.delete_pod_identity_association

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.delete_pod_identity_association.delete_pod_identity_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.delete_pod_identity_association_request.DeletePodIdentityAssociationRequest = {
            "cluster_name": cluster_name,
            "association_id": association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_cluster(
        self,
        name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.deregister_cluster_response.DeregisterClusterResponse":
        """<p>Deregisters a connected cluster to remove it from the Amazon EKS control plane.</p> <p>A connected cluster is a Kubernetes cluster that you've connected to your control plane using the <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-connector.html">Amazon EKS Connector</a>.</p>

        Args:
            name: <p>The name of the connected cluster to deregister.</p>

        Raises:
            capo_eks.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management</a> in the <i>IAM User Guide</i>. </p>
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.deregister_cluster_request.DeregisterClusterRequest]",
        ) -> OperationResponse[
            "capo_eks.types.deregister_cluster_response.DeregisterClusterResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.deregister_cluster

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.deregister_cluster.deregister_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.deregister_cluster_request.DeregisterClusterRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_access_entry(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_access_entry_response.DescribeAccessEntryResponse":
        """<p>Describes an access entry.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            principal_arn: <p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>

        Raises:
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_access_entry_request.DescribeAccessEntryRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_access_entry_response.DescribeAccessEntryResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_access_entry

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_access_entry.describe_access_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_access_entry_request.DescribeAccessEntryRequest = {
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_addon(
        self,
        cluster_name: "capo_eks.types.cluster_name.ClusterName",
        addon_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_addon_response.DescribeAddonResponse":
        """<p>Describes an Amazon EKS add-on.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            addon_name: <p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_addon_request.DescribeAddonRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_addon_response.DescribeAddonResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_addon

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_addon.describe_addon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_addon_request.DescribeAddonRequest = {
            "cluster_name": cluster_name,
            "addon_name": addon_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_addon_configuration(
        self,
        addon_name: "capo_eks.types.string.String",
        addon_version: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_addon_configuration_response.DescribeAddonConfigurationResponse":
        """<p>Returns configuration options.</p>

        Args:
            addon_name: <p>The name of the add-on. The name must match one of the names returned by <code>DescribeAddonVersions</code>.</p>
            addon_version: <p>The version of the add-on. The version must match one of the versions returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html"> <code>DescribeAddonVersions</code> </a>.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_addon_configuration_request.DescribeAddonConfigurationRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_addon_configuration_response.DescribeAddonConfigurationResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_addon_configuration

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_addon_configuration.describe_addon_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_addon_configuration_request.DescribeAddonConfigurationRequest = {
            "addon_name": addon_name,
            "addon_version": addon_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_addon_versions(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        kubernetes_version: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.describe_addon_versions_request_max_results.DescribeAddonVersionsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        addon_name: Optional["capo_eks.types.string.String"] = None,
        types: Optional["capo_eks.types.string_list.StringList"] = None,
        publishers: Optional["capo_eks.types.string_list.StringList"] = None,
        owners: Optional["capo_eks.types.string_list.StringList"] = None,
    ) -> (
        "capo_eks.types.describe_addon_versions_response.DescribeAddonVersionsResponse"
    ):
        """<p>Describes the versions for an add-on.</p> <p>Information such as the Kubernetes versions that you can use the add-on with, the <code>owner</code>, <code>publisher</code>, and the <code>type</code> of the add-on are returned.</p>

        Args:
            kubernetes_version: <p>The Kubernetes versions that you can use the add-on with.</p>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            addon_name: <p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>.</p>
            types: <p>The type of the add-on. For valid <code>types</code>, don't specify a value for this property.</p>
            publishers: <p>The publisher of the add-on. For valid <code>publishers</code>, don't specify a value for this property.</p>
            owners: <p>The owner of the add-on. For valid <code>owners</code>, don't specify a value for this property.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_addon_versions_request.DescribeAddonVersionsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_addon_versions_response.DescribeAddonVersionsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_addon_versions

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_addon_versions.describe_addon_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_addon_versions_request.DescribeAddonVersionsRequest = {}
        if kubernetes_version is not None:
            input_["kubernetes_version"] = kubernetes_version
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if addon_name is not None:
            input_["addon_name"] = addon_name
        if types is not None:
            input_["types"] = types
        if publishers is not None:
            input_["publishers"] = publishers
        if owners is not None:
            input_["owners"] = owners

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_addon_versions(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        kubernetes_version: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.describe_addon_versions_request_max_results.DescribeAddonVersionsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        addon_name: Optional["capo_eks.types.string.String"] = None,
        types: Optional["capo_eks.types.string_list.StringList"] = None,
        publishers: Optional["capo_eks.types.string_list.StringList"] = None,
        owners: Optional["capo_eks.types.string_list.StringList"] = None,
    ) -> "Iterator[capo_eks.types.addon_info.AddonInfo]":
        _token = next_token
        while True:
            _response = self.describe_addon_versions(
                config_overrides=config_overrides,
                kubernetes_version=kubernetes_version,
                max_results=max_results,
                next_token=_token,
                addon_name=addon_name,
                types=types,
                publishers=publishers,
                owners=owners,
            )
            _page = _resolve_path(_response, ("addons",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_capability(
        self,
        cluster_name: "capo_eks.types.string.String",
        capability_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_capability_response.DescribeCapabilityResponse":
        """<p>Returns detailed information about a specific managed capability in your Amazon EKS cluster, including its current status, configuration, health information, and any issues that may be affecting its operation.</p>

        Args:
            cluster_name: <p>The name of the Amazon EKS cluster that contains the capability you want to describe.</p>
            capability_name: <p>The name of the capability to describe.</p>

        Raises:
            capo_eks.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management</a> in the <i>IAM User Guide</i>. </p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_capability_request.DescribeCapabilityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_capability_response.DescribeCapabilityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_capability

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_capability.describe_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_capability_request.DescribeCapabilityRequest = {
            "cluster_name": cluster_name,
            "capability_name": capability_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_certificate_authority(
        self,
        cluster_name: "capo_eks.types.string.String",
        certificate_authority_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_certificate_authority_response.DescribeCertificateAuthorityResponse":
        """<p>Returns detailed information about a certificate authority (CA) in your cluster, including its validity period, signing and distribution status, provenance, scheduled auto-activation events, and public certificate data.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            certificate_authority_id: <p>The ID of the certificate authority to describe.</p>

        Raises:
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_certificate_authority_request.DescribeCertificateAuthorityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_certificate_authority_response.DescribeCertificateAuthorityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_certificate_authority

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_certificate_authority.describe_certificate_authority(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_certificate_authority_request.DescribeCertificateAuthorityRequest = {
            "cluster_name": cluster_name,
            "certificate_authority_id": certificate_authority_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cluster(
        self,
        name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_cluster_response.DescribeClusterResponse":
        """<p>Describes an Amazon EKS cluster.</p> <p>The API server endpoint and certificate authority data returned by this operation are required for <code>kubelet</code> and <code>kubectl</code> to communicate with your Kubernetes API server. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html">Creating or updating a <code>kubeconfig</code> file for an Amazon EKS cluster</a>.</p> <note> <p>The API server endpoint and certificate authority data aren't available until the cluster reaches the <code>ACTIVE</code> state.</p> </note>

        Args:
            name: <p>The name of your cluster.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a cluster
            This example command provides a description of the specified cluster in your default region.

            >>> client.describe_cluster(name='devel')
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_cluster_request.DescribeClusterRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_cluster_response.DescribeClusterResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_cluster

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_cluster.describe_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_cluster_request.DescribeClusterRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cluster_versions(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        cluster_type: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.describe_cluster_version_max_results.DescribeClusterVersionMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        default_only: Optional["capo_eks.types.boxed_boolean.BoxedBoolean"] = None,
        include_all: Optional["capo_eks.types.boxed_boolean.BoxedBoolean"] = None,
        cluster_versions: Optional["capo_eks.types.string_list.StringList"] = None,
        status: Optional[
            "capo_eks.types.cluster_version_status.ClusterVersionStatus"
        ] = None,
        version_status: Optional["capo_eks.types.version_status.VersionStatus"] = None,
    ) -> "capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse":
        """<p>Lists available Kubernetes versions for Amazon EKS clusters.</p>

        Args:
            cluster_type: <p>The type of cluster to filter versions by.</p>
            max_results: <p>Maximum number of results to return.</p>
            next_token: <p>Pagination token for the next set of results.</p>
            default_only: <p>Filter to show only default versions.</p>
            include_all: <p>Include all available versions in the response.</p>
            cluster_versions: <p>List of specific cluster versions to describe.</p>
            status: <important> <p>This field is deprecated. Use <code>versionStatus</code> instead, as that field matches for input and output of this action.</p> </important> <p>Filter versions by their current status.</p>
            version_status: <p>Filter versions by their current status.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_cluster_versions

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_cluster_versions.describe_cluster_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest = {}
        if cluster_type is not None:
            input_["cluster_type"] = cluster_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if default_only is not None:
            input_["default_only"] = default_only
        if include_all is not None:
            input_["include_all"] = include_all
        if cluster_versions is not None:
            input_["cluster_versions"] = cluster_versions
        if status is not None:
            input_["status"] = status
        if version_status is not None:
            input_["version_status"] = version_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_cluster_versions(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        cluster_type: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.describe_cluster_version_max_results.DescribeClusterVersionMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        default_only: Optional["capo_eks.types.boxed_boolean.BoxedBoolean"] = None,
        include_all: Optional["capo_eks.types.boxed_boolean.BoxedBoolean"] = None,
        cluster_versions: Optional["capo_eks.types.string_list.StringList"] = None,
        status: Optional[
            "capo_eks.types.cluster_version_status.ClusterVersionStatus"
        ] = None,
        version_status: Optional["capo_eks.types.version_status.VersionStatus"] = None,
    ) -> (
        "Iterator[capo_eks.types.cluster_version_information.ClusterVersionInformation]"
    ):
        _token = next_token
        while True:
            _response = self.describe_cluster_versions(
                config_overrides=config_overrides,
                cluster_type=cluster_type,
                max_results=max_results,
                next_token=_token,
                default_only=default_only,
                include_all=include_all,
                cluster_versions=cluster_versions,
                status=status,
                version_status=version_status,
            )
            _page = _resolve_path(_response, ("cluster_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_eks_anywhere_subscription(
        self,
        id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_eks_anywhere_subscription_response.DescribeEksAnywhereSubscriptionResponse":
        """<p>Returns descriptive information about a subscription.</p>

        Args:
            id: <p>The ID of the subscription.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_eks_anywhere_subscription_request.DescribeEksAnywhereSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_eks_anywhere_subscription_response.DescribeEksAnywhereSubscriptionResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_eks_anywhere_subscription

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_eks_anywhere_subscription.describe_eks_anywhere_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_eks_anywhere_subscription_request.DescribeEksAnywhereSubscriptionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fargate_profile(
        self,
        cluster_name: "capo_eks.types.string.String",
        fargate_profile_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_fargate_profile_response.DescribeFargateProfileResponse":
        """<p>Describes an Fargate profile.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            fargate_profile_name: <p>The name of the Fargate profile to describe.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_fargate_profile_request.DescribeFargateProfileRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_fargate_profile_response.DescribeFargateProfileResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_fargate_profile

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_fargate_profile.describe_fargate_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_fargate_profile_request.DescribeFargateProfileRequest = {
            "cluster_name": cluster_name,
            "fargate_profile_name": fargate_profile_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_identity_provider_config(
        self,
        cluster_name: "capo_eks.types.string.String",
        identity_provider_config: "capo_eks.types.identity_provider_config.IdentityProviderConfig",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_identity_provider_config_response.DescribeIdentityProviderConfigResponse":
        """<p>Describes an identity provider configuration.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            identity_provider_config: <p>An object representing an identity provider configuration.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_identity_provider_config_request.DescribeIdentityProviderConfigRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_identity_provider_config_response.DescribeIdentityProviderConfigResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_identity_provider_config

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_identity_provider_config.describe_identity_provider_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_identity_provider_config_request.DescribeIdentityProviderConfigRequest = {
            "cluster_name": cluster_name,
            "identity_provider_config": identity_provider_config,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_insight(
        self,
        cluster_name: "capo_eks.types.string.String",
        id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_insight_response.DescribeInsightResponse":
        """<p>Returns details about an insight that you specify using its ID.</p>

        Args:
            cluster_name: <p>The name of the cluster to describe the insight for.</p>
            id: <p>The identity of the insight to describe.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_insight_request.DescribeInsightRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_insight_response.DescribeInsightResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_insight

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_insight.describe_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_insight_request.DescribeInsightRequest = {
            "cluster_name": cluster_name,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_insights_refresh(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_insights_refresh_response.DescribeInsightsRefreshResponse":
        """<p>Returns the status of the latest on-demand cluster insights refresh operation.</p>

        Args:
            cluster_name: <p>The name of the cluster associated with the insights refresh operation.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_insights_refresh_request.DescribeInsightsRefreshRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_insights_refresh_response.DescribeInsightsRefreshResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_insights_refresh

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_insights_refresh.describe_insights_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_insights_refresh_request.DescribeInsightsRefreshRequest = {
            "cluster_name": cluster_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_nodegroup(
        self,
        cluster_name: "capo_eks.types.string.String",
        nodegroup_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_nodegroup_response.DescribeNodegroupResponse":
        """<p>Describes a managed node group.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            nodegroup_name: <p>The name of the node group to describe.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_nodegroup_request.DescribeNodegroupRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_nodegroup_response.DescribeNodegroupResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_nodegroup

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_nodegroup.describe_nodegroup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_nodegroup_request.DescribeNodegroupRequest = {
            "cluster_name": cluster_name,
            "nodegroup_name": nodegroup_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_pod_identity_association(
        self,
        cluster_name: "capo_eks.types.string.String",
        association_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.describe_pod_identity_association_response.DescribePodIdentityAssociationResponse":
        """<p>Returns descriptive information about an EKS Pod Identity association.</p> <p>This action requires the ID of the association. You can get the ID from the response to the <code>CreatePodIdentityAssocation</code> for newly created associations. Or, you can list the IDs for associations with <code>ListPodIdentityAssociations</code> and filter the list by namespace or service account.</p>

        Args:
            cluster_name: <p>The name of the cluster that the association is in.</p>
            association_id: <p>The ID of the association that you want the description of.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_pod_identity_association_request.DescribePodIdentityAssociationRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_pod_identity_association_response.DescribePodIdentityAssociationResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_pod_identity_association

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_pod_identity_association.describe_pod_identity_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_pod_identity_association_request.DescribePodIdentityAssociationRequest = {
            "cluster_name": cluster_name,
            "association_id": association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_update(
        self,
        name: "capo_eks.types.string.String",
        update_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        nodegroup_name: Optional["capo_eks.types.string.String"] = None,
        addon_name: Optional["capo_eks.types.string.String"] = None,
        capability_name: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.describe_update_response.DescribeUpdateResponse":
        """<p>Describes an update to an Amazon EKS resource.</p> <p>When the status of the update is <code>Successful</code>, the update is complete. If an update fails, the status is <code>Failed</code>, and an error detail explains the reason for the failure.</p>

        Args:
            name: <p>The name of the Amazon EKS cluster associated with the update.</p>
            update_id: <p>The ID of the update to describe.</p>
            nodegroup_name: <p>The name of the Amazon EKS node group associated with the update. This parameter is required if the update is a node group update.</p>
            addon_name: <p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>. This parameter is required if the update is an add-on update.</p>
            capability_name: <p>The name of the capability for which you want to describe updates.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.describe_update_request.DescribeUpdateRequest]",
        ) -> OperationResponse[
            "capo_eks.types.describe_update_response.DescribeUpdateResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.describe_update

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.describe_update.describe_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.describe_update_request.DescribeUpdateRequest = {
            "name": name,
            "update_id": update_id,
        }
        if nodegroup_name is not None:
            input_["nodegroup_name"] = nodegroup_name
        if addon_name is not None:
            input_["addon_name"] = addon_name
        if capability_name is not None:
            input_["capability_name"] = capability_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_access_policy(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        policy_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.disassociate_access_policy_response.DisassociateAccessPolicyResponse":
        """<p>Disassociates an access policy from an access entry.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            principal_arn: <p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>
            policy_arn: <p>The ARN of the policy to disassociate from the access entry. For a list of associated policies ARNs, use <code>ListAssociatedAccessPolicies</code>.</p>

        Raises:
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.disassociate_access_policy_request.DisassociateAccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_eks.types.disassociate_access_policy_response.DisassociateAccessPolicyResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.disassociate_access_policy

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.disassociate_access_policy.disassociate_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.disassociate_access_policy_request.DisassociateAccessPolicyRequest = {
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
            "policy_arn": policy_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_identity_provider_config(
        self,
        cluster_name: "capo_eks.types.string.String",
        identity_provider_config: "capo_eks.types.identity_provider_config.IdentityProviderConfig",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.disassociate_identity_provider_config_response.DisassociateIdentityProviderConfigResponse":
        """<p>Disassociates an identity provider configuration from a cluster.</p> <p>If you disassociate an identity provider from your cluster, users included in the provider can no longer access the cluster. However, you can still access the cluster with IAM principals.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            identity_provider_config: <p>An object representing an identity provider configuration.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.disassociate_identity_provider_config_request.DisassociateIdentityProviderConfigRequest]",
        ) -> OperationResponse[
            "capo_eks.types.disassociate_identity_provider_config_response.DisassociateIdentityProviderConfigResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.disassociate_identity_provider_config

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.disassociate_identity_provider_config.disassociate_identity_provider_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.disassociate_identity_provider_config_request.DisassociateIdentityProviderConfigRequest = {
            "cluster_name": cluster_name,
            "identity_provider_config": identity_provider_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_access_entries(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        associated_policy_arn: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_access_entries_request_max_results.ListAccessEntriesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_access_entries_response.ListAccessEntriesResponse":
        """<p>Lists the access entries for your cluster.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            associated_policy_arn: <p>The ARN of an <code>AccessPolicy</code>. When you specify an access policy ARN, only the access entries associated to that access policy are returned. For a list of available policy ARNs, use <code>ListAccessPolicies</code>.</p>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_access_entries_request.ListAccessEntriesRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_access_entries_response.ListAccessEntriesResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_access_entries

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_access_entries.list_access_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_access_entries_request.ListAccessEntriesRequest = {
            "cluster_name": cluster_name
        }
        if associated_policy_arn is not None:
            input_["associated_policy_arn"] = associated_policy_arn
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

    def iter_list_access_entries(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        associated_policy_arn: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_access_entries_request_max_results.ListAccessEntriesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_access_entries(
                cluster_name,
                config_overrides=config_overrides,
                associated_policy_arn=associated_policy_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("access_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_access_policies(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_access_policies_request_max_results.ListAccessPoliciesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_access_policies_response.ListAccessPoliciesResponse":
        """<p>Lists the available access policies. </p>

        Args:
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_access_policies_request.ListAccessPoliciesRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_access_policies_response.ListAccessPoliciesResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_access_policies

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_access_policies.list_access_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_access_policies_request.ListAccessPoliciesRequest = {}
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

    def iter_list_access_policies(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_access_policies_request_max_results.ListAccessPoliciesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.access_policy.AccessPolicy]":
        _token = next_token
        while True:
            _response = self.list_access_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("access_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_addons(
        self,
        cluster_name: "capo_eks.types.cluster_name.ClusterName",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_addons_request_max_results.ListAddonsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_addons_response.ListAddonsResponse":
        """<p>Lists the installed add-ons.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_addons_request.ListAddonsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_addons_response.ListAddonsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_addons

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_addons.list_addons(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_addons_request.ListAddonsRequest = {
            "cluster_name": cluster_name
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

    def iter_list_addons(
        self,
        cluster_name: "capo_eks.types.cluster_name.ClusterName",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_addons_request_max_results.ListAddonsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_addons(
                cluster_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("addons",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_associated_access_policies(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_associated_access_policies_request_max_results.ListAssociatedAccessPoliciesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_associated_access_policies_response.ListAssociatedAccessPoliciesResponse":
        """<p>Lists the access policies associated with an access entry.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            principal_arn: <p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_associated_access_policies_request.ListAssociatedAccessPoliciesRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_associated_access_policies_response.ListAssociatedAccessPoliciesResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_associated_access_policies

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_associated_access_policies.list_associated_access_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_associated_access_policies_request.ListAssociatedAccessPoliciesRequest = {
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
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

    def iter_list_associated_access_policies(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_associated_access_policies_request_max_results.ListAssociatedAccessPoliciesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.associated_access_policy.AssociatedAccessPolicy]":
        _token = next_token
        while True:
            _response = self.list_associated_access_policies(
                cluster_name,
                principal_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associated_access_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_capabilities(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_capabilities_request_max_results.ListCapabilitiesRequestMaxResults"
        ] = None,
    ) -> "capo_eks.types.list_capabilities_response.ListCapabilitiesResponse":
        """<p>Lists all managed capabilities in your Amazon EKS cluster. You can use this operation to get an overview of all capabilities and their current status.</p>

        Args:
            cluster_name: <p>The name of the Amazon EKS cluster for which you want to list capabilities.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value. If you don't specify a value, the default is 100 results.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_capabilities_request.ListCapabilitiesRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_capabilities_response.ListCapabilitiesResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_capabilities

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_capabilities.list_capabilities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_capabilities_request.ListCapabilitiesRequest = {
            "cluster_name": cluster_name
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

    def iter_list_capabilities(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_capabilities_request_max_results.ListCapabilitiesRequestMaxResults"
        ] = None,
    ) -> "Iterator[capo_eks.types.capability_summary.CapabilitySummary]":
        _token = next_token
        while True:
            _response = self.list_capabilities(
                cluster_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("capabilities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_certificate_authorities(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.certificate_authority_max_results.CertificateAuthorityMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_certificate_authorities_response.ListCertificateAuthoritiesResponse":
        """<p>Lists the certificate authorities (CAs) for your cluster. A cluster has at most two certificate authorities: the outgoing CA that's currently signing and, during a rotation, one successor CA.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value. If you don't specify a value, the default is 100 results.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_certificate_authorities_request.ListCertificateAuthoritiesRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_certificate_authorities_response.ListCertificateAuthoritiesResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_certificate_authorities

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_certificate_authorities.list_certificate_authorities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_certificate_authorities_request.ListCertificateAuthoritiesRequest = {
            "cluster_name": cluster_name
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

    def iter_list_certificate_authorities(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.certificate_authority_max_results.CertificateAuthorityMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.certificate_authority_summary.CertificateAuthoritySummary]":
        _token = next_token
        while True:
            _response = self.list_certificate_authorities(
                cluster_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("certificate_authorities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_clusters(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_clusters_request_max_results.ListClustersRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        include: Optional[
            "capo_eks.types.include_clusters_list.IncludeClustersList"
        ] = None,
    ) -> "capo_eks.types.list_clusters_response.ListClustersResponse":
        """<p>Lists the Amazon EKS clusters in your Amazon Web Services account in the specified Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            include: <p>Indicates whether external clusters are included in the returned list. Use '<code>all</code>' to return <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-connector.html">https://docs.aws.amazon.com/eks/latest/userguide/eks-connector.html</a>connected clusters, or blank to return only Amazon EKS clusters. '<code>all</code>' must be in lowercase otherwise an error occurs.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your available clusters
            This example command lists all of your available clusters in your default region.

            >>> client.list_clusters()
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_clusters_request.ListClustersRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_clusters

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_clusters_request.ListClustersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_clusters_request_max_results.ListClustersRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        include: Optional[
            "capo_eks.types.include_clusters_list.IncludeClustersList"
        ] = None,
    ) -> "Iterator[capo_eks.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include=include,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_eks_anywhere_subscriptions(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_eks_anywhere_subscriptions_request_max_results.ListEksAnywhereSubscriptionsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        include_status: Optional[
            "capo_eks.types.eks_anywhere_subscription_status_values.EksAnywhereSubscriptionStatusValues"
        ] = None,
    ) -> "capo_eks.types.list_eks_anywhere_subscriptions_response.ListEksAnywhereSubscriptionsResponse":
        """<p>Displays the full description of the subscription.</p>

        Args:
            max_results: <p>The maximum number of cluster results returned by ListEksAnywhereSubscriptions in paginated output. When you use this parameter, ListEksAnywhereSubscriptions returns only maxResults results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListEksAnywhereSubscriptions request with the returned nextToken value. This value can be between 1 and 100. If you don't use this parameter, ListEksAnywhereSubscriptions returns up to 10 results and a nextToken value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListEksAnywhereSubscriptions</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            include_status: <p>An array of subscription statuses to filter on.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_eks_anywhere_subscriptions_request.ListEksAnywhereSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_eks_anywhere_subscriptions_response.ListEksAnywhereSubscriptionsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_eks_anywhere_subscriptions

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_eks_anywhere_subscriptions.list_eks_anywhere_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_eks_anywhere_subscriptions_request.ListEksAnywhereSubscriptionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_status is not None:
            input_["include_status"] = include_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_eks_anywhere_subscriptions(
        self,
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_eks_anywhere_subscriptions_request_max_results.ListEksAnywhereSubscriptionsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        include_status: Optional[
            "capo_eks.types.eks_anywhere_subscription_status_values.EksAnywhereSubscriptionStatusValues"
        ] = None,
    ) -> "Iterator[capo_eks.types.eks_anywhere_subscription.EksAnywhereSubscription]":
        _token = next_token
        while True:
            _response = self.list_eks_anywhere_subscriptions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include_status=include_status,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_fargate_profiles(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.fargate_profiles_request_max_results.FargateProfilesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_fargate_profiles_response.ListFargateProfilesResponse":
        """<p>Lists the Fargate profiles associated with the specified cluster in your Amazon Web Services account in the specified Amazon Web Services Region.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_fargate_profiles_request.ListFargateProfilesRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_fargate_profiles_response.ListFargateProfilesResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_fargate_profiles

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_fargate_profiles.list_fargate_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_fargate_profiles_request.ListFargateProfilesRequest = {
            "cluster_name": cluster_name
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

    def iter_list_fargate_profiles(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.fargate_profiles_request_max_results.FargateProfilesRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_fargate_profiles(
                cluster_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fargate_profile_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_identity_provider_configs(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_identity_provider_configs_request_max_results.ListIdentityProviderConfigsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_identity_provider_configs_response.ListIdentityProviderConfigsResponse":
        """<p>Lists the identity provider configurations for your cluster.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_identity_provider_configs_request.ListIdentityProviderConfigsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_identity_provider_configs_response.ListIdentityProviderConfigsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_identity_provider_configs

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_identity_provider_configs.list_identity_provider_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_identity_provider_configs_request.ListIdentityProviderConfigsRequest = {
            "cluster_name": cluster_name
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

    def iter_list_identity_provider_configs(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_identity_provider_configs_request_max_results.ListIdentityProviderConfigsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.identity_provider_config.IdentityProviderConfig]":
        _token = next_token
        while True:
            _response = self.list_identity_provider_configs(
                cluster_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("identity_provider_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_insights(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        filter: Optional["capo_eks.types.insights_filter.InsightsFilter"] = None,
        max_results: Optional[
            "capo_eks.types.list_insights_max_results.ListInsightsMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_insights_response.ListInsightsResponse":
        """<p>Returns a list of all insights checked for against the specified cluster. You can filter which insights are returned by category, associated Kubernetes version, and status. The default filter lists all categories and every status.</p> <p>The following lists the available categories:</p> <ul> <li> <p> <code>UPGRADE_READINESS</code>: Amazon EKS identifies issues that could impact your ability to upgrade to new versions of Kubernetes. These are called upgrade insights.</p> </li> <li> <p> <code>MISCONFIGURATION</code>: Amazon EKS identifies misconfiguration in your EKS Hybrid Nodes setup that could impair functionality of your cluster or workloads. These are called configuration insights.</p> </li> </ul>

        Args:
            cluster_name: <p>The name of the Amazon EKS cluster associated with the insights.</p>
            filter: <p>The criteria to filter your list of insights for your cluster. You can filter which insights are returned by category, associated Kubernetes version, and status.</p>
            max_results: <p>The maximum number of identity provider configurations returned by <code>ListInsights</code> in paginated output. When you use this parameter, <code>ListInsights</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListInsights</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListInsights</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListInsights</code> request. When the results of a <code>ListInsights</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_insights_request.ListInsightsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_insights_response.ListInsightsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_insights

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_insights.list_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_insights_request.ListInsightsRequest = {
            "cluster_name": cluster_name
        }
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_insights(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        filter: Optional["capo_eks.types.insights_filter.InsightsFilter"] = None,
        max_results: Optional[
            "capo_eks.types.list_insights_max_results.ListInsightsMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.insight_summary.InsightSummary]":
        _token = next_token
        while True:
            _response = self.list_insights(
                cluster_name,
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("insights",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_nodegroups(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_nodegroups_request_max_results.ListNodegroupsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_nodegroups_response.ListNodegroupsResponse":
        """<p>Lists the managed node groups associated with the specified cluster in your Amazon Web Services account in the specified Amazon Web Services Region. Self-managed node groups aren't listed.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_nodegroups_request.ListNodegroupsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_nodegroups_response.ListNodegroupsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_nodegroups

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_nodegroups.list_nodegroups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_nodegroups_request.ListNodegroupsRequest = {
            "cluster_name": cluster_name
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

    def iter_list_nodegroups(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        max_results: Optional[
            "capo_eks.types.list_nodegroups_request_max_results.ListNodegroupsRequestMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_nodegroups(
                cluster_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("nodegroups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_pod_identity_associations(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        namespace: Optional["capo_eks.types.string.String"] = None,
        service_account: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_pod_identity_associations_max_results.ListPodIdentityAssociationsMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.list_pod_identity_associations_response.ListPodIdentityAssociationsResponse":
        """<p>List the EKS Pod Identity associations in a cluster. You can filter the list by the namespace that the association is in or the service account that the association uses.</p>

        Args:
            cluster_name: <p>The name of the cluster that the associations are in.</p>
            namespace: <p>The name of the Kubernetes namespace inside the cluster that the associations are in.</p>
            service_account: <p>The name of the Kubernetes service account that the associations use.</p>
            max_results: <p>The maximum number of EKS Pod Identity association results returned by <code>ListPodIdentityAssociations</code> in paginated output. When you use this parameter, <code>ListPodIdentityAssociations</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListPodIdentityAssociations</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListPodIdentityAssociations</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListUpdates</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_pod_identity_associations_request.ListPodIdentityAssociationsRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_pod_identity_associations_response.ListPodIdentityAssociationsResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_pod_identity_associations

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_pod_identity_associations.list_pod_identity_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_pod_identity_associations_request.ListPodIdentityAssociationsRequest = {
            "cluster_name": cluster_name
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if service_account is not None:
            input_["service_account"] = service_account
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

    def iter_list_pod_identity_associations(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        namespace: Optional["capo_eks.types.string.String"] = None,
        service_account: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_pod_identity_associations_max_results.ListPodIdentityAssociationsMaxResults"
        ] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "Iterator[capo_eks.types.pod_identity_association_summary.PodIdentityAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_pod_identity_associations(
                cluster_name,
                config_overrides=config_overrides,
                namespace=namespace,
                service_account=service_account,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags for an Amazon EKS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list tags for.</p>

        Raises:
            capo_eks.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning will depend on the API, and will be documented in the error message.</p>
            capo_eks.errors.not_found_exception.NotFoundException: <p>A service resource associated with the request could not be found. Clients should not retry such requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list tags for a cluster
            This example lists all of the tags for the `beta` cluster.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:eks:us-west-2:012345678910:cluster/beta')
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_tags_for_resource

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_updates(
        self,
        name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        nodegroup_name: Optional["capo_eks.types.string.String"] = None,
        addon_name: Optional["capo_eks.types.string.String"] = None,
        capability_name: Optional["capo_eks.types.string.String"] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_updates_request_max_results.ListUpdatesRequestMaxResults"
        ] = None,
    ) -> "capo_eks.types.list_updates_response.ListUpdatesResponse":
        """<p>Lists the updates associated with an Amazon EKS resource in your Amazon Web Services account, in the specified Amazon Web Services Region.</p>

        Args:
            name: <p>The name of the Amazon EKS cluster to list updates for.</p>
            nodegroup_name: <p>The name of the Amazon EKS managed node group to list updates for.</p>
            addon_name: <p>The names of the installed add-ons that have available updates.</p>
            capability_name: <p>The name of the capability for which you want to list updates.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.list_updates_request.ListUpdatesRequest]",
        ) -> OperationResponse[
            "capo_eks.types.list_updates_response.ListUpdatesResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.list_updates

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.list_updates.list_updates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.list_updates_request.ListUpdatesRequest = {"name": name}
        if nodegroup_name is not None:
            input_["nodegroup_name"] = nodegroup_name
        if addon_name is not None:
            input_["addon_name"] = addon_name
        if capability_name is not None:
            input_["capability_name"] = capability_name
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

    def iter_list_updates(
        self,
        name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        nodegroup_name: Optional["capo_eks.types.string.String"] = None,
        addon_name: Optional["capo_eks.types.string.String"] = None,
        capability_name: Optional["capo_eks.types.string.String"] = None,
        next_token: Optional["capo_eks.types.string.String"] = None,
        max_results: Optional[
            "capo_eks.types.list_updates_request_max_results.ListUpdatesRequestMaxResults"
        ] = None,
    ) -> "Iterator[capo_eks.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_updates(
                name,
                config_overrides=config_overrides,
                nodegroup_name=nodegroup_name,
                addon_name=addon_name,
                capability_name=capability_name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("update_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def register_cluster(
        self,
        name: "capo_eks.types.cluster_name.ClusterName",
        connector_config: "capo_eks.types.connector_config_request.ConnectorConfigRequest",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        tags: Optional["capo_eks.types.tag_map.TagMap"] = None,
    ) -> "capo_eks.types.register_cluster_response.RegisterClusterResponse":
        """<p>Connects a Kubernetes cluster to the Amazon EKS control plane. </p> <p>Any Kubernetes cluster can be connected to the Amazon EKS control plane to view current information about the cluster and its nodes. </p> <p>Cluster connection requires two steps. First, send a <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_RegisterClusterRequest.html"> <code>RegisterClusterRequest</code> </a> to add it to the Amazon EKS control plane.</p> <p>Second, a <a href="https://amazon-eks.s3.us-west-2.amazonaws.com/eks-connector/manifests/eks-connector/latest/eks-connector.yaml">Manifest</a> containing the <code>activationID</code> and <code>activationCode</code> must be applied to the Kubernetes cluster through it's native provider to provide visibility.</p> <p>After the manifest is updated and applied, the connected cluster is visible to the Amazon EKS control plane. If the manifest isn't applied within three days, the connected cluster will no longer be visible and must be deregistered using <code>DeregisterCluster</code>.</p>

        Args:
            name: <p>A unique name for this cluster in your Amazon Web Services Region.</p>
            connector_config: <p>The configuration settings required to connect the Kubernetes cluster to the Amazon EKS control plane.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>

        Raises:
            capo_eks.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management</a> in the <i>IAM User Guide</i>. </p>
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>You have encountered a service limit on the specified resource.</p>
            capo_eks.errors.resource_propagation_delay_exception.ResourcePropagationDelayException: <p>Required resources (such as service-linked roles) were created and are still propagating. Retry later.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.register_cluster_request.RegisterClusterRequest]",
        ) -> OperationResponse[
            "capo_eks.types.register_cluster_response.RegisterClusterResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.register_cluster

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.register_cluster.register_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.register_cluster_request.RegisterClusterRequest = {
            "name": name,
            "connector_config": connector_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_insights_refresh(
        self,
        cluster_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.start_insights_refresh_response.StartInsightsRefreshResponse":
        """<p>Initiates an on-demand refresh operation for cluster insights, getting the latest analysis outside of the standard refresh schedule.</p>

        Args:
            cluster_name: <p>The name of the cluster for the refresh insights operation.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.start_insights_refresh_request.StartInsightsRefreshRequest]",
        ) -> OperationResponse[
            "capo_eks.types.start_insights_refresh_response.StartInsightsRefreshResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.start_insights_refresh

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.start_insights_refresh.start_insights_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.start_insights_refresh_request.StartInsightsRefreshRequest = {
            "cluster_name": cluster_name
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
        resource_arn: "capo_eks.types.string.String",
        tags: "capo_eks.types.tag_map.TagMap",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to an Amazon EKS resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted. Tags that you create for Amazon EKS resources don't propagate to any other resources associated with the cluster. For example, if you tag a cluster with this operation, that tag doesn't automatically propagate to the subnets and nodes associated with the cluster.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>

        Raises:
            capo_eks.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning will depend on the API, and will be documented in the error message.</p>
            capo_eks.errors.not_found_exception.NotFoundException: <p>A service resource associated with the request could not be found. Clients should not retry such requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_eks.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.tag_resource

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_eks.types.string.String",
        tag_keys: "capo_eks.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
    ) -> "capo_eks.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from an Amazon EKS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>
            tag_keys: <p>The keys of the tags to remove.</p>

        Raises:
            capo_eks.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning will depend on the API, and will be documented in the error message.</p>
            capo_eks.errors.not_found_exception.NotFoundException: <p>A service resource associated with the request could not be found. Clients should not retry such requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_eks.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.untag_resource

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.untag_resource_request.UntagResourceRequest = {
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

    def update_access_entry(
        self,
        cluster_name: "capo_eks.types.string.String",
        principal_arn: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        kubernetes_groups: Optional["capo_eks.types.string_list.StringList"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        username: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.update_access_entry_response.UpdateAccessEntryResponse":
        """<p>Updates an access entry.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            principal_arn: <p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>
            kubernetes_groups: <p>The value for <code>name</code> that you've specified for <code>kind: Group</code> as a <code>subject</code> in a Kubernetes <code>RoleBinding</code> or <code>ClusterRoleBinding</code> object. Amazon EKS doesn't confirm that the value for <code>name</code> exists in any bindings on your cluster. You can specify one or more names.</p> <p>Kubernetes authorizes the <code>principalArn</code> of the access entry to access any cluster objects that you've specified in a Kubernetes <code>Role</code> or <code>ClusterRole</code> object that is also specified in a binding's <code>roleRef</code>. For more information about creating Kubernetes <code>RoleBinding</code>, <code>ClusterRoleBinding</code>, <code>Role</code>, or <code>ClusterRole</code> objects, see <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/">Using RBAC Authorization in the Kubernetes documentation</a>.</p> <p>If you want Amazon EKS to authorize the <code>principalArn</code> (instead of, or in addition to Kubernetes authorizing the <code>principalArn</code>), you can associate one or more access policies to the access entry using <code>AssociateAccessPolicy</code>. If you associate any access policies, the <code>principalARN</code> has all permissions assigned in the associated access policies and all permissions in any Kubernetes <code>Role</code> or <code>ClusterRole</code> objects that the group names are bound to.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            username: <p>The username to authenticate to Kubernetes with. We recommend not specifying a username and letting Amazon EKS specify it for you. For more information about the value Amazon EKS specifies for you, or constraints before specifying your own username, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#creating-access-entries">Creating access entries</a> in the <i>Amazon EKS User Guide</i>.</p>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_access_entry_request.UpdateAccessEntryRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_access_entry_response.UpdateAccessEntryResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_access_entry

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_access_entry.update_access_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_access_entry_request.UpdateAccessEntryRequest = {
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
        }
        if kubernetes_groups is not None:
            input_["kubernetes_groups"] = kubernetes_groups
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if username is not None:
            input_["username"] = username

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_addon(
        self,
        cluster_name: "capo_eks.types.cluster_name.ClusterName",
        addon_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        addon_version: Optional["capo_eks.types.string.String"] = None,
        service_account_role_arn: Optional["capo_eks.types.role_arn.RoleArn"] = None,
        resolve_conflicts: Optional[
            "capo_eks.types.resolve_conflicts.ResolveConflicts"
        ] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        configuration_values: Optional["capo_eks.types.string.String"] = None,
        pod_identity_associations: Optional[
            "capo_eks.types.addon_pod_identity_associations_list.AddonPodIdentityAssociationsList"
        ] = None,
    ) -> "capo_eks.types.update_addon_response.UpdateAddonResponse":
        """<p>Updates an Amazon EKS add-on.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            addon_name: <p>The name of the add-on. The name must match one of the names returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html"> <code>ListAddons</code> </a>.</p>
            addon_version: <p>The version of the add-on. The version must match one of the versions returned by <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html"> <code>DescribeAddonVersions</code> </a>.</p>
            service_account_role_arn: <p>The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-on's service account. The role must be assigned the IAM permissions required by the add-on. If you don't specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html">Amazon EKS node IAM role</a> in the <i>Amazon EKS User Guide</i>.</p> <note> <p>To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html">Enabling IAM roles for service accounts on your cluster</a> in the <i>Amazon EKS User Guide</i>.</p> </note>
            resolve_conflicts: <p>How to resolve field value conflicts for an Amazon EKS add-on if you've changed a value from the Amazon EKS default value. Conflicts are handled based on the option you choose:</p> <ul> <li> <p> <b>None</b> – Amazon EKS doesn't change the value. The update might fail.</p> </li> <li> <p> <b>Overwrite</b> – Amazon EKS overwrites the changed value back to the Amazon EKS default value.</p> </li> <li> <p> <b>Preserve</b> – Amazon EKS preserves the value. If you choose this option, we recommend that you test any field and value changes on a non-production cluster before updating the add-on on your production cluster.</p> </li> </ul>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            configuration_values: <p>The set of configuration values for the add-on that's created. The values that you provide are validated against the schema returned by <code>DescribeAddonConfiguration</code>.</p>
            pod_identity_associations: <p>An array of EKS Pod Identity associations to be updated. Each association maps a Kubernetes service account to an IAM role. If this value is left blank, no change. If an empty array is provided, existing associations owned by the add-on are deleted.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html">Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_addon_request.UpdateAddonRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_addon_response.UpdateAddonResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_addon

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_addon.update_addon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_addon_request.UpdateAddonRequest = {
            "cluster_name": cluster_name,
            "addon_name": addon_name,
        }
        if addon_version is not None:
            input_["addon_version"] = addon_version
        if service_account_role_arn is not None:
            input_["service_account_role_arn"] = service_account_role_arn
        if resolve_conflicts is not None:
            input_["resolve_conflicts"] = resolve_conflicts
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if configuration_values is not None:
            input_["configuration_values"] = configuration_values
        if pod_identity_associations is not None:
            input_["pod_identity_associations"] = pod_identity_associations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_capability(
        self,
        cluster_name: "capo_eks.types.string.String",
        capability_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        role_arn: Optional["capo_eks.types.string.String"] = None,
        configuration: Optional[
            "capo_eks.types.update_capability_configuration.UpdateCapabilityConfiguration"
        ] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        delete_propagation_policy: Optional[
            "capo_eks.types.capability_delete_propagation_policy.CapabilityDeletePropagationPolicy"
        ] = None,
    ) -> "capo_eks.types.update_capability_response.UpdateCapabilityResponse":
        """<p>Updates the configuration of a managed capability in your Amazon EKS cluster. You can update the IAM role, configuration settings, and delete propagation policy for a capability.</p> <p>When you update a capability, Amazon EKS applies the changes and may restart capability components as needed. The capability remains available during the update process, but some operations may be temporarily unavailable.</p>

        Args:
            cluster_name: <p>The name of the Amazon EKS cluster that contains the capability you want to update configuration for.</p>
            capability_name: <p>The name of the capability to update configuration for.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with Amazon Web Services services. If you specify a new role ARN, the capability will start using the new role for all subsequent operations.</p>
            configuration: <p>The updated configuration settings for the capability. You only need to specify the configuration parameters you want to change. For Argo CD capabilities, you can update RBAC role mappings and network access settings.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is valid for 24 hours after creation.</p>
            delete_propagation_policy: <p>The updated delete propagation policy for the capability. Currently, the only supported value is <code>RETAIN</code>.</p>

        Raises:
            capo_eks.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management</a> in the <i>IAM User Guide</i>. </p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_capability_request.UpdateCapabilityRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_capability_response.UpdateCapabilityResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_capability

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_capability.update_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_capability_request.UpdateCapabilityRequest = {
            "cluster_name": cluster_name,
            "capability_name": capability_name,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if configuration is not None:
            input_["configuration"] = configuration
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if delete_propagation_policy is not None:
            input_["delete_propagation_policy"] = delete_propagation_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cluster_config(
        self,
        name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        resources_vpc_config: Optional[
            "capo_eks.types.vpc_config_request.VpcConfigRequest"
        ] = None,
        logging: Optional["capo_eks.types.logging.Logging"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        access_config: Optional[
            "capo_eks.types.update_access_config_request.UpdateAccessConfigRequest"
        ] = None,
        upgrade_policy: Optional[
            "capo_eks.types.upgrade_policy_request.UpgradePolicyRequest"
        ] = None,
        zonal_shift_config: Optional[
            "capo_eks.types.zonal_shift_config_request.ZonalShiftConfigRequest"
        ] = None,
        compute_config: Optional[
            "capo_eks.types.compute_config_request.ComputeConfigRequest"
        ] = None,
        kubernetes_network_config: Optional[
            "capo_eks.types.kubernetes_network_config_request.KubernetesNetworkConfigRequest"
        ] = None,
        storage_config: Optional[
            "capo_eks.types.storage_config_request.StorageConfigRequest"
        ] = None,
        remote_network_config: Optional[
            "capo_eks.types.remote_network_config_request.RemoteNetworkConfigRequest"
        ] = None,
        deletion_protection: Optional[
            "capo_eks.types.boxed_boolean.BoxedBoolean"
        ] = None,
        control_plane_scaling_config: Optional[
            "capo_eks.types.control_plane_scaling_config.ControlPlaneScalingConfig"
        ] = None,
        kube_api_server_config: Optional[
            "capo_eks.types.kube_api_server_config_request.KubeApiServerConfigRequest"
        ] = None,
        kube_scheduler_config: Optional[
            "capo_eks.types.kube_scheduler_config_request.KubeSchedulerConfigRequest"
        ] = None,
        kube_controller_manager_config: Optional[
            "capo_eks.types.kube_controller_manager_config_request.KubeControllerManagerConfigRequest"
        ] = None,
    ) -> "capo_eks.types.update_cluster_config_response.UpdateClusterConfigResponse":
        """<p>Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with <code>DescribeUpdate</code>.</p> <p>You can use this operation to do the following actions:</p> <ul> <li> <p>You can use this API operation to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Cluster control plane logs</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <note> <p>CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see <a href="http://aws.amazon.com/cloudwatch/pricing/">CloudWatch Pricing</a>.</p> </note> </li> <li> <p>You can also use this API operation to enable or disable public and private access to your cluster's Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html"> Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> </li> <li> <p>You can also use this API operation to choose different subnets and security groups for the cluster. You must specify at least two subnets that are in different Availability Zones. You can't change which VPC the subnets are from, the subnets must be in the same VPC as the subnets that the cluster was created with. For more information about the VPC requirements, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> </li> <li> <p>You can also use this API operation to enable or disable ARC zonal shift. If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.</p> </li> <li> <p>You can also use this API operation to add, change, or remove the configuration in the cluster for EKS Hybrid Nodes. To remove the configuration, use the <code>remoteNetworkConfig</code> key with an object containing both subkeys with empty arrays for each. Here is an inline example: <code>"remoteNetworkConfig": { "remoteNodeNetworks": [], "remotePodNetworks": [] }</code>.</p> </li> </ul> <p>Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to <code>UPDATING</code> (this status transition is eventually consistent). When the update is complete (either <code>Failed</code> or <code>Successful</code>), the cluster status moves to <code>Active</code>.</p>

        Args:
            name: <p>The name of the Amazon EKS cluster to update.</p>
            resources_vpc_config: <p>An object representing the VPC configuration to use for the cluster update. You can use this parameter to update the control plane egress mode, the subnets used by the cluster, the security groups, and the endpoint access settings.</p>
            logging: <p>Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs . By default, cluster control plane logs aren't exported to CloudWatch Logs . For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS cluster control plane logs</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <note> <p>CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see <a href="http://aws.amazon.com/cloudwatch/pricing/">CloudWatch Pricing</a>.</p> </note>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            access_config: <p>The access configuration for the cluster.</p>
            upgrade_policy: <p>You can enable or disable extended support for clusters currently on standard support. You cannot disable extended support once it starts. You must enable extended support before your cluster exits standard support.</p>
            zonal_shift_config: <p>Enable or disable ARC zonal shift for the cluster. If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.</p> <p>Zonal shift is a feature of Amazon Application Recovery Controller (ARC). ARC zonal shift is designed to be a temporary measure that allows you to move traffic for a resource away from an impaired AZ until the zonal shift expires or you cancel it. You can extend the zonal shift if necessary.</p> <p>You can start a zonal shift for an EKS cluster, or you can allow Amazon Web Services to do it for you by enabling <i>zonal autoshift</i>. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. Additionally, any ALB or NLB handling ingress traffic for applications in your EKS cluster will automatically route traffic to targets in the healthy AZs. For more information about zonal shift in EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html">Learn about Amazon Application Recovery Controller (ARC) Zonal Shift in Amazon EKS</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>
            compute_config: <p>Update the configuration of the compute capability of your EKS Auto Mode cluster. For example, enable the capability.</p>
            storage_config: <p>Update the configuration of the block storage capability of your EKS Auto Mode cluster. For example, enable the capability.</p>
            deletion_protection: <p>Specifies whether to enable or disable deletion protection for the cluster. When enabled (<code>true</code>), the cluster cannot be deleted until deletion protection is explicitly disabled. When disabled (<code>false</code>), the cluster can be deleted normally.</p>
            control_plane_scaling_config: <p>The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.</p>
            kube_api_server_config: <p>The Kubernetes API server configuration for the updated cluster.</p>
            kube_scheduler_config: <p>The Kubernetes scheduler configuration for the updated cluster.</p>
            kube_controller_manager_config: <p>The Kubernetes controller manager configuration for the updated cluster.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_cluster_config_request.UpdateClusterConfigRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_cluster_config_response.UpdateClusterConfigResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_cluster_config

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_cluster_config.update_cluster_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_cluster_config_request.UpdateClusterConfigRequest = {
            "name": name
        }
        if resources_vpc_config is not None:
            input_["resources_vpc_config"] = resources_vpc_config
        if logging is not None:
            input_["logging"] = logging
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if access_config is not None:
            input_["access_config"] = access_config
        if upgrade_policy is not None:
            input_["upgrade_policy"] = upgrade_policy
        if zonal_shift_config is not None:
            input_["zonal_shift_config"] = zonal_shift_config
        if compute_config is not None:
            input_["compute_config"] = compute_config
        if kubernetes_network_config is not None:
            input_["kubernetes_network_config"] = kubernetes_network_config
        if storage_config is not None:
            input_["storage_config"] = storage_config
        if remote_network_config is not None:
            input_["remote_network_config"] = remote_network_config
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if control_plane_scaling_config is not None:
            input_["control_plane_scaling_config"] = control_plane_scaling_config
        if kube_api_server_config is not None:
            input_["kube_api_server_config"] = kube_api_server_config
        if kube_scheduler_config is not None:
            input_["kube_scheduler_config"] = kube_scheduler_config
        if kube_controller_manager_config is not None:
            input_["kube_controller_manager_config"] = kube_controller_manager_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cluster_version(
        self,
        name: "capo_eks.types.string.String",
        version: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        force: Optional["capo_eks.types.boolean.Boolean"] = None,
        rollback_config: Optional[
            "capo_eks.types.rollback_config.RollbackConfig"
        ] = None,
    ) -> "capo_eks.types.update_cluster_version_response.UpdateClusterVersionResponse":
        """<p>Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html"> <code>DescribeUpdate</code> </a> API operation.</p> <p>Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to <code>UPDATING</code> (this status transition is eventually consistent). When the update is complete (either <code>Failed</code> or <code>Successful</code>), the cluster status moves to <code>Active</code>.</p> <p>If your cluster has managed node groups attached to it, all of your node groups' Kubernetes versions must match the cluster's Kubernetes version in order to update the cluster to a new Kubernetes version.</p>

        Args:
            name: <p>The name of the Amazon EKS cluster to update.</p>
            version: <p>The desired Kubernetes version following a successful update.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            force: <p>Set this value to <code>true</code> to override upgrade-blocking or rollback-blocking readiness checks when updating a cluster.</p>
            rollback_config: <p>The rollback configuration for the cluster version rollback.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.invalid_state_exception.InvalidStateException: <p>Amazon EKS detected upgrade readiness issues. Call the <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html"> <code>ListInsights</code> </a> API to view detected upgrade blocking issues. Pass the <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html#API_UpdateClusterVersion_RequestBody"> <code>force</code> </a> flag when updating to override upgrade readiness errors.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because a service is throttling requests.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_cluster_version_request.UpdateClusterVersionRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_cluster_version_response.UpdateClusterVersionResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_cluster_version

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_cluster_version.update_cluster_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_cluster_version_request.UpdateClusterVersionRequest = {
            "name": name,
            "version": version,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if force is not None:
            input_["force"] = force
        if rollback_config is not None:
            input_["rollback_config"] = rollback_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_eks_anywhere_subscription(
        self,
        id: "capo_eks.types.string.String",
        auto_renew: "capo_eks.types.boolean.Boolean",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse":
        """<p>Update an EKS Anywhere Subscription. Only auto renewal and tags can be updated after subscription creation.</p>

        Args:
            id: <p>The ID of the subscription.</p>
            auto_renew: <p>A boolean indicating whether or not to automatically renew the subscription.</p>
            client_request_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_eks_anywhere_subscription_request.UpdateEksAnywhereSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_eks_anywhere_subscription_response.UpdateEksAnywhereSubscriptionResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_eks_anywhere_subscription

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_eks_anywhere_subscription.update_eks_anywhere_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_eks_anywhere_subscription_request.UpdateEksAnywhereSubscriptionRequest = {
            "id": id,
            "auto_renew": auto_renew,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_nodegroup_config(
        self,
        cluster_name: "capo_eks.types.string.String",
        nodegroup_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        labels: Optional[
            "capo_eks.types.update_labels_payload.UpdateLabelsPayload"
        ] = None,
        taints: Optional[
            "capo_eks.types.update_taints_payload.UpdateTaintsPayload"
        ] = None,
        scaling_config: Optional[
            "capo_eks.types.nodegroup_scaling_config.NodegroupScalingConfig"
        ] = None,
        update_config: Optional[
            "capo_eks.types.nodegroup_update_config.NodegroupUpdateConfig"
        ] = None,
        node_repair_config: Optional[
            "capo_eks.types.node_repair_config.NodeRepairConfig"
        ] = None,
        warm_pool_config: Optional[
            "capo_eks.types.warm_pool_config.WarmPoolConfig"
        ] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> (
        "capo_eks.types.update_nodegroup_config_response.UpdateNodegroupConfigResponse"
    ):
        """<p>Updates an Amazon EKS managed node group configuration. Your node group continues to function during the update. The response output includes an update ID that you can use to track the status of your node group update with the <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html"> <code>DescribeUpdate</code> </a> API operation. You can update the Kubernetes labels and taints for a node group and the scaling and version update configuration.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            nodegroup_name: <p>The name of the managed node group to update.</p>
            labels: <p>The Kubernetes <code>labels</code> to apply to the nodes in the node group after the update.</p>
            taints: <p>The Kubernetes taints to be applied to the nodes in the node group after the update. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html">Node taints on managed node groups</a>.</p>
            scaling_config: <p>The scaling configuration details for the Auto Scaling group after the update.</p>
            update_config: <p>The node group update configuration.</p>
            node_repair_config: <p>The node auto repair configuration for the node group.</p>
            warm_pool_config: <p>The warm pool configuration to apply to the node group. You can use this to add a warm pool to an existing node group or modify the settings of an existing warm pool.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_nodegroup_config_request.UpdateNodegroupConfigRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_nodegroup_config_response.UpdateNodegroupConfigResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_nodegroup_config

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_nodegroup_config.update_nodegroup_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_nodegroup_config_request.UpdateNodegroupConfigRequest = {
            "cluster_name": cluster_name,
            "nodegroup_name": nodegroup_name,
        }
        if labels is not None:
            input_["labels"] = labels
        if taints is not None:
            input_["taints"] = taints
        if scaling_config is not None:
            input_["scaling_config"] = scaling_config
        if update_config is not None:
            input_["update_config"] = update_config
        if node_repair_config is not None:
            input_["node_repair_config"] = node_repair_config
        if warm_pool_config is not None:
            input_["warm_pool_config"] = warm_pool_config
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_nodegroup_version(
        self,
        cluster_name: "capo_eks.types.string.String",
        nodegroup_name: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        version: Optional["capo_eks.types.string.String"] = None,
        release_version: Optional["capo_eks.types.string.String"] = None,
        launch_template: Optional[
            "capo_eks.types.launch_template_specification.LaunchTemplateSpecification"
        ] = None,
        force: Optional["capo_eks.types.boolean.Boolean"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.update_nodegroup_version_response.UpdateNodegroupVersionResponse":
        """<p>Updates the Kubernetes version or AMI version of an Amazon EKS managed node group.</p> <p>You can update a node group using a launch template only if the node group was originally deployed with a launch template. Additionally, the launch template ID or name must match what was used when the node group was created. You can update the launch template version with necessary changes.</p> <p>If you need to update a custom AMI in a node group that was deployed with a launch template, then update your custom AMI, specify the new ID in a new version of the launch template, and then update the node group to the new version of the launch template.</p> <p>If you update without a launch template, then you can update to the latest available AMI version of a node group's current Kubernetes version by not specifying a Kubernetes version in the request. You can update to the latest AMI version of your cluster's current Kubernetes version by specifying your cluster's Kubernetes version in the request. For information about Linux versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html">Amazon EKS optimized Amazon Linux AMI versions</a> in the <i>Amazon EKS User Guide</i>. For information about Windows versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html">Amazon EKS optimized Windows AMI versions</a> in the <i>Amazon EKS User Guide</i>. </p> <p>You cannot roll back a node group to an earlier Kubernetes version or AMI version.</p> <p>When a node in a managed node group is terminated due to a scaling action or update, every <code>Pod</code> on that node is drained first. Amazon EKS attempts to drain the nodes gracefully and will fail if it is unable to do so. You can <code>force</code> the update if Amazon EKS is unable to drain the nodes as a result of a <code>Pod</code> disruption budget issue.</p>

        Args:
            cluster_name: <p>The name of your cluster.</p>
            nodegroup_name: <p>The name of the managed node group to update.</p>
            version: <p>The Kubernetes version to update to. If no version is specified, then the node group will be updated to match the cluster's current Kubernetes version, and the latest available AMI for that version will be used. You can also specify the Kubernetes version of the cluster to update the node group to the latest AMI version of the cluster's Kubernetes version. If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>version</code>, or the node group update will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            release_version: <p>The AMI version of the Amazon EKS optimized AMI to use for the update. By default, the latest available AMI version for the node group's Kubernetes version is used. For information about Linux versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html">Amazon EKS optimized Amazon Linux AMI versions</a> in the <i>Amazon EKS User Guide</i>. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html">Amazon EKS optimized Windows AMI versions</a> in the <i>Amazon EKS User Guide</i>.</p> <p>If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>releaseVersion</code>, or the node group update will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>
            launch_template: <p>An object representing a node group's launch template specification. You can only update a node group using a launch template if the node group was originally deployed with a launch template. When updating, you must specify the same launch template ID or name that was used to create the node group.</p>
            force: <p>Force the update if any <code>Pod</code> on the existing node group can't be drained due to a <code>Pod</code> disruption budget issue. If an update fails because all Pods can't be drained, you can force the update after it fails to terminate the old node whether or not any <code>Pod</code> is running on the node.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_eks.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.</p>
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_nodegroup_version_request.UpdateNodegroupVersionRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_nodegroup_version_response.UpdateNodegroupVersionResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_nodegroup_version

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_nodegroup_version.update_nodegroup_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_nodegroup_version_request.UpdateNodegroupVersionRequest = {
            "cluster_name": cluster_name,
            "nodegroup_name": nodegroup_name,
        }
        if version is not None:
            input_["version"] = version
        if release_version is not None:
            input_["release_version"] = release_version
        if launch_template is not None:
            input_["launch_template"] = launch_template
        if force is not None:
            input_["force"] = force
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_pod_identity_association(
        self,
        cluster_name: "capo_eks.types.string.String",
        association_id: "capo_eks.types.string.String",
        *,
        config_overrides: Optional[EKSClientConfig] = None,
        role_arn: Optional["capo_eks.types.string.String"] = None,
        client_request_token: Optional["capo_eks.types.string.String"] = None,
        disable_session_tags: Optional[
            "capo_eks.types.boxed_boolean.BoxedBoolean"
        ] = None,
        target_role_arn: Optional["capo_eks.types.string.String"] = None,
        policy: Optional["capo_eks.types.string.String"] = None,
    ) -> "capo_eks.types.update_pod_identity_association_response.UpdatePodIdentityAssociationResponse":
        """<p>Updates a EKS Pod Identity association. In an update, you can change the IAM role, the target IAM role, or <code>disableSessionTags</code>. You must change at least one of these in an update. An association can't be moved between clusters, namespaces, or service accounts. If you need to edit the namespace or service account, you need to delete the association and then create a new association with your desired settings.</p> <p>Similar to Amazon Web Services IAM behavior, EKS Pod Identity associations are eventually consistent, and may take several seconds to be effective after the initial API call returns successfully. You must design your applications to account for these potential delays. We recommend that you don’t include association create/updates in the critical, high-availability code paths of your application. Instead, make changes in a separate initialization or setup routine that you run less frequently.</p> <p>You can set a <i>target IAM role</i> in the same or a different account for advanced scenarios. With a target role, EKS Pod Identity automatically performs two role assumptions in sequence: first assuming the role in the association that is in this account, then using those credentials to assume the target IAM role. This process provides your Pod with temporary credentials that have the permissions defined in the target role, allowing secure access to resources in another Amazon Web Services account.</p>

        Args:
            cluster_name: <p>The name of the cluster that you want to update the association in.</p>
            association_id: <p>The ID of the association to be updated.</p>
            role_arn: <p>The new IAM role to change in the association.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            disable_session_tags: <p>Disable the automatic sessions tags that are appended by EKS Pod Identity.</p> <p>EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to Amazon Web Services resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags">List of session tags added by EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p> <p>Amazon Web Services compresses inline session policies, managed policy ARNs, and session tags into a packed binary format that has a separate limit. If you receive a <code>PackedPolicyTooLarge</code> error indicating the packed binary format has exceeded the size limit, you can attempt to reduce the size by disabling the session tags added by EKS Pod Identity.</p>
            target_role_arn: <p>The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.</p> <p>When you run applications on Amazon EKS, your application might need to access Amazon Web Services resources from a different role that exists in the same or different Amazon Web Services account. For example, your application running in “Account A” might need to access resources, such as buckets in “Account B” or within “Account A” itself. You can create a association to access Amazon Web Services resources in “Account B” by creating two IAM roles: a role in “Account A” and a role in “Account B” (which can be the same or different account), each with the necessary trust and permission policies. After you provide these roles in the <i>IAM role</i> and <i>Target IAM role</i> fields, EKS will perform role chaining to ensure your application gets the required permissions. This means Role A will assume Role B, allowing your Pods to securely access resources like S3 buckets in the target account.</p>
            policy: <p>An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.</p> <p> <b>Important considerations</b> </p> <ul> <li> <p> <b>Session tags:</b> When using this policy, <code>disableSessionTags</code> must be set to <code>true</code>.</p> </li> <li> <p> <b>Target role permissions:</b> If you specify both a <code>TargetRoleArn</code> and a policy, the policy restrictions apply only to the target role's permissions, not to the initial role used for assuming the target role.</p> </li> </ul>

        Raises:
            capo_eks.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.</p>
            capo_eks.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. You can view your available clusters with <code>ListClusters</code>. You can view your available managed node groups with <code>ListNodegroups</code>. Amazon EKS clusters and node groups are Amazon Web Services Region specific.</p>
            capo_eks.errors.server_exception.ServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks.types.update_pod_identity_association_request.UpdatePodIdentityAssociationRequest]",
        ) -> OperationResponse[
            "capo_eks.types.update_pod_identity_association_response.UpdatePodIdentityAssociationResponse"
        ]:
            import capo_eks._operations.aws_wesley_frontend.update_pod_identity_association

            output, http_response = (
                capo_eks._operations.aws_wesley_frontend.update_pod_identity_association.update_pod_identity_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks.types.update_pod_identity_association_request.UpdatePodIdentityAssociationRequest = {
            "cluster_name": cluster_name,
            "association_id": association_id,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if disable_session_tags is not None:
            input_["disable_session_tags"] = disable_session_tags
        if target_role_arn is not None:
            input_["target_role_arn"] = target_role_arn
        if policy is not None:
            input_["policy"] = policy

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

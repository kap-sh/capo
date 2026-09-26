"""Generated from Smithy shape ``com.amazonaws.evs#AmazonElasticVMwareService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_evs._auth._signers
import capo_evs._auth._sigv4
from capo_evs._auth._identity import Credentials
from capo_evs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_evs._auth._zapros_handler import AuthMiddleware
from capo_evs._pagination import resolve_path as _resolve_path
from capo_evs._resources.amazon_elastic_v_mware_service.environment_resource import (
    AsyncEnvironmentResource,
)
from capo_evs._services._aws_config import aaws_config
from capo_evs._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_evs.types.allocation_id
    import capo_evs.types.appliance_fqdn
    import capo_evs.types.arn
    import capo_evs.types.associate_eip_to_vlan_request
    import capo_evs.types.associate_eip_to_vlan_response
    import capo_evs.types.association_id
    import capo_evs.types.client_token
    import capo_evs.types.connectivity_info
    import capo_evs.types.connector
    import capo_evs.types.connector_id
    import capo_evs.types.connector_type
    import capo_evs.types.create_entitlement_request
    import capo_evs.types.create_entitlement_response
    import capo_evs.types.create_environment_connector_request
    import capo_evs.types.create_environment_connector_response
    import capo_evs.types.create_environment_host_request
    import capo_evs.types.create_environment_host_response
    import capo_evs.types.create_environment_request
    import capo_evs.types.create_environment_response
    import capo_evs.types.delete_entitlement_request
    import capo_evs.types.delete_entitlement_response
    import capo_evs.types.delete_environment_connector_request
    import capo_evs.types.delete_environment_connector_response
    import capo_evs.types.delete_environment_host_request
    import capo_evs.types.delete_environment_host_response
    import capo_evs.types.delete_environment_request
    import capo_evs.types.delete_environment_response
    import capo_evs.types.disassociate_eip_from_vlan_request
    import capo_evs.types.disassociate_eip_from_vlan_response
    import capo_evs.types.entitlement_type
    import capo_evs.types.environment_id
    import capo_evs.types.environment_name
    import capo_evs.types.environment_state_list
    import capo_evs.types.environment_summary
    import capo_evs.types.esx_version
    import capo_evs.types.get_depot_url_request
    import capo_evs.types.get_depot_url_response
    import capo_evs.types.get_environment_request
    import capo_evs.types.get_environment_response
    import capo_evs.types.get_versions_request
    import capo_evs.types.get_versions_response
    import capo_evs.types.host
    import capo_evs.types.host_info_for_create
    import capo_evs.types.host_info_for_create_list
    import capo_evs.types.host_name
    import capo_evs.types.initial_vlans
    import capo_evs.types.license_info_list
    import capo_evs.types.list_environment_connectors_request
    import capo_evs.types.list_environment_connectors_response
    import capo_evs.types.list_environment_hosts_request
    import capo_evs.types.list_environment_hosts_response
    import capo_evs.types.list_environment_vlans_request
    import capo_evs.types.list_environment_vlans_response
    import capo_evs.types.list_environments_request
    import capo_evs.types.list_environments_response
    import capo_evs.types.list_tags_for_resource_request
    import capo_evs.types.list_tags_for_resource_response
    import capo_evs.types.list_vm_entitlements_request
    import capo_evs.types.list_vm_entitlements_response
    import capo_evs.types.max_results
    import capo_evs.types.pagination_token
    import capo_evs.types.request_tag_map
    import capo_evs.types.secret_identifier
    import capo_evs.types.service_access_security_groups
    import capo_evs.types.subnet_id
    import capo_evs.types.tag_keys
    import capo_evs.types.tag_resource_request
    import capo_evs.types.tag_resource_response
    import capo_evs.types.untag_resource_request
    import capo_evs.types.untag_resource_response
    import capo_evs.types.update_environment_connector_request
    import capo_evs.types.update_environment_connector_response
    import capo_evs.types.vcf_hostnames
    import capo_evs.types.vcf_version
    import capo_evs.types.vlan
    import capo_evs.types.vm_entitlement
    import capo_evs.types.vm_id_list
    import capo_evs.types.vpc_id


class AsyncevsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncevsClient:
    """A client for the ``evs`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncevsClientConfig(
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
        self.environment_resource = AsyncEnvironmentResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncevsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncevsClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def get_versions(
        self, *, config_overrides: Optional[AsyncevsClientConfig] = None
    ) -> "capo_evs.types.get_versions_response.GetVersionsResponse":
        """<p>Returns information about VCF versions, ESX versions and EC2 instance types provided by Amazon EVS. For each VCF version, the response also includes the default ESX version and provided EC2 instance types.</p>

        Raises:
            capo_evs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.get_versions_request.GetVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.get_versions_response.GetVersionsResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.get_versions

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.get_versions.async_get_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.get_versions_request.GetVersionsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_evs.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> "capo_evs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for an Amazon EVS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list tags for.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_evs.types.arn.Arn",
        tags: "capo_evs.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> "capo_evs.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to an Amazon EVS resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted. Tags that you create for Amazon EVS resources don't propagate to any other resources associated with the environment. For example, if you tag an environment with this operation, that tag doesn't automatically propagate to the VLAN subnets and hosts associated with the environment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other environment or Amazon Web Services resources.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one or more Amazon EVS resources exceeds the maximum allowed. For a list of Amazon EVS quotas, see <a href=\"https://docs.aws.amazon.com/evs/latest/userguide/service-quotas-evs.html\">Amazon EVS endpoints and quotas</a> in the <i>Amazon EVS User Guide</i>. Delete some resources or request an increase in your service quota. To request an increase, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html\">Amazon Web Services Service Quotas</a> in the <i>Amazon Web Services General Reference Guide</i>. </p>
            capo_evs.errors.tag_policy_exception.TagPolicyException: <note> <p> <code>TagPolicyException</code> is deprecated. See <a href=\"https://docs.aws.amazon.com/evs/latest/APIReference/API_ValidationException.html\"> <code>ValidationException</code> </a> instead.</p> </note> <p>The request doesn't comply with IAM tag policy. Correct your request and then retry it.</p>
            capo_evs.errors.too_many_tags_exception.TooManyTagsException: <note> <p> <code>TooManyTagsException</code> is deprecated. See <a href=\"https://docs.aws.amazon.com/evs/latest/APIReference/API_ServiceQuotaExceededException.html\"> <code>ServiceQuotaExceededException</code> </a> instead.</p> </note> <p>A service resource associated with the request has more than 200 tags.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_evs.types.arn.Arn",
        tag_keys: "capo_evs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> "capo_evs.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from an Amazon EVS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>
            tag_keys: <p>The keys of the tags to delete.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.tag_policy_exception.TagPolicyException: <note> <p> <code>TagPolicyException</code> is deprecated. See <a href=\"https://docs.aws.amazon.com/evs/latest/APIReference/API_ValidationException.html\"> <code>ValidationException</code> </a> instead.</p> </note> <p>The request doesn't comply with IAM tag policy. Correct your request and then retry it.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_environment(
        self,
        vpc_id: "capo_evs.types.vpc_id.VpcId",
        service_access_subnet_id: "capo_evs.types.subnet_id.SubnetId",
        vcf_version: "capo_evs.types.vcf_version.VcfVersion",
        terms_accepted: bool,
        license_info: "capo_evs.types.license_info_list.LicenseInfoList",
        initial_vlans: "capo_evs.types.initial_vlans.InitialVlans",
        hosts: "capo_evs.types.host_info_for_create_list.HostInfoForCreateList",
        connectivity_info: "capo_evs.types.connectivity_info.ConnectivityInfo",
        vcf_hostnames: "capo_evs.types.vcf_hostnames.VcfHostnames",
        site_id: str,
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
        environment_name: Optional[
            "capo_evs.types.environment_name.EnvironmentName"
        ] = None,
        kms_key_id: Optional[str] = None,
        tags: Optional["capo_evs.types.request_tag_map.RequestTagMap"] = None,
        service_access_security_groups: Optional[
            "capo_evs.types.service_access_security_groups.ServiceAccessSecurityGroups"
        ] = None,
    ) -> "capo_evs.types.create_environment_response.CreateEnvironmentResponse":
        r"""<p>Creates an Amazon EVS environment that runs VCF software, such as SDDC Manager, NSX Manager, and vCenter Server.</p> <p>During environment creation, Amazon EVS performs validations on DNS settings, provisions VLAN subnets and hosts, and deploys the supplied version of VCF.</p> <p>It can take several hours to create an environment. After the deployment completes, you can configure VCF in the vSphere user interface according to your needs.</p> <important> <p>When creating a new environment, the default ESX version for the selected VCF version will be used, you cannot choose a specific ESX version in <code>CreateEnvironment</code> action. When a host has been added with a specific ESX version, it can only be upgraded using vCenter Lifecycle Manager.</p> </important> <note> <p>You cannot use the <code>dedicatedHostId</code> and <code>placementGroupId</code> parameters together in the same <code>CreateEnvironment</code> action. This results in a <code>ValidationException</code> response.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_name: <p>The name to give to your environment. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character, and can't be longer than 100 characters. The name must be unique within the Amazon Web Services Region and Amazon Web Services account that you're creating the environment in.</p>
            kms_key_id: <p>A unique ID for the customer-managed KMS key that is used to encrypt the VCF credential pairs for SDDC Manager, NSX Manager, and vCenter appliances. These credentials are stored in Amazon Web Services Secrets Manager.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>
            service_access_security_groups: <p>The security group that controls communication between the Amazon EVS control plane and VPC. The default security group is used if a custom security group isn't specified.</p> <p>The security group should allow access to the following.</p> <ul> <li> <p>TCP/UDP access to the DNS servers</p> </li> <li> <p>HTTPS/SSH access to the host management VLAN subnet</p> </li> <li> <p>HTTPS/SSH access to the Management VM VLAN subnet</p> </li> </ul> <p>You should avoid modifying the security group rules after deployment, as this can break the persistent connection between the Amazon EVS control plane and VPC. This can cause future environment actions like adding or removing hosts to fail.</p>
            vpc_id: <p>A unique ID for the VPC that the environment is deployed inside.</p> <p>Amazon EVS requires that all VPC subnets exist in a single Availability Zone in a Region where the service is available.</p> <p>The VPC that you specify must have a valid DHCP option set with domain name, at least two DNS servers, and an NTP server. These settings are used to configure your VCF appliances and hosts. The VPC cannot be used with any other deployed Amazon EVS environment. Amazon EVS does not provide multi-VPC support for environments at this time.</p> <p>Amazon EVS does not support the following Amazon Web Services networking options for NSX overlay connectivity: cross-Region VPC peering, Amazon S3 gateway endpoints, or Amazon Web Services Direct Connect virtual private gateway associations.</p> <note> <p>Ensure that you specify a VPC that is adequately sized to accommodate the Amazon EVS subnets.</p> </note>
            service_access_subnet_id: <p>The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to validate mandatory DNS records for your VCF appliances and hosts and create the environment.</p>
            vcf_version: <p> The VCF version to use for the environment.</p>
            terms_accepted: <p>Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.</p>
            license_info: <p>The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.</p> <p>For information about minimum license requirements, see <a href=\"https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html\">the VCF subscriptions section</a> in the <i>Amazon EVS User Guide</i>.</p> <p>VCF licenses can be used for only one Amazon EVS environment. Amazon EVS does not support reuse of VCF licenses for multiple environments.</p> <p>VCF license information can be retrieved from the Broadcom portal.</p>
            initial_vlans: <p>The initial VLAN subnets for the Amazon EVS environment.</p> <note> <p>For each Amazon EVS VLAN subnet, you must specify a non-overlapping CIDR block. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.</p> </note>
            hosts: <p>The ESX hosts to add to the environment. Amazon EVS requires that you provide details for a minimum of 4 hosts during environment creation.</p> <p>For each host, you must provide the desired hostname, EC2 SSH keypair name, and EC2 instance type. Optionally, you can also provide a partition or cluster placement group to use, or use Amazon EC2 Dedicated Hosts.</p>
            connectivity_info: <p> The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX edges over the NSX uplink subnet, providing BGP-based dynamic routing for overlay networks.</p>
            vcf_hostnames: <p>The DNS hostnames for the virtual machines that host the VCF management appliances. Amazon EVS requires that you provide DNS hostnames for the following appliances: vCenter, NSX Manager, SDDC Manager, and Cloud Builder.</p>
            site_id: <p>The Broadcom Site ID that is allocated to you as part of your electronic software delivery. This ID allows customer access to the Broadcom portal, and is provided to you by Broadcom at the close of your software contract or contract renewal. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.</p>

        Raises:
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.create_environment

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.create_environment_request.CreateEnvironmentRequest = {
            "vpc_id": vpc_id,
            "service_access_subnet_id": service_access_subnet_id,
            "vcf_version": vcf_version,
            "terms_accepted": terms_accepted,
            "license_info": license_info,
            "initial_vlans": initial_vlans,
            "hosts": hosts,
            "connectivity_info": connectivity_info,
            "vcf_hostnames": vcf_hostnames,
            "site_id": site_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if service_access_security_groups is not None:
            input_["service_access_security_groups"] = service_access_security_groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> "capo_evs.types.get_environment_response.GetEnvironmentResponse":
        """<p>Returns a description of the specified environment.</p>

        Args:
            environment_id: <p>A unique ID for the environment.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.get_environment_request.GetEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.get_environment

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.get_environment_request.GetEnvironmentRequest = {
            "environment_id": environment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> "capo_evs.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes an Amazon EVS environment.</p> <p>Amazon EVS environments will only be enabled for deletion once the hosts are deleted. You can delete hosts using the <code>DeleteEnvironmentHost</code> action.</p> <p>Environment deletion also deletes the associated Amazon EVS VLAN subnets and Amazon Web Services Secrets Manager secrets that Amazon EVS created. Amazon Web Services resources that you create are not deleted. These resources may continue to incur costs.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID associated with the environment to be deleted.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.delete_environment

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.delete_environment_request.DeleteEnvironmentRequest = {
            "environment_id": environment_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environments(
        self,
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
        state: Optional[
            "capo_evs.types.environment_state_list.EnvironmentStateList"
        ] = None,
    ) -> "capo_evs.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists the Amazon EVS environments in your Amazon Web Services account in the specified Amazon Web Services Region.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            state: <p>The state of an environment. Used to filter response results to return only environments with the specified <code>environmentState</code>.</p>

        Raises:
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.list_environments

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.list_environments_request.ListEnvironmentsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state is not None:
            input_["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environments(
        self,
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
        state: Optional[
            "capo_evs.types.environment_state_list.EnvironmentStateList"
        ] = None,
    ) -> "AsyncIterator[capo_evs.types.environment_summary.EnvironmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                state=state,
            )
            _page = _resolve_path(_response, ("environment_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_eip_to_vlan(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        vlan_name: str,
        allocation_id: "capo_evs.types.allocation_id.AllocationId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> "capo_evs.types.associate_eip_to_vlan_response.AssociateEipToVlanResponse":
        """<p>Associates an Elastic IP address with a public HCX VLAN. This operation is only allowed for public HCX VLANs at this time.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment containing the VLAN that the Elastic IP address associates with.</p>
            vlan_name: <p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>
            allocation_id: <p>The Elastic IP address allocation ID.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.associate_eip_to_vlan_request.AssociateEipToVlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.associate_eip_to_vlan_response.AssociateEipToVlanResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.associate_eip_to_vlan

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.associate_eip_to_vlan.async_associate_eip_to_vlan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.associate_eip_to_vlan_request.AssociateEipToVlanRequest = {
            "environment_id": environment_id,
            "vlan_name": vlan_name,
            "allocation_id": allocation_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_entitlement(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        connector_id: "capo_evs.types.connector_id.ConnectorId",
        entitlement_type: "capo_evs.types.entitlement_type.EntitlementType",
        vm_ids: "capo_evs.types.vm_id_list.VmIdList",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> "capo_evs.types.create_entitlement_response.CreateEntitlementResponse":
        """<p>Creates a Windows Server License entitlement for virtual machines in an Amazon EVS environment using the provided vCenter Server connector. This is an asynchronous operation. Amazon EVS validates the specified virtual machines before starting usage tracking.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment to create the entitlement in.</p>
            connector_id: <p>A unique ID for the connector associated with the entitlement.</p>
            entitlement_type: <p>The type of entitlement to create.</p>
            vm_ids: <p>The list of VMware vSphere virtual machine managed object IDs to create entitlements for.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.create_entitlement_request.CreateEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.create_entitlement_response.CreateEntitlementResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.create_entitlement

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.create_entitlement.async_create_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.create_entitlement_request.CreateEntitlementRequest = {
            "environment_id": environment_id,
            "connector_id": connector_id,
            "entitlement_type": entitlement_type,
            "vm_ids": vm_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment_connector(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        type: "capo_evs.types.connector_type.ConnectorType",
        appliance_fqdn: "capo_evs.types.appliance_fqdn.ApplianceFqdn",
        secret_identifier: "capo_evs.types.secret_identifier.SecretIdentifier",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> "capo_evs.types.create_environment_connector_response.CreateEnvironmentConnectorResponse":
        """<p>Creates a connector for an Amazon EVS environment. A connector establishes a connection to a VCF appliance, such as vCenter, using a fully qualified domain name and an Amazon Web Services Secrets Manager secret that stores the appliance credentials.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment to create the connector in.</p>
            type: <p>The type of connector to create.</p>
            appliance_fqdn: <p>The fully qualified domain name (FQDN) of the VCF appliance that the connector targets.</p>
            secret_identifier: <p>The ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p> <important> <p>Do not use credentials with Administrator privileges. We recommend using a service account with the minimum required permissions.</p> </important>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.create_environment_connector_request.CreateEnvironmentConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.create_environment_connector_response.CreateEnvironmentConnectorResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.create_environment_connector

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.create_environment_connector.async_create_environment_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.create_environment_connector_request.CreateEnvironmentConnectorRequest = {
            "environment_id": environment_id,
            "type": type,
            "appliance_fqdn": appliance_fqdn,
            "secret_identifier": secret_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment_host(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        host: "capo_evs.types.host_info_for_create.HostInfoForCreate",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
        esx_version: Optional["capo_evs.types.esx_version.EsxVersion"] = None,
    ) -> (
        "capo_evs.types.create_environment_host_response.CreateEnvironmentHostResponse"
    ):
        """<p>Creates an ESX host and adds it to an Amazon EVS environment. Amazon EVS supports 4-32 hosts per environment.</p> <p>This action can only be used after the Amazon EVS environment is deployed.</p> <p>You can use the <code>dedicatedHostId</code> parameter to specify an Amazon EC2 Dedicated Host for ESX host creation.</p> <p> You can use the <code>placementGroupId</code> parameter to specify a cluster or partition placement group to launch EC2 instances into.</p> <note> <p>If you don't specify an ESX version when adding hosts using <code>CreateEnvironmentHost</code> action, Amazon EVS automatically uses the default ESX version associated with your environment's VCF version. To find the default ESX version for a particular VCF version, use the <code>GetVersions</code> action.</p> </note> <note> <p>You cannot use the <code>dedicatedHostId</code> and <code>placementGroupId</code> parameters together in the same <code>CreateEnvironmentHost</code> action. This results in a <code>ValidationException</code> response.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the host is added to.</p>
            host: <p>The host that is created and added to the environment.</p>
            esx_version: <p>The ESX version to use for the host.</p>

        Raises:
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.create_environment_host_request.CreateEnvironmentHostRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.create_environment_host_response.CreateEnvironmentHostResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.create_environment_host

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.create_environment_host.async_create_environment_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.create_environment_host_request.CreateEnvironmentHostRequest = {
            "environment_id": environment_id,
            "host": host,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if esx_version is not None:
            input_["esx_version"] = esx_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_entitlement(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        connector_id: "capo_evs.types.connector_id.ConnectorId",
        entitlement_type: "capo_evs.types.entitlement_type.EntitlementType",
        vm_ids: "capo_evs.types.vm_id_list.VmIdList",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> "capo_evs.types.delete_entitlement_response.DeleteEntitlementResponse":
        """<p>Deletes a Windows Server License entitlement for virtual machines in an Amazon EVS environment. Deleting an entitlement stops usage tracking for the specified virtual machines.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the entitlement deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the entitlement belongs to.</p>
            connector_id: <p>A unique ID for the connector associated with the entitlement.</p>
            entitlement_type: <p>The type of entitlement to delete.</p>
            vm_ids: <p>The list of VMware vSphere virtual machine managed object IDs to delete entitlements for.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.delete_entitlement_request.DeleteEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.delete_entitlement_response.DeleteEntitlementResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.delete_entitlement

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.delete_entitlement.async_delete_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.delete_entitlement_request.DeleteEntitlementRequest = {
            "environment_id": environment_id,
            "connector_id": connector_id,
            "entitlement_type": entitlement_type,
            "vm_ids": vm_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_connector(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        connector_id: "capo_evs.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> "capo_evs.types.delete_environment_connector_response.DeleteEnvironmentConnectorResponse":
        """<p>Deletes a connector from an Amazon EVS environment.</p> <note> <p>Before deleting a connector, you must remove all entitlements that are associated with the same vCenter.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the connector belongs to.</p>
            connector_id: <p>A unique ID for the connector to be deleted.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.delete_environment_connector_request.DeleteEnvironmentConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.delete_environment_connector_response.DeleteEnvironmentConnectorResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.delete_environment_connector

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.delete_environment_connector.async_delete_environment_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.delete_environment_connector_request.DeleteEnvironmentConnectorRequest = {
            "environment_id": environment_id,
            "connector_id": connector_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_host(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        host_name: "capo_evs.types.host_name.HostName",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_evs.types.delete_environment_host_response.DeleteEnvironmentHostResponse"
    ):
        """<p>Deletes a host from an Amazon EVS environment.</p> <note> <p>Before deleting a host, you must unassign and decommission the host from within the SDDC Manager user interface. Not doing so could impact the availability of your virtual machines or result in data loss.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the host deletion request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the host's environment.</p>
            host_name: <p>The DNS hostname associated with the host to be deleted.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.delete_environment_host_request.DeleteEnvironmentHostRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.delete_environment_host_response.DeleteEnvironmentHostResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.delete_environment_host

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.delete_environment_host.async_delete_environment_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.delete_environment_host_request.DeleteEnvironmentHostRequest = {
            "environment_id": environment_id,
            "host_name": host_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_eip_from_vlan(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        vlan_name: str,
        association_id: "capo_evs.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
    ) -> "capo_evs.types.disassociate_eip_from_vlan_response.DisassociateEipFromVlanResponse":
        """<p>Disassociates an Elastic IP address from a public HCX VLAN. This operation is only allowed for public HCX VLANs at this time.</p>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment containing the VLAN that the Elastic IP address disassociates from.</p>
            vlan_name: <p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>
            association_id: <p> A unique ID for the Elastic IP address association.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.disassociate_eip_from_vlan_request.DisassociateEipFromVlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.disassociate_eip_from_vlan_response.DisassociateEipFromVlanResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.disassociate_eip_from_vlan

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.disassociate_eip_from_vlan.async_disassociate_eip_from_vlan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.disassociate_eip_from_vlan_request.DisassociateEipFromVlanRequest = {
            "environment_id": environment_id,
            "vlan_name": vlan_name,
            "association_id": association_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_depot_url(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        rotate: Optional[bool] = None,
    ) -> "capo_evs.types.get_depot_url_response.GetDepotUrlResponse":
        """<p>Returns a URL and authentication token for accessing the Amazon EVS Custom Addon depot. Configure the depot URL as a download source in vSphere Lifecycle Manager (vLCM) to sync and install the Amazon EVS Custom Addon.</p> <p>The depot URL remains active until you rotate the authentication token by calling this action with <code>rotate</code> set to <code>true</code>.</p>

        Args:
            environment_id: <p>The unique ID of the Amazon EVS environment to get the depot URL for.</p>
            rotate: <p>Revokes the current authentication token and returns a new depot URL with a new token. Previously issued depot URLs will stop working within 5 minutes of rotation.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.get_depot_url_request.GetDepotUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.get_depot_url_response.GetDepotUrlResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.get_depot_url

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.get_depot_url.async_get_depot_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.get_depot_url_request.GetDepotUrlRequest = {
            "environment_id": environment_id
        }
        if rotate is not None:
            input_["rotate"] = rotate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environment_connectors(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "capo_evs.types.list_environment_connectors_response.ListEnvironmentConnectorsResponse":
        """<p>Lists the connectors within an environment. Returns the status of each connector and its applicable checks, among other connector details.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.list_environment_connectors_request.ListEnvironmentConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.list_environment_connectors_response.ListEnvironmentConnectorsResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.list_environment_connectors

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.list_environment_connectors.async_list_environment_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.list_environment_connectors_request.ListEnvironmentConnectorsRequest = {
            "environment_id": environment_id
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

    async def iter_list_environment_connectors(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_evs.types.connector.Connector]":
        _token = next_token
        while True:
            _response = await self.list_environment_connectors(
                environment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_hosts(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "capo_evs.types.list_environment_hosts_response.ListEnvironmentHostsResponse":
        """<p>List the hosts within an environment.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.list_environment_hosts_request.ListEnvironmentHostsRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.list_environment_hosts_response.ListEnvironmentHostsResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.list_environment_hosts

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.list_environment_hosts.async_list_environment_hosts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.list_environment_hosts_request.ListEnvironmentHostsRequest = {
            "environment_id": environment_id
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

    async def iter_list_environment_hosts(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_evs.types.host.Host]":
        _token = next_token
        while True:
            _response = await self.list_environment_hosts(
                environment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environment_hosts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_vlans(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "capo_evs.types.list_environment_vlans_response.ListEnvironmentVlansResponse":
        """<p>Lists environment VLANs that are associated with the specified environment.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.list_environment_vlans_request.ListEnvironmentVlansRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.list_environment_vlans_response.ListEnvironmentVlansResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.list_environment_vlans

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.list_environment_vlans.async_list_environment_vlans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.list_environment_vlans_request.ListEnvironmentVlansRequest = {
            "environment_id": environment_id
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

    async def iter_list_environment_vlans(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_evs.types.vlan.Vlan]":
        _token = next_token
        while True:
            _response = await self.list_environment_vlans(
                environment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environment_vlans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_vm_entitlements(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        connector_id: "capo_evs.types.connector_id.ConnectorId",
        entitlement_type: "capo_evs.types.entitlement_type.EntitlementType",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "capo_evs.types.list_vm_entitlements_response.ListVmEntitlementsResponse":
        """<p>Lists the Windows Server License entitlements for virtual machines in an Amazon EVS environment. Returns existing entitlements for virtual machines associated with the specified environment and connector.</p>

        Args:
            next_token: <p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>
            environment_id: <p>A unique ID for the environment.</p>
            connector_id: <p>A unique ID for the connector.</p>
            entitlement_type: <p>The type of entitlement to list.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.list_vm_entitlements_request.ListVmEntitlementsRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.list_vm_entitlements_response.ListVmEntitlementsResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.list_vm_entitlements

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.list_vm_entitlements.async_list_vm_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.list_vm_entitlements_request.ListVmEntitlementsRequest = {
            "environment_id": environment_id,
            "connector_id": connector_id,
            "entitlement_type": entitlement_type,
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

    async def iter_list_vm_entitlements(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        connector_id: "capo_evs.types.connector_id.ConnectorId",
        entitlement_type: "capo_evs.types.entitlement_type.EntitlementType",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        next_token: Optional["capo_evs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_evs.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_evs.types.vm_entitlement.VmEntitlement]":
        _token = next_token
        while True:
            _response = await self.list_vm_entitlements(
                environment_id,
                connector_id,
                entitlement_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entitlements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_environment_connector(
        self,
        environment_id: "capo_evs.types.environment_id.EnvironmentId",
        connector_id: "capo_evs.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
        client_token: Optional["capo_evs.types.client_token.ClientToken"] = None,
        appliance_fqdn: Optional["capo_evs.types.appliance_fqdn.ApplianceFqdn"] = None,
        secret_identifier: Optional[
            "capo_evs.types.secret_identifier.SecretIdentifier"
        ] = None,
    ) -> "capo_evs.types.update_environment_connector_response.UpdateEnvironmentConnectorResponse":
        """<p>Updates a connector for an Amazon EVS environment. You can update the Amazon Web Services Secrets Manager secret ARN or the appliance FQDN to reconfigure the connector metadata.</p> <note> <p>You cannot update both the secret and the FQDN in the same request.</p> </note>

        Args:
            client_token: <note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector update request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>
            environment_id: <p>A unique ID for the environment that the connector belongs to.</p>
            connector_id: <p>A unique ID for the connector to update.</p>
            appliance_fqdn: <p>The new fully qualified domain name (FQDN) of the VCF appliance that the connector connects to.</p>
            secret_identifier: <p>The new ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p>

        Raises:
            capo_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            capo_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            capo_evs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.</p>
            capo_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_evs.types.update_environment_connector_request.UpdateEnvironmentConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_evs.types.update_environment_connector_response.UpdateEnvironmentConnectorResponse"
        ]:
            import capo_evs._operations.amazon_elastic_v_mware_service.update_environment_connector

            (
                output,
                http_response,
            ) = await capo_evs._operations.amazon_elastic_v_mware_service.update_environment_connector.async_update_environment_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_evs.types.update_environment_connector_request.UpdateEnvironmentConnectorRequest = {
            "environment_id": environment_id,
            "connector_id": connector_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if appliance_fqdn is not None:
            input_["appliance_fqdn"] = appliance_fqdn
        if secret_identifier is not None:
            input_["secret_identifier"] = secret_identifier

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

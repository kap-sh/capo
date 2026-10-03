"""Generated from Smithy shape ``com.amazonaws.route53#AWSDnsV20130401``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_route_53._auth._signers
import capo_route_53._auth._sigv4
from capo_route_53._auth._identity import Credentials
from capo_route_53._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route_53._auth._zapros_handler import AuthMiddleware
from capo_route_53._pagination import resolve_path as _resolve_path
from capo_route_53._services._aws_config import aws_config
from capo_route_53._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_route_53.types.accelerated_recovery_enabled
    import capo_route_53.types.account_limit_type
    import capo_route_53.types.activate_key_signing_key_request
    import capo_route_53.types.activate_key_signing_key_response
    import capo_route_53.types.alarm_identifier
    import capo_route_53.types.associate_vpc_comment
    import capo_route_53.types.associate_vpc_with_hosted_zone_request
    import capo_route_53.types.associate_vpc_with_hosted_zone_response
    import capo_route_53.types.change_batch
    import capo_route_53.types.change_cidr_collection_request
    import capo_route_53.types.change_cidr_collection_response
    import capo_route_53.types.change_id
    import capo_route_53.types.change_resource_record_sets_request
    import capo_route_53.types.change_resource_record_sets_response
    import capo_route_53.types.change_tags_for_resource_request
    import capo_route_53.types.change_tags_for_resource_response
    import capo_route_53.types.child_health_check_list
    import capo_route_53.types.cidr_block_summary
    import capo_route_53.types.cidr_collection_changes
    import capo_route_53.types.cidr_location_name_default_not_allowed
    import capo_route_53.types.cidr_nonce
    import capo_route_53.types.cloud_watch_logs_log_group_arn
    import capo_route_53.types.collection_name
    import capo_route_53.types.collection_summary
    import capo_route_53.types.collection_version
    import capo_route_53.types.create_cidr_collection_request
    import capo_route_53.types.create_cidr_collection_response
    import capo_route_53.types.create_health_check_request
    import capo_route_53.types.create_health_check_response
    import capo_route_53.types.create_hosted_zone_request
    import capo_route_53.types.create_hosted_zone_response
    import capo_route_53.types.create_key_signing_key_request
    import capo_route_53.types.create_key_signing_key_response
    import capo_route_53.types.create_query_logging_config_request
    import capo_route_53.types.create_query_logging_config_response
    import capo_route_53.types.create_reusable_delegation_set_request
    import capo_route_53.types.create_reusable_delegation_set_response
    import capo_route_53.types.create_traffic_policy_instance_request
    import capo_route_53.types.create_traffic_policy_instance_response
    import capo_route_53.types.create_traffic_policy_request
    import capo_route_53.types.create_traffic_policy_response
    import capo_route_53.types.create_traffic_policy_version_request
    import capo_route_53.types.create_traffic_policy_version_response
    import capo_route_53.types.create_vpc_association_authorization_request
    import capo_route_53.types.create_vpc_association_authorization_response
    import capo_route_53.types.deactivate_key_signing_key_request
    import capo_route_53.types.deactivate_key_signing_key_response
    import capo_route_53.types.delete_cidr_collection_request
    import capo_route_53.types.delete_cidr_collection_response
    import capo_route_53.types.delete_health_check_request
    import capo_route_53.types.delete_health_check_response
    import capo_route_53.types.delete_hosted_zone_request
    import capo_route_53.types.delete_hosted_zone_response
    import capo_route_53.types.delete_key_signing_key_request
    import capo_route_53.types.delete_key_signing_key_response
    import capo_route_53.types.delete_query_logging_config_request
    import capo_route_53.types.delete_query_logging_config_response
    import capo_route_53.types.delete_reusable_delegation_set_request
    import capo_route_53.types.delete_reusable_delegation_set_response
    import capo_route_53.types.delete_traffic_policy_instance_request
    import capo_route_53.types.delete_traffic_policy_instance_response
    import capo_route_53.types.delete_traffic_policy_request
    import capo_route_53.types.delete_traffic_policy_response
    import capo_route_53.types.delete_vpc_association_authorization_request
    import capo_route_53.types.delete_vpc_association_authorization_response
    import capo_route_53.types.disable_hosted_zone_dnssec_request
    import capo_route_53.types.disable_hosted_zone_dnssec_response
    import capo_route_53.types.disabled
    import capo_route_53.types.disassociate_vpc_comment
    import capo_route_53.types.disassociate_vpc_from_hosted_zone_request
    import capo_route_53.types.disassociate_vpc_from_hosted_zone_response
    import capo_route_53.types.dns_name
    import capo_route_53.types.enable_hosted_zone_dnssec_request
    import capo_route_53.types.enable_hosted_zone_dnssec_response
    import capo_route_53.types.enable_sni
    import capo_route_53.types.failure_threshold
    import capo_route_53.types.fully_qualified_domain_name
    import capo_route_53.types.geo_location_continent_code
    import capo_route_53.types.geo_location_country_code
    import capo_route_53.types.geo_location_subdivision_code
    import capo_route_53.types.get_account_limit_request
    import capo_route_53.types.get_account_limit_response
    import capo_route_53.types.get_change_request
    import capo_route_53.types.get_change_response
    import capo_route_53.types.get_checker_ip_ranges_request
    import capo_route_53.types.get_checker_ip_ranges_response
    import capo_route_53.types.get_dnssec_request
    import capo_route_53.types.get_dnssec_response
    import capo_route_53.types.get_geo_location_request
    import capo_route_53.types.get_geo_location_response
    import capo_route_53.types.get_health_check_count_request
    import capo_route_53.types.get_health_check_count_response
    import capo_route_53.types.get_health_check_last_failure_reason_request
    import capo_route_53.types.get_health_check_last_failure_reason_response
    import capo_route_53.types.get_health_check_request
    import capo_route_53.types.get_health_check_response
    import capo_route_53.types.get_health_check_status_request
    import capo_route_53.types.get_health_check_status_response
    import capo_route_53.types.get_hosted_zone_count_request
    import capo_route_53.types.get_hosted_zone_count_response
    import capo_route_53.types.get_hosted_zone_limit_request
    import capo_route_53.types.get_hosted_zone_limit_response
    import capo_route_53.types.get_hosted_zone_request
    import capo_route_53.types.get_hosted_zone_response
    import capo_route_53.types.get_query_logging_config_request
    import capo_route_53.types.get_query_logging_config_response
    import capo_route_53.types.get_reusable_delegation_set_limit_request
    import capo_route_53.types.get_reusable_delegation_set_limit_response
    import capo_route_53.types.get_reusable_delegation_set_request
    import capo_route_53.types.get_reusable_delegation_set_response
    import capo_route_53.types.get_traffic_policy_instance_count_request
    import capo_route_53.types.get_traffic_policy_instance_count_response
    import capo_route_53.types.get_traffic_policy_instance_request
    import capo_route_53.types.get_traffic_policy_instance_response
    import capo_route_53.types.get_traffic_policy_request
    import capo_route_53.types.get_traffic_policy_response
    import capo_route_53.types.health_check
    import capo_route_53.types.health_check_config
    import capo_route_53.types.health_check_id
    import capo_route_53.types.health_check_nonce
    import capo_route_53.types.health_check_region_list
    import capo_route_53.types.health_check_version
    import capo_route_53.types.health_threshold
    import capo_route_53.types.hosted_zone
    import capo_route_53.types.hosted_zone_config
    import capo_route_53.types.hosted_zone_limit_type
    import capo_route_53.types.hosted_zone_type
    import capo_route_53.types.insufficient_data_health_status
    import capo_route_53.types.inverted
    import capo_route_53.types.ip_address
    import capo_route_53.types.list_cidr_blocks_request
    import capo_route_53.types.list_cidr_blocks_response
    import capo_route_53.types.list_cidr_collections_request
    import capo_route_53.types.list_cidr_collections_response
    import capo_route_53.types.list_cidr_locations_request
    import capo_route_53.types.list_cidr_locations_response
    import capo_route_53.types.list_geo_locations_request
    import capo_route_53.types.list_geo_locations_response
    import capo_route_53.types.list_health_checks_request
    import capo_route_53.types.list_health_checks_response
    import capo_route_53.types.list_hosted_zones_by_name_request
    import capo_route_53.types.list_hosted_zones_by_name_response
    import capo_route_53.types.list_hosted_zones_by_vpc_request
    import capo_route_53.types.list_hosted_zones_by_vpc_response
    import capo_route_53.types.list_hosted_zones_request
    import capo_route_53.types.list_hosted_zones_response
    import capo_route_53.types.list_query_logging_configs_request
    import capo_route_53.types.list_query_logging_configs_response
    import capo_route_53.types.list_resource_record_sets_request
    import capo_route_53.types.list_resource_record_sets_response
    import capo_route_53.types.list_reusable_delegation_sets_request
    import capo_route_53.types.list_reusable_delegation_sets_response
    import capo_route_53.types.list_tags_for_resource_request
    import capo_route_53.types.list_tags_for_resource_response
    import capo_route_53.types.list_tags_for_resources_request
    import capo_route_53.types.list_tags_for_resources_response
    import capo_route_53.types.list_traffic_policies_request
    import capo_route_53.types.list_traffic_policies_response
    import capo_route_53.types.list_traffic_policy_instances_by_hosted_zone_request
    import capo_route_53.types.list_traffic_policy_instances_by_hosted_zone_response
    import capo_route_53.types.list_traffic_policy_instances_by_policy_request
    import capo_route_53.types.list_traffic_policy_instances_by_policy_response
    import capo_route_53.types.list_traffic_policy_instances_request
    import capo_route_53.types.list_traffic_policy_instances_response
    import capo_route_53.types.list_traffic_policy_versions_request
    import capo_route_53.types.list_traffic_policy_versions_response
    import capo_route_53.types.list_vpc_association_authorizations_request
    import capo_route_53.types.list_vpc_association_authorizations_response
    import capo_route_53.types.location_summary
    import capo_route_53.types.nonce
    import capo_route_53.types.page_marker
    import capo_route_53.types.pagination_token
    import capo_route_53.types.port
    import capo_route_53.types.query_logging_config
    import capo_route_53.types.query_logging_config_id
    import capo_route_53.types.resettable_element_name_list
    import capo_route_53.types.resource_description
    import capo_route_53.types.resource_id
    import capo_route_53.types.resource_path
    import capo_route_53.types.resource_record_set_identifier
    import capo_route_53.types.reusable_delegation_set_limit_type
    import capo_route_53.types.rr_type
    import capo_route_53.types.search_string
    import capo_route_53.types.signing_key_name
    import capo_route_53.types.signing_key_status
    import capo_route_53.types.signing_key_string
    import capo_route_53.types.subnet_mask
    import capo_route_53.types.tag_key_list
    import capo_route_53.types.tag_list
    import capo_route_53.types.tag_resource_id
    import capo_route_53.types.tag_resource_id_list
    import capo_route_53.types.tag_resource_type
    import capo_route_53.types.test_dns_answer_request
    import capo_route_53.types.test_dns_answer_response
    import capo_route_53.types.traffic_policy_comment
    import capo_route_53.types.traffic_policy_document
    import capo_route_53.types.traffic_policy_id
    import capo_route_53.types.traffic_policy_instance_id
    import capo_route_53.types.traffic_policy_name
    import capo_route_53.types.traffic_policy_version
    import capo_route_53.types.traffic_policy_version_marker
    import capo_route_53.types.ttl
    import capo_route_53.types.update_health_check_request
    import capo_route_53.types.update_health_check_response
    import capo_route_53.types.update_hosted_zone_comment_request
    import capo_route_53.types.update_hosted_zone_comment_response
    import capo_route_53.types.update_hosted_zone_features_request
    import capo_route_53.types.update_hosted_zone_features_response
    import capo_route_53.types.update_traffic_policy_comment_request
    import capo_route_53.types.update_traffic_policy_comment_response
    import capo_route_53.types.update_traffic_policy_instance_request
    import capo_route_53.types.update_traffic_policy_instance_response
    import capo_route_53.types.uuid
    import capo_route_53.types.vpc
    import capo_route_53.types.vpc_id
    import capo_route_53.types.vpc_region


class Route53ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class Route53Client:
    """A client for the ``Route53`` service.

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
        self._config = Route53ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[Route53ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: Route53ClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def activate_key_signing_key(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        name: "capo_route_53.types.signing_key_name.SigningKeyName",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.activate_key_signing_key_response.ActivateKeySigningKeyResponse":
        """<p>Activates a key-signing key (KSK) so that it can be used for signing by DNSSEC. This operation changes the KSK status to <code>ACTIVE</code>.</p>

        Args:
            hosted_zone_id: <p>A unique string used to identify a hosted zone.</p>
            name: <p>A string used to identify a key-signing key (KSK). <code>Name</code> can include numbers, letters, and underscores (_). <code>Name</code> must be unique for each key-signing key in the same hosted zone.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_key_signing_key_status.InvalidKeySigningKeyStatus: <p>The key-signing key (KSK) status isn't valid or another KSK has the status <code>INTERNAL_FAILURE</code>.</p>
            capo_route_53.errors.invalid_kms_arn.InvalidKMSArn: <p>The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC signing.</p>
            capo_route_53.errors.invalid_signing_status.InvalidSigningStatus: <p>Your hosted zone status isn't valid for this operation. In the hosted zone, change the status to enable <code>DNSSEC</code> or disable <code>DNSSEC</code>.</p>
            capo_route_53.errors.no_such_key_signing_key.NoSuchKeySigningKey: <p>The specified key-signing key (KSK) doesn't exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.activate_key_signing_key_request.ActivateKeySigningKeyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.activate_key_signing_key_response.ActivateKeySigningKeyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.activate_key_signing_key

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.activate_key_signing_key.activate_key_signing_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.activate_key_signing_key_request.ActivateKeySigningKeyRequest = {
            "hosted_zone_id": hosted_zone_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_vpc_with_hosted_zone(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        vpc: "capo_route_53.types.vpc.VPC",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        comment: Optional[
            "capo_route_53.types.associate_vpc_comment.AssociateVPCComment"
        ] = None,
    ) -> "capo_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse":
        """<p>Associates an Amazon VPC with a private hosted zone. </p> <important> <p>To perform the association, the VPC and the private hosted zone must already exist. You can't convert a public hosted zone into a private hosted zone.</p> </important> <note> <p>If you want to associate a VPC that was created by using one Amazon Web Services account with a private hosted zone that was created by using a different account, the Amazon Web Services account that created the private hosted zone must first submit a <code>CreateVPCAssociationAuthorization</code> request. Then the account that created the VPC must submit an <code>AssociateVPCWithHostedZone</code> request.</p> </note> <note> <p>When granting access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.</p> <p>The following are the supported partitions:</p> <ul> <li> <p> <code>aws</code> - Amazon Web Services Regions</p> </li> <li> <p> <code>aws-cn</code> - China Regions</p> </li> <li> <p> <code>aws-us-gov</code> - Amazon Web Services GovCloud (US) Region</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Access Management</a> in the <i>Amazon Web Services General Reference</i>.</p> </note>

        Args:
            hosted_zone_id: <p>The ID of the private hosted zone that you want to associate an Amazon VPC with.</p> <p>Note that you can't associate a VPC with a hosted zone that doesn't have an existing VPC association.</p>
            vpc: <p>A complex type that contains information about the VPC that you want to associate with a private hosted zone.</p>
            comment: <p> <i>Optional:</i> A comment about the association request.</p>

        Raises:
            capo_route_53.errors.conflicting_domain_exists.ConflictingDomainExists: <p>The cause of this error depends on the operation that you're performing:</p> <ul> <li> <p> <b>Create a public hosted zone:</b> Two hosted zones that have the same name or that have a parent/child relationship (example.com and test.example.com) can't have any common name servers. You tried to create a hosted zone that has the same name as an existing hosted zone or that's the parent or child of an existing hosted zone, and you specified a delegation set that shares one or more name servers with the existing hosted zone. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html">CreateReusableDelegationSet</a>.</p> </li> <li> <p> <b>Create a private hosted zone:</b> A hosted zone with the specified name already exists and is already associated with the Amazon VPC that you specified.</p> </li> <li> <p> <b>Associate VPCs with a private hosted zone:</b> The VPC that you specified is already associated with another hosted zone that has the same name.</p> </li> </ul>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_vpc_id.InvalidVPCId: <p>The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.</p>
            capo_route_53.errors.limits_exceeded.LimitsExceeded: <p>This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.not_authorized_exception.NotAuthorizedException: <p>Associating the specified VPC with the specified hosted zone has not been authorized.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.public_zone_vpc_association.PublicZoneVPCAssociation: <p>You're trying to associate a VPC with a public hosted zone. Amazon Route 53 doesn't support associating a VPC with a public hosted zone.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To associate a VPC with a hosted zone
            The following example associates the VPC with ID vpc-1a2b3c4d with the hosted zone with ID Z3M3LMPEXAMPLE.

            >>> client.associate_vpc_with_hosted_zone(hosted_zone_id='Z3M3LMPEXAMPLE', vpc={'VPCId': 'vpc-1a2b3c4d', 'VPCRegion': 'us-east-2'}, comment='')
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.associate_vpc_with_hosted_zone_request.AssociateVPCWithHostedZoneRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.associate_vpc_with_hosted_zone_response.AssociateVPCWithHostedZoneResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.associate_vpc_with_hosted_zone

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.associate_vpc_with_hosted_zone.associate_vpc_with_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.associate_vpc_with_hosted_zone_request.AssociateVPCWithHostedZoneRequest = {
            "hosted_zone_id": hosted_zone_id,
            "vpc": vpc,
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

    def change_cidr_collection(
        self,
        id: "capo_route_53.types.uuid.UUID",
        changes: "capo_route_53.types.cidr_collection_changes.CidrCollectionChanges",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        collection_version: Optional[
            "capo_route_53.types.collection_version.CollectionVersion"
        ] = None,
    ) -> "capo_route_53.types.change_cidr_collection_response.ChangeCidrCollectionResponse":
        """<p>Creates, changes, or deletes CIDR blocks within a collection. Contains authoritative IP information mapping blocks to one or multiple locations.</p> <p>A change request can update multiple locations in a collection at a time, which is helpful if you want to move one or more CIDR blocks from one location to another in one transaction, without downtime. </p> <p> <b>Limits</b> </p> <p>The max number of CIDR blocks included in the request is 1000. As a result, big updates require multiple API calls.</p> <p> <b> PUT and DELETE_IF_EXISTS</b> </p> <p>Use <code>ChangeCidrCollection</code> to perform the following actions:</p> <ul> <li> <p> <code>PUT</code>: Create a CIDR block within the specified collection.</p> </li> <li> <p> <code> DELETE_IF_EXISTS</code>: Delete an existing CIDR block from the collection.</p> </li> </ul>

        Args:
            id: <p>The UUID of the CIDR collection to update.</p>
            collection_version: <p>A sequential counter that Amazon Route 53 sets to 1 when you create a collection and increments it by 1 each time you update the collection.</p> <p>We recommend that you use <code>ListCidrCollection</code> to get the current value of <code>CollectionVersion</code> for the collection that you want to update, and then include that value with the change request. This prevents Route 53 from overwriting an intervening update: </p> <ul> <li> <p>If the value in the request matches the value of <code>CollectionVersion</code> in the collection, Route 53 updates the collection.</p> </li> <li> <p>If the value of <code>CollectionVersion</code> in the collection is greater than the value in the request, the collection was changed after you got the version number. Route 53 does not update the collection, and it returns a <code>CidrCollectionVersionMismatch</code> error. </p> </li> </ul>
            changes: <p> Information about changes to a CIDR collection.</p>

        Raises:
            capo_route_53.errors.cidr_block_in_use_exception.CidrBlockInUseException: <p>This CIDR block is already in use.</p>
            capo_route_53.errors.cidr_collection_version_mismatch_exception.CidrCollectionVersionMismatchException: <p>The CIDR collection version you provided, doesn't match the one in the <code>ListCidrCollections</code> operation.</p>
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.limits_exceeded.LimitsExceeded: <p>This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.no_such_cidr_collection_exception.NoSuchCidrCollectionException: <p>The CIDR collection you specified, doesn't exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.change_cidr_collection_request.ChangeCidrCollectionRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.change_cidr_collection_response.ChangeCidrCollectionResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.change_cidr_collection

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.change_cidr_collection.change_cidr_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.change_cidr_collection_request.ChangeCidrCollectionRequest = {
            "id": id,
            "changes": changes,
        }
        if collection_version is not None:
            input_["collection_version"] = collection_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def change_resource_record_sets(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        change_batch: "capo_route_53.types.change_batch.ChangeBatch",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.change_resource_record_sets_response.ChangeResourceRecordSetsResponse":
        """<p>Creates, changes, or deletes a resource record set, which contains authoritative DNS information for a specified domain name or subdomain name. For example, you can use <code>ChangeResourceRecordSets</code> to create a resource record set that routes traffic for test.example.com to a web server that has an IP address of 192.0.2.44.</p> <p> <b>Deleting Resource Record Sets</b> </p> <p>To delete a resource record set, you must specify all the same values that you specified when you created it.</p> <p> <b>Change Batches and Transactional Changes</b> </p> <p>The request body must include a document with a <code>ChangeResourceRecordSetsRequest</code> element. The request body contains a list of change items, known as a change batch. Change batches are considered transactional changes. Route 53 validates the changes in the request and then either makes all or none of the changes in the change batch request. This ensures that DNS routing isn't adversely affected by partial changes to the resource record sets in a hosted zone. </p> <p>For example, suppose a change batch request contains two changes: it deletes the <code>CNAME</code> resource record set for www.example.com and creates an alias resource record set for www.example.com. If validation for both records succeeds, Route 53 deletes the first resource record set and creates the second resource record set in a single operation. If validation for either the <code>DELETE</code> or the <code>CREATE</code> action fails, then the request is canceled, and the original <code>CNAME</code> record continues to exist.</p> <note> <p>If you try to delete the same resource record set more than once in a single change batch, Route 53 returns an <code>InvalidChangeBatch</code> error.</p> </note> <p> <b>Traffic Flow</b> </p> <p>To create resource record sets for complex routing configurations, use either the traffic flow visual editor in the Route 53 console or the API actions for traffic policies and traffic policy instances. Save the configuration as a traffic policy, then associate the traffic policy with one or more domain names (such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in multiple hosted zones. You can roll back the updates if the new configuration isn't performing as expected. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html">Using Traffic Flow to Route DNS Traffic</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p> <b>Create, Delete, and Upsert</b> </p> <p>Use <code>ChangeResourceRecordsSetsRequest</code> to perform the following actions:</p> <ul> <li> <p> <code>CREATE</code>: Creates a resource record set that has the specified values.</p> </li> <li> <p> <code>DELETE</code>: Deletes an existing resource record set that has the specified values.</p> </li> <li> <p> <code>UPSERT</code>: If a resource set doesn't exist, Route 53 creates it. If a resource set exists Route 53 updates it with the values in the request. </p> </li> </ul> <p> <b>Syntaxes for Creating, Updating, and Deleting Resource Record Sets</b> </p> <p>The syntax for a request depends on the type of resource record set that you want to create, delete, or update, such as weighted, alias, or failover. The XML elements in your request must appear in the order listed in the syntax. </p> <p>For an example for each type of resource record set, see "Examples."</p> <p>Don't refer to the syntax in the "Parameter Syntax" section, which includes all of the elements for every kind of resource record set that you can create, delete, or update by using <code>ChangeResourceRecordSets</code>. </p> <p> <b>Change Propagation to Route 53 DNS Servers</b> </p> <p>When you submit a <code>ChangeResourceRecordSets</code> request, Route 53 propagates your changes to all of the Route 53 authoritative DNS servers managing the hosted zone. While your changes are propagating, <code>GetChange</code> returns a status of <code>PENDING</code>. When propagation is complete, <code>GetChange</code> returns a status of <code>INSYNC</code>. Changes generally propagate to all Route 53 name servers managing the hosted zone within 60 seconds. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html">GetChange</a>.</p> <p> <b>Limits on ChangeResourceRecordSets Requests</b> </p> <p>For information about the limits on a <code>ChangeResourceRecordSets</code> request, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>.</p>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone that contains the resource record sets that you want to change.</p>
            change_batch: <p>A complex type that contains an optional comment and the <code>Changes</code> element.</p>

        Raises:
            capo_route_53.errors.invalid_change_batch.InvalidChangeBatch: <p>This exception contains a list of messages that might contain one or more error messages. Each error message indicates one error in the change batch.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an alias resource record set
            The following example creates an alias resource record set that routes traffic to a CloudFront distribution.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'CloudFront distribution for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'AliasTarget': {'HostedZoneId': 'Z2FDTNDATAQYW2', 'DNSName': 'd123rk29d0stfj.cloudfront.net', 'EvaluateTargetHealth': False}}}]})
            To create failover alias resource record sets
            The following example creates primary and secondary failover alias resource record sets that route traffic to ELB load balancers. Traffic is generally routed to the primary resource, in the Ohio region. If that resource is unavailable, traffic is routed to the secondary resource, in the Oregon region.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'Failover alias configuration for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Ohio region', 'Failover': 'PRIMARY', 'AliasTarget': {'HostedZoneId': 'Z3AADJGX6KTTL2', 'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Oregon region', 'Failover': 'SECONDARY', 'AliasTarget': {'HostedZoneId': 'Z1H1FL5HABSF5', 'DNSName': 'example-com-987654321.us-west-2.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}]})
            To create failover resource record sets
            The following example creates primary and secondary failover resource record sets that route traffic to EC2 instances. Traffic is generally routed to the primary resource, in the Ohio region. If that resource is unavailable, traffic is routed to the secondary resource, in the Oregon region.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'Failover configuration for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Ohio region', 'Failover': 'PRIMARY', 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.44'}], 'HealthCheckId': 'abcdef11-2222-3333-4444-555555fedcba'}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Oregon region', 'Failover': 'SECONDARY', 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.45'}], 'HealthCheckId': 'abcdef66-7777-8888-9999-000000fedcba'}}]})
            To create geolocation alias resource record sets
            The following example creates four geolocation alias resource record sets that route traffic to ELB load balancers. Traffic is routed to one of four IP addresses, for North America (NA), for South America (SA), for Europe (EU), and for all other locations (*).

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'Geolocation alias configuration for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'North America', 'GeoLocation': {'ContinentCode': 'NA'}, 'AliasTarget': {'HostedZoneId': 'Z3AADJGX6KTTL2', 'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'South America', 'GeoLocation': {'ContinentCode': 'SA'}, 'AliasTarget': {'HostedZoneId': 'Z2P70J7HTTTPLU', 'DNSName': 'example-com-234567890.sa-east-1.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Europe', 'GeoLocation': {'ContinentCode': 'EU'}, 'AliasTarget': {'HostedZoneId': 'Z215JYRZR1TBD5', 'DNSName': 'example-com-234567890.eu-central-1.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Other locations', 'GeoLocation': {'CountryCode': '*'}, 'AliasTarget': {'HostedZoneId': 'Z1LMS91P8CMLE5', 'DNSName': 'example-com-234567890.ap-southeast-1.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}]})
            To create geolocation resource record sets
            The following example creates four geolocation resource record sets that use IPv4 addresses to route traffic to resources such as web servers running on EC2 instances. Traffic is routed to one of four IP addresses, for North America (NA), for South America (SA), for Europe (EU), and for all other locations (*).

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'Geolocation configuration for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'North America', 'GeoLocation': {'ContinentCode': 'NA'}, 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.44'}]}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'South America', 'GeoLocation': {'ContinentCode': 'SA'}, 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.45'}]}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Europe', 'GeoLocation': {'ContinentCode': 'EU'}, 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.46'}]}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Other locations', 'GeoLocation': {'CountryCode': '*'}, 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.47'}]}}]})
            To create latency alias resource record sets
            The following example creates two latency alias resource record sets that route traffic for example.com to ELB load balancers. Requests are routed either to the Ohio region or the Oregon region, depending on the latency between the user and those regions.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'ELB load balancers for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Ohio region', 'Region': 'us-east-2', 'AliasTarget': {'HostedZoneId': 'Z3AADJGX6KTTL2', 'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Oregon region', 'Region': 'us-west-2', 'AliasTarget': {'HostedZoneId': 'Z1H1FL5HABSF5', 'DNSName': 'example-com-987654321.us-west-2.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}]})
            To create latency resource record sets
            The following example creates two latency resource record sets that route traffic to EC2 instances. Traffic for example.com is routed either to the Ohio region or the Oregon region, depending on the latency between the user and those regions.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'EC2 instances for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Ohio region', 'Region': 'us-east-2', 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.44'}], 'HealthCheckId': 'abcdef11-2222-3333-4444-555555fedcba'}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Oregon region', 'Region': 'us-west-2', 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.45'}], 'HealthCheckId': 'abcdef66-7777-8888-9999-000000fedcba'}}]})
            To create a basic resource record set
            The following example creates a resource record set that routes Internet traffic to a resource with an IP address of 192.0.2.44.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'Web server for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.44'}]}}]})
            To create weighted alias resource record sets
            The following example creates two weighted alias resource record sets that route traffic to ELB load balancers. The resource with a Weight of 100 will get 1/3rd of traffic (100/100+200), and the other resource will get the rest of the traffic for example.com.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'ELB load balancers for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Ohio region', 'Weight': 100, 'AliasTarget': {'HostedZoneId': 'Z3AADJGX6KTTL2', 'DNSName': 'example-com-123456789.us-east-2.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Oregon region', 'Weight': 200, 'AliasTarget': {'HostedZoneId': 'Z1H1FL5HABSF5', 'DNSName': 'example-com-987654321.us-west-2.elb.amazonaws.com ', 'EvaluateTargetHealth': True}}}]})
            To create weighted resource record sets
            The following example creates two weighted resource record sets. The resource with a Weight of 100 will get 1/3rd of traffic (100/100+200), and the other resource will get the rest of the traffic for example.com.

            >>> client.change_resource_record_sets(hosted_zone_id='Z3M3LMPEXAMPLE', change_batch={'Comment': 'Web servers for example.com', 'Changes': [{'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Seattle data center', 'Weight': 100, 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.44'}], 'HealthCheckId': 'abcdef11-2222-3333-4444-555555fedcba'}}, {'Action': 'CREATE', 'ResourceRecordSet': {'Name': 'example.com', 'Type': 'A', 'SetIdentifier': 'Portland data center', 'Weight': 200, 'TTL': 60, 'ResourceRecords': [{'Value': '192.0.2.45'}], 'HealthCheckId': 'abcdef66-7777-8888-9999-000000fedcba'}}]})
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.change_resource_record_sets_request.ChangeResourceRecordSetsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.change_resource_record_sets_response.ChangeResourceRecordSetsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.change_resource_record_sets

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.change_resource_record_sets.change_resource_record_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.change_resource_record_sets_request.ChangeResourceRecordSetsRequest = {
            "hosted_zone_id": hosted_zone_id,
            "change_batch": change_batch,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def change_tags_for_resource(
        self,
        resource_type: "capo_route_53.types.tag_resource_type.TagResourceType",
        resource_id: "capo_route_53.types.tag_resource_id.TagResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        add_tags: Optional["capo_route_53.types.tag_list.TagList"] = None,
        remove_tag_keys: Optional["capo_route_53.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse":
        """<p>Adds, edits, or deletes tags for a health check or a hosted zone.</p> <p>For information about using tags for cost allocation, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Billing and Cost Management User Guide</i>.</p>

        Args:
            resource_type: <p>The type of the resource.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>
            resource_id: <p>The ID of the resource for which you want to add, change, or delete tags.</p>
            add_tags: <p>A complex type that contains a list of the tags that you want to add to the specified health check or hosted zone and/or the tags that you want to edit <code>Value</code> for.</p> <p>You can add a maximum of 10 tags to a health check or a hosted zone.</p>
            remove_tag_keys: <p>A complex type that contains a list of the tags that you want to delete from the specified health check or hosted zone. You can specify up to 10 keys.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add or remove tags from a hosted zone or health check
            The following example adds two tags and removes one tag from the hosted zone with ID Z3M3LMPEXAMPLE.

            >>> client.change_tags_for_resource(resource_type='hostedzone', resource_id='Z3M3LMPEXAMPLE', add_tags=[{'Key': 'apex', 'Value': '3874'}, {'Key': 'acme', 'Value': '4938'}], remove_tag_keys=['Nadir'])
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.change_tags_for_resource_request.ChangeTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.change_tags_for_resource_response.ChangeTagsForResourceResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.change_tags_for_resource

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.change_tags_for_resource.change_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.change_tags_for_resource_request.ChangeTagsForResourceRequest = {
            "resource_type": resource_type,
            "resource_id": resource_id,
        }
        if add_tags is not None:
            input_["add_tags"] = add_tags
        if remove_tag_keys is not None:
            input_["remove_tag_keys"] = remove_tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cidr_collection(
        self,
        name: "capo_route_53.types.collection_name.CollectionName",
        caller_reference: "capo_route_53.types.cidr_nonce.CidrNonce",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.create_cidr_collection_response.CreateCidrCollectionResponse":
        """<p>Creates a CIDR collection in the current Amazon Web Services account.</p>

        Args:
            name: <p>A unique identifier for the account that can be used to reference the collection from other API calls.</p>
            caller_reference: <p>A client-specific token that allows requests to be securely retried so that the intended outcome will only occur once, retries receive a similar response, and there are no additional edge cases to handle.</p>

        Raises:
            capo_route_53.errors.cidr_collection_already_exists_exception.CidrCollectionAlreadyExistsException: <p>A CIDR collection with this name and a different caller reference already exists in this account.</p>
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.limits_exceeded.LimitsExceeded: <p>This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_cidr_collection_request.CreateCidrCollectionRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_cidr_collection_response.CreateCidrCollectionResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_cidr_collection

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_cidr_collection.create_cidr_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_cidr_collection_request.CreateCidrCollectionRequest = {
            "name": name,
            "caller_reference": caller_reference,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_health_check(
        self,
        caller_reference: "capo_route_53.types.health_check_nonce.HealthCheckNonce",
        health_check_config: "capo_route_53.types.health_check_config.HealthCheckConfig",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.create_health_check_response.CreateHealthCheckResponse":
        """<p>Creates a new health check.</p> <p>For information about adding health checks to resource record sets, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSet.html#Route53-Type-ResourceRecordSet-HealthCheckId">HealthCheckId</a> in <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html">ChangeResourceRecordSets</a>. </p> <p> <b>ELB Load Balancers</b> </p> <p>If you're registering EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the EC2 instances. When you register an EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to a Route 53 health check.</p> <p> <b>Private Hosted Zones</b> </p> <p>You can associate health checks with failover resource record sets in a private hosted zone. Note the following:</p> <ul> <li> <p>Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC.</p> </li> <li> <p>You can configure a health checker to check the health of an external resource that the instance relies on, such as a database server.</p> </li> <li> <p>You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the state of the alarm. For example, you might create a CloudWatch metric that checks the status of the Amazon EC2 <code>StatusCheckFailed</code> metric, add an alarm to the metric, and then create a health check that is based on the state of the alarm. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html">Amazon CloudWatch User Guide</a>.</p> </li> </ul>

        Args:
            caller_reference: <p>A unique string that identifies the request and that allows you to retry a failed <code>CreateHealthCheck</code> request without the risk of creating two identical health checks:</p> <ul> <li> <p>If you send a <code>CreateHealthCheck</code> request with the same <code>CallerReference</code> and settings as a previous request, and if the health check doesn't exist, Amazon Route 53 creates the health check. If the health check does exist, Route 53 returns the health check configuration in the response. </p> </li> <li> <p>If you send a <code>CreateHealthCheck</code> request with the same <code>CallerReference</code> as a deleted health check, regardless of the settings, Route 53 returns a <code>HealthCheckAlreadyExists</code> error.</p> </li> <li> <p>If you send a <code>CreateHealthCheck</code> request with the same <code>CallerReference</code> as an existing health check but with different settings, Route 53 returns a <code>HealthCheckAlreadyExists</code> error.</p> </li> <li> <p>If you send a <code>CreateHealthCheck</code> request with a unique <code>CallerReference</code> but settings identical to an existing health check, Route 53 creates the health check.</p> </li> </ul> <p> Route 53 does not store the <code>CallerReference</code> for a deleted health check indefinitely. The <code>CallerReference</code> for a deleted health check will be deleted after a number of days.</p>
            health_check_config: <p>A complex type that contains settings for a new health check.</p>

        Raises:
            capo_route_53.errors.health_check_already_exists.HealthCheckAlreadyExists: <p> The health check you're attempting to create already exists. Amazon Route 53 returns this error when you submit a request that has the following values:</p> <ul> <li> <p>The same value for <code>CallerReference</code> as an existing health check, and one or more values that differ from the existing health check that has the same caller reference.</p> </li> <li> <p>The same value for <code>CallerReference</code> as a health check that you created and later deleted, regardless of the other settings in the request.</p> </li> </ul>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.too_many_health_checks.TooManyHealthChecks: <p>This health check can't be created because the current account has reached the limit on the number of active health checks.</p> <p>For information about default limits, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>For information about how to get the current limit for an account, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html">GetAccountLimit</a>. To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p> <p>You have reached the maximum number of active health checks for an Amazon Web Services account. To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_health_check_request.CreateHealthCheckRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_health_check_response.CreateHealthCheckResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_health_check

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_health_check.create_health_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_health_check_request.CreateHealthCheckRequest = {
            "caller_reference": caller_reference,
            "health_check_config": health_check_config,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_hosted_zone(
        self,
        name: "capo_route_53.types.dns_name.DNSName",
        caller_reference: "capo_route_53.types.nonce.Nonce",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        vpc: Optional["capo_route_53.types.vpc.VPC"] = None,
        hosted_zone_config: Optional[
            "capo_route_53.types.hosted_zone_config.HostedZoneConfig"
        ] = None,
        delegation_set_id: Optional[
            "capo_route_53.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_route_53.types.create_hosted_zone_response.CreateHostedZoneResponse":
        """<p>Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs). </p> <important> <p>You can't convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.</p> </important> <p>For more information about charges for hosted zones, see <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p> <p>Note the following:</p> <ul> <li> <p>You can't create a hosted zone for a top-level domain (TLD) such as .com.</p> </li> <li> <p>For public hosted zones, Route 53 automatically creates a default SOA record and four NS records for the zone. For more information about SOA and NS records, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/SOA-NSrecords.html">NS and SOA Records that Route 53 Creates for a Hosted Zone</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>If you want to use the same name servers for multiple public hosted zones, you can optionally associate a reusable delegation set with the hosted zone. See the <code>DelegationSetId</code> element.</p> </li> <li> <p>If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html">Migrating DNS Service for an Existing Domain to Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>. </p> </li> </ul> <p>When you submit a <code>CreateHostedZone</code> request, the initial status of the hosted zone is <code>PENDING</code>. For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to <code>INSYNC</code>.</p> <p>The <code>CreateHostedZone</code> request requires the caller to have an <code>ec2:DescribeVpcs</code> permission.</p> <note> <p>When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.</p> <p>The following are the supported partitions:</p> <ul> <li> <p> <code>aws</code> - Amazon Web Services Regions</p> </li> <li> <p> <code>aws-cn</code> - China Regions</p> </li> <li> <p> <code>aws-us-gov</code> - Amazon Web Services GovCloud (US) Region</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Access Management</a> in the <i>Amazon Web Services General Reference</i>.</p> </note>

        Args:
            name: <p>The name of the domain. Specify a fully qualified domain name, for example, <i>www.example.com</i>. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats <i>www.example.com</i> (without a trailing dot) and <i>www.example.com.</i> (with a trailing dot) as identical.</p> <p>If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of <code>NameServers</code> that <code>CreateHostedZone</code> returns in <code>DelegationSet</code>.</p>
            vpc: <p>(Private hosted zones only) A complex type that contains information about the Amazon VPC that you're associating with this hosted zone.</p> <p>You can specify only one Amazon VPC when you create a private hosted zone. If you are associating a VPC with a hosted zone with this request, the paramaters <code>VPCId</code> and <code>VPCRegion</code> are also required.</p> <p>To associate additional Amazon VPCs with the hosted zone, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html">AssociateVPCWithHostedZone</a> after you create a hosted zone.</p>
            caller_reference: <p>A unique string that identifies the request and that allows failed <code>CreateHostedZone</code> requests to be retried without the risk of executing the operation twice. You must use a unique <code>CallerReference</code> string every time you submit a <code>CreateHostedZone</code> request. <code>CallerReference</code> can be any unique string, for example, a date/time stamp.</p>
            hosted_zone_config: <p>(Optional) A complex type that contains the following optional values:</p> <ul> <li> <p>For public and private hosted zones, an optional comment</p> </li> <li> <p>For private hosted zones, an optional <code>PrivateZone</code> element</p> </li> </ul> <p>If you don't specify a comment or the <code>PrivateZone</code> element, omit <code>HostedZoneConfig</code> and the other elements.</p>
            delegation_set_id: <p>If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html">CreateReusableDelegationSet</a>.</p> <p>If you are using a reusable delegation set to create a public hosted zone for a subdomain, make sure that the parent hosted zone doesn't use one or more of the same name servers. If you have overlapping nameservers, the operation will cause a <code>ConflictingDomainsExist</code> error.</p>

        Raises:
            capo_route_53.errors.conflicting_domain_exists.ConflictingDomainExists: <p>The cause of this error depends on the operation that you're performing:</p> <ul> <li> <p> <b>Create a public hosted zone:</b> Two hosted zones that have the same name or that have a parent/child relationship (example.com and test.example.com) can't have any common name servers. You tried to create a hosted zone that has the same name as an existing hosted zone or that's the parent or child of an existing hosted zone, and you specified a delegation set that shares one or more name servers with the existing hosted zone. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html">CreateReusableDelegationSet</a>.</p> </li> <li> <p> <b>Create a private hosted zone:</b> A hosted zone with the specified name already exists and is already associated with the Amazon VPC that you specified.</p> </li> <li> <p> <b>Associate VPCs with a private hosted zone:</b> The VPC that you specified is already associated with another hosted zone that has the same name.</p> </li> </ul>
            capo_route_53.errors.delegation_set_not_available.DelegationSetNotAvailable: <p>You can create a hosted zone that has the same name as an existing hosted zone (example.com is common), but there is a limit to the number of hosted zones that have the same name. If you get this error, Amazon Route 53 has reached that limit. If you own the domain name and Route 53 generates this error, contact Customer Support.</p>
            capo_route_53.errors.delegation_set_not_reusable.DelegationSetNotReusable: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.hosted_zone_already_exists.HostedZoneAlreadyExists: <p>The hosted zone you're trying to create already exists. Amazon Route 53 returns this error when a hosted zone has already been created with the specified <code>CallerReference</code>.</p>
            capo_route_53.errors.invalid_domain_name.InvalidDomainName: <p>The specified domain name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_vpc_id.InvalidVPCId: <p>The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.</p>
            capo_route_53.errors.no_such_delegation_set.NoSuchDelegationSet: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.too_many_hosted_zones.TooManyHostedZones: <p>This operation can't be completed either because the current account has reached the limit on the number of hosted zones or because you've reached the limit on the number of hosted zones that can be associated with a reusable delegation set.</p> <p>For information about default limits, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>To get the current limit on hosted zones that can be created by an account, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html">GetAccountLimit</a>.</p> <p>To get the current limit on hosted zones that can be associated with a reusable delegation set, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSetLimit.html">GetReusableDelegationSetLimit</a>.</p> <p>To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_hosted_zone_request.CreateHostedZoneRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_hosted_zone_response.CreateHostedZoneResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_hosted_zone

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_hosted_zone.create_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_hosted_zone_request.CreateHostedZoneRequest = {
            "name": name,
            "caller_reference": caller_reference,
        }
        if vpc is not None:
            input_["vpc"] = vpc
        if hosted_zone_config is not None:
            input_["hosted_zone_config"] = hosted_zone_config
        if delegation_set_id is not None:
            input_["delegation_set_id"] = delegation_set_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_key_signing_key(
        self,
        caller_reference: "capo_route_53.types.nonce.Nonce",
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        key_management_service_arn: "capo_route_53.types.signing_key_string.SigningKeyString",
        name: "capo_route_53.types.signing_key_name.SigningKeyName",
        status: "capo_route_53.types.signing_key_status.SigningKeyStatus",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.create_key_signing_key_response.CreateKeySigningKeyResponse":
        """<p>Creates a new key-signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.</p>

        Args:
            caller_reference: <p>A unique string that identifies the request.</p>
            hosted_zone_id: <p>The unique string (ID) used to identify a hosted zone.</p>
            key_management_service_arn: <p>The Amazon resource name (ARN) for a customer managed key in Key Management Service (KMS). The <code>KeyManagementServiceArn</code> must be unique for each key-signing key (KSK) in a single hosted zone. To see an example of <code>KeyManagementServiceArn</code> that grants the correct permissions for DNSSEC, scroll down to <b>Example</b>. </p> <p>You must configure the customer managed customer managed key as follows:</p> <dl> <dt>Status</dt> <dd> <p>Enabled</p> </dd> <dt>Key spec</dt> <dd> <p>ECC_NIST_P256</p> </dd> <dt>Key usage</dt> <dd> <p>Sign and verify</p> </dd> <dt>Key policy</dt> <dd> <p>The key policy must give permission for the following actions:</p> <ul> <li> <p>DescribeKey</p> </li> <li> <p>GetPublicKey</p> </li> <li> <p>Sign</p> </li> </ul> <p>The key policy must also include the Amazon Route 53 service in the principal for your account. Specify the following:</p> <ul> <li> <p> <code>"Service": "dnssec-route53.amazonaws.com"</code> </p> </li> </ul> </dd> </dl> <p>For more information about working with a customer managed key in KMS, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html">Key Management Service concepts</a>.</p>
            name: <p>A string used to identify a key-signing key (KSK). <code>Name</code> can include numbers, letters, and underscores (_). <code>Name</code> must be unique for each key-signing key in the same hosted zone.</p>
            status: <p>A string specifying the initial status of the key-signing key (KSK). You can set the value to <code>ACTIVE</code> or <code>INACTIVE</code>.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_argument.InvalidArgument: <p>Parameter name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_key_signing_key_name.InvalidKeySigningKeyName: <p>The key-signing key (KSK) name that you specified isn't a valid name.</p>
            capo_route_53.errors.invalid_key_signing_key_status.InvalidKeySigningKeyStatus: <p>The key-signing key (KSK) status isn't valid or another KSK has the status <code>INTERNAL_FAILURE</code>.</p>
            capo_route_53.errors.invalid_kms_arn.InvalidKMSArn: <p>The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC signing.</p>
            capo_route_53.errors.invalid_signing_status.InvalidSigningStatus: <p>Your hosted zone status isn't valid for this operation. In the hosted zone, change the status to enable <code>DNSSEC</code> or disable <code>DNSSEC</code>.</p>
            capo_route_53.errors.key_signing_key_already_exists.KeySigningKeyAlreadyExists: <p>You've already created a key-signing key (KSK) with this name or with the same customer managed key ARN.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.too_many_key_signing_keys.TooManyKeySigningKeys: <p>You've reached the limit for the number of key-signing keys (KSKs). Remove at least one KSK, and then try again.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_key_signing_key_request.CreateKeySigningKeyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_key_signing_key_response.CreateKeySigningKeyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_key_signing_key

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_key_signing_key.create_key_signing_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_key_signing_key_request.CreateKeySigningKeyRequest = {
            "caller_reference": caller_reference,
            "hosted_zone_id": hosted_zone_id,
            "key_management_service_arn": key_management_service_arn,
            "name": name,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_query_logging_config(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        cloud_watch_logs_log_group_arn: "capo_route_53.types.cloud_watch_logs_log_group_arn.CloudWatchLogsLogGroupArn",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.create_query_logging_config_response.CreateQueryLoggingConfigResponse":
        """<p>Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.</p> <p>DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following:</p> <ul> <li> <p>Route 53 edge location that responded to the DNS query</p> </li> <li> <p>Domain or subdomain that was requested</p> </li> <li> <p>DNS record type, such as A or AAAA</p> </li> <li> <p>DNS response code, such as <code>NoError</code> or <code>ServFail</code> </p> </li> </ul> <dl> <dt>Log Group and Resource Policy</dt> <dd> <p>Before you create a query logging configuration, perform the following operations.</p> <note> <p>If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically.</p> </note> <ol> <li> <p>Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following:</p> <ul> <li> <p>You must create the log group in the us-east-1 region.</p> </li> <li> <p>You must use the same Amazon Web Services account to create the log group and the hosted zone that you want to configure query logging for.</p> </li> <li> <p>When you create log groups for query logging, we recommend that you use a consistent prefix, for example:</p> <p> <code>/aws/route53/<i>hosted zone name</i> </code> </p> <p>In the next step, you'll create a resource policy, which controls access to one or more log groups and the associated Amazon Web Services resources, such as Route 53 hosted zones. There's a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging.</p> </li> </ul> </li> <li> <p>Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. You must create the CloudWatch Logs resource policy in the us-east-1 region. For the value of <code>Resource</code>, specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with <code>*</code>, for example:</p> <p> <code>arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*</code> </p> <p>To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values:</p> <ul> <li> <p>For <code>aws:SourceArn</code>, supply the hosted zone ARN used in creating the query logging configuration. For example, <code>aws:SourceArn: arn:aws:route53:::hostedzone/hosted zone ID</code>.</p> </li> <li> <p>For <code>aws:SourceAccount</code>, supply the account ID for the account that creates the query logging configuration. For example, <code>aws:SourceAccount:111111111111</code>.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html">The confused deputy problem</a> in the <i>Amazon Web Services IAM User Guide</i>.</p> <note> <p>You can't use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the Amazon Web Services SDKs, or the CLI.</p> </note> </li> </ol> </dd> <dt>Log Streams and Edge Locations</dt> <dd> <p>When Route 53 finishes creating the configuration for DNS query logging, it does the following:</p> <ul> <li> <p>Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location.</p> </li> <li> <p>Begins to send query logs to the applicable log stream.</p> </li> </ul> <p>The name of each log stream is in the following format:</p> <p> <code> <i>hosted zone ID</i>/<i>edge location code</i> </code> </p> <p>The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Route 53 Global Network" on the <a href="http://aws.amazon.com/route53/details/">Route 53 Product Details</a> page.</p> </dd> <dt>Queries That Are Logged</dt> <dd> <p>Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn't forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html">Routing Internet Traffic to Your Website or Web Application</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </dd> <dt>Log File Format</dt> <dd> <p>For a list of the values in each query log and the format of each value, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html">Logging DNS Queries</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </dd> <dt>Pricing</dt> <dd> <p>For information about charges for query logs, see <a href="http://aws.amazon.com/cloudwatch/pricing/">Amazon CloudWatch Pricing</a>.</p> </dd> <dt>How to Stop Logging</dt> <dd> <p>If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html">DeleteQueryLoggingConfig</a>.</p> </dd> </dl>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone that you want to log queries for. You can log queries only for public hosted zones.</p>
            cloud_watch_logs_log_group_arn: <p>The Amazon Resource Name (ARN) for the log group that you want to Amazon Route 53 to send query logs to. This is the format of the ARN:</p> <p>arn:aws:logs:<i>region</i>:<i>account-id</i>:log-group:<i>log_group_name</i> </p> <p>To get the ARN for a log group, you can use the CloudWatch console, the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html">DescribeLogGroups</a> API action, the <a href="https://docs.aws.amazon.com/cli/latest/reference/logs/describe-log-groups.html">describe-log-groups</a> command, or the applicable command in one of the Amazon Web Services SDKs.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.insufficient_cloud_watch_logs_resource_policy.InsufficientCloudWatchLogsResourcePolicy: <p>Amazon Route 53 doesn't have the permissions required to create log streams and send query logs to log streams. Possible causes include the following:</p> <ul> <li> <p>There is no resource policy that specifies the log group ARN in the value for <code>Resource</code>.</p> </li> <li> <p>The resource policy that includes the log group ARN in the value for <code>Resource</code> doesn't have the necessary permissions.</p> </li> <li> <p>The resource policy hasn't finished propagating yet.</p> </li> <li> <p>The Key management service (KMS) key you specified doesn’t exist or it can’t be used with the log group associated with query log. Update or provide a resource policy to grant permissions for the KMS key.</p> </li> <li> <p>The Key management service (KMS) key you specified is marked as disabled for the log group associated with query log. Update or provide a resource policy to grant permissions for the KMS key.</p> </li> </ul>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_cloud_watch_logs_log_group.NoSuchCloudWatchLogsLogGroup: <p>There is no CloudWatch Logs log group with the specified ARN.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.query_logging_config_already_exists.QueryLoggingConfigAlreadyExists: <p>You can create only one query logging configuration for a hosted zone, and a query logging configuration already exists for this hosted zone.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_query_logging_config_request.CreateQueryLoggingConfigRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_query_logging_config_response.CreateQueryLoggingConfigResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_query_logging_config

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_query_logging_config.create_query_logging_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_query_logging_config_request.CreateQueryLoggingConfigRequest = {
            "hosted_zone_id": hosted_zone_id,
            "cloud_watch_logs_log_group_arn": cloud_watch_logs_log_group_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_reusable_delegation_set(
        self,
        caller_reference: "capo_route_53.types.nonce.Nonce",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        hosted_zone_id: Optional["capo_route_53.types.resource_id.ResourceId"] = None,
    ) -> "capo_route_53.types.create_reusable_delegation_set_response.CreateReusableDelegationSetResponse":
        """<p>Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones that were created by the same Amazon Web Services account. </p> <p>You can also create a reusable delegation set that uses the four name servers that are associated with an existing hosted zone. Specify the hosted zone ID in the <code>CreateReusableDelegationSet</code> request.</p> <note> <p>You can't associate a reusable delegation set with a private hosted zone.</p> </note> <p>For information about using a reusable delegation set to configure white label name servers, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-name-servers.html">Configuring White Label Name Servers</a>.</p> <p>The process for migrating existing hosted zones to use a reusable delegation set is comparable to the process for configuring white label name servers. You need to perform the following steps:</p> <ol> <li> <p>Create a reusable delegation set.</p> </li> <li> <p>Recreate hosted zones, and reduce the TTL to 60 seconds or less.</p> </li> <li> <p>Recreate resource record sets in the new hosted zones.</p> </li> <li> <p>Change the registrar's name servers to use the name servers for the new hosted zones.</p> </li> <li> <p>Monitor traffic for the website or application.</p> </li> <li> <p>Change TTLs back to their original values.</p> </li> </ol> <p>If you want to migrate existing hosted zones to use a reusable delegation set, the existing hosted zones can't use any of the name servers that are assigned to the reusable delegation set. If one or more hosted zones do use one or more name servers that are assigned to the reusable delegation set, you can do one of the following:</p> <ul> <li> <p>For small numbers of hosted zones—up to a few hundred—it's relatively easy to create reusable delegation sets until you get one that has four name servers that don't overlap with any of the name servers in your hosted zones.</p> </li> <li> <p>For larger numbers of hosted zones, the easiest solution is to use more than one reusable delegation set.</p> </li> <li> <p>For larger numbers of hosted zones, you can also migrate hosted zones that have overlapping name servers to hosted zones that don't have overlapping name servers, then migrate the hosted zones again to use the reusable delegation set.</p> </li> </ul>

        Args:
            caller_reference: <p>A unique string that identifies the request, and that allows you to retry failed <code>CreateReusableDelegationSet</code> requests without the risk of executing the operation twice. You must use a unique <code>CallerReference</code> string every time you submit a <code>CreateReusableDelegationSet</code> request. <code>CallerReference</code> can be any unique string, for example a date/time stamp.</p>
            hosted_zone_id: <p>If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone.</p>

        Raises:
            capo_route_53.errors.delegation_set_already_created.DelegationSetAlreadyCreated: <p>A delegation set with the same owner and caller reference combination has already been created.</p>
            capo_route_53.errors.delegation_set_already_reusable.DelegationSetAlreadyReusable: <p>The specified delegation set has already been marked as reusable.</p>
            capo_route_53.errors.delegation_set_not_available.DelegationSetNotAvailable: <p>You can create a hosted zone that has the same name as an existing hosted zone (example.com is common), but there is a limit to the number of hosted zones that have the same name. If you get this error, Amazon Route 53 has reached that limit. If you own the domain name and Route 53 generates this error, contact Customer Support.</p>
            capo_route_53.errors.hosted_zone_not_found.HostedZoneNotFound: <p>The specified HostedZone can't be found.</p>
            capo_route_53.errors.invalid_argument.InvalidArgument: <p>Parameter name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.limits_exceeded.LimitsExceeded: <p>This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_reusable_delegation_set_request.CreateReusableDelegationSetRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_reusable_delegation_set_response.CreateReusableDelegationSetResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_reusable_delegation_set

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_reusable_delegation_set.create_reusable_delegation_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_reusable_delegation_set_request.CreateReusableDelegationSetRequest = {
            "caller_reference": caller_reference
        }
        if hosted_zone_id is not None:
            input_["hosted_zone_id"] = hosted_zone_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_traffic_policy(
        self,
        name: "capo_route_53.types.traffic_policy_name.TrafficPolicyName",
        document: "capo_route_53.types.traffic_policy_document.TrafficPolicyDocument",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        comment: Optional[
            "capo_route_53.types.traffic_policy_comment.TrafficPolicyComment"
        ] = None,
    ) -> (
        "capo_route_53.types.create_traffic_policy_response.CreateTrafficPolicyResponse"
    ):
        """<p>Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).</p>

        Args:
            name: <p>The name of the traffic policy.</p>
            document: <p>The definition of this traffic policy in JSON format. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html">Traffic Policy Document Format</a>.</p>
            comment: <p>(Optional) Any comments that you want to include about the traffic policy.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_traffic_policy_document.InvalidTrafficPolicyDocument: <p>The format of the traffic policy document that you specified in the <code>Document</code> element is not valid.</p>
            capo_route_53.errors.too_many_traffic_policies.TooManyTrafficPolicies: <p>This traffic policy can't be created because the current account has reached the limit on the number of traffic policies.</p> <p>For information about default limits, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>To get the current limit for an account, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html">GetAccountLimit</a>. </p> <p>To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.traffic_policy_already_exists.TrafficPolicyAlreadyExists: <p>A traffic policy that has the same value for <code>Name</code> already exists.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_traffic_policy_request.CreateTrafficPolicyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_traffic_policy_response.CreateTrafficPolicyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_traffic_policy

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_traffic_policy.create_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_traffic_policy_request.CreateTrafficPolicyRequest = {
            "name": name,
            "document": document,
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

    def create_traffic_policy_instance(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        name: "capo_route_53.types.dns_name.DNSName",
        ttl: "capo_route_53.types.ttl.TTL",
        traffic_policy_id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        traffic_policy_version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse":
        """<p>Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version. In addition, <code>CreateTrafficPolicyInstance</code> associates the resource record sets with a specified domain name (such as example.com) or subdomain name (such as www.example.com). Amazon Route 53 responds to DNS queries for the domain or subdomain name by using the resource record sets that <code>CreateTrafficPolicyInstance</code> created.</p> <note> <p>After you submit an <code>CreateTrafficPolicyInstance</code> request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. Use <code>GetTrafficPolicyInstance</code> with the <code>id</code> of new traffic policy instance to confirm that the <code>CreateTrafficPolicyInstance</code> request completed successfully. For more information, see the <code>State</code> response element.</p> </note>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone that you want Amazon Route 53 to create resource record sets in by using the configuration in a traffic policy.</p>
            name: <p>The domain name (such as example.com) or subdomain name (such as www.example.com) for which Amazon Route 53 responds to DNS queries by using the resource record sets that Route 53 creates for this traffic policy instance.</p>
            ttl: <p>(Optional) The TTL that you want Amazon Route 53 to assign to all of the resource record sets that it creates in the specified hosted zone.</p>
            traffic_policy_id: <p>The ID of the traffic policy that you want to use to create resource record sets in the specified hosted zone.</p>
            traffic_policy_version: <p>The version of the traffic policy that you want to use to create resource record sets in the specified hosted zone.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.too_many_traffic_policy_instances.TooManyTrafficPolicyInstances: <p>This traffic policy instance can't be created because the current account has reached the limit on the number of traffic policy instances.</p> <p>For information about default limits, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>For information about how to get the current limit for an account, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetAccountLimit.html">GetAccountLimit</a>.</p> <p>To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.traffic_policy_instance_already_exists.TrafficPolicyInstanceAlreadyExists: <p>There is already a traffic policy instance with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_traffic_policy_instance_request.CreateTrafficPolicyInstanceRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_traffic_policy_instance_response.CreateTrafficPolicyInstanceResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_traffic_policy_instance

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_traffic_policy_instance.create_traffic_policy_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_traffic_policy_instance_request.CreateTrafficPolicyInstanceRequest = {
            "hosted_zone_id": hosted_zone_id,
            "name": name,
            "ttl": ttl,
            "traffic_policy_id": traffic_policy_id,
            "traffic_policy_version": traffic_policy_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_traffic_policy_version(
        self,
        id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        document: "capo_route_53.types.traffic_policy_document.TrafficPolicyDocument",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        comment: Optional[
            "capo_route_53.types.traffic_policy_comment.TrafficPolicyComment"
        ] = None,
    ) -> "capo_route_53.types.create_traffic_policy_version_response.CreateTrafficPolicyVersionResponse":
        """<p>Creates a new version of an existing traffic policy. When you create a new version of a traffic policy, you specify the ID of the traffic policy that you want to update and a JSON-formatted document that describes the new version. You use traffic policies to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com). You can create a maximum of 1000 versions of a traffic policy. If you reach the limit and need to create another version, you'll need to start a new traffic policy.</p>

        Args:
            id: <p>The ID of the traffic policy for which you want to create a new version.</p>
            document: <p>The definition of this version of the traffic policy, in JSON format. You specified the JSON in the <code>CreateTrafficPolicyVersion</code> request. For more information about the JSON format, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html">CreateTrafficPolicy</a>.</p>
            comment: <p>The comment that you specified in the <code>CreateTrafficPolicyVersion</code> request, if any.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_traffic_policy_document.InvalidTrafficPolicyDocument: <p>The format of the traffic policy document that you specified in the <code>Document</code> element is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.too_many_traffic_policy_versions_for_current_policy.TooManyTrafficPolicyVersionsForCurrentPolicy: <p>This traffic policy version can't be created because you've reached the limit of 1000 on the number of versions that you can create for the current traffic policy.</p> <p>To create more traffic policy versions, you can use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html">GetTrafficPolicy</a> to get the traffic policy document for a specified traffic policy version, and then use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html">CreateTrafficPolicy</a> to create a new traffic policy using the traffic policy document.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_traffic_policy_version_request.CreateTrafficPolicyVersionRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_traffic_policy_version_response.CreateTrafficPolicyVersionResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_traffic_policy_version

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_traffic_policy_version.create_traffic_policy_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_traffic_policy_version_request.CreateTrafficPolicyVersionRequest = {
            "id": id,
            "document": document,
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

    def create_vpc_association_authorization(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        vpc: "capo_route_53.types.vpc.VPC",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.create_vpc_association_authorization_response.CreateVPCAssociationAuthorizationResponse":
        """<p>Authorizes the Amazon Web Services account that created a specified VPC to submit an <code>AssociateVPCWithHostedZone</code> request to associate the VPC with a specified hosted zone that was created by a different account. To submit a <code>CreateVPCAssociationAuthorization</code> request, you must use the account that created the hosted zone. After you authorize the association, use the account that created the VPC to submit an <code>AssociateVPCWithHostedZone</code> request.</p> <note> <p>If you want to associate multiple VPCs that you created by using one account with a hosted zone that you created by using a different account, you must submit one authorization request for each VPC.</p> </note>

        Args:
            hosted_zone_id: <p>The ID of the private hosted zone that you want to authorize associating a VPC with.</p>
            vpc: <p>A complex type that contains the VPC ID and region for the VPC that you want to authorize associating with your hosted zone.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_vpc_id.InvalidVPCId: <p>The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.too_many_vpc_association_authorizations.TooManyVPCAssociationAuthorizations: <p>You've created the maximum number of authorizations that can be created for the specified hosted zone. To authorize another VPC to be associated with the hosted zone, submit a <code>DeleteVPCAssociationAuthorization</code> request to remove an existing authorization. To get a list of existing authorizations, submit a <code>ListVPCAssociationAuthorizations</code> request.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.create_vpc_association_authorization_request.CreateVPCAssociationAuthorizationRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.create_vpc_association_authorization_response.CreateVPCAssociationAuthorizationResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.create_vpc_association_authorization

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.create_vpc_association_authorization.create_vpc_association_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.create_vpc_association_authorization_request.CreateVPCAssociationAuthorizationRequest = {
            "hosted_zone_id": hosted_zone_id,
            "vpc": vpc,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deactivate_key_signing_key(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        name: "capo_route_53.types.signing_key_name.SigningKeyName",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.deactivate_key_signing_key_response.DeactivateKeySigningKeyResponse":
        """<p>Deactivates a key-signing key (KSK) so that it will not be used for signing by DNSSEC. This operation changes the KSK status to <code>INACTIVE</code>.</p>

        Args:
            hosted_zone_id: <p>A unique string used to identify a hosted zone.</p>
            name: <p>A string used to identify a key-signing key (KSK).</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_key_signing_key_status.InvalidKeySigningKeyStatus: <p>The key-signing key (KSK) status isn't valid or another KSK has the status <code>INTERNAL_FAILURE</code>.</p>
            capo_route_53.errors.invalid_signing_status.InvalidSigningStatus: <p>Your hosted zone status isn't valid for this operation. In the hosted zone, change the status to enable <code>DNSSEC</code> or disable <code>DNSSEC</code>.</p>
            capo_route_53.errors.key_signing_key_in_parent_ds_record.KeySigningKeyInParentDSRecord: <p>The key-signing key (KSK) is specified in a parent DS record.</p>
            capo_route_53.errors.key_signing_key_in_use.KeySigningKeyInUse: <p>The key-signing key (KSK) that you specified can't be deactivated because it's the only KSK for a currently-enabled DNSSEC. Disable DNSSEC signing, or add or enable another KSK.</p>
            capo_route_53.errors.no_such_key_signing_key.NoSuchKeySigningKey: <p>The specified key-signing key (KSK) doesn't exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.deactivate_key_signing_key_request.DeactivateKeySigningKeyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.deactivate_key_signing_key_response.DeactivateKeySigningKeyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.deactivate_key_signing_key

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.deactivate_key_signing_key.deactivate_key_signing_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.deactivate_key_signing_key_request.DeactivateKeySigningKeyRequest = {
            "hosted_zone_id": hosted_zone_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cidr_collection(
        self,
        id: "capo_route_53.types.uuid.UUID",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_cidr_collection_response.DeleteCidrCollectionResponse":
        """<p>Deletes a CIDR collection in the current Amazon Web Services account. The collection must be empty before it can be deleted.</p>

        Args:
            id: <p>The UUID of the collection to delete.</p>

        Raises:
            capo_route_53.errors.cidr_collection_in_use_exception.CidrCollectionInUseException: <p>This CIDR collection is in use, and isn't empty.</p>
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_cidr_collection_exception.NoSuchCidrCollectionException: <p>The CIDR collection you specified, doesn't exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_cidr_collection_request.DeleteCidrCollectionRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_cidr_collection_response.DeleteCidrCollectionResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_cidr_collection

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_cidr_collection.delete_cidr_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_cidr_collection_request.DeleteCidrCollectionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_health_check(
        self,
        health_check_id: "capo_route_53.types.health_check_id.HealthCheckId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_health_check_response.DeleteHealthCheckResponse":
        """<p>Deletes a health check.</p> <important> <p>Amazon Route 53 does not prevent you from deleting a health check even if the health check is associated with one or more resource record sets. If you delete a health check and you don't update the associated resource record sets, the future status of the health check can't be predicted and may change. This will affect the routing of DNS queries for your DNS failover configuration. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html#health-checks-deleting.html">Replacing and Deleting Health Checks</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </important> <p>If you're using Cloud Map and you configured Cloud Map to create a Route 53 health check when you register an instance, you can't use the Route 53 <code>DeleteHealthCheck</code> command to delete the health check. The health check is deleted automatically when you deregister the instance; there can be a delay of several hours before the health check is deleted from Route 53. </p>

        Args:
            health_check_id: <p>The ID of the health check that you want to delete.</p>

        Raises:
            capo_route_53.errors.health_check_in_use.HealthCheckInUse: <p>This error code is not in use.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_health_check_request.DeleteHealthCheckRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_health_check_response.DeleteHealthCheckResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_health_check

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_health_check.delete_health_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_health_check_request.DeleteHealthCheckRequest = {
            "health_check_id": health_check_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_hosted_zone(
        self,
        id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_hosted_zone_response.DeleteHostedZoneResponse":
        """<p>Deletes a hosted zone.</p> <p>If the hosted zone was created by another service, such as Cloud Map, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DeleteHostedZone.html#delete-public-hosted-zone-created-by-another-service">Deleting Public Hosted Zones That Were Created by Another Service</a> in the <i>Amazon Route 53 Developer Guide</i> for information about how to delete it. (The process is the same for public and private hosted zones that were created by another service.)</p> <p>If you want to keep your domain registration but you want to stop routing internet traffic to your website or web application, we recommend that you delete resource record sets in the hosted zone instead of deleting the hosted zone.</p> <important> <p>If you delete a hosted zone, you can't undelete it. You must create a new hosted zone and update the name servers for your domain registration, which can require up to 48 hours to take effect. (If you delegated responsibility for a subdomain to a hosted zone and you delete the child hosted zone, you must update the name servers in the parent hosted zone.) In addition, if you delete a hosted zone, someone could hijack the domain and route traffic to their own resources using your domain name.</p> </important> <p>If you want to avoid the monthly charge for the hosted zone, you can transfer DNS service for the domain to a free DNS service. When you transfer DNS service, you have to update the name servers for the domain registration. If the domain is registered with Route 53, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainNameservers.html">UpdateDomainNameservers</a> for information about how to replace Route 53 name servers with name servers for the new DNS service. If the domain is registered with another registrar, use the method provided by the registrar to update name servers for the domain registration. For more information, perform an internet search on "free DNS service."</p> <p>You can delete a hosted zone only if it contains only the default SOA and NS records and has DNSSEC signing disabled. If the hosted zone contains other records or has DNSSEC enabled, you must delete the records and disable DNSSEC before deletion. Attempting to delete a hosted zone with additional records or DNSSEC enabled returns a <code>HostedZoneNotEmpty</code> error. For information about deleting records, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html">ChangeResourceRecordSets</a>. </p> <p>To verify that the hosted zone has been deleted, do one of the following:</p> <ul> <li> <p>Use the <code>GetHostedZone</code> action to request information about the hosted zone.</p> </li> <li> <p>Use the <code>ListHostedZones</code> action to get a list of the hosted zones associated with the current Amazon Web Services account.</p> </li> </ul>

        Args:
            id: <p>The ID of the hosted zone you want to delete.</p>

        Raises:
            capo_route_53.errors.hosted_zone_not_empty.HostedZoneNotEmpty: <p>The hosted zone contains resource records that are not SOA or NS records.</p>
            capo_route_53.errors.invalid_domain_name.InvalidDomainName: <p>The specified domain name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_hosted_zone_request.DeleteHostedZoneRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_hosted_zone_response.DeleteHostedZoneResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_hosted_zone

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_hosted_zone.delete_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_hosted_zone_request.DeleteHostedZoneRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_key_signing_key(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        name: "capo_route_53.types.signing_key_name.SigningKeyName",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_key_signing_key_response.DeleteKeySigningKeyResponse":
        """<p>Deletes a key-signing key (KSK). Before you can delete a KSK, you must deactivate it. The KSK must be deactivated before you can delete it regardless of whether the hosted zone is enabled for DNSSEC signing.</p> <p>You can use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeactivateKeySigningKey.html">DeactivateKeySigningKey</a> to deactivate the key before you delete it.</p> <p>Use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetDNSSEC.html">GetDNSSEC</a> to verify that the KSK is in an <code>INACTIVE</code> status.</p>

        Args:
            hosted_zone_id: <p>A unique string used to identify a hosted zone.</p>
            name: <p>A string used to identify a key-signing key (KSK).</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_key_signing_key_status.InvalidKeySigningKeyStatus: <p>The key-signing key (KSK) status isn't valid or another KSK has the status <code>INTERNAL_FAILURE</code>.</p>
            capo_route_53.errors.invalid_kms_arn.InvalidKMSArn: <p>The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC signing.</p>
            capo_route_53.errors.invalid_signing_status.InvalidSigningStatus: <p>Your hosted zone status isn't valid for this operation. In the hosted zone, change the status to enable <code>DNSSEC</code> or disable <code>DNSSEC</code>.</p>
            capo_route_53.errors.no_such_key_signing_key.NoSuchKeySigningKey: <p>The specified key-signing key (KSK) doesn't exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_key_signing_key_request.DeleteKeySigningKeyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_key_signing_key_response.DeleteKeySigningKeyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_key_signing_key

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_key_signing_key.delete_key_signing_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_key_signing_key_request.DeleteKeySigningKeyRequest = {
            "hosted_zone_id": hosted_zone_id,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_query_logging_config(
        self,
        id: "capo_route_53.types.query_logging_config_id.QueryLoggingConfigId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_query_logging_config_response.DeleteQueryLoggingConfigResponse":
        """<p>Deletes a configuration for DNS query logging. If you delete a configuration, Amazon Route 53 stops sending query logs to CloudWatch Logs. Route 53 doesn't delete any logs that are already in CloudWatch Logs.</p> <p>For more information about DNS query logs, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html">CreateQueryLoggingConfig</a>.</p>

        Args:
            id: <p>The ID of the configuration that you want to delete. </p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_query_logging_config.NoSuchQueryLoggingConfig: <p>There is no DNS query logging configuration with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_query_logging_config_request.DeleteQueryLoggingConfigRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_query_logging_config_response.DeleteQueryLoggingConfigResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_query_logging_config

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_query_logging_config.delete_query_logging_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_query_logging_config_request.DeleteQueryLoggingConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_reusable_delegation_set(
        self,
        id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_reusable_delegation_set_response.DeleteReusableDelegationSetResponse":
        """<p>Deletes a reusable delegation set.</p> <important> <p>You can delete a reusable delegation set only if it isn't associated with any hosted zones.</p> </important> <p>To verify that the reusable delegation set is not associated with any hosted zones, submit a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSet.html">GetReusableDelegationSet</a> request and specify the ID of the reusable delegation set that you want to delete.</p>

        Args:
            id: <p>The ID of the reusable delegation set that you want to delete.</p>

        Raises:
            capo_route_53.errors.delegation_set_in_use.DelegationSetInUse: <p>The specified delegation contains associated hosted zones which must be deleted before the reusable delegation set can be deleted.</p>
            capo_route_53.errors.delegation_set_not_reusable.DelegationSetNotReusable: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_delegation_set.NoSuchDelegationSet: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_reusable_delegation_set_request.DeleteReusableDelegationSetRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_reusable_delegation_set_response.DeleteReusableDelegationSetResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_reusable_delegation_set

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_reusable_delegation_set.delete_reusable_delegation_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_reusable_delegation_set_request.DeleteReusableDelegationSetRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_traffic_policy(
        self,
        id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> (
        "capo_route_53.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse"
    ):
        """<p>Deletes a traffic policy.</p> <p>When you delete a traffic policy, Route 53 sets a flag on the policy to indicate that it has been deleted. However, Route 53 never fully deletes the traffic policy. Note the following:</p> <ul> <li> <p>Deleted traffic policies aren't listed if you run <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicies.html">ListTrafficPolicies</a>.</p> </li> <li> <p> There's no way to get a list of deleted policies.</p> </li> <li> <p>If you retain the ID of the policy, you can get information about the policy, including the traffic policy document, by running <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html">GetTrafficPolicy</a>.</p> </li> </ul>

        Args:
            id: <p>The ID of the traffic policy that you want to delete.</p>
            version: <p>The version number of the traffic policy that you want to delete.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.traffic_policy_in_use.TrafficPolicyInUse: <p>One or more traffic policy instances were created by using the specified traffic policy.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_traffic_policy

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_traffic_policy.delete_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest = {
            "id": id,
            "version": version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_traffic_policy_instance(
        self,
        id: "capo_route_53.types.traffic_policy_instance_id.TrafficPolicyInstanceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse":
        """<p>Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.</p> <note> <p>In the Route 53 console, traffic policy instances are known as policy records.</p> </note>

        Args:
            id: <p>The ID of the traffic policy instance that you want to delete. </p> <important> <p>When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.</p> </important>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance: <p>No traffic policy instance exists with the specified ID.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_traffic_policy_instance_request.DeleteTrafficPolicyInstanceRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_traffic_policy_instance_response.DeleteTrafficPolicyInstanceResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_traffic_policy_instance

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_traffic_policy_instance.delete_traffic_policy_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_traffic_policy_instance_request.DeleteTrafficPolicyInstanceRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_association_authorization(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        vpc: "capo_route_53.types.vpc.VPC",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.delete_vpc_association_authorization_response.DeleteVPCAssociationAuthorizationResponse":
        """<p>Removes authorization to submit an <code>AssociateVPCWithHostedZone</code> request to associate a specified VPC with a hosted zone that was created by a different account. You must use the account that created the hosted zone to submit a <code>DeleteVPCAssociationAuthorization</code> request.</p> <important> <p>Sending this request only prevents the Amazon Web Services account that created the VPC from associating the VPC with the Amazon Route 53 hosted zone in the future. If the VPC is already associated with the hosted zone, <code>DeleteVPCAssociationAuthorization</code> won't disassociate the VPC from the hosted zone. If you want to delete an existing association, use <code>DisassociateVPCFromHostedZone</code>.</p> </important>

        Args:
            hosted_zone_id: <p>When removing authorization to associate a VPC that was created by one Amazon Web Services account with a hosted zone that was created with a different Amazon Web Services account, the ID of the hosted zone.</p>
            vpc: <p>When removing authorization to associate a VPC that was created by one Amazon Web Services account with a hosted zone that was created with a different Amazon Web Services account, a complex type that includes the ID and region of the VPC.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_vpc_id.InvalidVPCId: <p>The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.vpc_association_authorization_not_found.VPCAssociationAuthorizationNotFound: <p>The VPC that you specified is not authorized to be associated with the hosted zone.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.delete_vpc_association_authorization_request.DeleteVPCAssociationAuthorizationRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.delete_vpc_association_authorization_response.DeleteVPCAssociationAuthorizationResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.delete_vpc_association_authorization

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.delete_vpc_association_authorization.delete_vpc_association_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.delete_vpc_association_authorization_request.DeleteVPCAssociationAuthorizationRequest = {
            "hosted_zone_id": hosted_zone_id,
            "vpc": vpc,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_hosted_zone_dnssec(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.disable_hosted_zone_dnssec_response.DisableHostedZoneDNSSECResponse":
        """<p>Disables DNSSEC signing in a specific hosted zone. This action does not deactivate any key-signing keys (KSKs) that are active in the hosted zone.</p>

        Args:
            hosted_zone_id: <p>A unique string used to identify a hosted zone.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.dnssec_not_found.DNSSECNotFound: <p>The hosted zone doesn't have any DNSSEC resources.</p>
            capo_route_53.errors.invalid_argument.InvalidArgument: <p>Parameter name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_key_signing_key_status.InvalidKeySigningKeyStatus: <p>The key-signing key (KSK) status isn't valid or another KSK has the status <code>INTERNAL_FAILURE</code>.</p>
            capo_route_53.errors.invalid_kms_arn.InvalidKMSArn: <p>The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC signing.</p>
            capo_route_53.errors.key_signing_key_in_parent_ds_record.KeySigningKeyInParentDSRecord: <p>The key-signing key (KSK) is specified in a parent DS record.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.disable_hosted_zone_dnssec_request.DisableHostedZoneDNSSECRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.disable_hosted_zone_dnssec_response.DisableHostedZoneDNSSECResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.disable_hosted_zone_dnssec

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.disable_hosted_zone_dnssec.disable_hosted_zone_dnssec(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.disable_hosted_zone_dnssec_request.DisableHostedZoneDNSSECRequest = {
            "hosted_zone_id": hosted_zone_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_vpc_from_hosted_zone(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        vpc: "capo_route_53.types.vpc.VPC",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        comment: Optional[
            "capo_route_53.types.disassociate_vpc_comment.DisassociateVPCComment"
        ] = None,
    ) -> "capo_route_53.types.disassociate_vpc_from_hosted_zone_response.DisassociateVPCFromHostedZoneResponse":
        """<p>Disassociates an Amazon Virtual Private Cloud (Amazon VPC) from an Amazon Route 53 private hosted zone. Note the following:</p> <ul> <li> <p>You can't disassociate the last Amazon VPC from a private hosted zone.</p> </li> <li> <p>You can't convert a private hosted zone into a public hosted zone.</p> </li> <li> <p>You can submit a <code>DisassociateVPCFromHostedZone</code> request using either the account that created the hosted zone or the account that created the Amazon VPC.</p> </li> <li> <p>Some services, such as Cloud Map and Amazon Elastic File System (Amazon EFS) automatically create hosted zones and associate VPCs with the hosted zones. A service can create a hosted zone using your account or using its own account. You can disassociate a VPC from a hosted zone only if the service created the hosted zone using your account.</p> <p>When you run <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html">DisassociateVPCFromHostedZone</a>, if the hosted zone has a value for <code>OwningAccount</code>, you can use <code>DisassociateVPCFromHostedZone</code>. If the hosted zone has a value for <code>OwningService</code>, you can't use <code>DisassociateVPCFromHostedZone</code>.</p> </li> </ul> <note> <p>When revoking access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.</p> <p>The following are the supported partitions:</p> <ul> <li> <p> <code>aws</code> - Amazon Web Services Regions</p> </li> <li> <p> <code>aws-cn</code> - China Regions</p> </li> <li> <p> <code>aws-us-gov</code> - Amazon Web Services GovCloud (US) Region</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Access Management</a> in the <i>Amazon Web Services General Reference</i>.</p> </note>

        Args:
            hosted_zone_id: <p>The ID of the private hosted zone that you want to disassociate a VPC from.</p>
            vpc: <p>A complex type that contains information about the VPC that you're disassociating from the specified hosted zone.</p>
            comment: <p> <i>Optional:</i> A comment about the disassociation request.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_vpc_id.InvalidVPCId: <p>The VPC ID that you specified either isn't a valid ID or the current account is not authorized to access this VPC.</p>
            capo_route_53.errors.last_vpc_association.LastVPCAssociation: <p>The VPC that you're trying to disassociate from the private hosted zone is the last VPC that is associated with the hosted zone. Amazon Route 53 doesn't support disassociating the last VPC from a hosted zone.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.vpc_association_not_found.VPCAssociationNotFound: <p>The specified VPC and hosted zone are not currently associated.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.disassociate_vpc_from_hosted_zone_request.DisassociateVPCFromHostedZoneRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.disassociate_vpc_from_hosted_zone_response.DisassociateVPCFromHostedZoneResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.disassociate_vpc_from_hosted_zone

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.disassociate_vpc_from_hosted_zone.disassociate_vpc_from_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.disassociate_vpc_from_hosted_zone_request.DisassociateVPCFromHostedZoneRequest = {
            "hosted_zone_id": hosted_zone_id,
            "vpc": vpc,
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

    def enable_hosted_zone_dnssec(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.enable_hosted_zone_dnssec_response.EnableHostedZoneDNSSECResponse":
        """<p>Enables DNSSEC signing in a specific hosted zone.</p>

        Args:
            hosted_zone_id: <p>A unique string used to identify a hosted zone.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.dnssec_not_found.DNSSECNotFound: <p>The hosted zone doesn't have any DNSSEC resources.</p>
            capo_route_53.errors.hosted_zone_partially_delegated.HostedZonePartiallyDelegated: <p>The hosted zone nameservers don't match the parent nameservers. The hosted zone and parent must have the same nameservers.</p>
            capo_route_53.errors.invalid_argument.InvalidArgument: <p>Parameter name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_key_signing_key_status.InvalidKeySigningKeyStatus: <p>The key-signing key (KSK) status isn't valid or another KSK has the status <code>INTERNAL_FAILURE</code>.</p>
            capo_route_53.errors.invalid_kms_arn.InvalidKMSArn: <p>The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC signing.</p>
            capo_route_53.errors.key_signing_key_with_active_status_not_found.KeySigningKeyWithActiveStatusNotFound: <p>A key-signing key (KSK) with <code>ACTIVE</code> status wasn't found.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.enable_hosted_zone_dnssec_request.EnableHostedZoneDNSSECRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.enable_hosted_zone_dnssec_response.EnableHostedZoneDNSSECResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.enable_hosted_zone_dnssec

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.enable_hosted_zone_dnssec.enable_hosted_zone_dnssec(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.enable_hosted_zone_dnssec_request.EnableHostedZoneDNSSECRequest = {
            "hosted_zone_id": hosted_zone_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_limit(
        self,
        type: "capo_route_53.types.account_limit_type.AccountLimitType",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_account_limit_response.GetAccountLimitResponse":
        """<p>Gets the specified limit for the current account, for example, the maximum number of health checks that you can create using the account.</p> <p>For the default limit, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>. To request a higher limit, <a href="https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53">open a case</a>.</p> <note> <p>You can also view account limits in Amazon Web Services Trusted Advisor. Sign in to the Amazon Web Services Management Console and open the Trusted Advisor console at <a href="https://console.aws.amazon.com/trustedadvisor">https://console.aws.amazon.com/trustedadvisor/</a>. Then choose <b>Service limits</b> in the navigation pane.</p> </note>

        Args:
            type: <p>The limit that you want to get. Valid values include the following:</p> <ul> <li> <p> <b>MAX_HEALTH_CHECKS_BY_OWNER</b>: The maximum number of health checks that you can create using the current account.</p> </li> <li> <p> <b>MAX_HOSTED_ZONES_BY_OWNER</b>: The maximum number of hosted zones that you can create using the current account.</p> </li> <li> <p> <b>MAX_REUSABLE_DELEGATION_SETS_BY_OWNER</b>: The maximum number of reusable delegation sets that you can create using the current account.</p> </li> <li> <p> <b>MAX_TRAFFIC_POLICIES_BY_OWNER</b>: The maximum number of traffic policies that you can create using the current account.</p> </li> <li> <p> <b>MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER</b>: The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)</p> </li> </ul>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_account_limit_request.GetAccountLimitRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_account_limit_response.GetAccountLimitResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_account_limit

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_account_limit.get_account_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_account_limit_request.GetAccountLimitRequest = {
            "type": type
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_change(
        self,
        id: "capo_route_53.types.change_id.ChangeId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_change_response.GetChangeResponse":
        """<p>Returns the current status of a change batch request. The status is one of the following values:</p> <ul> <li> <p> <code>PENDING</code> indicates that the changes in this request have not propagated to all Amazon Route 53 DNS servers managing the hosted zone. This is the initial status of all change batch requests.</p> </li> <li> <p> <code>INSYNC</code> indicates that the changes have propagated to all Route 53 DNS servers managing the hosted zone. </p> </li> </ul>

        Args:
            id: <p>The ID of the change batch request. The value that you specify here is the value that <code>ChangeResourceRecordSets</code> returned in the <code>Id</code> element when you submitted the request.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_change.NoSuchChange: <p>A change with the specified change ID does not exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_change_request.GetChangeRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_change_response.GetChangeResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_change

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_change.get_change(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_change_request.GetChangeRequest = {"id": id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_checker_ip_ranges(
        self, *, config_overrides: Optional[Route53ClientConfig] = None
    ) -> (
        "capo_route_53.types.get_checker_ip_ranges_response.GetCheckerIpRangesResponse"
    ):
        """<p>Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.</p> <important> <p> <code>GetCheckerIpRanges</code> still works, but we recommend that you download ip-ranges.json, which includes IP address ranges for all Amazon Web Services services. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-ip-addresses.html">IP Address Ranges of Amazon Route 53 Servers</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </important>

        Raises:
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_checker_ip_ranges_request.GetCheckerIpRangesRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_checker_ip_ranges_response.GetCheckerIpRangesResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_checker_ip_ranges

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_checker_ip_ranges.get_checker_ip_ranges(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_checker_ip_ranges_request.GetCheckerIpRangesRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dnssec(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_dnssec_response.GetDNSSECResponse":
        """<p>Returns information about DNSSEC for a specific hosted zone, including the key-signing keys (KSKs) in the hosted zone.</p>

        Args:
            hosted_zone_id: <p>A unique string used to identify a hosted zone.</p>

        Raises:
            capo_route_53.errors.invalid_argument.InvalidArgument: <p>Parameter name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_dnssec_request.GetDNSSECRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_dnssec_response.GetDNSSECResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_dnssec

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_dnssec.get_dnssec(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_dnssec_request.GetDNSSECRequest = {
            "hosted_zone_id": hosted_zone_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_geo_location(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        continent_code: Optional[
            "capo_route_53.types.geo_location_continent_code.GeoLocationContinentCode"
        ] = None,
        country_code: Optional[
            "capo_route_53.types.geo_location_country_code.GeoLocationCountryCode"
        ] = None,
        subdivision_code: Optional[
            "capo_route_53.types.geo_location_subdivision_code.GeoLocationSubdivisionCode"
        ] = None,
    ) -> "capo_route_53.types.get_geo_location_response.GetGeoLocationResponse":
        """<p>Gets information about whether a specified geographic location is supported for Amazon Route 53 geolocation resource record sets.</p> <p>Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.</p> <p>Use the following syntax to determine whether a continent is supported for geolocation:</p> <p> <code>GET /2013-04-01/geolocation?continentcode=<i>two-letter abbreviation for a continent</i> </code> </p> <p>Use the following syntax to determine whether a country is supported for geolocation:</p> <p> <code>GET /2013-04-01/geolocation?countrycode=<i>two-character country code</i> </code> </p> <p>Use the following syntax to determine whether a subdivision of a country is supported for geolocation:</p> <p> <code>GET /2013-04-01/geolocation?countrycode=<i>two-character country code</i>&subdivisioncode=<i>subdivision code</i> </code> </p>

        Args:
            continent_code: <p>For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Amazon Route 53 supports the following continent codes:</p> <ul> <li> <p> <b>AF</b>: Africa</p> </li> <li> <p> <b>AN</b>: Antarctica</p> </li> <li> <p> <b>AS</b>: Asia</p> </li> <li> <p> <b>EU</b>: Europe</p> </li> <li> <p> <b>OC</b>: Oceania</p> </li> <li> <p> <b>NA</b>: North America</p> </li> <li> <p> <b>SA</b>: South America</p> </li> </ul>
            country_code: <p>Amazon Route 53 uses the two-letter country codes that are specified in <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO standard 3166-1 alpha-2</a>.</p> <p>Route 53 also supports the country code <b>UA</b> for Ukraine.</p>
            subdivision_code: <p>The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see <a href="https://pe.usps.com/text/pub28/28apb.htm">Appendix B: Two–Letter State and Possession Abbreviations</a> on the United States Postal Service website. For a list of all supported subdivision codes, use the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html">ListGeoLocations</a> API.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_geo_location.NoSuchGeoLocation: <p>Amazon Route 53 doesn't support the specified geographic location. For a list of supported geolocation codes, see the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html">GeoLocation</a> data type.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_geo_location_request.GetGeoLocationRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_geo_location_response.GetGeoLocationResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_geo_location

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_geo_location.get_geo_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_geo_location_request.GetGeoLocationRequest = {}
        if continent_code is not None:
            input_["continent_code"] = continent_code
        if country_code is not None:
            input_["country_code"] = country_code
        if subdivision_code is not None:
            input_["subdivision_code"] = subdivision_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_health_check(
        self,
        health_check_id: "capo_route_53.types.health_check_id.HealthCheckId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_health_check_response.GetHealthCheckResponse":
        """<p>Gets information about a specified health check.</p>

        Args:
            health_check_id: <p>The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.</p>

        Raises:
            capo_route_53.errors.incompatible_version.IncompatibleVersion: <p>The resource you're trying to access is unsupported on this Amazon Route 53 endpoint.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_health_check_request.GetHealthCheckRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_health_check_response.GetHealthCheckResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_health_check

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_health_check.get_health_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_health_check_request.GetHealthCheckRequest = {
            "health_check_id": health_check_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_health_check_count(
        self, *, config_overrides: Optional[Route53ClientConfig] = None
    ) -> "capo_route_53.types.get_health_check_count_response.GetHealthCheckCountResponse":
        """<p>Retrieves the number of health checks that are associated with the current Amazon Web Services account.</p>

        Raises:
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_health_check_count_request.GetHealthCheckCountRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_health_check_count_response.GetHealthCheckCountResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_health_check_count

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_health_check_count.get_health_check_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_health_check_count_request.GetHealthCheckCountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_health_check_last_failure_reason(
        self,
        health_check_id: "capo_route_53.types.health_check_id.HealthCheckId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_health_check_last_failure_reason_response.GetHealthCheckLastFailureReasonResponse":
        """<p>Gets the reason that a specified health check failed most recently.</p>

        Args:
            health_check_id: <p>The ID for the health check for which you want the last failure reason. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p> <note> <p>If you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use <code>GetHealthCheckLastFailureReason</code> for a calculated health check.</p> </note>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_health_check_last_failure_reason_request.GetHealthCheckLastFailureReasonRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_health_check_last_failure_reason_response.GetHealthCheckLastFailureReasonResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_health_check_last_failure_reason

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_health_check_last_failure_reason.get_health_check_last_failure_reason(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_health_check_last_failure_reason_request.GetHealthCheckLastFailureReasonRequest = {
            "health_check_id": health_check_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_health_check_status(
        self,
        health_check_id: "capo_route_53.types.health_check_id.HealthCheckId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_health_check_status_response.GetHealthCheckStatusResponse":
        """<p>Gets status of a specified health check. </p> <important> <p>This API is intended for use during development to diagnose behavior. It doesn’t support production use-cases with high query rates that require immediate and actionable responses.</p> </important>

        Args:
            health_check_id: <p>The ID for the health check that you want the current status for. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p> <note> <p>If you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can't use <code>GetHealthCheckStatus</code> to get the status of a calculated health check.</p> </note>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_health_check_status_request.GetHealthCheckStatusRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_health_check_status_response.GetHealthCheckStatusResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_health_check_status

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_health_check_status.get_health_check_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_health_check_status_request.GetHealthCheckStatusRequest = {
            "health_check_id": health_check_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hosted_zone(
        self,
        id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_hosted_zone_response.GetHostedZoneResponse":
        """<p>Gets information about a specified hosted zone including the four name servers assigned to the hosted zone.</p> <p> <code></code> returns the VPCs associated with the specified hosted zone and does not reflect the VPC associations by Route 53 Profiles. To get the associations to a Profile, call the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileAssociations.html">ListProfileAssociations</a> API.</p>

        Args:
            id: <p>The ID of the hosted zone that you want to get information about.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a hosted zone
            The following example gets information about the Z3M3LMPEXAMPLE hosted zone.

            >>> client.get_hosted_zone(id='Z3M3LMPEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_hosted_zone_request.GetHostedZoneRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_hosted_zone_response.GetHostedZoneResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_hosted_zone

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_hosted_zone.get_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_hosted_zone_request.GetHostedZoneRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hosted_zone_count(
        self, *, config_overrides: Optional[Route53ClientConfig] = None
    ) -> (
        "capo_route_53.types.get_hosted_zone_count_response.GetHostedZoneCountResponse"
    ):
        """<p>Retrieves the number of hosted zones that are associated with the current Amazon Web Services account.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_hosted_zone_count_request.GetHostedZoneCountRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_hosted_zone_count_response.GetHostedZoneCountResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_hosted_zone_count

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_hosted_zone_count.get_hosted_zone_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_hosted_zone_count_request.GetHostedZoneCountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hosted_zone_limit(
        self,
        type: "capo_route_53.types.hosted_zone_limit_type.HostedZoneLimitType",
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> (
        "capo_route_53.types.get_hosted_zone_limit_response.GetHostedZoneLimitResponse"
    ):
        """<p>Gets the specified limit for a specified hosted zone, for example, the maximum number of records that you can create in the hosted zone. </p> <p>For the default limit, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>. To request a higher limit, <a href="https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53">open a case</a>.</p>

        Args:
            type: <p>The limit that you want to get. Valid values include the following:</p> <ul> <li> <p> <b>MAX_RRSETS_BY_ZONE</b>: The maximum number of records that you can create in the specified hosted zone.</p> </li> <li> <p> <b>MAX_VPCS_ASSOCIATED_BY_ZONE</b>: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.</p> </li> </ul>
            hosted_zone_id: <p>The ID of the hosted zone that you want to get a limit for.</p>

        Raises:
            capo_route_53.errors.hosted_zone_not_private.HostedZoneNotPrivate: <p>The specified hosted zone is a public hosted zone, not a private hosted zone.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_hosted_zone_limit_request.GetHostedZoneLimitRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_hosted_zone_limit_response.GetHostedZoneLimitResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_hosted_zone_limit

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_hosted_zone_limit.get_hosted_zone_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_hosted_zone_limit_request.GetHostedZoneLimitRequest = {
            "type": type,
            "hosted_zone_id": hosted_zone_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_logging_config(
        self,
        id: "capo_route_53.types.query_logging_config_id.QueryLoggingConfigId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_query_logging_config_response.GetQueryLoggingConfigResponse":
        """<p>Gets information about a specified configuration for DNS query logging.</p> <p>For more information about DNS query logs, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html">CreateQueryLoggingConfig</a> and <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html">Logging DNS Queries</a>.</p>

        Args:
            id: <p>The ID of the configuration for DNS query logging that you want to get information about.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_query_logging_config.NoSuchQueryLoggingConfig: <p>There is no DNS query logging configuration with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_query_logging_config_request.GetQueryLoggingConfigRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_query_logging_config_response.GetQueryLoggingConfigResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_query_logging_config

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_query_logging_config.get_query_logging_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_query_logging_config_request.GetQueryLoggingConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_reusable_delegation_set(
        self,
        id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_reusable_delegation_set_response.GetReusableDelegationSetResponse":
        """<p>Retrieves information about a specified reusable delegation set, including the four name servers that are assigned to the delegation set.</p>

        Args:
            id: <p>The ID of the reusable delegation set that you want to get a list of name servers for.</p>

        Raises:
            capo_route_53.errors.delegation_set_not_reusable.DelegationSetNotReusable: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_delegation_set.NoSuchDelegationSet: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_reusable_delegation_set_request.GetReusableDelegationSetRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_reusable_delegation_set_response.GetReusableDelegationSetResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_reusable_delegation_set

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_reusable_delegation_set.get_reusable_delegation_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_reusable_delegation_set_request.GetReusableDelegationSetRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_reusable_delegation_set_limit(
        self,
        type: "capo_route_53.types.reusable_delegation_set_limit_type.ReusableDelegationSetLimitType",
        delegation_set_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_reusable_delegation_set_limit_response.GetReusableDelegationSetLimitResponse":
        """<p>Gets the maximum number of hosted zones that you can associate with the specified reusable delegation set.</p> <p>For the default limit, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html">Limits</a> in the <i>Amazon Route 53 Developer Guide</i>. To request a higher limit, <a href="https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-route53">open a case</a>.</p>

        Args:
            type: <p>Specify <code>MAX_ZONES_BY_REUSABLE_DELEGATION_SET</code> to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.</p>
            delegation_set_id: <p>The ID of the delegation set that you want to get the limit for.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_delegation_set.NoSuchDelegationSet: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_reusable_delegation_set_limit_request.GetReusableDelegationSetLimitRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_reusable_delegation_set_limit_response.GetReusableDelegationSetLimitResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_reusable_delegation_set_limit

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_reusable_delegation_set_limit.get_reusable_delegation_set_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_reusable_delegation_set_limit_request.GetReusableDelegationSetLimitRequest = {
            "type": type,
            "delegation_set_id": delegation_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_traffic_policy(
        self,
        id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_traffic_policy_response.GetTrafficPolicyResponse":
        """<p>Gets information about a specific traffic policy version.</p> <p>For information about how of deleting a traffic policy affects the response from <code>GetTrafficPolicy</code>, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html">DeleteTrafficPolicy</a>. </p>

        Args:
            id: <p>The ID of the traffic policy that you want to get information about.</p>
            version: <p>The version number of the traffic policy that you want to get information about.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_traffic_policy_request.GetTrafficPolicyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_traffic_policy_response.GetTrafficPolicyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_traffic_policy

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_traffic_policy.get_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_traffic_policy_request.GetTrafficPolicyRequest = {
            "id": id,
            "version": version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_traffic_policy_instance(
        self,
        id: "capo_route_53.types.traffic_policy_instance_id.TrafficPolicyInstanceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.get_traffic_policy_instance_response.GetTrafficPolicyInstanceResponse":
        """<p>Gets information about a specified traffic policy instance.</p> <note> <p> Use <code>GetTrafficPolicyInstance</code> with the <code>id</code> of new traffic policy instance to confirm that the <code>CreateTrafficPolicyInstance</code> or an <code>UpdateTrafficPolicyInstance</code> request completed successfully. For more information, see the <code>State</code> response element.</p> </note> <note> <p>In the Route 53 console, traffic policy instances are known as policy records.</p> </note>

        Args:
            id: <p>The ID of the traffic policy instance that you want to get information about.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance: <p>No traffic policy instance exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_traffic_policy_instance_request.GetTrafficPolicyInstanceRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_traffic_policy_instance_response.GetTrafficPolicyInstanceResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_traffic_policy_instance

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_traffic_policy_instance.get_traffic_policy_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_traffic_policy_instance_request.GetTrafficPolicyInstanceRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_traffic_policy_instance_count(
        self, *, config_overrides: Optional[Route53ClientConfig] = None
    ) -> "capo_route_53.types.get_traffic_policy_instance_count_response.GetTrafficPolicyInstanceCountResponse":
        """<p>Gets the number of traffic policy instances that are associated with the current Amazon Web Services account.</p>

        Raises:
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.get_traffic_policy_instance_count_request.GetTrafficPolicyInstanceCountRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.get_traffic_policy_instance_count_response.GetTrafficPolicyInstanceCountResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.get_traffic_policy_instance_count

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.get_traffic_policy_instance_count.get_traffic_policy_instance_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.get_traffic_policy_instance_count_request.GetTrafficPolicyInstanceCountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cidr_blocks(
        self,
        collection_id: "capo_route_53.types.uuid.UUID",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        location_name: Optional[
            "capo_route_53.types.cidr_location_name_default_not_allowed.CidrLocationNameDefaultNotAllowed"
        ] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_route_53.types.list_cidr_blocks_response.ListCidrBlocksResponse":
        """<p>Returns a paginated list of location objects and their CIDR blocks.</p>

        Args:
            collection_id: <p>The UUID of the CIDR collection.</p>
            location_name: <p>The name of the CIDR collection location.</p>
            next_token: <p>An opaque pagination token to indicate where the service is to begin enumerating results.</p>
            max_results: <p>Maximum number of results you want returned.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_cidr_collection_exception.NoSuchCidrCollectionException: <p>The CIDR collection you specified, doesn't exist.</p>
            capo_route_53.errors.no_such_cidr_location_exception.NoSuchCidrLocationException: <p>The CIDR collection location doesn't match any locations in your account.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_cidr_blocks_request.ListCidrBlocksRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_cidr_blocks_response.ListCidrBlocksResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_cidr_blocks

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_cidr_blocks.list_cidr_blocks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_cidr_blocks_request.ListCidrBlocksRequest = {
            "collection_id": collection_id
        }
        if location_name is not None:
            input_["location_name"] = location_name
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

    def iter_list_cidr_blocks(
        self,
        collection_id: "capo_route_53.types.uuid.UUID",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        location_name: Optional[
            "capo_route_53.types.cidr_location_name_default_not_allowed.CidrLocationNameDefaultNotAllowed"
        ] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_route_53.types.cidr_block_summary.CidrBlockSummary]":
        _token = next_token
        while True:
            _response = self.list_cidr_blocks(
                collection_id,
                config_overrides=config_overrides,
                location_name=location_name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("cidr_blocks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cidr_collections(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_route_53.types.list_cidr_collections_response.ListCidrCollectionsResponse"
    ):
        """<p>Returns a paginated list of CIDR collections in the Amazon Web Services account (metadata only).</p>

        Args:
            next_token: <p>An opaque pagination token to indicate where the service is to begin enumerating results.</p> <p>If no value is provided, the listing of results starts from the beginning.</p>
            max_results: <p>The maximum number of CIDR collections to return in the response.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_cidr_collections_request.ListCidrCollectionsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_cidr_collections_response.ListCidrCollectionsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_cidr_collections

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_cidr_collections.list_cidr_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_cidr_collections_request.ListCidrCollectionsRequest = {}
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

    def iter_list_cidr_collections(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_route_53.types.collection_summary.CollectionSummary]":
        _token = next_token
        while True:
            _response = self.list_cidr_collections(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("cidr_collections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cidr_locations(
        self,
        collection_id: "capo_route_53.types.uuid.UUID",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_route_53.types.list_cidr_locations_response.ListCidrLocationsResponse":
        """<p>Returns a paginated list of CIDR locations for the given collection (metadata only, does not include CIDR blocks).</p>

        Args:
            collection_id: <p>The CIDR collection ID.</p>
            next_token: <p>An opaque pagination token to indicate where the service is to begin enumerating results.</p> <p>If no value is provided, the listing of results starts from the beginning.</p>
            max_results: <p>The maximum number of CIDR collection locations to return in the response.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_cidr_collection_exception.NoSuchCidrCollectionException: <p>The CIDR collection you specified, doesn't exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_cidr_locations_request.ListCidrLocationsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_cidr_locations_response.ListCidrLocationsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_cidr_locations

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_cidr_locations.list_cidr_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_cidr_locations_request.ListCidrLocationsRequest = {
            "collection_id": collection_id
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

    def iter_list_cidr_locations(
        self,
        collection_id: "capo_route_53.types.uuid.UUID",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_route_53.types.location_summary.LocationSummary]":
        _token = next_token
        while True:
            _response = self.list_cidr_locations(
                collection_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("cidr_locations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_geo_locations(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        start_continent_code: Optional[
            "capo_route_53.types.geo_location_continent_code.GeoLocationContinentCode"
        ] = None,
        start_country_code: Optional[
            "capo_route_53.types.geo_location_country_code.GeoLocationCountryCode"
        ] = None,
        start_subdivision_code: Optional[
            "capo_route_53.types.geo_location_subdivision_code.GeoLocationSubdivisionCode"
        ] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_geo_locations_response.ListGeoLocationsResponse":
        """<p>Retrieves a list of supported geographic locations.</p> <p>Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.</p> <p>Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.</p> <p>For a list of supported geolocation codes, see the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html">GeoLocation</a> data type.</p>

        Args:
            start_continent_code: <p>The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is true, and if <code>NextContinentCode</code> from the previous response has a value, enter that value in <code>startcontinentcode</code> to return the next page of results.</p> <p>Include <code>startcontinentcode</code> only if you want to list continents. Don't include <code>startcontinentcode</code> when you're listing countries or countries with their subdivisions.</p>
            start_country_code: <p>The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is <code>true</code>, and if <code>NextCountryCode</code> from the previous response has a value, enter that value in <code>startcountrycode</code> to return the next page of results.</p>
            start_subdivision_code: <p>The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if <code>IsTruncated</code> is <code>true</code>, and if <code>NextSubdivisionCode</code> from the previous response has a value, enter that value in <code>startsubdivisioncode</code> to return the next page of results.</p> <p>To list subdivisions (U.S. states), you must include both <code>startcountrycode</code> and <code>startsubdivisioncode</code>.</p>
            max_items: <p>(Optional) The maximum number of geolocations to be included in the response body for this request. If more than <code>maxitems</code> geolocations remain to be listed, then the value of the <code>IsTruncated</code> element in the response is <code>true</code>.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_geo_locations_request.ListGeoLocationsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_geo_locations_response.ListGeoLocationsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_geo_locations

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_geo_locations.list_geo_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_geo_locations_request.ListGeoLocationsRequest = {}
        if start_continent_code is not None:
            input_["start_continent_code"] = start_continent_code
        if start_country_code is not None:
            input_["start_country_code"] = start_country_code
        if start_subdivision_code is not None:
            input_["start_subdivision_code"] = start_subdivision_code
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_health_checks(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        marker: Optional["capo_route_53.types.page_marker.PageMarker"] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_health_checks_response.ListHealthChecksResponse":
        """<p>Retrieve a list of the health checks that are associated with the current Amazon Web Services account. </p>

        Args:
            marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more health checks. To get another group, submit another <code>ListHealthChecks</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more health checks to get.</p>
            max_items: <p>The maximum number of health checks that you want <code>ListHealthChecks</code> to return in response to the current request. Amazon Route 53 returns a maximum of 1000 items. If you set <code>MaxItems</code> to a value greater than 1000, Route 53 returns only the first 1000 health checks. </p>

        Raises:
            capo_route_53.errors.incompatible_version.IncompatibleVersion: <p>The resource you're trying to access is unsupported on this Amazon Route 53 endpoint.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_health_checks_request.ListHealthChecksRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_health_checks_response.ListHealthChecksResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_health_checks

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_health_checks.list_health_checks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_health_checks_request.ListHealthChecksRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_health_checks(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        marker: Optional["capo_route_53.types.page_marker.PageMarker"] = None,
        max_items: Optional[int] = None,
    ) -> "Iterator[capo_route_53.types.health_check.HealthCheck]":
        _token = marker
        while True:
            _response = self.list_health_checks(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("health_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token or not _resolve_path(_response, ("is_truncated",)):
                break

    def list_hosted_zones(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        marker: Optional["capo_route_53.types.page_marker.PageMarker"] = None,
        max_items: Optional[int] = None,
        delegation_set_id: Optional[
            "capo_route_53.types.resource_id.ResourceId"
        ] = None,
        hosted_zone_type: Optional[
            "capo_route_53.types.hosted_zone_type.HostedZoneType"
        ] = None,
    ) -> "capo_route_53.types.list_hosted_zones_response.ListHostedZonesResponse":
        """<p>Retrieves a list of the public and private hosted zones that are associated with the current Amazon Web Services account. The response includes a <code>HostedZones</code> child element for each hosted zone.</p> <p>Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of hosted zones, you can use the <code>maxitems</code> parameter to list them in groups of up to 100.</p>

        Args:
            marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more hosted zones. To get more hosted zones, submit another <code>ListHostedZones</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more hosted zones to get.</p>
            max_items: <p>(Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than <code>maxitems</code> hosted zones, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of <code>NextMarker</code> is the hosted zone ID of the first hosted zone that Route 53 will return if you submit another request.</p>
            delegation_set_id: <p>If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set. </p>
            hosted_zone_type: <p> (Optional) Specifies if the hosted zone is private. </p>

        Raises:
            capo_route_53.errors.delegation_set_not_reusable.DelegationSetNotReusable: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_delegation_set.NoSuchDelegationSet: <p>A reusable delegation set with the specified ID does not exist.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_hosted_zones_request.ListHostedZonesRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_hosted_zones_response.ListHostedZonesResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_hosted_zones

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_hosted_zones.list_hosted_zones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_hosted_zones_request.ListHostedZonesRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if delegation_set_id is not None:
            input_["delegation_set_id"] = delegation_set_id
        if hosted_zone_type is not None:
            input_["hosted_zone_type"] = hosted_zone_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_hosted_zones(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        marker: Optional["capo_route_53.types.page_marker.PageMarker"] = None,
        max_items: Optional[int] = None,
        delegation_set_id: Optional[
            "capo_route_53.types.resource_id.ResourceId"
        ] = None,
        hosted_zone_type: Optional[
            "capo_route_53.types.hosted_zone_type.HostedZoneType"
        ] = None,
    ) -> "Iterator[capo_route_53.types.hosted_zone.HostedZone]":
        _token = marker
        while True:
            _response = self.list_hosted_zones(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
                delegation_set_id=delegation_set_id,
                hosted_zone_type=hosted_zone_type,
            )
            _page = _resolve_path(_response, ("hosted_zones",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token or not _resolve_path(_response, ("is_truncated",)):
                break

    def list_hosted_zones_by_name(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        dns_name: Optional["capo_route_53.types.dns_name.DNSName"] = None,
        hosted_zone_id: Optional["capo_route_53.types.resource_id.ResourceId"] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_hosted_zones_by_name_response.ListHostedZonesByNameResponse":
        r"""<p>Retrieves a list of your hosted zones in lexicographic order. The response includes a <code>HostedZones</code> child element for each hosted zone created by the current Amazon Web Services account. </p> <p> <code>ListHostedZonesByName</code> sorts hosted zones by name with the labels reversed. For example:</p> <p> <code>com.example.www.</code> </p> <p>Note the trailing dot, which can change the sort order in some circumstances.</p> <p>If the domain name includes escape characters or Punycode, <code>ListHostedZonesByName</code> alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for exämple.com, you specify ex\344mple.com for the domain name. <code>ListHostedZonesByName</code> alphabetizes it as:</p> <p> <code>com.ex\344mple.</code> </p> <p>The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html">DNS Domain Name Format</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the <code>MaxItems</code> parameter to list them in groups of up to 100. The response includes values that help navigate from one group of <code>MaxItems</code> hosted zones to the next:</p> <ul> <li> <p>The <code>DNSName</code> and <code>HostedZoneId</code> elements in the response contain the values, if any, specified for the <code>dnsname</code> and <code>hostedzoneid</code> parameters in the request that produced the current response.</p> </li> <li> <p>The <code>MaxItems</code> element in the response contains the value, if any, that you specified for the <code>maxitems</code> parameter in the request that produced the current response.</p> </li> <li> <p>If the value of <code>IsTruncated</code> in the response is true, there are more hosted zones associated with the current Amazon Web Services account. </p> <p>If <code>IsTruncated</code> is false, this response includes the last hosted zone that is associated with the current account. The <code>NextDNSName</code> element and <code>NextHostedZoneId</code> elements are omitted from the response.</p> </li> <li> <p>The <code>NextDNSName</code> and <code>NextHostedZoneId</code> elements in the response contain the domain name and the hosted zone ID of the next hosted zone that is associated with the current Amazon Web Services account. If you want to list more hosted zones, make another call to <code>ListHostedZonesByName</code>, and specify the value of <code>NextDNSName</code> and <code>NextHostedZoneId</code> in the <code>dnsname</code> and <code>hostedzoneid</code> parameters, respectively.</p> </li> </ul>

        Args:
            dns_name: <p>(Optional) For your first request to <code>ListHostedZonesByName</code>, include the <code>dnsname</code> parameter only if you want to specify the name of the first hosted zone in the response. If you don't include the <code>dnsname</code> parameter, Amazon Route 53 returns all of the hosted zones that were created by the current Amazon Web Services account, in ASCII order. For subsequent requests, include both <code>dnsname</code> and <code>hostedzoneid</code> parameters. For <code>dnsname</code>, specify the value of <code>NextDNSName</code> from the previous response.</p>
            hosted_zone_id: <p>(Optional) For your first request to <code>ListHostedZonesByName</code>, do not include the <code>hostedzoneid</code> parameter.</p> <p>If you have more hosted zones than the value of <code>maxitems</code>, <code>ListHostedZonesByName</code> returns only the first <code>maxitems</code> hosted zones. To get the next group of <code>maxitems</code> hosted zones, submit another request to <code>ListHostedZonesByName</code> and include both <code>dnsname</code> and <code>hostedzoneid</code> parameters. For the value of <code>hostedzoneid</code>, specify the value of the <code>NextHostedZoneId</code> element from the previous response.</p>
            max_items: <p>The maximum number of hosted zones to be included in the response body for this request. If you have more than <code>maxitems</code> hosted zones, then the value of the <code>IsTruncated</code> element in the response is true, and the values of <code>NextDNSName</code> and <code>NextHostedZoneId</code> specify the first hosted zone in the next group of <code>maxitems</code> hosted zones. </p>

        Raises:
            capo_route_53.errors.invalid_domain_name.InvalidDomainName: <p>The specified domain name is not valid.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_hosted_zones_by_name_request.ListHostedZonesByNameRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_hosted_zones_by_name_response.ListHostedZonesByNameResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_hosted_zones_by_name

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_hosted_zones_by_name.list_hosted_zones_by_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_hosted_zones_by_name_request.ListHostedZonesByNameRequest = {}
        if dns_name is not None:
            input_["dns_name"] = dns_name
        if hosted_zone_id is not None:
            input_["hosted_zone_id"] = hosted_zone_id
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_hosted_zones_by_vpc(
        self,
        vpc_id: "capo_route_53.types.vpc_id.VPCId",
        vpc_region: "capo_route_53.types.vpc_region.VPCRegion",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        max_items: Optional[int] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse":
        """<p>Lists all the private hosted zones that a specified VPC is associated with, regardless of which Amazon Web Services account or Amazon Web Services service owns the hosted zones. The <code>HostedZoneOwner</code> structure in the response contains one of the following values:</p> <ul> <li> <p>An <code>OwningAccount</code> element, which contains the account number of either the current Amazon Web Services account or another Amazon Web Services account. Some services, such as Cloud Map, create hosted zones using the current account. </p> </li> <li> <p>An <code>OwningService</code> element, which identifies the Amazon Web Services service that created and owns the hosted zone. For example, if a hosted zone was created by Amazon Elastic File System (Amazon EFS), the value of <code>Owner</code> is <code>efs.amazonaws.com</code>. </p> </li> </ul> <p> <code>ListHostedZonesByVPC</code> returns the hosted zones associated with the specified VPC and does not reflect the hosted zone associations to VPCs via Route 53 Profiles. To get the associations to a Profile, call the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileResourceAssociations.html">ListProfileResourceAssociations</a> API.</p> <note> <p>When listing private hosted zones, the hosted zone and the Amazon VPC must belong to the same partition where the hosted zones were created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.</p> <p>The following are the supported partitions:</p> <ul> <li> <p> <code>aws</code> - Amazon Web Services Regions</p> </li> <li> <p> <code>aws-cn</code> - China Regions</p> </li> <li> <p> <code>aws-us-gov</code> - Amazon Web Services GovCloud (US) Region</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Access Management</a> in the <i>Amazon Web Services General Reference</i>.</p> </note>

        Args:
            vpc_id: <p>The ID of the Amazon VPC that you want to list hosted zones for.</p>
            vpc_region: <p>For the Amazon VPC that you specified for <code>VPCId</code>, the Amazon Web Services Region that you created the VPC in. </p>
            max_items: <p>(Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If the specified VPC is associated with more than <code>MaxItems</code> hosted zones, the response includes a <code>NextToken</code> element. <code>NextToken</code> contains an encrypted token that identifies the first hosted zone that Route 53 will return if you submit another request.</p>
            next_token: <p>If the previous response included a <code>NextToken</code> element, the specified VPC is associated with more hosted zones. To get more hosted zones, submit another <code>ListHostedZonesByVPC</code> request. </p> <p>For the value of <code>NextToken</code>, specify the value of <code>NextToken</code> from the previous response.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more hosted zones to get.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_pagination_token.InvalidPaginationToken: <p>The value that you specified to get the second or subsequent page of results is invalid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_hosted_zones_by_vpc_request.ListHostedZonesByVPCRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_hosted_zones_by_vpc_response.ListHostedZonesByVPCResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_hosted_zones_by_vpc

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_hosted_zones_by_vpc.list_hosted_zones_by_vpc(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_hosted_zones_by_vpc_request.ListHostedZonesByVPCRequest = {
            "vpc_id": vpc_id,
            "vpc_region": vpc_region,
        }
        if max_items is not None:
            input_["max_items"] = max_items
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_query_logging_configs(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        hosted_zone_id: Optional["capo_route_53.types.resource_id.ResourceId"] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_route_53.types.list_query_logging_configs_response.ListQueryLoggingConfigsResponse":
        """<p>Lists the configurations for DNS query logging that are associated with the current Amazon Web Services account or the configuration that is associated with a specified hosted zone.</p> <p>For more information about DNS query logs, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html">CreateQueryLoggingConfig</a>. Additional information, including the format of DNS query logs, appears in <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html">Logging DNS Queries</a> in the <i>Amazon Route 53 Developer Guide</i>.</p>

        Args:
            hosted_zone_id: <p>(Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in <code>HostedZoneId</code>. </p> <p>If you don't specify a hosted zone ID, <code>ListQueryLoggingConfigs</code> returns all of the configurations that are associated with the current Amazon Web Services account.</p>
            next_token: <p>(Optional) If the current Amazon Web Services account has more than <code>MaxResults</code> query logging configurations, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>ListQueryLoggingConfigs</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p>
            max_results: <p>(Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current Amazon Web Services account has more than <code>MaxResults</code> configurations, use the value of <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html#API_ListQueryLoggingConfigs_RequestSyntax">NextToken</a> in the response to get the next page of results.</p> <p>If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 100 configurations.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_pagination_token.InvalidPaginationToken: <p>The value that you specified to get the second or subsequent page of results is invalid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_query_logging_configs_request.ListQueryLoggingConfigsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_query_logging_configs_response.ListQueryLoggingConfigsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_query_logging_configs

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_query_logging_configs.list_query_logging_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_query_logging_configs_request.ListQueryLoggingConfigsRequest = {}
        if hosted_zone_id is not None:
            input_["hosted_zone_id"] = hosted_zone_id
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

    def iter_list_query_logging_configs(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        hosted_zone_id: Optional["capo_route_53.types.resource_id.ResourceId"] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_route_53.types.query_logging_config.QueryLoggingConfig]":
        _token = next_token
        while True:
            _response = self.list_query_logging_configs(
                config_overrides=config_overrides,
                hosted_zone_id=hosted_zone_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("query_logging_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_record_sets(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        start_record_name: Optional["capo_route_53.types.dns_name.DNSName"] = None,
        start_record_type: Optional["capo_route_53.types.rr_type.RRType"] = None,
        start_record_identifier: Optional[
            "capo_route_53.types.resource_record_set_identifier.ResourceRecordSetIdentifier"
        ] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_resource_record_sets_response.ListResourceRecordSetsResponse":
        """<p>Lists the resource record sets in a specified hosted zone.</p> <p> <code>ListResourceRecordSets</code> returns up to 300 resource record sets at a time in ASCII order, beginning at a position specified by the <code>name</code> and <code>type</code> elements.</p> <p> <b>Sort order</b> </p> <p> <code>ListResourceRecordSets</code> sorts results first by DNS name with the labels reversed, for example:</p> <p> <code>com.example.www.</code> </p> <p>Note the trailing dot, which can change the sort order when the record name contains characters that appear before <code>.</code> (decimal 46) in the ASCII table. These characters include the following: <code>! " # $ % & ' ( ) * + , -</code> </p> <p>When multiple records have the same DNS name, <code>ListResourceRecordSets</code> sorts results by the record type.</p> <p> <b>Specifying where to start listing records</b> </p> <p>You can use the name and type elements to specify the resource record set that the list begins with:</p> <dl> <dt>If you do not specify Name or Type</dt> <dd> <p>The results begin with the first resource record set that the hosted zone contains.</p> </dd> <dt>If you specify Name but not Type</dt> <dd> <p>The results begin with the first resource record set in the list whose name is greater than or equal to <code>Name</code>.</p> </dd> <dt>If you specify Type but not Name</dt> <dd> <p>Amazon Route 53 returns the <code>InvalidInput</code> error.</p> </dd> <dt>If you specify both Name and Type</dt> <dd> <p>The results begin with the first resource record set in the list whose name is greater than or equal to <code>Name</code>, and whose type is greater than or equal to <code>Type</code>.</p> <note> <p>Type is only used to sort between records with the same record Name.</p> </note> </dd> </dl> <p> <b>Resource record sets that are PENDING</b> </p> <p>This action returns the most current version of the records. This includes records that are <code>PENDING</code>, and that are not yet available on all Route 53 DNS servers.</p> <p> <b>Changing resource record sets</b> </p> <p>To ensure that you get an accurate listing of the resource record sets for a hosted zone at a point in time, do not submit a <code>ChangeResourceRecordSets</code> request while you're paging through the results of a <code>ListResourceRecordSets</code> request. If you do, some pages may display results without the latest changes while other pages display results with the latest changes.</p> <p> <b>Displaying the next page of results</b> </p> <p>If a <code>ListResourceRecordSets</code> command returns more than one page of results, the value of <code>IsTruncated</code> is <code>true</code>. To display the next page of results, get the values of <code>NextRecordName</code>, <code>NextRecordType</code>, and <code>NextRecordIdentifier</code> (if any) from the response. Then submit another <code>ListResourceRecordSets</code> request, and specify those values for <code>StartRecordName</code>, <code>StartRecordType</code>, and <code>StartRecordIdentifier</code>.</p>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone that contains the resource record sets that you want to list.</p>
            start_record_name: <p>The first name in the lexicographic ordering of resource record sets that you want to list. If the specified record name doesn't exist, the results begin with the first resource record set that has a name greater than the value of <code>name</code>.</p>
            start_record_type: <p>The type of resource record set to begin the record listing from.</p> <p>Valid values for basic resource record sets: <code>A</code> | <code>AAAA</code> | <code>CAA</code> | <code>CNAME</code> | <code>MX</code> | <code>NAPTR</code> | <code>NS</code> | <code>PTR</code> | <code>SOA</code> | <code>SPF</code> | <code>SRV</code> | <code>TXT</code> </p> <p>Values for weighted, latency, geolocation, and failover resource record sets: <code>A</code> | <code>AAAA</code> | <code>CAA</code> | <code>CNAME</code> | <code>MX</code> | <code>NAPTR</code> | <code>PTR</code> | <code>SPF</code> | <code>SRV</code> | <code>TXT</code> </p> <p>Values for alias resource record sets: </p> <ul> <li> <p> <b>API Gateway custom regional API or edge-optimized API</b>: A</p> </li> <li> <p> <b>CloudFront distribution</b>: A or AAAA</p> </li> <li> <p> <b>Elastic Beanstalk environment that has a regionalized subdomain</b>: A</p> </li> <li> <p> <b>Elastic Load Balancing load balancer</b>: A | AAAA</p> </li> <li> <p> <b>S3 bucket</b>: A</p> </li> <li> <p> <b>VPC interface VPC endpoint</b>: A</p> </li> <li> <p> <b>Another resource record set in this hosted zone:</b> The type of the resource record set that the alias references.</p> </li> </ul> <p>Constraint: Specifying <code>type</code> without specifying <code>name</code> returns an <code>InvalidInput</code> error.</p>
            start_record_identifier: <p> <i>Resource record sets that have a routing policy other than simple:</i> If results were truncated for a given DNS name and type, specify the value of <code>NextRecordIdentifier</code> from the previous response to get the next resource record set that has the current DNS name and type.</p>
            max_items: <p>(Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than <code>maxitems</code> resource record sets, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of the <code>NextRecordName</code> and <code>NextRecordType</code> elements in the response identify the first resource record set in the next group of <code>maxitems</code> resource record sets.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_resource_record_sets_request.ListResourceRecordSetsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_resource_record_sets_response.ListResourceRecordSetsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_resource_record_sets

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_resource_record_sets.list_resource_record_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_resource_record_sets_request.ListResourceRecordSetsRequest = {
            "hosted_zone_id": hosted_zone_id
        }
        if start_record_name is not None:
            input_["start_record_name"] = start_record_name
        if start_record_type is not None:
            input_["start_record_type"] = start_record_type
        if start_record_identifier is not None:
            input_["start_record_identifier"] = start_record_identifier
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_reusable_delegation_sets(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        marker: Optional["capo_route_53.types.page_marker.PageMarker"] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_reusable_delegation_sets_response.ListReusableDelegationSetsResponse":
        """<p>Retrieves a list of the reusable delegation sets that are associated with the current Amazon Web Services account.</p>

        Args:
            marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more reusable delegation sets. To get another group, submit another <code>ListReusableDelegationSets</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more reusable delegation sets to get.</p>
            max_items: <p>The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_reusable_delegation_sets_request.ListReusableDelegationSetsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_reusable_delegation_sets_response.ListReusableDelegationSetsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_reusable_delegation_sets

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_reusable_delegation_sets.list_reusable_delegation_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_reusable_delegation_sets_request.ListReusableDelegationSetsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_type: "capo_route_53.types.tag_resource_type.TagResourceType",
        resource_id: "capo_route_53.types.tag_resource_id.TagResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for one health check or hosted zone. </p> <p>For information about using tags for cost allocation, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Billing and Cost Management User Guide</i>.</p>

        Args:
            resource_type: <p>The type of the resource.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>
            resource_id: <p>The ID of the resource for which you want to retrieve tags.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_tags_for_resource

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_type": resource_type,
            "resource_id": resource_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resources(
        self,
        resource_type: "capo_route_53.types.tag_resource_type.TagResourceType",
        resource_ids: "capo_route_53.types.tag_resource_id_list.TagResourceIdList",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.list_tags_for_resources_response.ListTagsForResourcesResponse":
        """<p>Lists tags for up to 10 health checks or hosted zones.</p> <p>For information about using tags for cost allocation, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Billing and Cost Management User Guide</i>.</p>

        Args:
            resource_type: <p>The type of the resources.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>
            resource_ids: <p>A complex type that contains the ResourceId element for each resource for which you want to get a list of tags.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_tags_for_resources_request.ListTagsForResourcesRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_tags_for_resources_response.ListTagsForResourcesResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_tags_for_resources

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_tags_for_resources.list_tags_for_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_tags_for_resources_request.ListTagsForResourcesRequest = {
            "resource_type": resource_type,
            "resource_ids": resource_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_traffic_policies(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        traffic_policy_id_marker: Optional[
            "capo_route_53.types.traffic_policy_id.TrafficPolicyId"
        ] = None,
        max_items: Optional[int] = None,
    ) -> (
        "capo_route_53.types.list_traffic_policies_response.ListTrafficPoliciesResponse"
    ):
        """<p>Gets information about the latest version for every traffic policy that is associated with the current Amazon Web Services account. Policies are listed in the order that they were created in. </p> <p>For information about how of deleting a traffic policy affects the response from <code>ListTrafficPolicies</code>, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html">DeleteTrafficPolicy</a>. </p>

        Args:
            traffic_policy_id_marker: <p>(Conditional) For your first request to <code>ListTrafficPolicies</code>, don't include the <code>TrafficPolicyIdMarker</code> parameter.</p> <p>If you have more traffic policies than the value of <code>MaxItems</code>, <code>ListTrafficPolicies</code> returns only the first <code>MaxItems</code> traffic policies. To get the next group of policies, submit another request to <code>ListTrafficPolicies</code>. For the value of <code>TrafficPolicyIdMarker</code>, specify the value of <code>TrafficPolicyIdMarker</code> that was returned in the previous response.</p>
            max_items: <p>(Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than <code>MaxItems</code> traffic policies, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of <code>TrafficPolicyIdMarker</code> is the ID of the first traffic policy that Route 53 will return if you submit another request.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_traffic_policies_request.ListTrafficPoliciesRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_traffic_policies_response.ListTrafficPoliciesResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_traffic_policies

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_traffic_policies.list_traffic_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_traffic_policies_request.ListTrafficPoliciesRequest = {}
        if traffic_policy_id_marker is not None:
            input_["traffic_policy_id_marker"] = traffic_policy_id_marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_traffic_policy_instances(
        self,
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        hosted_zone_id_marker: Optional[
            "capo_route_53.types.resource_id.ResourceId"
        ] = None,
        traffic_policy_instance_name_marker: Optional[
            "capo_route_53.types.dns_name.DNSName"
        ] = None,
        traffic_policy_instance_type_marker: Optional[
            "capo_route_53.types.rr_type.RRType"
        ] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_traffic_policy_instances_response.ListTrafficPolicyInstancesResponse":
        """<p>Gets information about the traffic policy instances that you created by using the current Amazon Web Services account.</p> <note> <p>After you submit an <code>UpdateTrafficPolicyInstance</code> request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the <code>State</code> response element.</p> </note> <p>Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the <code>MaxItems</code> parameter to list them in groups of up to 100.</p>

        Args:
            hosted_zone_id_marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>HostedZoneId</code>, specify the value of <code>HostedZoneIdMarker</code> from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            traffic_policy_instance_name_marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            traffic_policy_instance_type_marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            max_items: <p>The maximum number of traffic policy instances that you want Amazon Route 53 to return in response to a <code>ListTrafficPolicyInstances</code> request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance in the next group of <code>MaxItems</code> traffic policy instances.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance: <p>No traffic policy instance exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_traffic_policy_instances_request.ListTrafficPolicyInstancesRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_traffic_policy_instances_response.ListTrafficPolicyInstancesResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_instances

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_instances.list_traffic_policy_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_traffic_policy_instances_request.ListTrafficPolicyInstancesRequest = {}
        if hosted_zone_id_marker is not None:
            input_["hosted_zone_id_marker"] = hosted_zone_id_marker
        if traffic_policy_instance_name_marker is not None:
            input_["traffic_policy_instance_name_marker"] = (
                traffic_policy_instance_name_marker
            )
        if traffic_policy_instance_type_marker is not None:
            input_["traffic_policy_instance_type_marker"] = (
                traffic_policy_instance_type_marker
            )
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_traffic_policy_instances_by_hosted_zone(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        traffic_policy_instance_name_marker: Optional[
            "capo_route_53.types.dns_name.DNSName"
        ] = None,
        traffic_policy_instance_type_marker: Optional[
            "capo_route_53.types.rr_type.RRType"
        ] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_traffic_policy_instances_by_hosted_zone_response.ListTrafficPolicyInstancesByHostedZoneResponse":
        """<p>Gets information about the traffic policy instances that you created in a specified hosted zone.</p> <note> <p>After you submit a <code>CreateTrafficPolicyInstance</code> or an <code>UpdateTrafficPolicyInstance</code> request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the <code>State</code> response element.</p> </note> <p>Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the <code>MaxItems</code> parameter to list them in groups of up to 100.</p>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone that you want to list traffic policy instances for.</p>
            traffic_policy_instance_name_marker: <p>If the value of <code>IsTruncated</code> in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            traffic_policy_instance_type_marker: <p>If the value of <code>IsTruncated</code> in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstances</code> request. For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            max_items: <p>The maximum number of traffic policy instances to be included in the response body for this request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance: <p>No traffic policy instance exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_traffic_policy_instances_by_hosted_zone_request.ListTrafficPolicyInstancesByHostedZoneRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_traffic_policy_instances_by_hosted_zone_response.ListTrafficPolicyInstancesByHostedZoneResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_instances_by_hosted_zone

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_instances_by_hosted_zone.list_traffic_policy_instances_by_hosted_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_traffic_policy_instances_by_hosted_zone_request.ListTrafficPolicyInstancesByHostedZoneRequest = {
            "hosted_zone_id": hosted_zone_id
        }
        if traffic_policy_instance_name_marker is not None:
            input_["traffic_policy_instance_name_marker"] = (
                traffic_policy_instance_name_marker
            )
        if traffic_policy_instance_type_marker is not None:
            input_["traffic_policy_instance_type_marker"] = (
                traffic_policy_instance_type_marker
            )
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_traffic_policy_instances_by_policy(
        self,
        traffic_policy_id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        traffic_policy_version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        hosted_zone_id_marker: Optional[
            "capo_route_53.types.resource_id.ResourceId"
        ] = None,
        traffic_policy_instance_name_marker: Optional[
            "capo_route_53.types.dns_name.DNSName"
        ] = None,
        traffic_policy_instance_type_marker: Optional[
            "capo_route_53.types.rr_type.RRType"
        ] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_traffic_policy_instances_by_policy_response.ListTrafficPolicyInstancesByPolicyResponse":
        """<p>Gets information about the traffic policy instances that you created by using a specify traffic policy version.</p> <note> <p>After you submit a <code>CreateTrafficPolicyInstance</code> or an <code>UpdateTrafficPolicyInstance</code> request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the <code>State</code> response element.</p> </note> <p>Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the <code>MaxItems</code> parameter to list them in groups of up to 100.</p>

        Args:
            traffic_policy_id: <p>The ID of the traffic policy for which you want to list traffic policy instances.</p>
            traffic_policy_version: <p>The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by <code>TrafficPolicyId</code>.</p>
            hosted_zone_id_marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request. </p> <p>For the value of <code>hostedzoneid</code>, specify the value of <code>HostedZoneIdMarker</code> from the previous response, which is the hosted zone ID of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            traffic_policy_instance_name_marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request.</p> <p>For the value of <code>trafficpolicyinstancename</code>, specify the value of <code>TrafficPolicyInstanceNameMarker</code> from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            traffic_policy_instance_type_marker: <p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more traffic policy instances. To get more traffic policy instances, submit another <code>ListTrafficPolicyInstancesByPolicy</code> request.</p> <p>For the value of <code>trafficpolicyinstancetype</code>, specify the value of <code>TrafficPolicyInstanceTypeMarker</code> from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more traffic policy instances to get.</p>
            max_items: <p>The maximum number of traffic policy instances to be included in the response body for this request. If you have more than <code>MaxItems</code> traffic policy instances, the value of the <code>IsTruncated</code> element in the response is <code>true</code>, and the values of <code>HostedZoneIdMarker</code>, <code>TrafficPolicyInstanceNameMarker</code>, and <code>TrafficPolicyInstanceTypeMarker</code> represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance: <p>No traffic policy instance exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_traffic_policy_instances_by_policy_request.ListTrafficPolicyInstancesByPolicyRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_traffic_policy_instances_by_policy_response.ListTrafficPolicyInstancesByPolicyResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_instances_by_policy

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_instances_by_policy.list_traffic_policy_instances_by_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_traffic_policy_instances_by_policy_request.ListTrafficPolicyInstancesByPolicyRequest = {
            "traffic_policy_id": traffic_policy_id,
            "traffic_policy_version": traffic_policy_version,
        }
        if hosted_zone_id_marker is not None:
            input_["hosted_zone_id_marker"] = hosted_zone_id_marker
        if traffic_policy_instance_name_marker is not None:
            input_["traffic_policy_instance_name_marker"] = (
                traffic_policy_instance_name_marker
            )
        if traffic_policy_instance_type_marker is not None:
            input_["traffic_policy_instance_type_marker"] = (
                traffic_policy_instance_type_marker
            )
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_traffic_policy_versions(
        self,
        id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        traffic_policy_version_marker: Optional[
            "capo_route_53.types.traffic_policy_version_marker.TrafficPolicyVersionMarker"
        ] = None,
        max_items: Optional[int] = None,
    ) -> "capo_route_53.types.list_traffic_policy_versions_response.ListTrafficPolicyVersionsResponse":
        """<p>Gets information about all of the versions for a specified traffic policy.</p> <p>Traffic policy versions are listed in numerical order by <code>VersionNumber</code>.</p>

        Args:
            id: <p>Specify the value of <code>Id</code> of the traffic policy for which you want to list all versions.</p>
            traffic_policy_version_marker: <p>For your first request to <code>ListTrafficPolicyVersions</code>, don't include the <code>TrafficPolicyVersionMarker</code> parameter.</p> <p>If you have more traffic policy versions than the value of <code>MaxItems</code>, <code>ListTrafficPolicyVersions</code> returns only the first group of <code>MaxItems</code> versions. To get more traffic policy versions, submit another <code>ListTrafficPolicyVersions</code> request. For the value of <code>TrafficPolicyVersionMarker</code>, specify the value of <code>TrafficPolicyVersionMarker</code> in the previous response.</p>
            max_items: <p>The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than <code>MaxItems</code> versions, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of the <code>TrafficPolicyVersionMarker</code> element is the ID of the first version that Route 53 will return if you submit another request.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_traffic_policy_versions_request.ListTrafficPolicyVersionsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_traffic_policy_versions_response.ListTrafficPolicyVersionsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_versions

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_traffic_policy_versions.list_traffic_policy_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_traffic_policy_versions_request.ListTrafficPolicyVersionsRequest = {
            "id": id
        }
        if traffic_policy_version_marker is not None:
            input_["traffic_policy_version_marker"] = traffic_policy_version_marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vpc_association_authorizations(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        next_token: Optional[
            "capo_route_53.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_route_53.types.list_vpc_association_authorizations_response.ListVPCAssociationAuthorizationsResponse":
        """<p>Gets a list of the VPCs that were created by other accounts and that can be associated with a specified hosted zone because you've submitted one or more <code>CreateVPCAssociationAuthorization</code> requests. </p> <p>The response includes a <code>VPCs</code> element with a <code>VPC</code> child element for each VPC that can be associated with the hosted zone.</p>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.</p>
            next_token: <p> <i>Optional</i>: If a response includes a <code>NextToken</code> element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of <code>NextToken</code> from the response in the <code>nexttoken</code> parameter in another <code>ListVPCAssociationAuthorizations</code> request.</p>
            max_results: <p> <i>Optional</i>: An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 50 VPCs per page.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.invalid_pagination_token.InvalidPaginationToken: <p>The value that you specified to get the second or subsequent page of results is invalid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.list_vpc_association_authorizations_request.ListVPCAssociationAuthorizationsRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.list_vpc_association_authorizations_response.ListVPCAssociationAuthorizationsResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.list_vpc_association_authorizations

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.list_vpc_association_authorizations.list_vpc_association_authorizations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.list_vpc_association_authorizations_request.ListVPCAssociationAuthorizationsRequest = {
            "hosted_zone_id": hosted_zone_id
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

    def test_dns_answer(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        record_name: "capo_route_53.types.dns_name.DNSName",
        record_type: "capo_route_53.types.rr_type.RRType",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        resolver_ip: Optional["capo_route_53.types.ip_address.IPAddress"] = None,
        edns0_client_subnet_ip: Optional[
            "capo_route_53.types.ip_address.IPAddress"
        ] = None,
        edns0_client_subnet_mask: Optional[
            "capo_route_53.types.subnet_mask.SubnetMask"
        ] = None,
    ) -> "capo_route_53.types.test_dns_answer_response.TestDNSAnswerResponse":
        """<p>Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask. </p> <p>This call only supports querying public hosted zones.</p> <note> <p>The <code>TestDnsAnswer </code> returns information similar to what you would expect from the answer section of the <code>dig</code> command. Therefore, if you query for the name servers of a subdomain that point to the parent name servers, those will not be returned.</p> </note>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.</p>
            record_name: <p>The name of the resource record set that you want Amazon Route 53 to simulate a query for.</p>
            record_type: <p>The type of the resource record set.</p>
            resolver_ip: <p>If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, <code>TestDnsAnswer</code> uses the IP address of a DNS resolver in the Amazon Web Services US East (N. Virginia) Region (<code>us-east-1</code>).</p>
            edns0_client_subnet_ip: <p>If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, <code>192.0.2.44</code> or <code>2001:db8:85a3::8a2e:370:7334</code>.</p>
            edns0_client_subnet_mask: <p>If you specify an IP address for <code>edns0clientsubnetip</code>, you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify <code>192.0.2.44</code> for <code>edns0clientsubnetip</code> and <code>24</code> for <code>edns0clientsubnetmask</code>, the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.</p> <p>The range of valid values depends on whether <code>edns0clientsubnetip</code> is an IPv4 or an IPv6 address:</p> <ul> <li> <p> <b>IPv4</b>: Specify a value between 0 and 32</p> </li> <li> <p> <b>IPv6</b>: Specify a value between 0 and 128</p> </li> </ul>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.test_dns_answer_request.TestDNSAnswerRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.test_dns_answer_response.TestDNSAnswerResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.test_dns_answer

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.test_dns_answer.test_dns_answer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.test_dns_answer_request.TestDNSAnswerRequest = {
            "hosted_zone_id": hosted_zone_id,
            "record_name": record_name,
            "record_type": record_type,
        }
        if resolver_ip is not None:
            input_["resolver_ip"] = resolver_ip
        if edns0_client_subnet_ip is not None:
            input_["edns0_client_subnet_ip"] = edns0_client_subnet_ip
        if edns0_client_subnet_mask is not None:
            input_["edns0_client_subnet_mask"] = edns0_client_subnet_mask

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_health_check(
        self,
        health_check_id: "capo_route_53.types.health_check_id.HealthCheckId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        health_check_version: Optional[
            "capo_route_53.types.health_check_version.HealthCheckVersion"
        ] = None,
        ip_address: Optional["capo_route_53.types.ip_address.IPAddress"] = None,
        port: Optional["capo_route_53.types.port.Port"] = None,
        resource_path: Optional[
            "capo_route_53.types.resource_path.ResourcePath"
        ] = None,
        fully_qualified_domain_name: Optional[
            "capo_route_53.types.fully_qualified_domain_name.FullyQualifiedDomainName"
        ] = None,
        search_string: Optional[
            "capo_route_53.types.search_string.SearchString"
        ] = None,
        failure_threshold: Optional[
            "capo_route_53.types.failure_threshold.FailureThreshold"
        ] = None,
        inverted: Optional["capo_route_53.types.inverted.Inverted"] = None,
        disabled: Optional["capo_route_53.types.disabled.Disabled"] = None,
        health_threshold: Optional[
            "capo_route_53.types.health_threshold.HealthThreshold"
        ] = None,
        child_health_checks: Optional[
            "capo_route_53.types.child_health_check_list.ChildHealthCheckList"
        ] = None,
        enable_sni: Optional["capo_route_53.types.enable_sni.EnableSNI"] = None,
        regions: Optional[
            "capo_route_53.types.health_check_region_list.HealthCheckRegionList"
        ] = None,
        alarm_identifier: Optional[
            "capo_route_53.types.alarm_identifier.AlarmIdentifier"
        ] = None,
        insufficient_data_health_status: Optional[
            "capo_route_53.types.insufficient_data_health_status.InsufficientDataHealthStatus"
        ] = None,
        reset_elements: Optional[
            "capo_route_53.types.resettable_element_name_list.ResettableElementNameList"
        ] = None,
    ) -> "capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse":
        """<p>Updates an existing health check. Note that some values can't be updated. </p> <p>For more information about updating health checks, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html">Creating, Updating, and Deleting Health Checks</a> in the <i>Amazon Route 53 Developer Guide</i>.</p>

        Args:
            health_check_id: <p>The ID for the health check for which you want detailed information. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p>
            health_check_version: <p>A sequential counter that Amazon Route 53 sets to <code>1</code> when you create a health check and increments by 1 each time you update settings for the health check.</p> <p>We recommend that you use <code>GetHealthCheck</code> or <code>ListHealthChecks</code> to get the current value of <code>HealthCheckVersion</code> for the health check that you want to update, and that you include that value in your <code>UpdateHealthCheck</code> request. This prevents Route 53 from overwriting an intervening update:</p> <ul> <li> <p>If the value in the <code>UpdateHealthCheck</code> request matches the value of <code>HealthCheckVersion</code> in the health check, Route 53 updates the health check with the new settings.</p> </li> <li> <p>If the value of <code>HealthCheckVersion</code> in the health check is greater, the health check was changed after you got the version number. Route 53 does not update the health check, and it returns a <code>HealthCheckVersionMismatch</code> error.</p> </li> </ul>
            ip_address: <p>The IPv4 or IPv6 IP address for the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for <code>IPAddress</code>, Route 53 sends a DNS request to resolve the domain name that you specify in <code>FullyQualifiedDomainName</code> at the interval that you specify in <code>RequestInterval</code>. Using an IP address that is returned by DNS, Route 53 then checks the health of the endpoint.</p> <p>Use one of the following formats for the value of <code>IPAddress</code>: </p> <ul> <li> <p> <b>IPv4 address</b>: four values between 0 and 255, separated by periods (.), for example, <code>192.0.2.44</code>.</p> </li> <li> <p> <b>IPv6 address</b>: eight groups of four hexadecimal values, separated by colons (:), for example, <code>2001:0db8:85a3:0000:0000:abcd:0001:2345</code>. You can also shorten IPv6 addresses as described in RFC 5952, for example, <code>2001:db8:85a3::abcd:1:2345</code>.</p> </li> </ul> <p>If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for <code>IPAddress</code>. This ensures that the IP address of your instance never changes. For more information, see the applicable documentation:</p> <ul> <li> <p>Linux: <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">Elastic IP Addresses (EIP)</a> in the <i>Amazon EC2 User Guide for Linux Instances</i> </p> </li> <li> <p>Windows: <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.html">Elastic IP Addresses (EIP)</a> in the <i>Amazon EC2 User Guide for Windows Instances</i> </p> </li> </ul> <note> <p>If a health check already has a value for <code>IPAddress</code>, you can change the value. However, you can't update an existing health check to add or remove the value of <code>IPAddress</code>. </p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName">FullyQualifiedDomainName</a>. </p> <p>Constraints: Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:</p> <ul> <li> <p> <a href="https://tools.ietf.org/html/rfc5735">RFC 5735, Special Use IPv4 Addresses</a> </p> </li> <li> <p> <a href="https://tools.ietf.org/html/rfc6598">RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space</a> </p> </li> <li> <p> <a href="https://tools.ietf.org/html/rfc5156">RFC 5156, Special-Use IPv6 Addresses</a> </p> </li> </ul>
            port: <p>The port on the endpoint that you want Amazon Route 53 to perform health checks on.</p> <note> <p>Don't specify a value for <code>Port</code> when you specify a value for <code>Type</code> of <code>CLOUDWATCH_METRIC</code> or <code>CALCULATED</code>.</p> </note>
            resource_path: <p>The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html. You can also include query string parameters, for example, <code>/welcome.html?language=jp&login=y</code>. </p> <p>Specify this value only if you want to change it.</p>
            fully_qualified_domain_name: <p>Amazon Route 53 behavior depends on whether you specify a value for <code>IPAddress</code>.</p> <note> <p>If a health check already has a value for <code>IPAddress</code>, you can change the value. However, you can't update an existing health check to add or remove the value of <code>IPAddress</code>. </p> </note> <p> <b>If you specify a value for</b> <code>IPAddress</code>:</p> <p>Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of <code>FullyQualifiedDomainName</code> in the <code>Host</code> header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.</p> <p>When Route 53 checks the health of an endpoint, here is how it constructs the <code>Host</code> header:</p> <ul> <li> <p>If you specify a value of <code>80</code> for <code>Port</code> and <code>HTTP</code> or <code>HTTP_STR_MATCH</code> for <code>Type</code>, Route 53 passes the value of <code>FullyQualifiedDomainName</code> to the endpoint in the <code>Host</code> header.</p> </li> <li> <p>If you specify a value of <code>443</code> for <code>Port</code> and <code>HTTPS</code> or <code>HTTPS_STR_MATCH</code> for <code>Type</code>, Route 53 passes the value of <code>FullyQualifiedDomainName</code> to the endpoint in the <code>Host</code> header.</p> </li> <li> <p>If you specify another value for <code>Port</code> and any value except <code>TCP</code> for <code>Type</code>, Route 53 passes <i> <code>FullyQualifiedDomainName</code>:<code>Port</code> </i> to the endpoint in the <code>Host</code> header.</p> </li> </ul> <p>If you don't specify a value for <code>FullyQualifiedDomainName</code>, Route 53 substitutes the value of <code>IPAddress</code> in the <code>Host</code> header in each of the above cases.</p> <p> <b>If you don't specify a value for</b> <code>IPAddress</code>:</p> <p>If you don't specify a value for <code>IPAddress</code>, Route 53 sends a DNS request to the domain that you specify in <code>FullyQualifiedDomainName</code> at the interval you specify in <code>RequestInterval</code>. Using an IPv4 address that is returned by DNS, Route 53 then checks the health of the endpoint.</p> <p>If you don't specify a value for <code>IPAddress</code>, you can’t update the health check to remove the <code>FullyQualifiedDomainName</code>; if you don’t specify a value for <code>IPAddress</code> on creation, a <code>FullyQualifiedDomainName</code> is required.</p> <note> <p>If you don't specify a value for <code>IPAddress</code>, Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for <code>FullyQualifiedDomainName</code>, the health check fails with a "DNS resolution failed" error.</p> </note> <p>If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by <code>FullyQualifiedDomainName</code>, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of <code>FullyQualifiedDomainName</code>, specify the domain name of the server (such as <code>us-east-2-www.example.com</code>), not the name of the resource record sets (www.example.com).</p> <important> <p>In this configuration, if the value of <code>FullyQualifiedDomainName</code> matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.</p> </important> <p>In addition, if the value of <code>Type</code> is <code>HTTP</code>, <code>HTTPS</code>, <code>HTTP_STR_MATCH</code>, or <code>HTTPS_STR_MATCH</code>, Route 53 passes the value of <code>FullyQualifiedDomainName</code> in the <code>Host</code> header, as it does when you specify a value for <code>IPAddress</code>. If the value of <code>Type</code> is <code>TCP</code>, Route 53 doesn't pass a <code>Host</code> header.</p>
            search_string: <p>If the value of <code>Type</code> is <code>HTTP_STR_MATCH</code> or <code>HTTPS_STR_MATCH</code>, the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy. (You can't change the value of <code>Type</code> when you update a health check.)</p>
            failure_threshold: <p>The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html">How Amazon Route 53 Determines Whether an Endpoint Is Healthy</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>Otherwise, if you don't specify a value for <code>FailureThreshold</code>, the default value is three health checks.</p>
            inverted: <p>Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.</p>
            disabled: <p>Stops Route 53 from performing health checks. When you disable a health check, here's what happens:</p> <ul> <li> <p> <b>Health checks that check the health of endpoints:</b> Route 53 stops submitting requests to your application, server, or other resource.</p> </li> <li> <p> <b>Calculated health checks:</b> Route 53 stops aggregating the status of the referenced health checks.</p> </li> <li> <p> <b>Health checks that monitor CloudWatch alarms:</b> Route 53 stops monitoring the corresponding CloudWatch metrics.</p> </li> </ul> <p>After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. Additionally, in disabled state, you can also invert the status of the health check to route traffic differently. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted">Inverted</a>. </p> <p>Charges for a health check still apply when the health check is disabled. For more information, see <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p>
            health_threshold: <p>The number of child health checks that are associated with a <code>CALCULATED</code> health that Amazon Route 53 must consider healthy for the <code>CALCULATED</code> health check to be considered healthy. To specify the child health checks that you want to associate with a <code>CALCULATED</code> health check, use the <code>ChildHealthChecks</code> and <code>ChildHealthCheck</code> elements.</p> <p>Note the following:</p> <ul> <li> <p>If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.</p> </li> <li> <p>If you specify <code>0</code>, Route 53 always considers this health check to be healthy.</p> </li> </ul>
            child_health_checks: <p>A complex type that contains one <code>ChildHealthCheck</code> element for each health check that you want to associate with a <code>CALCULATED</code> health check.</p>
            enable_sni: <p>Specify whether you want Amazon Route 53 to send the value of <code>FullyQualifiedDomainName</code> to the endpoint in the <code>client_hello</code> message during <code>TLS</code> negotiation. This allows the endpoint to respond to <code>HTTPS</code> health check requests with the applicable SSL/TLS certificate.</p> <p>Some endpoints require that HTTPS requests include the host name in the <code>client_hello</code> message. If you don't enable SNI, the status of the health check will be SSL alert <code>handshake_failure</code>. A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.</p> <p>The SSL/TLS certificate on your endpoint includes a domain name in the <code>Common Name</code> field and possibly several more in the <code>Subject Alternative Names</code> field. One of the domain names in the certificate should match the value that you specify for <code>FullyQualifiedDomainName</code>. If the endpoint responds to the <code>client_hello</code> message with a certificate that does not include the domain name that you specified in <code>FullyQualifiedDomainName</code>, a health checker will retry the handshake. In the second attempt, the health checker will omit <code>FullyQualifiedDomainName</code> from the <code>client_hello</code> message.</p>
            regions: <p>A complex type that contains one <code>Region</code> element for each region that you want Amazon Route 53 health checkers to check the specified endpoint from.</p>
            alarm_identifier: <p>A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.</p>
            insufficient_data_health_status: <p>When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:</p> <ul> <li> <p> <code>Healthy</code>: Route 53 considers the health check to be healthy.</p> </li> <li> <p> <code>Unhealthy</code>: Route 53 considers the health check to be unhealthy.</p> </li> <li> <p> <code>LastKnownStatus</code>: By default, Route 53 uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the status for the health check is healthy.</p> </li> </ul>
            reset_elements: <p>A complex type that contains one <code>ResettableElementName</code> element for each element that you want to reset to the default value. Valid values for <code>ResettableElementName</code> include the following:</p> <ul> <li> <p> <code>ChildHealthChecks</code>: Amazon Route 53 resets <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-ChildHealthChecks">ChildHealthChecks</a> to null.</p> </li> <li> <p> <code>FullyQualifiedDomainName</code>: Route 53 resets <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName">FullyQualifiedDomainName</a>. to null.</p> </li> <li> <p> <code>Regions</code>: Route 53 resets the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions">Regions</a> list to the default set of regions. </p> </li> <li> <p> <code>ResourcePath</code>: Route 53 resets <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-ResourcePath">ResourcePath</a> to null.</p> </li> </ul>

        Raises:
            capo_route_53.errors.health_check_version_mismatch.HealthCheckVersionMismatch: <p>The value of <code>HealthCheckVersion</code> in the request doesn't match the value of <code>HealthCheckVersion</code> in the health check.</p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_health_check.NoSuchHealthCheck: <p>No health check exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.update_health_check_request.UpdateHealthCheckRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.update_health_check_response.UpdateHealthCheckResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.update_health_check

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.update_health_check.update_health_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.update_health_check_request.UpdateHealthCheckRequest = {
            "health_check_id": health_check_id
        }
        if health_check_version is not None:
            input_["health_check_version"] = health_check_version
        if ip_address is not None:
            input_["ip_address"] = ip_address
        if port is not None:
            input_["port"] = port
        if resource_path is not None:
            input_["resource_path"] = resource_path
        if fully_qualified_domain_name is not None:
            input_["fully_qualified_domain_name"] = fully_qualified_domain_name
        if search_string is not None:
            input_["search_string"] = search_string
        if failure_threshold is not None:
            input_["failure_threshold"] = failure_threshold
        if inverted is not None:
            input_["inverted"] = inverted
        if disabled is not None:
            input_["disabled"] = disabled
        if health_threshold is not None:
            input_["health_threshold"] = health_threshold
        if child_health_checks is not None:
            input_["child_health_checks"] = child_health_checks
        if enable_sni is not None:
            input_["enable_sni"] = enable_sni
        if regions is not None:
            input_["regions"] = regions
        if alarm_identifier is not None:
            input_["alarm_identifier"] = alarm_identifier
        if insufficient_data_health_status is not None:
            input_["insufficient_data_health_status"] = insufficient_data_health_status
        if reset_elements is not None:
            input_["reset_elements"] = reset_elements

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_hosted_zone_comment(
        self,
        id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        comment: Optional[
            "capo_route_53.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse":
        """<p>Updates the comment for a specified hosted zone.</p>

        Args:
            id: <p>The ID for the hosted zone that you want to update the comment for.</p>
            comment: <p>The new comment for the hosted zone. If you don't specify a value for <code>Comment</code>, Amazon Route 53 deletes the existing value of the <code>Comment</code> element, if any.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.update_hosted_zone_comment_request.UpdateHostedZoneCommentRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.update_hosted_zone_comment_response.UpdateHostedZoneCommentResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.update_hosted_zone_comment

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.update_hosted_zone_comment.update_hosted_zone_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.update_hosted_zone_comment_request.UpdateHostedZoneCommentRequest = {
            "id": id
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

    def update_hosted_zone_features(
        self,
        hosted_zone_id: "capo_route_53.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
        enable_accelerated_recovery: Optional[
            "capo_route_53.types.accelerated_recovery_enabled.AcceleratedRecoveryEnabled"
        ] = None,
    ) -> "capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse":
        """<p>Updates the features configuration for a hosted zone. This operation allows you to enable or disable specific features for your hosted zone, such as accelerated recovery.</p> <p>Accelerated recovery enables you to update DNS records in your public hosted zone even when the us-east-1 region is unavailable.</p>

        Args:
            hosted_zone_id: <p>The ID of the hosted zone for which you want to update features. This is the unique identifier for your hosted zone.</p>
            enable_accelerated_recovery: <p>Specifies whether to enable accelerated recovery for the hosted zone. Set to <code>true</code> to enable accelerated recovery, or <code>false</code> to disable it.</p>

        Raises:
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.limits_exceeded.LimitsExceeded: <p>This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, <a href="http://aws.amazon.com/route53-request">create a case</a> with the Amazon Web Services Support Center.</p>
            capo_route_53.errors.no_such_hosted_zone.NoSuchHostedZone: <p>No hosted zone exists with the ID that you specified.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.update_hosted_zone_features_request.UpdateHostedZoneFeaturesRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.update_hosted_zone_features_response.UpdateHostedZoneFeaturesResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.update_hosted_zone_features

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.update_hosted_zone_features.update_hosted_zone_features(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.update_hosted_zone_features_request.UpdateHostedZoneFeaturesRequest = {
            "hosted_zone_id": hosted_zone_id
        }
        if enable_accelerated_recovery is not None:
            input_["enable_accelerated_recovery"] = enable_accelerated_recovery

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_traffic_policy_comment(
        self,
        id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion",
        comment: "capo_route_53.types.traffic_policy_comment.TrafficPolicyComment",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.update_traffic_policy_comment_response.UpdateTrafficPolicyCommentResponse":
        """<p>Updates the comment for a specified traffic policy version.</p>

        Args:
            id: <p>The value of <code>Id</code> for the traffic policy that you want to update the comment for.</p>
            version: <p>The value of <code>Version</code> for the traffic policy that you want to update the comment for.</p>
            comment: <p>The new comment for the specified traffic policy and version.</p>

        Raises:
            capo_route_53.errors.concurrent_modification.ConcurrentModification: <p>Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.update_traffic_policy_comment_request.UpdateTrafficPolicyCommentRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.update_traffic_policy_comment_response.UpdateTrafficPolicyCommentResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.update_traffic_policy_comment

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.update_traffic_policy_comment.update_traffic_policy_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.update_traffic_policy_comment_request.UpdateTrafficPolicyCommentRequest = {
            "id": id,
            "version": version,
            "comment": comment,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_traffic_policy_instance(
        self,
        id: "capo_route_53.types.traffic_policy_instance_id.TrafficPolicyInstanceId",
        ttl: "capo_route_53.types.ttl.TTL",
        traffic_policy_id: "capo_route_53.types.traffic_policy_id.TrafficPolicyId",
        traffic_policy_version: "capo_route_53.types.traffic_policy_version.TrafficPolicyVersion",
        *,
        config_overrides: Optional[Route53ClientConfig] = None,
    ) -> "capo_route_53.types.update_traffic_policy_instance_response.UpdateTrafficPolicyInstanceResponse":
        """<note> <p>After you submit a <code>UpdateTrafficPolicyInstance</code> request, there's a brief delay while Route 53 creates the resource record sets that are specified in the traffic policy definition. Use <code>GetTrafficPolicyInstance</code> with the <code>id</code> of updated traffic policy instance confirm that the <code>UpdateTrafficPolicyInstance</code> request completed successfully. For more information, see the <code>State</code> response element.</p> </note> <p>Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.</p> <p>When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Route 53 performs the following operations:</p> <ol> <li> <p>Route 53 creates a new group of resource record sets based on the specified traffic policy. This is true regardless of how significant the differences are between the existing resource record sets and the new resource record sets. </p> </li> <li> <p>When all of the new resource record sets have been created, Route 53 starts to respond to DNS queries for the root resource record set name (such as example.com) by using the new resource record sets.</p> </li> <li> <p>Route 53 deletes the old group of resource record sets that are associated with the root resource record set name.</p> </li> </ol>

        Args:
            id: <p>The ID of the traffic policy instance that you want to update.</p>
            ttl: <p>The TTL that you want Amazon Route 53 to assign to all of the updated resource record sets.</p>
            traffic_policy_id: <p>The ID of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.</p>
            traffic_policy_version: <p>The version of the traffic policy that you want Amazon Route 53 to use to update resource record sets for the specified traffic policy instance.</p>

        Raises:
            capo_route_53.errors.conflicting_types.ConflictingTypes: <p>You tried to update a traffic policy instance by using a traffic policy version that has a different DNS type than the current type for the instance. You specified the type in the JSON document in the <code>CreateTrafficPolicy</code> or <code>CreateTrafficPolicyVersion</code>request. </p>
            capo_route_53.errors.invalid_input.InvalidInput: <p>The input is not valid.</p>
            capo_route_53.errors.no_such_traffic_policy.NoSuchTrafficPolicy: <p>No traffic policy exists with the specified ID.</p>
            capo_route_53.errors.no_such_traffic_policy_instance.NoSuchTrafficPolicyInstance: <p>No traffic policy instance exists with the specified ID.</p>
            capo_route_53.errors.prior_request_not_complete.PriorRequestNotComplete: <p>If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an <code>HTTP 400 error</code> (<code>Bad request</code>). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.</p>
            capo_route_53.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route_53.types.update_traffic_policy_instance_request.UpdateTrafficPolicyInstanceRequest]",
        ) -> OperationResponse[
            "capo_route_53.types.update_traffic_policy_instance_response.UpdateTrafficPolicyInstanceResponse"
        ]:
            import capo_route_53._operations.aws_dns_v20130401.update_traffic_policy_instance

            output, http_response = (
                capo_route_53._operations.aws_dns_v20130401.update_traffic_policy_instance.update_traffic_policy_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route_53.types.update_traffic_policy_instance_request.UpdateTrafficPolicyInstanceRequest = {
            "id": id,
            "ttl": ttl,
            "traffic_policy_id": traffic_policy_id,
            "traffic_policy_version": traffic_policy_version,
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

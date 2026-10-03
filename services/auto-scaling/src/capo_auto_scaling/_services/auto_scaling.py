"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScaling_2011_01_01``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_auto_scaling._auth._signers
import capo_auto_scaling._auth._sigv4
from capo_auto_scaling._auth._identity import Credentials
from capo_auto_scaling._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_auto_scaling._auth._zapros_handler import AuthMiddleware
from capo_auto_scaling._pagination import resolve_path as _resolve_path
from capo_auto_scaling._services._aws_config import aws_config
from capo_auto_scaling._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_auto_scaling.types.activities_type
    import capo_auto_scaling.types.activity
    import capo_auto_scaling.types.activity_ids
    import capo_auto_scaling.types.activity_type
    import capo_auto_scaling.types.any_printable_ascii_string_max_len4000
    import capo_auto_scaling.types.ascii_string_max_len255
    import capo_auto_scaling.types.associate_public_ip_address
    import capo_auto_scaling.types.attach_instances_query
    import capo_auto_scaling.types.attach_load_balancer_target_groups_result_type
    import capo_auto_scaling.types.attach_load_balancer_target_groups_type
    import capo_auto_scaling.types.attach_load_balancers_result_type
    import capo_auto_scaling.types.attach_load_balancers_type
    import capo_auto_scaling.types.attach_traffic_sources_result_type
    import capo_auto_scaling.types.attach_traffic_sources_type
    import capo_auto_scaling.types.auto_scaling_group
    import capo_auto_scaling.types.auto_scaling_group_desired_capacity
    import capo_auto_scaling.types.auto_scaling_group_max_size
    import capo_auto_scaling.types.auto_scaling_group_min_size
    import capo_auto_scaling.types.auto_scaling_group_names
    import capo_auto_scaling.types.auto_scaling_group_names_type
    import capo_auto_scaling.types.auto_scaling_groups_type
    import capo_auto_scaling.types.auto_scaling_instance_details
    import capo_auto_scaling.types.auto_scaling_instances_type
    import capo_auto_scaling.types.auto_scaling_notification_types
    import capo_auto_scaling.types.availability_zone_distribution
    import capo_auto_scaling.types.availability_zone_ids
    import capo_auto_scaling.types.availability_zone_ids_limit1
    import capo_auto_scaling.types.availability_zone_impairment_policy
    import capo_auto_scaling.types.availability_zones
    import capo_auto_scaling.types.availability_zones_limit1
    import capo_auto_scaling.types.batch_delete_scheduled_action_answer
    import capo_auto_scaling.types.batch_delete_scheduled_action_type
    import capo_auto_scaling.types.batch_put_scheduled_update_group_action_answer
    import capo_auto_scaling.types.batch_put_scheduled_update_group_action_type
    import capo_auto_scaling.types.block_device_mappings
    import capo_auto_scaling.types.boolean_type
    import capo_auto_scaling.types.cancel_instance_refresh_answer
    import capo_auto_scaling.types.cancel_instance_refresh_type
    import capo_auto_scaling.types.capacity_rebalance_enabled
    import capo_auto_scaling.types.capacity_reservation_specification
    import capo_auto_scaling.types.classic_link_vpc_security_groups
    import capo_auto_scaling.types.client_token
    import capo_auto_scaling.types.complete_lifecycle_action_answer
    import capo_auto_scaling.types.complete_lifecycle_action_type
    import capo_auto_scaling.types.context
    import capo_auto_scaling.types.cooldown
    import capo_auto_scaling.types.create_auto_scaling_group_type
    import capo_auto_scaling.types.create_launch_configuration_type
    import capo_auto_scaling.types.create_or_update_tags_type
    import capo_auto_scaling.types.default_instance_warmup
    import capo_auto_scaling.types.delete_auto_scaling_group_type
    import capo_auto_scaling.types.delete_lifecycle_hook_answer
    import capo_auto_scaling.types.delete_lifecycle_hook_type
    import capo_auto_scaling.types.delete_notification_configuration_type
    import capo_auto_scaling.types.delete_policy_type
    import capo_auto_scaling.types.delete_scheduled_action_type
    import capo_auto_scaling.types.delete_tags_type
    import capo_auto_scaling.types.delete_warm_pool_answer
    import capo_auto_scaling.types.delete_warm_pool_type
    import capo_auto_scaling.types.deletion_protection
    import capo_auto_scaling.types.describe_account_limits_answer
    import capo_auto_scaling.types.describe_adjustment_types_answer
    import capo_auto_scaling.types.describe_auto_scaling_instances_type
    import capo_auto_scaling.types.describe_auto_scaling_notification_types_answer
    import capo_auto_scaling.types.describe_instance_refreshes_answer
    import capo_auto_scaling.types.describe_instance_refreshes_type
    import capo_auto_scaling.types.describe_lifecycle_hook_types_answer
    import capo_auto_scaling.types.describe_lifecycle_hooks_answer
    import capo_auto_scaling.types.describe_lifecycle_hooks_type
    import capo_auto_scaling.types.describe_load_balancer_target_groups_request
    import capo_auto_scaling.types.describe_load_balancer_target_groups_response
    import capo_auto_scaling.types.describe_load_balancers_request
    import capo_auto_scaling.types.describe_load_balancers_response
    import capo_auto_scaling.types.describe_metric_collection_types_answer
    import capo_auto_scaling.types.describe_notification_configurations_answer
    import capo_auto_scaling.types.describe_notification_configurations_type
    import capo_auto_scaling.types.describe_policies_type
    import capo_auto_scaling.types.describe_scaling_activities_type
    import capo_auto_scaling.types.describe_scheduled_actions_type
    import capo_auto_scaling.types.describe_tags_type
    import capo_auto_scaling.types.describe_termination_policy_types_answer
    import capo_auto_scaling.types.describe_traffic_sources_request
    import capo_auto_scaling.types.describe_traffic_sources_response
    import capo_auto_scaling.types.describe_warm_pool_answer
    import capo_auto_scaling.types.describe_warm_pool_type
    import capo_auto_scaling.types.desired_configuration
    import capo_auto_scaling.types.detach_instances_answer
    import capo_auto_scaling.types.detach_instances_query
    import capo_auto_scaling.types.detach_load_balancer_target_groups_result_type
    import capo_auto_scaling.types.detach_load_balancer_target_groups_type
    import capo_auto_scaling.types.detach_load_balancers_result_type
    import capo_auto_scaling.types.detach_load_balancers_type
    import capo_auto_scaling.types.detach_traffic_sources_result_type
    import capo_auto_scaling.types.detach_traffic_sources_type
    import capo_auto_scaling.types.disable_metrics_collection_query
    import capo_auto_scaling.types.ebs_optimized
    import capo_auto_scaling.types.enable_metrics_collection_query
    import capo_auto_scaling.types.enter_standby_answer
    import capo_auto_scaling.types.enter_standby_query
    import capo_auto_scaling.types.estimated_instance_warmup
    import capo_auto_scaling.types.execute_policy_type
    import capo_auto_scaling.types.exit_standby_answer
    import capo_auto_scaling.types.exit_standby_query
    import capo_auto_scaling.types.filters
    import capo_auto_scaling.types.force_delete
    import capo_auto_scaling.types.get_predictive_scaling_forecast_answer
    import capo_auto_scaling.types.get_predictive_scaling_forecast_type
    import capo_auto_scaling.types.health_check_grace_period
    import capo_auto_scaling.types.heartbeat_timeout
    import capo_auto_scaling.types.honor_cooldown
    import capo_auto_scaling.types.include_deleted_groups
    import capo_auto_scaling.types.include_instances
    import capo_auto_scaling.types.instance
    import capo_auto_scaling.types.instance_ids
    import capo_auto_scaling.types.instance_lifecycle_policy
    import capo_auto_scaling.types.instance_maintenance_policy
    import capo_auto_scaling.types.instance_metadata_options
    import capo_auto_scaling.types.instance_monitoring
    import capo_auto_scaling.types.instance_protected
    import capo_auto_scaling.types.instance_refresh_ids
    import capo_auto_scaling.types.instance_reuse_policy
    import capo_auto_scaling.types.launch_configuration
    import capo_auto_scaling.types.launch_configuration_name_type
    import capo_auto_scaling.types.launch_configuration_names
    import capo_auto_scaling.types.launch_configuration_names_type
    import capo_auto_scaling.types.launch_configurations_type
    import capo_auto_scaling.types.launch_instances_request
    import capo_auto_scaling.types.launch_instances_result
    import capo_auto_scaling.types.launch_template_specification
    import capo_auto_scaling.types.lifecycle_action_result
    import capo_auto_scaling.types.lifecycle_action_token
    import capo_auto_scaling.types.lifecycle_hook_names
    import capo_auto_scaling.types.lifecycle_hook_specifications
    import capo_auto_scaling.types.lifecycle_transition
    import capo_auto_scaling.types.load_balancer_names
    import capo_auto_scaling.types.max_group_prepared_capacity
    import capo_auto_scaling.types.max_instance_lifetime
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.metric_scale
    import capo_auto_scaling.types.metrics
    import capo_auto_scaling.types.min_adjustment_magnitude
    import capo_auto_scaling.types.min_adjustment_step
    import capo_auto_scaling.types.mixed_instances_policy
    import capo_auto_scaling.types.notification_configuration
    import capo_auto_scaling.types.notification_target_resource_name
    import capo_auto_scaling.types.operator
    import capo_auto_scaling.types.policies_type
    import capo_auto_scaling.types.policy_arn_type
    import capo_auto_scaling.types.policy_increment
    import capo_auto_scaling.types.policy_names
    import capo_auto_scaling.types.policy_types
    import capo_auto_scaling.types.predictive_scaling_configuration
    import capo_auto_scaling.types.process_names
    import capo_auto_scaling.types.processes_type
    import capo_auto_scaling.types.protected_from_scale_in
    import capo_auto_scaling.types.put_lifecycle_hook_answer
    import capo_auto_scaling.types.put_lifecycle_hook_type
    import capo_auto_scaling.types.put_notification_configuration_type
    import capo_auto_scaling.types.put_scaling_policy_type
    import capo_auto_scaling.types.put_scheduled_update_group_action_type
    import capo_auto_scaling.types.put_warm_pool_answer
    import capo_auto_scaling.types.put_warm_pool_type
    import capo_auto_scaling.types.record_lifecycle_action_heartbeat_answer
    import capo_auto_scaling.types.record_lifecycle_action_heartbeat_type
    import capo_auto_scaling.types.refresh_preferences
    import capo_auto_scaling.types.refresh_strategy
    import capo_auto_scaling.types.requested_capacity
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.retry_strategy
    import capo_auto_scaling.types.rollback_instance_refresh_answer
    import capo_auto_scaling.types.rollback_instance_refresh_type
    import capo_auto_scaling.types.scaling_policy
    import capo_auto_scaling.types.scaling_policy_enabled
    import capo_auto_scaling.types.scaling_process_query
    import capo_auto_scaling.types.scheduled_action_names
    import capo_auto_scaling.types.scheduled_actions_type
    import capo_auto_scaling.types.scheduled_update_group_action
    import capo_auto_scaling.types.scheduled_update_group_action_requests
    import capo_auto_scaling.types.security_groups
    import capo_auto_scaling.types.set_desired_capacity_type
    import capo_auto_scaling.types.set_instance_health_query
    import capo_auto_scaling.types.set_instance_protection_answer
    import capo_auto_scaling.types.set_instance_protection_query
    import capo_auto_scaling.types.should_decrement_desired_capacity
    import capo_auto_scaling.types.should_respect_grace_period
    import capo_auto_scaling.types.skip_zonal_shift_validation
    import capo_auto_scaling.types.spot_price
    import capo_auto_scaling.types.start_instance_refresh_answer
    import capo_auto_scaling.types.start_instance_refresh_type
    import capo_auto_scaling.types.step_adjustments
    import capo_auto_scaling.types.subnet_ids_limit1
    import capo_auto_scaling.types.tag_description
    import capo_auto_scaling.types.tags
    import capo_auto_scaling.types.tags_type
    import capo_auto_scaling.types.target_group_ar_ns
    import capo_auto_scaling.types.target_tracking_configuration
    import capo_auto_scaling.types.terminate_instance_in_auto_scaling_group_type
    import capo_auto_scaling.types.termination_instance_ids
    import capo_auto_scaling.types.termination_policies
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.traffic_sources
    import capo_auto_scaling.types.update_auto_scaling_group_type
    import capo_auto_scaling.types.update_placement_group_param
    import capo_auto_scaling.types.warm_pool_min_size
    import capo_auto_scaling.types.warm_pool_state
    import capo_auto_scaling.types.xml_string
    import capo_auto_scaling.types.xml_string_max_len19
    import capo_auto_scaling.types.xml_string_max_len32
    import capo_auto_scaling.types.xml_string_max_len64
    import capo_auto_scaling.types.xml_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len1600
    import capo_auto_scaling.types.xml_string_max_len5000
    import capo_auto_scaling.types.xml_string_user_data


class AutoScalingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AutoScalingClient:
    """A client for the ``AutoScaling`` service.

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
        self._config = AutoScalingClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AutoScalingClientConfig = config_overrides or {}
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

    def attach_instances(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.instance_ids.InstanceIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> None:
        """<p>Attaches one or more EC2 instances to the specified Auto Scaling group.</p> <p>When you attach instances, Amazon EC2 Auto Scaling increases the desired capacity of the group by the number of instances being attached. If the number of instances being attached plus the desired capacity of the group exceeds the maximum size of the group, the operation fails.</p> <p>If there is a Classic Load Balancer attached to your Auto Scaling group, the instances are also registered with the load balancer. If there are target groups attached to your Auto Scaling group, the instances are also registered with the target groups.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html">Detach or attach instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            instance_ids: <p>The IDs of the instances. You can specify up to 20 instances.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To attach an instance to an Auto Scaling group
            This example attaches the specified instance to the specified Auto Scaling group.

            >>> client.attach_instances(instance_ids=['i-93633f9b'], auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.attach_instances_query.AttachInstancesQuery]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_instances

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_instances.attach_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.attach_instances_query.AttachInstancesQuery = {}
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def attach_load_balancers(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        load_balancer_names: Optional[
            "capo_auto_scaling.types.load_balancer_names.LoadBalancerNames"
        ] = None,
    ) -> "capo_auto_scaling.types.attach_load_balancers_result_type.AttachLoadBalancersResultType":
        """<note> <p>This API operation is superseded by <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html">AttachTrafficSources</a>, which can attach multiple traffic sources types. We recommend using <code>AttachTrafficSources</code> to simplify how you manage traffic sources. However, we continue to support <code>AttachLoadBalancers</code>. You can use both the original <code>AttachLoadBalancers</code> API operation and <code>AttachTrafficSources</code> on the same Auto Scaling group.</p> </note> <p>Attaches one or more Classic Load Balancers to the specified Auto Scaling group. Amazon EC2 Auto Scaling registers the running instances with these Classic Load Balancers.</p> <p>To describe the load balancers for an Auto Scaling group, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancers.html">DescribeLoadBalancers</a> API. To detach a load balancer from the Auto Scaling group, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancers.html">DetachLoadBalancers</a> API.</p> <p>This operation is additive and does not detach existing Classic Load Balancers or target groups from the Auto Scaling group.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html">Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            load_balancer_names: <p>The names of the load balancers. You can specify up to 10 load balancers.</p>

        Raises:
            capo_auto_scaling.errors.instance_refresh_in_progress_fault.InstanceRefreshInProgressFault: <p>The request failed because an active instance refresh already exists for the specified Auto Scaling group.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To attach a load balancer to an Auto Scaling group
            This example attaches the specified load balancer to the specified Auto Scaling group.

            >>> client.attach_load_balancers(auto_scaling_group_name='my-auto-scaling-group', load_balancer_names=['my-load-balancer'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.attach_load_balancers_type.AttachLoadBalancersType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.attach_load_balancers_result_type.AttachLoadBalancersResultType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_load_balancers

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_load_balancers.attach_load_balancers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.attach_load_balancers_type.AttachLoadBalancersType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if load_balancer_names is not None:
            input_["load_balancer_names"] = load_balancer_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def attach_load_balancer_target_groups(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        target_group_ar_ns: Optional[
            "capo_auto_scaling.types.target_group_ar_ns.TargetGroupARNs"
        ] = None,
    ) -> "capo_auto_scaling.types.attach_load_balancer_target_groups_result_type.AttachLoadBalancerTargetGroupsResultType":
        """<note> <p>This API operation is superseded by <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html">AttachTrafficSources</a>, which can attach multiple traffic sources types. We recommend using <code>AttachTrafficSources</code> to simplify how you manage traffic sources. However, we continue to support <code>AttachLoadBalancerTargetGroups</code>. You can use both the original <code>AttachLoadBalancerTargetGroups</code> API operation and <code>AttachTrafficSources</code> on the same Auto Scaling group.</p> </note> <p>Attaches one or more target groups to the specified Auto Scaling group.</p> <p>This operation is used with the following load balancer types: </p> <ul> <li> <p>Application Load Balancer - Operates at the application layer (layer 7) and supports HTTP and HTTPS. </p> </li> <li> <p>Network Load Balancer - Operates at the transport layer (layer 4) and supports TCP, TLS, and UDP. </p> </li> <li> <p>Gateway Load Balancer - Operates at the network layer (layer 3).</p> </li> </ul> <p>To describe the target groups for an Auto Scaling group, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html">DescribeLoadBalancerTargetGroups</a> API. To detach the target group from the Auto Scaling group, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html">DetachLoadBalancerTargetGroups</a> API.</p> <p>This operation is additive and does not detach existing target groups or Classic Load Balancers from the Auto Scaling group.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html">Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            target_group_ar_ns: <p>The Amazon Resource Names (ARNs) of the target groups. You can specify up to 10 target groups. To get the ARN of a target group, use the Elastic Load Balancing <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html">DescribeTargetGroups</a> API operation.</p>

        Raises:
            capo_auto_scaling.errors.instance_refresh_in_progress_fault.InstanceRefreshInProgressFault: <p>The request failed because an active instance refresh already exists for the specified Auto Scaling group.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To attach a target group to an Auto Scaling group
            This example attaches the specified target group to the specified Auto Scaling group.

            >>> client.attach_load_balancer_target_groups(auto_scaling_group_name='my-auto-scaling-group', target_group_ar_ns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.attach_load_balancer_target_groups_type.AttachLoadBalancerTargetGroupsType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.attach_load_balancer_target_groups_result_type.AttachLoadBalancerTargetGroupsResultType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_load_balancer_target_groups

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_load_balancer_target_groups.attach_load_balancer_target_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.attach_load_balancer_target_groups_type.AttachLoadBalancerTargetGroupsType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if target_group_ar_ns is not None:
            input_["target_group_ar_ns"] = target_group_ar_ns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def attach_traffic_sources(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        traffic_sources: Optional[
            "capo_auto_scaling.types.traffic_sources.TrafficSources"
        ] = None,
        skip_zonal_shift_validation: Optional[
            "capo_auto_scaling.types.skip_zonal_shift_validation.SkipZonalShiftValidation"
        ] = None,
    ) -> "capo_auto_scaling.types.attach_traffic_sources_result_type.AttachTrafficSourcesResultType":
        """<p>Attaches one or more traffic sources to the specified Auto Scaling group.</p> <p>You can use any of the following as traffic sources for an Auto Scaling group:</p> <ul> <li> <p>Application Load Balancer</p> </li> <li> <p>Classic Load Balancer</p> </li> <li> <p>Gateway Load Balancer</p> </li> <li> <p>Network Load Balancer</p> </li> <li> <p>VPC Lattice</p> </li> </ul> <p>This operation is additive and does not detach existing traffic sources from the Auto Scaling group. </p> <p>After the operation completes, use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html">DescribeTrafficSources</a> API to return details about the state of the attachments between traffic sources and your Auto Scaling group. To detach a traffic source from the Auto Scaling group, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html">DetachTrafficSources</a> API.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            traffic_sources: <p>The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.</p>
            skip_zonal_shift_validation: <p> If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html">Auto Scaling group zonal shift</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>

        Raises:
            capo_auto_scaling.errors.instance_refresh_in_progress_fault.InstanceRefreshInProgressFault: <p>The request failed because an active instance refresh already exists for the specified Auto Scaling group.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To attach a target group to an Auto Scaling group
            This example attaches the specified target group to the specified Auto Scaling group.

            >>> client.attach_traffic_sources(auto_scaling_group_name='my-auto-scaling-group', traffic_sources=[{'Identifier': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'}])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.attach_traffic_sources_type.AttachTrafficSourcesType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.attach_traffic_sources_result_type.AttachTrafficSourcesResultType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_traffic_sources

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.attach_traffic_sources.attach_traffic_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.attach_traffic_sources_type.AttachTrafficSourcesType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if traffic_sources is not None:
            input_["traffic_sources"] = traffic_sources
        if skip_zonal_shift_validation is not None:
            input_["skip_zonal_shift_validation"] = skip_zonal_shift_validation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_scheduled_action(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scheduled_action_names: Optional[
            "capo_auto_scaling.types.scheduled_action_names.ScheduledActionNames"
        ] = None,
    ) -> "capo_auto_scaling.types.batch_delete_scheduled_action_answer.BatchDeleteScheduledActionAnswer":
        """<p>Deletes one or more scheduled actions for the specified Auto Scaling group.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            scheduled_action_names: <p>The names of the scheduled actions to delete. The maximum number allowed is 50. </p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.batch_delete_scheduled_action_type.BatchDeleteScheduledActionType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.batch_delete_scheduled_action_answer.BatchDeleteScheduledActionAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.batch_delete_scheduled_action

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.batch_delete_scheduled_action.batch_delete_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.batch_delete_scheduled_action_type.BatchDeleteScheduledActionType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if scheduled_action_names is not None:
            input_["scheduled_action_names"] = scheduled_action_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_put_scheduled_update_group_action(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scheduled_update_group_actions: Optional[
            "capo_auto_scaling.types.scheduled_update_group_action_requests.ScheduledUpdateGroupActionRequests"
        ] = None,
    ) -> "capo_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer":
        """<p>Creates or updates one or more scheduled scaling actions for an Auto Scaling group.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            scheduled_update_group_actions: <p>One or more scheduled actions. The maximum number allowed is 50.</p>

        Raises:
            capo_auto_scaling.errors.already_exists_fault.AlreadyExistsFault: <p>You already have an Auto Scaling group or launch configuration with this name.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.batch_put_scheduled_update_group_action_type.BatchPutScheduledUpdateGroupActionType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.batch_put_scheduled_update_group_action_answer.BatchPutScheduledUpdateGroupActionAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.batch_put_scheduled_update_group_action

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.batch_put_scheduled_update_group_action.batch_put_scheduled_update_group_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.batch_put_scheduled_update_group_action_type.BatchPutScheduledUpdateGroupActionType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if scheduled_update_group_actions is not None:
            input_["scheduled_update_group_actions"] = scheduled_update_group_actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_instance_refresh(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        wait_for_transitioning_instances: Optional[
            "capo_auto_scaling.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_auto_scaling.types.cancel_instance_refresh_answer.CancelInstanceRefreshAnswer":
        """<p>Cancels an instance refresh or rollback that is in progress. If an instance refresh or rollback is not in progress, an <code>ActiveInstanceRefreshNotFound</code> error occurs.</p> <p>This operation is part of the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html">instance refresh feature</a> in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.</p> <p>When you cancel an instance refresh, this does not roll back any changes that it made. Use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackInstanceRefresh.html">RollbackInstanceRefresh</a> API to roll back instead.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            wait_for_transitioning_instances: <p>When cancelling an instance refresh, this indicates whether to wait for in-flight launches and terminations to complete. The default is true.</p> <p>When set to false, Amazon EC2 Auto Scaling cancels the instance refresh without waiting for any pending launches or terminations to complete.</p>

        Raises:
            capo_auto_scaling.errors.active_instance_refresh_not_found_fault.ActiveInstanceRefreshNotFoundFault: <p>The request failed because an active instance refresh or rollback for the specified Auto Scaling group was not found.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel an instance refresh
            This example cancels an instance refresh operation in progress.

            >>> client.cancel_instance_refresh(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.cancel_instance_refresh_type.CancelInstanceRefreshType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.cancel_instance_refresh_answer.CancelInstanceRefreshAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.cancel_instance_refresh

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.cancel_instance_refresh.cancel_instance_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.cancel_instance_refresh_type.CancelInstanceRefreshType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if wait_for_transitioning_instances is not None:
            input_["wait_for_transitioning_instances"] = (
                wait_for_transitioning_instances
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def complete_lifecycle_action(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        lifecycle_hook_name: Optional[
            "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.resource_name.ResourceName"
        ] = None,
        lifecycle_action_token: Optional[
            "capo_auto_scaling.types.lifecycle_action_token.LifecycleActionToken"
        ] = None,
        lifecycle_action_result: Optional[
            "capo_auto_scaling.types.lifecycle_action_result.LifecycleActionResult"
        ] = None,
        instance_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
        ] = None,
    ) -> "capo_auto_scaling.types.complete_lifecycle_action_answer.CompleteLifecycleActionAnswer":
        """<p>Completes the lifecycle action for the specified token or instance with the specified result.</p> <p>This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:</p> <ol> <li> <p>(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.</p> </li> <li> <p>(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.</p> </li> <li> <p>(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.</p> </li> <li> <p>Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.</p> </li> <li> <p>If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state.</p> </li> <li> <p> <b>If you finish before the timeout period ends, send a callback by using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html">CompleteLifecycleAction</a> API call.</b> </p> </li> </ol> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/completing-lifecycle-hooks.html">Complete a lifecycle action</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            lifecycle_hook_name: <p>The name of the lifecycle hook.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            lifecycle_action_token: <p>A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.</p>
            lifecycle_action_result: <p>The action for the group to take. You can specify either <code>CONTINUE</code> or <code>ABANDON</code>.</p>
            instance_id: <p>The ID of the instance.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To complete the lifecycle action
            This example notifies Auto Scaling that the specified lifecycle action is complete so that it can finish launching or terminating the instance.

            >>> client.complete_lifecycle_action(lifecycle_hook_name='my-lifecycle-hook', auto_scaling_group_name='my-auto-scaling-group', lifecycle_action_token='bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635', lifecycle_action_result='CONTINUE')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.complete_lifecycle_action_type.CompleteLifecycleActionType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.complete_lifecycle_action_answer.CompleteLifecycleActionAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.complete_lifecycle_action

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.complete_lifecycle_action.complete_lifecycle_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.complete_lifecycle_action_type.CompleteLifecycleActionType = {}
        if lifecycle_hook_name is not None:
            input_["lifecycle_hook_name"] = lifecycle_hook_name
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if lifecycle_action_token is not None:
            input_["lifecycle_action_token"] = lifecycle_action_token
        if lifecycle_action_result is not None:
            input_["lifecycle_action_result"] = lifecycle_action_result
        if instance_id is not None:
            input_["instance_id"] = instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_auto_scaling_group(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        launch_configuration_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        launch_template: Optional[
            "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
        ] = None,
        mixed_instances_policy: Optional[
            "capo_auto_scaling.types.mixed_instances_policy.MixedInstancesPolicy"
        ] = None,
        instance_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
        ] = None,
        min_size: Optional[
            "capo_auto_scaling.types.auto_scaling_group_min_size.AutoScalingGroupMinSize"
        ] = None,
        max_size: Optional[
            "capo_auto_scaling.types.auto_scaling_group_max_size.AutoScalingGroupMaxSize"
        ] = None,
        desired_capacity: Optional[
            "capo_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
        ] = None,
        default_cooldown: Optional["capo_auto_scaling.types.cooldown.Cooldown"] = None,
        availability_zones: Optional[
            "capo_auto_scaling.types.availability_zones.AvailabilityZones"
        ] = None,
        availability_zone_ids: Optional[
            "capo_auto_scaling.types.availability_zone_ids.AvailabilityZoneIds"
        ] = None,
        load_balancer_names: Optional[
            "capo_auto_scaling.types.load_balancer_names.LoadBalancerNames"
        ] = None,
        target_group_ar_ns: Optional[
            "capo_auto_scaling.types.target_group_ar_ns.TargetGroupARNs"
        ] = None,
        health_check_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
        ] = None,
        health_check_grace_period: Optional[
            "capo_auto_scaling.types.health_check_grace_period.HealthCheckGracePeriod"
        ] = None,
        placement_group: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        vpc_zone_identifier: Optional[
            "capo_auto_scaling.types.xml_string_max_len5000.XmlStringMaxLen5000"
        ] = None,
        termination_policies: Optional[
            "capo_auto_scaling.types.termination_policies.TerminationPolicies"
        ] = None,
        new_instances_protected_from_scale_in: Optional[
            "capo_auto_scaling.types.instance_protected.InstanceProtected"
        ] = None,
        capacity_rebalance: Optional[
            "capo_auto_scaling.types.capacity_rebalance_enabled.CapacityRebalanceEnabled"
        ] = None,
        lifecycle_hook_specification_list: Optional[
            "capo_auto_scaling.types.lifecycle_hook_specifications.LifecycleHookSpecifications"
        ] = None,
        deletion_protection: Optional[
            "capo_auto_scaling.types.deletion_protection.DeletionProtection"
        ] = None,
        tags: Optional["capo_auto_scaling.types.tags.Tags"] = None,
        service_linked_role_arn: Optional[
            "capo_auto_scaling.types.resource_name.ResourceName"
        ] = None,
        max_instance_lifetime: Optional[
            "capo_auto_scaling.types.max_instance_lifetime.MaxInstanceLifetime"
        ] = None,
        context: Optional["capo_auto_scaling.types.context.Context"] = None,
        desired_capacity_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        default_instance_warmup: Optional[
            "capo_auto_scaling.types.default_instance_warmup.DefaultInstanceWarmup"
        ] = None,
        traffic_sources: Optional[
            "capo_auto_scaling.types.traffic_sources.TrafficSources"
        ] = None,
        instance_maintenance_policy: Optional[
            "capo_auto_scaling.types.instance_maintenance_policy.InstanceMaintenancePolicy"
        ] = None,
        availability_zone_distribution: Optional[
            "capo_auto_scaling.types.availability_zone_distribution.AvailabilityZoneDistribution"
        ] = None,
        availability_zone_impairment_policy: Optional[
            "capo_auto_scaling.types.availability_zone_impairment_policy.AvailabilityZoneImpairmentPolicy"
        ] = None,
        skip_zonal_shift_validation: Optional[
            "capo_auto_scaling.types.skip_zonal_shift_validation.SkipZonalShiftValidation"
        ] = None,
        capacity_reservation_specification: Optional[
            "capo_auto_scaling.types.capacity_reservation_specification.CapacityReservationSpecification"
        ] = None,
        instance_lifecycle_policy: Optional[
            "capo_auto_scaling.types.instance_lifecycle_policy.InstanceLifecyclePolicy"
        ] = None,
        operator: Optional["capo_auto_scaling.types.operator.Operator"] = None,
    ) -> None:
        """<p> <b>We strongly recommend using a launch template when calling this operation to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.</b> </p> <p>Creates an Auto Scaling group with the specified name and attributes. </p> <p>If you exceed your maximum limit of Auto Scaling groups, the call fails. To query this limit, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> API. For information about updating this limit, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html">Quotas for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>If you're new to Amazon EC2 Auto Scaling, see the introductory tutorials in <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html">Get started with Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Every Auto Scaling group has three size properties (<code>DesiredCapacity</code>, <code>MaxSize</code>, and <code>MinSize</code>). Usually, you set these sizes based on a specific number of instances. However, if you configure a mixed instances policy that defines weights for the instance types, you must specify these sizes with the same units that you use for weighting instances.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group. This name must be unique per Region per account.</p> <p>The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters.</p> <note> <p>You cannot use a colon (:) in the name.</p> </note>
            launch_configuration_name: <p>The name of the launch configuration to use to launch instances. </p> <p>Conditional: You must specify either a launch template (<code>LaunchTemplate</code> or <code>MixedInstancesPolicy</code>) or a launch configuration (<code>LaunchConfigurationName</code> or <code>InstanceId</code>).</p>
            launch_template: <p>Information used to specify the launch template and version to use to launch instances. </p> <p>Conditional: You must specify either a launch template (<code>LaunchTemplate</code> or <code>MixedInstancesPolicy</code>) or a launch configuration (<code>LaunchConfigurationName</code> or <code>InstanceId</code>).</p> <note> <p>The launch template that is specified must be configured for use with an Auto Scaling group. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html">Create a launch template for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> </note>
            mixed_instances_policy: <p>The mixed instances policy. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html">Auto Scaling groups with multiple instance types and purchase options</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. To learn how to prioritize multiple capacity types, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-distribution-segments.html">Use Distribution Segments to target multiple capacity types</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            instance_id: <p>The ID of the instance used to base the launch configuration on. If specified, Amazon EC2 Auto Scaling uses the configuration values from the specified instance to create a new launch configuration. To get the instance ID, use the Amazon EC2 <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html">DescribeInstances</a> API operation. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-from-instance.html">Create an Auto Scaling group using parameters from an existing instance</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            min_size: <p>The minimum size of the group.</p>
            max_size: <p>The maximum size of the group.</p> <note> <p>With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above <code>MaxSize</code> to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above <code>MaxSize</code> by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).</p> </note>
            desired_capacity: <p>The desired capacity is the initial capacity of the Auto Scaling group at the time of its creation and the capacity it attempts to maintain. It can scale beyond this capacity if you configure auto scaling. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity, the default is the minimum size of the group.</p>
            default_cooldown: <p> <i>Only needed if you use simple scaling policies.</i> </p> <p>The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html">Scaling cooldowns for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Default: <code>300</code> seconds</p>
            availability_zones: <p>A list of Availability Zones where instances in the Auto Scaling group can be created. Used for launching into the default VPC subnet in each Availability Zone when not using the <code>VPCZoneIdentifier</code> property, or for attaching a network interface when an existing network interface ID is specified in a launch template.</p>
            availability_zone_ids: <p> A list of Availability Zone IDs where the Auto Scaling group can launch instances. You cannot specify both AvailabilityZones and AvailabilityZoneIds in the same request. </p>
            load_balancer_names: <p>A list of Classic Load Balancers associated with this Auto Scaling group. For Application Load Balancers, Network Load Balancers, and Gateway Load Balancers, specify the <code>TargetGroupARNs</code> property instead.</p>
            target_group_ar_ns: <p>The Amazon Resource Names (ARN) of the Elastic Load Balancing target groups to associate with the Auto Scaling group. Instances are registered as targets with the target groups. The target groups receive incoming traffic and route requests to one or more registered targets. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html">Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            health_check_type: <p>A comma-separated value string of one or more health check types.</p> <p>The valid values are <code>EC2</code>, <code>EBS</code>, <code>ELB</code>, and <code>VPC_LATTICE</code>. <code>EC2</code> is the default health check and cannot be disabled. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html">Health checks for instances in an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Only specify <code>EC2</code> if you must clear a value that was previously set.</p>
            health_check_grace_period: <p>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the <code>InService</code> state. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html">Set the health check grace period for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Default: <code>0</code> seconds</p>
            placement_group: <p>The name of the placement group into which to launch your instances. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">Placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>A <i>cluster</i> placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group. </p> </note>
            vpc_zone_identifier: <p>A comma-separated list of subnet IDs for a virtual private cloud (VPC) where instances in the Auto Scaling group can be created. If you specify <code>VPCZoneIdentifier</code> with <code>AvailabilityZones</code>, the subnets that you specify must reside in those Availability Zones.</p>
            termination_policies: <p>A policy or a list of policies that are used to select the instance to terminate. These policies are executed in the order that you list them. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html">Configure termination policies for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Valid values: <code>Default</code> | <code>AllocationStrategy</code> | <code>ClosestToNextInstanceHour</code> | <code>NewestInstance</code> | <code>OldestInstance</code> | <code>OldestLaunchConfiguration</code> | <code>OldestLaunchTemplate</code> | <code>arn:aws:lambda:region:account-id:function:my-function:my-alias</code> </p>
            new_instances_protected_from_scale_in: <p>Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html">Use instance scale-in protection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            capacity_rebalance: <p>Indicates whether Capacity Rebalancing is enabled. Otherwise, Capacity Rebalancing is disabled. When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of interruption. After launching a new instance, it then terminates an old instance. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html">Use Capacity Rebalancing to handle Amazon EC2 Spot Interruptions</a> in the in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            lifecycle_hook_specification_list: <p>One or more lifecycle hooks to add to the Auto Scaling group before instances are launched.</p>
            deletion_protection: <p> The deletion protection setting for the Auto Scaling group. This setting helps safeguard your Auto Scaling group and its instances by controlling whether the <code>DeleteAutoScalingGroup</code> operation is allowed. When deletion protection is enabled, users cannot delete the Auto Scaling group according to the specified protection level until the setting is changed back to a less restrictive level. </p> <p> The valid values are <code>none</code>, <code>prevent-force-deletion</code>, and <code>prevent-all-deletion</code>. </p> <p> Default: <code>none</code> </p> <p> For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/resource-deletion-protection.html"> Configure deletion protection for your Amazon EC2 Auto Scaling resources</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>
            tags: <p>One or more tags. You can tag your Auto Scaling group and propagate the tags to the Amazon EC2 instances it launches. Tags are not propagated to Amazon EBS volumes. To add tags to Amazon EBS volumes, specify the tags in a launch template but use caution. If the launch template specifies an instance tag with a key that is also specified for the Auto Scaling group, Amazon EC2 Auto Scaling overrides the value of that instance tag with the value specified by the Auto Scaling group. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html">Tag Auto Scaling groups and instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            service_linked_role_arn: <p>The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services service on your behalf. By default, Amazon EC2 Auto Scaling uses a service-linked role named <code>AWSServiceRoleForAutoScaling</code>, which it creates if it does not exist. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html">Service-linked roles</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            max_instance_lifetime: <p>The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html">Replace Auto Scaling instances based on maximum instance lifetime</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            context: <p>Reserved.</p>
            desired_capacity_type: <p>The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports <code>DesiredCapacityType</code> for attribute-based instance type selection only. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html">Create a mixed instances group using attribute-based instance type selection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>By default, Amazon EC2 Auto Scaling specifies <code>units</code>, which translates into number of instances.</p> <p>Valid values: <code>units</code> | <code>vcpu</code> | <code>memory-mib</code> </p>
            default_instance_warmup: <p>The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the <code>InService</code> state. </p> <p>During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html">Set the default instance warmup for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <important> <p>To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, <i>even if it is set to 0 seconds</i>. To remove a value that you previously set, include the property but specify <code>-1</code> for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of <code>0</code> or other nominal value.</p> </important> <p>Default: None </p>
            traffic_sources: <p>The list of traffic sources to attach to this Auto Scaling group. You can use any of the following as traffic sources for an Auto Scaling group: Classic Load Balancer, Application Load Balancer, Gateway Load Balancer, Network Load Balancer, and VPC Lattice.</p>
            instance_maintenance_policy: <p>An instance maintenance policy. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html">Set instance maintenance policy</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            availability_zone_distribution: <p>The instance capacity distribution across Availability Zones.</p>
            availability_zone_impairment_policy: <p> The policy for Availability Zone impairment. </p>
            skip_zonal_shift_validation: <p> If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html">Auto Scaling group zonal shift</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>
            capacity_reservation_specification: <p> The capacity reservation specification for the Auto Scaling group. </p>
            instance_lifecycle_policy: <p> The instance lifecycle policy for the Auto Scaling group. This policy controls instance behavior when an instance transitions through its lifecycle states. Configure retention triggers to specify when instances should move to a <code>Retained</code> state instead of automatic termination. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html"> Control instance retention with instance lifecycle policies</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p> <note> <p>Instances in a Retained state will continue to incur standard EC2 charges until terminated.</p> </note>
            operator: <p>The entity that manages the Auto Scaling group. If you specify this parameter, Amazon EC2 Auto Scaling passes the operator identity to EC2 for instance launches and only allows the designated operator to make changes to the Auto Scaling group. All mutating API calls from non-operator callers are rejected with an <code>AccessDenied</code> exception.</p>

        Raises:
            capo_auto_scaling.errors.already_exists_fault.AlreadyExistsFault: <p>You already have an Auto Scaling group or launch configuration with this name.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an Auto Scaling group with an attached target group
            This example creates an Auto Scaling group and attaches the specified target group.

            >>> client.create_auto_scaling_group(auto_scaling_group_name='my-auto-scaling-group', launch_template={'LaunchTemplateName': 'my-template-for-auto-scaling', 'Version': '$Default'}, min_size=1, max_size=3, target_group_ar_ns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'], health_check_type='ELB', health_check_grace_period=300, vpc_zone_identifier='subnet-057fa0918fEXAMPLE, subnet-610acd08EXAMPLE')
            To create an Auto Scaling group with a mixed instances policy
            This example creates an Auto Scaling group with a mixed instances policy. It specifies the c5.large, c5a.large, and c6g.large instance types and defines a different launch template for the c6g.large instance type.

            >>> client.create_auto_scaling_group(auto_scaling_group_name='my-asg', mixed_instances_policy={'LaunchTemplate': {'LaunchTemplateSpecification': {'LaunchTemplateName': 'my-launch-template-for-x86', 'Version': '$Default'}, 'Overrides': [{'InstanceType': 'c6g.large', 'LaunchTemplateSpecification': {'LaunchTemplateName': 'my-launch-template-for-arm', 'Version': '$Default'}}, {'InstanceType': 'c5.large'}, {'InstanceType': 'c5a.large'}]}, 'InstancesDistribution': {'OnDemandBaseCapacity': 1, 'OnDemandPercentageAboveBaseCapacity': 50, 'SpotAllocationStrategy': 'price-capacity-optimized'}}, min_size=1, max_size=5, desired_capacity=3, vpc_zone_identifier='subnet-057fa0918fEXAMPLE, subnet-610acd08EXAMPLE')
            To create an Auto Scaling group using attribute-based instance type selection
            This example creates an Auto Scaling group using attribute-based instance type selection. It requires the instance types to have a minimum of four vCPUs and a maximum of eight vCPUs, a minimum of 16,384 MiB of memory, and an Intel manufactured CPU.

            >>> client.create_auto_scaling_group(auto_scaling_group_name='my-asg', mixed_instances_policy={'LaunchTemplate': {'LaunchTemplateSpecification': {'LaunchTemplateName': 'my-template-for-auto-scaling', 'Version': '$Default'}, 'Overrides': [{'InstanceRequirements': {'VCpuCount': {'Min': 4, 'Max': 8}, 'MemoryMiB': {'Min': 16384}, 'CpuManufacturers': ['intel']}}]}, 'InstancesDistribution': {'OnDemandPercentageAboveBaseCapacity': 50, 'SpotAllocationStrategy': 'price-capacity-optimized'}}, min_size=0, max_size=100, desired_capacity=4, desired_capacity_type='units', vpc_zone_identifier='subnet-057fa0918fEXAMPLE, subnet-610acd08EXAMPLE')
            To create an Auto Scaling group using Distribution Segments
            This example creates an Auto Scaling group that uses Distribution Segments to prioritize On-Demand Capacity Reservations, Capacity Blocks, interruptible Capacity Reservations, and then On-Demand capacity.

            >>> client.create_auto_scaling_group(auto_scaling_group_name='my-asg', mixed_instances_policy={'LaunchTemplate': {'LaunchTemplateSpecification': {'LaunchTemplateName': 'my-template-for-auto-scaling', 'Version': '$Default'}, 'Overrides': [{'InstanceType': 'm5.24xlarge'}, {'InstanceType': 'p5.48xlarge'}]}, 'InstancesDistribution': {'OnDemandAllocationStrategy': 'prioritized', 'DistributionSegments': [{'TargetCapacityTypes': ['on-demand-capacity-reservation', 'capacity-block', 'interruptible-capacity-reservation', 'on-demand']}]}}, capacity_reservation_specification={'CapacityReservationTarget': {'CapacityReservationResourceGroupArns': ['arn:aws:resource-groups:us-east-1:123456789012:group/my-capacity-reservation-group']}}, min_size=0, max_size=10, desired_capacity=5, vpc_zone_identifier='subnet-057fa0918fEXAMPLE')
            To create an Auto Scaling group
            This example creates an Auto Scaling group.

            >>> client.create_auto_scaling_group(auto_scaling_group_name='my-auto-scaling-group', launch_template={'LaunchTemplateName': 'my-template-for-auto-scaling', 'Version': '$Default'}, min_size=1, max_size=3, max_instance_lifetime=2592000, default_instance_warmup=120, vpc_zone_identifier='subnet-057fa0918fEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.create_auto_scaling_group_type.CreateAutoScalingGroupType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.create_auto_scaling_group

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.create_auto_scaling_group.create_auto_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.create_auto_scaling_group_type.CreateAutoScalingGroupType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if launch_configuration_name is not None:
            input_["launch_configuration_name"] = launch_configuration_name
        if launch_template is not None:
            input_["launch_template"] = launch_template
        if mixed_instances_policy is not None:
            input_["mixed_instances_policy"] = mixed_instances_policy
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if min_size is not None:
            input_["min_size"] = min_size
        if max_size is not None:
            input_["max_size"] = max_size
        if desired_capacity is not None:
            input_["desired_capacity"] = desired_capacity
        if default_cooldown is not None:
            input_["default_cooldown"] = default_cooldown
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if availability_zone_ids is not None:
            input_["availability_zone_ids"] = availability_zone_ids
        if load_balancer_names is not None:
            input_["load_balancer_names"] = load_balancer_names
        if target_group_ar_ns is not None:
            input_["target_group_ar_ns"] = target_group_ar_ns
        if health_check_type is not None:
            input_["health_check_type"] = health_check_type
        if health_check_grace_period is not None:
            input_["health_check_grace_period"] = health_check_grace_period
        if placement_group is not None:
            input_["placement_group"] = placement_group
        if vpc_zone_identifier is not None:
            input_["vpc_zone_identifier"] = vpc_zone_identifier
        if termination_policies is not None:
            input_["termination_policies"] = termination_policies
        if new_instances_protected_from_scale_in is not None:
            input_["new_instances_protected_from_scale_in"] = (
                new_instances_protected_from_scale_in
            )
        if capacity_rebalance is not None:
            input_["capacity_rebalance"] = capacity_rebalance
        if lifecycle_hook_specification_list is not None:
            input_["lifecycle_hook_specification_list"] = (
                lifecycle_hook_specification_list
            )
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if service_linked_role_arn is not None:
            input_["service_linked_role_arn"] = service_linked_role_arn
        if max_instance_lifetime is not None:
            input_["max_instance_lifetime"] = max_instance_lifetime
        if context is not None:
            input_["context"] = context
        if desired_capacity_type is not None:
            input_["desired_capacity_type"] = desired_capacity_type
        if default_instance_warmup is not None:
            input_["default_instance_warmup"] = default_instance_warmup
        if traffic_sources is not None:
            input_["traffic_sources"] = traffic_sources
        if instance_maintenance_policy is not None:
            input_["instance_maintenance_policy"] = instance_maintenance_policy
        if availability_zone_distribution is not None:
            input_["availability_zone_distribution"] = availability_zone_distribution
        if availability_zone_impairment_policy is not None:
            input_["availability_zone_impairment_policy"] = (
                availability_zone_impairment_policy
            )
        if skip_zonal_shift_validation is not None:
            input_["skip_zonal_shift_validation"] = skip_zonal_shift_validation
        if capacity_reservation_specification is not None:
            input_["capacity_reservation_specification"] = (
                capacity_reservation_specification
            )
        if instance_lifecycle_policy is not None:
            input_["instance_lifecycle_policy"] = instance_lifecycle_policy
        if operator is not None:
            input_["operator"] = operator

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_launch_configuration(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        launch_configuration_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        image_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        key_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        security_groups: Optional[
            "capo_auto_scaling.types.security_groups.SecurityGroups"
        ] = None,
        classic_link_vpc_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        classic_link_vpc_security_groups: Optional[
            "capo_auto_scaling.types.classic_link_vpc_security_groups.ClassicLinkVPCSecurityGroups"
        ] = None,
        user_data: Optional[
            "capo_auto_scaling.types.xml_string_user_data.XmlStringUserData"
        ] = None,
        instance_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
        ] = None,
        instance_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        kernel_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        ramdisk_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        block_device_mappings: Optional[
            "capo_auto_scaling.types.block_device_mappings.BlockDeviceMappings"
        ] = None,
        instance_monitoring: Optional[
            "capo_auto_scaling.types.instance_monitoring.InstanceMonitoring"
        ] = None,
        spot_price: Optional["capo_auto_scaling.types.spot_price.SpotPrice"] = None,
        iam_instance_profile: Optional[
            "capo_auto_scaling.types.xml_string_max_len1600.XmlStringMaxLen1600"
        ] = None,
        ebs_optimized: Optional[
            "capo_auto_scaling.types.ebs_optimized.EbsOptimized"
        ] = None,
        associate_public_ip_address: Optional[
            "capo_auto_scaling.types.associate_public_ip_address.AssociatePublicIpAddress"
        ] = None,
        placement_tenancy: Optional[
            "capo_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
        ] = None,
        metadata_options: Optional[
            "capo_auto_scaling.types.instance_metadata_options.InstanceMetadataOptions"
        ] = None,
    ) -> None:
        """<p>Creates a launch configuration.</p> <p>If you exceed your maximum limit of launch configurations, the call fails. To query this limit, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> API. For information about updating this limit, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html">Quotas for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html">Launch configurations</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <note> <p>Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a launch template or a launch configuration. We strongly recommend that you do not use launch configurations. They do not provide full functionality for Amazon EC2 Auto Scaling or Amazon EC2. For information about using launch templates, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html">Launch templates</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> </note>

        Args:
            launch_configuration_name: <p>The name of the launch configuration. This name must be unique per Region per account.</p>
            image_id: <p>The ID of the Amazon Machine Image (AMI) that was assigned during registration. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html">Find a Linux AMI</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you specify <code>InstanceId</code>, an <code>ImageId</code> is not required.</p>
            key_name: <p>The name of the key pair. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html">Amazon EC2 key pairs and Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>
            security_groups: <p>A list that contains the security group IDs to assign to the instances in the Auto Scaling group. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html">Control traffic to your Amazon Web Services resources using security groups</a> in the <i>Amazon Virtual Private Cloud User Guide</i>.</p>
            classic_link_vpc_id: <p>Available for backward compatibility.</p>
            classic_link_vpc_security_groups: <p>Available for backward compatibility.</p>
            user_data: <p>The user data to make available to the launched EC2 instances. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html">Instance metadata and user data</a> (Linux) and <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-metadata.html">Instance metadata and user data</a> (Windows). If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text. User data is limited to 16 KB.</p>
            instance_id: <p>The ID of the instance to use to create the launch configuration. The new launch configuration derives attributes from the instance, except for the block device mapping.</p> <p>To create a launch configuration with a block device mapping or override any other instance attributes, specify them as part of the same request.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html">Create a launch configuration</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            instance_type: <p>Specifies the instance type of the EC2 instance. For information about available instance types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes">Available instance types</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you specify <code>InstanceId</code>, an <code>InstanceType</code> is not required.</p>
            kernel_id: <p>The ID of the kernel associated with the AMI.</p> <note> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html">User provided kernels</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>
            ramdisk_id: <p>The ID of the RAM disk to select.</p> <note> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html">User provided kernels</a> in the <i>Amazon EC2 User Guide</i>.</p> </note>
            block_device_mappings: <p>The block device mapping entries that define the block devices to attach to the instances at launch. By default, the block devices specified in the block device mapping for the AMI are used. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html">Block device mappings</a> in the <i>Amazon EC2 User Guide</i>.</p>
            instance_monitoring: <p>Controls whether instances in this group are launched with detailed (<code>true</code>) or basic (<code>false</code>) monitoring.</p> <p>The default value is <code>true</code> (enabled).</p> <important> <p>When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/latest/userguide/enable-as-instance-metrics.html">Configure monitoring for Auto Scaling instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> </important>
            spot_price: <p>The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot price. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-spot-instances.html">Request Spot Instances for fault-tolerant and flexible applications</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Valid Range: Minimum value of 0.001</p> <note> <p>When you change your maximum price by creating a new launch configuration, running instances will continue to run as long as the maximum price for those running instances is higher than the current Spot price.</p> </note>
            iam_instance_profile: <p>The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html">IAM role for applications that run on Amazon EC2 instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            ebs_optimized: <p>Specifies whether the launch configuration is optimized for EBS I/O (<code>true</code>) or not (<code>false</code>). The optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization is not available with all instance types. Additional fees are incurred when you enable EBS optimization for an instance type that is not EBS-optimized by default. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html">Amazon EBS-optimized instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>The default value is <code>false</code>.</p>
            associate_public_ip_address: <p>Specifies whether to assign a public IPv4 address to the group's instances. If the instance is launched into a default subnet, the default is to assign a public IPv4 address, unless you disabled the option to assign a public IPv4 address on the subnet. If the instance is launched into a nondefault subnet, the default is not to assign a public IPv4 address, unless you enabled the option to assign a public IPv4 address on the subnet.</p> <p>If you specify <code>true</code>, each instance in the Auto Scaling group receives a unique public IPv4 address. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html">Provide network connectivity for your Auto Scaling instances using Amazon VPC</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>If you specify this property, you must specify at least one subnet for <code>VPCZoneIdentifier</code> when you create your group.</p>
            placement_tenancy: <p>The tenancy of the instance, either <code>default</code> or <code>dedicated</code>. An instance with <code>dedicated</code> tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC. To launch dedicated instances into a shared tenancy VPC (a VPC with the instance placement tenancy attribute set to <code>default</code>), you must set the value of this property to <code>dedicated</code>.</p> <p>If you specify <code>PlacementTenancy</code>, you must specify at least one subnet for <code>VPCZoneIdentifier</code> when you create your group.</p> <p>Valid values: <code>default</code> | <code>dedicated</code> </p>
            metadata_options: <p>The metadata options for the instances. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html#launch-configurations-imds">Configure the instance metadata options</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Raises:
            capo_auto_scaling.errors.already_exists_fault.AlreadyExistsFault: <p>You already have an Auto Scaling group or launch configuration with this name.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a launch configuration
            This example creates a launch configuration.

            >>> client.create_launch_configuration(launch_configuration_name='my-launch-config', image_id='ami-12345678', security_groups=['sg-eb2af88e'], instance_type='m3.medium', iam_instance_profile='my-iam-role')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.create_launch_configuration_type.CreateLaunchConfigurationType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.create_launch_configuration

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.create_launch_configuration.create_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.create_launch_configuration_type.CreateLaunchConfigurationType = {}
        if launch_configuration_name is not None:
            input_["launch_configuration_name"] = launch_configuration_name
        if image_id is not None:
            input_["image_id"] = image_id
        if key_name is not None:
            input_["key_name"] = key_name
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if classic_link_vpc_id is not None:
            input_["classic_link_vpc_id"] = classic_link_vpc_id
        if classic_link_vpc_security_groups is not None:
            input_["classic_link_vpc_security_groups"] = (
                classic_link_vpc_security_groups
            )
        if user_data is not None:
            input_["user_data"] = user_data
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if kernel_id is not None:
            input_["kernel_id"] = kernel_id
        if ramdisk_id is not None:
            input_["ramdisk_id"] = ramdisk_id
        if block_device_mappings is not None:
            input_["block_device_mappings"] = block_device_mappings
        if instance_monitoring is not None:
            input_["instance_monitoring"] = instance_monitoring
        if spot_price is not None:
            input_["spot_price"] = spot_price
        if iam_instance_profile is not None:
            input_["iam_instance_profile"] = iam_instance_profile
        if ebs_optimized is not None:
            input_["ebs_optimized"] = ebs_optimized
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if placement_tenancy is not None:
            input_["placement_tenancy"] = placement_tenancy
        if metadata_options is not None:
            input_["metadata_options"] = metadata_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_or_update_tags(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        tags: Optional["capo_auto_scaling.types.tags.Tags"] = None,
    ) -> None:
        """<p>Creates or updates tags for the specified Auto Scaling group.</p> <p>When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html">Tag Auto Scaling groups and instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            tags: <p>One or more tags.</p>

        Raises:
            capo_auto_scaling.errors.already_exists_fault.AlreadyExistsFault: <p>You already have an Auto Scaling group or launch configuration with this name.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.resource_in_use_fault.ResourceInUseFault: <p>The operation can't be performed because the resource is in use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create or update tags for an Auto Scaling group
            This example adds two tags to the specified Auto Scaling group.

            >>> client.create_or_update_tags(tags=[{'ResourceId': 'my-auto-scaling-group', 'ResourceType': 'auto-scaling-group', 'Key': 'Role', 'Value': 'WebServer', 'PropagateAtLaunch': True}, {'ResourceId': 'my-auto-scaling-group', 'ResourceType': 'auto-scaling-group', 'Key': 'Dept', 'Value': 'Research', 'PropagateAtLaunch': True}])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.create_or_update_tags_type.CreateOrUpdateTagsType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.create_or_update_tags

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.create_or_update_tags.create_or_update_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.create_or_update_tags_type.CreateOrUpdateTagsType = {}
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_auto_scaling_group(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        force_delete: Optional[
            "capo_auto_scaling.types.force_delete.ForceDelete"
        ] = None,
    ) -> None:
        """<p>Deletes the specified Auto Scaling group.</p> <p>If the group has instances or scaling activities in progress, you must specify the option to force the deletion in order for it to succeed. The force delete operation will also terminate the EC2 instances. If the group has a warm pool, the force delete option also deletes the warm pool.</p> <p>To remove instances from the Auto Scaling group before deleting it, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachInstances.html">DetachInstances</a> API with the list of instances and the option to decrement the desired capacity. This ensures that Amazon EC2 Auto Scaling does not launch replacement instances.</p> <p>To terminate all instances before deleting the Auto Scaling group, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_UpdateAutoScalingGroup.html">UpdateAutoScalingGroup</a> API and set the minimum size and desired capacity of the Auto Scaling group to zero.</p> <p>If the group has scaling policies, deleting the group deletes the policies, the underlying alarm actions, and any alarm that no longer has an associated action.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html">Delete your Auto Scaling infrastructure</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            force_delete: <p>Specifies that the group is to be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This action also deletes any outstanding lifecycle actions associated with the group.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.resource_in_use_fault.ResourceInUseFault: <p>The operation can't be performed because the resource is in use.</p>
            capo_auto_scaling.errors.scaling_activity_in_progress_fault.ScalingActivityInProgressFault: <p>The operation can't be performed because there are scaling activities in progress.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an Auto Scaling group
            This example deletes the specified Auto Scaling group.

            >>> client.delete_auto_scaling_group(auto_scaling_group_name='my-auto-scaling-group')
            To delete an Auto Scaling group and all its instances
            This example deletes the specified Auto Scaling group and all its instances.

            >>> client.delete_auto_scaling_group(auto_scaling_group_name='my-auto-scaling-group', force_delete=True)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.delete_auto_scaling_group_type.DeleteAutoScalingGroupType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_auto_scaling_group

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_auto_scaling_group.delete_auto_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.delete_auto_scaling_group_type.DeleteAutoScalingGroupType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_launch_configuration(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        launch_configuration_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> None:
        """<p>Deletes the specified launch configuration.</p> <p>The launch configuration must not be attached to an Auto Scaling group. When this call completes, the launch configuration is no longer available for use.</p>

        Args:
            launch_configuration_name: <p>The name of the launch configuration.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.resource_in_use_fault.ResourceInUseFault: <p>The operation can't be performed because the resource is in use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a launch configuration
            This example deletes the specified launch configuration.

            >>> client.delete_launch_configuration(launch_configuration_name='my-launch-config')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.launch_configuration_name_type.LaunchConfigurationNameType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_launch_configuration

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_launch_configuration.delete_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.launch_configuration_name_type.LaunchConfigurationNameType = {}
        if launch_configuration_name is not None:
            input_["launch_configuration_name"] = launch_configuration_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_lifecycle_hook(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        lifecycle_hook_name: Optional[
            "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> (
        "capo_auto_scaling.types.delete_lifecycle_hook_answer.DeleteLifecycleHookAnswer"
    ):
        """<p>Deletes the specified lifecycle hook.</p> <p>If there are any outstanding lifecycle actions, they are completed first (<code>ABANDON</code> for launching instances, <code>CONTINUE</code> for terminating instances).</p>

        Args:
            lifecycle_hook_name: <p>The name of the lifecycle hook.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a lifecycle hook
            This example deletes the specified lifecycle hook.

            >>> client.delete_lifecycle_hook(lifecycle_hook_name='my-lifecycle-hook', auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.delete_lifecycle_hook_type.DeleteLifecycleHookType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.delete_lifecycle_hook_answer.DeleteLifecycleHookAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_lifecycle_hook

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_lifecycle_hook.delete_lifecycle_hook(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.delete_lifecycle_hook_type.DeleteLifecycleHookType = {}
        if lifecycle_hook_name is not None:
            input_["lifecycle_hook_name"] = lifecycle_hook_name
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_notification_configuration(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        topic_arn: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> None:
        """<p>Deletes the specified notification.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon SNS topic.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an Auto Scaling notification
            This example deletes the specified notification from the specified Auto Scaling group.

            >>> client.delete_notification_configuration(auto_scaling_group_name='my-auto-scaling-group', topic_arn='arn:aws:sns:us-west-2:123456789012:my-sns-topic')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.delete_notification_configuration_type.DeleteNotificationConfigurationType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_notification_configuration

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_notification_configuration.delete_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.delete_notification_configuration_type.DeleteNotificationConfigurationType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if topic_arn is not None:
            input_["topic_arn"] = topic_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        policy_name: Optional[
            "capo_auto_scaling.types.resource_name.ResourceName"
        ] = None,
    ) -> None:
        """<p>Deletes the specified scaling policy.</p> <p>Deleting either a step scaling policy or a simple scaling policy deletes the underlying alarm action, but does not delete the alarm, even if it no longer has an associated action.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/deleting-scaling-policy.html">Delete a scaling policy</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            policy_name: <p>The name or Amazon Resource Name (ARN) of the policy.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an Auto Scaling policy
            This example deletes the specified Auto Scaling policy.

            >>> client.delete_policy(auto_scaling_group_name='my-auto-scaling-group', policy_name='my-step-scale-out-policy')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.delete_policy_type.DeletePolicyType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_policy

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.delete_policy_type.DeletePolicyType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if policy_name is not None:
            input_["policy_name"] = policy_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scheduled_action(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scheduled_action_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> None:
        """<p>Deletes the specified scheduled action.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            scheduled_action_name: <p>The name of the action to delete.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a scheduled action from an Auto Scaling group
            This example deletes the specified scheduled action from the specified Auto Scaling group.

            >>> client.delete_scheduled_action(auto_scaling_group_name='my-auto-scaling-group', scheduled_action_name='my-scheduled-action')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.delete_scheduled_action_type.DeleteScheduledActionType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_scheduled_action

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_scheduled_action.delete_scheduled_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.delete_scheduled_action_type.DeleteScheduledActionType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if scheduled_action_name is not None:
            input_["scheduled_action_name"] = scheduled_action_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tags(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        tags: Optional["capo_auto_scaling.types.tags.Tags"] = None,
    ) -> None:
        """<p>Deletes the specified tags.</p>

        Args:
            tags: <p>One or more tags.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.resource_in_use_fault.ResourceInUseFault: <p>The operation can't be performed because the resource is in use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a tag from an Auto Scaling group
            This example deletes the specified tag from the specified Auto Scaling group.

            >>> client.delete_tags(tags=[{'ResourceId': 'my-auto-scaling-group', 'ResourceType': 'auto-scaling-group', 'Key': 'Dept', 'Value': 'Research'}])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.delete_tags_type.DeleteTagsType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_tags

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_tags.delete_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.delete_tags_type.DeleteTagsType = {}
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_warm_pool(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        force_delete: Optional[
            "capo_auto_scaling.types.force_delete.ForceDelete"
        ] = None,
    ) -> "capo_auto_scaling.types.delete_warm_pool_answer.DeleteWarmPoolAnswer":
        """<p>Deletes the warm pool for the specified Auto Scaling group.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html">Warm pools for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            force_delete: <p>Specifies that the warm pool is to be deleted along with all of its associated instances, without waiting for all instances to be terminated. This parameter also deletes any outstanding lifecycle actions associated with the warm pool instances.</p>

        Raises:
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.resource_in_use_fault.ResourceInUseFault: <p>The operation can't be performed because the resource is in use.</p>
            capo_auto_scaling.errors.scaling_activity_in_progress_fault.ScalingActivityInProgressFault: <p>The operation can't be performed because there are scaling activities in progress.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.delete_warm_pool_type.DeleteWarmPoolType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.delete_warm_pool_answer.DeleteWarmPoolAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_warm_pool

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.delete_warm_pool.delete_warm_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.delete_warm_pool_type.DeleteWarmPoolType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account_limits(
        self, *, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> "capo_auto_scaling.types.describe_account_limits_answer.DescribeAccountLimitsAnswer":
        """<p>Describes the current Amazon EC2 Auto Scaling resource quotas for your account.</p> <p>When you establish an Amazon Web Services account, the account has initial quotas on the maximum number of Auto Scaling groups and launch configurations that you can create in a given Region. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html">Quotas for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe your Auto Scaling account limits
            This example describes the Amazon EC2 Auto Scaling service quotas for your account.

            >>> client.describe_account_limits()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_account_limits_answer.DescribeAccountLimitsAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_account_limits

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_account_limits.describe_account_limits(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_adjustment_types(
        self, *, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> "capo_auto_scaling.types.describe_adjustment_types_answer.DescribeAdjustmentTypesAnswer":
        """<p>Describes the available adjustment types for step scaling and simple scaling policies.</p> <p>The following adjustment types are supported:</p> <ul> <li> <p> <code>ChangeInCapacity</code> </p> </li> <li> <p> <code>ExactCapacity</code> </p> </li> <li> <p> <code>PercentChangeInCapacity</code> </p> </li> </ul>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the Amazon EC2 Auto Scaling adjustment types
            This example describes the available adjustment types.

            >>> client.describe_adjustment_types()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_adjustment_types_answer.DescribeAdjustmentTypesAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_adjustment_types

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_adjustment_types.describe_adjustment_types(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_auto_scaling_groups(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_names: Optional[
            "capo_auto_scaling.types.auto_scaling_group_names.AutoScalingGroupNames"
        ] = None,
        include_instances: Optional[
            "capo_auto_scaling.types.include_instances.IncludeInstances"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        filters: Optional["capo_auto_scaling.types.filters.Filters"] = None,
    ) -> "capo_auto_scaling.types.auto_scaling_groups_type.AutoScalingGroupsType":
        """<p>Gets information about the Auto Scaling groups in the account and Region.</p> <p>If you specify Auto Scaling group names, the output includes information for only the specified Auto Scaling groups. If you specify filters, the output includes information for only those Auto Scaling groups that meet the filter criteria. If you do not specify group names or filters, the output includes information for all Auto Scaling groups. </p> <p>This operation also returns information about instances in Auto Scaling groups. To retrieve information about the instances in a warm pool, you must call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html">DescribeWarmPool</a> API. </p>

        Args:
            auto_scaling_group_names: <p>The names of the Auto Scaling groups. By default, you can only specify up to 50 names. You can optionally increase this limit using the <code>MaxRecords</code> property.</p> <p>If you omit this property, all Auto Scaling groups are described.</p>
            include_instances: <p> Specifies whether to include information about Amazon EC2 instances in the response. When set to <code>true</code> (default), the response includes instance details. </p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>
            filters: <p>One or more filters to limit the results based on specific tags. </p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe an Auto Scaling group
            This example describes the specified Auto Scaling group.

            >>> client.describe_auto_scaling_groups(auto_scaling_group_names=['my-auto-scaling-group'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.auto_scaling_group_names_type.AutoScalingGroupNamesType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.auto_scaling_groups_type.AutoScalingGroupsType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_auto_scaling_groups

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_auto_scaling_groups.describe_auto_scaling_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.auto_scaling_group_names_type.AutoScalingGroupNamesType = {}
        if auto_scaling_group_names is not None:
            input_["auto_scaling_group_names"] = auto_scaling_group_names
        if include_instances is not None:
            input_["include_instances"] = include_instances
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_auto_scaling_groups(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_names: Optional[
            "capo_auto_scaling.types.auto_scaling_group_names.AutoScalingGroupNames"
        ] = None,
        include_instances: Optional[
            "capo_auto_scaling.types.include_instances.IncludeInstances"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        filters: Optional["capo_auto_scaling.types.filters.Filters"] = None,
    ) -> "Iterator[capo_auto_scaling.types.auto_scaling_group.AutoScalingGroup]":
        _token = next_token
        while True:
            _response = self.describe_auto_scaling_groups(
                config_overrides=config_overrides,
                auto_scaling_group_names=auto_scaling_group_names,
                include_instances=include_instances,
                next_token=_token,
                max_records=max_records,
                filters=filters,
            )
            _page = _resolve_path(_response, ("auto_scaling_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_auto_scaling_instances(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.instance_ids.InstanceIds"
        ] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
    ) -> "capo_auto_scaling.types.auto_scaling_instances_type.AutoScalingInstancesType":
        """<p>Gets information about the Auto Scaling instances in the account and Region.</p>

        Args:
            instance_ids: <p>The IDs of the instances. If you omit this property, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.</p> <p>Array Members: Maximum number of 50 items.</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>50</code>.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe one or more Auto Scaling instances
            This example describes the specified Auto Scaling instance.

            >>> client.describe_auto_scaling_instances(instance_ids=['i-05b4f7d5be44822a6'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_auto_scaling_instances_type.DescribeAutoScalingInstancesType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.auto_scaling_instances_type.AutoScalingInstancesType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_auto_scaling_instances

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_auto_scaling_instances.describe_auto_scaling_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_auto_scaling_instances_type.DescribeAutoScalingInstancesType = {}
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_auto_scaling_instances(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.instance_ids.InstanceIds"
        ] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
    ) -> "Iterator[capo_auto_scaling.types.auto_scaling_instance_details.AutoScalingInstanceDetails]":
        _token = next_token
        while True:
            _response = self.describe_auto_scaling_instances(
                config_overrides=config_overrides,
                instance_ids=instance_ids,
                max_records=max_records,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("auto_scaling_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_auto_scaling_notification_types(
        self, *, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> "capo_auto_scaling.types.describe_auto_scaling_notification_types_answer.DescribeAutoScalingNotificationTypesAnswer":
        """<p>Describes the notification types that are supported by Amazon EC2 Auto Scaling.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the Auto Scaling notification types
            This example describes the available notification types.

            >>> client.describe_auto_scaling_notification_types()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_auto_scaling_notification_types_answer.DescribeAutoScalingNotificationTypesAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_auto_scaling_notification_types

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_auto_scaling_notification_types.describe_auto_scaling_notification_types(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_instance_refreshes(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        instance_refresh_ids: Optional[
            "capo_auto_scaling.types.instance_refresh_ids.InstanceRefreshIds"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.describe_instance_refreshes_answer.DescribeInstanceRefreshesAnswer":
        """<p>Gets information about the instance refreshes for the specified Auto Scaling group from the previous six weeks.</p> <p>This operation is part of the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html">instance refresh feature</a> in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.</p> <p>To help you determine the status of an instance refresh, Amazon EC2 Auto Scaling returns information about the instance refreshes you previously initiated, including their status, start time, end time, the percentage of the instance refresh that is complete, and the number of instances remaining to update before the instance refresh is complete. If a rollback is initiated while an instance refresh is in progress, Amazon EC2 Auto Scaling also returns information about the rollback of the instance refresh.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            instance_refresh_ids: <p>One or more instance refresh IDs.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_instance_refreshes_type.DescribeInstanceRefreshesType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_instance_refreshes_answer.DescribeInstanceRefreshesAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_instance_refreshes

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_instance_refreshes.describe_instance_refreshes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_instance_refreshes_type.DescribeInstanceRefreshesType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if instance_refresh_ids is not None:
            input_["instance_refresh_ids"] = instance_refresh_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_instance_refreshes(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        instance_refresh_ids: Optional[
            "capo_auto_scaling.types.instance_refresh_ids.InstanceRefreshIds"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.describe_instance_refreshes_answer.DescribeInstanceRefreshesAnswer]":
        _token = next_token
        while True:
            _response = self.describe_instance_refreshes(
                config_overrides=config_overrides,
                auto_scaling_group_name=auto_scaling_group_name,
                instance_refresh_ids=instance_refresh_ids,
                next_token=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_launch_configurations(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        launch_configuration_names: Optional[
            "capo_auto_scaling.types.launch_configuration_names.LaunchConfigurationNames"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.launch_configurations_type.LaunchConfigurationsType":
        """<p>Gets information about the launch configurations in the account and Region.</p>

        Args:
            launch_configuration_names: <p>The launch configuration names. If you omit this property, all launch configurations are described.</p> <p>Array Members: Maximum number of 50 items.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe Auto Scaling launch configurations
            This example describes the specified launch configuration.

            >>> client.describe_launch_configurations(launch_configuration_names=['my-launch-config'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.launch_configuration_names_type.LaunchConfigurationNamesType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.launch_configurations_type.LaunchConfigurationsType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_launch_configurations

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_launch_configurations.describe_launch_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.launch_configuration_names_type.LaunchConfigurationNamesType = {}
        if launch_configuration_names is not None:
            input_["launch_configuration_names"] = launch_configuration_names
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_launch_configurations(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        launch_configuration_names: Optional[
            "capo_auto_scaling.types.launch_configuration_names.LaunchConfigurationNames"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.launch_configuration.LaunchConfiguration]":
        _token = next_token
        while True:
            _response = self.describe_launch_configurations(
                config_overrides=config_overrides,
                launch_configuration_names=launch_configuration_names,
                next_token=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("launch_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_lifecycle_hooks(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        lifecycle_hook_names: Optional[
            "capo_auto_scaling.types.lifecycle_hook_names.LifecycleHookNames"
        ] = None,
    ) -> "capo_auto_scaling.types.describe_lifecycle_hooks_answer.DescribeLifecycleHooksAnswer":
        """<p>Gets information about the lifecycle hooks for the specified Auto Scaling group.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            lifecycle_hook_names: <p>The names of one or more lifecycle hooks. If you omit this property, all lifecycle hooks are described.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe your lifecycle hooks
            This example describes the lifecycle hooks for the specified Auto Scaling group.

            >>> client.describe_lifecycle_hooks(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_lifecycle_hooks_type.DescribeLifecycleHooksType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_lifecycle_hooks_answer.DescribeLifecycleHooksAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_lifecycle_hooks

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_lifecycle_hooks.describe_lifecycle_hooks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_lifecycle_hooks_type.DescribeLifecycleHooksType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if lifecycle_hook_names is not None:
            input_["lifecycle_hook_names"] = lifecycle_hook_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_lifecycle_hook_types(
        self, *, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> "capo_auto_scaling.types.describe_lifecycle_hook_types_answer.DescribeLifecycleHookTypesAnswer":
        """<p>Describes the available types of lifecycle hooks.</p> <p>The following hook types are supported:</p> <ul> <li> <p> <code>autoscaling:EC2_INSTANCE_LAUNCHING</code> </p> </li> <li> <p> <code>autoscaling:EC2_INSTANCE_TERMINATING</code> </p> </li> </ul>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the available types of lifecycle hooks
            This example describes the available lifecycle hook types.

            >>> client.describe_lifecycle_hook_types()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_lifecycle_hook_types_answer.DescribeLifecycleHookTypesAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_lifecycle_hook_types

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_lifecycle_hook_types.describe_lifecycle_hook_types(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_load_balancers(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.describe_load_balancers_response.DescribeLoadBalancersResponse":
        """<note> <p>This API operation is superseded by <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html">DescribeTrafficSources</a>, which can describe multiple traffic sources types. We recommend using <code>DescribeTrafficSources</code> to simplify how you manage traffic sources. However, we continue to support <code>DescribeLoadBalancers</code>. You can use both the original <code>DescribeLoadBalancers</code> API operation and <code>DescribeTrafficSources</code> on the same Auto Scaling group.</p> </note> <p>Gets information about the load balancers for the specified Auto Scaling group.</p> <p>This operation describes only Classic Load Balancers. If you have Application Load Balancers, Network Load Balancers, or Gateway Load Balancers, use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html">DescribeLoadBalancerTargetGroups</a> API instead.</p> <p>To determine the attachment status of the load balancer, use the <code>State</code> element in the response. When you attach a load balancer to an Auto Scaling group, the initial <code>State</code> value is <code>Adding</code>. The state transitions to <code>Added</code> after all Auto Scaling instances are registered with the load balancer. If Elastic Load Balancing health checks are enabled for the Auto Scaling group, the state transitions to <code>InService</code> after at least one Auto Scaling instance passes the health check. When the load balancer is in the <code>InService</code> state, Amazon EC2 Auto Scaling can terminate and replace any instances that are reported as unhealthy. If no registered instances pass the health checks, the load balancer doesn't enter the <code>InService</code> state. </p> <p>Load balancers also have an <code>InService</code> state if you attach them in the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html">CreateAutoScalingGroup</a> API call. If your load balancer state is <code>InService</code>, but it is not working properly, check the scaling activities by calling <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html">DescribeScalingActivities</a> and take any corrective actions necessary.</p> <p>For help with failed health checks, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html">Troubleshooting Amazon EC2 Auto Scaling: Health checks</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html">Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>100</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the load balancers for an Auto Scaling group
            This example describes the load balancers attached to the specified Auto Scaling group.

            >>> client.describe_load_balancers(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_load_balancers_request.DescribeLoadBalancersRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_load_balancers_response.DescribeLoadBalancersResponse"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_load_balancers

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_load_balancers.describe_load_balancers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_load_balancers_request.DescribeLoadBalancersRequest = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_load_balancers(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.describe_load_balancers_response.DescribeLoadBalancersResponse]":
        _token = next_token
        while True:
            _response = self.describe_load_balancers(
                config_overrides=config_overrides,
                auto_scaling_group_name=auto_scaling_group_name,
                next_token=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_load_balancer_target_groups(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.describe_load_balancer_target_groups_response.DescribeLoadBalancerTargetGroupsResponse":
        """<note> <p>This API operation is superseded by <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html">DescribeTrafficSources</a>, which can describe multiple traffic sources types. We recommend using <code>DetachTrafficSources</code> to simplify how you manage traffic sources. However, we continue to support <code>DescribeLoadBalancerTargetGroups</code>. You can use both the original <code>DescribeLoadBalancerTargetGroups</code> API operation and <code>DescribeTrafficSources</code> on the same Auto Scaling group.</p> </note> <p>Gets information about the Elastic Load Balancing target groups for the specified Auto Scaling group.</p> <p>To determine the attachment status of the target group, use the <code>State</code> element in the response. When you attach a target group to an Auto Scaling group, the initial <code>State</code> value is <code>Adding</code>. The state transitions to <code>Added</code> after all Auto Scaling instances are registered with the target group. If Elastic Load Balancing health checks are enabled for the Auto Scaling group, the state transitions to <code>InService</code> after at least one Auto Scaling instance passes the health check. When the target group is in the <code>InService</code> state, Amazon EC2 Auto Scaling can terminate and replace any instances that are reported as unhealthy. If no registered instances pass the health checks, the target group doesn't enter the <code>InService</code> state. </p> <p>Target groups also have an <code>InService</code> state if you attach them in the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html">CreateAutoScalingGroup</a> API call. If your target group state is <code>InService</code>, but it is not working properly, check the scaling activities by calling <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html">DescribeScalingActivities</a> and take any corrective actions necessary.</p> <p>For help with failed health checks, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html">Troubleshooting Amazon EC2 Auto Scaling: Health checks</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html">Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p> <note> <p>You can use this operation to describe target groups that were attached by using <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html">AttachLoadBalancerTargetGroups</a>, but not for target groups that were attached by using <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html">AttachTrafficSources</a>.</p> </note>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>100</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the target groups for an Auto Scaling group
            This example describes the target groups attached to the specified Auto Scaling group.

            >>> client.describe_load_balancer_target_groups(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_load_balancer_target_groups_request.DescribeLoadBalancerTargetGroupsRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_load_balancer_target_groups_response.DescribeLoadBalancerTargetGroupsResponse"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_load_balancer_target_groups

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_load_balancer_target_groups.describe_load_balancer_target_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_load_balancer_target_groups_request.DescribeLoadBalancerTargetGroupsRequest = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_load_balancer_target_groups(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.describe_load_balancer_target_groups_response.DescribeLoadBalancerTargetGroupsResponse]":
        _token = next_token
        while True:
            _response = self.describe_load_balancer_target_groups(
                config_overrides=config_overrides,
                auto_scaling_group_name=auto_scaling_group_name,
                next_token=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_metric_collection_types(
        self, *, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> "capo_auto_scaling.types.describe_metric_collection_types_answer.DescribeMetricCollectionTypesAnswer":
        """<p>Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the Auto Scaling metric collection types
            This example describes the available metric collection types.

            >>> client.describe_metric_collection_types()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_metric_collection_types_answer.DescribeMetricCollectionTypesAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_metric_collection_types

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_metric_collection_types.describe_metric_collection_types(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_notification_configurations(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_names: Optional[
            "capo_auto_scaling.types.auto_scaling_group_names.AutoScalingGroupNames"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.describe_notification_configurations_answer.DescribeNotificationConfigurationsAnswer":
        """<p>Gets information about the Amazon SNS notifications that are configured for one or more Auto Scaling groups.</p>

        Args:
            auto_scaling_group_names: <p>The name of the Auto Scaling group.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe Auto Scaling notification configurations
            This example describes the notification configurations for the specified Auto Scaling group.

            >>> client.describe_notification_configurations(auto_scaling_group_names=['my-auto-scaling-group'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_notification_configurations_type.DescribeNotificationConfigurationsType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_notification_configurations_answer.DescribeNotificationConfigurationsAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_notification_configurations

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_notification_configurations.describe_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_notification_configurations_type.DescribeNotificationConfigurationsType = {}
        if auto_scaling_group_names is not None:
            input_["auto_scaling_group_names"] = auto_scaling_group_names
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_notification_configurations(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_names: Optional[
            "capo_auto_scaling.types.auto_scaling_group_names.AutoScalingGroupNames"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.notification_configuration.NotificationConfiguration]":
        _token = next_token
        while True:
            _response = self.describe_notification_configurations(
                config_overrides=config_overrides,
                auto_scaling_group_names=auto_scaling_group_names,
                next_token=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("notification_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_policies(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        policy_names: Optional[
            "capo_auto_scaling.types.policy_names.PolicyNames"
        ] = None,
        policy_types: Optional[
            "capo_auto_scaling.types.policy_types.PolicyTypes"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.policies_type.PoliciesType":
        """<p>Gets information about the scaling policies in the account and Region.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            policy_names: <p>The names of one or more policies. If you omit this property, all policies are described. If a group name is provided, the results are limited to that group. If you specify an unknown policy name, it is ignored with no error.</p> <p>Array Members: Maximum number of 50 items.</p>
            policy_types: <p>One or more policy types. The valid values are <code>SimpleScaling</code>, <code>StepScaling</code>, <code>TargetTrackingScaling</code>, and <code>PredictiveScaling</code>.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to be returned with each call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe scaling policies
            This example describes the policies for the specified Auto Scaling group.

            >>> client.describe_policies(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_policies_type.DescribePoliciesType]",
        ) -> OperationResponse["capo_auto_scaling.types.policies_type.PoliciesType"]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_policies

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_policies.describe_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_policies_type.DescribePoliciesType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if policy_names is not None:
            input_["policy_names"] = policy_names
        if policy_types is not None:
            input_["policy_types"] = policy_types
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_policies(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        policy_names: Optional[
            "capo_auto_scaling.types.policy_names.PolicyNames"
        ] = None,
        policy_types: Optional[
            "capo_auto_scaling.types.policy_types.PolicyTypes"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.scaling_policy.ScalingPolicy]":
        _token = next_token
        while True:
            _response = self.describe_policies(
                config_overrides=config_overrides,
                auto_scaling_group_name=auto_scaling_group_name,
                policy_names=policy_names,
                policy_types=policy_types,
                next_token=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("scaling_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_scaling_activities(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        activity_ids: Optional[
            "capo_auto_scaling.types.activity_ids.ActivityIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        include_deleted_groups: Optional[
            "capo_auto_scaling.types.include_deleted_groups.IncludeDeletedGroups"
        ] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        filters: Optional["capo_auto_scaling.types.filters.Filters"] = None,
    ) -> "capo_auto_scaling.types.activities_type.ActivitiesType":
        """<p>Gets information about the scaling activities in the account and Region.</p> <p>When scaling events occur, you see a record of the scaling activity in the scaling activities. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html">Verify a scaling activity for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>If the scaling event succeeds, the value of the <code>StatusCode</code> element in the response is <code>Successful</code>. If an attempt to launch instances failed, the <code>StatusCode</code> value is <code>Failed</code> or <code>Cancelled</code> and the <code>StatusMessage</code> element in the response indicates the cause of the failure. For help interpreting the <code>StatusMessage</code>, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html">Troubleshooting Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>

        Args:
            activity_ids: <p> The activity IDs of the desired scaling activities. If unknown activity IDs are requested, they are ignored with no error. Only activities started within the last six weeks can be returned regardless of the activity IDs specified. If other filters are specified with the request, only results matching all filter criteria can be returned. </p> <p>Array Members: Maximum number of 50 IDs.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p> <important> <p> Omitting this property performs an account-wide operation, which can result in slower or timed-out requests. </p> </important>
            include_deleted_groups: <p>Indicates whether to include scaling activity from deleted Auto Scaling groups.</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>100</code> and the maximum value is <code>100</code>.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            filters: <p> One or more filters to limit the results based on specific criteria. The following filters are supported: </p> <ul> <li> <p> <code>StartTimeLowerBound</code> - The earliest scaling activities to return based on the activity start time. Scaling activities with a start time earlier than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified. </p> </li> <li> <p> <code>StartTimeUpperBound</code> - The latest scaling activities to return based on the activity start time. Scaling activities with a start time later than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified. </p> </li> <li> <p> <code>Status</code> - The <code>StatusCode</code> value of the scaling activity. This filter can only be used in combination with the <code>AutoScalingGroupName</code> parameter. For valid <code>StatusCode</code> values, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Activity.html">Activity</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>. </p> </li> </ul> <p> <code>StartTimeLowerBound</code> and <code>StartTimeUpperBound</code> accept ISO 8601 formatted timestamps. Timestamps without a timezone offset are assumed to be UTC. </p> <ul> <li> <p> <code>2000-01-18T08:15:00Z</code> </p> </li> <li> <p> <code>2000-01-18T16:15:00+08:00</code> </p> </li> </ul>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the scaling activities for an Auto Scaling group
            This example describes the scaling activities for the specified Auto Scaling group.

            >>> client.describe_scaling_activities(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_scaling_activities_type.DescribeScalingActivitiesType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.activities_type.ActivitiesType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_scaling_activities

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_scaling_activities.describe_scaling_activities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_scaling_activities_type.DescribeScalingActivitiesType = {}
        if activity_ids is not None:
            input_["activity_ids"] = activity_ids
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if include_deleted_groups is not None:
            input_["include_deleted_groups"] = include_deleted_groups
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_scaling_activities(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        activity_ids: Optional[
            "capo_auto_scaling.types.activity_ids.ActivityIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        include_deleted_groups: Optional[
            "capo_auto_scaling.types.include_deleted_groups.IncludeDeletedGroups"
        ] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        filters: Optional["capo_auto_scaling.types.filters.Filters"] = None,
    ) -> "Iterator[capo_auto_scaling.types.activity.Activity]":
        _token = next_token
        while True:
            _response = self.describe_scaling_activities(
                config_overrides=config_overrides,
                activity_ids=activity_ids,
                auto_scaling_group_name=auto_scaling_group_name,
                include_deleted_groups=include_deleted_groups,
                max_records=max_records,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_scaling_process_types(
        self, *, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> "capo_auto_scaling.types.processes_type.ProcessesType":
        """<p>Describes the scaling process types for use with the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html">ResumeProcesses</a> and <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendProcesses.html">SuspendProcesses</a> APIs.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the Auto Scaling process types
            This example describes the Auto Scaling process types.

            >>> client.describe_scaling_process_types()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse["capo_auto_scaling.types.processes_type.ProcessesType"]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_scaling_process_types

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_scaling_process_types.describe_scaling_process_types(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scheduled_actions(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scheduled_action_names: Optional[
            "capo_auto_scaling.types.scheduled_action_names.ScheduledActionNames"
        ] = None,
        start_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        end_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.scheduled_actions_type.ScheduledActionsType":
        """<p>Gets information about the scheduled actions that haven't run or that have not reached their end time.</p> <p>To describe the scaling activities for scheduled actions that have already run, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html">DescribeScalingActivities</a> API.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            scheduled_action_names: <p>The names of one or more scheduled actions. If you omit this property, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.</p> <p>Array Members: Maximum number of 50 actions.</p>
            start_time: <p>The earliest scheduled start time to return. If scheduled action names are provided, this property is ignored.</p>
            end_time: <p>The latest scheduled start time to return. If scheduled action names are provided, this property is ignored.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe scheduled actions
            This example describes the scheduled actions for the specified Auto Scaling group.

            >>> client.describe_scheduled_actions(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_scheduled_actions_type.DescribeScheduledActionsType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.scheduled_actions_type.ScheduledActionsType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_scheduled_actions

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_scheduled_actions.describe_scheduled_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_scheduled_actions_type.DescribeScheduledActionsType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if scheduled_action_names is not None:
            input_["scheduled_action_names"] = scheduled_action_names
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_scheduled_actions(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scheduled_action_names: Optional[
            "capo_auto_scaling.types.scheduled_action_names.ScheduledActionNames"
        ] = None,
        start_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        end_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.scheduled_update_group_action.ScheduledUpdateGroupAction]":
        _token = next_token
        while True:
            _response = self.describe_scheduled_actions(
                config_overrides=config_overrides,
                auto_scaling_group_name=auto_scaling_group_name,
                scheduled_action_names=scheduled_action_names,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("scheduled_update_group_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_tags(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        filters: Optional["capo_auto_scaling.types.filters.Filters"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.tags_type.TagsType":
        """<p>Describes the specified tags.</p> <p>You can use filters to limit the results. For example, you can query for the tags for a specific Auto Scaling group. You can specify multiple values for a filter. A tag must match at least one of the specified values for it to be included in the results.</p> <p>You can also specify multiple filters. The result includes information for a particular tag only if it matches all the filters. If there's no match, no special message is returned.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html">Tag Auto Scaling groups and instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            filters: <p>One or more filters to scope the tags to return. The maximum number of filters per filter type (for example, <code>auto-scaling-group</code>) is 1000.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe tags
            This example describes the tags for the specified Auto Scaling group.

            >>> client.describe_tags(filters=[{'Values': ['my-auto-scaling-group'], 'Name': 'auto-scaling-group'}])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_tags_type.DescribeTagsType]",
        ) -> OperationResponse["capo_auto_scaling.types.tags_type.TagsType"]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_tags

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_tags.describe_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_tags_type.DescribeTagsType = {}
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_tags(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        filters: Optional["capo_auto_scaling.types.filters.Filters"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.tag_description.TagDescription]":
        _token = next_token
        while True:
            _response = self.describe_tags(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_termination_policy_types(
        self, *, config_overrides: Optional[AutoScalingClientConfig] = None
    ) -> "capo_auto_scaling.types.describe_termination_policy_types_answer.DescribeTerminationPolicyTypesAnswer":
        """<p>Describes the termination policies supported by Amazon EC2 Auto Scaling.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html">Configure termination policies for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe termination policy types
            This example describes the available termination policy types.

            >>> client.describe_termination_policy_types()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_termination_policy_types_answer.DescribeTerminationPolicyTypesAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_termination_policy_types

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_termination_policy_types.describe_termination_policy_types(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_traffic_sources(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        traffic_source_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "capo_auto_scaling.types.describe_traffic_sources_response.DescribeTrafficSourcesResponse":
        """<p>Gets information about the traffic sources for the specified Auto Scaling group.</p> <p>You can optionally provide a traffic source type. If you provide a traffic source type, then the results only include that traffic source type.</p> <p>If you do not provide a traffic source type, then the results include all the traffic sources for the specified Auto Scaling group. </p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            traffic_source_type: <p>The traffic source type that you want to describe.</p> <p>The following lists the valid values:</p> <ul> <li> <p> <code>elb</code> if the traffic source is a Classic Load Balancer.</p> </li> <li> <p> <code>elbv2</code> if the traffic source is a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer.</p> </li> <li> <p> <code>vpc-lattice</code> if the traffic source is VPC Lattice.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_records: <p>The maximum number of items to return with this call. The maximum value is <code>50</code>.</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe the target groups for an Auto Scaling group
            This example describes the target groups attached to the specified Auto Scaling group.

            >>> client.describe_traffic_sources(auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_traffic_sources_request.DescribeTrafficSourcesRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_traffic_sources_response.DescribeTrafficSourcesResponse"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_traffic_sources

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_traffic_sources.describe_traffic_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_traffic_sources_request.DescribeTrafficSourcesRequest = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if traffic_source_type is not None:
            input_["traffic_source_type"] = traffic_source_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_traffic_sources(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        traffic_source_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
    ) -> "Iterator[capo_auto_scaling.types.describe_traffic_sources_response.DescribeTrafficSourcesResponse]":
        _token = next_token
        while True:
            _response = self.describe_traffic_sources(
                config_overrides=config_overrides,
                auto_scaling_group_name=auto_scaling_group_name,
                traffic_source_type=traffic_source_type,
                next_token=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_warm_pool(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
    ) -> "capo_auto_scaling.types.describe_warm_pool_answer.DescribeWarmPoolAnswer":
        """<p>Gets information about a warm pool and its instances.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html">Warm pools for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            max_records: <p>The maximum number of instances to return with this call. The maximum value is <code>50</code>.</p>
            next_token: <p>The token for the next set of instances to return. (You received this token from a previous call.)</p>

        Raises:
            capo_auto_scaling.errors.invalid_next_token.InvalidNextToken: <p>The <code>NextToken</code> value is not valid.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.describe_warm_pool_type.DescribeWarmPoolType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.describe_warm_pool_answer.DescribeWarmPoolAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_warm_pool

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.describe_warm_pool.describe_warm_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.describe_warm_pool_type.DescribeWarmPoolType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_warm_pool(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        max_records: Optional["capo_auto_scaling.types.max_records.MaxRecords"] = None,
        next_token: Optional["capo_auto_scaling.types.xml_string.XmlString"] = None,
    ) -> "Iterator[capo_auto_scaling.types.instance.Instance]":
        _token = next_token
        while True:
            _response = self.describe_warm_pool(
                config_overrides=config_overrides,
                auto_scaling_group_name=auto_scaling_group_name,
                max_records=max_records,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def detach_instances(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.instance_ids.InstanceIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        should_decrement_desired_capacity: Optional[
            "capo_auto_scaling.types.should_decrement_desired_capacity.ShouldDecrementDesiredCapacity"
        ] = None,
    ) -> "capo_auto_scaling.types.detach_instances_answer.DetachInstancesAnswer":
        """<p>Removes one or more instances from the specified Auto Scaling group.</p> <p>After the instances are detached, you can manage them independent of the Auto Scaling group.</p> <p>If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are detached.</p> <p>If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html">Detach or attach instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            instance_ids: <p>The IDs of the instances. You can specify up to 20 instances.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            should_decrement_desired_capacity: <p>Indicates whether the Auto Scaling group decrements the desired capacity value by the number of instances detached.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detach an instance from an Auto Scaling group
            This example detaches the specified instance from the specified Auto Scaling group.

            >>> client.detach_instances(instance_ids=['i-93633f9b'], auto_scaling_group_name='my-auto-scaling-group', should_decrement_desired_capacity=True)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.detach_instances_query.DetachInstancesQuery]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.detach_instances_answer.DetachInstancesAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_instances

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_instances.detach_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.detach_instances_query.DetachInstancesQuery = {}
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if should_decrement_desired_capacity is not None:
            input_["should_decrement_desired_capacity"] = (
                should_decrement_desired_capacity
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detach_load_balancers(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        load_balancer_names: Optional[
            "capo_auto_scaling.types.load_balancer_names.LoadBalancerNames"
        ] = None,
    ) -> "capo_auto_scaling.types.detach_load_balancers_result_type.DetachLoadBalancersResultType":
        """<note> <p>This API operation is superseded by <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html">DetachTrafficSources</a>, which can detach multiple traffic sources types. We recommend using <code>DetachTrafficSources</code> to simplify how you manage traffic sources. However, we continue to support <code>DetachLoadBalancers</code>. You can use both the original <code>DetachLoadBalancers</code> API operation and <code>DetachTrafficSources</code> on the same Auto Scaling group.</p> </note> <p>Detaches one or more Classic Load Balancers from the specified Auto Scaling group.</p> <p>This operation detaches only Classic Load Balancers. If you have Application Load Balancers, Network Load Balancers, or Gateway Load Balancers, use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html">DetachLoadBalancerTargetGroups</a> API instead.</p> <p>When you detach a load balancer, it enters the <code>Removing</code> state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancers.html">DescribeLoadBalancers</a> API call. The instances remain running.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            load_balancer_names: <p>The names of the load balancers. You can specify up to 10 load balancers.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detach a load balancer from an Auto Scaling group
            This example detaches the specified load balancer from the specified Auto Scaling group.

            >>> client.detach_load_balancers(auto_scaling_group_name='my-auto-scaling-group', load_balancer_names=['my-load-balancer'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.detach_load_balancers_type.DetachLoadBalancersType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.detach_load_balancers_result_type.DetachLoadBalancersResultType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_load_balancers

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_load_balancers.detach_load_balancers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.detach_load_balancers_type.DetachLoadBalancersType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if load_balancer_names is not None:
            input_["load_balancer_names"] = load_balancer_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detach_load_balancer_target_groups(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        target_group_ar_ns: Optional[
            "capo_auto_scaling.types.target_group_ar_ns.TargetGroupARNs"
        ] = None,
    ) -> "capo_auto_scaling.types.detach_load_balancer_target_groups_result_type.DetachLoadBalancerTargetGroupsResultType":
        """<note> <p>This API operation is superseded by <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html">DetachTrafficSources</a>, which can detach multiple traffic sources types. We recommend using <code>DetachTrafficSources</code> to simplify how you manage traffic sources. However, we continue to support <code>DetachLoadBalancerTargetGroups</code>. You can use both the original <code>DetachLoadBalancerTargetGroups</code> API operation and <code>DetachTrafficSources</code> on the same Auto Scaling group.</p> </note> <p>Detaches one or more target groups from the specified Auto Scaling group.</p> <p>When you detach a target group, it enters the <code>Removing</code> state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the target group using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html">DescribeLoadBalancerTargetGroups</a> API call. The instances remain running.</p> <note> <p>You can use this operation to detach target groups that were attached by using <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html">AttachLoadBalancerTargetGroups</a>, but not for target groups that were attached by using <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html">AttachTrafficSources</a>.</p> </note>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            target_group_ar_ns: <p>The Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detach a target group from an Auto Scaling group
            This example detaches the specified target group from the specified Auto Scaling group

            >>> client.detach_load_balancer_target_groups(auto_scaling_group_name='my-auto-scaling-group', target_group_ar_ns=['arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.detach_load_balancer_target_groups_type.DetachLoadBalancerTargetGroupsType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.detach_load_balancer_target_groups_result_type.DetachLoadBalancerTargetGroupsResultType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_load_balancer_target_groups

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_load_balancer_target_groups.detach_load_balancer_target_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.detach_load_balancer_target_groups_type.DetachLoadBalancerTargetGroupsType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if target_group_ar_ns is not None:
            input_["target_group_ar_ns"] = target_group_ar_ns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detach_traffic_sources(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        traffic_sources: Optional[
            "capo_auto_scaling.types.traffic_sources.TrafficSources"
        ] = None,
    ) -> "capo_auto_scaling.types.detach_traffic_sources_result_type.DetachTrafficSourcesResultType":
        """<p>Detaches one or more traffic sources from the specified Auto Scaling group.</p> <p>When you detach a traffic source, it enters the <code>Removing</code> state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the traffic source using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html">DescribeTrafficSources</a> API call. The instances continue to run.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            traffic_sources: <p>The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To detach a target group from an Auto Scaling group
            This example detaches the specified target group from the specified Auto Scaling group.

            >>> client.detach_traffic_sources(auto_scaling_group_name='my-auto-scaling-group', traffic_sources=[{'Identifier': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'}])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.detach_traffic_sources_type.DetachTrafficSourcesType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.detach_traffic_sources_result_type.DetachTrafficSourcesResultType"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_traffic_sources

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.detach_traffic_sources.detach_traffic_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.detach_traffic_sources_type.DetachTrafficSourcesType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if traffic_sources is not None:
            input_["traffic_sources"] = traffic_sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_metrics_collection(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        metrics: Optional["capo_auto_scaling.types.metrics.Metrics"] = None,
    ) -> None:
        """<p>Disables group metrics collection for the specified Auto Scaling group.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            metrics: <p>Identifies the metrics to disable.</p> <p>You can specify one or more of the following metrics:</p> <ul> <li> <p> <code>GroupMinSize</code> </p> </li> <li> <p> <code>GroupMaxSize</code> </p> </li> <li> <p> <code>GroupDesiredCapacity</code> </p> </li> <li> <p> <code>GroupInServiceInstances</code> </p> </li> <li> <p> <code>GroupPendingInstances</code> </p> </li> <li> <p> <code>GroupStandbyInstances</code> </p> </li> <li> <p> <code>GroupTerminatingInstances</code> </p> </li> <li> <p> <code>GroupTotalInstances</code> </p> </li> <li> <p> <code>GroupInServiceCapacity</code> </p> </li> <li> <p> <code>GroupPendingCapacity</code> </p> </li> <li> <p> <code>GroupStandbyCapacity</code> </p> </li> <li> <p> <code>GroupTerminatingCapacity</code> </p> </li> <li> <p> <code>GroupTotalCapacity</code> </p> </li> <li> <p> <code>WarmPoolDesiredCapacity</code> </p> </li> <li> <p> <code>WarmPoolWarmedCapacity</code> </p> </li> <li> <p> <code>WarmPoolPendingCapacity</code> </p> </li> <li> <p> <code>WarmPoolTerminatingCapacity</code> </p> </li> <li> <p> <code>WarmPoolTotalCapacity</code> </p> </li> <li> <p> <code>GroupAndWarmPoolDesiredCapacity</code> </p> </li> <li> <p> <code>GroupAndWarmPoolTotalCapacity</code> </p> </li> </ul> <p>If you omit this property, all metrics are disabled.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html">Amazon CloudWatch metrics for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disable metrics collection for an Auto Scaling group
            This example disables collecting data for the GroupDesiredCapacity metric for the specified Auto Scaling group.

            >>> client.disable_metrics_collection(auto_scaling_group_name='my-auto-scaling-group', metrics=['GroupDesiredCapacity'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.disable_metrics_collection_query.DisableMetricsCollectionQuery]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.disable_metrics_collection

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.disable_metrics_collection.disable_metrics_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.disable_metrics_collection_query.DisableMetricsCollectionQuery = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if metrics is not None:
            input_["metrics"] = metrics

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_metrics_collection(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        metrics: Optional["capo_auto_scaling.types.metrics.Metrics"] = None,
        granularity: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> None:
        """<p>Enables group metrics collection for the specified Auto Scaling group.</p> <p>You can use these metrics to track changes in an Auto Scaling group and to set alarms on threshold values. You can view group metrics using the Amazon EC2 Auto Scaling console or the CloudWatch console. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html">Monitor CloudWatch metrics for your Auto Scaling groups and instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            metrics: <p>Identifies the metrics to enable.</p> <p>You can specify one or more of the following metrics:</p> <ul> <li> <p> <code>GroupMinSize</code> </p> </li> <li> <p> <code>GroupMaxSize</code> </p> </li> <li> <p> <code>GroupDesiredCapacity</code> </p> </li> <li> <p> <code>GroupInServiceInstances</code> </p> </li> <li> <p> <code>GroupPendingInstances</code> </p> </li> <li> <p> <code>GroupStandbyInstances</code> </p> </li> <li> <p> <code>GroupTerminatingInstances</code> </p> </li> <li> <p> <code>GroupTotalInstances</code> </p> </li> <li> <p> <code>GroupInServiceCapacity</code> </p> </li> <li> <p> <code>GroupPendingCapacity</code> </p> </li> <li> <p> <code>GroupStandbyCapacity</code> </p> </li> <li> <p> <code>GroupTerminatingCapacity</code> </p> </li> <li> <p> <code>GroupTotalCapacity</code> </p> </li> <li> <p> <code>WarmPoolDesiredCapacity</code> </p> </li> <li> <p> <code>WarmPoolWarmedCapacity</code> </p> </li> <li> <p> <code>WarmPoolPendingCapacity</code> </p> </li> <li> <p> <code>WarmPoolTerminatingCapacity</code> </p> </li> <li> <p> <code>WarmPoolTotalCapacity</code> </p> </li> <li> <p> <code>GroupAndWarmPoolDesiredCapacity</code> </p> </li> <li> <p> <code>GroupAndWarmPoolTotalCapacity</code> </p> </li> </ul> <p>If you specify <code>Granularity</code> and don't specify any metrics, all metrics are enabled.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html">Amazon CloudWatch metrics for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            granularity: <p>The frequency at which Amazon EC2 Auto Scaling sends aggregated data to CloudWatch. The only valid value is <code>1Minute</code>.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable metrics collection for an Auto Scaling group
            This example enables data collection for the specified Auto Scaling group.

            >>> client.enable_metrics_collection(auto_scaling_group_name='my-auto-scaling-group', granularity='1Minute')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.enable_metrics_collection_query.EnableMetricsCollectionQuery]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.enable_metrics_collection

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.enable_metrics_collection.enable_metrics_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.enable_metrics_collection_query.EnableMetricsCollectionQuery = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if metrics is not None:
            input_["metrics"] = metrics
        if granularity is not None:
            input_["granularity"] = granularity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enter_standby(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.instance_ids.InstanceIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        should_decrement_desired_capacity: Optional[
            "capo_auto_scaling.types.should_decrement_desired_capacity.ShouldDecrementDesiredCapacity"
        ] = None,
    ) -> "capo_auto_scaling.types.enter_standby_answer.EnterStandbyAnswer":
        """<p>Moves the specified instances into the standby state.</p> <p>If you choose to decrement the desired capacity of the Auto Scaling group, the instances can enter standby as long as the desired capacity of the Auto Scaling group after the instances are placed into standby is equal to or greater than the minimum capacity of the group.</p> <p>If you choose not to decrement the desired capacity of the Auto Scaling group, the Auto Scaling group launches new instances to replace the instances on standby.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html">Temporarily removing instances from your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            instance_ids: <p>The IDs of the instances. You can specify up to 20 instances.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            should_decrement_desired_capacity: <p>Indicates whether to decrement the desired capacity of the Auto Scaling group by the number of instances moved to <code>Standby</code> mode.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To move instances into standby mode
            This example puts the specified instance into standby mode.

            >>> client.enter_standby(instance_ids=['i-93633f9b'], auto_scaling_group_name='my-auto-scaling-group', should_decrement_desired_capacity=True)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.enter_standby_query.EnterStandbyQuery]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.enter_standby_answer.EnterStandbyAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.enter_standby

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.enter_standby.enter_standby(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.enter_standby_query.EnterStandbyQuery = {}
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if should_decrement_desired_capacity is not None:
            input_["should_decrement_desired_capacity"] = (
                should_decrement_desired_capacity
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_policy(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        policy_name: Optional[
            "capo_auto_scaling.types.resource_name.ResourceName"
        ] = None,
        honor_cooldown: Optional[
            "capo_auto_scaling.types.honor_cooldown.HonorCooldown"
        ] = None,
        metric_value: Optional[
            "capo_auto_scaling.types.metric_scale.MetricScale"
        ] = None,
        breach_threshold: Optional[
            "capo_auto_scaling.types.metric_scale.MetricScale"
        ] = None,
    ) -> None:
        """<p>Executes the specified policy. This can be useful for testing the design of your scaling policy.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            policy_name: <p>The name or ARN of the policy.</p>
            honor_cooldown: <p>Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before executing the policy.</p> <p>Valid only if the policy type is <code>SimpleScaling</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html">Scaling cooldowns for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            metric_value: <p>The metric value to compare to <code>BreachThreshold</code>. This enables you to execute a policy of type <code>StepScaling</code> and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.</p> <p>If you specify a metric value that doesn't correspond to a step adjustment for the policy, the call returns an error.</p> <p>Required if the policy type is <code>StepScaling</code> and not supported otherwise.</p>
            breach_threshold: <p>The breach threshold for the alarm.</p> <p>Required if the policy type is <code>StepScaling</code> and not supported otherwise.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.scaling_activity_in_progress_fault.ScalingActivityInProgressFault: <p>The operation can't be performed because there are scaling activities in progress.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To execute a scaling policy
            This example executes the specified policy.

            >>> client.execute_policy(auto_scaling_group_name='my-auto-scaling-group', policy_name='my-step-scale-out-policy', breach_threshold=50.0, metric_value=59.0)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.execute_policy_type.ExecutePolicyType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.execute_policy

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.execute_policy.execute_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.execute_policy_type.ExecutePolicyType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if honor_cooldown is not None:
            input_["honor_cooldown"] = honor_cooldown
        if metric_value is not None:
            input_["metric_value"] = metric_value
        if breach_threshold is not None:
            input_["breach_threshold"] = breach_threshold

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def exit_standby(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.instance_ids.InstanceIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> "capo_auto_scaling.types.exit_standby_answer.ExitStandbyAnswer":
        """<p>Moves the specified instances out of the standby state.</p> <p>After you put the instances back in service, the desired capacity is incremented.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html">Temporarily removing instances from your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            instance_ids: <p>The IDs of the instances. You can specify up to 20 instances.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To move instances out of standby mode
            This example moves the specified instance out of standby mode.

            >>> client.exit_standby(instance_ids=['i-93633f9b'], auto_scaling_group_name='my-auto-scaling-group')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.exit_standby_query.ExitStandbyQuery]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.exit_standby_answer.ExitStandbyAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.exit_standby

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.exit_standby.exit_standby(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.exit_standby_query.ExitStandbyQuery = {}
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_predictive_scaling_forecast(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        policy_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        start_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        end_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
    ) -> "capo_auto_scaling.types.get_predictive_scaling_forecast_answer.GetPredictiveScalingForecastAnswer":
        """<p>Retrieves the forecast data for a predictive scaling policy.</p> <p>Load forecasts are predictions of the hourly load values using historical load data from CloudWatch and an analysis of historical trends. Capacity forecasts are represented as predicted values for the minimum capacity that is needed on an hourly basis, based on the hourly load forecast.</p> <p>A minimum of 24 hours of data is required to create the initial forecasts. However, having a full 14 days of historical data results in more accurate forecasts.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html">Predictive scaling for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            policy_name: <p>The name of the policy.</p>
            start_time: <p>The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time.</p>
            end_time: <p>The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days. </p> <p>Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. Amazon EC2 Auto Scaling only issues forecasts for periods of two days in advance.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.get_predictive_scaling_forecast_type.GetPredictiveScalingForecastType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.get_predictive_scaling_forecast_answer.GetPredictiveScalingForecastAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.get_predictive_scaling_forecast

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.get_predictive_scaling_forecast.get_predictive_scaling_forecast(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.get_predictive_scaling_forecast_type.GetPredictiveScalingForecastType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def launch_instances(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        requested_capacity: Optional[
            "capo_auto_scaling.types.requested_capacity.RequestedCapacity"
        ] = None,
        client_token: Optional[
            "capo_auto_scaling.types.client_token.ClientToken"
        ] = None,
        availability_zones: Optional[
            "capo_auto_scaling.types.availability_zones_limit1.AvailabilityZonesLimit1"
        ] = None,
        availability_zone_ids: Optional[
            "capo_auto_scaling.types.availability_zone_ids_limit1.AvailabilityZoneIdsLimit1"
        ] = None,
        subnet_ids: Optional[
            "capo_auto_scaling.types.subnet_ids_limit1.SubnetIdsLimit1"
        ] = None,
        retry_strategy: Optional[
            "capo_auto_scaling.types.retry_strategy.RetryStrategy"
        ] = None,
    ) -> "capo_auto_scaling.types.launch_instances_result.LaunchInstancesResult":
        """<p> Launches a specified number of instances in an Auto Scaling group. Returns instance IDs and other details if launch is successful or error details if launch is unsuccessful. </p>

        Args:
            auto_scaling_group_name: <p> The name of the Auto Scaling group to launch instances into. </p>
            requested_capacity: <p> The number of instances to launch. Although this value can exceed 100 for instance weights, the actual instance count is limited to 100 instances per launch. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            availability_zones: <p> The Availability Zones for the instance launch. Must match or be included in the Auto Scaling group's Availability Zone configuration. Either <code>AvailabilityZones</code> or <code>SubnetIds</code> must be specified for groups with multiple Availability Zone configurations. </p>
            availability_zone_ids: <p> A list of Availability Zone IDs where instances should be launched. Must match or be included in the group's AZ configuration. You cannot specify both AvailabilityZones and AvailabilityZoneIds. Required for multi-AZ groups, optional for single-AZ groups. </p>
            subnet_ids: <p> The subnet IDs for the instance launch. Either <code>AvailabilityZones</code> or <code>SubnetIds</code> must be specified. If both are specified, the subnets must reside in the specified Availability Zones. </p>
            retry_strategy: <p> Specifies whether to retry asynchronously if the synchronous launch fails. Valid values are NONE (default, no async retry) and RETRY_WITH_GROUP_CONFIGURATION (increase desired capacity and retry with group configuration). </p>

        Raises:
            capo_auto_scaling.errors.idempotent_call_in_progress_fault.IdempotentCallInProgressFault: <p> The service is currently processing another request with the same client token. Retry the request with the same client token—the in-flight operation will complete and return its result. </p>
            capo_auto_scaling.errors.idempotent_parameter_mismatch_error.IdempotentParameterMismatchError: <p> Indicates that the parameters in the current request do not match the parameters from a previous request with the same client token within the idempotency window. </p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.launch_instances_request.LaunchInstancesRequest]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.launch_instances_result.LaunchInstancesResult"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.launch_instances

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.launch_instances.launch_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.launch_instances_request.LaunchInstancesRequest = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if requested_capacity is not None:
            input_["requested_capacity"] = requested_capacity
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if availability_zone_ids is not None:
            input_["availability_zone_ids"] = availability_zone_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if retry_strategy is not None:
            input_["retry_strategy"] = retry_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_lifecycle_hook(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        lifecycle_hook_name: Optional[
            "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        lifecycle_transition: Optional[
            "capo_auto_scaling.types.lifecycle_transition.LifecycleTransition"
        ] = None,
        role_arn: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        notification_target_arn: Optional[
            "capo_auto_scaling.types.notification_target_resource_name.NotificationTargetResourceName"
        ] = None,
        notification_metadata: Optional[
            "capo_auto_scaling.types.any_printable_ascii_string_max_len4000.AnyPrintableAsciiStringMaxLen4000"
        ] = None,
        heartbeat_timeout: Optional[
            "capo_auto_scaling.types.heartbeat_timeout.HeartbeatTimeout"
        ] = None,
        default_result: Optional[
            "capo_auto_scaling.types.lifecycle_action_result.LifecycleActionResult"
        ] = None,
    ) -> "capo_auto_scaling.types.put_lifecycle_hook_answer.PutLifecycleHookAnswer":
        """<p>Creates or updates a lifecycle hook for the specified Auto Scaling group.</p> <p>Lifecycle hooks let you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.</p> <p>This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:</p> <ol> <li> <p>(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.</p> </li> <li> <p>(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.</p> </li> <li> <p>(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.</p> </li> <li> <p> <b>Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.</b> </p> </li> <li> <p>If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RecordLifecycleActionHeartbeat.html">RecordLifecycleActionHeartbeat</a> API call.</p> </li> <li> <p>If you finish before the timeout period ends, send a callback by using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html">CompleteLifecycleAction</a> API call.</p> </li> </ol> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html">Amazon EC2 Auto Scaling lifecycle hooks</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails.</p> <p>You can view the lifecycle hooks for an Auto Scaling group using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHooks.html">DescribeLifecycleHooks</a> API call. If you are no longer using a lifecycle hook, you can delete it by calling the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteLifecycleHook.html">DeleteLifecycleHook</a> API.</p>

        Args:
            lifecycle_hook_name: <p>The name of the lifecycle hook.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            lifecycle_transition: <p>The lifecycle transition. For Auto Scaling groups, there are two major lifecycle transitions.</p> <ul> <li> <p>To create a lifecycle hook for scale-out events, specify <code>autoscaling:EC2_INSTANCE_LAUNCHING</code>.</p> </li> <li> <p>To create a lifecycle hook for scale-in events, specify <code>autoscaling:EC2_INSTANCE_TERMINATING</code>.</p> </li> </ul> <p>Required for new lifecycle hooks, but optional when updating existing hooks.</p>
            role_arn: <p>The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.</p> <p>Valid only if the notification target is an Amazon SNS topic or an Amazon SQS queue. Required for new lifecycle hooks, but optional when updating existing hooks.</p>
            notification_target_arn: <p>The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in a wait state for the lifecycle hook. You can specify either an Amazon SNS topic or an Amazon SQS queue.</p> <p>If you specify an empty string, this overrides the current ARN.</p> <p>This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key-value pair format when sending notifications to an Amazon SNS topic.</p> <p>When you specify a notification target, Amazon EC2 Auto Scaling sends it a test message. Test messages contain the following additional key-value pair: <code>"Event": "autoscaling:TEST_NOTIFICATION"</code>.</p>
            notification_metadata: <p>Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.</p>
            heartbeat_timeout: <p>The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from <code>30</code> to <code>7200</code> seconds. The default value is <code>3600</code> seconds (1 hour).</p>
            default_result: <p>The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The default value is <code>ABANDON</code>.</p> <p>Valid values: <code>CONTINUE</code> | <code>ABANDON</code> </p>

        Raises:
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a launch lifecycle hook
            This example creates a lifecycle hook for instance launch.

            >>> client.put_lifecycle_hook(lifecycle_hook_name='my-launch-lifecycle-hook', heartbeat_timeout=300, auto_scaling_group_name='my-auto-scaling-group', lifecycle_transition='autoscaling:EC2_INSTANCE_LAUNCHING', default_result='CONTINUE')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.put_lifecycle_hook_type.PutLifecycleHookType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.put_lifecycle_hook_answer.PutLifecycleHookAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.put_lifecycle_hook

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.put_lifecycle_hook.put_lifecycle_hook(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.put_lifecycle_hook_type.PutLifecycleHookType = {}
        if lifecycle_hook_name is not None:
            input_["lifecycle_hook_name"] = lifecycle_hook_name
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if lifecycle_transition is not None:
            input_["lifecycle_transition"] = lifecycle_transition
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if notification_target_arn is not None:
            input_["notification_target_arn"] = notification_target_arn
        if notification_metadata is not None:
            input_["notification_metadata"] = notification_metadata
        if heartbeat_timeout is not None:
            input_["heartbeat_timeout"] = heartbeat_timeout
        if default_result is not None:
            input_["default_result"] = default_result

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_notification_configuration(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        topic_arn: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        notification_types: Optional[
            "capo_auto_scaling.types.auto_scaling_notification_types.AutoScalingNotificationTypes"
        ] = None,
    ) -> None:
        """<p>Configures an Auto Scaling group to send notifications when specified events take place. Subscribers to the specified topic can have messages delivered to an endpoint such as a web server or an email address.</p> <p>This configuration overwrites any existing configuration.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-sns-notifications.html">Amazon SNS notification options for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>If you exceed your maximum limit of SNS topics, which is 10 per Auto Scaling group, the call fails.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon SNS topic.</p>
            notification_types: <p>The type of event that causes the notification to be sent. To query the notification types supported by Amazon EC2 Auto Scaling, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingNotificationTypes.html">DescribeAutoScalingNotificationTypes</a> API.</p>

        Raises:
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add an Auto Scaling notification
            This example adds the specified notification to the specified Auto Scaling group.

            >>> client.put_notification_configuration(auto_scaling_group_name='my-auto-scaling-group', topic_arn='arn:aws:sns:us-west-2:123456789012:my-sns-topic', notification_types=['autoscaling:TEST_NOTIFICATION'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.put_notification_configuration_type.PutNotificationConfigurationType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.put_notification_configuration

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.put_notification_configuration.put_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.put_notification_configuration_type.PutNotificationConfigurationType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if topic_arn is not None:
            input_["topic_arn"] = topic_arn
        if notification_types is not None:
            input_["notification_types"] = notification_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_scaling_policy(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        policy_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        policy_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
        ] = None,
        adjustment_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        min_adjustment_step: Optional[
            "capo_auto_scaling.types.min_adjustment_step.MinAdjustmentStep"
        ] = None,
        min_adjustment_magnitude: Optional[
            "capo_auto_scaling.types.min_adjustment_magnitude.MinAdjustmentMagnitude"
        ] = None,
        scaling_adjustment: Optional[
            "capo_auto_scaling.types.policy_increment.PolicyIncrement"
        ] = None,
        cooldown: Optional["capo_auto_scaling.types.cooldown.Cooldown"] = None,
        metric_aggregation_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
        ] = None,
        step_adjustments: Optional[
            "capo_auto_scaling.types.step_adjustments.StepAdjustments"
        ] = None,
        estimated_instance_warmup: Optional[
            "capo_auto_scaling.types.estimated_instance_warmup.EstimatedInstanceWarmup"
        ] = None,
        target_tracking_configuration: Optional[
            "capo_auto_scaling.types.target_tracking_configuration.TargetTrackingConfiguration"
        ] = None,
        enabled: Optional[
            "capo_auto_scaling.types.scaling_policy_enabled.ScalingPolicyEnabled"
        ] = None,
        predictive_scaling_configuration: Optional[
            "capo_auto_scaling.types.predictive_scaling_configuration.PredictiveScalingConfiguration"
        ] = None,
    ) -> "capo_auto_scaling.types.policy_arn_type.PolicyARNType":
        """<p>Creates or updates a scaling policy for an Auto Scaling group. Scaling policies are used to scale an Auto Scaling group based on configurable metrics. If no policies are defined, the dynamic scaling and predictive scaling features are not used. </p> <p>For more information about using dynamic scaling, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html">Target tracking scaling policies</a> and <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html">Step and simple scaling policies</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>For more information about using predictive scaling, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html">Predictive scaling for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>You can view the scaling policies for an Auto Scaling group using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html">DescribePolicies</a> API call. If you are no longer using a scaling policy, you can delete it by calling the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeletePolicy.html">DeletePolicy</a> API.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            policy_name: <p>The name of the policy.</p>
            policy_type: <p>One of the following policy types: </p> <ul> <li> <p> <code>TargetTrackingScaling</code> </p> </li> <li> <p> <code>StepScaling</code> </p> </li> <li> <p> <code>SimpleScaling</code> (default)</p> </li> <li> <p> <code>PredictiveScaling</code> </p> </li> </ul>
            adjustment_type: <p>Specifies how the scaling adjustment is interpreted (for example, an absolute number or a percentage). The valid values are <code>ChangeInCapacity</code>, <code>ExactCapacity</code>, and <code>PercentChangeInCapacity</code>.</p> <p>Required if the policy type is <code>StepScaling</code> or <code>SimpleScaling</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment">Scaling adjustment types</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            min_adjustment_step: <p>Available for backward compatibility. Use <code>MinAdjustmentMagnitude</code> instead.</p>
            min_adjustment_magnitude: <p>The minimum value to scale by when the adjustment type is <code>PercentChangeInCapacity</code>. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a <code>MinAdjustmentMagnitude</code> of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a <code>MinAdjustmentMagnitude</code> of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.</p> <p>Valid only if the policy type is <code>StepScaling</code> or <code>SimpleScaling</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment">Scaling adjustment types</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <note> <p>Some Auto Scaling groups use instance weights. In this case, set the <code>MinAdjustmentMagnitude</code> to a value that is at least as large as your largest instance weight.</p> </note>
            scaling_adjustment: <p>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a non-negative value.</p> <p>Required if the policy type is <code>SimpleScaling</code>. (Not used with any other policy type.) </p>
            cooldown: <p>A cooldown period, in seconds, that applies to a specific simple scaling policy. When a cooldown period is specified here, it overrides the default cooldown.</p> <p>Valid only if the policy type is <code>SimpleScaling</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html">Scaling cooldowns for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Default: None</p>
            metric_aggregation_type: <p>The aggregation type for the CloudWatch metrics. The valid values are <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code>. If the aggregation type is null, the value is treated as <code>Average</code>.</p> <p>Valid only if the policy type is <code>StepScaling</code>.</p>
            step_adjustments: <p>A set of adjustments that enable you to scale based on the size of the alarm breach.</p> <p>Required if the policy type is <code>StepScaling</code>. (Not used with any other policy type.) </p>
            estimated_instance_warmup: <p> <i>Not needed if the default instance warmup is defined for the group.</i> </p> <p>The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This warm-up period applies to instances launched due to a specific target tracking or step scaling policy. When a warm-up period is specified here, it overrides the default instance warmup.</p> <p>Valid only if the policy type is <code>TargetTrackingScaling</code> or <code>StepScaling</code>.</p> <note> <p>The default is to use the value for the default instance warmup defined for the group. If default instance warmup is null, then <code>EstimatedInstanceWarmup</code> falls back to the value of default cooldown.</p> </note>
            target_tracking_configuration: <p>A target tracking scaling policy. Provides support for predefined or custom metrics.</p> <p>The following predefined metrics are available:</p> <ul> <li> <p> <code>ASGAverageCPUUtilization</code> </p> </li> <li> <p> <code>ASGAverageNetworkIn</code> </p> </li> <li> <p> <code>ASGAverageNetworkOut</code> </p> </li> <li> <p> <code>ALBRequestCountPerTarget</code> </p> </li> </ul> <p>If you specify <code>ALBRequestCountPerTarget</code> for the metric, you must specify the <code>ResourceLabel</code> property with the <code>PredefinedMetricSpecification</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingConfiguration.html">TargetTrackingConfiguration</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p> <p>Required if the policy type is <code>TargetTrackingScaling</code>.</p>
            enabled: <p>Indicates whether the scaling policy is enabled or disabled. The default is enabled. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enable-disable-scaling-policy.html">Disable a scaling policy for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            predictive_scaling_configuration: <p>A predictive scaling policy. Provides support for predefined and custom metrics.</p> <p>Predefined metrics include CPU utilization, network in/out, and the Application Load Balancer request count.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingConfiguration.html">PredictiveScalingConfiguration</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p> <p>Required if the policy type is <code>PredictiveScaling</code>.</p>

        Raises:
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a scaling policy to an Auto Scaling group
            This example adds the specified policy to the specified Auto Scaling group.

            >>> client.put_scaling_policy(auto_scaling_group_name='my-auto-scaling-group', policy_name='alb1000-target-tracking-scaling-policy', policy_type='TargetTrackingScaling', target_tracking_configuration={'TargetValue': 1000.0, 'PredefinedMetricSpecification': {'PredefinedMetricType': 'ALBRequestCountPerTarget', 'ResourceLabel': 'app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff'}})
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.put_scaling_policy_type.PutScalingPolicyType]",
        ) -> OperationResponse["capo_auto_scaling.types.policy_arn_type.PolicyARNType"]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.put_scaling_policy

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.put_scaling_policy.put_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.put_scaling_policy_type.PutScalingPolicyType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if policy_type is not None:
            input_["policy_type"] = policy_type
        if adjustment_type is not None:
            input_["adjustment_type"] = adjustment_type
        if min_adjustment_step is not None:
            input_["min_adjustment_step"] = min_adjustment_step
        if min_adjustment_magnitude is not None:
            input_["min_adjustment_magnitude"] = min_adjustment_magnitude
        if scaling_adjustment is not None:
            input_["scaling_adjustment"] = scaling_adjustment
        if cooldown is not None:
            input_["cooldown"] = cooldown
        if metric_aggregation_type is not None:
            input_["metric_aggregation_type"] = metric_aggregation_type
        if step_adjustments is not None:
            input_["step_adjustments"] = step_adjustments
        if estimated_instance_warmup is not None:
            input_["estimated_instance_warmup"] = estimated_instance_warmup
        if target_tracking_configuration is not None:
            input_["target_tracking_configuration"] = target_tracking_configuration
        if enabled is not None:
            input_["enabled"] = enabled
        if predictive_scaling_configuration is not None:
            input_["predictive_scaling_configuration"] = (
                predictive_scaling_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_scheduled_update_group_action(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scheduled_action_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        time: Optional["capo_auto_scaling.types.timestamp_type.TimestampType"] = None,
        start_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        end_time: Optional[
            "capo_auto_scaling.types.timestamp_type.TimestampType"
        ] = None,
        recurrence: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        min_size: Optional[
            "capo_auto_scaling.types.auto_scaling_group_min_size.AutoScalingGroupMinSize"
        ] = None,
        max_size: Optional[
            "capo_auto_scaling.types.auto_scaling_group_max_size.AutoScalingGroupMaxSize"
        ] = None,
        desired_capacity: Optional[
            "capo_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
        ] = None,
        time_zone: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> None:
        """<p>Creates or updates a scheduled scaling action for an Auto Scaling group.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html">Scheduled scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>You can view the scheduled actions for an Auto Scaling group using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScheduledActions.html">DescribeScheduledActions</a> API call. If you are no longer using a scheduled action, you can delete it by calling the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteScheduledAction.html">DeleteScheduledAction</a> API.</p> <p>If you try to schedule your action in the past, Amazon EC2 Auto Scaling returns an error message.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            scheduled_action_name: <p>The name of this scaling action.</p>
            time: <p>This property is no longer used.</p>
            start_time: <p>The date and time for this action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, <code>"2021-06-01T00:00:00Z"</code>).</p> <p>If you specify <code>Recurrence</code> and <code>StartTime</code>, Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.</p>
            end_time: <p>The date and time for the recurring schedule to end, in UTC. For example, <code>"2021-06-01T00:00:00Z"</code>.</p>
            recurrence: <p>The recurring schedule for this action. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, <code>"30 0 1 1,6,12 *"</code>). For more information about this format, see <a href="http://crontab.org">Crontab</a>.</p> <p>When <code>StartTime</code> and <code>EndTime</code> are specified with <code>Recurrence</code>, they form the boundaries of when the recurring action starts and stops.</p> <p>Cron expressions use Universal Coordinated Time (UTC) by default.</p>
            min_size: <p>The minimum size of the Auto Scaling group.</p>
            max_size: <p>The maximum size of the Auto Scaling group.</p>
            desired_capacity: <p>The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain. It can scale beyond this capacity if you add more scaling conditions. </p> <note> <p>You must specify at least one of the following properties: <code>MaxSize</code>, <code>MinSize</code>, or <code>DesiredCapacity</code>. </p> </note>
            time_zone: <p>Specifies the time zone for a cron expression. If a time zone is not provided, UTC is used by default. </p> <p>Valid values are the canonical names of the IANA time zones, derived from the IANA Time Zone Database (such as <code>Etc/GMT+9</code> or <code>Pacific/Tahiti</code>). For more information, see <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">https://en.wikipedia.org/wiki/List_of_tz_database_time_zones</a>.</p>

        Raises:
            capo_auto_scaling.errors.already_exists_fault.AlreadyExistsFault: <p>You already have an Auto Scaling group or launch configuration with this name.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a scheduled action to an Auto Scaling group
            This example adds the specified scheduled action to the specified Auto Scaling group.

            >>> client.put_scheduled_update_group_action(auto_scaling_group_name='my-auto-scaling-group', scheduled_action_name='my-scheduled-action', start_time='2014-05-12T08:00:00Z', end_time='2014-05-12T08:00:00Z', min_size=2, max_size=6, desired_capacity=4)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.put_scheduled_update_group_action_type.PutScheduledUpdateGroupActionType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.put_scheduled_update_group_action

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.put_scheduled_update_group_action.put_scheduled_update_group_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.put_scheduled_update_group_action_type.PutScheduledUpdateGroupActionType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if scheduled_action_name is not None:
            input_["scheduled_action_name"] = scheduled_action_name
        if time is not None:
            input_["time"] = time
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if recurrence is not None:
            input_["recurrence"] = recurrence
        if min_size is not None:
            input_["min_size"] = min_size
        if max_size is not None:
            input_["max_size"] = max_size
        if desired_capacity is not None:
            input_["desired_capacity"] = desired_capacity
        if time_zone is not None:
            input_["time_zone"] = time_zone

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_warm_pool(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        max_group_prepared_capacity: Optional[
            "capo_auto_scaling.types.max_group_prepared_capacity.MaxGroupPreparedCapacity"
        ] = None,
        min_size: Optional[
            "capo_auto_scaling.types.warm_pool_min_size.WarmPoolMinSize"
        ] = None,
        pool_state: Optional[
            "capo_auto_scaling.types.warm_pool_state.WarmPoolState"
        ] = None,
        instance_reuse_policy: Optional[
            "capo_auto_scaling.types.instance_reuse_policy.InstanceReusePolicy"
        ] = None,
    ) -> "capo_auto_scaling.types.put_warm_pool_answer.PutWarmPoolAnswer":
        """<p>Creates or updates a warm pool for the specified Auto Scaling group. A warm pool is a pool of pre-initialized EC2 instances that sits alongside the Auto Scaling group. Whenever your application needs to scale out, the Auto Scaling group can draw on the warm pool to meet its new desired capacity.</p> <p>This operation must be called from the Region in which the Auto Scaling group was created.</p> <p>You can view the instances in the warm pool using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html">DescribeWarmPool</a> API call. If you are no longer using a warm pool, you can delete it by calling the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteWarmPool.html">DeleteWarmPool</a> API.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html">Warm pools for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            max_group_prepared_capacity: <p>Specifies the maximum number of instances that are allowed to be in the warm pool or in any state except <code>Terminated</code> for the Auto Scaling group. This is an optional property. Specify it only if you do not want the warm pool size to be determined by the difference between the group's maximum capacity and its desired capacity. </p> <important> <p>If a value for <code>MaxGroupPreparedCapacity</code> is not specified, Amazon EC2 Auto Scaling launches and maintains the difference between the group's maximum capacity and its desired capacity. If you specify a value for <code>MaxGroupPreparedCapacity</code>, Amazon EC2 Auto Scaling uses the difference between the <code>MaxGroupPreparedCapacity</code> and the desired capacity instead. </p> <p>The size of the warm pool is dynamic. Only when <code>MaxGroupPreparedCapacity</code> and <code>MinSize</code> are set to the same value does the warm pool have an absolute size.</p> </important> <p>If the desired capacity of the Auto Scaling group is higher than the <code>MaxGroupPreparedCapacity</code>, the capacity of the warm pool is 0, unless you specify a value for <code>MinSize</code>. To remove a value that you previously set, include the property but specify -1 for the value. </p>
            min_size: <p>Specifies the minimum number of instances to maintain in the warm pool. This helps you to ensure that there is always a certain number of warmed instances available to handle traffic spikes. Defaults to 0 if not specified.</p>
            pool_state: <p>Sets the instance state to transition to after the lifecycle actions are complete. Default is <code>Stopped</code>.</p>
            instance_reuse_policy: <p>Indicates whether instances in the Auto Scaling group can be returned to the warm pool on scale in. The default is to terminate instances in the Auto Scaling group when the group scales in.</p>

        Raises:
            capo_auto_scaling.errors.instance_refresh_in_progress_fault.InstanceRefreshInProgressFault: <p>The request failed because an active instance refresh already exists for the specified Auto Scaling group.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a warm pool for an Auto Scaling group
            This example creates a warm pool for the specified Auto Scaling group.

            >>> client.put_warm_pool(auto_scaling_group_name='my-auto-scaling-group', min_size=30, pool_state='Hibernated', instance_reuse_policy={'ReuseOnScaleIn': True})
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.put_warm_pool_type.PutWarmPoolType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.put_warm_pool_answer.PutWarmPoolAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.put_warm_pool

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.put_warm_pool.put_warm_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.put_warm_pool_type.PutWarmPoolType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if max_group_prepared_capacity is not None:
            input_["max_group_prepared_capacity"] = max_group_prepared_capacity
        if min_size is not None:
            input_["min_size"] = min_size
        if pool_state is not None:
            input_["pool_state"] = pool_state
        if instance_reuse_policy is not None:
            input_["instance_reuse_policy"] = instance_reuse_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def record_lifecycle_action_heartbeat(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        lifecycle_hook_name: Optional[
            "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.resource_name.ResourceName"
        ] = None,
        lifecycle_action_token: Optional[
            "capo_auto_scaling.types.lifecycle_action_token.LifecycleActionToken"
        ] = None,
        instance_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
        ] = None,
    ) -> "capo_auto_scaling.types.record_lifecycle_action_heartbeat_answer.RecordLifecycleActionHeartbeatAnswer":
        """<p>Records a heartbeat for the lifecycle action associated with the specified token or instance. This extends the timeout by the length of time defined using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutLifecycleHook.html">PutLifecycleHook</a> API call.</p> <p>This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:</p> <ol> <li> <p>(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.</p> </li> <li> <p>(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.</p> </li> <li> <p>(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.</p> </li> <li> <p>Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.</p> </li> <li> <p> <b>If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state.</b> </p> </li> <li> <p>If you finish before the timeout period ends, send a callback by using the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html">CompleteLifecycleAction</a> API call.</p> </li> </ol> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html">Amazon EC2 Auto Scaling lifecycle hooks</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            lifecycle_hook_name: <p>The name of the lifecycle hook.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            lifecycle_action_token: <p>A token that uniquely identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target that you specified when you created the lifecycle hook.</p>
            instance_id: <p>The ID of the instance.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To record a lifecycle action heartbeat
            This example records a lifecycle action heartbeat to keep the instance in a pending state.

            >>> client.record_lifecycle_action_heartbeat(lifecycle_hook_name='my-lifecycle-hook', auto_scaling_group_name='my-auto-scaling-group', lifecycle_action_token='bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.record_lifecycle_action_heartbeat_type.RecordLifecycleActionHeartbeatType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.record_lifecycle_action_heartbeat_answer.RecordLifecycleActionHeartbeatAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.record_lifecycle_action_heartbeat

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.record_lifecycle_action_heartbeat.record_lifecycle_action_heartbeat(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.record_lifecycle_action_heartbeat_type.RecordLifecycleActionHeartbeatType = {}
        if lifecycle_hook_name is not None:
            input_["lifecycle_hook_name"] = lifecycle_hook_name
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if lifecycle_action_token is not None:
            input_["lifecycle_action_token"] = lifecycle_action_token
        if instance_id is not None:
            input_["instance_id"] = instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resume_processes(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scaling_processes: Optional[
            "capo_auto_scaling.types.process_names.ProcessNames"
        ] = None,
    ) -> None:
        """<p>Resumes the specified suspended auto scaling processes, or all suspended process, for the specified Auto Scaling group.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html">Suspend and resume Amazon EC2 Auto Scaling processes</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            scaling_processes: <p>One or more of the following processes:</p> <ul> <li> <p> <code>Launch</code> </p> </li> <li> <p> <code>Terminate</code> </p> </li> <li> <p> <code>AddToLoadBalancer</code> </p> </li> <li> <p> <code>AlarmNotification</code> </p> </li> <li> <p> <code>AZRebalance</code> </p> </li> <li> <p> <code>HealthCheck</code> </p> </li> <li> <p> <code>InstanceRefresh</code> </p> </li> <li> <p> <code>ReplaceUnhealthy</code> </p> </li> <li> <p> <code>ScheduledActions</code> </p> </li> </ul> <p>If you omit this property, all processes are specified.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.resource_in_use_fault.ResourceInUseFault: <p>The operation can't be performed because the resource is in use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To resume Auto Scaling processes
            This example resumes the specified suspended scaling process for the specified Auto Scaling group.

            >>> client.resume_processes(auto_scaling_group_name='my-auto-scaling-group', scaling_processes=['AlarmNotification'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.scaling_process_query.ScalingProcessQuery]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.resume_processes

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.resume_processes.resume_processes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.scaling_process_query.ScalingProcessQuery = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if scaling_processes is not None:
            input_["scaling_processes"] = scaling_processes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rollback_instance_refresh(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
    ) -> "capo_auto_scaling.types.rollback_instance_refresh_answer.RollbackInstanceRefreshAnswer":
        """<p>Cancels an instance refresh that is in progress and rolls back any changes that it made. Amazon EC2 Auto Scaling replaces any instances that were replaced during the instance refresh. This restores your Auto Scaling group to the configuration that it was using before the start of the instance refresh. </p> <p>This operation is part of the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html">instance refresh feature</a> in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.</p> <p>A rollback is not supported in the following situations: </p> <ul> <li> <p>There is no desired configuration specified for the instance refresh.</p> </li> <li> <p>The Auto Scaling group has a launch template that uses an Amazon Web Services Systems Manager parameter instead of an AMI ID for the <code>ImageId</code> property.</p> </li> <li> <p>The Auto Scaling group uses the launch template's <code>$Latest</code> or <code>$Default</code> version.</p> </li> </ul> <p>When you receive a successful response from this operation, Amazon EC2 Auto Scaling immediately begins replacing instances. You can check the status of this operation through the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html">DescribeInstanceRefreshes</a> API operation. </p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>

        Raises:
            capo_auto_scaling.errors.active_instance_refresh_not_found_fault.ActiveInstanceRefreshNotFoundFault: <p>The request failed because an active instance refresh or rollback for the specified Auto Scaling group was not found.</p>
            capo_auto_scaling.errors.irreversible_instance_refresh_fault.IrreversibleInstanceRefreshFault: <p>The request failed because a desired configuration was not found or an incompatible launch template (uses a Systems Manager parameter instead of an AMI ID) or launch template version (<code>$Latest</code> or <code>$Default</code>) is present on the Auto Scaling group.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.rollback_instance_refresh_type.RollbackInstanceRefreshType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.rollback_instance_refresh_answer.RollbackInstanceRefreshAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.rollback_instance_refresh

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.rollback_instance_refresh.rollback_instance_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.rollback_instance_refresh_type.RollbackInstanceRefreshType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_desired_capacity(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        desired_capacity: Optional[
            "capo_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
        ] = None,
        honor_cooldown: Optional[
            "capo_auto_scaling.types.honor_cooldown.HonorCooldown"
        ] = None,
    ) -> None:
        """<p>Sets the size of the specified Auto Scaling group.</p> <p>If a scale-in activity occurs as a result of a new <code>DesiredCapacity</code> value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html">Manual scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            desired_capacity: <p>The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain.</p>
            honor_cooldown: <p>Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity. By default, Amazon EC2 Auto Scaling does not honor the cooldown period during manual scaling activities.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.scaling_activity_in_progress_fault.ScalingActivityInProgressFault: <p>The operation can't be performed because there are scaling activities in progress.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set the desired capacity for an Auto Scaling group
            This example sets the desired capacity for the specified Auto Scaling group.

            >>> client.set_desired_capacity(auto_scaling_group_name='my-auto-scaling-group', desired_capacity=2, honor_cooldown=True)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.set_desired_capacity_type.SetDesiredCapacityType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.set_desired_capacity

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.set_desired_capacity.set_desired_capacity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.set_desired_capacity_type.SetDesiredCapacityType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if desired_capacity is not None:
            input_["desired_capacity"] = desired_capacity
        if honor_cooldown is not None:
            input_["honor_cooldown"] = honor_cooldown

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_instance_health(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
        ] = None,
        health_status: Optional[
            "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
        ] = None,
        should_respect_grace_period: Optional[
            "capo_auto_scaling.types.should_respect_grace_period.ShouldRespectGracePeriod"
        ] = None,
    ) -> None:
        """<p>Sets the health status of the specified instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-up-a-custom-health-check.html">Set up a custom health check for your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            instance_id: <p>The ID of the instance.</p>
            health_status: <p>The health status of the instance. Set to <code>Healthy</code> to have the instance remain in service. Set to <code>Unhealthy</code> to have the instance be out of service. Amazon EC2 Auto Scaling terminates and replaces the unhealthy instance.</p>
            should_respect_grace_period: <p>If the Auto Scaling group of the specified instance has a <code>HealthCheckGracePeriod</code> specified for the group, by default, this call respects the grace period. Set this to <code>False</code>, to have the call not respect the grace period associated with the group.</p> <p>For more information about the health check grace period, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html">Set the health check grace period for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set the health status of an instance
            This example sets the health status of the specified instance to Unhealthy.

            >>> client.set_instance_health(instance_id='i-93633f9b', health_status='Unhealthy')
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.set_instance_health_query.SetInstanceHealthQuery]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.set_instance_health

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.set_instance_health.set_instance_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.set_instance_health_query.SetInstanceHealthQuery = {}
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if health_status is not None:
            input_["health_status"] = health_status
        if should_respect_grace_period is not None:
            input_["should_respect_grace_period"] = should_respect_grace_period

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_instance_protection(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.instance_ids.InstanceIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        protected_from_scale_in: Optional[
            "capo_auto_scaling.types.protected_from_scale_in.ProtectedFromScaleIn"
        ] = None,
    ) -> "capo_auto_scaling.types.set_instance_protection_answer.SetInstanceProtectionAnswer":
        """<p>Updates the instance protection settings of the specified instances. This operation cannot be called on instances in a warm pool.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html">Use instance scale-in protection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>If you exceed your maximum limit of instance IDs, which is 50 per Auto Scaling group, the call fails.</p>

        Args:
            instance_ids: <p>One or more instance IDs. You can specify up to 50 instances.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            protected_from_scale_in: <p>Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.</p>

        Raises:
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable instance protection for an instance
            This example enables instance protection for the specified instance.

            >>> client.set_instance_protection(instance_ids=['i-93633f9b'], auto_scaling_group_name='my-auto-scaling-group', protected_from_scale_in=True)
            To disable instance protection for an instance
            This example disables instance protection for the specified instance.

            >>> client.set_instance_protection(instance_ids=['i-93633f9b'], auto_scaling_group_name='my-auto-scaling-group', protected_from_scale_in=False)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.set_instance_protection_query.SetInstanceProtectionQuery]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.set_instance_protection_answer.SetInstanceProtectionAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.set_instance_protection

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.set_instance_protection.set_instance_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.set_instance_protection_query.SetInstanceProtectionQuery = {}
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if protected_from_scale_in is not None:
            input_["protected_from_scale_in"] = protected_from_scale_in

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_instance_refresh(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        strategy: Optional[
            "capo_auto_scaling.types.refresh_strategy.RefreshStrategy"
        ] = None,
        desired_configuration: Optional[
            "capo_auto_scaling.types.desired_configuration.DesiredConfiguration"
        ] = None,
        preferences: Optional[
            "capo_auto_scaling.types.refresh_preferences.RefreshPreferences"
        ] = None,
    ) -> "capo_auto_scaling.types.start_instance_refresh_answer.StartInstanceRefreshAnswer":
        """<p>Starts an instance refresh.</p> <p>This operation is part of the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html">instance refresh feature</a> in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group. This feature is helpful, for example, when you have a new AMI or a new user data script. You just need to create a new launch template that specifies the new AMI or user data script. Then start an instance refresh to immediately begin the process of updating instances in the group. </p> <p>If successful, the request's response contains a unique ID that you can use to track the progress of the instance refresh. To query its status, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html">DescribeInstanceRefreshes</a> API. To describe the instance refreshes that have already run, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html">DescribeInstanceRefreshes</a> API. To cancel an instance refresh that is in progress, use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CancelInstanceRefresh.html">CancelInstanceRefresh</a> API. </p> <p>An instance refresh might fail for several reasons, such as EC2 launch failures, misconfigured health checks, or not ignoring or allowing the termination of instances that are in <code>Standby</code> state or protected from scale in. You can monitor for failed EC2 launches using the scaling activities. To find the scaling activities, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html">DescribeScalingActivities</a> API.</p> <p>If you enable auto rollback, your Auto Scaling group will be rolled back automatically when the instance refresh fails. You can enable this feature before starting an instance refresh by specifying the <code>AutoRollback</code> property in the instance refresh preferences. Otherwise, to roll back an instance refresh before it finishes, use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackInstanceRefresh.html">RollbackInstanceRefresh</a> API. </p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            strategy: <p>The strategy to use for the instance refresh. The default value is <code>Rolling</code>.</p>
            desired_configuration: <p>The desired configuration. For example, the desired configuration can specify a new launch template or a new version of the current launch template.</p> <p>Once the instance refresh succeeds, Amazon EC2 Auto Scaling updates the settings of the Auto Scaling group to reflect the new desired configuration. </p> <note> <p>When you specify a new launch template or a new version of the current launch template for your desired configuration, consider enabling the <code>SkipMatching</code> property in preferences. If it's enabled, Amazon EC2 Auto Scaling skips replacing instances that already use the specified launch template and instance types. This can help you reduce the number of replacements that are required to apply updates. </p> </note>
            preferences: <p>Sets your preferences for the instance refresh so that it performs as expected when you start it. Includes the instance warmup time, the minimum and maximum healthy percentages, and the behaviors that you want Amazon EC2 Auto Scaling to use if instances that are in <code>Standby</code> state or protected from scale in are found. You can also choose to enable additional features, such as the following:</p> <ul> <li> <p>Auto rollback</p> </li> <li> <p>Checkpoints</p> </li> <li> <p>CloudWatch alarms</p> </li> <li> <p>Skip matching</p> </li> <li> <p>Bake time</p> </li> </ul>

        Raises:
            capo_auto_scaling.errors.instance_refresh_in_progress_fault.InstanceRefreshInProgressFault: <p>The request failed because an active instance refresh already exists for the specified Auto Scaling group.</p>
            capo_auto_scaling.errors.limit_exceeded_fault.LimitExceededFault: <p>You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html">DescribeAccountLimits</a> in the <i>Amazon EC2 Auto Scaling API Reference</i>.</p>
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start an instance refresh
            This example starts an instance refresh for the specified Auto Scaling group.

            >>> client.start_instance_refresh(auto_scaling_group_name='my-auto-scaling-group', desired_configuration={'LaunchTemplate': {'LaunchTemplateName': 'my-template-for-auto-scaling', 'Version': '$Latest'}}, preferences={'AutoRollback': True, 'InstanceWarmup': 200, 'MinHealthyPercentage': 90, 'MaxHealthyPercentage': 120, 'AlarmSpecification': {'Alarms': ['my-alarm']}})
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.start_instance_refresh_type.StartInstanceRefreshType]",
        ) -> OperationResponse[
            "capo_auto_scaling.types.start_instance_refresh_answer.StartInstanceRefreshAnswer"
        ]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.start_instance_refresh

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.start_instance_refresh.start_instance_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.start_instance_refresh_type.StartInstanceRefreshType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if strategy is not None:
            input_["strategy"] = strategy
        if desired_configuration is not None:
            input_["desired_configuration"] = desired_configuration
        if preferences is not None:
            input_["preferences"] = preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def suspend_processes(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        scaling_processes: Optional[
            "capo_auto_scaling.types.process_names.ProcessNames"
        ] = None,
    ) -> None:
        """<p>Suspends the specified auto scaling processes, or all processes, for the specified Auto Scaling group.</p> <p>If you suspend either the <code>Launch</code> or <code>Terminate</code> process types, it can prevent other process types from functioning properly. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html">Suspend and resume Amazon EC2 Auto Scaling processes</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>To resume processes that have been suspended, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html">ResumeProcesses</a> API.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            scaling_processes: <p>One or more of the following processes:</p> <ul> <li> <p> <code>Launch</code> </p> </li> <li> <p> <code>Terminate</code> </p> </li> <li> <p> <code>AddToLoadBalancer</code> </p> </li> <li> <p> <code>AlarmNotification</code> </p> </li> <li> <p> <code>AZRebalance</code> </p> </li> <li> <p> <code>HealthCheck</code> </p> </li> <li> <p> <code>InstanceRefresh</code> </p> </li> <li> <p> <code>ReplaceUnhealthy</code> </p> </li> <li> <p> <code>ScheduledActions</code> </p> </li> </ul> <p>If you omit this property, all processes are specified.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.resource_in_use_fault.ResourceInUseFault: <p>The operation can't be performed because the resource is in use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To suspend Auto Scaling processes
            This example suspends the specified scaling process for the specified Auto Scaling group.

            >>> client.suspend_processes(auto_scaling_group_name='my-auto-scaling-group', scaling_processes=['AlarmNotification'])
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.scaling_process_query.ScalingProcessQuery]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.suspend_processes

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.suspend_processes.suspend_processes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.scaling_process_query.ScalingProcessQuery = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if scaling_processes is not None:
            input_["scaling_processes"] = scaling_processes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_instance_in_auto_scaling_group(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        instance_id: Optional[
            "capo_auto_scaling.types.xml_string_max_len19.XmlStringMaxLen19"
        ] = None,
        instance_ids: Optional[
            "capo_auto_scaling.types.termination_instance_ids.TerminationInstanceIds"
        ] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        should_decrement_desired_capacity: Optional[
            "capo_auto_scaling.types.should_decrement_desired_capacity.ShouldDecrementDesiredCapacity"
        ] = None,
    ) -> "capo_auto_scaling.types.activity_type.ActivityType":
        """<p>Terminates the specified instance and optionally adjusts the desired group size. This operation cannot be called on instances in a warm pool.</p> <p>This call simply makes a termination request. The instances are not terminated immediately. When an instance is terminated, the instance status changes to <code>terminated</code>. You can't connect to or start an instance after you've terminated it.</p> <p>If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are terminated. </p> <p>To terminate multiple instances in a single call, use the <code>InstanceIds</code> and <code>AutoScalingGroupName</code> parameters instead of <code>InstanceId</code>. When terminating multiple instances, the response populates <code>Activities</code> instead of <code>Activity</code>.</p> <p>By default, Amazon EC2 Auto Scaling balances instances across all Availability Zones. If you decrement the desired capacity, your Auto Scaling group can become unbalanced between Availability Zones. Amazon EC2 Auto Scaling tries to rebalance the group, and rebalancing might terminate instances in other zones. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html">Manual scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

        Args:
            instance_id: <p>The ID of the instance.</p>
            instance_ids: <p>The IDs of the instances. You can specify up to 100 instances.</p> <p>This parameter requires that you also specify <code>AutoScalingGroupName</code>.</p>
            auto_scaling_group_name: <p>The name of the Auto Scaling group. Required when using <code>InstanceIds</code>.</p>
            should_decrement_desired_capacity: <p>Indicates whether terminating the instance also decrements the size of the Auto Scaling group.</p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.scaling_activity_in_progress_fault.ScalingActivityInProgressFault: <p>The operation can't be performed because there are scaling activities in progress.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To terminate an instance in an Auto Scaling group
            This example terminates the specified instance from the specified Auto Scaling group without updating the size of the group. Auto Scaling launches a replacement instance after the specified instance terminates.

            >>> client.terminate_instance_in_auto_scaling_group(instance_id='i-93633f9b', should_decrement_desired_capacity=False)
            To terminate multiple instances in an Auto Scaling group
            This example terminates multiple instances from the specified Auto Scaling group without updating the size of the group. Auto Scaling launches replacement instances after the specified instances terminate.

            >>> client.terminate_instance_in_auto_scaling_group(instance_ids=['i-93633f9b', 'i-ab4d5e6f7'], auto_scaling_group_name='my-asg', should_decrement_desired_capacity=False)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.terminate_instance_in_auto_scaling_group_type.TerminateInstanceInAutoScalingGroupType]",
        ) -> OperationResponse["capo_auto_scaling.types.activity_type.ActivityType"]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.terminate_instance_in_auto_scaling_group

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.terminate_instance_in_auto_scaling_group.terminate_instance_in_auto_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.terminate_instance_in_auto_scaling_group_type.TerminateInstanceInAutoScalingGroupType = {}
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if should_decrement_desired_capacity is not None:
            input_["should_decrement_desired_capacity"] = (
                should_decrement_desired_capacity
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_auto_scaling_group(
        self,
        *,
        config_overrides: Optional[AutoScalingClientConfig] = None,
        auto_scaling_group_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        launch_configuration_name: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        launch_template: Optional[
            "capo_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
        ] = None,
        mixed_instances_policy: Optional[
            "capo_auto_scaling.types.mixed_instances_policy.MixedInstancesPolicy"
        ] = None,
        min_size: Optional[
            "capo_auto_scaling.types.auto_scaling_group_min_size.AutoScalingGroupMinSize"
        ] = None,
        max_size: Optional[
            "capo_auto_scaling.types.auto_scaling_group_max_size.AutoScalingGroupMaxSize"
        ] = None,
        desired_capacity: Optional[
            "capo_auto_scaling.types.auto_scaling_group_desired_capacity.AutoScalingGroupDesiredCapacity"
        ] = None,
        default_cooldown: Optional["capo_auto_scaling.types.cooldown.Cooldown"] = None,
        availability_zones: Optional[
            "capo_auto_scaling.types.availability_zones.AvailabilityZones"
        ] = None,
        availability_zone_ids: Optional[
            "capo_auto_scaling.types.availability_zone_ids.AvailabilityZoneIds"
        ] = None,
        health_check_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
        ] = None,
        health_check_grace_period: Optional[
            "capo_auto_scaling.types.health_check_grace_period.HealthCheckGracePeriod"
        ] = None,
        placement_group: Optional[
            "capo_auto_scaling.types.update_placement_group_param.UpdatePlacementGroupParam"
        ] = None,
        vpc_zone_identifier: Optional[
            "capo_auto_scaling.types.xml_string_max_len5000.XmlStringMaxLen5000"
        ] = None,
        termination_policies: Optional[
            "capo_auto_scaling.types.termination_policies.TerminationPolicies"
        ] = None,
        new_instances_protected_from_scale_in: Optional[
            "capo_auto_scaling.types.instance_protected.InstanceProtected"
        ] = None,
        service_linked_role_arn: Optional[
            "capo_auto_scaling.types.resource_name.ResourceName"
        ] = None,
        max_instance_lifetime: Optional[
            "capo_auto_scaling.types.max_instance_lifetime.MaxInstanceLifetime"
        ] = None,
        capacity_rebalance: Optional[
            "capo_auto_scaling.types.capacity_rebalance_enabled.CapacityRebalanceEnabled"
        ] = None,
        context: Optional["capo_auto_scaling.types.context.Context"] = None,
        desired_capacity_type: Optional[
            "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
        ] = None,
        default_instance_warmup: Optional[
            "capo_auto_scaling.types.default_instance_warmup.DefaultInstanceWarmup"
        ] = None,
        instance_maintenance_policy: Optional[
            "capo_auto_scaling.types.instance_maintenance_policy.InstanceMaintenancePolicy"
        ] = None,
        availability_zone_distribution: Optional[
            "capo_auto_scaling.types.availability_zone_distribution.AvailabilityZoneDistribution"
        ] = None,
        availability_zone_impairment_policy: Optional[
            "capo_auto_scaling.types.availability_zone_impairment_policy.AvailabilityZoneImpairmentPolicy"
        ] = None,
        skip_zonal_shift_validation: Optional[
            "capo_auto_scaling.types.skip_zonal_shift_validation.SkipZonalShiftValidation"
        ] = None,
        capacity_reservation_specification: Optional[
            "capo_auto_scaling.types.capacity_reservation_specification.CapacityReservationSpecification"
        ] = None,
        instance_lifecycle_policy: Optional[
            "capo_auto_scaling.types.instance_lifecycle_policy.InstanceLifecyclePolicy"
        ] = None,
        deletion_protection: Optional[
            "capo_auto_scaling.types.deletion_protection.DeletionProtection"
        ] = None,
    ) -> None:
        """<p> <b>We strongly recommend that all Auto Scaling groups use launch templates to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.</b> </p> <p>Updates the configuration for the specified Auto Scaling group.</p> <p>To update an Auto Scaling group, specify the name of the group and the property that you want to change. Any properties that you don't specify are not changed by this update request. The new settings take effect on any scaling activities after this call returns. </p> <p>If you associate a new launch configuration or template with an Auto Scaling group, all new instances will get the updated configuration. Existing instances continue to run with the configuration that they were originally launched with. When you update a group to specify a mixed instances policy instead of a launch configuration or template, existing instances may be replaced to match the new purchasing options that you specified in the policy. For example, if the group currently has 100% On-Demand capacity and the policy specifies 50% Spot capacity, this means that half of your instances will be gradually terminated and relaunched as Spot Instances. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that updating your group does not compromise the performance or availability of your application.</p> <p>Note the following about changing <code>DesiredCapacity</code>, <code>MaxSize</code>, or <code>MinSize</code>:</p> <ul> <li> <p>If a scale-in activity occurs as a result of a new <code>DesiredCapacity</code> value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate.</p> </li> <li> <p>If you specify a new value for <code>MinSize</code> without specifying a value for <code>DesiredCapacity</code>, and the new <code>MinSize</code> is larger than the current size of the group, this sets the group's <code>DesiredCapacity</code> to the new <code>MinSize</code> value.</p> </li> <li> <p>If you specify a new value for <code>MaxSize</code> without specifying a value for <code>DesiredCapacity</code>, and the new <code>MaxSize</code> is smaller than the current size of the group, this sets the group's <code>DesiredCapacity</code> to the new <code>MaxSize</code> value.</p> </li> </ul> <p>To see which properties have been set, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html">DescribeAutoScalingGroups</a> API. To view the scaling policies for an Auto Scaling group, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html">DescribePolicies</a> API. If the group has scaling policies, you can update them by calling the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html">PutScalingPolicy</a> API.</p>

        Args:
            auto_scaling_group_name: <p>The name of the Auto Scaling group.</p>
            launch_configuration_name: <p>The name of the launch configuration. If you specify <code>LaunchConfigurationName</code> in your update request, you can't specify <code>LaunchTemplate</code> or <code>MixedInstancesPolicy</code>.</p>
            launch_template: <p>The launch template and version to use to specify the updates. If you specify <code>LaunchTemplate</code> in your update request, you can't specify <code>LaunchConfigurationName</code> or <code>MixedInstancesPolicy</code>.</p>
            mixed_instances_policy: <p>The mixed instances policy. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html">Auto Scaling groups with multiple instance types and purchase options</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>You can remove the Distribution Segments configuration by specifying <code>OnDemandBaseCapacity</code> or <code>OnDemandPercentageAboveBaseCapacity</code>. You can also remove it explicitly by specifying an empty list for <code>DistributionSegments</code>.</p>
            min_size: <p>The minimum size of the Auto Scaling group.</p>
            max_size: <p>The maximum size of the Auto Scaling group.</p> <note> <p>With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above <code>MaxSize</code> to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above <code>MaxSize</code> by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).</p> </note>
            desired_capacity: <p>The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.</p>
            default_cooldown: <p> <i>Only needed if you use simple scaling policies.</i> </p> <p>The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html">Scaling cooldowns for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            availability_zones: <p>One or more Availability Zones for the group.</p>
            availability_zone_ids: <p> A list of Availability Zone IDs for the Auto Scaling group. You cannot specify both AvailabilityZones and AvailabilityZoneIds in the same request. </p>
            health_check_type: <p>A comma-separated value string of one or more health check types.</p> <p>The valid values are <code>EC2</code>, <code>EBS</code>, <code>ELB</code>, and <code>VPC_LATTICE</code>. <code>EC2</code> is the default health check and cannot be disabled. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html">Health checks for instances in an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Only specify <code>EC2</code> if you must clear a value that was previously set.</p>
            health_check_grace_period: <p>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the <code>InService</code> state. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html">Set the health check grace period for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            placement_group: <p>The name of an existing placement group into which to launch your instances. To remove the placement group setting, pass an empty string for <code>placement-group</code>. For more information about placement groups, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">Placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>A <i>cluster</i> placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group. </p> </note>
            vpc_zone_identifier: <p>A comma-separated list of subnet IDs for a virtual private cloud (VPC). If you specify <code>VPCZoneIdentifier</code> with <code>AvailabilityZones</code>, the subnets that you specify must reside in those Availability Zones.</p>
            termination_policies: <p>A policy or a list of policies that are used to select the instances to terminate. The policies are executed in the order that you list them. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html">Configure termination policies for Amazon EC2 Auto Scaling</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Valid values: <code>Default</code> | <code>AllocationStrategy</code> | <code>ClosestToNextInstanceHour</code> | <code>NewestInstance</code> | <code>OldestInstance</code> | <code>OldestLaunchConfiguration</code> | <code>OldestLaunchTemplate</code> | <code>arn:aws:lambda:region:account-id:function:my-function:my-alias</code> </p>
            new_instances_protected_from_scale_in: <p>Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html">Use instance scale-in protection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            service_linked_role_arn: <p>The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html">Service-linked roles</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            max_instance_lifetime: <p>The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). To clear a previously set value, specify a new value of 0. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html">Replacing Auto Scaling instances based on maximum instance lifetime</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            capacity_rebalance: <p>Enables or disables Capacity Rebalancing. If Capacity Rebalancing is disabled, proactive replacement of at-risk Spot Instances does not occur. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html">Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <note> <p>To suspend rebalancing across Availability Zones, use the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendedProcess.html">SuspendProcesses</a> API.</p> </note>
            context: <p>Reserved.</p>
            desired_capacity_type: <p>The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports <code>DesiredCapacityType</code> for attribute-based instance type selection only. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html">Create a mixed instances group using attribute-based instance type selection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>By default, Amazon EC2 Auto Scaling specifies <code>units</code>, which translates into number of instances.</p> <p>Valid values: <code>units</code> | <code>vcpu</code> | <code>memory-mib</code> </p>
            default_instance_warmup: <p>The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the <code>InService</code> state. </p> <p>During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html">Set the default instance warmup for an Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <important> <p>To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, <i>even if it is set to 0 seconds</i>. To remove a value that you previously set, include the property but specify <code>-1</code> for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of <code>0</code> or other nominal value.</p> </important>
            instance_maintenance_policy: <p>An instance maintenance policy. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html">Set instance maintenance policy</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
            availability_zone_distribution: <p> The instance capacity distribution across Availability Zones. </p>
            availability_zone_impairment_policy: <p> The policy for Availability Zone impairment. </p>
            skip_zonal_shift_validation: <p> If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html">Auto Scaling group zonal shift</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>
            capacity_reservation_specification: <p> The capacity reservation specification for the Auto Scaling group. </p>
            instance_lifecycle_policy: <p> The instance lifecycle policy for the Auto Scaling group. This policy controls instance behavior when an instance transitions through its lifecycle states. Configure retention triggers to specify when instances should move to a <code>Retained</code> state instead of automatic termination. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html"> Control instance retention with instance lifecycle policies</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>
            deletion_protection: <p> The deletion protection setting for the Auto Scaling group. This setting helps safeguard your Auto Scaling group and its instances by controlling whether the <code>DeleteAutoScalingGroup</code> operation is allowed. When deletion protection is enabled, users cannot delete the Auto Scaling group according to the specified protection level until the setting is changed back to a less restrictive level. </p> <p> The valid values are <code>none</code>, <code>prevent-force-deletion</code>, and <code>prevent-all-deletion</code>. </p> <p> Default: <code>none</code> </p> <p> For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/resource-deletion-protection.html"> Configure deletion protection for your Amazon EC2 Auto Scaling resources</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>

        Raises:
            capo_auto_scaling.errors.resource_contention_fault.ResourceContentionFault: <p>You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).</p>
            capo_auto_scaling.errors.scaling_activity_in_progress_fault.ScalingActivityInProgressFault: <p>The operation can't be performed because there are scaling activities in progress.</p>
            capo_auto_scaling.errors.service_linked_role_failure.ServiceLinkedRoleFailure: <p>The service-linked role is not yet ready for use.</p>
            capo_auto_scaling.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an Auto Scaling group
            This example updates multiple properties at the same time.

            >>> client.update_auto_scaling_group(auto_scaling_group_name='my-auto-scaling-group', launch_template={'LaunchTemplateName': 'my-template-for-auto-scaling', 'Version': '2'}, min_size=1, max_size=5, new_instances_protected_from_scale_in=True)
        """

        def _handler(
            req: "OperationRequest[capo_auto_scaling.types.update_auto_scaling_group_type.UpdateAutoScalingGroupType]",
        ) -> OperationResponse[None]:
            import capo_auto_scaling._operations.auto_scaling_2011_01_01.update_auto_scaling_group

            output, http_response = (
                capo_auto_scaling._operations.auto_scaling_2011_01_01.update_auto_scaling_group.update_auto_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auto_scaling.types.update_auto_scaling_group_type.UpdateAutoScalingGroupType = {}
        if auto_scaling_group_name is not None:
            input_["auto_scaling_group_name"] = auto_scaling_group_name
        if launch_configuration_name is not None:
            input_["launch_configuration_name"] = launch_configuration_name
        if launch_template is not None:
            input_["launch_template"] = launch_template
        if mixed_instances_policy is not None:
            input_["mixed_instances_policy"] = mixed_instances_policy
        if min_size is not None:
            input_["min_size"] = min_size
        if max_size is not None:
            input_["max_size"] = max_size
        if desired_capacity is not None:
            input_["desired_capacity"] = desired_capacity
        if default_cooldown is not None:
            input_["default_cooldown"] = default_cooldown
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if availability_zone_ids is not None:
            input_["availability_zone_ids"] = availability_zone_ids
        if health_check_type is not None:
            input_["health_check_type"] = health_check_type
        if health_check_grace_period is not None:
            input_["health_check_grace_period"] = health_check_grace_period
        if placement_group is not None:
            input_["placement_group"] = placement_group
        if vpc_zone_identifier is not None:
            input_["vpc_zone_identifier"] = vpc_zone_identifier
        if termination_policies is not None:
            input_["termination_policies"] = termination_policies
        if new_instances_protected_from_scale_in is not None:
            input_["new_instances_protected_from_scale_in"] = (
                new_instances_protected_from_scale_in
            )
        if service_linked_role_arn is not None:
            input_["service_linked_role_arn"] = service_linked_role_arn
        if max_instance_lifetime is not None:
            input_["max_instance_lifetime"] = max_instance_lifetime
        if capacity_rebalance is not None:
            input_["capacity_rebalance"] = capacity_rebalance
        if context is not None:
            input_["context"] = context
        if desired_capacity_type is not None:
            input_["desired_capacity_type"] = desired_capacity_type
        if default_instance_warmup is not None:
            input_["default_instance_warmup"] = default_instance_warmup
        if instance_maintenance_policy is not None:
            input_["instance_maintenance_policy"] = instance_maintenance_policy
        if availability_zone_distribution is not None:
            input_["availability_zone_distribution"] = availability_zone_distribution
        if availability_zone_impairment_policy is not None:
            input_["availability_zone_impairment_policy"] = (
                availability_zone_impairment_policy
            )
        if skip_zonal_shift_validation is not None:
            input_["skip_zonal_shift_validation"] = skip_zonal_shift_validation
        if capacity_reservation_specification is not None:
            input_["capacity_reservation_specification"] = (
                capacity_reservation_specification
            )
        if instance_lifecycle_policy is not None:
            input_["instance_lifecycle_policy"] = instance_lifecycle_policy
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

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

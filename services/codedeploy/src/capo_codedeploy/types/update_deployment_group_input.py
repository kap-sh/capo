"""Generated from Smithy shape ``com.amazonaws.codedeploy#UpdateDeploymentGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codedeploy.types.alarm_configuration
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.auto_rollback_configuration
    import capo_codedeploy.types.auto_scaling_group_name_list
    import capo_codedeploy.types.blue_green_deployment_configuration
    import capo_codedeploy.types.deployment_config_name
    import capo_codedeploy.types.deployment_group_name
    import capo_codedeploy.types.deployment_style
    import capo_codedeploy.types.ec2_tag_filter_list
    import capo_codedeploy.types.ec2_tag_set
    import capo_codedeploy.types.ecs_service_list
    import capo_codedeploy.types.load_balancer_info
    import capo_codedeploy.types.nullable_boolean
    import capo_codedeploy.types.on_premises_tag_set
    import capo_codedeploy.types.outdated_instances_strategy
    import capo_codedeploy.types.role
    import capo_codedeploy.types.tag_filter_list
    import capo_codedeploy.types.trigger_config_list


class UpdateDeploymentGroupInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p>The application name that corresponds to the deployment group to update.</p>"""
    current_deployment_group_name: (
        "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
    )
    """<p>The current name of the deployment group.</p>"""
    new_deployment_group_name: NotRequired[
        "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
    ]
    """<p>The new name of the deployment group, if you want to change it.</p>"""
    deployment_config_name: NotRequired[
        "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    """<p>The replacement deployment configuration name to use, if you want to change it.</p>"""
    ec2_tag_filters: NotRequired[
        "capo_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
    ]
    """<p>The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.</p>"""
    on_premises_instance_tag_filters: NotRequired[
        "capo_codedeploy.types.tag_filter_list.TagFilterList"
    ]
    """<p>The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.</p>"""
    auto_scaling_groups: NotRequired[
        "capo_codedeploy.types.auto_scaling_group_name_list.AutoScalingGroupNameList"
    ]
    """<p>The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them.</p> <ul> <li> <p>To keep the Auto Scaling groups, enter their names or do not specify this parameter. </p> </li> <li> <p>To remove Auto Scaling groups, specify a non-null empty list of Auto Scaling group names to detach all CodeDeploy-managed Auto Scaling lifecycle hooks. For examples, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-auto-scaling.html#troubleshooting-auto-scaling-heartbeat">Amazon EC2 instances in an Amazon EC2 Auto Scaling group fail to launch and receive the error "Heartbeat Timeout"</a> in the <i>CodeDeploy User Guide</i>.</p> </li> </ul>"""
    service_role_arn: NotRequired["capo_codedeploy.types.role.Role"]
    """<p>A replacement ARN for the service role, if you want to change it.</p>"""
    trigger_configurations: NotRequired[
        "capo_codedeploy.types.trigger_config_list.TriggerConfigList"
    ]
    """<p>Information about triggers to change when the deployment group is updated. For examples, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-edit.html">Edit a Trigger in a CodeDeploy Deployment Group</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    alarm_configuration: NotRequired[
        "capo_codedeploy.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.</p>"""
    auto_rollback_configuration: NotRequired[
        "capo_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
    ]
    """<p>Information for an automatic rollback configuration that is added or changed when a deployment group is updated.</p>"""
    outdated_instances_strategy: NotRequired[
        "capo_codedeploy.types.outdated_instances_strategy.OutdatedInstancesStrategy"
    ]
    """<p>Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.</p> <p>If this option is set to <code>UPDATE</code> or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.</p> <p>If this option is set to <code>IGNORE</code>, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.</p>"""
    deployment_style: NotRequired[
        "capo_codedeploy.types.deployment_style.DeploymentStyle"
    ]
    """<p>Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.</p>"""
    blue_green_deployment_configuration: NotRequired[
        "capo_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
    ]
    """<p>Information about blue/green deployment options for a deployment group.</p>"""
    load_balancer_info: NotRequired[
        "capo_codedeploy.types.load_balancer_info.LoadBalancerInfo"
    ]
    """<p>Information about the load balancer used in a deployment.</p>"""
    ec2_tag_set: NotRequired["capo_codedeploy.types.ec2_tag_set.EC2TagSet"]
    """<p>Information about groups of tags applied to on-premises instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups.</p>"""
    ecs_services: NotRequired["capo_codedeploy.types.ecs_service_list.ECSServiceList"]
    """<p> The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <code><clustername>:<servicename></code>. </p>"""
    on_premises_tag_set: NotRequired[
        "capo_codedeploy.types.on_premises_tag_set.OnPremisesTagSet"
    ]
    """<p>Information about an on-premises instance tag set. The deployment group includes only on-premises instances identified by all the tag groups.</p>"""
    termination_hook_enabled: NotRequired[
        "capo_codedeploy.types.nullable_boolean.NullableBoolean"
    ]
    """<p>This parameter only applies if you are using CodeDeploy with Amazon EC2 Auto Scaling. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html">Integrating CodeDeploy with Amazon EC2 Auto Scaling</a> in the <i>CodeDeploy User Guide</i>.</p> <p>Set <code>terminationHookEnabled</code> to <code>true</code> to have CodeDeploy install a termination hook into your Auto Scaling group when you update a deployment group. When this hook is installed, CodeDeploy will perform termination deployments.</p> <p>For information about termination deployments, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable">Enabling termination deployments during Auto Scaling scale-in events</a> in the <i>CodeDeploy User Guide</i>.</p> <p>For more information about Auto Scaling scale-in events, see the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html#as-lifecycle-scale-in">Scale in</a> topic in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDeploymentGroupInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    out["currentDeploymentGroupName"] = value["current_deployment_group_name"]
    if "new_deployment_group_name" in value:
        out["newDeploymentGroupName"] = value["new_deployment_group_name"]
    if "deployment_config_name" in value:
        out["deploymentConfigName"] = value["deployment_config_name"]
    if "ec2_tag_filters" in value:
        import capo_codedeploy.types.ec2_tag_filter_list

        out["ec2TagFilters"] = (
            capo_codedeploy.types.ec2_tag_filter_list.serialize_aws_json_1_1(
                value["ec2_tag_filters"]
            )
        )
    if "on_premises_instance_tag_filters" in value:
        import capo_codedeploy.types.tag_filter_list

        out["onPremisesInstanceTagFilters"] = (
            capo_codedeploy.types.tag_filter_list.serialize_aws_json_1_1(
                value["on_premises_instance_tag_filters"]
            )
        )
    if "auto_scaling_groups" in value:
        import capo_codedeploy.types.auto_scaling_group_name_list

        out["autoScalingGroups"] = (
            capo_codedeploy.types.auto_scaling_group_name_list.serialize_aws_json_1_1(
                value["auto_scaling_groups"]
            )
        )
    if "service_role_arn" in value:
        out["serviceRoleArn"] = value["service_role_arn"]
    if "trigger_configurations" in value:
        import capo_codedeploy.types.trigger_config_list

        out["triggerConfigurations"] = (
            capo_codedeploy.types.trigger_config_list.serialize_aws_json_1_1(
                value["trigger_configurations"]
            )
        )
    if "alarm_configuration" in value:
        import capo_codedeploy.types.alarm_configuration

        out["alarmConfiguration"] = (
            capo_codedeploy.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "auto_rollback_configuration" in value:
        import capo_codedeploy.types.auto_rollback_configuration

        out["autoRollbackConfiguration"] = (
            capo_codedeploy.types.auto_rollback_configuration.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    if "outdated_instances_strategy" in value:
        import capo_codedeploy.types.outdated_instances_strategy

        out["outdatedInstancesStrategy"] = (
            capo_codedeploy.types.outdated_instances_strategy.serialize_aws_json_1_1(
                value["outdated_instances_strategy"]
            )
        )
    if "deployment_style" in value:
        import capo_codedeploy.types.deployment_style

        out["deploymentStyle"] = (
            capo_codedeploy.types.deployment_style.serialize_aws_json_1_1(
                value["deployment_style"]
            )
        )
    if "blue_green_deployment_configuration" in value:
        import capo_codedeploy.types.blue_green_deployment_configuration

        out["blueGreenDeploymentConfiguration"] = (
            capo_codedeploy.types.blue_green_deployment_configuration.serialize_aws_json_1_1(
                value["blue_green_deployment_configuration"]
            )
        )
    if "load_balancer_info" in value:
        import capo_codedeploy.types.load_balancer_info

        out["loadBalancerInfo"] = (
            capo_codedeploy.types.load_balancer_info.serialize_aws_json_1_1(
                value["load_balancer_info"]
            )
        )
    if "ec2_tag_set" in value:
        import capo_codedeploy.types.ec2_tag_set

        out["ec2TagSet"] = capo_codedeploy.types.ec2_tag_set.serialize_aws_json_1_1(
            value["ec2_tag_set"]
        )
    if "ecs_services" in value:
        import capo_codedeploy.types.ecs_service_list

        out["ecsServices"] = (
            capo_codedeploy.types.ecs_service_list.serialize_aws_json_1_1(
                value["ecs_services"]
            )
        )
    if "on_premises_tag_set" in value:
        import capo_codedeploy.types.on_premises_tag_set

        out["onPremisesTagSet"] = (
            capo_codedeploy.types.on_premises_tag_set.serialize_aws_json_1_1(
                value["on_premises_tag_set"]
            )
        )
    if "termination_hook_enabled" in value:
        out["terminationHookEnabled"] = value["termination_hook_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDeploymentGroupInput:
    out: UpdateDeploymentGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "UpdateDeploymentGroupInput.application_name required"
        )
    if data.get("currentDeploymentGroupName") is not None:
        out["current_deployment_group_name"] = data["currentDeploymentGroupName"]
    else:
        raise DeserializationError(
            "UpdateDeploymentGroupInput.current_deployment_group_name required"
        )
    if data.get("newDeploymentGroupName") is not None:
        out["new_deployment_group_name"] = data["newDeploymentGroupName"]
    if data.get("deploymentConfigName") is not None:
        out["deployment_config_name"] = data["deploymentConfigName"]
    if data.get("ec2TagFilters") is not None:
        import capo_codedeploy.types.ec2_tag_filter_list

        out["ec2_tag_filters"] = (
            capo_codedeploy.types.ec2_tag_filter_list.deserialize_aws_json_1_1(
                data["ec2TagFilters"]
            )
        )
    if data.get("onPremisesInstanceTagFilters") is not None:
        import capo_codedeploy.types.tag_filter_list

        out["on_premises_instance_tag_filters"] = (
            capo_codedeploy.types.tag_filter_list.deserialize_aws_json_1_1(
                data["onPremisesInstanceTagFilters"]
            )
        )
    if data.get("autoScalingGroups") is not None:
        import capo_codedeploy.types.auto_scaling_group_name_list

        out["auto_scaling_groups"] = (
            capo_codedeploy.types.auto_scaling_group_name_list.deserialize_aws_json_1_1(
                data["autoScalingGroups"]
            )
        )
    if data.get("serviceRoleArn") is not None:
        out["service_role_arn"] = data["serviceRoleArn"]
    if data.get("triggerConfigurations") is not None:
        import capo_codedeploy.types.trigger_config_list

        out["trigger_configurations"] = (
            capo_codedeploy.types.trigger_config_list.deserialize_aws_json_1_1(
                data["triggerConfigurations"]
            )
        )
    if data.get("alarmConfiguration") is not None:
        import capo_codedeploy.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_codedeploy.types.alarm_configuration.deserialize_aws_json_1_1(
                data["alarmConfiguration"]
            )
        )
    if data.get("autoRollbackConfiguration") is not None:
        import capo_codedeploy.types.auto_rollback_configuration

        out["auto_rollback_configuration"] = (
            capo_codedeploy.types.auto_rollback_configuration.deserialize_aws_json_1_1(
                data["autoRollbackConfiguration"]
            )
        )
    if data.get("outdatedInstancesStrategy") is not None:
        import capo_codedeploy.types.outdated_instances_strategy

        out["outdated_instances_strategy"] = (
            capo_codedeploy.types.outdated_instances_strategy.deserialize_aws_json_1_1(
                data["outdatedInstancesStrategy"]
            )
        )
    if data.get("deploymentStyle") is not None:
        import capo_codedeploy.types.deployment_style

        out["deployment_style"] = (
            capo_codedeploy.types.deployment_style.deserialize_aws_json_1_1(
                data["deploymentStyle"]
            )
        )
    if data.get("blueGreenDeploymentConfiguration") is not None:
        import capo_codedeploy.types.blue_green_deployment_configuration

        out["blue_green_deployment_configuration"] = (
            capo_codedeploy.types.blue_green_deployment_configuration.deserialize_aws_json_1_1(
                data["blueGreenDeploymentConfiguration"]
            )
        )
    if data.get("loadBalancerInfo") is not None:
        import capo_codedeploy.types.load_balancer_info

        out["load_balancer_info"] = (
            capo_codedeploy.types.load_balancer_info.deserialize_aws_json_1_1(
                data["loadBalancerInfo"]
            )
        )
    if data.get("ec2TagSet") is not None:
        import capo_codedeploy.types.ec2_tag_set

        out["ec2_tag_set"] = capo_codedeploy.types.ec2_tag_set.deserialize_aws_json_1_1(
            data["ec2TagSet"]
        )
    if data.get("ecsServices") is not None:
        import capo_codedeploy.types.ecs_service_list

        out["ecs_services"] = (
            capo_codedeploy.types.ecs_service_list.deserialize_aws_json_1_1(
                data["ecsServices"]
            )
        )
    if data.get("onPremisesTagSet") is not None:
        import capo_codedeploy.types.on_premises_tag_set

        out["on_premises_tag_set"] = (
            capo_codedeploy.types.on_premises_tag_set.deserialize_aws_json_1_1(
                data["onPremisesTagSet"]
            )
        )
    if data.get("terminationHookEnabled") is not None:
        out["termination_hook_enabled"] = data["terminationHookEnabled"]
    return out

"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentGroupInput``."""

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
    import capo_codedeploy.types.tag_list
    import capo_codedeploy.types.trigger_config_list


class CreateDeploymentGroupInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""
    deployment_group_name: (
        "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
    )
    """<p>The name of a new deployment group for the specified application.</p>"""
    deployment_config_name: NotRequired[
        "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    """<p>If specified, the deployment configuration name can be either one of the predefined configurations provided with CodeDeploy or a custom deployment configuration that you create by calling the create deployment configuration operation.</p> <p> <code>CodeDeployDefault.OneAtATime</code> is the default deployment configuration. It is used if a configuration isn't specified for the deployment or deployment group.</p> <p>For more information about the predefined deployment configurations in CodeDeploy, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html">Working with Deployment Configurations in CodeDeploy</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    ec2_tag_filters: NotRequired[
        "capo_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
    ]
    """<p>The Amazon EC2 tags on which to filter. The deployment group includes Amazon EC2 instances with any of the specified tags. Cannot be used in the same call as ec2TagSet.</p>"""
    on_premises_instance_tag_filters: NotRequired[
        "capo_codedeploy.types.tag_filter_list.TagFilterList"
    ]
    """<p>The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags. Cannot be used in the same call as <code>OnPremisesTagSet</code>.</p>"""
    auto_scaling_groups: NotRequired[
        "capo_codedeploy.types.auto_scaling_group_name_list.AutoScalingGroupNameList"
    ]
    """<p>A list of associated Amazon EC2 Auto Scaling groups.</p>"""
    service_role_arn: "capo_codedeploy.types.role.Role"
    """<p>A service role Amazon Resource Name (ARN) that allows CodeDeploy to act on the user's behalf when interacting with Amazon Web Services services.</p>"""
    trigger_configurations: NotRequired[
        "capo_codedeploy.types.trigger_config_list.TriggerConfigList"
    ]
    """<p>Information about triggers to create when the deployment group is created. For examples, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-sns.html">Create a Trigger for an CodeDeploy Event</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    alarm_configuration: NotRequired[
        "capo_codedeploy.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>Information to add about Amazon CloudWatch alarms when the deployment group is created.</p>"""
    auto_rollback_configuration: NotRequired[
        "capo_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
    ]
    """<p>Configuration information for an automatic rollback that is added when a deployment group is created.</p>"""
    outdated_instances_strategy: NotRequired[
        "capo_codedeploy.types.outdated_instances_strategy.OutdatedInstancesStrategy"
    ]
    """<p>Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.</p> <p>If this option is set to <code>UPDATE</code> or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.</p> <p>If this option is set to <code>IGNORE</code>, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.</p>"""
    deployment_style: NotRequired[
        "capo_codedeploy.types.deployment_style.DeploymentStyle"
    ]
    """<p>Information about the type of deployment, in-place or blue/green, that you want to run and whether to route deployment traffic behind a load balancer.</p>"""
    blue_green_deployment_configuration: NotRequired[
        "capo_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
    ]
    """<p>Information about blue/green deployment options for a deployment group.</p>"""
    load_balancer_info: NotRequired[
        "capo_codedeploy.types.load_balancer_info.LoadBalancerInfo"
    ]
    """<p>Information about the load balancer used in a deployment.</p>"""
    ec2_tag_set: NotRequired["capo_codedeploy.types.ec2_tag_set.EC2TagSet"]
    """<p>Information about groups of tags applied to Amazon EC2 instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups. Cannot be used in the same call as <code>ec2TagFilters</code>.</p>"""
    ecs_services: NotRequired["capo_codedeploy.types.ecs_service_list.ECSServiceList"]
    """<p> The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <code><clustername>:<servicename></code>. </p>"""
    on_premises_tag_set: NotRequired[
        "capo_codedeploy.types.on_premises_tag_set.OnPremisesTagSet"
    ]
    """<p>Information about groups of tags applied to on-premises instances. The deployment group includes only on-premises instances identified by all of the tag groups. Cannot be used in the same call as <code>onPremisesInstanceTagFilters</code>.</p>"""
    tags: NotRequired["capo_codedeploy.types.tag_list.TagList"]
    """<p> The metadata that you apply to CodeDeploy deployment groups to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define. </p>"""
    termination_hook_enabled: NotRequired[
        "capo_codedeploy.types.nullable_boolean.NullableBoolean"
    ]
    """<p>This parameter only applies if you are using CodeDeploy with Amazon EC2 Auto Scaling. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html">Integrating CodeDeploy with Amazon EC2 Auto Scaling</a> in the <i>CodeDeploy User Guide</i>.</p> <p>Set <code>terminationHookEnabled</code> to <code>true</code> to have CodeDeploy install a termination hook into your Auto Scaling group when you create a deployment group. When this hook is installed, CodeDeploy will perform termination deployments.</p> <p>For information about termination deployments, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable">Enabling termination deployments during Auto Scaling scale-in events</a> in the <i>CodeDeploy User Guide</i>.</p> <p>For more information about Auto Scaling scale-in events, see the <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html#as-lifecycle-scale-in">Scale in</a> topic in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeploymentGroupInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    out["deploymentGroupName"] = value["deployment_group_name"]
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
    if "tags" in value:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "termination_hook_enabled" in value:
        out["terminationHookEnabled"] = value["termination_hook_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeploymentGroupInput:
    out: CreateDeploymentGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "CreateDeploymentGroupInput.application_name required"
        )
    if data.get("deploymentGroupName") is not None:
        out["deployment_group_name"] = data["deploymentGroupName"]
    else:
        raise DeserializationError(
            "CreateDeploymentGroupInput.deployment_group_name required"
        )
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
    else:
        raise DeserializationError(
            "CreateDeploymentGroupInput.service_role_arn required"
        )
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
    if data.get("tags") is not None:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("terminationHookEnabled") is not None:
        out["termination_hook_enabled"] = data["terminationHookEnabled"]
    return out

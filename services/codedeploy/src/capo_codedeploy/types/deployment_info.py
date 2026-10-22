"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.additional_deployment_status_info
    import capo_codedeploy.types.alarm_configuration
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.auto_rollback_configuration
    import capo_codedeploy.types.blue_green_deployment_configuration
    import capo_codedeploy.types.boolean
    import capo_codedeploy.types.compute_platform
    import capo_codedeploy.types.deployment_config_name
    import capo_codedeploy.types.deployment_creator
    import capo_codedeploy.types.deployment_group_name
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.deployment_mode
    import capo_codedeploy.types.deployment_overview
    import capo_codedeploy.types.deployment_status
    import capo_codedeploy.types.deployment_status_message_list
    import capo_codedeploy.types.deployment_style
    import capo_codedeploy.types.description
    import capo_codedeploy.types.ec2_deployment_options
    import capo_codedeploy.types.error_information
    import capo_codedeploy.types.external_id
    import capo_codedeploy.types.file_exists_behavior
    import capo_codedeploy.types.load_balancer_info
    import capo_codedeploy.types.related_deployments
    import capo_codedeploy.types.revision_location
    import capo_codedeploy.types.rollback_info
    import capo_codedeploy.types.target_instances
    import capo_codedeploy.types.timestamp


class DeploymentInfo(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_codedeploy.types.application_name.ApplicationName"
    ]
    """<p>The application name.</p>"""
    deployment_group_name: NotRequired[
        "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
    ]
    """<p> The deployment group name. </p>"""
    deployment_config_name: NotRequired[
        "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    """<p> The deployment configuration name. </p>"""
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    previous_revision: NotRequired[
        "capo_codedeploy.types.revision_location.RevisionLocation"
    ]
    """<p>Information about the application revision that was deployed to the deployment group before the most recent successful deployment.</p>"""
    revision: NotRequired["capo_codedeploy.types.revision_location.RevisionLocation"]
    """<p>Information about the location of stored application artifacts and the service from which to retrieve them.</p>"""
    status: NotRequired["capo_codedeploy.types.deployment_status.DeploymentStatus"]
    """<p>The current state of the deployment as a whole.</p>"""
    error_information: NotRequired[
        "capo_codedeploy.types.error_information.ErrorInformation"
    ]
    """<p>Information about any error associated with this deployment.</p>"""
    create_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment was created.</p>"""
    start_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment was deployed to the deployment group.</p> <p>In some cases, the reported value of the start time might be later than the complete time. This is due to differences in the clock settings of backend servers that participate in the deployment process.</p>"""
    complete_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment was complete.</p>"""
    deployment_overview: NotRequired[
        "capo_codedeploy.types.deployment_overview.DeploymentOverview"
    ]
    """<p>A summary of the deployment status of the instances in the deployment.</p>"""
    description: NotRequired["capo_codedeploy.types.description.Description"]
    """<p>A comment about the deployment.</p>"""
    creator: NotRequired["capo_codedeploy.types.deployment_creator.DeploymentCreator"]
    """<p>The means by which the deployment was created:</p> <ul> <li> <p> <code>user</code>: A user created the deployment.</p> </li> <li> <p> <code>autoscaling</code>: Amazon EC2 Auto Scaling created the deployment.</p> </li> <li> <p> <code>codeDeployRollback</code>: A rollback process created the deployment.</p> </li> <li> <p> <code>CodeDeployAutoUpdate</code>: An auto-update process created the deployment when it detected outdated Amazon EC2 instances.</p> </li> </ul>"""
    ignore_application_stop_failures: "capo_codedeploy.types.boolean.Boolean"
    """<p> If true, then if an <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, or <code>AfterBlockTraffic</code> deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if <code>ApplicationStop</code> fails, the deployment continues with DownloadBundle. If <code>BeforeBlockTraffic</code> fails, the deployment continues with <code>BlockTraffic</code>. If <code>AfterBlockTraffic</code> fails, the deployment continues with <code>ApplicationStop</code>. </p> <p> If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted. </p> <p> During a deployment, the CodeDeploy agent runs the scripts specified for <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail. </p> <p> If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use <code>ignoreApplicationStopFailures</code> to specify that the <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> failures should be ignored. </p>"""
    auto_rollback_configuration: NotRequired[
        "capo_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
    ]
    """<p>Information about the automatic rollback configuration associated with the deployment.</p>"""
    update_outdated_instances_only: "capo_codedeploy.types.boolean.Boolean"
    """<p>Indicates whether only instances that are not running the latest application revision are to be deployed to.</p>"""
    rollback_info: NotRequired["capo_codedeploy.types.rollback_info.RollbackInfo"]
    """<p>Information about a deployment rollback.</p>"""
    deployment_style: NotRequired[
        "capo_codedeploy.types.deployment_style.DeploymentStyle"
    ]
    """<p>Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.</p>"""
    target_instances: NotRequired[
        "capo_codedeploy.types.target_instances.TargetInstances"
    ]
    """<p>Information about the instances that belong to the replacement environment in a blue/green deployment.</p>"""
    instance_termination_wait_time_started: "capo_codedeploy.types.boolean.Boolean"
    """<p>Indicates whether the wait period set for the termination of instances in the original environment has started. Status is 'false' if the KEEP_ALIVE option is specified. Otherwise, 'true' as soon as the termination wait period starts.</p>"""
    blue_green_deployment_configuration: NotRequired[
        "capo_codedeploy.types.blue_green_deployment_configuration.BlueGreenDeploymentConfiguration"
    ]
    """<p>Information about blue/green deployment options for this deployment.</p>"""
    load_balancer_info: NotRequired[
        "capo_codedeploy.types.load_balancer_info.LoadBalancerInfo"
    ]
    """<p>Information about the load balancer used in the deployment.</p>"""
    additional_deployment_status_info: NotRequired[
        "capo_codedeploy.types.additional_deployment_status_info.AdditionalDeploymentStatusInfo"
    ]
    """<p>Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.</p>"""
    file_exists_behavior: NotRequired[
        "capo_codedeploy.types.file_exists_behavior.FileExistsBehavior"
    ]
    """<p>Information about how CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.</p> <ul> <li> <p> <code>DISALLOW</code>: The deployment fails. This is also the default behavior if no option is specified.</p> </li> <li> <p> <code>OVERWRITE</code>: The version of the file from the application revision currently being deployed replaces the version already on the instance.</p> </li> <li> <p> <code>RETAIN</code>: The version of the file already on the instance is kept and used as part of the new deployment.</p> </li> </ul>"""
    deployment_mode: NotRequired["capo_codedeploy.types.deployment_mode.DeploymentMode"]
    """<p>The deployment's type. Valid values are:</p> <ul> <li> <p> <code>STANDARD</code>: The deployment installed the specified revision.</p> </li> <li> <p> <code>RESTART</code>: The deployment restarted the application on the target instances using the revision from the deployment group's last successful deployment, without downloading a new revision.</p> </li> </ul> <p>This field is absent for deployments created before <code>deploymentMode</code> existed, and for <code>STANDARD</code> deployments. An absent value must not be interpreted as <code>STANDARD</code>; it simply means no value was recorded either way.</p>"""
    deployment_status_messages: NotRequired[
        "capo_codedeploy.types.deployment_status_message_list.DeploymentStatusMessageList"
    ]
    """<p>Messages that contain information about the status of a deployment.</p>"""
    compute_platform: NotRequired[
        "capo_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p>The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>"""
    external_id: NotRequired["capo_codedeploy.types.external_id.ExternalId"]
    """<p>The unique ID for an external resource (for example, a CloudFormation stack ID) that is linked to this deployment.</p>"""
    related_deployments: NotRequired[
        "capo_codedeploy.types.related_deployments.RelatedDeployments"
    ]
    override_alarm_configuration: NotRequired[
        "capo_codedeploy.types.alarm_configuration.AlarmConfiguration"
    ]
    ec2_deployment_options: NotRequired[
        "capo_codedeploy.types.ec2_deployment_options.EC2DeploymentOptions"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentInfo) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "deployment_group_name" in value:
        out["deploymentGroupName"] = value["deployment_group_name"]
    if "deployment_config_name" in value:
        out["deploymentConfigName"] = value["deployment_config_name"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "previous_revision" in value:
        import capo_codedeploy.types.revision_location

        out["previousRevision"] = (
            capo_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["previous_revision"]
            )
        )
    if "revision" in value:
        import capo_codedeploy.types.revision_location

        out["revision"] = (
            capo_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["revision"]
            )
        )
    if "status" in value:
        import capo_codedeploy.types.deployment_status

        out["status"] = capo_codedeploy.types.deployment_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_information" in value:
        import capo_codedeploy.types.error_information

        out["errorInformation"] = (
            capo_codedeploy.types.error_information.serialize_aws_json_1_1(
                value["error_information"]
            )
        )
    if "create_time" in value:
        import capo_codedeploy.types.timestamp

        out["createTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "start_time" in value:
        import capo_codedeploy.types.timestamp

        out["startTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "complete_time" in value:
        import capo_codedeploy.types.timestamp

        out["completeTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["complete_time"]
        )
    if "deployment_overview" in value:
        import capo_codedeploy.types.deployment_overview

        out["deploymentOverview"] = (
            capo_codedeploy.types.deployment_overview.serialize_aws_json_1_1(
                value["deployment_overview"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "creator" in value:
        import capo_codedeploy.types.deployment_creator

        out["creator"] = (
            capo_codedeploy.types.deployment_creator.serialize_aws_json_1_1(
                value["creator"]
            )
        )
    out["ignoreApplicationStopFailures"] = value.get(
        "ignore_application_stop_failures", False
    )
    if "auto_rollback_configuration" in value:
        import capo_codedeploy.types.auto_rollback_configuration

        out["autoRollbackConfiguration"] = (
            capo_codedeploy.types.auto_rollback_configuration.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    out["updateOutdatedInstancesOnly"] = value.get(
        "update_outdated_instances_only", False
    )
    if "rollback_info" in value:
        import capo_codedeploy.types.rollback_info

        out["rollbackInfo"] = (
            capo_codedeploy.types.rollback_info.serialize_aws_json_1_1(
                value["rollback_info"]
            )
        )
    if "deployment_style" in value:
        import capo_codedeploy.types.deployment_style

        out["deploymentStyle"] = (
            capo_codedeploy.types.deployment_style.serialize_aws_json_1_1(
                value["deployment_style"]
            )
        )
    if "target_instances" in value:
        import capo_codedeploy.types.target_instances

        out["targetInstances"] = (
            capo_codedeploy.types.target_instances.serialize_aws_json_1_1(
                value["target_instances"]
            )
        )
    out["instanceTerminationWaitTimeStarted"] = value.get(
        "instance_termination_wait_time_started", False
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
    if "additional_deployment_status_info" in value:
        out["additionalDeploymentStatusInfo"] = value[
            "additional_deployment_status_info"
        ]
    if "file_exists_behavior" in value:
        import capo_codedeploy.types.file_exists_behavior

        out["fileExistsBehavior"] = (
            capo_codedeploy.types.file_exists_behavior.serialize_aws_json_1_1(
                value["file_exists_behavior"]
            )
        )
    if "deployment_mode" in value:
        import capo_codedeploy.types.deployment_mode

        out["deploymentMode"] = (
            capo_codedeploy.types.deployment_mode.serialize_aws_json_1_1(
                value["deployment_mode"]
            )
        )
    if "deployment_status_messages" in value:
        import capo_codedeploy.types.deployment_status_message_list

        out["deploymentStatusMessages"] = (
            capo_codedeploy.types.deployment_status_message_list.serialize_aws_json_1_1(
                value["deployment_status_messages"]
            )
        )
    if "compute_platform" in value:
        import capo_codedeploy.types.compute_platform

        out["computePlatform"] = (
            capo_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
            )
        )
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "related_deployments" in value:
        import capo_codedeploy.types.related_deployments

        out["relatedDeployments"] = (
            capo_codedeploy.types.related_deployments.serialize_aws_json_1_1(
                value["related_deployments"]
            )
        )
    if "override_alarm_configuration" in value:
        import capo_codedeploy.types.alarm_configuration

        out["overrideAlarmConfiguration"] = (
            capo_codedeploy.types.alarm_configuration.serialize_aws_json_1_1(
                value["override_alarm_configuration"]
            )
        )
    if "ec2_deployment_options" in value:
        import capo_codedeploy.types.ec2_deployment_options

        out["ec2DeploymentOptions"] = (
            capo_codedeploy.types.ec2_deployment_options.serialize_aws_json_1_1(
                value["ec2_deployment_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentInfo:
    out: DeploymentInfo = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("deploymentGroupName") is not None:
        out["deployment_group_name"] = data["deploymentGroupName"]
    if data.get("deploymentConfigName") is not None:
        out["deployment_config_name"] = data["deploymentConfigName"]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("previousRevision") is not None:
        import capo_codedeploy.types.revision_location

        out["previous_revision"] = (
            capo_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["previousRevision"]
            )
        )
    if data.get("revision") is not None:
        import capo_codedeploy.types.revision_location

        out["revision"] = (
            capo_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revision"]
            )
        )
    if data.get("status") is not None:
        import capo_codedeploy.types.deployment_status

        out["status"] = (
            capo_codedeploy.types.deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("errorInformation") is not None:
        import capo_codedeploy.types.error_information

        out["error_information"] = (
            capo_codedeploy.types.error_information.deserialize_aws_json_1_1(
                data["errorInformation"]
            )
        )
    if data.get("createTime") is not None:
        import capo_codedeploy.types.timestamp

        out["create_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["createTime"]
        )
    if data.get("startTime") is not None:
        import capo_codedeploy.types.timestamp

        out["start_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("completeTime") is not None:
        import capo_codedeploy.types.timestamp

        out["complete_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["completeTime"]
        )
    if data.get("deploymentOverview") is not None:
        import capo_codedeploy.types.deployment_overview

        out["deployment_overview"] = (
            capo_codedeploy.types.deployment_overview.deserialize_aws_json_1_1(
                data["deploymentOverview"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creator") is not None:
        import capo_codedeploy.types.deployment_creator

        out["creator"] = (
            capo_codedeploy.types.deployment_creator.deserialize_aws_json_1_1(
                data["creator"]
            )
        )
    if data.get("ignoreApplicationStopFailures") is not None:
        out["ignore_application_stop_failures"] = data["ignoreApplicationStopFailures"]
    else:
        out["ignore_application_stop_failures"] = False
    if data.get("autoRollbackConfiguration") is not None:
        import capo_codedeploy.types.auto_rollback_configuration

        out["auto_rollback_configuration"] = (
            capo_codedeploy.types.auto_rollback_configuration.deserialize_aws_json_1_1(
                data["autoRollbackConfiguration"]
            )
        )
    if data.get("updateOutdatedInstancesOnly") is not None:
        out["update_outdated_instances_only"] = data["updateOutdatedInstancesOnly"]
    else:
        out["update_outdated_instances_only"] = False
    if data.get("rollbackInfo") is not None:
        import capo_codedeploy.types.rollback_info

        out["rollback_info"] = (
            capo_codedeploy.types.rollback_info.deserialize_aws_json_1_1(
                data["rollbackInfo"]
            )
        )
    if data.get("deploymentStyle") is not None:
        import capo_codedeploy.types.deployment_style

        out["deployment_style"] = (
            capo_codedeploy.types.deployment_style.deserialize_aws_json_1_1(
                data["deploymentStyle"]
            )
        )
    if data.get("targetInstances") is not None:
        import capo_codedeploy.types.target_instances

        out["target_instances"] = (
            capo_codedeploy.types.target_instances.deserialize_aws_json_1_1(
                data["targetInstances"]
            )
        )
    if data.get("instanceTerminationWaitTimeStarted") is not None:
        out["instance_termination_wait_time_started"] = data[
            "instanceTerminationWaitTimeStarted"
        ]
    else:
        out["instance_termination_wait_time_started"] = False
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
    if data.get("additionalDeploymentStatusInfo") is not None:
        out["additional_deployment_status_info"] = data[
            "additionalDeploymentStatusInfo"
        ]
    if data.get("fileExistsBehavior") is not None:
        import capo_codedeploy.types.file_exists_behavior

        out["file_exists_behavior"] = (
            capo_codedeploy.types.file_exists_behavior.deserialize_aws_json_1_1(
                data["fileExistsBehavior"]
            )
        )
    if data.get("deploymentMode") is not None:
        import capo_codedeploy.types.deployment_mode

        out["deployment_mode"] = (
            capo_codedeploy.types.deployment_mode.deserialize_aws_json_1_1(
                data["deploymentMode"]
            )
        )
    if data.get("deploymentStatusMessages") is not None:
        import capo_codedeploy.types.deployment_status_message_list

        out["deployment_status_messages"] = (
            capo_codedeploy.types.deployment_status_message_list.deserialize_aws_json_1_1(
                data["deploymentStatusMessages"]
            )
        )
    if data.get("computePlatform") is not None:
        import capo_codedeploy.types.compute_platform

        out["compute_platform"] = (
            capo_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
            )
        )
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("relatedDeployments") is not None:
        import capo_codedeploy.types.related_deployments

        out["related_deployments"] = (
            capo_codedeploy.types.related_deployments.deserialize_aws_json_1_1(
                data["relatedDeployments"]
            )
        )
    if data.get("overrideAlarmConfiguration") is not None:
        import capo_codedeploy.types.alarm_configuration

        out["override_alarm_configuration"] = (
            capo_codedeploy.types.alarm_configuration.deserialize_aws_json_1_1(
                data["overrideAlarmConfiguration"]
            )
        )
    if data.get("ec2DeploymentOptions") is not None:
        import capo_codedeploy.types.ec2_deployment_options

        out["ec2_deployment_options"] = (
            capo_codedeploy.types.ec2_deployment_options.deserialize_aws_json_1_1(
                data["ec2DeploymentOptions"]
            )
        )
    return out

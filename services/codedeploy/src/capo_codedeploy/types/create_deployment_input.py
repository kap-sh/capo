"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.alarm_configuration
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.auto_rollback_configuration
    import capo_codedeploy.types.boolean
    import capo_codedeploy.types.deployment_config_name
    import capo_codedeploy.types.deployment_group_name
    import capo_codedeploy.types.deployment_mode
    import capo_codedeploy.types.description
    import capo_codedeploy.types.ec2_deployment_options
    import capo_codedeploy.types.file_exists_behavior
    import capo_codedeploy.types.revision_location
    import capo_codedeploy.types.target_instances


class CreateDeploymentInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""
    deployment_group_name: NotRequired[
        "capo_codedeploy.types.deployment_group_name.DeploymentGroupName"
    ]
    """<p>The name of the deployment group.</p>"""
    revision: NotRequired["capo_codedeploy.types.revision_location.RevisionLocation"]
    """<p> The type and location of the revision to deploy. </p>"""
    deployment_config_name: NotRequired[
        "capo_codedeploy.types.deployment_config_name.DeploymentConfigName"
    ]
    """<p>The name of a deployment configuration associated with the user or Amazon Web Services account.</p> <p>If not specified, the value configured in the deployment group is used as the default. If the deployment group does not have a deployment configuration associated with it, <code>CodeDeployDefault</code>.<code>OneAtATime</code> is used by default.</p>"""
    description: NotRequired["capo_codedeploy.types.description.Description"]
    """<p>A comment about the deployment.</p>"""
    ignore_application_stop_failures: NotRequired[
        "capo_codedeploy.types.boolean.Boolean"
    ]
    """<p> If true, then if an <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, or <code>AfterBlockTraffic</code> deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if <code>ApplicationStop</code> fails, the deployment continues with <code>DownloadBundle</code>. If <code>BeforeBlockTraffic</code> fails, the deployment continues with <code>BlockTraffic</code>. If <code>AfterBlockTraffic</code> fails, the deployment continues with <code>ApplicationStop</code>. </p> <p> If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted. </p> <p> During a deployment, the CodeDeploy agent runs the scripts specified for <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail. </p> <p> If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use <code>ignoreApplicationStopFailures</code> to specify that the <code>ApplicationStop</code>, <code>BeforeBlockTraffic</code>, and <code>AfterBlockTraffic</code> failures should be ignored. </p>"""
    target_instances: NotRequired[
        "capo_codedeploy.types.target_instances.TargetInstances"
    ]
    """<p> Information about the instances that belong to the replacement environment in a blue/green deployment. </p>"""
    auto_rollback_configuration: NotRequired[
        "capo_codedeploy.types.auto_rollback_configuration.AutoRollbackConfiguration"
    ]
    """<p>Configuration information for an automatic rollback that is added when a deployment is created.</p>"""
    update_outdated_instances_only: NotRequired["capo_codedeploy.types.boolean.Boolean"]
    """<p> Indicates whether to deploy to all instances or only to instances that are not running the latest application revision. </p>"""
    file_exists_behavior: NotRequired[
        "capo_codedeploy.types.file_exists_behavior.FileExistsBehavior"
    ]
    """<p>Information about how CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.</p> <p>The <code>fileExistsBehavior</code> parameter takes any of the following values:</p> <ul> <li> <p>DISALLOW: The deployment fails. This is also the default behavior if no option is specified.</p> </li> <li> <p>OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.</p> </li> <li> <p>RETAIN: The version of the file already on the instance is kept and used as part of the new deployment.</p> </li> </ul>"""
    deployment_mode: NotRequired["capo_codedeploy.types.deployment_mode.DeploymentMode"]
    """<p>The type of deployment to create. Valid values are:</p> <ul> <li> <p> <code>STANDARD</code>: Deploys the specified revision. This is the default behavior if <code>deploymentMode</code> is not specified.</p> </li> <li> <p> <code>RESTART</code>: Restarts the application on the target instances using the revision from the deployment group's last successful deployment, without downloading a new revision. <code>RESTART</code> is supported only for EC2/On-premises in-place deployments.</p> <p>When <code>deploymentMode</code> is <code>RESTART</code>, the following apply:</p> <ul> <li> <p>The call is rejected for Amazon ECS and Lambda deployments.</p> </li> <li> <p>The <code>revision</code> parameter (including its <code>s3Location</code> and <code>gitHubLocation</code>) must not be specified, and is rejected if provided. The revision is resolved by the service from the deployment group's last successful deployment.</p> </li> <li> <p>The <code>updateOutdatedInstancesOnly</code> parameter must not be set to <code>true</code>, and is rejected if provided.</p> </li> </ul> </li> </ul>"""
    override_alarm_configuration: NotRequired[
        "capo_codedeploy.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>Allows you to specify information about alarms associated with a deployment. The alarm configuration that you specify here will override the alarm configuration at the deployment group level. Consider overriding the alarm configuration if you have set up alarms at the deployment group level that are causing deployment failures. In this case, you would call <code>CreateDeployment</code> to create a new deployment that uses a previous application revision that is known to work, and set its alarm configuration to turn off alarm polling. Turning off alarm polling ensures that the new deployment proceeds without being blocked by the alarm that was generated by the previous, failed, deployment.</p> <note> <p>If you specify an <code>overrideAlarmConfiguration</code>, you need the <code>UpdateDeploymentGroup</code> IAM permission when calling <code>CreateDeployment</code>.</p> </note>"""
    ec2_deployment_options: NotRequired[
        "capo_codedeploy.types.ec2_deployment_options.EC2DeploymentOptions"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeploymentInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    if "deployment_group_name" in value:
        out["deploymentGroupName"] = value["deployment_group_name"]
    if "revision" in value:
        import capo_codedeploy.types.revision_location

        out["revision"] = (
            capo_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["revision"]
            )
        )
    if "deployment_config_name" in value:
        out["deploymentConfigName"] = value["deployment_config_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "ignore_application_stop_failures" in value:
        out["ignoreApplicationStopFailures"] = value["ignore_application_stop_failures"]
    if "target_instances" in value:
        import capo_codedeploy.types.target_instances

        out["targetInstances"] = (
            capo_codedeploy.types.target_instances.serialize_aws_json_1_1(
                value["target_instances"]
            )
        )
    if "auto_rollback_configuration" in value:
        import capo_codedeploy.types.auto_rollback_configuration

        out["autoRollbackConfiguration"] = (
            capo_codedeploy.types.auto_rollback_configuration.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    if "update_outdated_instances_only" in value:
        out["updateOutdatedInstancesOnly"] = value["update_outdated_instances_only"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateDeploymentInput:
    out: CreateDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("deploymentGroupName") is not None:
        out["deployment_group_name"] = data["deploymentGroupName"]
    if data.get("revision") is not None:
        import capo_codedeploy.types.revision_location

        out["revision"] = (
            capo_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revision"]
            )
        )
    if data.get("deploymentConfigName") is not None:
        out["deployment_config_name"] = data["deploymentConfigName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ignoreApplicationStopFailures") is not None:
        out["ignore_application_stop_failures"] = data["ignoreApplicationStopFailures"]
    if data.get("targetInstances") is not None:
        import capo_codedeploy.types.target_instances

        out["target_instances"] = (
            capo_codedeploy.types.target_instances.deserialize_aws_json_1_1(
                data["targetInstances"]
            )
        )
    if data.get("autoRollbackConfiguration") is not None:
        import capo_codedeploy.types.auto_rollback_configuration

        out["auto_rollback_configuration"] = (
            capo_codedeploy.types.auto_rollback_configuration.deserialize_aws_json_1_1(
                data["autoRollbackConfiguration"]
            )
        )
    if data.get("updateOutdatedInstancesOnly") is not None:
        out["update_outdated_instances_only"] = data["updateOutdatedInstancesOnly"]
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

"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateDaemonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.daemon_deployment_configuration
    import capo_ecs.types.daemon_propagate_tags
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class UpdateDaemonRequest(TypedDict, closed=True):
    daemon_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to update.</p>"""
    daemon_task_definition_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon task definition to use for the updated daemon.</p>"""
    capacity_provider_arns: "capo_ecs.types.string_list.StringList"
    """<p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon.</p>"""
    deployment_configuration: NotRequired[
        "capo_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>"""
    propagate_tags: NotRequired[
        "capo_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
    ]
    """<p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation.</p>"""
    enable_ecs_managed_tags: "capo_ecs.types.boolean.Boolean"
    """<p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    enable_execute_command: "capo_ecs.types.boolean.Boolean"
    """<p>If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon. If <code>false</code>, the execute command functionality is turned off.</p>"""
    critical: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If the <code>critical</code> parameter of a daemon is <code>true</code>, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the <code>critical</code> parameter is <code>false</code>, the daemon task failure doesn't affect the other tasks on the instance. The default value is <code>true</code>.</p> <p>A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.</p> <p>Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.</p> <p>Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDaemonRequest) -> dict:
    out: dict = {}
    out["daemonArn"] = value["daemon_arn"]
    out["daemonTaskDefinitionArn"] = value["daemon_task_definition_arn"]
    import capo_ecs.types.string_list

    out["capacityProviderArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["capacity_provider_arns"]
    )
    if "deployment_configuration" in value:
        import capo_ecs.types.daemon_deployment_configuration

        out["deploymentConfiguration"] = (
            capo_ecs.types.daemon_deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "propagate_tags" in value:
        import capo_ecs.types.daemon_propagate_tags

        out["propagateTags"] = (
            capo_ecs.types.daemon_propagate_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    out["enableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
    if "critical" in value:
        out["critical"] = value["critical"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDaemonRequest:
    out: UpdateDaemonRequest = {}  # type: ignore[typeddict-item]
    if data.get("daemonArn") is not None:
        out["daemon_arn"] = data["daemonArn"]
    else:
        raise DeserializationError("UpdateDaemonRequest.daemon_arn required")
    if data.get("daemonTaskDefinitionArn") is not None:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    else:
        raise DeserializationError(
            "UpdateDaemonRequest.daemon_task_definition_arn required"
        )
    if data.get("capacityProviderArns") is not None:
        import capo_ecs.types.string_list

        out["capacity_provider_arns"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["capacityProviderArns"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDaemonRequest.capacity_provider_arns required"
        )
    if data.get("deploymentConfiguration") is not None:
        import capo_ecs.types.daemon_deployment_configuration

        out["deployment_configuration"] = (
            capo_ecs.types.daemon_deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
            )
        )
    if data.get("propagateTags") is not None:
        import capo_ecs.types.daemon_propagate_tags

        out["propagate_tags"] = (
            capo_ecs.types.daemon_propagate_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    if data.get("enableECSManagedTags") is not None:
        out["enable_ecs_managed_tags"] = data["enableECSManagedTags"]
    else:
        out["enable_ecs_managed_tags"] = False
    if data.get("enableExecuteCommand") is not None:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    else:
        out["enable_execute_command"] = False
    if data.get("critical") is not None:
        out["critical"] = data["critical"]
    return out

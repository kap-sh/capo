"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.deployment_lifecycle_hook_stage_list
    import capo_ecs.types.deployment_lifecycle_hook_target_type
    import capo_ecs.types.deployment_lifecycle_hook_timeout_configuration
    import capo_ecs.types.hook_details
    import capo_ecs.types.iam_role_arn
    import capo_ecs.types.string


class DeploymentLifecycleHook(TypedDict, closed=True):
    target_type: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_target_type.DeploymentLifecycleHookTargetType"
    ]
    """<p>The type of action the lifecycle hook performs. Valid values are:</p> <ul> <li> <p> <code>AWS_LAMBDA</code> - Invokes a Lambda function at the specified lifecycle stage. This is the default value.</p> </li> <li> <p> <code>PAUSE</code> - Pauses the deployment at the specified lifecycle stage until you call <code>ContinueServiceDeployment</code> to continue or roll back.</p> </li> </ul> <p>This field is optional. If not specified, the default value is <code>AWS_LAMBDA</code>.</p>"""
    hook_target_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the hook target. For <code>AWS_LAMBDA</code> hooks, this is the Lambda function ARN. This field is not applicable for <code>PAUSE</code> hooks.</p> <p>You must provide this parameter when configuring an <code>AWS_LAMBDA</code> lifecycle hook.</p>"""
    role_arn: NotRequired["capo_ecs.types.iam_role_arn.IAMRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon ECS permission to call Lambda functions on your behalf.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-permissions.html">Permissions required for Lambda functions in Amazon ECS blue/green deployments</a> in the <i> Amazon Elastic Container Service Developer Guide</i>.</p>"""
    lifecycle_stages: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_stage_list.DeploymentLifecycleHookStageList"
    ]
    """<p>The lifecycle stages at which to run the hook. Choose from these valid values:</p> <ul> <li> <p>RECONCILE_SERVICE</p> <p>The reconciliation stage that only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state.</p> <p>You can use a lifecycle hook for this stage.</p> </li> <li> <p>PRE_SCALE_UP</p> <p>The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic.</p> <p>You can use a lifecycle hook for this stage.</p> </li> <li> <p>POST_SCALE_UP</p> <p>The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic.</p> <p>You can use a lifecycle hook for this stage.</p> </li> <li> <p>TEST_TRAFFIC_SHIFT</p> <p>The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic.</p> <p>You can use a lifecycle hook for this stage.</p> </li> <li> <p>POST_TEST_TRAFFIC_SHIFT</p> <p>The test traffic shift is complete. The green service revision handles 100% of the test traffic.</p> <p>You can use a lifecycle hook for this stage.</p> </li> <li> <p>PRE_PRODUCTION_TRAFFIC_SHIFT</p> <p>Occurs before production traffic shift. For linear and canary deployments, this stage is invoked before every traffic shift step.</p> <p>You can use a lifecycle hook for this stage.</p> </li> <li> <p>PRODUCTION_TRAFFIC_SHIFT</p> <p>Production traffic is shifting to the green service revision. The green service revision is migrating from 0% to 100% of production traffic. For linear and canary deployments, this stage is invoked at every traffic shift step.</p> <p>You can use a lifecycle hook for this stage.</p> </li> <li> <p>POST_PRODUCTION_TRAFFIC_SHIFT</p> <p>The production traffic shift is complete.</p> <p>You can use a lifecycle hook for this stage.</p> </li> </ul> <note> <p> <code>PAUSE</code> hooks cannot be configured at <code>TEST_TRAFFIC_SHIFT</code> or <code>PRODUCTION_TRAFFIC_SHIFT</code> stages. These stages are only valid for <code>AWS_LAMBDA</code> hooks.</p> </note> <p>You must provide this parameter when configuring a deployment lifecycle hook.</p>"""
    hook_details: NotRequired["capo_ecs.types.hook_details.HookDetails"]
    """<p>Use this field to specify custom parameters that Amazon ECS passes to your Lambda function on each invocation. This field is not used for <code>PAUSE</code> hooks.</p>"""
    timeout_configuration: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_timeout_configuration.DeploymentLifecycleHookTimeoutConfiguration"
    ]
    """<p>The timeout configuration for the lifecycle hook. This specifies how long Amazon ECS waits before taking the timeout action if the hook is not resolved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHook) -> dict:
    out: dict = {}
    if "target_type" in value:
        import capo_ecs.types.deployment_lifecycle_hook_target_type

        out["targetType"] = (
            capo_ecs.types.deployment_lifecycle_hook_target_type.serialize_aws_json_1_1(
                value["target_type"]
            )
        )
    if "hook_target_arn" in value:
        out["hookTargetArn"] = value["hook_target_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "lifecycle_stages" in value:
        import capo_ecs.types.deployment_lifecycle_hook_stage_list

        out["lifecycleStages"] = (
            capo_ecs.types.deployment_lifecycle_hook_stage_list.serialize_aws_json_1_1(
                value["lifecycle_stages"]
            )
        )
    if "hook_details" in value:
        out["hookDetails"] = value["hook_details"]
    if "timeout_configuration" in value:
        import capo_ecs.types.deployment_lifecycle_hook_timeout_configuration

        out["timeoutConfiguration"] = (
            capo_ecs.types.deployment_lifecycle_hook_timeout_configuration.serialize_aws_json_1_1(
                value["timeout_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentLifecycleHook:
    out: DeploymentLifecycleHook = {}  # type: ignore[typeddict-item]
    if data.get("targetType") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_target_type

        out["target_type"] = (
            capo_ecs.types.deployment_lifecycle_hook_target_type.deserialize_aws_json_1_1(
                data["targetType"]
            )
        )
    if data.get("hookTargetArn") is not None:
        out["hook_target_arn"] = data["hookTargetArn"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("lifecycleStages") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_stage_list

        out["lifecycle_stages"] = (
            capo_ecs.types.deployment_lifecycle_hook_stage_list.deserialize_aws_json_1_1(
                data["lifecycleStages"]
            )
        )
    if data.get("hookDetails") is not None:
        out["hook_details"] = data["hookDetails"]
    if data.get("timeoutConfiguration") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_timeout_configuration

        out["timeout_configuration"] = (
            capo_ecs.types.deployment_lifecycle_hook_timeout_configuration.deserialize_aws_json_1_1(
                data["timeoutConfiguration"]
            )
        )
    return out

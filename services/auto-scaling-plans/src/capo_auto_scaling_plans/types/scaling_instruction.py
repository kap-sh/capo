"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.customized_load_metric_specification
    import capo_auto_scaling_plans.types.disable_dynamic_scaling
    import capo_auto_scaling_plans.types.predefined_load_metric_specification
    import capo_auto_scaling_plans.types.predictive_scaling_max_capacity_behavior
    import capo_auto_scaling_plans.types.predictive_scaling_mode
    import capo_auto_scaling_plans.types.resource_capacity
    import capo_auto_scaling_plans.types.resource_id_max_len1600
    import capo_auto_scaling_plans.types.scalable_dimension
    import capo_auto_scaling_plans.types.scaling_policy_update_behavior
    import capo_auto_scaling_plans.types.scheduled_action_buffer_time
    import capo_auto_scaling_plans.types.service_namespace
    import capo_auto_scaling_plans.types.target_tracking_configurations


class ScalingInstruction(TypedDict, closed=True):
    service_namespace: (
        "capo_auto_scaling_plans.types.service_namespace.ServiceNamespace"
    )
    """<p>The namespace of the AWS service.</p>"""
    resource_id: (
        "capo_auto_scaling_plans.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    )
    """<p>The ID of the resource. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>Auto Scaling group - The resource type is <code>autoScalingGroup</code> and the unique identifier is the name of the Auto Scaling group. Example: <code>autoScalingGroup/my-asg</code>.</p> </li> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/default/sample-webapp</code>.</p> </li> <li> <p>Spot Fleet request - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the resource ID. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the resource ID. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> </ul>"""
    scalable_dimension: (
        "capo_auto_scaling_plans.types.scalable_dimension.ScalableDimension"
    )
    """<p>The scalable dimension associated with the resource.</p> <ul> <li> <p> <code>autoscaling:autoScalingGroup:DesiredCapacity</code> - The desired capacity of an Auto Scaling group.</p> </li> <li> <p> <code>ecs:service:DesiredCount</code> - The desired task count of an ECS service.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet request.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> </ul>"""
    min_capacity: "capo_auto_scaling_plans.types.resource_capacity.ResourceCapacity"
    """<p>The minimum capacity of the resource. </p>"""
    max_capacity: "capo_auto_scaling_plans.types.resource_capacity.ResourceCapacity"
    """<p>The maximum capacity of the resource. The exception to this upper limit is if you specify a non-default setting for <b>PredictiveScalingMaxCapacityBehavior</b>. </p>"""
    target_tracking_configurations: "capo_auto_scaling_plans.types.target_tracking_configurations.TargetTrackingConfigurations"
    """<p>The target tracking configurations (up to 10). Each of these structures must specify a unique scaling metric and a target value for the metric. </p>"""
    predefined_load_metric_specification: NotRequired[
        "capo_auto_scaling_plans.types.predefined_load_metric_specification.PredefinedLoadMetricSpecification"
    ]
    """<p>The predefined load metric to use for predictive scaling. This parameter or a <b>CustomizedLoadMetricSpecification</b> is required when configuring predictive scaling, and cannot be used otherwise. </p>"""
    customized_load_metric_specification: NotRequired[
        "capo_auto_scaling_plans.types.customized_load_metric_specification.CustomizedLoadMetricSpecification"
    ]
    """<p>The customized load metric to use for predictive scaling. This parameter or a <b>PredefinedLoadMetricSpecification</b> is required when configuring predictive scaling, and cannot be used otherwise. </p>"""
    scheduled_action_buffer_time: NotRequired[
        "capo_auto_scaling_plans.types.scheduled_action_buffer_time.ScheduledActionBufferTime"
    ]
    """<p>The amount of time, in seconds, to buffer the run time of scheduled scaling actions when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and the buffer time is 5 minutes, then the run time of the corresponding scheduled scaling action will be 9:55 AM. The intention is to give resources time to be provisioned. For example, it can take a few minutes to launch an EC2 instance. The actual amount of time required depends on several factors, such as the size of the instance and whether there are startup scripts to complete. </p> <p>The value must be less than the forecast interval duration of 3600 seconds (60 minutes). The default is 300 seconds. </p> <p>Only valid when configuring predictive scaling. </p>"""
    predictive_scaling_max_capacity_behavior: NotRequired[
        "capo_auto_scaling_plans.types.predictive_scaling_max_capacity_behavior.PredictiveScalingMaxCapacityBehavior"
    ]
    """<p>Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity specified for the resource. The default value is <code>SetForecastCapacityToMaxCapacity</code>.</p> <p>The following are possible values:</p> <ul> <li> <p> <code>SetForecastCapacityToMaxCapacity</code> - AWS Auto Scaling cannot scale resource capacity higher than the maximum capacity. The maximum capacity is enforced as a hard limit. </p> </li> <li> <p> <code>SetMaxCapacityToForecastCapacity</code> - AWS Auto Scaling may scale resource capacity higher than the maximum capacity to equal but not exceed forecast capacity.</p> </li> <li> <p> <code>SetMaxCapacityAboveForecastCapacity</code> - AWS Auto Scaling may scale resource capacity higher than the maximum capacity by a specified buffer value. The intention is to give the target tracking scaling policy extra capacity if unexpected traffic occurs. </p> </li> </ul> <p>Only valid when configuring predictive scaling.</p>"""
    predictive_scaling_max_capacity_buffer: NotRequired[
        "capo_auto_scaling_plans.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.</p> <p>Only valid when configuring predictive scaling. Required if the <b>PredictiveScalingMaxCapacityBehavior</b> is set to <code>SetMaxCapacityAboveForecastCapacity</code>, and cannot be used otherwise.</p> <p>The range is 1-100.</p>"""
    predictive_scaling_mode: NotRequired[
        "capo_auto_scaling_plans.types.predictive_scaling_mode.PredictiveScalingMode"
    ]
    """<p>The predictive scaling mode. The default value is <code>ForecastAndScale</code>. Otherwise, AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions based on the capacity forecast. </p>"""
    scaling_policy_update_behavior: NotRequired[
        "capo_auto_scaling_plans.types.scaling_policy_update_behavior.ScalingPolicyUpdateBehavior"
    ]
    """<p>Controls whether a resource's externally created scaling policies are kept or replaced. </p> <p>The default value is <code>KeepExternalPolicies</code>. If the parameter is set to <code>ReplaceExternalPolicies</code>, any scaling policies that are external to AWS Auto Scaling are deleted and new target tracking scaling policies created. </p> <p>Only valid when configuring dynamic scaling. </p> <p>Condition: The number of existing policies to be replaced must be less than or equal to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all existing policies and does not create new ones.</p>"""
    disable_dynamic_scaling: NotRequired[
        "capo_auto_scaling_plans.types.disable_dynamic_scaling.DisableDynamicScaling"
    ]
    """<p>Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based on the specified target tracking configurations. </p> <p>The default is enabled (<code>false</code>). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingInstruction) -> dict:
    out: dict = {}
    import capo_auto_scaling_plans.types.service_namespace

    out["ServiceNamespace"] = (
        capo_auto_scaling_plans.types.service_namespace.serialize_aws_json_1_1(
            value["service_namespace"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import capo_auto_scaling_plans.types.scalable_dimension

    out["ScalableDimension"] = (
        capo_auto_scaling_plans.types.scalable_dimension.serialize_aws_json_1_1(
            value["scalable_dimension"]
        )
    )
    out["MinCapacity"] = value["min_capacity"]
    out["MaxCapacity"] = value["max_capacity"]
    import capo_auto_scaling_plans.types.target_tracking_configurations

    out["TargetTrackingConfigurations"] = (
        capo_auto_scaling_plans.types.target_tracking_configurations.serialize_aws_json_1_1(
            value["target_tracking_configurations"]
        )
    )
    if "predefined_load_metric_specification" in value:
        import capo_auto_scaling_plans.types.predefined_load_metric_specification

        out["PredefinedLoadMetricSpecification"] = (
            capo_auto_scaling_plans.types.predefined_load_metric_specification.serialize_aws_json_1_1(
                value["predefined_load_metric_specification"]
            )
        )
    if "customized_load_metric_specification" in value:
        import capo_auto_scaling_plans.types.customized_load_metric_specification

        out["CustomizedLoadMetricSpecification"] = (
            capo_auto_scaling_plans.types.customized_load_metric_specification.serialize_aws_json_1_1(
                value["customized_load_metric_specification"]
            )
        )
    if "scheduled_action_buffer_time" in value:
        out["ScheduledActionBufferTime"] = value["scheduled_action_buffer_time"]
    if "predictive_scaling_max_capacity_behavior" in value:
        import capo_auto_scaling_plans.types.predictive_scaling_max_capacity_behavior

        out["PredictiveScalingMaxCapacityBehavior"] = (
            capo_auto_scaling_plans.types.predictive_scaling_max_capacity_behavior.serialize_aws_json_1_1(
                value["predictive_scaling_max_capacity_behavior"]
            )
        )
    if "predictive_scaling_max_capacity_buffer" in value:
        out["PredictiveScalingMaxCapacityBuffer"] = value[
            "predictive_scaling_max_capacity_buffer"
        ]
    if "predictive_scaling_mode" in value:
        import capo_auto_scaling_plans.types.predictive_scaling_mode

        out["PredictiveScalingMode"] = (
            capo_auto_scaling_plans.types.predictive_scaling_mode.serialize_aws_json_1_1(
                value["predictive_scaling_mode"]
            )
        )
    if "scaling_policy_update_behavior" in value:
        import capo_auto_scaling_plans.types.scaling_policy_update_behavior

        out["ScalingPolicyUpdateBehavior"] = (
            capo_auto_scaling_plans.types.scaling_policy_update_behavior.serialize_aws_json_1_1(
                value["scaling_policy_update_behavior"]
            )
        )
    if "disable_dynamic_scaling" in value:
        out["DisableDynamicScaling"] = value["disable_dynamic_scaling"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingInstruction:
    out: ScalingInstruction = {}  # type: ignore[typeddict-item]
    if data.get("ServiceNamespace") is not None:
        import capo_auto_scaling_plans.types.service_namespace

        out["service_namespace"] = (
            capo_auto_scaling_plans.types.service_namespace.deserialize_aws_json_1_1(
                data["ServiceNamespace"]
            )
        )
    else:
        import typing

        out["service_namespace"] = typing.cast(
            "capo_auto_scaling_plans.types.service_namespace.ServiceNamespace", ""
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ScalableDimension") is not None:
        import capo_auto_scaling_plans.types.scalable_dimension

        out["scalable_dimension"] = (
            capo_auto_scaling_plans.types.scalable_dimension.deserialize_aws_json_1_1(
                data["ScalableDimension"]
            )
        )
    else:
        import typing

        out["scalable_dimension"] = typing.cast(
            "capo_auto_scaling_plans.types.scalable_dimension.ScalableDimension", ""
        )
    if data.get("MinCapacity") is not None:
        out["min_capacity"] = data["MinCapacity"]
    else:
        out["min_capacity"] = 0
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = data["MaxCapacity"]
    else:
        out["max_capacity"] = 0
    if data.get("TargetTrackingConfigurations") is not None:
        import capo_auto_scaling_plans.types.target_tracking_configurations

        out["target_tracking_configurations"] = (
            capo_auto_scaling_plans.types.target_tracking_configurations.deserialize_aws_json_1_1(
                data["TargetTrackingConfigurations"]
            )
        )
    else:
        out["target_tracking_configurations"] = []
    if data.get("PredefinedLoadMetricSpecification") is not None:
        import capo_auto_scaling_plans.types.predefined_load_metric_specification

        out["predefined_load_metric_specification"] = (
            capo_auto_scaling_plans.types.predefined_load_metric_specification.deserialize_aws_json_1_1(
                data["PredefinedLoadMetricSpecification"]
            )
        )
    if data.get("CustomizedLoadMetricSpecification") is not None:
        import capo_auto_scaling_plans.types.customized_load_metric_specification

        out["customized_load_metric_specification"] = (
            capo_auto_scaling_plans.types.customized_load_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedLoadMetricSpecification"]
            )
        )
    if data.get("ScheduledActionBufferTime") is not None:
        out["scheduled_action_buffer_time"] = data["ScheduledActionBufferTime"]
    if data.get("PredictiveScalingMaxCapacityBehavior") is not None:
        import capo_auto_scaling_plans.types.predictive_scaling_max_capacity_behavior

        out["predictive_scaling_max_capacity_behavior"] = (
            capo_auto_scaling_plans.types.predictive_scaling_max_capacity_behavior.deserialize_aws_json_1_1(
                data["PredictiveScalingMaxCapacityBehavior"]
            )
        )
    if data.get("PredictiveScalingMaxCapacityBuffer") is not None:
        out["predictive_scaling_max_capacity_buffer"] = data[
            "PredictiveScalingMaxCapacityBuffer"
        ]
    if data.get("PredictiveScalingMode") is not None:
        import capo_auto_scaling_plans.types.predictive_scaling_mode

        out["predictive_scaling_mode"] = (
            capo_auto_scaling_plans.types.predictive_scaling_mode.deserialize_aws_json_1_1(
                data["PredictiveScalingMode"]
            )
        )
    if data.get("ScalingPolicyUpdateBehavior") is not None:
        import capo_auto_scaling_plans.types.scaling_policy_update_behavior

        out["scaling_policy_update_behavior"] = (
            capo_auto_scaling_plans.types.scaling_policy_update_behavior.deserialize_aws_json_1_1(
                data["ScalingPolicyUpdateBehavior"]
            )
        )
    if data.get("DisableDynamicScaling") is not None:
        out["disable_dynamic_scaling"] = data["DisableDynamicScaling"]
    return out

"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlanResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.resource_id_max_len1600
    import capo_auto_scaling_plans.types.scalable_dimension
    import capo_auto_scaling_plans.types.scaling_plan_name
    import capo_auto_scaling_plans.types.scaling_plan_version
    import capo_auto_scaling_plans.types.scaling_policies
    import capo_auto_scaling_plans.types.scaling_status_code
    import capo_auto_scaling_plans.types.service_namespace
    import capo_auto_scaling_plans.types.xml_string


class ScalingPlanResource(TypedDict, closed=True):
    scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan.</p>"""
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
    """<p>The scalable dimension for the resource.</p> <ul> <li> <p> <code>autoscaling:autoScalingGroup:DesiredCapacity</code> - The desired capacity of an Auto Scaling group.</p> </li> <li> <p> <code>ecs:service:DesiredCount</code> - The desired task count of an ECS service.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet request.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> </ul>"""
    scaling_policies: NotRequired[
        "capo_auto_scaling_plans.types.scaling_policies.ScalingPolicies"
    ]
    """<p>The scaling policies.</p>"""
    scaling_status_code: (
        "capo_auto_scaling_plans.types.scaling_status_code.ScalingStatusCode"
    )
    """<p>The scaling status of the resource.</p> <ul> <li> <p> <code>Active</code> - The scaling configuration is active.</p> </li> <li> <p> <code>Inactive</code> - The scaling configuration is not active because the scaling plan is being created or the scaling configuration could not be applied. Check the status message for more information.</p> </li> <li> <p> <code>PartiallyActive</code> - The scaling configuration is partially active because the scaling plan is being created or deleted or the scaling configuration could not be fully applied. Check the status message for more information.</p> </li> </ul>"""
    scaling_status_message: NotRequired[
        "capo_auto_scaling_plans.types.xml_string.XmlString"
    ]
    """<p>A simple message about the current scaling status of the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPlanResource) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
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
    if "scaling_policies" in value:
        import capo_auto_scaling_plans.types.scaling_policies

        out["ScalingPolicies"] = (
            capo_auto_scaling_plans.types.scaling_policies.serialize_aws_json_1_1(
                value["scaling_policies"]
            )
        )
    import capo_auto_scaling_plans.types.scaling_status_code

    out["ScalingStatusCode"] = (
        capo_auto_scaling_plans.types.scaling_status_code.serialize_aws_json_1_1(
            value["scaling_status_code"]
        )
    )
    if "scaling_status_message" in value:
        out["ScalingStatusMessage"] = value["scaling_status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPlanResource:
    out: ScalingPlanResource = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPlanName") is not None:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        out["scaling_plan_name"] = ""
    if data.get("ScalingPlanVersion") is not None:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        out["scaling_plan_version"] = 0
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
    if data.get("ScalingPolicies") is not None:
        import capo_auto_scaling_plans.types.scaling_policies

        out["scaling_policies"] = (
            capo_auto_scaling_plans.types.scaling_policies.deserialize_aws_json_1_1(
                data["ScalingPolicies"]
            )
        )
    if data.get("ScalingStatusCode") is not None:
        import capo_auto_scaling_plans.types.scaling_status_code

        out["scaling_status_code"] = (
            capo_auto_scaling_plans.types.scaling_status_code.deserialize_aws_json_1_1(
                data["ScalingStatusCode"]
            )
        )
    else:
        import typing

        out["scaling_status_code"] = typing.cast(
            "capo_auto_scaling_plans.types.scaling_status_code.ScalingStatusCode", ""
        )
    if data.get("ScalingStatusMessage") is not None:
        out["scaling_status_message"] = data["ScalingStatusMessage"]
    return out

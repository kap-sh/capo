"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.access_key
    import capo_guardduty.types.autoscaling_auto_scaling_group
    import capo_guardduty.types.bedrock_guardrail_resource
    import capo_guardduty.types.cloudformation_stack
    import capo_guardduty.types.container_finding_resource
    import capo_guardduty.types.ec2_image
    import capo_guardduty.types.ec2_instance
    import capo_guardduty.types.ec2_launch_template
    import capo_guardduty.types.ec2_network_interface
    import capo_guardduty.types.ec2_vpc
    import capo_guardduty.types.ecs_cluster
    import capo_guardduty.types.ecs_task
    import capo_guardduty.types.eks_cluster
    import capo_guardduty.types.iam_instance_profile_v2
    import capo_guardduty.types.kubernetes_workload
    import capo_guardduty.types.s3_bucket
    import capo_guardduty.types.s3_object


class ResourceData(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_guardduty.types.s3_bucket.S3Bucket"]
    """<p>Contains information about the Amazon S3 bucket.</p>"""
    ec2_instance: NotRequired["capo_guardduty.types.ec2_instance.Ec2Instance"]
    """<p>Contains information about the Amazon EC2 instance.</p>"""
    access_key: NotRequired["capo_guardduty.types.access_key.AccessKey"]
    """<p>Contains information about the IAM access key details of a user that involved in the GuardDuty finding.</p>"""
    ec2_network_interface: NotRequired[
        "capo_guardduty.types.ec2_network_interface.Ec2NetworkInterface"
    ]
    """<p>Contains information about the elastic network interface of the Amazon EC2 instance.</p>"""
    s3_object: NotRequired["capo_guardduty.types.s3_object.S3Object"]
    """<p>Contains information about the Amazon S3 object.</p>"""
    eks_cluster: NotRequired["capo_guardduty.types.eks_cluster.EksCluster"]
    """<p>Contains detailed information about the Amazon EKS cluster associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    kubernetes_workload: NotRequired[
        "capo_guardduty.types.kubernetes_workload.KubernetesWorkload"
    ]
    """<p>Contains detailed information about the Kubernetes workload associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    container: NotRequired[
        "capo_guardduty.types.container_finding_resource.ContainerFindingResource"
    ]
    """<p>Contains detailed information about the container associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ecs_cluster: NotRequired["capo_guardduty.types.ecs_cluster.EcsCluster"]
    """<p>Contains detailed information about the Amazon ECS cluster associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ecs_task: NotRequired["capo_guardduty.types.ecs_task.EcsTask"]
    """<p>Contains detailed information about the Amazon ECS task associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    iam_instance_profile: NotRequired[
        "capo_guardduty.types.iam_instance_profile_v2.IamInstanceProfileV2"
    ]
    """<p>Contains detailed information about the IAM instance profile associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    autoscaling_auto_scaling_group: NotRequired[
        "capo_guardduty.types.autoscaling_auto_scaling_group.AutoscalingAutoScalingGroup"
    ]
    """<p>Contains detailed information about the Auto Scaling Group associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ec2_launch_template: NotRequired[
        "capo_guardduty.types.ec2_launch_template.Ec2LaunchTemplate"
    ]
    """<p>Contains detailed information about the EC2 launch template associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ec2_vpc: NotRequired["capo_guardduty.types.ec2_vpc.Ec2Vpc"]
    """<p>Contains detailed information about the EC2 VPC associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ec2_image: NotRequired["capo_guardduty.types.ec2_image.Ec2Image"]
    """<p>Contains detailed information about the EC2 Image associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    cloudformation_stack: NotRequired[
        "capo_guardduty.types.cloudformation_stack.CloudformationStack"
    ]
    """<p>Contains detailed information about the CloudFormation stack associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    bedrock_guardrail: NotRequired[
        "capo_guardduty.types.bedrock_guardrail_resource.BedrockGuardrailResource"
    ]
    """<p>Contains detailed information about the Amazon Bedrock guardrail associated with the activity that prompted GuardDuty to generate a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceData) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        import capo_guardduty.types.s3_bucket

        out["s3Bucket"] = capo_guardduty.types.s3_bucket.serialize_json(
            value["s3_bucket"]
        )
    if "ec2_instance" in value:
        import capo_guardduty.types.ec2_instance

        out["ec2Instance"] = capo_guardduty.types.ec2_instance.serialize_json(
            value["ec2_instance"]
        )
    if "access_key" in value:
        import capo_guardduty.types.access_key

        out["accessKey"] = capo_guardduty.types.access_key.serialize_json(
            value["access_key"]
        )
    if "ec2_network_interface" in value:
        import capo_guardduty.types.ec2_network_interface

        out["ec2NetworkInterface"] = (
            capo_guardduty.types.ec2_network_interface.serialize_json(
                value["ec2_network_interface"]
            )
        )
    if "s3_object" in value:
        import capo_guardduty.types.s3_object

        out["s3Object"] = capo_guardduty.types.s3_object.serialize_json(
            value["s3_object"]
        )
    if "eks_cluster" in value:
        import capo_guardduty.types.eks_cluster

        out["eksCluster"] = capo_guardduty.types.eks_cluster.serialize_json(
            value["eks_cluster"]
        )
    if "kubernetes_workload" in value:
        import capo_guardduty.types.kubernetes_workload

        out["kubernetesWorkload"] = (
            capo_guardduty.types.kubernetes_workload.serialize_json(
                value["kubernetes_workload"]
            )
        )
    if "container" in value:
        import capo_guardduty.types.container_finding_resource

        out["container"] = (
            capo_guardduty.types.container_finding_resource.serialize_json(
                value["container"]
            )
        )
    if "ecs_cluster" in value:
        import capo_guardduty.types.ecs_cluster

        out["ecsCluster"] = capo_guardduty.types.ecs_cluster.serialize_json(
            value["ecs_cluster"]
        )
    if "ecs_task" in value:
        import capo_guardduty.types.ecs_task

        out["ecsTask"] = capo_guardduty.types.ecs_task.serialize_json(value["ecs_task"])
    if "iam_instance_profile" in value:
        import capo_guardduty.types.iam_instance_profile_v2

        out["iamInstanceProfile"] = (
            capo_guardduty.types.iam_instance_profile_v2.serialize_json(
                value["iam_instance_profile"]
            )
        )
    if "autoscaling_auto_scaling_group" in value:
        import capo_guardduty.types.autoscaling_auto_scaling_group

        out["autoscalingAutoScalingGroup"] = (
            capo_guardduty.types.autoscaling_auto_scaling_group.serialize_json(
                value["autoscaling_auto_scaling_group"]
            )
        )
    if "ec2_launch_template" in value:
        import capo_guardduty.types.ec2_launch_template

        out["ec2LaunchTemplate"] = (
            capo_guardduty.types.ec2_launch_template.serialize_json(
                value["ec2_launch_template"]
            )
        )
    if "ec2_vpc" in value:
        import capo_guardduty.types.ec2_vpc

        out["ec2Vpc"] = capo_guardduty.types.ec2_vpc.serialize_json(value["ec2_vpc"])
    if "ec2_image" in value:
        import capo_guardduty.types.ec2_image

        out["ec2Image"] = capo_guardduty.types.ec2_image.serialize_json(
            value["ec2_image"]
        )
    if "cloudformation_stack" in value:
        import capo_guardduty.types.cloudformation_stack

        out["cloudformationStack"] = (
            capo_guardduty.types.cloudformation_stack.serialize_json(
                value["cloudformation_stack"]
            )
        )
    if "bedrock_guardrail" in value:
        import capo_guardduty.types.bedrock_guardrail_resource

        out["bedrockGuardrail"] = (
            capo_guardduty.types.bedrock_guardrail_resource.serialize_json(
                value["bedrock_guardrail"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceData:
    out: ResourceData = {}  # type: ignore[typeddict-item]
    if data.get("s3Bucket") is not None:
        import capo_guardduty.types.s3_bucket

        out["s3_bucket"] = capo_guardduty.types.s3_bucket.deserialize_json(
            data["s3Bucket"]
        )
    if data.get("ec2Instance") is not None:
        import capo_guardduty.types.ec2_instance

        out["ec2_instance"] = capo_guardduty.types.ec2_instance.deserialize_json(
            data["ec2Instance"]
        )
    if data.get("accessKey") is not None:
        import capo_guardduty.types.access_key

        out["access_key"] = capo_guardduty.types.access_key.deserialize_json(
            data["accessKey"]
        )
    if data.get("ec2NetworkInterface") is not None:
        import capo_guardduty.types.ec2_network_interface

        out["ec2_network_interface"] = (
            capo_guardduty.types.ec2_network_interface.deserialize_json(
                data["ec2NetworkInterface"]
            )
        )
    if data.get("s3Object") is not None:
        import capo_guardduty.types.s3_object

        out["s3_object"] = capo_guardduty.types.s3_object.deserialize_json(
            data["s3Object"]
        )
    if data.get("eksCluster") is not None:
        import capo_guardduty.types.eks_cluster

        out["eks_cluster"] = capo_guardduty.types.eks_cluster.deserialize_json(
            data["eksCluster"]
        )
    if data.get("kubernetesWorkload") is not None:
        import capo_guardduty.types.kubernetes_workload

        out["kubernetes_workload"] = (
            capo_guardduty.types.kubernetes_workload.deserialize_json(
                data["kubernetesWorkload"]
            )
        )
    if data.get("container") is not None:
        import capo_guardduty.types.container_finding_resource

        out["container"] = (
            capo_guardduty.types.container_finding_resource.deserialize_json(
                data["container"]
            )
        )
    if data.get("ecsCluster") is not None:
        import capo_guardduty.types.ecs_cluster

        out["ecs_cluster"] = capo_guardduty.types.ecs_cluster.deserialize_json(
            data["ecsCluster"]
        )
    if data.get("ecsTask") is not None:
        import capo_guardduty.types.ecs_task

        out["ecs_task"] = capo_guardduty.types.ecs_task.deserialize_json(
            data["ecsTask"]
        )
    if data.get("iamInstanceProfile") is not None:
        import capo_guardduty.types.iam_instance_profile_v2

        out["iam_instance_profile"] = (
            capo_guardduty.types.iam_instance_profile_v2.deserialize_json(
                data["iamInstanceProfile"]
            )
        )
    if data.get("autoscalingAutoScalingGroup") is not None:
        import capo_guardduty.types.autoscaling_auto_scaling_group

        out["autoscaling_auto_scaling_group"] = (
            capo_guardduty.types.autoscaling_auto_scaling_group.deserialize_json(
                data["autoscalingAutoScalingGroup"]
            )
        )
    if data.get("ec2LaunchTemplate") is not None:
        import capo_guardduty.types.ec2_launch_template

        out["ec2_launch_template"] = (
            capo_guardduty.types.ec2_launch_template.deserialize_json(
                data["ec2LaunchTemplate"]
            )
        )
    if data.get("ec2Vpc") is not None:
        import capo_guardduty.types.ec2_vpc

        out["ec2_vpc"] = capo_guardduty.types.ec2_vpc.deserialize_json(data["ec2Vpc"])
    if data.get("ec2Image") is not None:
        import capo_guardduty.types.ec2_image

        out["ec2_image"] = capo_guardduty.types.ec2_image.deserialize_json(
            data["ec2Image"]
        )
    if data.get("cloudformationStack") is not None:
        import capo_guardduty.types.cloudformation_stack

        out["cloudformation_stack"] = (
            capo_guardduty.types.cloudformation_stack.deserialize_json(
                data["cloudformationStack"]
            )
        )
    if data.get("bedrockGuardrail") is not None:
        import capo_guardduty.types.bedrock_guardrail_resource

        out["bedrock_guardrail"] = (
            capo_guardduty.types.bedrock_guardrail_resource.deserialize_json(
                data["bedrockGuardrail"]
            )
        )
    return out


def redact_sensitive(value: ResourceData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ec2_network_interface" in value:
        import capo_guardduty.types.ec2_network_interface

        out["ec2_network_interface"] = (
            capo_guardduty.types.ec2_network_interface.redact_sensitive(
                value["ec2_network_interface"]
            )
        )
    return out

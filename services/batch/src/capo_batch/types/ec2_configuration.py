"""Generated from Smithy shape ``com.amazonaws.batch#Ec2Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.image_id_override
    import capo_batch.types.image_type
    import capo_batch.types.kubernetes_version
    import capo_batch.types.string


class Ec2Configuration(TypedDict, closed=True):
    image_type: NotRequired["capo_batch.types.image_type.ImageType"]
    """<p>The image type to match with the instance type to select an AMI. The supported values are different for <code>ECS</code> and <code>EKS</code> resources.</p> <dl> <dt>ECS</dt> <dd> <p>If the <code>imageIdOverride</code> parameter isn't specified, then a recent <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html">Amazon ECS-optimized Amazon Linux 2023 AMI</a> (<code>ECS_AL2023</code>) is used. If a new image type is specified in an update, but neither an <code>imageId</code> nor a <code>imageIdOverride</code> parameter is specified, then the latest Amazon ECS optimized AMI for that image type that's supported by Batch is used.</p> <important> <p>Amazon Web Services is ending support for Amazon ECS Amazon Linux 2-optimized and accelerated AMIs on June 30, 2026. On January 12, 2026, Batch changed the default AMI for new Amazon ECS compute environments from Amazon Linux 2 to Amazon Linux 2023. Effective June 30, 2026, Batch will block creation of new Amazon ECS compute environments using Batch-provided Amazon Linux 2 AMIs. We strongly recommend migrating your existing Batch Amazon ECS compute environments to Amazon Linux 2023 prior to June 30, 2026. For more information on upgrading from AL2 to AL2023, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/ecs-migration-2023.html">How to migrate from ECS AL2 to ECS AL2023</a> in the <i>Batch User Guide</i>.</p> </important> <dl> <dt>ECS_AL2</dt> <dd> <p> <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html">Amazon Linux 2</a>: Used for non-GPU instance families.</p> </dd> <dt>ECS_AL2_NVIDIA</dt> <dd> <p> <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#gpuami">Amazon Linux 2 (GPU)</a>: Used for GPU instance families (for example <code>P4</code> and <code>G4</code>) and non Amazon Web Services Graviton-based instance types.</p> </dd> <dt>ECS_AL2023</dt> <dd> <p> <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html">Amazon Linux 2023</a>: Default for all non-GPU instance families.</p> <note> <p>Amazon Linux 2023 does not support <code>A1</code> instances.</p> </note> </dd> <dt>ECS_AL2023_NVIDIA</dt> <dd> <p> <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#gpuami">Amazon Linux 2023 (GPU)</a>: Default for all GPU instance families and can be used for all non Amazon Web Services Graviton-based instance types.</p> <note> <p>ECS_AL2023_NVIDIA doesn't support <code>p3</code> and <code>g3</code> instance types.</p> </note> </dd> </dl> </dd> <dt>EKS</dt> <dd> <p>If the <code>imageIdOverride</code> parameter isn't specified, then a recent <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html">Amazon EKS-optimized Amazon Linux 2023 AMI</a> (<code>EKS_AL2023</code>) is used. If a new image type is specified in an update, but neither an <code>imageId</code> nor a <code>imageIdOverride</code> parameter is specified, then the latest Amazon EKS optimized AMI for that image type that Batch supports is used.</p> <important> <p>Amazon Linux 2023 AMIs are the default on Batch for Amazon EKS.</p> <p>Amazon Web Services ended support for Amazon EKS AL2-optimized and AL2-accelerated AMIs on November 26, 2025. Batch Amazon EKS compute environments using Amazon Linux 2 will no longer receive software updates, security patches, or bug fixes from Amazon Web Services. We recommend migrating to Amazon Linux 2023. For more information on upgrading from AL2 to AL2023, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/eks-migration-2023.html">How to upgrade from EKS AL2 to EKS AL2023</a> in the <i>Batch User Guide</i>.</p> </important> <dl> <dt>EKS_AL2</dt> <dd> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html">Amazon Linux 2</a>: Used for non-GPU instance families.</p> </dd> <dt>EKS_AL2_NVIDIA</dt> <dd> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html">Amazon Linux 2 (accelerated)</a>: Used for GPU instance families (for example, <code>P4</code> and <code>G4</code>) and can be used for all non Amazon Web Services Graviton-based instance types.</p> </dd> <dt>EKS_AL2023</dt> <dd> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html">Amazon Linux 2023</a>: Default for non-GPU instance families.</p> <note> <p>Amazon Linux 2023 does not support <code>A1</code> instances.</p> </note> </dd> <dt>EKS_AL2023_NVIDIA</dt> <dd> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html">Amazon Linux 2023 (accelerated)</a>: Default for GPU instance families and can be used for all non Amazon Web Services Graviton-based instance types.</p> </dd> </dl> </dd> </dl>"""
    image_id_override: NotRequired["capo_batch.types.image_id_override.ImageIdOverride"]
    """<p>The AMI ID used for instances launched in the compute environment that match the image type. This setting overrides the <code>imageId</code> set in the <code>computeResource</code> object.</p> <note> <p>The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2023 AMI. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html">Amazon ECS-optimized Amazon Linux 2023 AMI</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>"""
    batch_image_status: NotRequired["capo_batch.types.string.String"]
    """<p>The status of the Batch-provided default AMIs associated with the <code>imageType</code>.</p> <p>The field only appears after the compute environment has begun scaling instances using the <code>imageType</code>. The field is not present when an image is specified in <code>ComputeResources.imageId</code> (deprecated), the default launch template, or <code>Ec2Configuration.imageIdOverride</code>. The field is also not present when the compute environment has a launch template override. For more information on image selection, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/ami-selection-order.html">AMI selection order</a>.</p> <note> <p>This field is read-only and only appears in the <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeComputeEnvironments.html">DescribeComputeEnvironments</a> response.</p> </note> <ul> <li> <p> <code>LATEST</code> − Using the most recent AMI supported</p> </li> <li> <p> <code>UPDATE_AVAILABLE</code> − An updated AMI is available</p> <ul> <li> <p>If a compute environment has multiple AMIs for the <code>imageType</code> and any one AMI has <code>UPDATE_AVAILABLE</code>, the status shows <code>UPDATE_AVAILABLE</code>.</p> </li> <li> <p>For compute environments that use <code>BEST_FIT</code> as their allocation strategy, you can perform a <a href="https://docs.aws.amazon.com/batch/latest/userguide/blue-green-updates.html">blue/green update</a> to update the AMI.</p> </li> <li> <p>For all other compute environments, you can perform an <a href="https://docs.aws.amazon.com/batch/latest/userguide/managing-ami-versions.html#updating-ami-versions">AMI version update</a> to update the AMI to the latest version.</p> </li> </ul> </li> </ul>"""
    image_kubernetes_version: NotRequired[
        "capo_batch.types.kubernetes_version.KubernetesVersion"
    ]
    """<p>The Kubernetes version for the compute environment. If you don't specify a value, the latest version that Batch supports is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Configuration) -> dict:
    out: dict = {}
    if "image_type" in value:
        out["imageType"] = value["image_type"]
    if "image_id_override" in value:
        out["imageIdOverride"] = value["image_id_override"]
    if "batch_image_status" in value:
        out["batchImageStatus"] = value["batch_image_status"]
    if "image_kubernetes_version" in value:
        out["imageKubernetesVersion"] = value["image_kubernetes_version"]
    return out


def deserialize_json(data: dict) -> Ec2Configuration:
    out: Ec2Configuration = {}  # type: ignore[typeddict-item]
    if data.get("imageType") is not None:
        out["image_type"] = data["imageType"]
    if data.get("imageIdOverride") is not None:
        out["image_id_override"] = data["imageIdOverride"]
    if data.get("batchImageStatus") is not None:
        out["batch_image_status"] = data["batchImageStatus"]
    if data.get("imageKubernetesVersion") is not None:
        out["image_kubernetes_version"] = data["imageKubernetesVersion"]
    return out

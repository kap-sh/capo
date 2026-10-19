"""Generated from Smithy shape ``com.amazonaws.bedrock#SageMakerEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.instance_count
    import capo_bedrock.types.instance_type
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.vpc_config


class SageMakerEndpoint(TypedDict, closed=True):
    initial_instance_count: "capo_bedrock.types.instance_count.InstanceCount"
    """<p>The number of Amazon EC2 compute instances to deploy for initial endpoint creation.</p>"""
    instance_type: "capo_bedrock.types.instance_type.InstanceType"
    """<p>The Amazon EC2 compute instance type to deploy for hosting the model.</p>"""
    execution_role: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on Amazon EC2 compute instances or for batch transform jobs.</p>"""
    kms_encryption_key: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the Amazon EC2 compute instance that hosts the endpoint.</p>"""
    vpc: NotRequired["capo_bedrock.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerEndpoint) -> dict:
    out: dict = {}
    out["initialInstanceCount"] = value["initial_instance_count"]
    out["instanceType"] = value["instance_type"]
    out["executionRole"] = value["execution_role"]
    if "kms_encryption_key" in value:
        out["kmsEncryptionKey"] = value["kms_encryption_key"]
    if "vpc" in value:
        import capo_bedrock.types.vpc_config

        out["vpc"] = capo_bedrock.types.vpc_config.serialize_json(value["vpc"])
    return out


def deserialize_json(data: dict) -> SageMakerEndpoint:
    out: SageMakerEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("initialInstanceCount") is not None:
        out["initial_instance_count"] = data["initialInstanceCount"]
    else:
        out["initial_instance_count"] = 0
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    else:
        out["execution_role"] = ""
    if data.get("kmsEncryptionKey") is not None:
        out["kms_encryption_key"] = data["kmsEncryptionKey"]
    if data.get("vpc") is not None:
        import capo_bedrock.types.vpc_config

        out["vpc"] = capo_bedrock.types.vpc_config.deserialize_json(data["vpc"])
    return out

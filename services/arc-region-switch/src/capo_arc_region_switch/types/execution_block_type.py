"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionBlockType``."""

from typing import Literal, TypeAlias, cast

ExecutionBlockType: TypeAlias = Literal[
    "CustomActionLambda",
    "ManualApproval",
    "AuroraGlobalDatabase",
    "EC2AutoScaling",
    "ARCRoutingControl",
    "ARCRegionSwitchPlan",
    "Parallel",
    "ECSServiceScaling",
    "EKSResourceScaling",
    "Route53HealthCheck",
    "DocumentDb",
    "RdsPromoteReadReplica",
    "RdsCreateCrossRegionReplica",
    "LambdaEventSourceMapping",
    "AuroraServerlessScaling",
    "AuroraProvisionedScaling",
    "NeptuneGlobalDatabase",
    "RdsSwitchoverReadReplica",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionBlockType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionBlockType:
    return cast(ExecutionBlockType, data)

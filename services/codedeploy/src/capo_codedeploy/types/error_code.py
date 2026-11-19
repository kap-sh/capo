"""Generated from Smithy shape ``com.amazonaws.codedeploy#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "AGENT_ISSUE",
    "ALARM_ACTIVE",
    "APPLICATION_MISSING",
    "AUTOSCALING_VALIDATION_ERROR",
    "AUTO_SCALING_CONFIGURATION",
    "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
    "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
    "CUSTOMER_APPLICATION_UNHEALTHY",
    "DEPLOYMENT_GROUP_MISSING",
    "ECS_UPDATE_ERROR",
    "ELASTIC_LOAD_BALANCING_INVALID",
    "ELB_INVALID_INSTANCE",
    "HEALTH_CONSTRAINTS",
    "HEALTH_CONSTRAINTS_INVALID",
    "HOOK_EXECUTION_FAILURE",
    "IAM_ROLE_MISSING",
    "IAM_ROLE_PERMISSIONS",
    "INTERNAL_ERROR",
    "INVALID_ECS_SERVICE",
    "INVALID_LAMBDA_CONFIGURATION",
    "INVALID_LAMBDA_FUNCTION",
    "INVALID_REVISION",
    "MANUAL_STOP",
    "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
    "MISSING_ELB_INFORMATION",
    "MISSING_GITHUB_TOKEN",
    "NO_EC2_SUBSCRIPTION",
    "NO_INSTANCES",
    "OVER_MAX_INSTANCES",
    "RESOURCE_LIMIT_EXCEEDED",
    "REVISION_MISSING",
    "THROTTLED",
    "TIMEOUT",
    "CLOUDFORMATION_STACK_FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    return cast(ErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> ErrorCode:
    return cast(ErrorCode, data)

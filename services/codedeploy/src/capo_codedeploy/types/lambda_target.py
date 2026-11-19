"""Generated from Smithy shape ``com.amazonaws.codedeploy#LambdaTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.lambda_function_info
    import capo_codedeploy.types.lifecycle_event_list
    import capo_codedeploy.types.target_arn
    import capo_codedeploy.types.target_id
    import capo_codedeploy.types.target_status
    import capo_codedeploy.types.time


class LambdaTarget(TypedDict, closed=True):
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    target_id: NotRequired["capo_codedeploy.types.target_id.TargetId"]
    """<p> The unique ID of a deployment target that has a type of <code>lambdaTarget</code>. </p>"""
    target_arn: NotRequired["capo_codedeploy.types.target_arn.TargetArn"]
    """<p> The Amazon Resource Name (ARN) of the target. </p>"""
    status: NotRequired["capo_codedeploy.types.target_status.TargetStatus"]
    """<p> The status an Lambda deployment's target Lambda function. </p>"""
    last_updated_at: NotRequired["capo_codedeploy.types.time.Time"]
    """<p> The date and time when the target Lambda function was updated by a deployment. </p>"""
    lifecycle_events: NotRequired[
        "capo_codedeploy.types.lifecycle_event_list.LifecycleEventList"
    ]
    """<p> The lifecycle events of the deployment to this target Lambda function. </p>"""
    lambda_function_info: NotRequired[
        "capo_codedeploy.types.lambda_function_info.LambdaFunctionInfo"
    ]
    """<p> A <code>LambdaFunctionInfo</code> object that describes a target Lambda function. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaTarget) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import capo_codedeploy.types.target_status

        out["status"] = capo_codedeploy.types.target_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "last_updated_at" in value:
        import capo_codedeploy.types.time

        out["lastUpdatedAt"] = capo_codedeploy.types.time.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "lifecycle_events" in value:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            capo_codedeploy.types.lifecycle_event_list.serialize_aws_json_1_1(
                value["lifecycle_events"]
            )
        )
    if "lambda_function_info" in value:
        import capo_codedeploy.types.lambda_function_info

        out["lambdaFunctionInfo"] = (
            capo_codedeploy.types.lambda_function_info.serialize_aws_json_1_1(
                value["lambda_function_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaTarget:
    out: LambdaTarget = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("status") is not None:
        import capo_codedeploy.types.target_status

        out["status"] = capo_codedeploy.types.target_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_codedeploy.types.time

        out["last_updated_at"] = capo_codedeploy.types.time.deserialize_aws_json_1_1(
            data["lastUpdatedAt"]
        )
    if data.get("lifecycleEvents") is not None:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            capo_codedeploy.types.lifecycle_event_list.deserialize_aws_json_1_1(
                data["lifecycleEvents"]
            )
        )
    if data.get("lambdaFunctionInfo") is not None:
        import capo_codedeploy.types.lambda_function_info

        out["lambda_function_info"] = (
            capo_codedeploy.types.lambda_function_info.deserialize_aws_json_1_1(
                data["lambdaFunctionInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaTarget) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import capo_codedeploy.types.target_status

        out["status"] = capo_codedeploy.types.target_status.serialize_cbor(
            value["status"]
        )
    if "last_updated_at" in value:
        import capo_codedeploy.types.time

        out["lastUpdatedAt"] = capo_codedeploy.types.time.serialize_cbor(
            value["last_updated_at"]
        )
    if "lifecycle_events" in value:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            capo_codedeploy.types.lifecycle_event_list.serialize_cbor(
                value["lifecycle_events"]
            )
        )
    if "lambda_function_info" in value:
        import capo_codedeploy.types.lambda_function_info

        out["lambdaFunctionInfo"] = (
            capo_codedeploy.types.lambda_function_info.serialize_cbor(
                value["lambda_function_info"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LambdaTarget:
    out: LambdaTarget = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("status") is not None:
        import capo_codedeploy.types.target_status

        out["status"] = capo_codedeploy.types.target_status.deserialize_cbor(
            data["status"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_codedeploy.types.time

        out["last_updated_at"] = capo_codedeploy.types.time.deserialize_cbor(
            data["lastUpdatedAt"]
        )
    if data.get("lifecycleEvents") is not None:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            capo_codedeploy.types.lifecycle_event_list.deserialize_cbor(
                data["lifecycleEvents"]
            )
        )
    if data.get("lambdaFunctionInfo") is not None:
        import capo_codedeploy.types.lambda_function_info

        out["lambda_function_info"] = (
            capo_codedeploy.types.lambda_function_info.deserialize_cbor(
                data["lambdaFunctionInfo"]
            )
        )
    return out

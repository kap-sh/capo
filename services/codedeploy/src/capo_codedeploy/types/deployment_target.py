"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.cloud_formation_target
    import capo_codedeploy.types.deployment_target_type
    import capo_codedeploy.types.ecs_target
    import capo_codedeploy.types.instance_target
    import capo_codedeploy.types.lambda_target


class DeploymentTarget(TypedDict, closed=True):
    deployment_target_type: NotRequired[
        "capo_codedeploy.types.deployment_target_type.DeploymentTargetType"
    ]
    """<p>The deployment type that is specific to the deployment's compute platform or deployments initiated by a CloudFormation stack update.</p>"""
    instance_target: NotRequired["capo_codedeploy.types.instance_target.InstanceTarget"]
    """<p> Information about the target for a deployment that uses the EC2/On-premises compute platform. </p>"""
    lambda_target: NotRequired["capo_codedeploy.types.lambda_target.LambdaTarget"]
    """<p> Information about the target for a deployment that uses the Lambda compute platform. </p>"""
    ecs_target: NotRequired["capo_codedeploy.types.ecs_target.ECSTarget"]
    """<p> Information about the target for a deployment that uses the Amazon ECS compute platform. </p>"""
    cloud_formation_target: NotRequired[
        "capo_codedeploy.types.cloud_formation_target.CloudFormationTarget"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentTarget) -> dict:
    out: dict = {}
    if "deployment_target_type" in value:
        import capo_codedeploy.types.deployment_target_type

        out["deploymentTargetType"] = (
            capo_codedeploy.types.deployment_target_type.serialize_aws_json_1_1(
                value["deployment_target_type"]
            )
        )
    if "instance_target" in value:
        import capo_codedeploy.types.instance_target

        out["instanceTarget"] = (
            capo_codedeploy.types.instance_target.serialize_aws_json_1_1(
                value["instance_target"]
            )
        )
    if "lambda_target" in value:
        import capo_codedeploy.types.lambda_target

        out["lambdaTarget"] = (
            capo_codedeploy.types.lambda_target.serialize_aws_json_1_1(
                value["lambda_target"]
            )
        )
    if "ecs_target" in value:
        import capo_codedeploy.types.ecs_target

        out["ecsTarget"] = capo_codedeploy.types.ecs_target.serialize_aws_json_1_1(
            value["ecs_target"]
        )
    if "cloud_formation_target" in value:
        import capo_codedeploy.types.cloud_formation_target

        out["cloudFormationTarget"] = (
            capo_codedeploy.types.cloud_formation_target.serialize_aws_json_1_1(
                value["cloud_formation_target"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentTarget:
    out: DeploymentTarget = {}  # type: ignore[typeddict-item]
    if data.get("deploymentTargetType") is not None:
        import capo_codedeploy.types.deployment_target_type

        out["deployment_target_type"] = (
            capo_codedeploy.types.deployment_target_type.deserialize_aws_json_1_1(
                data["deploymentTargetType"]
            )
        )
    if data.get("instanceTarget") is not None:
        import capo_codedeploy.types.instance_target

        out["instance_target"] = (
            capo_codedeploy.types.instance_target.deserialize_aws_json_1_1(
                data["instanceTarget"]
            )
        )
    if data.get("lambdaTarget") is not None:
        import capo_codedeploy.types.lambda_target

        out["lambda_target"] = (
            capo_codedeploy.types.lambda_target.deserialize_aws_json_1_1(
                data["lambdaTarget"]
            )
        )
    if data.get("ecsTarget") is not None:
        import capo_codedeploy.types.ecs_target

        out["ecs_target"] = capo_codedeploy.types.ecs_target.deserialize_aws_json_1_1(
            data["ecsTarget"]
        )
    if data.get("cloudFormationTarget") is not None:
        import capo_codedeploy.types.cloud_formation_target

        out["cloud_formation_target"] = (
            capo_codedeploy.types.cloud_formation_target.deserialize_aws_json_1_1(
                data["cloudFormationTarget"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentTarget) -> dict:
    out: dict = {}
    if "deployment_target_type" in value:
        import capo_codedeploy.types.deployment_target_type

        out["deploymentTargetType"] = (
            capo_codedeploy.types.deployment_target_type.serialize_cbor(
                value["deployment_target_type"]
            )
        )
    if "instance_target" in value:
        import capo_codedeploy.types.instance_target

        out["instanceTarget"] = capo_codedeploy.types.instance_target.serialize_cbor(
            value["instance_target"]
        )
    if "lambda_target" in value:
        import capo_codedeploy.types.lambda_target

        out["lambdaTarget"] = capo_codedeploy.types.lambda_target.serialize_cbor(
            value["lambda_target"]
        )
    if "ecs_target" in value:
        import capo_codedeploy.types.ecs_target

        out["ecsTarget"] = capo_codedeploy.types.ecs_target.serialize_cbor(
            value["ecs_target"]
        )
    if "cloud_formation_target" in value:
        import capo_codedeploy.types.cloud_formation_target

        out["cloudFormationTarget"] = (
            capo_codedeploy.types.cloud_formation_target.serialize_cbor(
                value["cloud_formation_target"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeploymentTarget:
    out: DeploymentTarget = {}  # type: ignore[typeddict-item]
    if data.get("deploymentTargetType") is not None:
        import capo_codedeploy.types.deployment_target_type

        out["deployment_target_type"] = (
            capo_codedeploy.types.deployment_target_type.deserialize_cbor(
                data["deploymentTargetType"]
            )
        )
    if data.get("instanceTarget") is not None:
        import capo_codedeploy.types.instance_target

        out["instance_target"] = capo_codedeploy.types.instance_target.deserialize_cbor(
            data["instanceTarget"]
        )
    if data.get("lambdaTarget") is not None:
        import capo_codedeploy.types.lambda_target

        out["lambda_target"] = capo_codedeploy.types.lambda_target.deserialize_cbor(
            data["lambdaTarget"]
        )
    if data.get("ecsTarget") is not None:
        import capo_codedeploy.types.ecs_target

        out["ecs_target"] = capo_codedeploy.types.ecs_target.deserialize_cbor(
            data["ecsTarget"]
        )
    if data.get("cloudFormationTarget") is not None:
        import capo_codedeploy.types.cloud_formation_target

        out["cloud_formation_target"] = (
            capo_codedeploy.types.cloud_formation_target.deserialize_cbor(
                data["cloudFormationTarget"]
            )
        )
    return out

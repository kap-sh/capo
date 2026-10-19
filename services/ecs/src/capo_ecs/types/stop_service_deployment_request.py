"""Generated from Smithy shape ``com.amazonaws.ecs#StopServiceDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.stop_service_deployment_stop_type
    import capo_ecs.types.string


class StopServiceDeploymentRequest(TypedDict, closed=True):
    service_deployment_arn: "capo_ecs.types.string.String"
    """<p>The ARN of the service deployment that you want to stop.</p>"""
    stop_type: NotRequired[
        "capo_ecs.types.stop_service_deployment_stop_type.StopServiceDeploymentStopType"
    ]
    """<p>How you want Amazon ECS to stop the service. </p> <p>The valid values are <code>ROLLBACK</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopServiceDeploymentRequest) -> dict:
    out: dict = {}
    out["serviceDeploymentArn"] = value["service_deployment_arn"]
    if "stop_type" in value:
        import capo_ecs.types.stop_service_deployment_stop_type

        out["stopType"] = (
            capo_ecs.types.stop_service_deployment_stop_type.serialize_aws_json_1_1(
                value["stop_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopServiceDeploymentRequest:
    out: StopServiceDeploymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceDeploymentArn") is not None:
        out["service_deployment_arn"] = data["serviceDeploymentArn"]
    else:
        out["service_deployment_arn"] = ""
    if data.get("stopType") is not None:
        import capo_ecs.types.stop_service_deployment_stop_type

        out["stop_type"] = (
            capo_ecs.types.stop_service_deployment_stop_type.deserialize_aws_json_1_1(
                data["stopType"]
            )
        )
    return out

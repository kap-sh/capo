"""Generated from Smithy shape ``com.amazonaws.ecs#CreateServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service


class CreateServiceResponse(TypedDict, closed=True):
    service: NotRequired["capo_ecs.types.service.Service"]
    """<p>The full description of your service following the create call.</p> <p>A service will return either a <code>capacityProviderStrategy</code> or <code>launchType</code> parameter, but not both, depending where one was specified when it was created.</p> <p>If a service is using the <code>ECS</code> deployment controller, the <code>deploymentController</code> and <code>taskSets</code> parameters will not be returned.</p> <p>if the service uses the <code>CODE_DEPLOY</code> deployment controller, the <code>deploymentController</code>, <code>taskSets</code> and <code>deployments</code> parameters will be returned, however the <code>deployments</code> parameter will be an empty list.</p> <p>The response includes a <code>lifecycleHookDetails</code> field, which is an empty array when the service is created or updated. The values are populated when a lifecycle hook executes and are available as part of the service deployment details (<a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html">DescribeServiceDeployments</a>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_ecs.types.service

        out["service"] = capo_ecs.types.service.serialize_aws_json_1_1(value["service"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateServiceResponse:
    out: CreateServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_ecs.types.service

        out["service"] = capo_ecs.types.service.deserialize_aws_json_1_1(
            data["service"]
        )
    return out

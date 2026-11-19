"""Generated from Smithy shape ``com.amazonaws.sagemaker#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.destination_resource_arn
    import capo_sagemaker.types.routing_status


class Destination(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_sagemaker.types.destination_resource_arn.DestinationResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint or inference component. The destination can be in any account, and in any Amazon Web Services Region in the same partition as the inference router. To use a destination in another account, its owner must allow your account to invoke it through your router, in an endpoint policy.</p>"""
    routing_status: NotRequired["capo_sagemaker.types.routing_status.RoutingStatus"]
    """<p>Whether the inference router can send requests to the destination, as checked when you called <code>DescribeInferenceRouter</code>. This value isn't the destination's own status. SageMaker AI ignores this field in <code>CreateInferenceRouter</code> and <code>UpdateInferenceRouter</code> requests.</p> <dl> <dt>Routable</dt> <dd> <p>The destination is serving and the router can send it requests. A routable destination can still be overloaded.</p> </dd> <dt>Unroutable</dt> <dd> <p>The destination can't serve requests. For example, it's being created or has failed, or it has no capacity and no way to get any. A destination in your account that doesn't exist is also <code>Unroutable</code>.</p> </dd> <dt>Unknown</dt> <dd> <p>SageMaker AI couldn't check the destination, for example because you aren't allowed to describe it or the check timed out. The destination might still be serving.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Destination) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "routing_status" in value:
        import capo_sagemaker.types.routing_status

        out["RoutingStatus"] = (
            capo_sagemaker.types.routing_status.serialize_aws_json_1_1(
                value["routing_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("RoutingStatus") is not None:
        import capo_sagemaker.types.routing_status

        out["routing_status"] = (
            capo_sagemaker.types.routing_status.deserialize_aws_json_1_1(
                data["RoutingStatus"]
            )
        )
    return out

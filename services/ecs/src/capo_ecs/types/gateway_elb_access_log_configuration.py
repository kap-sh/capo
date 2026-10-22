"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayElbAccessLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_elb_access_log_destination


class GatewayElbAccessLogConfiguration(TypedDict, closed=True):
    destination: NotRequired[
        "capo_ecs.types.gateway_elb_access_log_destination.GatewayElbAccessLogDestination"
    ]
    """<p>The destination where access logs are delivered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayElbAccessLogConfiguration) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_ecs.types.gateway_elb_access_log_destination

        out["destination"] = (
            capo_ecs.types.gateway_elb_access_log_destination.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayElbAccessLogConfiguration:
    out: GatewayElbAccessLogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destination") is not None:
        import capo_ecs.types.gateway_elb_access_log_destination

        out["destination"] = (
            capo_ecs.types.gateway_elb_access_log_destination.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    return out

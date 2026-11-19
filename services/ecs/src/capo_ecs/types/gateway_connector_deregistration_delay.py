"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectorDeregistrationDelay``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer


class GatewayConnectorDeregistrationDelay(TypedDict, closed=True):
    timeout_seconds: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The amount of time, in seconds, to wait before a deregistering target is removed. A value of <code>0</code> removes the target immediately. The valid range is 0-3600 seconds. The default value is 300 seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectorDeregistrationDelay) -> dict:
    out: dict = {}
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayConnectorDeregistrationDelay:
    out: GatewayConnectorDeregistrationDelay = {}  # type: ignore[typeddict-item]
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    return out

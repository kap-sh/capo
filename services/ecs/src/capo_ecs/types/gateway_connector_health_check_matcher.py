"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectorHealthCheckMatcher``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class GatewayConnectorHealthCheckMatcher(TypedDict, closed=True):
    http_code: NotRequired["capo_ecs.types.string.String"]
    """<p>The HTTP codes that indicate a successful response from a target.</p>"""
    grpc_code: NotRequired["capo_ecs.types.string.String"]
    """<p>The gRPC codes that indicate a successful response from a target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectorHealthCheckMatcher) -> dict:
    out: dict = {}
    if "http_code" in value:
        out["httpCode"] = value["http_code"]
    if "grpc_code" in value:
        out["grpcCode"] = value["grpc_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayConnectorHealthCheckMatcher:
    out: GatewayConnectorHealthCheckMatcher = {}  # type: ignore[typeddict-item]
    if data.get("httpCode") is not None:
        out["http_code"] = data["httpCode"]
    if data.get("grpcCode") is not None:
        out["grpc_code"] = data["grpcCode"]
    return out

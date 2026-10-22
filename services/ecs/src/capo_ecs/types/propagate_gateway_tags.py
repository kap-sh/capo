"""Generated from Smithy shape ``com.amazonaws.ecs#PropagateGatewayTags``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether the tags on a gateway are propagated to the infrastructure that the gateway manages.</p>"""
PropagateGatewayTags: TypeAlias = Literal[
    "NONE",
    "GATEWAY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropagateGatewayTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropagateGatewayTags:
    return cast(PropagateGatewayTags, data)

"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.connection_arn


class GetConnectionInput(TypedDict, closed=True):
    connection_arn: "capo_codestar_connections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of a connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionInput) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionInput:
    out: GetConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        out["connection_arn"] = ""
    return out

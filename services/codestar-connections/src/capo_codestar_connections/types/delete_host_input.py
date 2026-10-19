"""Generated from Smithy shape ``com.amazonaws.codestarconnections#DeleteHostInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.host_arn


class DeleteHostInput(TypedDict, closed=True):
    host_arn: "capo_codestar_connections.types.host_arn.HostArn"
    """<p>The Amazon Resource Name (ARN) of the host to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteHostInput) -> dict:
    out: dict = {}
    out["HostArn"] = value["host_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteHostInput:
    out: DeleteHostInput = {}  # type: ignore[typeddict-item]
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    else:
        out["host_arn"] = ""
    return out

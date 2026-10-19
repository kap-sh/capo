"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetHostInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.host_arn


class GetHostInput(TypedDict, closed=True):
    host_arn: "capo_codeconnections.types.host_arn.HostArn"
    """<p>The Amazon Resource Name (ARN) of the requested host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetHostInput) -> dict:
    out: dict = {}
    out["HostArn"] = value["host_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetHostInput:
    out: GetHostInput = {}  # type: ignore[typeddict-item]
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    else:
        out["host_arn"] = ""
    return out

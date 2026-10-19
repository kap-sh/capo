"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DescribeDaemonRequest(TypedDict, closed=True):
    daemon_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonRequest) -> dict:
    out: dict = {}
    out["daemonArn"] = value["daemon_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonRequest:
    out: DescribeDaemonRequest = {}  # type: ignore[typeddict-item]
    if data.get("daemonArn") is not None:
        out["daemon_arn"] = data["daemonArn"]
    else:
        out["daemon_arn"] = ""
    return out

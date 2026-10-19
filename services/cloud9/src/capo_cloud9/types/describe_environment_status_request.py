"""Generated from Smithy shape ``com.amazonaws.cloud9#DescribeEnvironmentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_id


class DescribeEnvironmentStatusRequest(TypedDict, closed=True):
    environment_id: "capo_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment to get status information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEnvironmentStatusRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEnvironmentStatusRequest:
    out: DescribeEnvironmentStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    return out

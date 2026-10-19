"""Generated from Smithy shape ``com.amazonaws.interconnect#GetEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.environment_id


class GetEnvironmentRequest(TypedDict, closed=True):
    id: "capo_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of the specific <a>Environment</a> to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentRequest:
    out: GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeConnectionsOnInterconnectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.interconnect_id


class DescribeConnectionsOnInterconnectRequest(TypedDict, closed=True):
    interconnect_id: "capo_direct_connect.types.interconnect_id.InterconnectId"
    """<p>The ID of the interconnect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionsOnInterconnectRequest) -> dict:
    out: dict = {}
    out["interconnectId"] = value["interconnect_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionsOnInterconnectRequest:
    out: DescribeConnectionsOnInterconnectRequest = {}  # type: ignore[typeddict-item]
    if data.get("interconnectId") is not None:
        out["interconnect_id"] = data["interconnectId"]
    else:
        out["interconnect_id"] = ""
    return out

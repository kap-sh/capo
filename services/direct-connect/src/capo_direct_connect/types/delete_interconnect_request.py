"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteInterconnectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.interconnect_id


class DeleteInterconnectRequest(TypedDict, closed=True):
    interconnect_id: "capo_direct_connect.types.interconnect_id.InterconnectId"
    """<p>The ID of the interconnect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInterconnectRequest) -> dict:
    out: dict = {}
    out["interconnectId"] = value["interconnect_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInterconnectRequest:
    out: DeleteInterconnectRequest = {}  # type: ignore[typeddict-item]
    if data.get("interconnectId") is not None:
        out["interconnect_id"] = data["interconnectId"]
    else:
        out["interconnect_id"] = ""
    return out

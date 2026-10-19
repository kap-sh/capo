"""Generated from Smithy shape ``com.amazonaws.keyspaces#ClientSideTimestamps``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.client_side_timestamps_status


class ClientSideTimestamps(TypedDict, closed=True):
    status: (
        "capo_keyspaces.types.client_side_timestamps_status.ClientSideTimestampsStatus"
    )
    """<p>Shows how to enable client-side timestamps settings for the specified table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClientSideTimestamps) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ClientSideTimestamps:
    out: ClientSideTimestamps = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out

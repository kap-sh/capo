"""Generated from Smithy shape ``com.amazonaws.keyspaces#PointInTimeRecovery``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.point_in_time_recovery_status


class PointInTimeRecovery(TypedDict, closed=True):
    status: (
        "capo_keyspaces.types.point_in_time_recovery_status.PointInTimeRecoveryStatus"
    )
    """<p>The options are:</p> <ul> <li> <p> <code>status=ENABLED</code> </p> </li> <li> <p> <code>status=DISABLED</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecovery) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecovery:
    out: PointInTimeRecovery = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out

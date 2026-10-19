"""Generated from Smithy shape ``com.amazonaws.quicksight#RdsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.database
    import capo_quicksight.types.instance_id


class RdsParameters(TypedDict, closed=True):
    instance_id: "capo_quicksight.types.instance_id.InstanceId"
    """<p>Instance ID.</p>"""
    database: "capo_quicksight.types.database.Database"
    """<p>Database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsParameters) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["Database"] = value["database"]
    return out


def deserialize_json(data: dict) -> RdsParameters:
    out: RdsParameters = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    return out

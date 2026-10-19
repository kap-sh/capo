"""Generated from Smithy shape ``com.amazonaws.qapps#DeleteQAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class DeleteQAppInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQAppInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    return out


def deserialize_json(data: dict) -> DeleteQAppInput:
    out: DeleteQAppInput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.qapps#AssociateQAppWithUserInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class AssociateQAppWithUserInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The ID of the Amazon Q App to associate with the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateQAppWithUserInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    return out


def deserialize_json(data: dict) -> AssociateQAppWithUserInput:
    out: AssociateQAppWithUserInput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    return out

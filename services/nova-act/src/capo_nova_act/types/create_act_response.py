"""Generated from Smithy shape ``com.amazonaws.novaact#CreateActResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.act_status
    import capo_nova_act.types.uuid_string


class CreateActResponse(TypedDict, closed=True):
    act_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier for the created act.</p>"""
    status: "capo_nova_act.types.act_status.ActStatus"
    """<p>The initial status of the act after creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActResponse) -> dict:
    out: dict = {}
    out["actId"] = value["act_id"]
    import capo_nova_act.types.act_status

    out["status"] = capo_nova_act.types.act_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateActResponse:
    out: CreateActResponse = {}  # type: ignore[typeddict-item]
    if data.get("actId") is not None:
        out["act_id"] = data["actId"]
    else:
        out["act_id"] = ""
    if data.get("status") is not None:
        import capo_nova_act.types.act_status

        out["status"] = capo_nova_act.types.act_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_nova_act.types.act_status.ActStatus", "")
    return out

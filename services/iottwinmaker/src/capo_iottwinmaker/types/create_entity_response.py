"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.state
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class CreateEntityResponse(TypedDict, closed=True):
    entity_id: "capo_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the entity.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was created.</p>"""
    state: "capo_iottwinmaker.types.state.State"
    """<p>The current state of the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEntityResponse) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    out["arn"] = value["arn"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> CreateEntityResponse:
    out: CreateEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        out["entity_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("creationDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        import datetime

        out["creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out

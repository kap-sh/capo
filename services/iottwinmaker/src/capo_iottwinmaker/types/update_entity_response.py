"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.state
    import capo_iottwinmaker.types.timestamp


class UpdateEntityResponse(TypedDict, closed=True):
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the entity was last updated.</p>"""
    state: "capo_iottwinmaker.types.state.State"
    """<p>The current state of the entity update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEntityResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> UpdateEntityResponse:
    out: UpdateEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out

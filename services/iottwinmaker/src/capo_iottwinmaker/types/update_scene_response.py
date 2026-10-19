"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateSceneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.timestamp


class UpdateSceneResponse(TypedDict, closed=True):
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSceneResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSceneResponse:
    out: UpdateSceneResponse = {}  # type: ignore[typeddict-item]
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
    return out

"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

TimeWindow = TypedDict(
    "TimeWindow",
    {
        "from": NotRequired["datetime.datetime"],
        "to": NotRequired["datetime.datetime"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: TimeWindow) -> dict:
    out: dict = {}
    if "from" in value:
        import capo_wellarchitected._protocol.serialize

        out["from"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["from"]
        )
    if "to" in value:
        import capo_wellarchitected._protocol.serialize

        out["to"] = capo_wellarchitected._protocol.serialize.fmt_date_time(value["to"])
    return out


def deserialize_json(data: dict) -> TimeWindow:
    out: TimeWindow = {}  # type: ignore[typeddict-item]
    if data.get("from") is not None:
        import datetime

        out["from"] = datetime.datetime.fromisoformat(
            data["from"].replace("Z", "+00:00")
        )
    if data.get("to") is not None:
        import datetime

        out["to"] = datetime.datetime.fromisoformat(data["to"].replace("Z", "+00:00"))
    return out

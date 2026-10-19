"""Generated from Smithy shape ``com.amazonaws.connect#SentimentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.behavior


class SentimentConfiguration(TypedDict, closed=True):
    behavior: "capo_connect.types.behavior.Behavior"
    """<p>Controls whether sentiment analysis is applied to the analytics output. Valid values: <code>Enable</code> | <code>Disable</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SentimentConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.behavior

    out["Behavior"] = capo_connect.types.behavior.serialize_json(value["behavior"])
    return out


def deserialize_json(data: dict) -> SentimentConfiguration:
    out: SentimentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Behavior") is not None:
        import capo_connect.types.behavior

        out["behavior"] = capo_connect.types.behavior.deserialize_json(data["Behavior"])
    else:
        import typing

        out["behavior"] = typing.cast("capo_connect.types.behavior.Behavior", "")
    return out

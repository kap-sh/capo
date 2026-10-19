"""Generated from Smithy shape ``com.amazonaws.quicksight#UserNameOrEmailFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filter_value


class UserNameOrEmailFilter(TypedDict, closed=True):
    prefix: "capo_quicksight.types.filter_value.FilterValue"
    """<p>The prefix to match against username or email (starts-with match).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserNameOrEmailFilter) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> UserNameOrEmailFilter:
    out: UserNameOrEmailFilter = {}  # type: ignore[typeddict-item]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    return out

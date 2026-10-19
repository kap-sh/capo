"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.ruleset_name


class CreateRulesetResponse(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The unique name of the created ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRulesetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateRulesetResponse:
    out: CreateRulesetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out

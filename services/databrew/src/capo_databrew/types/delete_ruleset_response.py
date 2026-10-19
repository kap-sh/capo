"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.ruleset_name


class DeleteRulesetResponse(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the deleted ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRulesetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteRulesetResponse:
    out: DeleteRulesetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out

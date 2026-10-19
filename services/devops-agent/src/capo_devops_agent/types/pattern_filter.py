"""Generated from Smithy shape ``com.amazonaws.devopsagent#PatternFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.trigger_regex_pattern_list


class PatternFilter(TypedDict, closed=True):
    patterns: (
        "capo_devops_agent.types.trigger_regex_pattern_list.TriggerRegexPatternList"
    )
    """<p>Anchored full-match regex patterns. The condition passes when the value matches at least one pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatternFilter) -> dict:
    out: dict = {}
    import capo_devops_agent.types.trigger_regex_pattern_list

    out["patterns"] = capo_devops_agent.types.trigger_regex_pattern_list.serialize_json(
        value["patterns"]
    )
    return out


def deserialize_json(data: dict) -> PatternFilter:
    out: PatternFilter = {}  # type: ignore[typeddict-item]
    if data.get("patterns") is not None:
        import capo_devops_agent.types.trigger_regex_pattern_list

        out["patterns"] = (
            capo_devops_agent.types.trigger_regex_pattern_list.deserialize_json(
                data["patterns"]
            )
        )
    else:
        out["patterns"] = []
    return out

"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.trigger_filter_match_mode
    import capo_securityagent.types.trigger_filter_type
    import capo_securityagent.types.trigger_regex_pattern_list


class TriggerFilter(TypedDict, closed=True):
    type: "capo_securityagent.types.trigger_filter_type.TriggerFilterType"
    """<p>The pull request value to match.</p>"""
    patterns: (
        "capo_securityagent.types.trigger_regex_pattern_list.TriggerRegexPatternList"
    )
    """<p>The regular expressions to match against the value.</p>"""
    match_mode: NotRequired[
        "capo_securityagent.types.trigger_filter_match_mode.TriggerFilterMatchMode"
    ]
    """<p>Whether the value must match the patterns. The default is <code>INCLUDE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerFilter) -> dict:
    out: dict = {}
    import capo_securityagent.types.trigger_filter_type

    out["type"] = capo_securityagent.types.trigger_filter_type.serialize_json(
        value["type"]
    )
    import capo_securityagent.types.trigger_regex_pattern_list

    out["patterns"] = (
        capo_securityagent.types.trigger_regex_pattern_list.serialize_json(
            value["patterns"]
        )
    )
    if "match_mode" in value:
        import capo_securityagent.types.trigger_filter_match_mode

        out["matchMode"] = (
            capo_securityagent.types.trigger_filter_match_mode.serialize_json(
                value["match_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> TriggerFilter:
    out: TriggerFilter = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_securityagent.types.trigger_filter_type

        out["type"] = capo_securityagent.types.trigger_filter_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("TriggerFilter.type required")
    if data.get("patterns") is not None:
        import capo_securityagent.types.trigger_regex_pattern_list

        out["patterns"] = (
            capo_securityagent.types.trigger_regex_pattern_list.deserialize_json(
                data["patterns"]
            )
        )
    else:
        raise DeserializationError("TriggerFilter.patterns required")
    if data.get("matchMode") is not None:
        import capo_securityagent.types.trigger_filter_match_mode

        out["match_mode"] = (
            capo_securityagent.types.trigger_filter_match_mode.deserialize_json(
                data["matchMode"]
            )
        )
    return out

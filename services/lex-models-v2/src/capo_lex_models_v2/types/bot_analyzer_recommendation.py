"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.issue_location
    import capo_lex_models_v2.types.priority


class BotAnalyzerRecommendation(TypedDict, closed=True):
    issue_location: "capo_lex_models_v2.types.issue_location.IssueLocation"
    """<p>The location information for the identified issue within the bot configuration.</p>"""
    priority: "capo_lex_models_v2.types.priority.Priority"
    """<p>The priority level of the recommendation.</p> <p>Valid Values: <code>High | Medium | Low</code> </p>"""
    issue_description: "capo_lex_models_v2.types.description.Description"
    """<p>A detailed description of the identified configuration issue.</p>"""
    proposed_fix: "capo_lex_models_v2.types.description.Description"
    """<p>The recommended solution to address the identified issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAnalyzerRecommendation) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.issue_location

    out["issueLocation"] = capo_lex_models_v2.types.issue_location.serialize_json(
        value["issue_location"]
    )
    import capo_lex_models_v2.types.priority

    out["priority"] = capo_lex_models_v2.types.priority.serialize_json(
        value["priority"]
    )
    out["issueDescription"] = value["issue_description"]
    out["proposedFix"] = value["proposed_fix"]
    return out


def deserialize_json(data: dict) -> BotAnalyzerRecommendation:
    out: BotAnalyzerRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("issueLocation") is not None:
        import capo_lex_models_v2.types.issue_location

        out["issue_location"] = (
            capo_lex_models_v2.types.issue_location.deserialize_json(
                data["issueLocation"]
            )
        )
    else:
        raise DeserializationError("BotAnalyzerRecommendation.issue_location required")
    if data.get("priority") is not None:
        import capo_lex_models_v2.types.priority

        out["priority"] = capo_lex_models_v2.types.priority.deserialize_json(
            data["priority"]
        )
    else:
        import typing

        out["priority"] = typing.cast("capo_lex_models_v2.types.priority.Priority", "")
    if data.get("issueDescription") is not None:
        out["issue_description"] = data["issueDescription"]
    else:
        out["issue_description"] = ""
    if data.get("proposedFix") is not None:
        out["proposed_fix"] = data["proposedFix"]
    else:
        out["proposed_fix"] = ""
    return out

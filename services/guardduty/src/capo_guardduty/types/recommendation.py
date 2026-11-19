"""Generated from Smithy shape ``com.amazonaws.guardduty#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.action_priority
    import capo_guardduty.types.cli_commands
    import capo_guardduty.types.recommendation_category
    import capo_guardduty.types.string


class Recommendation(TypedDict, closed=True):
    title: NotRequired["capo_guardduty.types.string.String"]
    """<p>A short title for the recommendation.</p>"""
    rationale: NotRequired["capo_guardduty.types.string.String"]
    """<p>The reason for the recommendation.</p>"""
    category: NotRequired[
        "capo_guardduty.types.recommendation_category.RecommendationCategory"
    ]
    """<p>The category of the recommendation. Possible values are <code>ENABLE_PROTECTION</code>, <code>FURTHER_INVESTIGATION</code>, <code>SUPPRESSION_RULE</code>, <code>HARDENING</code>, and <code>MONITORING</code>.</p>"""
    priority: NotRequired["capo_guardduty.types.action_priority.ActionPriority"]
    """<p>The priority of the recommendation. Possible values are <code>IMMEDIATE</code>, <code>SHORT_TERM</code>, and <code>STRATEGIC</code>.</p>"""
    cli_commands: NotRequired["capo_guardduty.types.cli_commands.CliCommands"]
    """<p>CLI commands that you can run to carry out the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "rationale" in value:
        out["rationale"] = value["rationale"]
    if "category" in value:
        import capo_guardduty.types.recommendation_category

        out["category"] = capo_guardduty.types.recommendation_category.serialize_json(
            value["category"]
        )
    if "priority" in value:
        import capo_guardduty.types.action_priority

        out["priority"] = capo_guardduty.types.action_priority.serialize_json(
            value["priority"]
        )
    if "cli_commands" in value:
        import capo_guardduty.types.cli_commands

        out["cliCommands"] = capo_guardduty.types.cli_commands.serialize_json(
            value["cli_commands"]
        )
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("rationale") is not None:
        out["rationale"] = data["rationale"]
    if data.get("category") is not None:
        import capo_guardduty.types.recommendation_category

        out["category"] = capo_guardduty.types.recommendation_category.deserialize_json(
            data["category"]
        )
    if data.get("priority") is not None:
        import capo_guardduty.types.action_priority

        out["priority"] = capo_guardduty.types.action_priority.deserialize_json(
            data["priority"]
        )
    if data.get("cliCommands") is not None:
        import capo_guardduty.types.cli_commands

        out["cli_commands"] = capo_guardduty.types.cli_commands.deserialize_json(
            data["cliCommands"]
        )
    return out

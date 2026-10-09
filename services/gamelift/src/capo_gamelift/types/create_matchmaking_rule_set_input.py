"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateMatchmakingRuleSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_id_string_model
    import capo_gamelift.types.rule_set_body
    import capo_gamelift.types.tag_list


class CreateMatchmakingRuleSetInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for the matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional <code>name</code> field in the rule set body.</p>"""
    rule_set_body: NotRequired["capo_gamelift.types.rule_set_body.RuleSetBody"]
    """<p>A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.</p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new matchmaking rule set resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMatchmakingRuleSetInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "rule_set_body" in value:
        out["RuleSetBody"] = value["rule_set_body"]
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMatchmakingRuleSetInput:
    out: CreateMatchmakingRuleSetInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RuleSetBody") is not None:
        out["rule_set_body"] = data["RuleSetBody"]
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

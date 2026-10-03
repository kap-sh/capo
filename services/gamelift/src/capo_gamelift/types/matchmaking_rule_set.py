"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingRuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_id_string_model
    import capo_gamelift.types.matchmaking_rule_set_arn
    import capo_gamelift.types.rule_set_body
    import capo_gamelift.types.timestamp


class MatchmakingRuleSet(TypedDict, closed=True):
    rule_set_name: NotRequired[
        "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for the matchmaking rule set</p>"""
    rule_set_arn: NotRequired[
        "capo_gamelift.types.matchmaking_rule_set_arn.MatchmakingRuleSetArn"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers matchmaking rule set resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::matchmakingruleset/<ruleset name></code>. In a GameLift rule set ARN, the resource ID matches the <i>RuleSetName</i> value.</p>"""
    rule_set_body: NotRequired["capo_gamelift.types.rule_set_body.RuleSetBody"]
    """<p>A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingRuleSet) -> dict:
    out: dict = {}
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "rule_set_arn" in value:
        out["RuleSetArn"] = value["rule_set_arn"]
    if "rule_set_body" in value:
        out["RuleSetBody"] = value["rule_set_body"]
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MatchmakingRuleSet:
    out: MatchmakingRuleSet = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    if data.get("RuleSetArn") is not None:
        out["rule_set_arn"] = data["RuleSetArn"]
    if data.get("RuleSetBody") is not None:
        out["rule_set_body"] = data["RuleSetBody"]
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out

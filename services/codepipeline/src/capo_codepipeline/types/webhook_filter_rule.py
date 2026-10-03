"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookFilterRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.json_path
    import capo_codepipeline.types.match_equals


class WebhookFilterRule(TypedDict, closed=True):
    json_path: "capo_codepipeline.types.json_path.JsonPath"
    """<p>A JsonPath expression that is applied to the body/payload of the webhook. The value selected by the JsonPath expression must match the value specified in the <code>MatchEquals</code> field. Otherwise, the request is ignored. For more information, see <a href="https://github.com/json-path/JsonPath">Java JsonPath implementation</a> in GitHub.</p>"""
    match_equals: NotRequired["capo_codepipeline.types.match_equals.MatchEquals"]
    """<p>The value selected by the <code>JsonPath</code> expression must match what is supplied in the <code>MatchEquals</code> field. Otherwise, the request is ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly brackets. For example, if the value supplied here is "refs/heads/{Branch}" and the target action has an action configuration property called "Branch" with a value of "main", the <code>MatchEquals</code> value is evaluated as "refs/heads/main". For a list of action configuration properties for built-in action types, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements">Pipeline Structure Reference Action Requirements</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookFilterRule) -> dict:
    out: dict = {}
    out["jsonPath"] = value["json_path"]
    if "match_equals" in value:
        out["matchEquals"] = value["match_equals"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebhookFilterRule:
    out: WebhookFilterRule = {}  # type: ignore[typeddict-item]
    if data.get("jsonPath") is not None:
        out["json_path"] = data["jsonPath"]
    else:
        raise DeserializationError("WebhookFilterRule.json_path required")
    if data.get("matchEquals") is not None:
        out["match_equals"] = data["matchEquals"]
    return out

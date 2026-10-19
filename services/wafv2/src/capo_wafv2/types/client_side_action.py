"""Generated from Smithy shape ``com.amazonaws.wafv2#ClientSideAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.regular_expression_list
    import capo_wafv2.types.sensitivity_to_act
    import capo_wafv2.types.usage_of_action


class ClientSideAction(TypedDict, closed=True):
    usage_of_action: "capo_wafv2.types.usage_of_action.UsageOfAction"
    """<p>Determines whether to use the <code>AWSManagedRulesAntiDDoSRuleSet</code> rules <code>ChallengeAllDuringEvent</code> and <code>ChallengeDDoSRequests</code> in the rule group evaluation and the related label <code>awswaf:managed:aws:anti-ddos:challengeable-request</code>. </p> <ul> <li> <p>If usage is enabled: </p> <ul> <li> <p>The managed rule group adds the label <code>awswaf:managed:aws:anti-ddos:challengeable-request</code> to any web request whose URL does <i>NOT</i> match the regular expressions provided in the <code>ClientSideAction</code> setting <code>ExemptUriRegularExpressions</code>. </p> </li> <li> <p>The two rules are evaluated against web requests for protected resources that are experiencing a DDoS attack. The two rules only apply their action to matching requests that have the label <code>awswaf:managed:aws:anti-ddos:challengeable-request</code>. </p> </li> </ul> </li> <li> <p>If usage is disabled: </p> <ul> <li> <p>The managed rule group doesn't add the label <code>awswaf:managed:aws:anti-ddos:challengeable-request</code> to any web requests. </p> </li> <li> <p>The two rules are not evaluated.</p> </li> <li> <p>None of the other <code>ClientSideAction</code> settings have any effect.</p> </li> </ul> </li> </ul> <note> <p>This setting only enables or disables the use of the two anti-DDOS rules <code>ChallengeAllDuringEvent</code> and <code>ChallengeDDoSRequests</code> in the anti-DDoS managed rule group. </p> <p>This setting doesn't alter the action setting in the two rules. To override the actions used by the rules <code>ChallengeAllDuringEvent</code> and <code>ChallengeDDoSRequests</code>, enable this setting, and then override the rule actions in the usual way, in your managed rule group configuration. </p> </note>"""
    sensitivity: NotRequired["capo_wafv2.types.sensitivity_to_act.SensitivityToAct"]
    """<p>The sensitivity that the rule group rule <code>ChallengeDDoSRequests</code> uses when matching against the DDoS suspicion labeling on a request. The managed rule group adds the labeling during DDoS events, before the <code>ChallengeDDoSRequests</code> rule runs. </p> <p>The higher the sensitivity, the more levels of labeling that the rule matches: </p> <ul> <li> <p>Low sensitivity is less sensitive, causing the rule to match only on the most likely participants in an attack, which are the requests with the high suspicion label <code>awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request</code>.</p> </li> <li> <p>Medium sensitivity causes the rule to match on the medium and high suspicion labels.</p> </li> <li> <p>High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.</p> </li> </ul> <p>Default: <code>HIGH</code> </p>"""
    exempt_uri_regular_expressions: NotRequired[
        "capo_wafv2.types.regular_expression_list.RegularExpressionList"
    ]
    r"""<p>The regular expression to match against the web request URI, used to identify requests that can't handle a silent browser challenge. When the <code>ClientSideAction</code> setting <code>UsageOfAction</code> is enabled, the managed rule group uses this setting to determine which requests to label with <code>awswaf:managed:aws:anti-ddos:challengeable-request</code>. If <code>UsageOfAction</code> is disabled, this setting has no effect and the managed rule group doesn't add the label to any requests.</p> <p>The anti-DDoS managed rule group doesn't evaluate the rules <code>ChallengeDDoSRequests</code> or <code>ChallengeAllDuringEvent</code> for web requests whose URIs match this regex. This is true regardless of whether you override the rule action for either of the rules in your web ACL configuration. </p> <p>Amazon Web Services recommends using a regular expression. </p> <p>This setting is required if <code>UsageOfAction</code> is set to <code>ENABLED</code>. If required, you can provide between 1 and 5 regex objects in the array of settings. </p> <p>Amazon Web Services recommends starting with the following setting. Review and update it for your application's needs:</p> <p> <code>\/api\/|\.(acc|avi|css|gif|jpe?g|js|mp[34]|ogg|otf|pdf|png|tiff?|ttf|webm|webp|woff2?)$</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientSideAction) -> dict:
    out: dict = {}
    import capo_wafv2.types.usage_of_action

    out["UsageOfAction"] = capo_wafv2.types.usage_of_action.serialize_aws_json_1_1(
        value["usage_of_action"]
    )
    if "sensitivity" in value:
        import capo_wafv2.types.sensitivity_to_act

        out["Sensitivity"] = capo_wafv2.types.sensitivity_to_act.serialize_aws_json_1_1(
            value["sensitivity"]
        )
    if "exempt_uri_regular_expressions" in value:
        import capo_wafv2.types.regular_expression_list

        out["ExemptUriRegularExpressions"] = (
            capo_wafv2.types.regular_expression_list.serialize_aws_json_1_1(
                value["exempt_uri_regular_expressions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientSideAction:
    out: ClientSideAction = {}  # type: ignore[typeddict-item]
    if data.get("UsageOfAction") is not None:
        import capo_wafv2.types.usage_of_action

        out["usage_of_action"] = (
            capo_wafv2.types.usage_of_action.deserialize_aws_json_1_1(
                data["UsageOfAction"]
            )
        )
    else:
        import typing

        out["usage_of_action"] = typing.cast(
            "capo_wafv2.types.usage_of_action.UsageOfAction", ""
        )
    if data.get("Sensitivity") is not None:
        import capo_wafv2.types.sensitivity_to_act

        out["sensitivity"] = (
            capo_wafv2.types.sensitivity_to_act.deserialize_aws_json_1_1(
                data["Sensitivity"]
            )
        )
    if data.get("ExemptUriRegularExpressions") is not None:
        import capo_wafv2.types.regular_expression_list

        out["exempt_uri_regular_expressions"] = (
            capo_wafv2.types.regular_expression_list.deserialize_aws_json_1_1(
                data["ExemptUriRegularExpressions"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.wafv2#AWSManagedRulesATPRuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.boolean
    import capo_wafv2.types.request_inspection
    import capo_wafv2.types.response_inspection
    import capo_wafv2.types.string


class AWSManagedRulesATPRuleSet(TypedDict, closed=True):
    login_path: "capo_wafv2.types.string.String"
    """<p>The path of the login endpoint for your application. For example, for the URL <code>https://example.com/web/login</code>, you would provide the path <code>/web/login</code>. Login paths that start with the path that you provide are considered a match. For example <code>/web/login</code> matches the login paths <code>/web/login</code>, <code>/web/login/</code>, <code>/web/loginPage</code>, and <code>/web/login/thisPage</code>, but doesn't match the login path <code>/home/web/login</code> or <code>/website/login</code>.</p> <p>The rule group inspects only HTTP <code>POST</code> requests to your specified login endpoint.</p>"""
    request_inspection: NotRequired[
        "capo_wafv2.types.request_inspection.RequestInspection"
    ]
    """<p>The criteria for inspecting login requests, used by the ATP rule group to validate credentials usage. </p>"""
    response_inspection: NotRequired[
        "capo_wafv2.types.response_inspection.ResponseInspection"
    ]
    """<p>The criteria for inspecting responses to login requests, used by the ATP rule group to track login failure rates. </p> <note> <p>Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.</p> </note> <p>The ATP rule group evaluates the responses that your protected resources send back to client login attempts, keeping count of successful and failed attempts for each IP address and client session. Using this information, the rule group labels and mitigates requests from client sessions and IP addresses that have had too many failed login attempts in a short amount of time. </p>"""
    enable_regex_in_path: "capo_wafv2.types.boolean.Boolean"
    """<p>Allow the use of regular expressions in the login page path. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSManagedRulesATPRuleSet) -> dict:
    out: dict = {}
    out["LoginPath"] = value["login_path"]
    if "request_inspection" in value:
        import capo_wafv2.types.request_inspection

        out["RequestInspection"] = (
            capo_wafv2.types.request_inspection.serialize_aws_json_1_1(
                value["request_inspection"]
            )
        )
    if "response_inspection" in value:
        import capo_wafv2.types.response_inspection

        out["ResponseInspection"] = (
            capo_wafv2.types.response_inspection.serialize_aws_json_1_1(
                value["response_inspection"]
            )
        )
    out["EnableRegexInPath"] = value.get("enable_regex_in_path", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AWSManagedRulesATPRuleSet:
    out: AWSManagedRulesATPRuleSet = {}  # type: ignore[typeddict-item]
    if data.get("LoginPath") is not None:
        out["login_path"] = data["LoginPath"]
    else:
        out["login_path"] = ""
    if data.get("RequestInspection") is not None:
        import capo_wafv2.types.request_inspection

        out["request_inspection"] = (
            capo_wafv2.types.request_inspection.deserialize_aws_json_1_1(
                data["RequestInspection"]
            )
        )
    if data.get("ResponseInspection") is not None:
        import capo_wafv2.types.response_inspection

        out["response_inspection"] = (
            capo_wafv2.types.response_inspection.deserialize_aws_json_1_1(
                data["ResponseInspection"]
            )
        )
    if data.get("EnableRegexInPath") is not None:
        out["enable_regex_in_path"] = data["EnableRegexInPath"]
    else:
        out["enable_regex_in_path"] = False
    return out

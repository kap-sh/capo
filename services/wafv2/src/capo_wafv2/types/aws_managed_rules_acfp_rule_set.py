"""Generated from Smithy shape ``com.amazonaws.wafv2#AWSManagedRulesACFPRuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.boolean
    import capo_wafv2.types.creation_path_string
    import capo_wafv2.types.registration_page_path_string
    import capo_wafv2.types.request_inspection_acfp
    import capo_wafv2.types.response_inspection


class AWSManagedRulesACFPRuleSet(TypedDict, closed=True):
    creation_path: "capo_wafv2.types.creation_path_string.CreationPathString"
    """<p>The path of the account creation endpoint for your application. This is the page on your website that accepts the completed registration form for a new user. This page must accept <code>POST</code> requests.</p> <p>For example, for the URL <code>https://example.com/web/newaccount</code>, you would provide the path <code>/web/newaccount</code>. Account creation page paths that start with the path that you provide are considered a match. For example <code>/web/newaccount</code> matches the account creation paths <code>/web/newaccount</code>, <code>/web/newaccount/</code>, <code>/web/newaccountPage</code>, and <code>/web/newaccount/thisPage</code>, but doesn't match the path <code>/home/web/newaccount</code> or <code>/website/newaccount</code>. </p>"""
    registration_page_path: (
        "capo_wafv2.types.registration_page_path_string.RegistrationPagePathString"
    )
    """<p>The path of the account registration endpoint for your application. This is the page on your website that presents the registration form to new users. </p> <note> <p>This page must accept <code>GET</code> text/html requests.</p> </note> <p>For example, for the URL <code>https://example.com/web/registration</code>, you would provide the path <code>/web/registration</code>. Registration page paths that start with the path that you provide are considered a match. For example <code>/web/registration</code> matches the registration paths <code>/web/registration</code>, <code>/web/registration/</code>, <code>/web/registrationPage</code>, and <code>/web/registration/thisPage</code>, but doesn't match the path <code>/home/web/registration</code> or <code>/website/registration</code>. </p>"""
    request_inspection: "capo_wafv2.types.request_inspection_acfp.RequestInspectionACFP"
    """<p>The criteria for inspecting account creation requests, used by the ACFP rule group to validate and track account creation attempts. </p>"""
    response_inspection: NotRequired[
        "capo_wafv2.types.response_inspection.ResponseInspection"
    ]
    """<p>The criteria for inspecting responses to account creation requests, used by the ACFP rule group to track account creation success rates. </p> <note> <p>Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.</p> </note> <p>The ACFP rule group evaluates the responses that your protected resources send back to client account creation attempts, keeping count of successful and failed attempts from each IP address and client session. Using this information, the rule group labels and mitigates requests from client sessions and IP addresses that have had too many successful account creation attempts in a short amount of time. </p>"""
    enable_regex_in_path: "capo_wafv2.types.boolean.Boolean"
    """<p>Allow the use of regular expressions in the registration page path and the account creation path. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSManagedRulesACFPRuleSet) -> dict:
    out: dict = {}
    out["CreationPath"] = value["creation_path"]
    out["RegistrationPagePath"] = value["registration_page_path"]
    import capo_wafv2.types.request_inspection_acfp

    out["RequestInspection"] = (
        capo_wafv2.types.request_inspection_acfp.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> AWSManagedRulesACFPRuleSet:
    out: AWSManagedRulesACFPRuleSet = {}  # type: ignore[typeddict-item]
    if data.get("CreationPath") is not None:
        out["creation_path"] = data["CreationPath"]
    else:
        out["creation_path"] = ""
    if data.get("RegistrationPagePath") is not None:
        out["registration_page_path"] = data["RegistrationPagePath"]
    else:
        out["registration_page_path"] = ""
    if data.get("RequestInspection") is not None:
        import capo_wafv2.types.request_inspection_acfp

        out["request_inspection"] = (
            capo_wafv2.types.request_inspection_acfp.deserialize_aws_json_1_1(
                data["RequestInspection"]
            )
        )
    else:
        raise DeserializationError(
            "AWSManagedRulesACFPRuleSet.request_inspection required"
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

"""Generated from Smithy shape ``com.amazonaws.auditmanager#SourceKeyword``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.keyword_input_type
    import capo_auditmanager.types.keyword_value


class SourceKeyword(TypedDict, closed=True):
    keyword_input_type: NotRequired[
        "capo_auditmanager.types.keyword_input_type.KeywordInputType"
    ]
    """<p> The input method for the keyword. </p> <ul> <li> <p> <code>SELECT_FROM_LIST</code> is used when mapping a data source for automated evidence.</p> <ul> <li> <p>When <code>keywordInputType</code> is <code>SELECT_FROM_LIST</code>, a keyword must be selected to collect automated evidence. For example, this keyword can be a CloudTrail event name, a rule name for Config, a Security Hub CSPM control, or the name of an Amazon Web Services API call.</p> </li> </ul> </li> <li> <p> <code>UPLOAD_FILE</code> and <code>INPUT_TEXT</code> are only used when mapping a data source for manual evidence.</p> <ul> <li> <p>When <code>keywordInputType</code> is <code>UPLOAD_FILE</code>, a file must be uploaded as manual evidence.</p> </li> <li> <p>When <code>keywordInputType</code> is <code>INPUT_TEXT</code>, text must be entered as manual evidence.</p> </li> </ul> </li> </ul>"""
    keyword_value: NotRequired["capo_auditmanager.types.keyword_value.KeywordValue"]
    """<p> The value of the keyword that's used when mapping a control data source. For example, this can be a CloudTrail event name, a rule name for Config, a Security Hub CSPM control, or the name of an Amazon Web Services API call. </p> <p>If you’re mapping a data source to a rule in Config, the <code>keywordValue</code> that you specify depends on the type of rule:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">managed rules</a>, you can use the rule identifier as the <code>keywordValue</code>. You can find the rule identifier from the <a href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">list of Config managed rules</a>. For some rules, the rule identifier is different from the rule name. For example, the rule name <code>restricted-ssh</code> has the following rule identifier: <code>INCOMING_SSH_DISABLED</code>. Make sure to use the rule identifier, not the rule name. </p> <p>Keyword example for managed rules:</p> <ul> <li> <p>Managed rule name: <a href="https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-acl-prohibited.html">s3-bucket-acl-prohibited</a> </p> <p> <code>keywordValue</code>: <code>S3_BUCKET_ACL_PROHIBITED</code> </p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html">custom rules</a>, you form the <code>keywordValue</code> by adding the <code>Custom_</code> prefix to the rule name. This prefix distinguishes the custom rule from a managed rule. </p> <p>Keyword example for custom rules:</p> <ul> <li> <p>Custom rule name: my-custom-config-rule</p> <p> <code>keywordValue</code>: <code>Custom_my-custom-config-rule</code> </p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/developerguide/service-linked-awsconfig-rules.html">service-linked rules</a>, you form the <code>keywordValue</code> by adding the <code>Custom_</code> prefix to the rule name. In addition, you remove the suffix ID that appears at the end of the rule name. </p> <p>Keyword examples for service-linked rules:</p> <ul> <li> <p>Service-linked rule name: CustomRuleForAccount-conformance-pack-szsm1uv0w</p> <p> <code>keywordValue</code>: <code>Custom_CustomRuleForAccount-conformance-pack</code> </p> </li> <li> <p>Service-linked rule name: OrgConfigRule-s3-bucket-versioning-enabled-dbgzf8ba</p> <p> <code>keywordValue</code>: <code>Custom_OrgConfigRule-s3-bucket-versioning-enabled</code> </p> </li> </ul> </li> </ul> <important> <p>The <code>keywordValue</code> is case sensitive. If you enter a value incorrectly, Audit Manager might not recognize the data source mapping. As a result, you might not successfully collect evidence from that data source as intended. </p> <p>Keep in mind the following requirements, depending on the data source type that you're using. </p> <ol> <li> <p>For Config: </p> <ul> <li> <p>For managed rules, make sure that the <code>keywordValue</code> is the rule identifier in <code>ALL_CAPS_WITH_UNDERSCORES</code>. For example, <code>CLOUDWATCH_LOG_GROUP_ENCRYPTED</code>. For accuracy, we recommend that you reference the list of <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html">supported Config managed rules</a>.</p> </li> <li> <p>For custom rules, make sure that the <code>keywordValue</code> has the <code>Custom_</code> prefix followed by the custom rule name. The format of the custom rule name itself may vary. For accuracy, we recommend that you visit the <a href="https://console.aws.amazon.com/config/">Config console</a> to verify your custom rule name.</p> </li> </ul> </li> <li> <p>For Security Hub CSPM: The format varies for Security Hub CSPM control names. For accuracy, we recommend that you reference the list of <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-ash.html">supported Security Hub CSPM controls</a>.</p> </li> <li> <p>For Amazon Web Services API calls: Make sure that the <code>keywordValue</code> is written as <code>serviceprefix_ActionName</code>. For example, <code>iam_ListGroups</code>. For accuracy, we recommend that you reference the list of <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-api.html">supported API calls</a>.</p> </li> <li> <p>For CloudTrail: Make sure that the <code>keywordValue</code> is written as <code>serviceprefix_ActionName</code>. For example, <code>cloudtrail_StartLogging</code>. For accuracy, we recommend that you review the Amazon Web Services service prefix and action names in the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Service Authorization Reference</a>.</p> </li> </ol> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceKeyword) -> dict:
    out: dict = {}
    if "keyword_input_type" in value:
        import capo_auditmanager.types.keyword_input_type

        out["keywordInputType"] = (
            capo_auditmanager.types.keyword_input_type.serialize_json(
                value["keyword_input_type"]
            )
        )
    if "keyword_value" in value:
        out["keywordValue"] = value["keyword_value"]
    return out


def deserialize_json(data: dict) -> SourceKeyword:
    out: SourceKeyword = {}  # type: ignore[typeddict-item]
    if data.get("keywordInputType") is not None:
        import capo_auditmanager.types.keyword_input_type

        out["keyword_input_type"] = (
            capo_auditmanager.types.keyword_input_type.deserialize_json(
                data["keywordInputType"]
            )
        )
    if data.get("keywordValue") is not None:
        out["keyword_value"] = data["keywordValue"]
    return out

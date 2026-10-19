"""Generated from Smithy shape ``com.amazonaws.support#DescribeSupportedLanguagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.nullable_boolean_type
    import capo_support.types.validated_category_code
    import capo_support.types.validated_issue_type_string
    import capo_support.types.validated_service_code


class DescribeSupportedLanguagesRequest(TypedDict, closed=True):
    issue_type: (
        "capo_support.types.validated_issue_type_string.ValidatedIssueTypeString"
    )
    """<p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>.</p>"""
    service_code: "capo_support.types.validated_service_code.ValidatedServiceCode"
    """<p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>"""
    category_code: "capo_support.types.validated_category_code.ValidatedCategoryCode"
    """<p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually returning supported languages. When set to <code>true</code>, the request is validated but no languages are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSupportedLanguagesRequest) -> dict:
    out: dict = {}
    out["issueType"] = value["issue_type"]
    out["serviceCode"] = value["service_code"]
    out["categoryCode"] = value["category_code"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSupportedLanguagesRequest:
    out: DescribeSupportedLanguagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("issueType") is not None:
        out["issue_type"] = data["issueType"]
    else:
        out["issue_type"] = ""
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        out["service_code"] = ""
    if data.get("categoryCode") is not None:
        out["category_code"] = data["categoryCode"]
    else:
        out["category_code"] = ""
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out

"""Generated from Smithy shape ``com.amazonaws.support#DescribeCreateCaseOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.category_code
    import capo_support.types.issue_type
    import capo_support.types.language
    import capo_support.types.nullable_boolean_type
    import capo_support.types.service_code2


class DescribeCreateCaseOptionsRequest(TypedDict, closed=True):
    issue_type: "capo_support.types.issue_type.IssueType"
    """<p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>"""
    service_code: "capo_support.types.service_code2.ServiceCode2"
    """<p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>"""
    language: "capo_support.types.language.Language"
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""
    category_code: "capo_support.types.category_code.CategoryCode"
    """<p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually returning case option data. When set to <code>true</code>, the request is validated but no options are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCreateCaseOptionsRequest) -> dict:
    out: dict = {}
    out["issueType"] = value["issue_type"]
    out["serviceCode"] = value["service_code"]
    out["language"] = value["language"]
    out["categoryCode"] = value["category_code"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCreateCaseOptionsRequest:
    out: DescribeCreateCaseOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("issueType") is not None:
        out["issue_type"] = data["issueType"]
    else:
        raise DeserializationError(
            "DescribeCreateCaseOptionsRequest.issue_type required"
        )
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "DescribeCreateCaseOptionsRequest.service_code required"
        )
    if data.get("language") is not None:
        out["language"] = data["language"]
    else:
        raise DeserializationError("DescribeCreateCaseOptionsRequest.language required")
    if data.get("categoryCode") is not None:
        out["category_code"] = data["categoryCode"]
    else:
        raise DeserializationError(
            "DescribeCreateCaseOptionsRequest.category_code required"
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out

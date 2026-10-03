"""Generated from Smithy shape ``com.amazonaws.support#DescribeCasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.after_time
    import capo_support.types.before_time
    import capo_support.types.case_id_list
    import capo_support.types.display_id
    import capo_support.types.include_communications
    import capo_support.types.include_resolved_cases
    import capo_support.types.language
    import capo_support.types.max_results
    import capo_support.types.next_token
    import capo_support.types.nullable_boolean_type


class DescribeCasesRequest(TypedDict, closed=True):
    case_id_list: NotRequired["capo_support.types.case_id_list.CaseIdList"]
    """<p>A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.</p>"""
    display_id: NotRequired["capo_support.types.display_id.DisplayId"]
    """<p>The ID displayed for a case in the Amazon Web Services Support Center user interface.</p>"""
    after_time: NotRequired["capo_support.types.after_time.AfterTime"]
    """<p>The start date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>"""
    before_time: NotRequired["capo_support.types.before_time.BeforeTime"]
    """<p>The end date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>"""
    include_resolved_cases: (
        "capo_support.types.include_resolved_cases.IncludeResolvedCases"
    )
    """<p>Specifies whether to include resolved support cases in the <code>DescribeCases</code> response. By default, resolved cases aren't included.</p>"""
    next_token: NotRequired["capo_support.types.next_token.NextToken"]
    """<p>A resumption point for pagination.</p>"""
    max_results: NotRequired["capo_support.types.max_results.MaxResults"]
    """<p>The maximum number of results to return before paginating.</p>"""
    language: NotRequired["capo_support.types.language.Language"]
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""
    include_communications: NotRequired[
        "capo_support.types.include_communications.IncludeCommunications"
    ]
    """<p>Specifies whether to include communications in the <code>DescribeCases</code> response. By default, communications are included.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually returning case data. When set to <code>true</code>, the request is validated but no cases are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCasesRequest) -> dict:
    out: dict = {}
    if "case_id_list" in value:
        import capo_support.types.case_id_list

        out["caseIdList"] = capo_support.types.case_id_list.serialize_aws_json_1_1(
            value["case_id_list"]
        )
    if "display_id" in value:
        out["displayId"] = value["display_id"]
    if "after_time" in value:
        out["afterTime"] = value["after_time"]
    if "before_time" in value:
        out["beforeTime"] = value["before_time"]
    out["includeResolvedCases"] = value.get("include_resolved_cases", False)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "language" in value:
        out["language"] = value["language"]
    if "include_communications" in value:
        out["includeCommunications"] = value["include_communications"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCasesRequest:
    out: DescribeCasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("caseIdList") is not None:
        import capo_support.types.case_id_list

        out["case_id_list"] = capo_support.types.case_id_list.deserialize_aws_json_1_1(
            data["caseIdList"]
        )
    if data.get("displayId") is not None:
        out["display_id"] = data["displayId"]
    if data.get("afterTime") is not None:
        out["after_time"] = data["afterTime"]
    if data.get("beforeTime") is not None:
        out["before_time"] = data["beforeTime"]
    if data.get("includeResolvedCases") is not None:
        out["include_resolved_cases"] = data["includeResolvedCases"]
    else:
        out["include_resolved_cases"] = False
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("includeCommunications") is not None:
        out["include_communications"] = data["includeCommunications"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out

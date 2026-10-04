"""Generated from Smithy shape ``com.amazonaws.securityhub#GetRemediationsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.guidance_format
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.remediation_filters
    import capo_securityhub.types.remediation_string_uid


class GetRemediationsV2Request(TypedDict, closed=True):
    target_uid: NotRequired[
        "capo_securityhub.types.remediation_string_uid.RemediationStringUid"
    ]
    """<p>The unique identifier (ID) of an existing remediation target to return. Returns the single matching target. You can't use <code>TargetUid</code> together with <code>MetadataUid</code> or <code>Filters</code>.</p>"""
    metadata_uid: NotRequired[
        "capo_securityhub.types.remediation_string_uid.RemediationStringUid"
    ]
    """<p>The unique identifier (ID) of the Security Hub exposure finding, found under the <code>metadata.uid</code> field of the finding. Returns the remediation targets associated with that finding. You can't use <code>MetadataUid</code> together with <code>TargetUid</code> or <code>Filters</code>.</p>"""
    filters: NotRequired[
        "capo_securityhub.types.remediation_filters.RemediationFilters"
    ]
    """<p>Filters remediation targets based on a set of criteria. You can't use <code>Filters</code> together with <code>TargetUid</code> or <code>MetadataUid</code>.</p>"""
    show_guidance: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether to show remediation target guidance.</p>"""
    guidance_format: NotRequired[
        "capo_securityhub.types.guidance_format.GuidanceFormat"
    ]
    """<p>The format of the remediation guidance examples to return. Valid values are <code>All</code>, <code>AwsCli</code>, <code>Cli</code>, <code>Python</code>, <code>Terraform</code>, <code>Cdk</code>, <code>CloudFormation</code>, <code>IaC</code>, and <code>Template</code>. If you don't specify a value, all formats are returned. Applies only when <code>ShowGuidance</code> is <code>true</code>.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Valid range is 1-100. If you don't specify a value, the operation returns up to 25 results.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token used to paginate the remediations target list returned. On your first call to <code>GetRemediationsV2</code>, omit this parameter or set it to <code>NULL</code>. For subsequent calls, use the <code>NextToken</code> value returned in the previous response to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRemediationsV2Request) -> dict:
    out: dict = {}
    if "target_uid" in value:
        out["TargetUid"] = value["target_uid"]
    if "metadata_uid" in value:
        out["MetadataUid"] = value["metadata_uid"]
    if "filters" in value:
        import capo_securityhub.types.remediation_filters

        out["Filters"] = capo_securityhub.types.remediation_filters.serialize_json(
            value["filters"]
        )
    if "show_guidance" in value:
        out["ShowGuidance"] = value["show_guidance"]
    if "guidance_format" in value:
        import capo_securityhub.types.guidance_format

        out["GuidanceFormat"] = capo_securityhub.types.guidance_format.serialize_json(
            value["guidance_format"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetRemediationsV2Request:
    out: GetRemediationsV2Request = {}  # type: ignore[typeddict-item]
    if data.get("TargetUid") is not None:
        out["target_uid"] = data["TargetUid"]
    if data.get("MetadataUid") is not None:
        out["metadata_uid"] = data["MetadataUid"]
    if data.get("Filters") is not None:
        import capo_securityhub.types.remediation_filters

        out["filters"] = capo_securityhub.types.remediation_filters.deserialize_json(
            data["Filters"]
        )
    if data.get("ShowGuidance") is not None:
        out["show_guidance"] = data["ShowGuidance"]
    if data.get("GuidanceFormat") is not None:
        import capo_securityhub.types.guidance_format

        out["guidance_format"] = (
            capo_securityhub.types.guidance_format.deserialize_json(
                data["GuidanceFormat"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

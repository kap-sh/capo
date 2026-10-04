"""Generated from Smithy shape ``com.amazonaws.securityhub#ListExposuresByRemediationV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.remediation_string_uid


class ListExposuresByRemediationV2Request(TypedDict, closed=True):
    target_uid: NotRequired[
        "capo_securityhub.types.remediation_string_uid.RemediationStringUid"
    ]
    """<p>The unique identifier (ID) of an existing remediation target to list exposure findings for.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Valid range is 1-100. If you don't specify a value, the operation returns up to 25 results.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token used to paginate the exposures list returned. On your first call to <code>ListExposuresByRemediationV2</code>, omit this parameter or set it to <code>NULL</code>. For subsequent calls, use the <code>NextToken</code> value returned in the previous response to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExposuresByRemediationV2Request) -> dict:
    out: dict = {}
    if "target_uid" in value:
        out["TargetUid"] = value["target_uid"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExposuresByRemediationV2Request:
    out: ListExposuresByRemediationV2Request = {}  # type: ignore[typeddict-item]
    if data.get("TargetUid") is not None:
        out["target_uid"] = data["TargetUid"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

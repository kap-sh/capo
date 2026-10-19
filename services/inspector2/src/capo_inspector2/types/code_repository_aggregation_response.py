"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeRepositoryAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.severity_counts


class CodeRepositoryAggregationResponse(TypedDict, closed=True):
    project_names: "str"
    """<p>The names of the projects associated with the code repository.</p>"""
    provider_type: NotRequired["str"]
    """<p>The type of repository provider for the code repository.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    exploit_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings that have an exploit available for the code repository.</p>"""
    fix_available_active_findings_count: NotRequired["int"]
    """<p>The number of active findings that have a fix available for the code repository.</p>"""
    account_id: NotRequired["str"]
    """<p>The Amazon Web Services account ID associated with the code repository.</p>"""
    resource_id: NotRequired["str"]
    """<p>The resource ID of the code repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRepositoryAggregationResponse) -> dict:
    out: dict = {}
    out["projectNames"] = value["project_names"]
    if "provider_type" in value:
        out["providerType"] = value["provider_type"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "exploit_available_active_findings_count" in value:
        out["exploitAvailableActiveFindingsCount"] = value[
            "exploit_available_active_findings_count"
        ]
    if "fix_available_active_findings_count" in value:
        out["fixAvailableActiveFindingsCount"] = value[
            "fix_available_active_findings_count"
        ]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> CodeRepositoryAggregationResponse:
    out: CodeRepositoryAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("projectNames") is not None:
        out["project_names"] = data["projectNames"]
    else:
        out["project_names"] = ""
    if data.get("providerType") is not None:
        out["provider_type"] = data["providerType"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("exploitAvailableActiveFindingsCount") is not None:
        out["exploit_available_active_findings_count"] = data[
            "exploitAvailableActiveFindingsCount"
        ]
    if data.get("fixAvailableActiveFindingsCount") is not None:
        out["fix_available_active_findings_count"] = data[
            "fixAvailableActiveFindingsCount"
        ]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    return out

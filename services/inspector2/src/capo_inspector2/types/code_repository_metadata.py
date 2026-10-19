"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeRepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_repository_integration_arn
    import capo_inspector2.types.code_repository_on_demand_scan
    import capo_inspector2.types.commit_id
    import capo_inspector2.types.project_code_security_scan_configuration


class CodeRepositoryMetadata(TypedDict, closed=True):
    project_name: "str"
    """<p>The name of the project in the code repository.</p>"""
    integration_arn: NotRequired[
        "capo_inspector2.types.code_repository_integration_arn.CodeRepositoryIntegrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the code security integration associated with the repository.</p>"""
    provider_type: "str"
    """<p>The type of repository provider (such as GitHub, GitLab, etc.).</p>"""
    provider_type_visibility: "str"
    """<p>The visibility setting of the repository (public or private).</p>"""
    last_scanned_commit_id: NotRequired["capo_inspector2.types.commit_id.CommitId"]
    """<p>The ID of the last commit that was scanned in the repository.</p>"""
    scan_configuration: NotRequired[
        "capo_inspector2.types.project_code_security_scan_configuration.ProjectCodeSecurityScanConfiguration"
    ]
    """<p>The scan configuration settings applied to the code repository.</p>"""
    on_demand_scan: NotRequired[
        "capo_inspector2.types.code_repository_on_demand_scan.CodeRepositoryOnDemandScan"
    ]
    """<p>Information about on-demand scans performed on the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRepositoryMetadata) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "integration_arn" in value:
        out["integrationArn"] = value["integration_arn"]
    out["providerType"] = value["provider_type"]
    out["providerTypeVisibility"] = value["provider_type_visibility"]
    if "last_scanned_commit_id" in value:
        out["lastScannedCommitId"] = value["last_scanned_commit_id"]
    if "scan_configuration" in value:
        import capo_inspector2.types.project_code_security_scan_configuration

        out["scanConfiguration"] = (
            capo_inspector2.types.project_code_security_scan_configuration.serialize_json(
                value["scan_configuration"]
            )
        )
    if "on_demand_scan" in value:
        import capo_inspector2.types.code_repository_on_demand_scan

        out["onDemandScan"] = (
            capo_inspector2.types.code_repository_on_demand_scan.serialize_json(
                value["on_demand_scan"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeRepositoryMetadata:
    out: CodeRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    if data.get("providerType") is not None:
        out["provider_type"] = data["providerType"]
    else:
        out["provider_type"] = ""
    if data.get("providerTypeVisibility") is not None:
        out["provider_type_visibility"] = data["providerTypeVisibility"]
    else:
        out["provider_type_visibility"] = ""
    if data.get("lastScannedCommitId") is not None:
        out["last_scanned_commit_id"] = data["lastScannedCommitId"]
    if data.get("scanConfiguration") is not None:
        import capo_inspector2.types.project_code_security_scan_configuration

        out["scan_configuration"] = (
            capo_inspector2.types.project_code_security_scan_configuration.deserialize_json(
                data["scanConfiguration"]
            )
        )
    if data.get("onDemandScan") is not None:
        import capo_inspector2.types.code_repository_on_demand_scan

        out["on_demand_scan"] = (
            capo_inspector2.types.code_repository_on_demand_scan.deserialize_json(
                data["onDemandScan"]
            )
        )
    return out

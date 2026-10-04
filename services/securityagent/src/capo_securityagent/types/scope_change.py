"""Generated from Smithy shape ``com.amazonaws.securityagent#ScopeChange``."""

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError


class ScopeChange(TypedDict, closed=True):
    integration_id: "str"
    """<p>The identifier of the integration for the source-code provider that hosts the repository.</p>"""
    provider_resource_id: "str"
    """<p>The provider-specific identifier of the repository the change belongs to.</p>"""
    base_commit_sha: NotRequired["str"]
    """<p>The commit SHA that the change is compared against. When omitted, the change is evaluated against the head commit alone.</p>"""
    head_commit_sha: "str"
    """<p>The commit SHA at the tip of the change to be tested.</p>"""
    trigger_run_id: NotRequired["str"]
    """<p>The identifier of the CI/CD pipeline run that triggered this pentest job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeChange) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["providerResourceId"] = value["provider_resource_id"]
    if "base_commit_sha" in value:
        out["baseCommitSha"] = value["base_commit_sha"]
    out["headCommitSha"] = value["head_commit_sha"]
    if "trigger_run_id" in value:
        out["triggerRunId"] = value["trigger_run_id"]
    return out


def deserialize_json(data: dict) -> ScopeChange:
    out: ScopeChange = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError("ScopeChange.integration_id required")
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        raise DeserializationError("ScopeChange.provider_resource_id required")
    if data.get("baseCommitSha") is not None:
        out["base_commit_sha"] = data["baseCommitSha"]
    if data.get("headCommitSha") is not None:
        out["head_commit_sha"] = data["headCommitSha"]
    else:
        raise DeserializationError("ScopeChange.head_commit_sha required")
    if data.get("triggerRunId") is not None:
        out["trigger_run_id"] = data["triggerRunId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.continuum#CreateCodeFindingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.finding_client_token


class CreateCodeFindingInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The environment to ingest the finding into."""
    ocsf_document: "object"
    """The OCSF finding document to ingest, verbatim. Must declare a class_uid Continuum supports (2002 Vulnerability Finding, or 2007 Application Security Posture Finding) and validate against the vendored OCSF JSON Schema for that class, including the Continuum overlay requirements that finding_info.uid be present and that vulnerabilities[0].affected_code[0].file identify the code location. With several repositories in the environment, the file path must begin with the repository name. Maximum size 256 KB. Stored verbatim and normalized into the typed Finding members returned by GetCodeFinding. GetCodeFinding does not return the document itself."""
    client_token: NotRequired[
        "capo_continuum.types.finding_client_token.FindingClientToken"
    ]
    """Caller-provided idempotency token. A retry with the same token and an identical finding document replays the original result; the same token with different content is rejected."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeFindingInput) -> dict:
    out: dict = {}
    out["ocsfDocument"] = value["ocsf_document"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCodeFindingInput:
    out: CreateCodeFindingInput = {}  # type: ignore[typeddict-item]
    if data.get("ocsfDocument") is not None:
        out["ocsf_document"] = data["ocsfDocument"]
    else:
        out["ocsf_document"] = None
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

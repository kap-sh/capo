"""Generated from Smithy shape ``com.amazonaws.continuum#RemediationProposalBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_citation
    import capo_continuum.types.artifact_sha256
    import capo_continuum.types.issue_artifact_content
    import capo_continuum.types.patch_format


class RemediationProposalBody(TypedDict, closed=True):
    patch: "capo_continuum.types.issue_artifact_content.IssueArtifactContent"
    """The patch exactly as the remediation agent produced it, unmodified."""
    format: NotRequired["capo_continuum.types.patch_format.PatchFormat"]
    """The patch's wire format, which determines how to apply it. Absent when the producer recorded a format with no mapping yet."""
    filename: NotRequired["capo_continuum.types.artifact_citation.ArtifactCitation"]
    """Filename the producer suggests for the patch, when it named one."""
    patch_sha256: NotRequired["capo_continuum.types.artifact_sha256.ArtifactSha256"]
    """SHA-256 of the patch bytes in lowercase hex, as recorded by the producer. Lets a caller confirm the patch it applies is byte-for-byte the one that was reviewed. Computed over the patch bytes, so it is verifiable against `patch` without trusting this value."""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationProposalBody) -> dict:
    out: dict = {}
    out["patch"] = value["patch"]
    if "format" in value:
        import capo_continuum.types.patch_format

        out["format"] = capo_continuum.types.patch_format.serialize_json(
            value["format"]
        )
    if "filename" in value:
        out["filename"] = value["filename"]
    if "patch_sha256" in value:
        out["patchSha256"] = value["patch_sha256"]
    return out


def deserialize_json(data: dict) -> RemediationProposalBody:
    out: RemediationProposalBody = {}  # type: ignore[typeddict-item]
    if data.get("patch") is not None:
        out["patch"] = data["patch"]
    else:
        out["patch"] = ""
    if data.get("format") is not None:
        import capo_continuum.types.patch_format

        out["format"] = capo_continuum.types.patch_format.deserialize_json(
            data["format"]
        )
    if data.get("filename") is not None:
        out["filename"] = data["filename"]
    if data.get("patchSha256") is not None:
        out["patch_sha256"] = data["patchSha256"]
    return out

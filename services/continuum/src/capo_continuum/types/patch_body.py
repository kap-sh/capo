"""Generated from Smithy shape ``com.amazonaws.continuum#PatchBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_sha256
    import capo_continuum.types.build_repository_name
    import capo_continuum.types.issue_artifact_content
    import capo_continuum.types.patch_delivery
    import capo_continuum.types.patch_format


class PatchBody(TypedDict, closed=True):
    patch: "capo_continuum.types.issue_artifact_content.IssueArtifactContent"
    """The patch exactly as stored, unmodified. Control Plane accepted it only as a text unified diff, so `git apply` applies it."""
    format: NotRequired["capo_continuum.types.patch_format.PatchFormat"]
    """The patch's wire format, read from the patch itself, which determines how to apply it. Absent when the patch starts with neither a git mailbox header nor a `diff --git` header."""
    repository_name: NotRequired[
        "capo_continuum.types.build_repository_name.BuildRepositoryName"
    ]
    """The repository the patch applies to, as named in the source snapshot it was generated against."""
    patch_sha256: "capo_continuum.types.artifact_sha256.ArtifactSha256"
    """SHA-256 of the patch's UTF-8 bytes in lowercase hex, computed by Control Plane when it stored the patch. Lets a caller confirm the patch it applies is byte-for-byte the one that was reviewed. Computed over the patch bytes, so it is verifiable against `patch` without trusting this value."""
    size_bytes: "int"
    """Size of the patch in UTF-8 bytes, the unit the digest is computed over."""
    delivery: NotRequired["capo_continuum.types.patch_delivery.PatchDelivery"]
    """Delivery of the patch to the customer's bucket or repository. Absent when the artifact has no delivery destination."""


# --- restJson1 ser/de ---
def serialize_json(value: PatchBody) -> dict:
    out: dict = {}
    out["patch"] = value["patch"]
    if "format" in value:
        import capo_continuum.types.patch_format

        out["format"] = capo_continuum.types.patch_format.serialize_json(
            value["format"]
        )
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    out["patchSha256"] = value["patch_sha256"]
    out["sizeBytes"] = value["size_bytes"]
    if "delivery" in value:
        import capo_continuum.types.patch_delivery

        out["delivery"] = capo_continuum.types.patch_delivery.serialize_json(
            value["delivery"]
        )
    return out


def deserialize_json(data: dict) -> PatchBody:
    out: PatchBody = {}  # type: ignore[typeddict-item]
    if data.get("patch") is not None:
        out["patch"] = data["patch"]
    else:
        out["patch"] = ""
    if data.get("format") is not None:
        import capo_continuum.types.patch_format

        out["format"] = capo_continuum.types.patch_format.deserialize_json(
            data["format"]
        )
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("patchSha256") is not None:
        out["patch_sha256"] = data["patchSha256"]
    else:
        out["patch_sha256"] = ""
    if data.get("sizeBytes") is not None:
        out["size_bytes"] = data["sizeBytes"]
    else:
        out["size_bytes"] = 0
    if data.get("delivery") is not None:
        import capo_continuum.types.patch_delivery

        out["delivery"] = capo_continuum.types.patch_delivery.deserialize_json(
            data["delivery"]
        )
    return out

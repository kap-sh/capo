"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeIssueArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.issue_artifact_body
    import capo_continuum.types.issue_artifact_id
    import capo_continuum.types.issue_artifact_media_type
    import capo_continuum.types.issue_artifact_producer_summary
    import capo_continuum.types.issue_artifact_type


class GetCodeIssueArtifactOutput(TypedDict, closed=True):
    artifact_id: "capo_continuum.types.issue_artifact_id.IssueArtifactId"
    """The unique identifier of the artifact."""
    artifact_type: "capo_continuum.types.issue_artifact_type.IssueArtifactType"
    """Semantic category of the artifact."""
    media_type: "capo_continuum.types.issue_artifact_media_type.IssueArtifactMediaType"
    """MIME type the producer declared for its content."""
    body: "capo_continuum.types.issue_artifact_body.IssueArtifactBody"
    """The artifact body, projected against the shape defined for its artifactType. A type with a defined shape is returned as that structure, and anything else through `IssueArtifactBody.raw`."""
    metadata: NotRequired["object"]
    """Producer-defined structured metadata, when the producer supplied any. Returned only for an artifactType whose content has no defined shape, so that the artifact stays inspectable. For an artifactType with a defined shape, `body` carries the content and this member is omitted."""
    producer: "capo_continuum.types.issue_artifact_producer_summary.IssueArtifactProducerSummary"
    """The agent that produced the artifact."""
    created_at: "datetime.datetime"
    """The timestamp when the artifact was created."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeIssueArtifactOutput) -> dict:
    out: dict = {}
    out["artifactId"] = value["artifact_id"]
    import capo_continuum.types.issue_artifact_type

    out["artifactType"] = capo_continuum.types.issue_artifact_type.serialize_json(
        value["artifact_type"]
    )
    out["mediaType"] = value["media_type"]
    import capo_continuum.types.issue_artifact_body

    out["body"] = capo_continuum.types.issue_artifact_body.serialize_json(value["body"])
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    import capo_continuum.types.issue_artifact_producer_summary

    out["producer"] = (
        capo_continuum.types.issue_artifact_producer_summary.serialize_json(
            value["producer"]
        )
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> GetCodeIssueArtifactOutput:
    out: GetCodeIssueArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("artifactId") is not None:
        out["artifact_id"] = data["artifactId"]
    else:
        out["artifact_id"] = ""
    if data.get("artifactType") is not None:
        import capo_continuum.types.issue_artifact_type

        out["artifact_type"] = (
            capo_continuum.types.issue_artifact_type.deserialize_json(
                data["artifactType"]
            )
        )
    else:
        import typing

        out["artifact_type"] = typing.cast(
            "capo_continuum.types.issue_artifact_type.IssueArtifactType", ""
        )
    if data.get("mediaType") is not None:
        out["media_type"] = data["mediaType"]
    else:
        out["media_type"] = ""
    if data.get("body") is not None:
        import capo_continuum.types.issue_artifact_body

        out["body"] = capo_continuum.types.issue_artifact_body.deserialize_json(
            data["body"]
        )
    else:
        out["body"] = {"$unknown": {"name": ""}}
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    if data.get("producer") is not None:
        import capo_continuum.types.issue_artifact_producer_summary

        out["producer"] = (
            capo_continuum.types.issue_artifact_producer_summary.deserialize_json(
                data["producer"]
            )
        )
    else:
        raise DeserializationError("GetCodeIssueArtifactOutput.producer required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

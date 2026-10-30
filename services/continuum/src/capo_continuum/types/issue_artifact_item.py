"""Generated from Smithy shape ``com.amazonaws.continuum#IssueArtifactItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.issue_artifact_id
    import capo_continuum.types.issue_artifact_media_type
    import capo_continuum.types.issue_artifact_producer_summary
    import capo_continuum.types.issue_artifact_type


class IssueArtifactItem(TypedDict, closed=True):
    artifact_id: "capo_continuum.types.issue_artifact_id.IssueArtifactId"
    """The unique identifier of the artifact."""
    artifact_type: "capo_continuum.types.issue_artifact_type.IssueArtifactType"
    """Semantic category of the artifact."""
    media_type: "capo_continuum.types.issue_artifact_media_type.IssueArtifactMediaType"
    """MIME type of the artifact content."""
    producer: "capo_continuum.types.issue_artifact_producer_summary.IssueArtifactProducerSummary"
    """The agent that produced the artifact."""
    content_size_bytes: "int"
    """Size of the artifact content in bytes. The content itself is returned by GetCodeIssueArtifact."""
    created_at: "datetime.datetime"
    """The timestamp when the artifact was created."""


# --- restJson1 ser/de ---
def serialize_json(value: IssueArtifactItem) -> dict:
    out: dict = {}
    out["artifactId"] = value["artifact_id"]
    import capo_continuum.types.issue_artifact_type

    out["artifactType"] = capo_continuum.types.issue_artifact_type.serialize_json(
        value["artifact_type"]
    )
    out["mediaType"] = value["media_type"]
    import capo_continuum.types.issue_artifact_producer_summary

    out["producer"] = (
        capo_continuum.types.issue_artifact_producer_summary.serialize_json(
            value["producer"]
        )
    )
    out["contentSizeBytes"] = value["content_size_bytes"]
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> IssueArtifactItem:
    out: IssueArtifactItem = {}  # type: ignore[typeddict-item]
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
    if data.get("producer") is not None:
        import capo_continuum.types.issue_artifact_producer_summary

        out["producer"] = (
            capo_continuum.types.issue_artifact_producer_summary.deserialize_json(
                data["producer"]
            )
        )
    else:
        raise DeserializationError("IssueArtifactItem.producer required")
    if data.get("contentSizeBytes") is not None:
        out["content_size_bytes"] = data["contentSizeBytes"]
    else:
        out["content_size_bytes"] = 0
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

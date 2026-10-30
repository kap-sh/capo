"""Generated from Smithy shape ``com.amazonaws.continuum#IssueArtifactProducerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.issue_artifact_producer_name


class IssueArtifactProducerSummary(TypedDict, closed=True):
    agent: "capo_continuum.types.issue_artifact_producer_name.IssueArtifactProducerName"
    """Stable producer name, such as ContinuumValidation."""


# --- restJson1 ser/de ---
def serialize_json(value: IssueArtifactProducerSummary) -> dict:
    out: dict = {}
    out["agent"] = value["agent"]
    return out


def deserialize_json(data: dict) -> IssueArtifactProducerSummary:
    out: IssueArtifactProducerSummary = {}  # type: ignore[typeddict-item]
    if data.get("agent") is not None:
        out["agent"] = data["agent"]
    else:
        out["agent"] = ""
    return out

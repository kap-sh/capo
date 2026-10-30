"""Generated from Smithy shape ``com.amazonaws.continuum#ArtifactCitations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.artifact_citation

ArtifactCitations: TypeAlias = list[
    "capo_continuum.types.artifact_citation.ArtifactCitation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactCitations) -> list:
    return list(value)


def deserialize_json(data: list) -> ArtifactCitations:
    return [item for item in data if item is not None]

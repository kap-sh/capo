"""Generated from Smithy shape ``com.amazonaws.continuum#ArtifactHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.artifact_citation
    import capo_continuum.types.artifact_text

ArtifactHeaders: TypeAlias = dict[
    "capo_continuum.types.artifact_citation.ArtifactCitation",
    "capo_continuum.types.artifact_text.ArtifactText",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ArtifactHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ArtifactHeaders:
    out: ArtifactHeaders = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out

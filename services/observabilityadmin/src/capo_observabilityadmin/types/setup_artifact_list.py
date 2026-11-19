"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SetupArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.setup_artifact

SetupArtifactList: TypeAlias = list[
    "capo_observabilityadmin.types.setup_artifact.SetupArtifact"
]


# --- restJson1 ser/de ---
def serialize_json(value: SetupArtifactList) -> list:
    import capo_observabilityadmin.types.setup_artifact

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.setup_artifact.serialize_json(item))
    return out


def deserialize_json(data: list) -> SetupArtifactList:
    import capo_observabilityadmin.types.setup_artifact

    out: SetupArtifactList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_observabilityadmin.types.setup_artifact.deserialize_json(item))
    return out

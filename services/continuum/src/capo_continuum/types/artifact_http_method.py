"""Generated from Smithy shape ``com.amazonaws.continuum#ArtifactHttpMethod``."""

from typing import Literal, TypeAlias, cast

"""HTTP method recorded on an exploit artifact. An enum rather than a pattern-constrained string: callers branch on the method, so the full set belongs in the generated SDKs. A producer value outside this set omits the exploit artifact rather than surfacing an unmodeled method."""
ArtifactHttpMethod: TypeAlias = Literal[
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactHttpMethod) -> str:
    return value


def deserialize_json(data: str) -> ArtifactHttpMethod:
    return cast(ArtifactHttpMethod, data)

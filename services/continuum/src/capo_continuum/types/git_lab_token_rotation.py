"""Generated from Smithy shape ``com.amazonaws.continuum#GitLabTokenRotation``."""

from typing import Literal, TypeAlias, cast

"""How a GitLab integration's access token is rotated."""
GitLabTokenRotation: TypeAlias = Literal[
    "AUTOMATIC",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GitLabTokenRotation) -> str:
    return value


def deserialize_json(data: str) -> GitLabTokenRotation:
    return cast(GitLabTokenRotation, data)

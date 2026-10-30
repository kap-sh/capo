"""Generated from Smithy shape ``com.amazonaws.continuum#GitLabTargetType``."""

from typing import Literal, TypeAlias, cast

"""Whether the GitLab integration targets an entire group or a single project."""
GitLabTargetType: TypeAlias = Literal[
    "GROUP",
    "PROJECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: GitLabTargetType) -> str:
    return value


def deserialize_json(data: str) -> GitLabTargetType:
    return cast(GitLabTargetType, data)

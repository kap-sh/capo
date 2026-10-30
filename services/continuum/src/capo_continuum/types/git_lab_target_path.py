"""Generated from Smithy shape ``com.amazonaws.continuum#GitLabTargetPath``."""

from typing import TypeAlias

"""The GitLab group or project path (nested, slash-separated), e.g. "my-org/platform/widgets". Each slash-delimited segment must start with an alphanumeric, so `..` segments and empty, leading or trailing slashes are rejected."""
GitLabTargetPath: TypeAlias = str

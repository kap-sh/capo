"""Generated from Smithy shape ``com.amazonaws.continuum#IssueArtifactContent``."""

from typing import TypeAlias

"""Inline artifact content. One shared shape keeps the existing content member and generated SDK type stable across artifact kinds instead of adding a PATCH-only member or changing the wire contract to a kind-specific union. The shared model bound accommodates PATCH; kind-specific limits are enforced by the service after deserialization: PATCH accepts up to 5,242,880 UTF-8 bytes (5 MiB), while non-PATCH kinds, including initial Issue artifacts, are limited to 1,048,576 characters (1 MiB of characters). The wider shared model bound is not the non-PATCH limit. PATCH reads return the raw content from the immutable service copy; storage receipts remain private implementation data."""
IssueArtifactContent: TypeAlias = str

"""Generated from Smithy shape ``com.amazonaws.continuum#ArtifactCitation``."""

from typing import TypeAlias

"""A citation supporting a claim: file:line, an HTTP response, or a graph node id. 1024 rather than 512: validation agents cite a span of reasoning rather than a single location, reaching ~930 characters, and an over-long citation drops its entire `ReasoningStep` — claim included — rather than just the citation."""
ArtifactCitation: TypeAlias = str

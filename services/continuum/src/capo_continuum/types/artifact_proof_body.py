"""Generated from Smithy shape ``com.amazonaws.continuum#ArtifactProofBody``."""

from typing import TypeAlias

"""The body of a proof: executed code, the output it produced, or an annotated source walk. Its own type rather than `ArtifactText` because these are whole documents, not fields: observed bodies reach 12.8K of code and 16K of captured output. At most one proof is present per artifact, so a large bound here does not multiply the way `ArtifactText`'s does."""
ArtifactProofBody: TypeAlias = str

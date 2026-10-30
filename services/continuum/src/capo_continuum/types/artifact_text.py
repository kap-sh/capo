"""Generated from Smithy shape ``com.amazonaws.continuum#ArtifactText``."""

from typing import TypeAlias

"""A bounded free-text field in a projected artifact body. 8192 rather than 4096: a validation agent's reasoning `claim` runs to ~5.6K in practice, and a claim dropped on length takes its whole `ReasoningStep` with it. Deliberately NOT raised to the proof-body bound — this type is also the member of a 50-entry `ReasoningSteps` list and of `ArtifactHeaders`, so its bound multiplies into the worst-case response size. The product of these bounds is NOT what actually caps a response. Every projected body is read out of one `IssueArtifactContent`, itself bounded at 5 MiB, so no projection can exceed the size of the content it came from whatever the member bounds permit. Keeping this one modest is about not inflating a typical response, not about the ceiling."""
ArtifactText: TypeAlias = str

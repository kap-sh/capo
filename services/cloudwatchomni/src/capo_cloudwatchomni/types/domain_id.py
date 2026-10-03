"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DomainId``."""

from typing import TypeAlias

"""Domain identifier in "d-{base36}" format, e.g. "d-5h2neqbcpc4sk6gswog". Minted by the backend as "d-" + base36(UUID) — at most "d-" plus 25 chars. Note: not a bare UUID (unlike space/grant ids), so a UUID pattern would wrongly reject valid domain ids."""
DomainId: TypeAlias = str

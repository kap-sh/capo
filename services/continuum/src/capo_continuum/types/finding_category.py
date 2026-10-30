"""Generated from Smithy shape ``com.amazonaws.continuum#FindingCategory``."""

from typing import TypeAlias

"""A vulnerability-taxonomy label: the producer's category, sub-category, or OWASP category. Deliberately unconstrained beyond length -- producers do not share a taxonomy, so this is NOT a stable filter key across finding types. Use `cweIds` when a stable classification is needed."""
FindingCategory: TypeAlias = str

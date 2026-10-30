"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationConfidence``."""

from typing import TypeAlias

"""Confidence in a validation verdict, on the producer's native 0-1 scale. Deliberately unconstrained in the model: the smithy-rs server SDK rejects `@range` on a double (smithy-rs#2007). The bound is enforced where the value is produced instead — Control Plane projects this from stored content and omits the member when the stored value falls outside 0-1, so an out-of-range producer value never surfaces here as a valid confidence. The rest of the body still projects; only the confidence is dropped."""
ValidationConfidence: TypeAlias = float

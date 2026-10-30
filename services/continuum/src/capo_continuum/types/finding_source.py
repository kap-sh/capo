"""Generated from Smithy shape ``com.amazonaws.continuum#FindingSource``."""

from typing import TypeAlias

"""The system that produced a finding -- Continuum's own scanner, or the product name (falling back to the vendor name) from a customer document's OCSF metadata.product. Distinguishes two customer integrations that share a `type`."""
FindingSource: TypeAlias = str

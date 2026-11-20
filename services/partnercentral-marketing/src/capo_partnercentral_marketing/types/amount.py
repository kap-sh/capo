"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#Amount``."""

from typing import TypeAlias

"""A decimal amount. Accepts "100", "100.5", or "100.00". A string, not a float, because a budget is exact and binary floating point cannot represent every two-decimal value."""
Amount: TypeAlias = str

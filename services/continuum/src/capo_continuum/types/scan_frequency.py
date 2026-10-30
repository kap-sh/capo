"""Generated from Smithy shape ``com.amazonaws.continuum#ScanFrequency``."""

from typing import TypeAlias

"""ISO-8601 duration requested for recurring scans. Supported values are P1D (1 day), P2D (2 days), P7D (7 days), and PT0H (manual scans only). Existing environments with no cadence or a legacy PT6H, PT12H, or PT24H cadence use P1D. Legacy PT48H uses P2D. New requests must use a supported value."""
ScanFrequency: TypeAlias = str

"""Generated from Smithy shape ``com.amazonaws.continuum#CollectorArn``."""

from typing import TypeAlias

"""The Amazon Resource Name (ARN) of the Collector. Format: arn:{partition}:continuum:{region}:{account}:collectors/{collectorId} The resource-id segment is a fresh, randomly generated identifier assigned when the Collector is created — not a fixed or predictable value."""
CollectorArn: TypeAlias = str

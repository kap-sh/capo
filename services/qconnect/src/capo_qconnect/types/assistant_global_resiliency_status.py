"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantGlobalResiliencyStatus``."""

from typing import TypeAlias

"""Whether an assistant's Connect instance is replicated by Amazon Connect Global Resiliency. Distinct from `GlobalResiliencyStatus` on `ModelSummary`, which answers a different question - is this *model* published across the replication group. This one answers whether *this assistant* is subject to that constraint at all."""
AssistantGlobalResiliencyStatus: TypeAlias = str

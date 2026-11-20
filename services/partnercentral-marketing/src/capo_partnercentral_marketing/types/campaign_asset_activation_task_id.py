"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetActivationTaskId``."""

from typing import TypeAlias

"""Service-minted activation task identifier: `atsk-` and 13 characters, from AWS Marketplace's ID Generation Service (DG-082). The suffix is any 13 ASCII letters or digits, because IDGS's own spec is ambiguous about its charset (DG-092). It refuses an ARN, and it refuses a campaign id, which a client may otherwise mistake for a task id."""
CampaignAssetActivationTaskId: TypeAlias = str

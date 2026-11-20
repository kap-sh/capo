"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignTemplateId``."""

from typing import TypeAlias

"""A campaign template's id. A campaign template has no ARN and is not an IAM resource type: its operations are action-only (DG-084). So an id is the only way to name one, and an ARN, or any value with `:` or `/`, is refused as an invalid id. `tmpl-` and 13 lowercase letters or digits (DG-088)."""
CampaignTemplateId: TypeAlias = str

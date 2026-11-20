"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#EngagementGroupId``."""

from typing import TypeAlias

"""An engagement group's id, as `ListEngagementGroups` (AWS Partner Central Selling) returns it: `eng-grp-` and 14 lowercase alphanumerics. The same constraints as the Leads model's `GroupId`, whose pattern pins only the current shape: if Leads relaxes it, so does this."""
EngagementGroupId: TypeAlias = str

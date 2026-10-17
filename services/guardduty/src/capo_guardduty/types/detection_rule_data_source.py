"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleDataSource``."""

from typing import Literal, TypeAlias, cast

DetectionRuleDataSource: TypeAlias = Literal["CloudTrailManagementEvent",]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleDataSource) -> str:
    return value


def deserialize_json(data: str) -> DetectionRuleDataSource:
    return cast(DetectionRuleDataSource, data)

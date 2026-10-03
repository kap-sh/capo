"""Generated from Smithy shape ``com.amazonaws.iot#AlertTargetType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of alert target: one of "SNS".</p>"""
AlertTargetType: TypeAlias = Literal["SNS",]


# --- restJson1 ser/de ---
def serialize_json(value: AlertTargetType) -> str:
    return value


def deserialize_json(data: str) -> AlertTargetType:
    return cast(AlertTargetType, data)

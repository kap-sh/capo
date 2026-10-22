"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of insight.</p>"""
InsightType: TypeAlias = Literal["FAILURE",]


# --- restJson1 ser/de ---
def serialize_json(value: InsightType) -> str:
    return value


def deserialize_json(data: str) -> InsightType:
    return cast(InsightType, data)

"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DevOpsAgentVerdict``."""

from typing import Literal, TypeAlias, cast

DevOpsAgentVerdict: TypeAlias = Literal[
    "PASS",
    "FAIL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DevOpsAgentVerdict) -> str:
    return value


def deserialize_json(data: str) -> DevOpsAgentVerdict:
    return cast(DevOpsAgentVerdict, data)

"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerFilterType``."""

from typing import Literal, TypeAlias, cast

"""<p>A pull request value that a filter matches.</p>"""
TriggerFilterType: TypeAlias = Literal[
    "TARGET_BRANCH",
    "LABEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerFilterType) -> str:
    return value


def deserialize_json(data: str) -> TriggerFilterType:
    return cast(TriggerFilterType, data)

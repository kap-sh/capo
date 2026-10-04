"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerEvent``."""

from typing import Literal, TypeAlias, cast

"""<p>A pull request event that can start an automatic code review. For GitLab repositories, pull request refers to a merge request.</p>"""
TriggerEvent: TypeAlias = Literal[
    "PULL_REQUEST_READY_FOR_REVIEW",
    "PULL_REQUEST_DRAFT",
    "PULL_REQUEST_LABEL_ADDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerEvent) -> str:
    return value


def deserialize_json(data: str) -> TriggerEvent:
    return cast(TriggerEvent, data)

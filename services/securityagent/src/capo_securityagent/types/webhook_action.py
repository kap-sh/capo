"""Generated from Smithy shape ``com.amazonaws.securityagent#WebhookAction``."""

from typing import Literal, TypeAlias, cast

"""<p>The action to perform on an integration's webhook.</p>"""
WebhookAction: TypeAlias = Literal[
    "CREATE_IF_ABSENT",
    "ROTATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: WebhookAction) -> str:
    return value


def deserialize_json(data: str) -> WebhookAction:
    return cast(WebhookAction, data)

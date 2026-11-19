"""Generated from Smithy shape ``com.amazonaws.mediatailor#ManifestServicePublishOptInEventType``."""

from typing import Literal, TypeAlias, cast

ManifestServicePublishOptInEventType: TypeAlias = Literal[
    "PRE_SESSION_INIT_HOOK_SUMMARY",
    "PRE_SESSION_INIT_FUNCTION_COMPLETED",
    "POST_ORIGIN_RESPONSE_HOOK_SUMMARY",
    "POST_ORIGIN_RESPONSE_FUNCTION_COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManifestServicePublishOptInEventType) -> str:
    return value


def deserialize_json(data: str) -> ManifestServicePublishOptInEventType:
    return cast(ManifestServicePublishOptInEventType, data)

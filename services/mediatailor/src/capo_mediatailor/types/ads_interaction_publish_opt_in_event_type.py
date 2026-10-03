"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdsInteractionPublishOptInEventType``."""

from typing import Literal, TypeAlias, cast

"""<p>An ADS interaction log event type that MediaTailor emits only when you opt in to it. For descriptions of each event type, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ads-log-format.html">MediaTailor ADS logs description and event types</a> in Elemental MediaTailor User Guide.</p>"""
AdsInteractionPublishOptInEventType: TypeAlias = Literal[
    "RAW_ADS_RESPONSE",
    "RAW_ADS_REQUEST",
    "RAW_BID_REQUEST",
    "RAW_BID_RESPONSE",
    "PRE_ADS_REQUEST_HOOK_SUMMARY",
    "PRE_ADS_REQUEST_FUNCTION_COMPLETED",
    "POST_ADS_RESPONSE_HOOK_SUMMARY",
    "POST_ADS_RESPONSE_FUNCTION_COMPLETED",
    "PRE_MANIFEST_INSERTION_HOOK_SUMMARY",
    "PRE_MANIFEST_INSERTION_FUNCTION_COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdsInteractionPublishOptInEventType) -> str:
    return value


def deserialize_json(data: str) -> AdsInteractionPublishOptInEventType:
    return cast(AdsInteractionPublishOptInEventType, data)

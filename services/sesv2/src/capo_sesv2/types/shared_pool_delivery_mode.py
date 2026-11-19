"""Generated from Smithy shape ``com.amazonaws.sesv2#SharedPoolDeliveryMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The shared pool delivery mode for a configuration set. See <code>DeliveryOptions$SharedPoolDeliveryMode</code> for the list of supported values and their meanings.</p>"""
SharedPoolDeliveryMode: TypeAlias = Literal[
    "GLOBAL",
    "REGIONAL",
    "ACCOUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedPoolDeliveryMode) -> str:
    return value


def deserialize_json(data: str) -> SharedPoolDeliveryMode:
    return cast(SharedPoolDeliveryMode, data)

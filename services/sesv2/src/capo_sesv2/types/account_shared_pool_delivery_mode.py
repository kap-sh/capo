"""Generated from Smithy shape ``com.amazonaws.sesv2#AccountSharedPoolDeliveryMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The shared pool delivery mode for an Amazon SES account. See <code>PutAccountDeliveryAttributesRequest$SharedPoolDeliveryMode</code> for the list of supported values and their meanings.</p>"""
AccountSharedPoolDeliveryMode: TypeAlias = Literal[
    "GLOBAL",
    "REGIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountSharedPoolDeliveryMode) -> str:
    return value


def deserialize_json(data: str) -> AccountSharedPoolDeliveryMode:
    return cast(AccountSharedPoolDeliveryMode, data)

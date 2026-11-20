"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: datetime.datetime) -> datetime.datetime:
    return value


def deserialize_cbor(data: datetime.datetime) -> datetime.datetime:
    return data

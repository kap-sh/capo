"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SocialConnectionStatus``."""

from typing import Literal, TypeAlias, cast

"""Authorization state of a social connection. The execution backend's view, plus one thing it does not report: a Facebook connection with no Page reads `active` there but cannot post (`PAGE_REQUIRED`). There is deliberately no "authorizing" value: a connection exists only once consent has completed, so an unfinished consent is simply not in the list."""
SocialConnectionStatus: TypeAlias = Literal[
    "AUTHORIZED",
    "EXPIRED",
    "PAGE_REQUIRED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SocialConnectionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> SocialConnectionStatus:
    return cast(SocialConnectionStatus, data)

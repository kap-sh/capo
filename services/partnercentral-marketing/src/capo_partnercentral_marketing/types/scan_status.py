"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ScanStatus``."""

from typing import Literal, TypeAlias, cast

"""The verdict of a file's malware and content-quality scan. <p>A process with an outcome, not a resource with a lifecycle — hence `Status`. A file is accepted and scanned afterwards, so `PENDING` is a real, observable state rather than an internal one, and it is a refusal at launch rather than something a launch waits on."""
ScanStatus: TypeAlias = Literal[
    "PENDING",
    "CLEAN",
    "REJECTED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScanStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ScanStatus:
    return cast(ScanStatus, data)

"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#FileFormat``."""

from typing import Literal, TypeAlias, cast

"""Concrete file format of a rendered or downloadable artifact. DG-030 added `HTML` and `IMAGE` so one enum covers both the download-only office formats and the formats the service renders itself. Before that, an asset carried an ad-hoc `HTML | PDF` and a template entry an ad-hoc `HTML | PDF | IMAGE`, and the two disagreed with each other."""
FileFormat: TypeAlias = Literal[
    "PDF",
    "DOCX",
    "PPTX",
    "HTML",
    "IMAGE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FileFormat) -> str:
    return value


def deserialize_cbor(data: str) -> FileFormat:
    return cast(FileFormat, data)

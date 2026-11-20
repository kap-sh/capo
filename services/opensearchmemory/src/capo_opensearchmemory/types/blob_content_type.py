"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BlobContentType``."""

from typing import Literal, TypeAlias, cast

"""<p>The media type of a document submitted as a <code>blob</code>. Only PDF is supported.</p>"""
BlobContentType: TypeAlias = Literal[
    "application/pdf",
    "image/png",
    "image/jpeg",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlobContentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BlobContentType:
    return cast(BlobContentType, data)

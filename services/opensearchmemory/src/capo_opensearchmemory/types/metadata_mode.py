"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MetadataMode``."""

from typing import Literal, TypeAlias, cast

"""<p>How an <code>UpdateMemory</code> request's <code>metadata</code> combines with the stored metadata. The default is <code>REPLACE</code>.</p>"""
MetadataMode: TypeAlias = Literal[
    "REPLACE",
    "MERGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetadataMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetadataMode:
    return cast(MetadataMode, data)

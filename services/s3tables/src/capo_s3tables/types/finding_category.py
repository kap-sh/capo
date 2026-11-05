"""Generated from Smithy shape ``com.amazonaws.s3tables#FindingCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>The category of a compatibility report finding, by what you change to fix it. Valid values:</p> <ul> <li> <p> <code>access</code> - A permission or a request setting. You don't need to change the source.</p> </li> <li> <p> <code>metadata</code> - The Amazon Web Services Glue table definition, or properties of a source object, such as its size, storage class, encryption or Parquet types.</p> </li> <li> <p> <code>data</code> - The contents of a source object, such as a partition value that can't be read, an object overwritten after an earlier migration, or a corrupt file.</p> </li> <li> <p> <code>internal</code> - An internal error in S3 Tables. Retry the migration, and contact Amazon Web Services Support if the error persists.</p> </li> </ul>"""
FindingCategory: TypeAlias = Literal[
    "access",
    "metadata",
    "data",
    "internal",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingCategory) -> str:
    return value


def deserialize_json(data: str) -> FindingCategory:
    return cast(FindingCategory, data)

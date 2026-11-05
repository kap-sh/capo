"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationSourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of source that a migration reads from. It names the member that is set in <code>SourceConfiguration</code>.</p>"""
MigrationSourceType: TypeAlias = Literal["glueTable",]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationSourceType) -> str:
    return value


def deserialize_json(data: str) -> MigrationSourceType:
    return cast(MigrationSourceType, data)

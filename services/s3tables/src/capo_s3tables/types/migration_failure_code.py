"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationFailureCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason a migration failed. Each code names the cause, or the report that lists the findings.</p>"""
MigrationFailureCode: TypeAlias = Literal[
    "rolePermissions",
    "sourcePermissions",
    "destinationPermissions",
    "resourceNotFound",
    "sourceNotSupported",
    "objectMigrationReport",
    "objectCompatibilityReport",
    "tableCompatibilityReport",
    "internalError",
    "reportBucketNotSupported",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationFailureCode) -> str:
    return value


def deserialize_json(data: str) -> MigrationFailureCode:
    return cast(MigrationFailureCode, data)

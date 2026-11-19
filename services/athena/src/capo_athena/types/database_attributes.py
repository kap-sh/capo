"""Generated from Smithy shape ``com.amazonaws.athena#DatabaseAttributes``."""

from typing import Literal, TypeAlias, cast

"""<p>A database property that can be requested in the <code>AttributesToGet</code> parameter of <code>ListDatabases</code>.</p>"""
DatabaseAttributes: TypeAlias = Literal["NAME",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseAttributes:
    return cast(DatabaseAttributes, data)

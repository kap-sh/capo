"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportDataType``."""

from typing import Literal, TypeAlias, cast

"""<p>The category of data that an export job produces. Currently, the only supported value is <code>FINDINGS</code>.</p>"""
ExportDataType: TypeAlias = Literal["FINDINGS",]


# --- restJson1 ser/de ---
def serialize_json(value: ExportDataType) -> str:
    return value


def deserialize_json(data: str) -> ExportDataType:
    return cast(ExportDataType, data)

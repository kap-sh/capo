"""Generated from Smithy shape ``com.amazonaws.sesv2#DimensionValueSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The location where the Amazon SES API v2 finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an <code>X-SES-MESSAGE-TAGS</code> header or a parameter to the <code>SendEmail</code> or <code>SendBulkEmail</code> operation, choose <code>MESSAGE_TAG</code>. To use your own email headers, choose <code>EMAIL_HEADER</code>. To use link tags, choose <code>LINK_TAG</code>.</p>"""
DimensionValueSource: TypeAlias = Literal[
    "MESSAGE_TAG",
    "EMAIL_HEADER",
    "LINK_TAG",
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionValueSource) -> str:
    return value


def deserialize_json(data: str) -> DimensionValueSource:
    return cast(DimensionValueSource, data)

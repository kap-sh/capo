"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TemplateFieldSection``."""

from typing import Literal, TypeAlias, cast

"""Layout section of a template field."""
TemplateFieldSection: TypeAlias = Literal[
    "HEADER",
    "BODY",
    "FOOTER",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TemplateFieldSection) -> str:
    return value


def deserialize_cbor(data: str) -> TemplateFieldSection:
    return cast(TemplateFieldSection, data)

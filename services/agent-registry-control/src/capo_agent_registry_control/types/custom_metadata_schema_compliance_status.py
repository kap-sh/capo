"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CustomMetadataSchemaComplianceStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Indicates whether a registry record's custom metadata conforms to the registry's current schema. <code>COMPLIANT</code> means all required fields are present and all values match their declared types. <code>NON_COMPLIANT</code> means the metadata does not satisfy the current schema, for example because the schema was updated after the record was last modified.</p>"""
CustomMetadataSchemaComplianceStatus: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetadataSchemaComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomMetadataSchemaComplianceStatus:
    return cast(CustomMetadataSchemaComplianceStatus, data)

"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.custom_s3_location
    import capo_bedrock_agent.types.document_access_control_list
    import capo_bedrock_agent.types.metadata_attributes
    import capo_bedrock_agent.types.metadata_source_type


class DocumentMetadata(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.metadata_source_type.MetadataSourceType"
    """<p>The type of the source source from which to add metadata.</p>"""
    inline_attributes: NotRequired[
        "capo_bedrock_agent.types.metadata_attributes.MetadataAttributes"
    ]
    """<p>An array of objects, each of which defines a metadata attribute to associate with the content to ingest. You define the attributes inline.</p>"""
    s3_location: NotRequired[
        "capo_bedrock_agent.types.custom_s3_location.CustomS3Location"
    ]
    """<p>The Amazon S3 location of the file containing metadata to associate with the content to ingest.</p>"""
    access_control_list: NotRequired[
        "capo_bedrock_agent.types.document_access_control_list.DocumentAccessControlList"
    ]
    """<p>Access control list for the document. Used when metadata type is IN_LINE_ATTRIBUTE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentMetadata) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.metadata_source_type

    out["type"] = capo_bedrock_agent.types.metadata_source_type.serialize_json(
        value["type"]
    )
    if "inline_attributes" in value:
        import capo_bedrock_agent.types.metadata_attributes

        out["inlineAttributes"] = (
            capo_bedrock_agent.types.metadata_attributes.serialize_json(
                value["inline_attributes"]
            )
        )
    if "s3_location" in value:
        import capo_bedrock_agent.types.custom_s3_location

        out["s3Location"] = capo_bedrock_agent.types.custom_s3_location.serialize_json(
            value["s3_location"]
        )
    if "access_control_list" in value:
        import capo_bedrock_agent.types.document_access_control_list

        out["accessControlList"] = (
            capo_bedrock_agent.types.document_access_control_list.serialize_json(
                value["access_control_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.metadata_source_type

        out["type"] = capo_bedrock_agent.types.metadata_source_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("DocumentMetadata.type required")
    if data.get("inlineAttributes") is not None:
        import capo_bedrock_agent.types.metadata_attributes

        out["inline_attributes"] = (
            capo_bedrock_agent.types.metadata_attributes.deserialize_json(
                data["inlineAttributes"]
            )
        )
    if data.get("s3Location") is not None:
        import capo_bedrock_agent.types.custom_s3_location

        out["s3_location"] = (
            capo_bedrock_agent.types.custom_s3_location.deserialize_json(
                data["s3Location"]
            )
        )
    if data.get("accessControlList") is not None:
        import capo_bedrock_agent.types.document_access_control_list

        out["access_control_list"] = (
            capo_bedrock_agent.types.document_access_control_list.deserialize_json(
                data["accessControlList"]
            )
        )
    return out


def redact_sensitive(value: DocumentMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline_attributes" in value:
        import capo_bedrock_agent.types.metadata_attributes

        out["inline_attributes"] = (
            capo_bedrock_agent.types.metadata_attributes.redact_sensitive(
                value["inline_attributes"]
            )
        )
    if "access_control_list" in value:
        import capo_bedrock_agent.types.document_access_control_list

        out["access_control_list"] = (
            capo_bedrock_agent.types.document_access_control_list.redact_sensitive(
                value["access_control_list"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentMetadataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_value_type
    import capo_kendra.types.document_metadata_configuration_name
    import capo_kendra.types.relevance
    import capo_kendra.types.search


class DocumentMetadataConfiguration(TypedDict, closed=True):
    name: "capo_kendra.types.document_metadata_configuration_name.DocumentMetadataConfigurationName"
    """<p>The name of the index field.</p>"""
    type: "capo_kendra.types.document_attribute_value_type.DocumentAttributeValueType"
    """<p>The data type of the index field. </p>"""
    relevance: NotRequired["capo_kendra.types.relevance.Relevance"]
    """<p>Provides tuning parameters to determine how the field affects the search results.</p>"""
    search: NotRequired["capo_kendra.types.search.Search"]
    """<p>Provides information about how the field is used during a search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadataConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_kendra.types.document_attribute_value_type

    out["Type"] = (
        capo_kendra.types.document_attribute_value_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    if "relevance" in value:
        import capo_kendra.types.relevance

        out["Relevance"] = capo_kendra.types.relevance.serialize_aws_json_1_1(
            value["relevance"]
        )
    if "search" in value:
        import capo_kendra.types.search

        out["Search"] = capo_kendra.types.search.serialize_aws_json_1_1(value["search"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadataConfiguration:
    out: DocumentMetadataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_kendra.types.document_attribute_value_type

        out["type"] = (
            capo_kendra.types.document_attribute_value_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_kendra.types.document_attribute_value_type.DocumentAttributeValueType",
            "",
        )
    if data.get("Relevance") is not None:
        import capo_kendra.types.relevance

        out["relevance"] = capo_kendra.types.relevance.deserialize_aws_json_1_1(
            data["Relevance"]
        )
    if data.get("Search") is not None:
        import capo_kendra.types.search

        out["search"] = capo_kendra.types.search.deserialize_aws_json_1_1(
            data["Search"]
        )
    return out

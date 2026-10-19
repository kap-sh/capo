"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentRelevanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.document_metadata_configuration_name
    import capo_kendra.types.relevance


class DocumentRelevanceConfiguration(TypedDict, closed=True):
    name: "capo_kendra.types.document_metadata_configuration_name.DocumentMetadataConfigurationName"
    """<p>The name of the index field.</p>"""
    relevance: "capo_kendra.types.relevance.Relevance"
    """<p>Provides information for tuning the relevance of a field in a search. When a query includes terms that match the field, the results are given a boost in the response based on these tuning parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentRelevanceConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_kendra.types.relevance

    out["Relevance"] = capo_kendra.types.relevance.serialize_aws_json_1_1(
        value["relevance"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentRelevanceConfiguration:
    out: DocumentRelevanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Relevance") is not None:
        import capo_kendra.types.relevance

        out["relevance"] = capo_kendra.types.relevance.deserialize_aws_json_1_1(
            data["Relevance"]
        )
    else:
        raise DeserializationError("DocumentRelevanceConfiguration.relevance required")
    return out

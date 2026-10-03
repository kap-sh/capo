"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeValueCountPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_value
    import capo_kendra.types.facet_result_list
    import capo_kendra.types.integer


class DocumentAttributeValueCountPair(TypedDict, closed=True):
    document_attribute_value: NotRequired[
        "capo_kendra.types.document_attribute_value.DocumentAttributeValue"
    ]
    """<p>The value of the attribute/field. For example, "HR".</p>"""
    count: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The number of documents in the response that have the attribute/field value for the key.</p>"""
    facet_results: NotRequired["capo_kendra.types.facet_result_list.FacetResultList"]
    """<p>Contains the results of a document attribute/field that is a nested facet. A <code>FacetResult</code> contains the counts for each facet nested within a facet.</p> <p>For example, the document attribute or facet "Department" includes a value called "Engineering". In addition, the document attribute or facet "SubDepartment" includes the values "Frontend" and "Backend" for documents assigned to "Engineering". You can display nested facets in the search results so that documents can be searched not only by department but also by a sub department within a department. The counts for documents that belong to "Frontend" and "Backend" within "Engineering" are returned for a query.</p> <p></p> <p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeValueCountPair) -> dict:
    out: dict = {}
    if "document_attribute_value" in value:
        import capo_kendra.types.document_attribute_value

        out["DocumentAttributeValue"] = (
            capo_kendra.types.document_attribute_value.serialize_aws_json_1_1(
                value["document_attribute_value"]
            )
        )
    if "count" in value:
        out["Count"] = value["count"]
    if "facet_results" in value:
        import capo_kendra.types.facet_result_list

        out["FacetResults"] = (
            capo_kendra.types.facet_result_list.serialize_aws_json_1_1(
                value["facet_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAttributeValueCountPair:
    out: DocumentAttributeValueCountPair = {}  # type: ignore[typeddict-item]
    if data.get("DocumentAttributeValue") is not None:
        import capo_kendra.types.document_attribute_value

        out["document_attribute_value"] = (
            capo_kendra.types.document_attribute_value.deserialize_aws_json_1_1(
                data["DocumentAttributeValue"]
            )
        )
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    if data.get("FacetResults") is not None:
        import capo_kendra.types.facet_result_list

        out["facet_results"] = (
            capo_kendra.types.facet_result_list.deserialize_aws_json_1_1(
                data["FacetResults"]
            )
        )
    return out

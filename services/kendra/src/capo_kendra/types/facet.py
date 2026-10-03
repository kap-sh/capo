"""Generated from Smithy shape ``com.amazonaws.kendra#Facet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_key
    import capo_kendra.types.facet_list
    import capo_kendra.types.top_document_attribute_value_count_pairs_size


class Facet(TypedDict, closed=True):
    document_attribute_key: NotRequired[
        "capo_kendra.types.document_attribute_key.DocumentAttributeKey"
    ]
    """<p>The unique key for the document attribute.</p>"""
    facets: NotRequired["capo_kendra.types.facet_list.FacetList"]
    """<p>An array of document attributes that are nested facets within a facet.</p> <p>For example, the document attribute or facet "Department" includes a value called "Engineering". In addition, the document attribute or facet "SubDepartment" includes the values "Frontend" and "Backend" for documents assigned to "Engineering". You can display nested facets in the search results so that documents can be searched not only by department but also by a sub department within a department. This helps your users further narrow their search.</p> <p>You can only have one nested facet within a facet. If you want to increase this limit, contact <a href="http://aws.amazon.com/contact-us/">Support</a>.</p>"""
    max_results: "capo_kendra.types.top_document_attribute_value_count_pairs_size.TopDocumentAttributeValueCountPairsSize"
    """<p>Maximum number of facet values per facet. The default is 10. You can use this to limit the number of facet values to less than 10. If you want to increase the default, contact <a href="http://aws.amazon.com/contact-us/">Support</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Facet) -> dict:
    out: dict = {}
    if "document_attribute_key" in value:
        out["DocumentAttributeKey"] = value["document_attribute_key"]
    if "facets" in value:
        import capo_kendra.types.facet_list

        out["Facets"] = capo_kendra.types.facet_list.serialize_aws_json_1_1(
            value["facets"]
        )
    out["MaxResults"] = value.get("max_results", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Facet:
    out: Facet = {}  # type: ignore[typeddict-item]
    if data.get("DocumentAttributeKey") is not None:
        out["document_attribute_key"] = data["DocumentAttributeKey"]
    if data.get("Facets") is not None:
        import capo_kendra.types.facet_list

        out["facets"] = capo_kendra.types.facet_list.deserialize_aws_json_1_1(
            data["Facets"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    return out

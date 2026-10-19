"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteIndexFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.dynamic_field_name


class DeleteIndexFieldRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    index_field_name: "capo_cloudsearch.types.dynamic_field_name.DynamicFieldName"
    """<p>The name of the index field your want to remove from the domain's indexing options.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIndexFieldRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    pairs.append((f"{key_prefix}IndexFieldName", str(value["index_field_name"])))


def deserialize_query(el: Element) -> DeleteIndexFieldRequest:
    out: DeleteIndexFieldRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_index_field_name = el.find("IndexFieldName")
    if child_index_field_name is not None:
        out["index_field_name"] = str(child_index_field_name.text or "")
    else:
        out["index_field_name"] = ""
    return out

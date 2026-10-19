"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineIndexFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.index_field


class DefineIndexFieldRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    index_field: "capo_cloudsearch.types.index_field.IndexField"
    """<p>The index field and field options you want to configure. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineIndexFieldRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    import capo_cloudsearch.types.index_field

    capo_cloudsearch.types.index_field.serialize_query(
        value["index_field"], pairs, f"{key_prefix}IndexField"
    )


def deserialize_query(el: Element) -> DefineIndexFieldRequest:
    out: DefineIndexFieldRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_index_field = el.find("IndexField")
    if child_index_field is not None:
        import capo_cloudsearch.types.index_field

        out["index_field"] = capo_cloudsearch.types.index_field.deserialize_query(
            child_index_field
        )
    else:
        raise DeserializationError("DefineIndexFieldRequest.index_field required")
    return out

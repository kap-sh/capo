"""Generated from Smithy shape ``com.amazonaws.cloudsearch#Suggester``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.document_suggester_options
    import capo_cloudsearch.types.standard_name


class Suggester(TypedDict, closed=True):
    suggester_name: "capo_cloudsearch.types.standard_name.StandardName"
    document_suggester_options: (
        "capo_cloudsearch.types.document_suggester_options.DocumentSuggesterOptions"
    )


# --- awsQuery ser/de ---
def serialize_query(
    value: Suggester, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SuggesterName", str(value["suggester_name"])))
    import capo_cloudsearch.types.document_suggester_options

    capo_cloudsearch.types.document_suggester_options.serialize_query(
        value["document_suggester_options"],
        pairs,
        f"{key_prefix}DocumentSuggesterOptions",
    )


def deserialize_query(el: Element) -> Suggester:
    out: Suggester = {}  # type: ignore[typeddict-item]
    child_suggester_name = el.find("SuggesterName")
    if child_suggester_name is not None:
        out["suggester_name"] = str(child_suggester_name.text or "")
    else:
        out["suggester_name"] = ""
    child_document_suggester_options = el.find("DocumentSuggesterOptions")
    if child_document_suggester_options is not None:
        import capo_cloudsearch.types.document_suggester_options

        out["document_suggester_options"] = (
            capo_cloudsearch.types.document_suggester_options.deserialize_query(
                child_document_suggester_options
            )
        )
    else:
        raise DeserializationError("Suggester.document_suggester_options required")
    return out

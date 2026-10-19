"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteSuggesterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.standard_name


class DeleteSuggesterRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    suggester_name: "capo_cloudsearch.types.standard_name.StandardName"
    """<p>Specifies the name of the suggester you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSuggesterRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    pairs.append((f"{key_prefix}SuggesterName", str(value["suggester_name"])))


def deserialize_query(el: Element) -> DeleteSuggesterRequest:
    out: DeleteSuggesterRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_suggester_name = el.find("SuggesterName")
    if child_suggester_name is not None:
        out["suggester_name"] = str(child_suggester_name.text or "")
    else:
        out["suggester_name"] = ""
    return out

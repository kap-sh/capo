"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineSuggesterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.suggester


class DefineSuggesterRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    suggester: "capo_cloudsearch.types.suggester.Suggester"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineSuggesterRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    import capo_cloudsearch.types.suggester

    capo_cloudsearch.types.suggester.serialize_query(
        value["suggester"], pairs, f"{key_prefix}Suggester"
    )


def deserialize_query(el: Element) -> DefineSuggesterRequest:
    out: DefineSuggesterRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_suggester = el.find("Suggester")
    if child_suggester is not None:
        import capo_cloudsearch.types.suggester

        out["suggester"] = capo_cloudsearch.types.suggester.deserialize_query(
            child_suggester
        )
    else:
        raise DeserializationError("DefineSuggesterRequest.suggester required")
    return out

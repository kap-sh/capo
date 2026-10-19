"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineAnalysisSchemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.analysis_scheme
    import capo_cloudsearch.types.domain_name


class DefineAnalysisSchemeRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    analysis_scheme: "capo_cloudsearch.types.analysis_scheme.AnalysisScheme"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineAnalysisSchemeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    import capo_cloudsearch.types.analysis_scheme

    capo_cloudsearch.types.analysis_scheme.serialize_query(
        value["analysis_scheme"], pairs, f"{key_prefix}AnalysisScheme"
    )


def deserialize_query(el: Element) -> DefineAnalysisSchemeRequest:
    out: DefineAnalysisSchemeRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_analysis_scheme = el.find("AnalysisScheme")
    if child_analysis_scheme is not None:
        import capo_cloudsearch.types.analysis_scheme

        out["analysis_scheme"] = (
            capo_cloudsearch.types.analysis_scheme.deserialize_query(
                child_analysis_scheme
            )
        )
    else:
        raise DeserializationError(
            "DefineAnalysisSchemeRequest.analysis_scheme required"
        )
    return out

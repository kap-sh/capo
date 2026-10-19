"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteAnalysisSchemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.standard_name


class DeleteAnalysisSchemeRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    analysis_scheme_name: "capo_cloudsearch.types.standard_name.StandardName"
    """<p>The name of the analysis scheme you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAnalysisSchemeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    pairs.append(
        (f"{key_prefix}AnalysisSchemeName", str(value["analysis_scheme_name"]))
    )


def deserialize_query(el: Element) -> DeleteAnalysisSchemeRequest:
    out: DeleteAnalysisSchemeRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_analysis_scheme_name = el.find("AnalysisSchemeName")
    if child_analysis_scheme_name is not None:
        out["analysis_scheme_name"] = str(child_analysis_scheme_name.text or "")
    else:
        out["analysis_scheme_name"] = ""
    return out

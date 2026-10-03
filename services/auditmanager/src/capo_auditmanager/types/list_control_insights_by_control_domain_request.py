"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListControlInsightsByControlDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_domain_id
    import capo_auditmanager.types.max_results
    import capo_auditmanager.types.token


class ListControlInsightsByControlDomainRequest(TypedDict, closed=True):
    control_domain_id: "capo_auditmanager.types.control_domain_id.ControlDomainId"
    """<p>The unique identifier for the control domain. </p> <p>Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["capo_auditmanager.types.max_results.MaxResults"]
    """<p>Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlInsightsByControlDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListControlInsightsByControlDomainRequest:
    out: ListControlInsightsByControlDomainRequest = {}  # type: ignore[typeddict-item]
    return out

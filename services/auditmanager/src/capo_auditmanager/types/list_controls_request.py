"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListControlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_catalog_id
    import capo_auditmanager.types.control_type
    import capo_auditmanager.types.max_results
    import capo_auditmanager.types.token


class ListControlsRequest(TypedDict, closed=True):
    control_type: "capo_auditmanager.types.control_type.ControlType"
    """<p>A filter that narrows the list of controls to a specific type. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["capo_auditmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results on a page or for an API request call. </p>"""
    control_catalog_id: NotRequired[
        "capo_auditmanager.types.control_catalog_id.ControlCatalogId"
    ]
    """<p>A filter that narrows the list of controls to a specific resource from the Amazon Web Services Control Catalog. </p> <p>To use this parameter, specify the ARN of the Control Catalog resource. You can specify either a control domain, a control objective, or a common control. For information about how to find the ARNs for these resources, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a>, <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListObjectives.html"> <code>ListObjectives</code> </a>, and <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html"> <code>ListCommonControls</code> </a>.</p> <note> <p>You can only filter by one Control Catalog resource at a time. Specifying multiple resource ARNs isn’t currently supported. If you want to filter by more than one ARN, we recommend that you run the <code>ListControls</code> operation separately for each ARN. </p> </note> <p>Alternatively, specify <code>UNCATEGORIZED</code> to list controls that aren't mapped to a Control Catalog resource. For example, this operation might return a list of custom controls that don't belong to any control domain or control objective.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListControlsRequest:
    out: ListControlsRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchImageSetsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.next_token
    import capo_medical_imaging.types.search_criteria


class SearchImageSetsRequest(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The identifier of the data store where the image sets reside.</p>"""
    search_criteria: NotRequired[
        "capo_medical_imaging.types.search_criteria.SearchCriteria"
    ]
    """<p>The search criteria that filters by applying a maximum of 1 item to <code>SearchByAttribute</code>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that can be returned in a search.</p>"""
    next_token: NotRequired["capo_medical_imaging.types.next_token.NextToken"]
    """<p>The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchImageSetsRequest) -> dict:
    out: dict = {}
    if "search_criteria" in value:
        import capo_medical_imaging.types.search_criteria

        out["searchCriteria"] = (
            capo_medical_imaging.types.search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchImageSetsRequest:
    out: SearchImageSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("searchCriteria") is not None:
        import capo_medical_imaging.types.search_criteria

        out["search_criteria"] = (
            capo_medical_imaging.types.search_criteria.deserialize_json(
                data["searchCriteria"]
            )
        )
    return out


def redact_sensitive(value: SearchImageSetsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "search_criteria" in value:
        out["search_criteria"] = "*** Sensitive Data Redacted ***"
    return out

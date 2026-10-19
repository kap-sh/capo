"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeFeaturedResultsSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set_id
    import capo_kendra.types.index_id


class DescribeFeaturedResultsSetRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used for featuring results.</p>"""
    featured_results_set_id: (
        "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    )
    """<p>The identifier of the set of featured results that you want to get information on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeaturedResultsSetRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["FeaturedResultsSetId"] = value["featured_results_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeaturedResultsSetRequest:
    out: DescribeFeaturedResultsSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("FeaturedResultsSetId") is not None:
        out["featured_results_set_id"] = data["FeaturedResultsSetId"]
    else:
        out["featured_results_set_id"] = ""
    return out

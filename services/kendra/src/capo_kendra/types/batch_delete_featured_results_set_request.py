"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteFeaturedResultsSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set_id_list
    import capo_kendra.types.index_id


class BatchDeleteFeaturedResultsSetRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used for featuring results.</p>"""
    featured_results_set_ids: (
        "capo_kendra.types.featured_results_set_id_list.FeaturedResultsSetIdList"
    )
    """<p>The identifiers of the featured results sets that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFeaturedResultsSetRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    import capo_kendra.types.featured_results_set_id_list

    out["FeaturedResultsSetIds"] = (
        capo_kendra.types.featured_results_set_id_list.serialize_aws_json_1_1(
            value["featured_results_set_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteFeaturedResultsSetRequest:
    out: BatchDeleteFeaturedResultsSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("FeaturedResultsSetIds") is not None:
        import capo_kendra.types.featured_results_set_id_list

        out["featured_results_set_ids"] = (
            capo_kendra.types.featured_results_set_id_list.deserialize_aws_json_1_1(
                data["FeaturedResultsSetIds"]
            )
        )
    else:
        out["featured_results_set_ids"] = []
    return out

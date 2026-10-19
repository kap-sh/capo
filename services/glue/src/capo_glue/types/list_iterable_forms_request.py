"""Generated from Smithy shape ``com.amazonaws.glue#ListIterableFormsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_id
    import capo_glue.types.iterable_form_name
    import capo_glue.types.page_size
    import capo_glue.types.token


class ListIterableFormsRequest(TypedDict, closed=True):
    asset_identifier: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset.</p>"""
    iterable_form_name: "capo_glue.types.iterable_form_name.IterableFormName"
    """<p>The name of the iterable form to list items from.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIterableFormsRequest) -> dict:
    out: dict = {}
    out["AssetIdentifier"] = value["asset_identifier"]
    out["IterableFormName"] = value["iterable_form_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIterableFormsRequest:
    out: ListIterableFormsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetIdentifier") is not None:
        out["asset_identifier"] = data["AssetIdentifier"]
    else:
        out["asset_identifier"] = ""
    if data.get("IterableFormName") is not None:
        out["iterable_form_name"] = data["IterableFormName"]
    else:
        out["iterable_form_name"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

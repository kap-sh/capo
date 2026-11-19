"""Generated from Smithy shape ``com.amazonaws.transcribe#ListCallAnalyticsCategoriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.category_properties_list
    import capo_transcribe.types.next_token


class ListCallAnalyticsCategoriesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    categories: NotRequired[
        "capo_transcribe.types.category_properties_list.CategoryPropertiesList"
    ]
    """<p>Provides detailed information about your Call Analytics categories, including all the rules associated with each category.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCallAnalyticsCategoriesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "categories" in value:
        import capo_transcribe.types.category_properties_list

        out["Categories"] = (
            capo_transcribe.types.category_properties_list.serialize_aws_json_1_1(
                value["categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCallAnalyticsCategoriesResponse:
    out: ListCallAnalyticsCategoriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Categories") is not None:
        import capo_transcribe.types.category_properties_list

        out["categories"] = (
            capo_transcribe.types.category_properties_list.deserialize_aws_json_1_1(
                data["Categories"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCallAnalyticsCategoriesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "categories" in value:
        import capo_transcribe.types.category_properties_list

        out["Categories"] = (
            capo_transcribe.types.category_properties_list.serialize_cbor(
                value["categories"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListCallAnalyticsCategoriesResponse:
    out: ListCallAnalyticsCategoriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Categories") is not None:
        import capo_transcribe.types.category_properties_list

        out["categories"] = (
            capo_transcribe.types.category_properties_list.deserialize_cbor(
                data["Categories"]
            )
        )
    return out

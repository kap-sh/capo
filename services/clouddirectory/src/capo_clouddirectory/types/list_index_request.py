"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.consistency_level
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results
    import capo_clouddirectory.types.object_attribute_range_list
    import capo_clouddirectory.types.object_reference


class ListIndexRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory that the index exists in.</p>"""
    ranges_on_indexed_values: NotRequired[
        "capo_clouddirectory.types.object_attribute_range_list.ObjectAttributeRangeList"
    ]
    """<p>Specifies the ranges of indexed values that you want to query.</p>"""
    index_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference to the index to list.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of objects in a single page to retrieve from the index during a request. For more information, see <a href="http://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html">Amazon Cloud Directory Limits</a>.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>The consistency level to execute the request at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexRequest) -> dict:
    out: dict = {}
    if "ranges_on_indexed_values" in value:
        import capo_clouddirectory.types.object_attribute_range_list

        out["RangesOnIndexedValues"] = (
            capo_clouddirectory.types.object_attribute_range_list.serialize_json(
                value["ranges_on_indexed_values"]
            )
        )
    import capo_clouddirectory.types.object_reference

    out["IndexReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["index_reference"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIndexRequest:
    out: ListIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("RangesOnIndexedValues") is not None:
        import capo_clouddirectory.types.object_attribute_range_list

        out["ranges_on_indexed_values"] = (
            capo_clouddirectory.types.object_attribute_range_list.deserialize_json(
                data["RangesOnIndexedValues"]
            )
        )
    if data.get("IndexReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["index_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["IndexReference"]
            )
        )
    else:
        raise DeserializationError("ListIndexRequest.index_reference required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

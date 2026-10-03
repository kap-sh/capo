"""Generated from Smithy shape ``com.amazonaws.kendra#Relevance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.document_metadata_boolean
    import capo_kendra.types.duration
    import capo_kendra.types.importance
    import capo_kendra.types.order
    import capo_kendra.types.value_importance_map


class Relevance(TypedDict, closed=True):
    freshness: NotRequired[
        "capo_kendra.types.document_metadata_boolean.DocumentMetadataBoolean"
    ]
    """<p>Indicates that this field determines how "fresh" a document is. For example, if document 1 was created on November 5, and document 2 was created on October 31, document 1 is "fresher" than document 2. Only applies to <code>DATE</code> fields.</p>"""
    importance: NotRequired["capo_kendra.types.importance.Importance"]
    """<p>The relative importance of the field in the search. Larger numbers provide more of a boost than smaller numbers.</p>"""
    duration: NotRequired["capo_kendra.types.duration.Duration"]
    """<p>Specifies the time period that the boost applies to. For example, to make the boost apply to documents with the field value within the last month, you would use "2628000s". Once the field value is beyond the specified range, the effect of the boost drops off. The higher the importance, the faster the effect drops off. If you don't specify a value, the default is 3 months. The value of the field is a numeric string followed by the character "s", for example "86400s" for one day, or "604800s" for one week. </p> <p>Only applies to <code>DATE</code> fields.</p>"""
    rank_order: NotRequired["capo_kendra.types.order.Order"]
    """<p>Determines how values should be interpreted.</p> <p>When the <code>RankOrder</code> field is <code>ASCENDING</code>, higher numbers are better. For example, a document with a rating score of 10 is higher ranking than a document with a rating score of 1.</p> <p>When the <code>RankOrder</code> field is <code>DESCENDING</code>, lower numbers are better. For example, in a task tracking application, a priority 1 task is more important than a priority 5 task.</p> <p>Only applies to <code>LONG</code> fields.</p>"""
    value_importance_map: NotRequired[
        "capo_kendra.types.value_importance_map.ValueImportanceMap"
    ]
    """<p>A list of values that should be given a different boost when they appear in the result list. For example, if you are boosting a field called "department", query terms that match the department field are boosted in the result. However, you can add entries from the department field to boost documents with those values higher. </p> <p>For example, you can add entries to the map with names of departments. If you add "HR",5 and "Legal",3 those departments are given special attention when they appear in the metadata of a document. When those terms appear they are given the specified importance instead of the regular importance for the boost.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Relevance) -> dict:
    out: dict = {}
    if "freshness" in value:
        out["Freshness"] = value["freshness"]
    if "importance" in value:
        out["Importance"] = value["importance"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "rank_order" in value:
        import capo_kendra.types.order

        out["RankOrder"] = capo_kendra.types.order.serialize_aws_json_1_1(
            value["rank_order"]
        )
    if "value_importance_map" in value:
        import capo_kendra.types.value_importance_map

        out["ValueImportanceMap"] = (
            capo_kendra.types.value_importance_map.serialize_aws_json_1_1(
                value["value_importance_map"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Relevance:
    out: Relevance = {}  # type: ignore[typeddict-item]
    if data.get("Freshness") is not None:
        out["freshness"] = data["Freshness"]
    if data.get("Importance") is not None:
        out["importance"] = data["Importance"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("RankOrder") is not None:
        import capo_kendra.types.order

        out["rank_order"] = capo_kendra.types.order.deserialize_aws_json_1_1(
            data["RankOrder"]
        )
    if data.get("ValueImportanceMap") is not None:
        import capo_kendra.types.value_importance_map

        out["value_importance_map"] = (
            capo_kendra.types.value_importance_map.deserialize_aws_json_1_1(
                data["ValueImportanceMap"]
            )
        )
    return out

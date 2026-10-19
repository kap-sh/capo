"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSchemaField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.content_type
    import capo_customer_profiles.types.feature_type
    import capo_customer_profiles.types.text


class RecommenderSchemaField(TypedDict, closed=True):
    target_field_name: "capo_customer_profiles.types.text.text"
    """<p>The name of the target field in the dataset, such as <code>Location.City</code> or <code>Attributes.MealTime</code>.</p>"""
    content_type: NotRequired["capo_customer_profiles.types.content_type.ContentType"]
    """<p>The data type of the column value. Valid values are <code>String</code> and <code>Number</code>. The default value is <code>String</code>.</p>"""
    feature_type: NotRequired["capo_customer_profiles.types.feature_type.FeatureType"]
    """<p>How the column is treated for model training. Valid values are <code>CATEGORICAL</code> and <code>TEXTUAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSchemaField) -> dict:
    out: dict = {}
    out["TargetFieldName"] = value["target_field_name"]
    if "content_type" in value:
        import capo_customer_profiles.types.content_type

        out["ContentType"] = capo_customer_profiles.types.content_type.serialize_json(
            value["content_type"]
        )
    if "feature_type" in value:
        import capo_customer_profiles.types.feature_type

        out["FeatureType"] = capo_customer_profiles.types.feature_type.serialize_json(
            value["feature_type"]
        )
    return out


def deserialize_json(data: dict) -> RecommenderSchemaField:
    out: RecommenderSchemaField = {}  # type: ignore[typeddict-item]
    if data.get("TargetFieldName") is not None:
        out["target_field_name"] = data["TargetFieldName"]
    else:
        out["target_field_name"] = ""
    if data.get("ContentType") is not None:
        import capo_customer_profiles.types.content_type

        out["content_type"] = (
            capo_customer_profiles.types.content_type.deserialize_json(
                data["ContentType"]
            )
        )
    if data.get("FeatureType") is not None:
        import capo_customer_profiles.types.feature_type

        out["feature_type"] = (
            capo_customer_profiles.types.feature_type.deserialize_json(
                data["FeatureType"]
            )
        )
    return out

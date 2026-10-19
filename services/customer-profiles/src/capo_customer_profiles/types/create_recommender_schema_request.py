"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_schema_fields
    import capo_customer_profiles.types.tag_map


class CreateRecommenderSchemaRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_schema_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender schema. The name must be unique within the domain.</p>"""
    fields: (
        "capo_customer_profiles.types.recommender_schema_fields.RecommenderSchemaFields"
    )
    """<p>A map of dataset type to column definitions that specifies which data columns to include in the schema. The <code>_webAnalytics</code> and <code>_catalogItem</code> keys are supported.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderSchemaRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.recommender_schema_fields

    out["Fields"] = (
        capo_customer_profiles.types.recommender_schema_fields.serialize_json(
            value["fields"]
        )
    )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecommenderSchemaRequest:
    out: CreateRecommenderSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("Fields") is not None:
        import capo_customer_profiles.types.recommender_schema_fields

        out["fields"] = (
            capo_customer_profiles.types.recommender_schema_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        out["fields"] = {}
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_config
    import capo_customer_profiles.types.recommender_recipe_name
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map


class CreateRecommenderRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender.</p>"""
    recommender_recipe_name: (
        "capo_customer_profiles.types.recommender_recipe_name.RecommenderRecipeName"
    )
    """<p>The name of the recommeder recipe.</p>"""
    recommender_config: NotRequired[
        "capo_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The recommender configuration.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the domain object type.</p>"""
    recommender_schema_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema to use for this recommender. If not specified, the default schema is used.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.recommender_recipe_name

    out["RecommenderRecipeName"] = (
        capo_customer_profiles.types.recommender_recipe_name.serialize_json(
            value["recommender_recipe_name"]
        )
    )
    if "recommender_config" in value:
        import capo_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            capo_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecommenderRequest:
    out: CreateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderRecipeName") is not None:
        import capo_customer_profiles.types.recommender_recipe_name

        out["recommender_recipe_name"] = (
            capo_customer_profiles.types.recommender_recipe_name.deserialize_json(
                data["RecommenderRecipeName"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRecommenderRequest.recommender_recipe_name required"
        )
    if data.get("RecommenderConfig") is not None:
        import capo_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            capo_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RecommenderSchemaName") is not None:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateRecommenderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

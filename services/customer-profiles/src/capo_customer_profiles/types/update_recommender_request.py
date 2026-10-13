"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateRecommenderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_config
    import capo_customer_profiles.types.recommender_version_name
    import capo_customer_profiles.types.sensitive_text


class UpdateRecommenderRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender to update.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The new description to assign to the recommender.</p>"""
    recommender_config: NotRequired[
        "capo_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The new configuration settings to apply to the recommender, including updated parameters and settings that define its behavior.</p>"""
    recommender_version_name: NotRequired[
        "capo_customer_profiles.types.recommender_version_name.RecommenderVersionName"
    ]
    """<p>The name of a specific recommender version to activate as part of this update (for example, to roll back to a previously trained version).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "recommender_config" in value:
        import capo_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            capo_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    if "recommender_version_name" in value:
        out["RecommenderVersionName"] = value["recommender_version_name"]
    return out


def deserialize_json(data: dict) -> UpdateRecommenderRequest:
    out: UpdateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RecommenderConfig") is not None:
        import capo_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            capo_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    if data.get("RecommenderVersionName") is not None:
        out["recommender_version_name"] = data["RecommenderVersionName"]
    return out


def redact_sensitive(value: UpdateRecommenderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

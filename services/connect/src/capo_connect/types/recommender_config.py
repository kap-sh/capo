"""Generated from Smithy shape ``com.amazonaws.connect#RecommenderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.personalize_domain_name
    import capo_connect.types.recommender_context
    import capo_connect.types.recommender_name


class RecommenderConfig(TypedDict, closed=True):
    domain_name: "capo_connect.types.personalize_domain_name.PersonalizeDomainName"
    """<p>The name of the Amazon Personalize domain that hosts the recommender.</p>"""
    recommender_name: "capo_connect.types.recommender_name.RecommenderName"
    """<p>The name of the recommender used to generate the recommendations.</p>"""
    context: NotRequired["capo_connect.types.recommender_context.RecommenderContext"]
    """<p>A map of contextual key-value pairs supplied to the recommender to influence the recommendations returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderConfig) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["RecommenderName"] = value["recommender_name"]
    if "context" in value:
        import capo_connect.types.recommender_context

        out["Context"] = capo_connect.types.recommender_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> RecommenderConfig:
    out: RecommenderConfig = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("RecommenderName") is not None:
        out["recommender_name"] = data["RecommenderName"]
    else:
        out["recommender_name"] = ""
    if data.get("Context") is not None:
        import capo_connect.types.recommender_context

        out["context"] = capo_connect.types.recommender_context.deserialize_json(
            data["Context"]
        )
    return out

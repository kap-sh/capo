"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#GetRecommendationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation


class GetRecommendationResponse(TypedDict, closed=True):
    recommendation: NotRequired[
        "capo_trustedadvisor.types.recommendation.Recommendation"
    ]
    """<p>The Recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationResponse) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import capo_trustedadvisor.types.recommendation

        out["recommendation"] = capo_trustedadvisor.types.recommendation.serialize_json(
            value["recommendation"]
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationResponse:
    out: GetRecommendationResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendation") is not None:
        import capo_trustedadvisor.types.recommendation

        out["recommendation"] = (
            capo_trustedadvisor.types.recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    return out


def redact_sensitive(value: GetRecommendationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendation" in value:
        import capo_trustedadvisor.types.recommendation

        out["recommendation"] = (
            capo_trustedadvisor.types.recommendation.redact_sensitive(
                value["recommendation"]
            )
        )
    return out

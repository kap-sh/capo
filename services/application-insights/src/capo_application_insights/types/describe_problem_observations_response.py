"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeProblemObservationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.related_observations


class DescribeProblemObservationsResponse(TypedDict, closed=True):
    related_observations: NotRequired[
        "capo_application_insights.types.related_observations.RelatedObservations"
    ]
    """<p>Observations related to the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProblemObservationsResponse) -> dict:
    out: dict = {}
    if "related_observations" in value:
        import capo_application_insights.types.related_observations

        out["RelatedObservations"] = (
            capo_application_insights.types.related_observations.serialize_aws_json_1_1(
                value["related_observations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProblemObservationsResponse:
    out: DescribeProblemObservationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RelatedObservations") is not None:
        import capo_application_insights.types.related_observations

        out["related_observations"] = (
            capo_application_insights.types.related_observations.deserialize_aws_json_1_1(
                data["RelatedObservations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProblemObservationsResponse) -> dict:
    out: dict = {}
    if "related_observations" in value:
        import capo_application_insights.types.related_observations

        out["RelatedObservations"] = (
            capo_application_insights.types.related_observations.serialize_cbor(
                value["related_observations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeProblemObservationsResponse:
    out: DescribeProblemObservationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RelatedObservations") is not None:
        import capo_application_insights.types.related_observations

        out["related_observations"] = (
            capo_application_insights.types.related_observations.deserialize_cbor(
                data["RelatedObservations"]
            )
        )
    return out

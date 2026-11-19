"""Generated from Smithy shape ``com.amazonaws.applicationinsights#RelatedObservations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.observation_list


class RelatedObservations(TypedDict, closed=True):
    observation_list: NotRequired[
        "capo_application_insights.types.observation_list.ObservationList"
    ]
    """<p>The list of observations related to the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedObservations) -> dict:
    out: dict = {}
    if "observation_list" in value:
        import capo_application_insights.types.observation_list

        out["ObservationList"] = (
            capo_application_insights.types.observation_list.serialize_aws_json_1_1(
                value["observation_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelatedObservations:
    out: RelatedObservations = {}  # type: ignore[typeddict-item]
    if data.get("ObservationList") is not None:
        import capo_application_insights.types.observation_list

        out["observation_list"] = (
            capo_application_insights.types.observation_list.deserialize_aws_json_1_1(
                data["ObservationList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RelatedObservations) -> dict:
    out: dict = {}
    if "observation_list" in value:
        import capo_application_insights.types.observation_list

        out["ObservationList"] = (
            capo_application_insights.types.observation_list.serialize_cbor(
                value["observation_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RelatedObservations:
    out: RelatedObservations = {}  # type: ignore[typeddict-item]
    if data.get("ObservationList") is not None:
        import capo_application_insights.types.observation_list

        out["observation_list"] = (
            capo_application_insights.types.observation_list.deserialize_cbor(
                data["ObservationList"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeObservationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.observation


class DescribeObservationResponse(TypedDict, closed=True):
    observation: NotRequired["capo_application_insights.types.observation.Observation"]
    """<p>Information about the observation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeObservationResponse) -> dict:
    out: dict = {}
    if "observation" in value:
        import capo_application_insights.types.observation

        out["Observation"] = (
            capo_application_insights.types.observation.serialize_aws_json_1_1(
                value["observation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeObservationResponse:
    out: DescribeObservationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Observation") is not None:
        import capo_application_insights.types.observation

        out["observation"] = (
            capo_application_insights.types.observation.deserialize_aws_json_1_1(
                data["Observation"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeObservationResponse) -> dict:
    out: dict = {}
    if "observation" in value:
        import capo_application_insights.types.observation

        out["Observation"] = capo_application_insights.types.observation.serialize_cbor(
            value["observation"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeObservationResponse:
    out: DescribeObservationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Observation") is not None:
        import capo_application_insights.types.observation

        out["observation"] = (
            capo_application_insights.types.observation.deserialize_cbor(
                data["Observation"]
            )
        )
    return out

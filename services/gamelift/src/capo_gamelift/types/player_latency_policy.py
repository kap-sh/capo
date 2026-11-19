"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerLatencyPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.whole_number


class PlayerLatencyPolicy(TypedDict, closed=True):
    maximum_individual_player_latency_milliseconds: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.</p>"""
    policy_duration_seconds: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerLatencyPolicy) -> dict:
    out: dict = {}
    if "maximum_individual_player_latency_milliseconds" in value:
        out["MaximumIndividualPlayerLatencyMilliseconds"] = value[
            "maximum_individual_player_latency_milliseconds"
        ]
    if "policy_duration_seconds" in value:
        out["PolicyDurationSeconds"] = value["policy_duration_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerLatencyPolicy:
    out: PlayerLatencyPolicy = {}  # type: ignore[typeddict-item]
    if data.get("MaximumIndividualPlayerLatencyMilliseconds") is not None:
        out["maximum_individual_player_latency_milliseconds"] = data[
            "MaximumIndividualPlayerLatencyMilliseconds"
        ]
    if data.get("PolicyDurationSeconds") is not None:
        out["policy_duration_seconds"] = data["PolicyDurationSeconds"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlayerLatencyPolicy) -> dict:
    out: dict = {}
    if "maximum_individual_player_latency_milliseconds" in value:
        out["MaximumIndividualPlayerLatencyMilliseconds"] = value[
            "maximum_individual_player_latency_milliseconds"
        ]
    if "policy_duration_seconds" in value:
        out["PolicyDurationSeconds"] = value["policy_duration_seconds"]
    return out


def deserialize_cbor(data: dict) -> PlayerLatencyPolicy:
    out: PlayerLatencyPolicy = {}  # type: ignore[typeddict-item]
    if data.get("MaximumIndividualPlayerLatencyMilliseconds") is not None:
        out["maximum_individual_player_latency_milliseconds"] = data[
            "MaximumIndividualPlayerLatencyMilliseconds"
        ]
    if data.get("PolicyDurationSeconds") is not None:
        out["policy_duration_seconds"] = data["PolicyDurationSeconds"]
    return out

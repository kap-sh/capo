"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerSupportabilityScoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_supportability_score_set
    import capo_ec2.types.supportability_score


class GetCapacityManagerSupportabilityScoresResult(TypedDict, closed=True):
    aggregate_score: NotRequired[
        "capo_ec2.types.supportability_score.SupportabilityScore"
    ]
    """<p> The score for all instance type and Availability Zone combinations in the request together. A <code>high</code> aggregate score with lower individual scores means that no single combination can support the full request, but the combinations together can. </p>"""
    capacity_manager_supportability_scores: NotRequired[
        "capo_ec2.types.capacity_manager_supportability_score_set.CapacityManagerSupportabilityScoreSet"
    ]
    """<p> The score for each instance type and Availability Zone combination in the request. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerSupportabilityScoresResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "aggregate_score" in value:
        import capo_ec2.types.supportability_score

        capo_ec2.types.supportability_score.serialize_ec2_query(
            value["aggregate_score"], pairs, f"{key_prefix}AggregateScore"
        )
    if "capacity_manager_supportability_scores" in value:
        import capo_ec2.types.capacity_manager_supportability_score_set

        capo_ec2.types.capacity_manager_supportability_score_set.serialize_ec2_query(
            value["capacity_manager_supportability_scores"],
            pairs,
            f"{key_prefix}CapacityManagerSupportabilityScoreSet",
        )


def deserialize_ec2_query(el: Element) -> GetCapacityManagerSupportabilityScoresResult:
    out: GetCapacityManagerSupportabilityScoresResult = {}  # type: ignore[typeddict-item]
    child_aggregate_score = el.find("aggregateScore")
    if child_aggregate_score is not None:
        import capo_ec2.types.supportability_score

        out["aggregate_score"] = (
            capo_ec2.types.supportability_score.deserialize_ec2_query(
                child_aggregate_score
            )
        )
    child_capacity_manager_supportability_scores = el.find(
        "capacityManagerSupportabilityScoreSet"
    )
    if child_capacity_manager_supportability_scores is not None:
        import capo_ec2.types.capacity_manager_supportability_score_set

        out["capacity_manager_supportability_scores"] = (
            capo_ec2.types.capacity_manager_supportability_score_set.deserialize_ec2_query(
                child_capacity_manager_supportability_scores
            )
        )
    return out

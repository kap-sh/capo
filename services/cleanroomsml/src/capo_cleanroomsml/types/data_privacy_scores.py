"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DataPrivacyScores``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.membership_inference_attack_score_list


class DataPrivacyScores(TypedDict, closed=True):
    membership_inference_attack_scores: "capo_cleanroomsml.types.membership_inference_attack_score_list.MembershipInferenceAttackScoreList"
    """<p>Scores that evaluate the vulnerability of the synthetic data to membership inference attacks, which attempt to determine whether a specific individual was a member of the original dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrivacyScores) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.membership_inference_attack_score_list

    out["membershipInferenceAttackScores"] = (
        capo_cleanroomsml.types.membership_inference_attack_score_list.serialize_json(
            value["membership_inference_attack_scores"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataPrivacyScores:
    out: DataPrivacyScores = {}  # type: ignore[typeddict-item]
    if data.get("membershipInferenceAttackScores") is not None:
        import capo_cleanroomsml.types.membership_inference_attack_score_list

        out["membership_inference_attack_scores"] = (
            capo_cleanroomsml.types.membership_inference_attack_score_list.deserialize_json(
                data["membershipInferenceAttackScores"]
            )
        )
    else:
        out["membership_inference_attack_scores"] = []
    return out

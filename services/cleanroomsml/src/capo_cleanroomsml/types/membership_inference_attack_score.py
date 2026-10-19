"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MembershipInferenceAttackScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.membership_inference_attack_version


class MembershipInferenceAttackScore(TypedDict, closed=True):
    attack_version: "capo_cleanroomsml.types.membership_inference_attack_version.MembershipInferenceAttackVersion"
    """<p>The version of the membership inference attack, which consists of the attack type and its version number, used to generate this privacy score.</p>"""
    score: "float"
    """<p>The numerical score representing the vulnerability to membership inference attacks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipInferenceAttackScore) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.membership_inference_attack_version

    out["attackVersion"] = (
        capo_cleanroomsml.types.membership_inference_attack_version.serialize_json(
            value["attack_version"]
        )
    )
    out["score"] = (
        "NaN"
        if value["score"] != value["score"]
        else "Infinity"
        if value["score"] == float("inf")
        else "-Infinity"
        if value["score"] == float("-inf")
        else value["score"]
    )
    return out


def deserialize_json(data: dict) -> MembershipInferenceAttackScore:
    out: MembershipInferenceAttackScore = {}  # type: ignore[typeddict-item]
    if data.get("attackVersion") is not None:
        import capo_cleanroomsml.types.membership_inference_attack_version

        out["attack_version"] = (
            capo_cleanroomsml.types.membership_inference_attack_version.deserialize_json(
                data["attackVersion"]
            )
        )
    else:
        import typing

        out["attack_version"] = typing.cast(
            "capo_cleanroomsml.types.membership_inference_attack_version.MembershipInferenceAttackVersion",
            "",
        )
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0.0
    return out

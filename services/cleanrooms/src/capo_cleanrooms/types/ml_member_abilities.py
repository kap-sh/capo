"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MLMemberAbilities``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.custom_ml_member_abilities


class MLMemberAbilities(TypedDict, closed=True):
    custom_ml_member_abilities: (
        "capo_cleanrooms.types.custom_ml_member_abilities.CustomMLMemberAbilities"
    )
    """<p>The custom ML member abilities for a collaboration member. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MLMemberAbilities) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.custom_ml_member_abilities

    out["customMLMemberAbilities"] = (
        capo_cleanrooms.types.custom_ml_member_abilities.serialize_json(
            value["custom_ml_member_abilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> MLMemberAbilities:
    out: MLMemberAbilities = {}  # type: ignore[typeddict-item]
    if data.get("customMLMemberAbilities") is not None:
        import capo_cleanrooms.types.custom_ml_member_abilities

        out["custom_ml_member_abilities"] = (
            capo_cleanrooms.types.custom_ml_member_abilities.deserialize_json(
                data["customMLMemberAbilities"]
            )
        )
    else:
        out["custom_ml_member_abilities"] = []
    return out

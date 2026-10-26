"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RecommendedStep``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.unused_permissions_recommended_step


class _RecommendedStep_unusedPermissionsRecommendedStep(TypedDict, closed=True):
    unusedPermissionsRecommendedStep: "capo_accessanalyzer.types.unused_permissions_recommended_step.UnusedPermissionsRecommendedStep"


RecommendedStep: TypeAlias = (
    _RecommendedStep_unusedPermissionsRecommendedStep | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedStep) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RecommendedStep: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "unusedPermissionsRecommendedStep" in value:
        import capo_accessanalyzer.types.unused_permissions_recommended_step

        return {
            "unusedPermissionsRecommendedStep": capo_accessanalyzer.types.unused_permissions_recommended_step.serialize_json(
                value["unusedPermissionsRecommendedStep"]
            )
        }
    else:
        raise SerializationError("RecommendedStep: no variant present")


def deserialize_json(data: dict) -> RecommendedStep:
    if data.get("unusedPermissionsRecommendedStep") is not None:
        import capo_accessanalyzer.types.unused_permissions_recommended_step

        return {
            "unusedPermissionsRecommendedStep": capo_accessanalyzer.types.unused_permissions_recommended_step.deserialize_json(
                data["unusedPermissionsRecommendedStep"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RecommendedStep: no recognized variant key")

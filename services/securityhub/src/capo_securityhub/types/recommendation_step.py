"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationStep``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.unused_permissions_recommendation_step


class _RecommendationStep_UnusedPermissions(TypedDict, closed=True):
    UnusedPermissions: "capo_securityhub.types.unused_permissions_recommendation_step.UnusedPermissionsRecommendationStep"


RecommendationStep: TypeAlias = (
    _RecommendationStep_UnusedPermissions | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStep) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RecommendationStep: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "UnusedPermissions" in value:
        import capo_securityhub.types.unused_permissions_recommendation_step

        return {
            "UnusedPermissions": capo_securityhub.types.unused_permissions_recommendation_step.serialize_json(
                value["UnusedPermissions"]
            )
        }
    else:
        raise SerializationError("RecommendationStep: no variant present")


def deserialize_json(data: dict) -> RecommendationStep:
    if data.get("UnusedPermissions") is not None:
        import capo_securityhub.types.unused_permissions_recommendation_step

        return {
            "UnusedPermissions": capo_securityhub.types.unused_permissions_recommendation_step.deserialize_json(
                data["UnusedPermissions"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RecommendationStep: no recognized variant key")

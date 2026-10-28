"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportPreferences``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_discovery_service.errors import (
    DeserializationError,
    SerializationError,
)
from capo_application_discovery_service.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_discovery_service.types.ec2_recommendations_export_preferences


class ExportPreferencesEc2RecommendationsPreferencesMember(TypedDict, closed=True):
    ec2RecommendationsPreferences: "capo_application_discovery_service.types.ec2_recommendations_export_preferences.Ec2RecommendationsExportPreferences"


ExportPreferences: TypeAlias = (
    ExportPreferencesEc2RecommendationsPreferencesMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportPreferences) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExportPreferences: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ec2RecommendationsPreferences" in value:
        import capo_application_discovery_service.types.ec2_recommendations_export_preferences

        return {
            "ec2RecommendationsPreferences": capo_application_discovery_service.types.ec2_recommendations_export_preferences.serialize_aws_json_1_1(
                value["ec2RecommendationsPreferences"]
            )
        }
    else:
        raise SerializationError("ExportPreferences: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ExportPreferences:
    if data.get("ec2RecommendationsPreferences") is not None:
        import capo_application_discovery_service.types.ec2_recommendations_export_preferences

        return {
            "ec2RecommendationsPreferences": capo_application_discovery_service.types.ec2_recommendations_export_preferences.deserialize_aws_json_1_1(
                data["ec2RecommendationsPreferences"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExportPreferences: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorAdditionalConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.feature_additional_configuration
    import capo_guardduty.types.feature_status
    import capo_guardduty.types.managed_by
    import capo_guardduty.types.timestamp


class DetectorAdditionalConfigurationResult(TypedDict, closed=True):
    name: NotRequired[
        "capo_guardduty.types.feature_additional_configuration.FeatureAdditionalConfiguration"
    ]
    """<p>Name of the additional configuration.</p>"""
    status: NotRequired["capo_guardduty.types.feature_status.FeatureStatus"]
    """<p>Status of the additional configuration.</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the additional configuration was last updated. This is in UTC format.</p>"""
    managed_by: NotRequired["capo_guardduty.types.managed_by.ManagedBy"]
    """<p>Indicates what manages the additional configuration. A value of <code>GUARDDUTY_POLICY</code> means a GuardDuty policy manages the additional configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorAdditionalConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_guardduty.types.feature_additional_configuration

        out["name"] = (
            capo_guardduty.types.feature_additional_configuration.serialize_json(
                value["name"]
            )
        )
    if "status" in value:
        import capo_guardduty.types.feature_status

        out["status"] = capo_guardduty.types.feature_status.serialize_json(
            value["status"]
        )
    if "updated_at" in value:
        import capo_guardduty.types.timestamp

        out["updatedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "managed_by" in value:
        import capo_guardduty.types.managed_by

        out["managedBy"] = capo_guardduty.types.managed_by.serialize_json(
            value["managed_by"]
        )
    return out


def deserialize_json(data: dict) -> DetectorAdditionalConfigurationResult:
    out: DetectorAdditionalConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_guardduty.types.feature_additional_configuration

        out["name"] = (
            capo_guardduty.types.feature_additional_configuration.deserialize_json(
                data["name"]
            )
        )
    if data.get("status") is not None:
        import capo_guardduty.types.feature_status

        out["status"] = capo_guardduty.types.feature_status.deserialize_json(
            data["status"]
        )
    if data.get("updatedAt") is not None:
        import capo_guardduty.types.timestamp

        out["updated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("managedBy") is not None:
        import capo_guardduty.types.managed_by

        out["managed_by"] = capo_guardduty.types.managed_by.deserialize_json(
            data["managedBy"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberFeaturesConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.feature_status
    import capo_guardduty.types.managed_by
    import capo_guardduty.types.member_additional_configuration_results
    import capo_guardduty.types.org_feature
    import capo_guardduty.types.timestamp


class MemberFeaturesConfigurationResult(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.org_feature.OrgFeature"]
    """<p>Indicates the name of the feature that is enabled for the detector.</p>"""
    status: NotRequired["capo_guardduty.types.feature_status.FeatureStatus"]
    """<p>Indicates the status of the feature that is enabled for the detector.</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the feature object was updated.</p>"""
    additional_configuration: NotRequired[
        "capo_guardduty.types.member_additional_configuration_results.MemberAdditionalConfigurationResults"
    ]
    """<p>Indicates the additional configuration of the feature that is configured for the member account.</p>"""
    managed_by: NotRequired["capo_guardduty.types.managed_by.ManagedBy"]
    """<p>Indicates what manages the feature. A value of <code>GUARDDUTY_POLICY</code> means a GuardDuty policy manages the feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFeaturesConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_guardduty.types.org_feature

        out["name"] = capo_guardduty.types.org_feature.serialize_json(value["name"])
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
    if "additional_configuration" in value:
        import capo_guardduty.types.member_additional_configuration_results

        out["additionalConfiguration"] = (
            capo_guardduty.types.member_additional_configuration_results.serialize_json(
                value["additional_configuration"]
            )
        )
    if "managed_by" in value:
        import capo_guardduty.types.managed_by

        out["managedBy"] = capo_guardduty.types.managed_by.serialize_json(
            value["managed_by"]
        )
    return out


def deserialize_json(data: dict) -> MemberFeaturesConfigurationResult:
    out: MemberFeaturesConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_guardduty.types.org_feature

        out["name"] = capo_guardduty.types.org_feature.deserialize_json(data["name"])
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
    if data.get("additionalConfiguration") is not None:
        import capo_guardduty.types.member_additional_configuration_results

        out["additional_configuration"] = (
            capo_guardduty.types.member_additional_configuration_results.deserialize_json(
                data["additionalConfiguration"]
            )
        )
    if data.get("managedBy") is not None:
        import capo_guardduty.types.managed_by

        out["managed_by"] = capo_guardduty.types.managed_by.deserialize_json(
            data["managedBy"]
        )
    return out

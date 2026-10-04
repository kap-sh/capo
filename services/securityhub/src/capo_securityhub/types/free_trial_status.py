"""Generated from Smithy shape ``com.amazonaws.securityhub#FreeTrialStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.free_trial_status_value
    import capo_securityhub.types.free_trial_type
    import capo_securityhub.types.timestamp


class FreeTrialStatus(TypedDict, closed=True):
    feature_type: NotRequired["capo_securityhub.types.free_trial_type.FreeTrialType"]
    """<p>The feature that the free trial period applies to. Valid values:</p> <ul> <li> <p> <code>SECURITY_HUB_V2</code> specifies Security Hub.</p> </li> <li> <p> <code>SECURITY_HUB_V2_MULTI_CLOUD_AZURE</code> specifies Security Hub coverage for Microsoft Azure resources.</p> </li> </ul>"""
    status: NotRequired[
        "capo_securityhub.types.free_trial_status_value.FreeTrialStatusValue"
    ]
    """<p>Specifies whether the free trial period is currently active. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> specifies that the free trial period is ongoing.</p> </li> <li> <p> <code>INACTIVE</code> specifies that the free trial period has ended, or that it never started.</p> </li> </ul> <p>To determine whether a trial has expired, compare <code>ExpiresAt</code> to the current time.</p>"""
    started_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The date and time at which the free trial period began.</p>"""
    expires_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The date and time at which the free trial period ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialStatus) -> dict:
    out: dict = {}
    if "feature_type" in value:
        import capo_securityhub.types.free_trial_type

        out["FeatureType"] = capo_securityhub.types.free_trial_type.serialize_json(
            value["feature_type"]
        )
    if "status" in value:
        import capo_securityhub.types.free_trial_status_value

        out["Status"] = capo_securityhub.types.free_trial_status_value.serialize_json(
            value["status"]
        )
    if "started_at" in value:
        import capo_securityhub.types.timestamp

        out["StartedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "expires_at" in value:
        import capo_securityhub.types.timestamp

        out["ExpiresAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> FreeTrialStatus:
    out: FreeTrialStatus = {}  # type: ignore[typeddict-item]
    if data.get("FeatureType") is not None:
        import capo_securityhub.types.free_trial_type

        out["feature_type"] = capo_securityhub.types.free_trial_type.deserialize_json(
            data["FeatureType"]
        )
    if data.get("Status") is not None:
        import capo_securityhub.types.free_trial_status_value

        out["status"] = capo_securityhub.types.free_trial_status_value.deserialize_json(
            data["Status"]
        )
    if data.get("StartedAt") is not None:
        import capo_securityhub.types.timestamp

        out["started_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["StartedAt"]
        )
    if data.get("ExpiresAt") is not None:
        import capo_securityhub.types.timestamp

        out["expires_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["ExpiresAt"]
        )
    return out

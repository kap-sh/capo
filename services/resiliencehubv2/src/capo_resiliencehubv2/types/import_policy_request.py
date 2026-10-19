"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ImportPolicyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.availability_slo
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.multi_az_disaster_recovery_approach
    import capo_resiliencehubv2.types.multi_region_disaster_recovery_approach
    import capo_resiliencehubv2.types.tag_map


class ImportPolicyRequest(TypedDict, closed=True):
    v1_policy_arn: "capo_resiliencehubv2.types.arn.Arn"
    kms_key_id: NotRequired["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    availability_slo: NotRequired[
        "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The availability SLO to set on the imported policy.</p>"""
    multi_az_disaster_recovery_approach: NotRequired[
        "capo_resiliencehubv2.types.multi_az_disaster_recovery_approach.MultiAzDisasterRecoveryApproach"
    ]
    """<p>The multi-AZ disaster recovery approach for the imported policy.</p>"""
    multi_region_disaster_recovery_approach: NotRequired[
        "capo_resiliencehubv2.types.multi_region_disaster_recovery_approach.MultiRegionDisasterRecoveryApproach"
    ]
    """<p>The multi-Region disaster recovery approach for the imported policy.</p>"""
    tags: NotRequired["capo_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportPolicyRequest) -> dict:
    out: dict = {}
    out["v1PolicyArn"] = value["v1_policy_arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "availability_slo" in value:
        import capo_resiliencehubv2.types.availability_slo

        out["availabilitySlo"] = (
            capo_resiliencehubv2.types.availability_slo.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az_disaster_recovery_approach" in value:
        import capo_resiliencehubv2.types.multi_az_disaster_recovery_approach

        out["multiAzDisasterRecoveryApproach"] = (
            capo_resiliencehubv2.types.multi_az_disaster_recovery_approach.serialize_json(
                value["multi_az_disaster_recovery_approach"]
            )
        )
    if "multi_region_disaster_recovery_approach" in value:
        import capo_resiliencehubv2.types.multi_region_disaster_recovery_approach

        out["multiRegionDisasterRecoveryApproach"] = (
            capo_resiliencehubv2.types.multi_region_disaster_recovery_approach.serialize_json(
                value["multi_region_disaster_recovery_approach"]
            )
        )
    if "tags" in value:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportPolicyRequest:
    out: ImportPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("v1PolicyArn") is not None:
        out["v1_policy_arn"] = data["v1PolicyArn"]
    else:
        out["v1_policy_arn"] = ""
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("availabilitySlo") is not None:
        import capo_resiliencehubv2.types.availability_slo

        out["availability_slo"] = (
            capo_resiliencehubv2.types.availability_slo.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if data.get("multiAzDisasterRecoveryApproach") is not None:
        import capo_resiliencehubv2.types.multi_az_disaster_recovery_approach

        out["multi_az_disaster_recovery_approach"] = (
            capo_resiliencehubv2.types.multi_az_disaster_recovery_approach.deserialize_json(
                data["multiAzDisasterRecoveryApproach"]
            )
        )
    if data.get("multiRegionDisasterRecoveryApproach") is not None:
        import capo_resiliencehubv2.types.multi_region_disaster_recovery_approach

        out["multi_region_disaster_recovery_approach"] = (
            capo_resiliencehubv2.types.multi_region_disaster_recovery_approach.deserialize_json(
                data["multiRegionDisasterRecoveryApproach"]
            )
        )
    if data.get("tags") is not None:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: ImportPolicyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreatePolicyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.availability_slo
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.data_recovery_targets
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.long_description
    import capo_resiliencehubv2.types.multi_az_targets
    import capo_resiliencehubv2.types.multi_region_targets
    import capo_resiliencehubv2.types.tag_map


class CreatePolicyRequest(TypedDict, closed=True):
    name: "capo_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "capo_resiliencehubv2.types.long_description.LongDescription"
    ]
    availability_slo: NotRequired[
        "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The availability SLO for the resilience policy.</p>"""
    multi_az: NotRequired["capo_resiliencehubv2.types.multi_az_targets.MultiAzTargets"]
    """<p>The multi-AZ disaster recovery targets for the resilience policy.</p>"""
    multi_region: NotRequired[
        "capo_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
    ]
    """<p>The multi-Region disaster recovery targets for the resilience policy.</p>"""
    data_recovery: NotRequired[
        "capo_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
    ]
    """<p>The data recovery targets for the resilience policy.</p>"""
    sharing_enabled: NotRequired["bool"]
    """<p>Specifies whether cross-account sharing is enabled for the policy. Only a delegated administrator or the management account can enable sharing.</p>"""
    kms_key_id: NotRequired["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    tags: NotRequired["capo_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "availability_slo" in value:
        import capo_resiliencehubv2.types.availability_slo

        out["availabilitySlo"] = (
            capo_resiliencehubv2.types.availability_slo.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az" in value:
        import capo_resiliencehubv2.types.multi_az_targets

        out["multiAz"] = capo_resiliencehubv2.types.multi_az_targets.serialize_json(
            value["multi_az"]
        )
    if "multi_region" in value:
        import capo_resiliencehubv2.types.multi_region_targets

        out["multiRegion"] = (
            capo_resiliencehubv2.types.multi_region_targets.serialize_json(
                value["multi_region"]
            )
        )
    if "data_recovery" in value:
        import capo_resiliencehubv2.types.data_recovery_targets

        out["dataRecovery"] = (
            capo_resiliencehubv2.types.data_recovery_targets.serialize_json(
                value["data_recovery"]
            )
        )
    if "sharing_enabled" in value:
        out["sharingEnabled"] = value["sharing_enabled"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePolicyRequest:
    out: CreatePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("availabilitySlo") is not None:
        import capo_resiliencehubv2.types.availability_slo

        out["availability_slo"] = (
            capo_resiliencehubv2.types.availability_slo.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if data.get("multiAz") is not None:
        import capo_resiliencehubv2.types.multi_az_targets

        out["multi_az"] = capo_resiliencehubv2.types.multi_az_targets.deserialize_json(
            data["multiAz"]
        )
    if data.get("multiRegion") is not None:
        import capo_resiliencehubv2.types.multi_region_targets

        out["multi_region"] = (
            capo_resiliencehubv2.types.multi_region_targets.deserialize_json(
                data["multiRegion"]
            )
        )
    if data.get("dataRecovery") is not None:
        import capo_resiliencehubv2.types.data_recovery_targets

        out["data_recovery"] = (
            capo_resiliencehubv2.types.data_recovery_targets.deserialize_json(
                data["dataRecovery"]
            )
        )
    if data.get("sharingEnabled") is not None:
        out["sharing_enabled"] = data["sharingEnabled"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_resiliencehubv2.types.tag_map

        out["tags"] = capo_resiliencehubv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreatePolicyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out

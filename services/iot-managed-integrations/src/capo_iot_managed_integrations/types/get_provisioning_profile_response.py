"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetProvisioningProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.claim_certificate
    import capo_iot_managed_integrations.types.provisioning_profile_arn
    import capo_iot_managed_integrations.types.provisioning_profile_id
    import capo_iot_managed_integrations.types.provisioning_profile_name
    import capo_iot_managed_integrations.types.provisioning_profile_status
    import capo_iot_managed_integrations.types.provisioning_type
    import capo_iot_managed_integrations.types.tags_map


class GetProvisioningProfileResponse(TypedDict, closed=True):
    arn: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_arn.ProvisioningProfileArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the provisioning profile.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
    ]
    """<p>The name of the provisioning profile.</p>"""
    provisioning_type: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_type.ProvisioningType"
    ]
    """<p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>"""
    id: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId"
    ]
    """<p>The provisioning profile id.</p>"""
    status: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_status.ProvisioningProfileStatus"
    ]
    """<p>The status of a provisioning profile.</p>"""
    claim_certificate: NotRequired[
        "capo_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
    ]
    """<p>The body of the PEM-encoded claim certificate.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the provisioning profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProvisioningProfileResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "provisioning_type" in value:
        import capo_iot_managed_integrations.types.provisioning_type

        out["ProvisioningType"] = (
            capo_iot_managed_integrations.types.provisioning_type.serialize_json(
                value["provisioning_type"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_iot_managed_integrations.types.provisioning_profile_status

        out["Status"] = (
            capo_iot_managed_integrations.types.provisioning_profile_status.serialize_json(
                value["status"]
            )
        )
    if "claim_certificate" in value:
        out["ClaimCertificate"] = value["claim_certificate"]
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetProvisioningProfileResponse:
    out: GetProvisioningProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ProvisioningType") is not None:
        import capo_iot_managed_integrations.types.provisioning_type

        out["provisioning_type"] = (
            capo_iot_managed_integrations.types.provisioning_type.deserialize_json(
                data["ProvisioningType"]
            )
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_iot_managed_integrations.types.provisioning_profile_status

        out["status"] = (
            capo_iot_managed_integrations.types.provisioning_profile_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ClaimCertificate") is not None:
        out["claim_certificate"] = data["ClaimCertificate"]
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetProvisioningProfileResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "claim_certificate" in value:
        out["claim_certificate"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateProvisioningProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.ca_certificate
    import capo_iot_managed_integrations.types.claim_certificate
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.provisioning_profile_name
    import capo_iot_managed_integrations.types.provisioning_type
    import capo_iot_managed_integrations.types.tags_map


class CreateProvisioningProfileRequest(TypedDict, closed=True):
    provisioning_type: (
        "capo_iot_managed_integrations.types.provisioning_type.ProvisioningType"
    )
    """<p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>"""
    ca_certificate: NotRequired[
        "capo_iot_managed_integrations.types.ca_certificate.CaCertificate"
    ]
    """<p>The body of the PEM-encoded certificate authority (CA) certificate.</p>"""
    claim_certificate: NotRequired[
        "capo_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
    ]
    """<p>The body of the PEM-encoded claim certificate. If a claim certificate is provided, it will be used for the provisioning profile. Otherwise, a claim certificate will be generated.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
    ]
    """<p>The name of the provisioning profile.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the provisioning profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningProfileRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.provisioning_type

    out["ProvisioningType"] = (
        capo_iot_managed_integrations.types.provisioning_type.serialize_json(
            value["provisioning_type"]
        )
    )
    if "ca_certificate" in value:
        out["CaCertificate"] = value["ca_certificate"]
    if "claim_certificate" in value:
        out["ClaimCertificate"] = value["claim_certificate"]
    if "name" in value:
        out["Name"] = value["name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateProvisioningProfileRequest:
    out: CreateProvisioningProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningType") is not None:
        import capo_iot_managed_integrations.types.provisioning_type

        out["provisioning_type"] = (
            capo_iot_managed_integrations.types.provisioning_type.deserialize_json(
                data["ProvisioningType"]
            )
        )
    else:
        import typing

        out["provisioning_type"] = typing.cast(
            "capo_iot_managed_integrations.types.provisioning_type.ProvisioningType", ""
        )
    if data.get("CaCertificate") is not None:
        out["ca_certificate"] = data["CaCertificate"]
    if data.get("ClaimCertificate") is not None:
        out["claim_certificate"] = data["ClaimCertificate"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateProvisioningProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ca_certificate" in value:
        out["ca_certificate"] = "*** Sensitive Data Redacted ***"
    if "claim_certificate" in value:
        out["claim_certificate"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out

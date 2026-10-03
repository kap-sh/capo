"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#SpekeKeyProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.content_key_period_configuration
    import capo_mediapackagev2.types.drm_systems
    import capo_mediapackagev2.types.encryption_contract_configuration
    import capo_mediapackagev2.types.speke_version


class SpekeKeyProvider(TypedDict, closed=True):
    encryption_contract_configuration: "capo_mediapackagev2.types.encryption_contract_configuration.EncryptionContractConfiguration"
    """<p>Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.</p>"""
    resource_id: "str"
    """<p>The unique identifier for the content. The service sends this to the key server to identify the current endpoint. How unique you make this depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.</p> <p>The following example shows a resource ID: <code>MovieNight20171126093045</code> </p>"""
    drm_systems: "capo_mediapackagev2.types.drm_systems.DrmSystems"
    """<p>The DRM solution provider you're using to protect your content during distribution.</p>"""
    role_arn: "str"
    """<p>The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.</p> <p>Valid format: <code>arn:aws:iam::{accountID}:role/{name}</code>. The following example shows a role ARN: <code>arn:aws:iam::444455556666:role/SpekeAccess</code> </p>"""
    url: "str"
    """<p>The URL of the API Gateway proxy that you set up to talk to your key server. The API Gateway proxy must reside in the same AWS Region as MediaPackage and must start with https://.</p> <p>The following example shows a URL: <code>https://1wm2dx1f33.execute-api.us-west-2.amazonaws.com/SpekeSample/copyProtection</code> </p>"""
    certificate_arn: NotRequired["str"]
    """<p>The ARN for the certificate that you imported to Amazon Web Services Certificate Manager to add content key encryption to this endpoint. For this feature to work, your DRM key provider must support content key encryption.</p>"""
    speke_version: NotRequired["capo_mediapackagev2.types.speke_version.SpekeVersion"]
    """<p>Specifies the SPEKE version used with your DRM key provider. If you don't specify a value, the default is <code>V2_0</code>.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>V2_0</code> - Follows the SPEKE Version 2.0 contract and signals only the content key index in key requests. This is the default.</p> </li> <li> <p> <code>V2_1</code> - Follows the SPEKE Version 2.1 contract and additionally supports signaling the start and end times a content key is used for, using <code>ContentKeyPeriodConfiguration</code>.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/speke/latest/documentation/standard-payload-components-v2.html">SPEKE Version 2.0 payload</a>.</p>"""
    content_key_period_configuration: NotRequired[
        "capo_mediapackagev2.types.content_key_period_configuration.ContentKeyPeriodConfiguration"
    ]
    """<p>The configuration that controls whether MediaPackage signals the start and end times a content key is used for, in the <code>ContentKeyPeriod</code> sent to your DRM key provider. Signaling this timing is supported only when key rotation is enabled (<code>KeyRotationIntervalSeconds</code> is set to a non-zero value) and <code>SpekeVersion</code> is <code>V2_1</code>. You can update these settings on an existing origin endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpekeKeyProvider) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types.encryption_contract_configuration

    out["EncryptionContractConfiguration"] = (
        capo_mediapackagev2.types.encryption_contract_configuration.serialize_json(
            value["encryption_contract_configuration"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import capo_mediapackagev2.types.drm_systems

    out["DrmSystems"] = capo_mediapackagev2.types.drm_systems.serialize_json(
        value["drm_systems"]
    )
    out["RoleArn"] = value["role_arn"]
    out["Url"] = value["url"]
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "speke_version" in value:
        import capo_mediapackagev2.types.speke_version

        out["SpekeVersion"] = capo_mediapackagev2.types.speke_version.serialize_json(
            value["speke_version"]
        )
    if "content_key_period_configuration" in value:
        import capo_mediapackagev2.types.content_key_period_configuration

        out["ContentKeyPeriodConfiguration"] = (
            capo_mediapackagev2.types.content_key_period_configuration.serialize_json(
                value["content_key_period_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpekeKeyProvider:
    out: SpekeKeyProvider = {}  # type: ignore[typeddict-item]
    if data.get("EncryptionContractConfiguration") is not None:
        import capo_mediapackagev2.types.encryption_contract_configuration

        out["encryption_contract_configuration"] = (
            capo_mediapackagev2.types.encryption_contract_configuration.deserialize_json(
                data["EncryptionContractConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SpekeKeyProvider.encryption_contract_configuration required"
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("SpekeKeyProvider.resource_id required")
    if data.get("DrmSystems") is not None:
        import capo_mediapackagev2.types.drm_systems

        out["drm_systems"] = capo_mediapackagev2.types.drm_systems.deserialize_json(
            data["DrmSystems"]
        )
    else:
        raise DeserializationError("SpekeKeyProvider.drm_systems required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("SpekeKeyProvider.role_arn required")
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("SpekeKeyProvider.url required")
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("SpekeVersion") is not None:
        import capo_mediapackagev2.types.speke_version

        out["speke_version"] = capo_mediapackagev2.types.speke_version.deserialize_json(
            data["SpekeVersion"]
        )
    if data.get("ContentKeyPeriodConfiguration") is not None:
        import capo_mediapackagev2.types.content_key_period_configuration

        out["content_key_period_configuration"] = (
            capo_mediapackagev2.types.content_key_period_configuration.deserialize_json(
                data["ContentKeyPeriodConfiguration"]
            )
        )
    return out

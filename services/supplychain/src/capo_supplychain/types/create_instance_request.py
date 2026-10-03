"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.client_token
    import capo_supplychain.types.instance_description
    import capo_supplychain.types.instance_name
    import capo_supplychain.types.instance_web_app_dns_domain
    import capo_supplychain.types.kms_key_arn
    import capo_supplychain.types.tag_map


class CreateInstanceRequest(TypedDict, closed=True):
    instance_name: NotRequired["capo_supplychain.types.instance_name.InstanceName"]
    """<p>The AWS Supply Chain instance name.</p>"""
    instance_description: NotRequired[
        "capo_supplychain.types.instance_description.InstanceDescription"
    ]
    """<p>The AWS Supply Chain instance description.</p>"""
    kms_key_arn: NotRequired["capo_supplychain.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon Web Services owned KMS key. If you don't provide anything here, AWS Supply Chain uses the Amazon Web Services owned KMS key.</p>"""
    web_app_dns_domain: NotRequired[
        "capo_supplychain.types.instance_web_app_dns_domain.InstanceWebAppDnsDomain"
    ]
    """<p>The DNS subdomain of the web app. This would be "example" in the URL "example.scn.global.on.aws". You can set this to a custom value, as long as the domain isn't already being used by someone else. The name may only include alphanumeric characters and hyphens.</p>"""
    tags: NotRequired["capo_supplychain.types.tag_map.TagMap"]
    """<p>The Amazon Web Services tags of an instance to be created.</p>"""
    client_token: NotRequired["capo_supplychain.types.client_token.ClientToken"]
    """<p>The client token for idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInstanceRequest) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "instance_description" in value:
        out["instanceDescription"] = value["instance_description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "web_app_dns_domain" in value:
        out["webAppDnsDomain"] = value["web_app_dns_domain"]
    if "tags" in value:
        import capo_supplychain.types.tag_map

        out["tags"] = capo_supplychain.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateInstanceRequest:
    out: CreateInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    if data.get("instanceDescription") is not None:
        out["instance_description"] = data["instanceDescription"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("webAppDnsDomain") is not None:
        out["web_app_dns_domain"] = data["webAppDnsDomain"]
    if data.get("tags") is not None:
        import capo_supplychain.types.tag_map

        out["tags"] = capo_supplychain.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

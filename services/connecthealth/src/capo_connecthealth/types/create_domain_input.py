"""Generated from Smithy shape ``com.amazonaws.connecthealth#CreateDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.create_web_app_configuration
    import capo_connecthealth.types.domain_name
    import capo_connecthealth.types.kms_key_arn
    import capo_connecthealth.types.tag_map


class CreateDomainInput(TypedDict, closed=True):
    name: "capo_connecthealth.types.domain_name.DomainName"
    """<p>The name for the new Domain.</p>"""
    kms_key_arn: NotRequired["capo_connecthealth.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key to use for encrypting data in this Domain.</p>"""
    web_app_setup_configuration: NotRequired[
        "capo_connecthealth.types.create_web_app_configuration.CreateWebAppConfiguration"
    ]
    """<p>Configuration for the Domain web application. Optional, but if provided all fields are required.</p>"""
    tags: NotRequired["capo_connecthealth.types.tag_map.TagMap"]
    """<p>Tags to associate with the Domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "web_app_setup_configuration" in value:
        import capo_connecthealth.types.create_web_app_configuration

        out["webAppSetupConfiguration"] = (
            capo_connecthealth.types.create_web_app_configuration.serialize_json(
                value["web_app_setup_configuration"]
            )
        )
    if "tags" in value:
        import capo_connecthealth.types.tag_map

        out["tags"] = capo_connecthealth.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDomainInput:
    out: CreateDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("webAppSetupConfiguration") is not None:
        import capo_connecthealth.types.create_web_app_configuration

        out["web_app_setup_configuration"] = (
            capo_connecthealth.types.create_web_app_configuration.deserialize_json(
                data["webAppSetupConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_connecthealth.types.tag_map

        out["tags"] = capo_connecthealth.types.tag_map.deserialize_json(data["tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.domain_arn
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.domain_name
    import capo_connecthealth.types.domain_status
    import capo_connecthealth.types.encryption_context
    import capo_connecthealth.types.kms_key_arn
    import capo_connecthealth.types.tag_map
    import capo_connecthealth.types.web_app_configuration
    import capo_connecthealth.types.web_app_url


class GetDomainOutput(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p/>"""
    arn: "capo_connecthealth.types.domain_arn.DomainArn"
    """<p/>"""
    name: "capo_connecthealth.types.domain_name.DomainName"
    """<p/>"""
    kms_key_arn: NotRequired["capo_connecthealth.types.kms_key_arn.KmsKeyArn"]
    """<p/>"""
    encryption_context: NotRequired[
        "capo_connecthealth.types.encryption_context.EncryptionContext"
    ]
    """<p/>"""
    status: "capo_connecthealth.types.domain_status.DomainStatus"
    """<p/>"""
    web_app_url: NotRequired["capo_connecthealth.types.web_app_url.WebAppUrl"]
    """<p/>"""
    web_app_configuration: NotRequired[
        "capo_connecthealth.types.web_app_configuration.WebAppConfiguration"
    ]
    """<p/>"""
    created_at: "datetime.datetime"
    """<p/>"""
    tags: NotRequired["capo_connecthealth.types.tag_map.TagMap"]
    """<p>Tags associated with the Domain</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "encryption_context" in value:
        import capo_connecthealth.types.encryption_context

        out["encryptionContext"] = (
            capo_connecthealth.types.encryption_context.serialize_json(
                value["encryption_context"]
            )
        )
    import capo_connecthealth.types.domain_status

    out["status"] = capo_connecthealth.types.domain_status.serialize_json(
        value["status"]
    )
    if "web_app_url" in value:
        out["webAppUrl"] = value["web_app_url"]
    if "web_app_configuration" in value:
        import capo_connecthealth.types.web_app_configuration

        out["webAppConfiguration"] = (
            capo_connecthealth.types.web_app_configuration.serialize_json(
                value["web_app_configuration"]
            )
        )
    import capo_connecthealth.types._prelude.timestamp

    out["createdAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "tags" in value:
        import capo_connecthealth.types.tag_map

        out["tags"] = capo_connecthealth.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDomainOutput:
    out: GetDomainOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("encryptionContext") is not None:
        import capo_connecthealth.types.encryption_context

        out["encryption_context"] = (
            capo_connecthealth.types.encryption_context.deserialize_json(
                data["encryptionContext"]
            )
        )
    if data.get("status") is not None:
        import capo_connecthealth.types.domain_status

        out["status"] = capo_connecthealth.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connecthealth.types.domain_status.DomainStatus", ""
        )
    if data.get("webAppUrl") is not None:
        out["web_app_url"] = data["webAppUrl"]
    if data.get("webAppConfiguration") is not None:
        import capo_connecthealth.types.web_app_configuration

        out["web_app_configuration"] = (
            capo_connecthealth.types.web_app_configuration.deserialize_json(
                data["webAppConfiguration"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["created_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("tags") is not None:
        import capo_connecthealth.types.tag_map

        out["tags"] = capo_connecthealth.types.tag_map.deserialize_json(data["tags"])
    return out

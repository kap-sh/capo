"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.date
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.string_with_char_limit1024


class RemediationException(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule.</p>"""
    resource_type: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The type of a resource.</p>"""
    resource_id: (
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    )
    """<p>The ID of the resource (for example., sg-xxxxxx).</p>"""
    message: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>An explanation of an remediation exception.</p>"""
    expiration_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time when the remediation exception will be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationException) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    out["ResourceType"] = value["resource_type"]
    out["ResourceId"] = value["resource_id"]
    if "message" in value:
        out["Message"] = value["message"]
    if "expiration_time" in value:
        import capo_config_service.types.date

        out["ExpirationTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["expiration_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationException:
    out: RemediationException = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ExpirationTime") is not None:
        import capo_config_service.types.date

        out["expiration_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    return out

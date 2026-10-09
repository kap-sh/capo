"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisterServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.kms_key_arn
    import capo_devops_agent.types.post_register_service_supported_service
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.service_details
    import capo_devops_agent.types.service_name_input
    import capo_devops_agent.types.tags


class RegisterServiceInput(TypedDict, closed=True):
    service: "capo_devops_agent.types.post_register_service_supported_service.PostRegisterServiceSupportedService"
    service_details: "capo_devops_agent.types.service_details.ServiceDetails"
    """<p>Service-specific authorization configuration parameters</p>"""
    kms_key_arn: NotRequired["capo_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    private_connection_name: NotRequired[
        "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection to use for VPC connectivity.</p>"""
    target_url_private_connection_name: NotRequired[
        "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.</p>"""
    exchange_url_private_connection_name: NotRequired[
        "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.</p>"""
    name: NotRequired["capo_devops_agent.types.service_name_input.ServiceNameInput"]
    """<p>The display name for the service registration.</p>"""
    tags: NotRequired["capo_devops_agent.types.tags.Tags"]
    """<p>Tags to add to the Service at registration time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterServiceInput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.service_details

    out["serviceDetails"] = capo_devops_agent.types.service_details.serialize_json(
        value["service_details"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "private_connection_name" in value:
        out["privateConnectionName"] = value["private_connection_name"]
    if "target_url_private_connection_name" in value:
        out["targetUrlPrivateConnectionName"] = value[
            "target_url_private_connection_name"
        ]
    if "exchange_url_private_connection_name" in value:
        out["exchangeUrlPrivateConnectionName"] = value[
            "exchange_url_private_connection_name"
        ]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegisterServiceInput:
    out: RegisterServiceInput = {}  # type: ignore[typeddict-item]
    if data.get("serviceDetails") is not None:
        import capo_devops_agent.types.service_details

        out["service_details"] = (
            capo_devops_agent.types.service_details.deserialize_json(
                data["serviceDetails"]
            )
        )
    else:
        raise DeserializationError("RegisterServiceInput.service_details required")
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    if data.get("targetUrlPrivateConnectionName") is not None:
        out["target_url_private_connection_name"] = data[
            "targetUrlPrivateConnectionName"
        ]
    if data.get("exchangeUrlPrivateConnectionName") is not None:
        out["exchange_url_private_connection_name"] = data[
            "exchangeUrlPrivateConnectionName"
        ]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.deserialize_json(data["tags"])
    return out

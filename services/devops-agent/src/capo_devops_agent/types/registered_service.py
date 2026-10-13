"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredService``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.additional_service_details
    import capo_devops_agent.types.document_list
    import capo_devops_agent.types.kms_key_arn
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.service
    import capo_devops_agent.types.service_id
    import capo_devops_agent.types.service_name


class RegisteredService(TypedDict, closed=True):
    service_id: "capo_devops_agent.types.service_id.ServiceId"
    """<p>The unique identifier of a service.</p>"""
    service_type: "capo_devops_agent.types.service.Service"
    """<p>The service type e.g github or dynatrace</p>"""
    name: NotRequired["capo_devops_agent.types.service_name.ServiceName"]
    """<p>The display name of the registered service.</p>"""
    accessible_resources: NotRequired[
        "capo_devops_agent.types.document_list.DocumentList"
    ]
    """<p>List of accessible resources for this service.</p>"""
    additional_service_details: NotRequired[
        "capo_devops_agent.types.additional_service_details.AdditionalServiceDetails"
    ]
    """<p>Additional details specific to the service type.</p>"""
    kms_key_arn: NotRequired["capo_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    private_connection_name: NotRequired[
        "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection used for VPC connectivity.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was registered.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredService) -> dict:
    out: dict = {}
    out["serviceId"] = value["service_id"]
    import capo_devops_agent.types.service

    out["serviceType"] = capo_devops_agent.types.service.serialize_json(
        value["service_type"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "accessible_resources" in value:
        import capo_devops_agent.types.document_list

        out["accessibleResources"] = (
            capo_devops_agent.types.document_list.serialize_json(
                value["accessible_resources"]
            )
        )
    if "additional_service_details" in value:
        import capo_devops_agent.types.additional_service_details

        out["additionalServiceDetails"] = (
            capo_devops_agent.types.additional_service_details.serialize_json(
                value["additional_service_details"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "private_connection_name" in value:
        out["privateConnectionName"] = value["private_connection_name"]
    if "created_at" in value:
        import capo_devops_agent._protocol.serialize

        out["createdAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_devops_agent._protocol.serialize

        out["updatedAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> RegisteredService:
    out: RegisteredService = {}  # type: ignore[typeddict-item]
    if data.get("serviceId") is not None:
        out["service_id"] = data["serviceId"]
    else:
        raise DeserializationError("RegisteredService.service_id required")
    if data.get("serviceType") is not None:
        import capo_devops_agent.types.service

        out["service_type"] = capo_devops_agent.types.service.deserialize_json(
            data["serviceType"]
        )
    else:
        raise DeserializationError("RegisteredService.service_type required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("accessibleResources") is not None:
        import capo_devops_agent.types.document_list

        out["accessible_resources"] = (
            capo_devops_agent.types.document_list.deserialize_json(
                data["accessibleResources"]
            )
        )
    if data.get("additionalServiceDetails") is not None:
        import capo_devops_agent.types.additional_service_details

        out["additional_service_details"] = (
            capo_devops_agent.types.additional_service_details.deserialize_json(
                data["additionalServiceDetails"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: RegisteredService) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "additional_service_details" in value:
        import capo_devops_agent.types.additional_service_details

        out["additional_service_details"] = (
            capo_devops_agent.types.additional_service_details.redact_sensitive(
                value["additional_service_details"]
            )
        )
    return out

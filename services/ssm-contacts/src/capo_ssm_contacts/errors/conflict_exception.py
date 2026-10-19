"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.dependent_entity_list
    import capo_ssm_contacts.types.string


class ConflictException_(TypedDict, closed=True):
    message: "capo_ssm_contacts.types.string.String"
    resource_id: "capo_ssm_contacts.types.string.String"
    """Identifier of the resource in use"""
    resource_type: "capo_ssm_contacts.types.string.String"
    """Type of the resource in use"""
    dependent_entities: NotRequired[
        "capo_ssm_contacts.types.dependent_entity_list.DependentEntityList"
    ]
    """List of dependent entities containing information on relation type and resourceArns linked to the resource in use"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "dependent_entities" in value:
        import capo_ssm_contacts.types.dependent_entity_list

        out["DependentEntities"] = (
            capo_ssm_contacts.types.dependent_entity_list.serialize_aws_json_1_1(
                value["dependent_entities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("DependentEntities") is not None:
        import capo_ssm_contacts.types.dependent_entity_list

        out["dependent_entities"] = (
            capo_ssm_contacts.types.dependent_entity_list.deserialize_aws_json_1_1(
                data["DependentEntities"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmcontacts#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)

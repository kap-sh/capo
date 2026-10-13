"""Generated from Smithy shape ``com.amazonaws.workmail#CreateResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.organization_id
    import capo_workmail.types.resource_description
    import capo_workmail.types.resource_name
    import capo_workmail.types.resource_type


class CreateResourceRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier associated with the organization for which the resource is created.</p>"""
    name: "capo_workmail.types.resource_name.ResourceName"
    """<p>The name of the new resource.</p>"""
    type: "capo_workmail.types.resource_type.ResourceType"
    """<p>The type of the new resource. The available types are <code>equipment</code> and <code>room</code>.</p>"""
    description: NotRequired[
        "capo_workmail.types.resource_description.ResourceDescription"
    ]
    """<p>Resource description.</p>"""
    hidden_from_global_address_list: "capo_workmail.types.boolean.Boolean"
    """<p>If this parameter is enabled, the resource will be hidden from the address book.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Name"] = value["name"]
    import capo_workmail.types.resource_type

    out["Type"] = capo_workmail.types.resource_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["HiddenFromGlobalAddressList"] = value.get(
        "hidden_from_global_address_list", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceRequest:
    out: CreateResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("CreateResourceRequest.organization_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateResourceRequest.name required")
    if data.get("Type") is not None:
        import capo_workmail.types.resource_type

        out["type"] = capo_workmail.types.resource_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateResourceRequest.type required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("HiddenFromGlobalAddressList") is not None:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    else:
        out["hidden_from_global_address_list"] = False
    return out


def redact_sensitive(value: CreateResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

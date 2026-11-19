"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.service_action_definition_type
    import capo_service_catalog.types.service_action_description
    import capo_service_catalog.types.service_action_name


class ServiceActionSummary(TypedDict, closed=True):
    id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The self-service action identifier.</p>"""
    name: NotRequired[
        "capo_service_catalog.types.service_action_name.ServiceActionName"
    ]
    """<p>The self-service action name.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.service_action_description.ServiceActionDescription"
    ]
    """<p>The self-service action description.</p>"""
    definition_type: NotRequired[
        "capo_service_catalog.types.service_action_definition_type.ServiceActionDefinitionType"
    ]
    """<p>The self-service action definition type. For example, <code>SSM_AUTOMATION</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "definition_type" in value:
        import capo_service_catalog.types.service_action_definition_type

        out["DefinitionType"] = (
            capo_service_catalog.types.service_action_definition_type.serialize_aws_json_1_1(
                value["definition_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceActionSummary:
    out: ServiceActionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefinitionType") is not None:
        import capo_service_catalog.types.service_action_definition_type

        out["definition_type"] = (
            capo_service_catalog.types.service_action_definition_type.deserialize_aws_json_1_1(
                data["DefinitionType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceActionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "definition_type" in value:
        import capo_service_catalog.types.service_action_definition_type

        out["DefinitionType"] = (
            capo_service_catalog.types.service_action_definition_type.serialize_cbor(
                value["definition_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ServiceActionSummary:
    out: ServiceActionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefinitionType") is not None:
        import capo_service_catalog.types.service_action_definition_type

        out["definition_type"] = (
            capo_service_catalog.types.service_action_definition_type.deserialize_cbor(
                data["DefinitionType"]
            )
        )
    return out

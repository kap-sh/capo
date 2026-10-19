"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateServiceActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.service_action_definition_map
    import capo_service_catalog.types.service_action_description
    import capo_service_catalog.types.service_action_name


class UpdateServiceActionInput(TypedDict, closed=True):
    id: "capo_service_catalog.types.id.Id"
    """<p>The self-service action identifier.</p>"""
    name: NotRequired[
        "capo_service_catalog.types.service_action_name.ServiceActionName"
    ]
    """<p>The self-service action name.</p>"""
    definition: NotRequired[
        "capo_service_catalog.types.service_action_definition_map.ServiceActionDefinitionMap"
    ]
    """<p>A map that defines the self-service action.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.service_action_description.ServiceActionDescription"
    ]
    """<p>The self-service action description.</p>"""
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceActionInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "definition" in value:
        import capo_service_catalog.types.service_action_definition_map

        out["Definition"] = (
            capo_service_catalog.types.service_action_definition_map.serialize_aws_json_1_1(
                value["definition"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceActionInput:
    out: UpdateServiceActionInput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Definition") is not None:
        import capo_service_catalog.types.service_action_definition_map

        out["definition"] = (
            capo_service_catalog.types.service_action_definition_map.deserialize_aws_json_1_1(
                data["Definition"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    return out

"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateServiceActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.service_action_definition_map
    import capo_service_catalog.types.service_action_definition_type
    import capo_service_catalog.types.service_action_description
    import capo_service_catalog.types.service_action_name


class CreateServiceActionInput(TypedDict, closed=True):
    name: "capo_service_catalog.types.service_action_name.ServiceActionName"
    """<p>The self-service action name.</p>"""
    definition_type: "capo_service_catalog.types.service_action_definition_type.ServiceActionDefinitionType"
    """<p>The service action definition type. For example, <code>SSM_AUTOMATION</code>.</p>"""
    definition: "capo_service_catalog.types.service_action_definition_map.ServiceActionDefinitionMap"
    r"""<p>The self-service action definition. Can be one of the following:</p> <dl> <dt>Name</dt> <dd> <p>The name of the Amazon Web Services Systems Manager document (SSM document). For example, <code>AWS-RestartEC2Instance</code>.</p> <p>If you are using a shared SSM document, you must provide the ARN instead of the name.</p> </dd> <dt>Version</dt> <dd> <p>The Amazon Web Services Systems Manager automation document version. For example, <code>"Version": "1"</code> </p> </dd> <dt>AssumeRole</dt> <dd> <p>The Amazon Resource Name (ARN) of the role that performs the self-service actions on your behalf. For example, <code>"AssumeRole": "arn:aws:iam::12345678910:role/ActionRole"</code>.</p> <p>To reuse the provisioned product launch role, set to <code>"AssumeRole": "LAUNCH_ROLE"</code>.</p> </dd> <dt>Parameters</dt> <dd> <p>The list of parameters in JSON format.</p> <p>For example: <code>[{\"Name\":\"InstanceId\",\"Type\":\"TARGET\"}]</code> or <code>[{\"Name\":\"InstanceId\",\"Type\":\"TEXT_VALUE\"}]</code>.</p> </dd> </dl>"""
    description: NotRequired[
        "capo_service_catalog.types.service_action_description.ServiceActionDescription"
    ]
    """<p>The self-service action description.</p>"""
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServiceActionInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_service_catalog.types.service_action_definition_type

    out["DefinitionType"] = (
        capo_service_catalog.types.service_action_definition_type.serialize_aws_json_1_1(
            value["definition_type"]
        )
    )
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
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateServiceActionInput:
    out: CreateServiceActionInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateServiceActionInput.name required")
    if data.get("DefinitionType") is not None:
        import capo_service_catalog.types.service_action_definition_type

        out["definition_type"] = (
            capo_service_catalog.types.service_action_definition_type.deserialize_aws_json_1_1(
                data["DefinitionType"]
            )
        )
    else:
        raise DeserializationError("CreateServiceActionInput.definition_type required")
    if data.get("Definition") is not None:
        import capo_service_catalog.types.service_action_definition_map

        out["definition"] = (
            capo_service_catalog.types.service_action_definition_map.deserialize_aws_json_1_1(
                data["Definition"]
            )
        )
    else:
        raise DeserializationError("CreateServiceActionInput.definition required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "CreateServiceActionInput.idempotency_token required"
        )
    return out

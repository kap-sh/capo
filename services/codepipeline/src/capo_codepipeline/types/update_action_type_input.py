"""Generated from Smithy shape ``com.amazonaws.codepipeline#UpdateActionTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type_declaration


class UpdateActionTypeInput(TypedDict, closed=True):
    action_type: "capo_codepipeline.types.action_type_declaration.ActionTypeDeclaration"
    """<p>The action type definition for the action type to be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateActionTypeInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type_declaration

    out["actionType"] = (
        capo_codepipeline.types.action_type_declaration.serialize_aws_json_1_1(
            value["action_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateActionTypeInput:
    out: UpdateActionTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_codepipeline.types.action_type_declaration

        out["action_type"] = (
            capo_codepipeline.types.action_type_declaration.deserialize_aws_json_1_1(
                data["actionType"]
            )
        )
    else:
        raise DeserializationError("UpdateActionTypeInput.action_type required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateActionTypeInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type_declaration

    out["actionType"] = capo_codepipeline.types.action_type_declaration.serialize_cbor(
        value["action_type"]
    )
    return out


def deserialize_cbor(data: dict) -> UpdateActionTypeInput:
    out: UpdateActionTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_codepipeline.types.action_type_declaration

        out["action_type"] = (
            capo_codepipeline.types.action_type_declaration.deserialize_cbor(
                data["actionType"]
            )
        )
    else:
        raise DeserializationError("UpdateActionTypeInput.action_type required")
    return out

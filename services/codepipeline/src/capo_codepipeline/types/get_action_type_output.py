"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetActionTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type_declaration


class GetActionTypeOutput(TypedDict, closed=True):
    action_type: NotRequired[
        "capo_codepipeline.types.action_type_declaration.ActionTypeDeclaration"
    ]
    """<p>The action type information for the requested action type, such as the action type ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetActionTypeOutput) -> dict:
    out: dict = {}
    if "action_type" in value:
        import capo_codepipeline.types.action_type_declaration

        out["actionType"] = (
            capo_codepipeline.types.action_type_declaration.serialize_aws_json_1_1(
                value["action_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetActionTypeOutput:
    out: GetActionTypeOutput = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_codepipeline.types.action_type_declaration

        out["action_type"] = (
            capo_codepipeline.types.action_type_declaration.deserialize_aws_json_1_1(
                data["actionType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetActionTypeOutput) -> dict:
    out: dict = {}
    if "action_type" in value:
        import capo_codepipeline.types.action_type_declaration

        out["actionType"] = (
            capo_codepipeline.types.action_type_declaration.serialize_cbor(
                value["action_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetActionTypeOutput:
    out: GetActionTypeOutput = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_codepipeline.types.action_type_declaration

        out["action_type"] = (
            capo_codepipeline.types.action_type_declaration.deserialize_cbor(
                data["actionType"]
            )
        )
    return out

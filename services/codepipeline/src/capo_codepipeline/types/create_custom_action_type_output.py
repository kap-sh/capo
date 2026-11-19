"""Generated from Smithy shape ``com.amazonaws.codepipeline#CreateCustomActionTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type
    import capo_codepipeline.types.tag_list


class CreateCustomActionTypeOutput(TypedDict, closed=True):
    action_type: "capo_codepipeline.types.action_type.ActionType"
    """<p>Returns information about the details of an action type.</p>"""
    tags: NotRequired["capo_codepipeline.types.tag_list.TagList"]
    """<p>Specifies the tags applied to the custom action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomActionTypeOutput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type

    out["actionType"] = capo_codepipeline.types.action_type.serialize_aws_json_1_1(
        value["action_type"]
    )
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomActionTypeOutput:
    out: CreateCustomActionTypeOutput = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_codepipeline.types.action_type

        out["action_type"] = (
            capo_codepipeline.types.action_type.deserialize_aws_json_1_1(
                data["actionType"]
            )
        )
    else:
        raise DeserializationError("CreateCustomActionTypeOutput.action_type required")
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateCustomActionTypeOutput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_type

    out["actionType"] = capo_codepipeline.types.action_type.serialize_cbor(
        value["action_type"]
    )
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> CreateCustomActionTypeOutput:
    out: CreateCustomActionTypeOutput = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_codepipeline.types.action_type

        out["action_type"] = capo_codepipeline.types.action_type.deserialize_cbor(
            data["actionType"]
        )
    else:
        raise DeserializationError("CreateCustomActionTypeOutput.action_type required")
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_cbor(data["tags"])
    return out

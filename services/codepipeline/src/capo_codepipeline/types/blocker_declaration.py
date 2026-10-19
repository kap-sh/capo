"""Generated from Smithy shape ``com.amazonaws.codepipeline#BlockerDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.blocker_name
    import capo_codepipeline.types.blocker_type


class BlockerDeclaration(TypedDict, closed=True):
    name: "capo_codepipeline.types.blocker_name.BlockerName"
    """<p>Reserved for future use.</p>"""
    type: "capo_codepipeline.types.blocker_type.BlockerType"
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockerDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_codepipeline.types.blocker_type

    out["type"] = capo_codepipeline.types.blocker_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockerDeclaration:
    out: BlockerDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_codepipeline.types.blocker_type

        out["type"] = capo_codepipeline.types.blocker_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codepipeline.types.blocker_type.BlockerType", ""
        )
    return out

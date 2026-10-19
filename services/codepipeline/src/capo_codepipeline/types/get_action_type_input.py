"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetActionTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_category
    import capo_codepipeline.types.action_provider
    import capo_codepipeline.types.action_type_owner
    import capo_codepipeline.types.version


class GetActionTypeInput(TypedDict, closed=True):
    category: "capo_codepipeline.types.action_category.ActionCategory"
    """<p>Defines what kind of action can be taken in the stage. The following are the valid values:</p> <ul> <li> <p> <code>Source</code> </p> </li> <li> <p> <code>Build</code> </p> </li> <li> <p> <code>Test</code> </p> </li> <li> <p> <code>Deploy</code> </p> </li> <li> <p> <code>Approval</code> </p> </li> <li> <p> <code>Invoke</code> </p> </li> <li> <p> <code>Compute</code> </p> </li> </ul>"""
    owner: "capo_codepipeline.types.action_type_owner.ActionTypeOwner"
    """<p>The creator of an action type that was created with any supported integration model. There are two valid values: <code>AWS</code> and <code>ThirdParty</code>.</p>"""
    provider: "capo_codepipeline.types.action_provider.ActionProvider"
    """<p>The provider of the action type being called. The provider name is specified when the action type is created.</p>"""
    version: "capo_codepipeline.types.version.Version"
    """<p>A string that describes the action type version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetActionTypeInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_category

    out["category"] = capo_codepipeline.types.action_category.serialize_aws_json_1_1(
        value["category"]
    )
    out["owner"] = value["owner"]
    out["provider"] = value["provider"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetActionTypeInput:
    out: GetActionTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("category") is not None:
        import capo_codepipeline.types.action_category

        out["category"] = (
            capo_codepipeline.types.action_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_codepipeline.types.action_category.ActionCategory", ""
        )
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        out["owner"] = ""
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out

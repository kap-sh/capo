"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeleteCustomActionTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_category
    import capo_codepipeline.types.action_provider
    import capo_codepipeline.types.version


class DeleteCustomActionTypeInput(TypedDict, closed=True):
    category: "capo_codepipeline.types.action_category.ActionCategory"
    """<p>The category of the custom action that you want to delete, such as source or deploy.</p>"""
    provider: "capo_codepipeline.types.action_provider.ActionProvider"
    """<p>The provider of the service used in the custom action, such as CodeDeploy.</p>"""
    version: "capo_codepipeline.types.version.Version"
    """<p>The version of the custom action to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCustomActionTypeInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_category

    out["category"] = capo_codepipeline.types.action_category.serialize_aws_json_1_1(
        value["category"]
    )
    out["provider"] = value["provider"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCustomActionTypeInput:
    out: DeleteCustomActionTypeInput = {}  # type: ignore[typeddict-item]
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
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out

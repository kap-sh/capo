"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_category
    import capo_codepipeline.types.action_owner
    import capo_codepipeline.types.action_provider
    import capo_codepipeline.types.version


class ActionTypeId(TypedDict, closed=True):
    category: "capo_codepipeline.types.action_category.ActionCategory"
    """<p>A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values. </p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Invoke</p> </li> <li> <p>Approval</p> </li> <li> <p>Compute</p> </li> </ul>"""
    owner: "capo_codepipeline.types.action_owner.ActionOwner"
    """<p>The creator of the action being called. There are three valid values for the <code>Owner</code> field in the action category section within your pipeline structure: <code>AWS</code>, <code>ThirdParty</code>, and <code>Custom</code>. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers">Valid Action Types and Providers in CodePipeline</a>.</p>"""
    provider: "capo_codepipeline.types.action_provider.ActionProvider"
    """<p>The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of CodeDeploy, which would be specified as <code>CodeDeploy</code>. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers">Valid Action Types and Providers in CodePipeline</a>.</p>"""
    version: "capo_codepipeline.types.version.Version"
    """<p>A string that describes the action version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeId) -> dict:
    out: dict = {}
    import capo_codepipeline.types.action_category

    out["category"] = capo_codepipeline.types.action_category.serialize_aws_json_1_1(
        value["category"]
    )
    import capo_codepipeline.types.action_owner

    out["owner"] = capo_codepipeline.types.action_owner.serialize_aws_json_1_1(
        value["owner"]
    )
    out["provider"] = value["provider"]
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeId:
    out: ActionTypeId = {}  # type: ignore[typeddict-item]
    if data.get("category") is not None:
        import capo_codepipeline.types.action_category

        out["category"] = (
            capo_codepipeline.types.action_category.deserialize_aws_json_1_1(
                data["category"]
            )
        )
    else:
        raise DeserializationError("ActionTypeId.category required")
    if data.get("owner") is not None:
        import capo_codepipeline.types.action_owner

        out["owner"] = capo_codepipeline.types.action_owner.deserialize_aws_json_1_1(
            data["owner"]
        )
    else:
        raise DeserializationError("ActionTypeId.owner required")
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("ActionTypeId.provider required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("ActionTypeId.version required")
    return out

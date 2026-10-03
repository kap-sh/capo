"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAccountCustomizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.account_customization
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.tag_list


class CreateAccountCustomizationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to customize Quick Sight for.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The Quick Sight namespace that you want to add customizations to.</p>"""
    account_customization: (
        "capo_quicksight.types.account_customization.AccountCustomization"
    )
    """<p>The Quick Sight customizations you're adding. You can add these to an Amazon Web Services account and a QuickSight namespace. </p> <p>For example, you can add a default theme by setting <code>AccountCustomization</code> to the midnight theme: <code>"AccountCustomization": { "DefaultTheme": "arn:aws:quicksight::aws:theme/MIDNIGHT" }</code>. Or, you can add a custom theme by specifying <code>"AccountCustomization": { "DefaultTheme": "arn:aws:quicksight:us-west-2:111122223333:theme/bdb844d0-0fe9-4d9d-b520-0fe602d93639" }</code>. </p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>A list of the tags that you want to attach to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountCustomizationRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.account_customization

    out["AccountCustomization"] = (
        capo_quicksight.types.account_customization.serialize_json(
            value["account_customization"]
        )
    )
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAccountCustomizationRequest:
    out: CreateAccountCustomizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountCustomization") is not None:
        import capo_quicksight.types.account_customization

        out["account_customization"] = (
            capo_quicksight.types.account_customization.deserialize_json(
                data["AccountCustomization"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccountCustomizationRequest.account_customization required"
        )
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.identity_store
    import capo_quicksight.types.namespace
    import capo_quicksight.types.tag_list


class CreateNamespaceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create the Quick Sight namespace in.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The name that you want to use to describe the new namespace.</p>"""
    identity_store: "capo_quicksight.types.identity_store.IdentityStore"
    """<p>Specifies the type of your user identity directory. Currently, this supports users with an identity type of <code>QUICKSIGHT</code>.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>The tags that you want to associate with the namespace that you're creating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNamespaceRequest) -> dict:
    out: dict = {}
    out["Namespace"] = value["namespace"]
    import capo_quicksight.types.identity_store

    out["IdentityStore"] = capo_quicksight.types.identity_store.serialize_json(
        value["identity_store"]
    )
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateNamespaceRequest:
    out: CreateNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    else:
        out["namespace"] = ""
    if data.get("IdentityStore") is not None:
        import capo_quicksight.types.identity_store

        out["identity_store"] = capo_quicksight.types.identity_store.deserialize_json(
            data["IdentityStore"]
        )
    else:
        import typing

        out["identity_store"] = typing.cast(
            "capo_quicksight.types.identity_store.IdentityStore", ""
        )
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out

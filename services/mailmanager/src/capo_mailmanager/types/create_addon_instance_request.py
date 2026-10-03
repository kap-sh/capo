"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddonInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_subscription_id
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.tag_list


class CreateAddonInstanceRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    addon_subscription_id: (
        "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId"
    )
    """<p>The unique ID of a previously created subscription that an Add On instance is created for. You can only have one instance per subscription.</p>"""
    tags: NotRequired["capo_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddonInstanceRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["AddonSubscriptionId"] = value["addon_subscription_id"]
    if "tags" in value:
        import capo_mailmanager.types.tag_list

        out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddonInstanceRequest:
    out: CreateAddonInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("AddonSubscriptionId") is not None:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    else:
        raise DeserializationError(
            "CreateAddonInstanceRequest.addon_subscription_id required"
        )
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out

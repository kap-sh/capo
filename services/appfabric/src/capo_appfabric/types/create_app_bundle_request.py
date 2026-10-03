"""Generated from Smithy shape ``com.amazonaws.appfabric#CreateAppBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.identifier
    import capo_appfabric.types.tag_list
    import capo_appfabric.types.uuid


class CreateAppBundleRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_appfabric.types.uuid.UUID"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    customer_managed_key_identifier: NotRequired[
        "capo_appfabric.types.identifier.Identifier"
    ]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service (KMS) key to use to encrypt the application data. If this is not specified, an Amazon Web Services owned key is used for encryption.</p>"""
    tags: NotRequired["capo_appfabric.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppBundleRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "customer_managed_key_identifier" in value:
        out["customerManagedKeyIdentifier"] = value["customer_managed_key_identifier"]
    if "tags" in value:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAppBundleRequest:
    out: CreateAppBundleRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("customerManagedKeyIdentifier") is not None:
        out["customer_managed_key_identifier"] = data["customerManagedKeyIdentifier"]
    if data.get("tags") is not None:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.deserialize_json(data["tags"])
    return out

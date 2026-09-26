"""Generated from Smithy shape ``com.amazonaws.accountaccess#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.identity_source
    import capo_account_access.types.tags_map


class CreateApplicationRequest(TypedDict, closed=True):
    identity_source: "capo_account_access.types.identity_source.IdentitySource"
    """<p>Specifies the identity source for the application. The identity source defines the IAM Identity Center instance that provides principals for entitlements.</p>"""
    tags: NotRequired["capo_account_access.types.tags_map.TagsMap"]
    """<p>Specifies the tags to assign to the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    import capo_account_access.types.identity_source

    out["identitySource"] = capo_account_access.types.identity_source.serialize_json(
        value["identity_source"]
    )
    if "tags" in value:
        import capo_account_access.types.tags_map

        out["tags"] = capo_account_access.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("identitySource") is not None:
        import capo_account_access.types.identity_source

        out["identity_source"] = (
            capo_account_access.types.identity_source.deserialize_json(
                data["identitySource"]
            )
        )
    else:
        raise DeserializationError("CreateApplicationRequest.identity_source required")
    if data.get("tags") is not None:
        import capo_account_access.types.tags_map

        out["tags"] = capo_account_access.types.tags_map.deserialize_json(data["tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstancesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_list
    import capo_chime_sdk_identity.types.next_token


class ListAppInstancesResponse(TypedDict, closed=True):
    app_instances: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_list.AppInstanceList"
    ]
    """<p>The information for each <code>AppInstance</code>.</p>"""
    next_token: NotRequired["capo_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API requests until the maximum number of <code>AppInstance</code>s is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstancesResponse) -> dict:
    out: dict = {}
    if "app_instances" in value:
        import capo_chime_sdk_identity.types.app_instance_list

        out["AppInstances"] = (
            capo_chime_sdk_identity.types.app_instance_list.serialize_json(
                value["app_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstancesResponse:
    out: ListAppInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstances") is not None:
        import capo_chime_sdk_identity.types.app_instance_list

        out["app_instances"] = (
            capo_chime_sdk_identity.types.app_instance_list.deserialize_json(
                data["AppInstances"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAppInstancesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instances" in value:
        import capo_chime_sdk_identity.types.app_instance_list

        out["app_instances"] = (
            capo_chime_sdk_identity.types.app_instance_list.redact_sensitive(
                value["app_instances"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out

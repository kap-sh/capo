"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUserEndpointsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list
    import capo_chime_sdk_identity.types.next_token


class ListAppInstanceUserEndpointsResponse(TypedDict, closed=True):
    app_instance_user_endpoints: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list.AppInstanceUserEndpointSummaryList"
    ]
    """<p>The information for each requested <code>AppInstanceUserEndpoint</code>.</p>"""
    next_token: NotRequired["capo_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested endpoints are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUserEndpointsResponse) -> dict:
    out: dict = {}
    if "app_instance_user_endpoints" in value:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list

        out["AppInstanceUserEndpoints"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list.serialize_json(
                value["app_instance_user_endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceUserEndpointsResponse:
    out: ListAppInstanceUserEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceUserEndpoints") is not None:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list

        out["app_instance_user_endpoints"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list.deserialize_json(
                data["AppInstanceUserEndpoints"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAppInstanceUserEndpointsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_user_endpoints" in value:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list

        out["app_instance_user_endpoints"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint_summary_list.redact_sensitive(
                value["app_instance_user_endpoints"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out

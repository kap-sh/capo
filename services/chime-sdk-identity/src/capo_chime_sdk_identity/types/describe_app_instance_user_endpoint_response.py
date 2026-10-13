"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceUserEndpointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_user_endpoint


class DescribeAppInstanceUserEndpointResponse(TypedDict, closed=True):
    app_instance_user_endpoint: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_user_endpoint.AppInstanceUserEndpoint"
    ]
    """<p>The full details of an <code>AppInstanceUserEndpoint</code>: the <code>AppInstanceUserArn</code>, ID, name, type, resource ARN, attributes, allow messages, state, and created and last updated timestamps. All timestamps use epoch milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceUserEndpointResponse) -> dict:
    out: dict = {}
    if "app_instance_user_endpoint" in value:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint

        out["AppInstanceUserEndpoint"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint.serialize_json(
                value["app_instance_user_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceUserEndpointResponse:
    out: DescribeAppInstanceUserEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceUserEndpoint") is not None:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint

        out["app_instance_user_endpoint"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint.deserialize_json(
                data["AppInstanceUserEndpoint"]
            )
        )
    return out


def redact_sensitive(value: DescribeAppInstanceUserEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_user_endpoint" in value:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint

        out["app_instance_user_endpoint"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint.redact_sensitive(
                value["app_instance_user_endpoint"]
            )
        )
    return out

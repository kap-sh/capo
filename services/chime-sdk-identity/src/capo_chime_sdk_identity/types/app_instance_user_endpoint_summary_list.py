"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserEndpointSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary

AppInstanceUserEndpointSummaryList: TypeAlias = list[
    "capo_chime_sdk_identity.types.app_instance_user_endpoint_summary.AppInstanceUserEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserEndpointSummaryList) -> list:
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_identity.types.app_instance_user_endpoint_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AppInstanceUserEndpointSummaryList:
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary

    out: AppInstanceUserEndpointSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_identity.types.app_instance_user_endpoint_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AppInstanceUserEndpointSummaryList) -> list[Any]:
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_summary

    return [
        capo_chime_sdk_identity.types.app_instance_user_endpoint_summary.redact_sensitive(
            item
        )
        for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.endpoint_status
    import capo_chime_sdk_identity.types.endpoint_status_reason


class EndpointState(TypedDict, closed=True):
    status: "capo_chime_sdk_identity.types.endpoint_status.EndpointStatus"
    """<p>Enum that indicates the Status of an <code>AppInstanceUserEndpoint</code>.</p>"""
    status_reason: NotRequired[
        "capo_chime_sdk_identity.types.endpoint_status_reason.EndpointStatusReason"
    ]
    """<p>The reason for the <code>EndpointStatus</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointState) -> dict:
    out: dict = {}
    import capo_chime_sdk_identity.types.endpoint_status

    out["Status"] = capo_chime_sdk_identity.types.endpoint_status.serialize_json(
        value["status"]
    )
    if "status_reason" in value:
        import capo_chime_sdk_identity.types.endpoint_status_reason

        out["StatusReason"] = (
            capo_chime_sdk_identity.types.endpoint_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> EndpointState:
    out: EndpointState = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_chime_sdk_identity.types.endpoint_status

        out["status"] = capo_chime_sdk_identity.types.endpoint_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_chime_sdk_identity.types.endpoint_status.EndpointStatus", ""
        )
    if data.get("StatusReason") is not None:
        import capo_chime_sdk_identity.types.endpoint_status_reason

        out["status_reason"] = (
            capo_chime_sdk_identity.types.endpoint_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    return out

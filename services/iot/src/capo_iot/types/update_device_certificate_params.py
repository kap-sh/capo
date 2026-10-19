"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDeviceCertificateParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.device_certificate_update_action


class UpdateDeviceCertificateParams(TypedDict, closed=True):
    action: (
        "capo_iot.types.device_certificate_update_action.DeviceCertificateUpdateAction"
    )
    """<p>The action that you want to apply to the device certificate. The only supported value is <code>DEACTIVATE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceCertificateParams) -> dict:
    out: dict = {}
    import capo_iot.types.device_certificate_update_action

    out["action"] = capo_iot.types.device_certificate_update_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDeviceCertificateParams:
    out: UpdateDeviceCertificateParams = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_iot.types.device_certificate_update_action

        out["action"] = (
            capo_iot.types.device_certificate_update_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_iot.types.device_certificate_update_action.DeviceCertificateUpdateAction",
            "",
        )
    return out

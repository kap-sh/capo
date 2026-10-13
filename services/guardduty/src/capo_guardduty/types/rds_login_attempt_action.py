"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsLoginAttemptAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.login_attributes
    import capo_guardduty.types.remote_ip_details


class RdsLoginAttemptAction(TypedDict, closed=True):
    remote_ip_details: NotRequired[
        "capo_guardduty.types.remote_ip_details.RemoteIpDetails"
    ]
    login_attributes: NotRequired[
        "capo_guardduty.types.login_attributes.LoginAttributes"
    ]
    """<p>Indicates the login attributes used in the login attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsLoginAttemptAction) -> dict:
    out: dict = {}
    if "remote_ip_details" in value:
        import capo_guardduty.types.remote_ip_details

        out["remoteIpDetails"] = capo_guardduty.types.remote_ip_details.serialize_json(
            value["remote_ip_details"]
        )
    if "login_attributes" in value:
        import capo_guardduty.types.login_attributes

        out["LoginAttributes"] = capo_guardduty.types.login_attributes.serialize_json(
            value["login_attributes"]
        )
    return out


def deserialize_json(data: dict) -> RdsLoginAttemptAction:
    out: RdsLoginAttemptAction = {}  # type: ignore[typeddict-item]
    if data.get("remoteIpDetails") is not None:
        import capo_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            capo_guardduty.types.remote_ip_details.deserialize_json(
                data["remoteIpDetails"]
            )
        )
    if data.get("LoginAttributes") is not None:
        import capo_guardduty.types.login_attributes

        out["login_attributes"] = (
            capo_guardduty.types.login_attributes.deserialize_json(
                data["LoginAttributes"]
            )
        )
    return out


def redact_sensitive(value: RdsLoginAttemptAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "remote_ip_details" in value:
        import capo_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            capo_guardduty.types.remote_ip_details.redact_sensitive(
                value["remote_ip_details"]
            )
        )
    return out

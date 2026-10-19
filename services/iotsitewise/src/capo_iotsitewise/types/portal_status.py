"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.monitor_error_details
    import capo_iotsitewise.types.portal_state


class PortalStatus(TypedDict, closed=True):
    state: "capo_iotsitewise.types.portal_state.PortalState"
    """<p>The current state of the portal.</p>"""
    error: NotRequired[
        "capo_iotsitewise.types.monitor_error_details.MonitorErrorDetails"
    ]
    """<p>Contains associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.portal_state

    out["state"] = capo_iotsitewise.types.portal_state.serialize_json(value["state"])
    if "error" in value:
        import capo_iotsitewise.types.monitor_error_details

        out["error"] = capo_iotsitewise.types.monitor_error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> PortalStatus:
    out: PortalStatus = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.portal_state

        out["state"] = capo_iotsitewise.types.portal_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.portal_state.PortalState", ""
        )
    if data.get("error") is not None:
        import capo_iotsitewise.types.monitor_error_details

        out["error"] = capo_iotsitewise.types.monitor_error_details.deserialize_json(
            data["error"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.mediatailor#BeaconingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.client_side_beaconing_configuration


class BeaconingConfiguration(TypedDict, closed=True):
    client_side: NotRequired[
        "capo_mediatailor.types.client_side_beaconing_configuration.ClientSideBeaconingConfiguration"
    ]
    """<p>The beaconing settings for client-side reporting sessions. If you omit this object, MediaTailor uses <code>INSIGHTS</code> reporting mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BeaconingConfiguration) -> dict:
    out: dict = {}
    if "client_side" in value:
        import capo_mediatailor.types.client_side_beaconing_configuration

        out["ClientSide"] = (
            capo_mediatailor.types.client_side_beaconing_configuration.serialize_json(
                value["client_side"]
            )
        )
    return out


def deserialize_json(data: dict) -> BeaconingConfiguration:
    out: BeaconingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ClientSide") is not None:
        import capo_mediatailor.types.client_side_beaconing_configuration

        out["client_side"] = (
            capo_mediatailor.types.client_side_beaconing_configuration.deserialize_json(
                data["ClientSide"]
            )
        )
    return out

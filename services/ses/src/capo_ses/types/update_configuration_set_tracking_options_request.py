"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetTrackingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.tracking_options


class UpdateConfigurationSetTrackingOptionsRequest(TypedDict, closed=True):
    configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set.</p>"""
    tracking_options: "capo_ses.types.tracking_options.TrackingOptions"


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationSetTrackingOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
    )
    import capo_ses.types.tracking_options

    capo_ses.types.tracking_options.serialize_query(
        value["tracking_options"], pairs, f"{key_prefix}TrackingOptions"
    )


def deserialize_query(el: Element) -> UpdateConfigurationSetTrackingOptionsRequest:
    out: UpdateConfigurationSetTrackingOptionsRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        out["configuration_set_name"] = ""
    child_tracking_options = el.find("TrackingOptions")
    if child_tracking_options is not None:
        import capo_ses.types.tracking_options

        out["tracking_options"] = capo_ses.types.tracking_options.deserialize_query(
            child_tracking_options
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationSetTrackingOptionsRequest.tracking_options required"
        )
    return out

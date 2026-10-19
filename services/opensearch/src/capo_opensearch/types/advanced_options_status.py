"""Generated from Smithy shape ``com.amazonaws.opensearch#AdvancedOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.advanced_options
    import capo_opensearch.types.option_status


class AdvancedOptionsStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.advanced_options.AdvancedOptions"
    """<p>The status of advanced options for the specified domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The status of advanced options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedOptionsStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.advanced_options

    out["Options"] = capo_opensearch.types.advanced_options.serialize_json(
        value["options"]
    )
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> AdvancedOptionsStatus:
    out: AdvancedOptionsStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_opensearch.types.advanced_options

        out["options"] = capo_opensearch.types.advanced_options.deserialize_json(
            data["Options"]
        )
    else:
        out["options"] = {}
    if data.get("Status") is not None:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("AdvancedOptionsStatus.status required")
    return out

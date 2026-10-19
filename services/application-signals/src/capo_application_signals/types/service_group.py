"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.group_identifier
    import capo_application_signals.types.group_name
    import capo_application_signals.types.group_source
    import capo_application_signals.types.group_value


class ServiceGroup(TypedDict, closed=True):
    group_name: "capo_application_signals.types.group_name.GroupName"
    """<p>The name of the grouping attribute, such as <code>BusinessUnit</code> or <code>Environment</code>.</p>"""
    group_value: "capo_application_signals.types.group_value.GroupValue"
    """<p>The value of the grouping attribute for this service, such as <code>Payments</code> or <code>Production</code>.</p>"""
    group_source: "capo_application_signals.types.group_source.GroupSource"
    """<p>The source of the grouping attribute, such as <code>TAG</code>, <code>OTEL</code>, or <code>DEFAULT</code>.</p>"""
    group_identifier: "capo_application_signals.types.group_identifier.GroupIdentifier"
    """<p>A unique identifier for this grouping attribute value, used for filtering and API operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceGroup) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    out["GroupValue"] = value["group_value"]
    out["GroupSource"] = value["group_source"]
    out["GroupIdentifier"] = value["group_identifier"]
    return out


def deserialize_json(data: dict) -> ServiceGroup:
    out: ServiceGroup = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("GroupValue") is not None:
        out["group_value"] = data["GroupValue"]
    else:
        out["group_value"] = ""
    if data.get("GroupSource") is not None:
        out["group_source"] = data["GroupSource"]
    else:
        out["group_source"] = ""
    if data.get("GroupIdentifier") is not None:
        out["group_identifier"] = data["GroupIdentifier"]
    else:
        out["group_identifier"] = ""
    return out

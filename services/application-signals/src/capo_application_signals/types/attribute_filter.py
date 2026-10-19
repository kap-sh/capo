"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attribute_filter_name
    import capo_application_signals.types.attribute_filter_values


class AttributeFilter(TypedDict, closed=True):
    attribute_filter_name: (
        "capo_application_signals.types.attribute_filter_name.AttributeFilterName"
    )
    """<p>The name of the attribute to filter by, such as <code>Platform</code>, <code>Environment</code>, or <code>BusinessUnit</code>.</p>"""
    attribute_filter_values: (
        "capo_application_signals.types.attribute_filter_values.AttributeFilterValues"
    )
    """<p>An array of values to match for the specified attribute. Services that have any of these values for the attribute will be included in the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeFilter) -> dict:
    out: dict = {}
    out["AttributeFilterName"] = value["attribute_filter_name"]
    import capo_application_signals.types.attribute_filter_values

    out["AttributeFilterValues"] = (
        capo_application_signals.types.attribute_filter_values.serialize_json(
            value["attribute_filter_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> AttributeFilter:
    out: AttributeFilter = {}  # type: ignore[typeddict-item]
    if data.get("AttributeFilterName") is not None:
        out["attribute_filter_name"] = data["AttributeFilterName"]
    else:
        out["attribute_filter_name"] = ""
    if data.get("AttributeFilterValues") is not None:
        import capo_application_signals.types.attribute_filter_values

        out["attribute_filter_values"] = (
            capo_application_signals.types.attribute_filter_values.deserialize_json(
                data["AttributeFilterValues"]
            )
        )
    else:
        out["attribute_filter_values"] = []
    return out

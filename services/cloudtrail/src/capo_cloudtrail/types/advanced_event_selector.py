"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AdvancedEventSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_field_selectors
    import capo_cloudtrail.types.selector_name


class AdvancedEventSelector(TypedDict, closed=True):
    name: NotRequired["capo_cloudtrail.types.selector_name.SelectorName"]
    """<p>An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".</p>"""
    field_selectors: (
        "capo_cloudtrail.types.advanced_field_selectors.AdvancedFieldSelectors"
    )
    """<p>Contains all selector statements in an advanced event selector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedEventSelector) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import capo_cloudtrail.types.advanced_field_selectors

    out["FieldSelectors"] = (
        capo_cloudtrail.types.advanced_field_selectors.serialize_aws_json_1_1(
            value["field_selectors"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdvancedEventSelector:
    out: AdvancedEventSelector = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("FieldSelectors") is not None:
        import capo_cloudtrail.types.advanced_field_selectors

        out["field_selectors"] = (
            capo_cloudtrail.types.advanced_field_selectors.deserialize_aws_json_1_1(
                data["FieldSelectors"]
            )
        )
    else:
        raise DeserializationError("AdvancedEventSelector.field_selectors required")
    return out

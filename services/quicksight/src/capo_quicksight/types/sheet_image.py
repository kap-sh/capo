"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.image_custom_action_list
    import capo_quicksight.types.image_interaction_options
    import capo_quicksight.types.long_plain_text
    import capo_quicksight.types.sheet_image_scaling_configuration
    import capo_quicksight.types.sheet_image_source
    import capo_quicksight.types.sheet_image_tooltip_configuration
    import capo_quicksight.types.short_restrictive_resource_id


class SheetImage(TypedDict, closed=True):
    sheet_image_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the sheet image.</p>"""
    source: "capo_quicksight.types.sheet_image_source.SheetImageSource"
    """<p>The source of the image.</p>"""
    scaling: NotRequired[
        "capo_quicksight.types.sheet_image_scaling_configuration.SheetImageScalingConfiguration"
    ]
    """<p>Determines how the image is scaled.</p>"""
    tooltip: NotRequired[
        "capo_quicksight.types.sheet_image_tooltip_configuration.SheetImageTooltipConfiguration"
    ]
    """<p>The tooltip to be shown when hovering over the image.</p>"""
    image_content_alt_text: NotRequired[
        "capo_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the image.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.image_interaction_options.ImageInteractionOptions"
    ]
    """<p>The general image interactions setup for an image.</p>"""
    actions: NotRequired[
        "capo_quicksight.types.image_custom_action_list.ImageCustomActionList"
    ]
    """<p>A list of custom actions that are configured for an image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImage) -> dict:
    out: dict = {}
    out["SheetImageId"] = value["sheet_image_id"]
    import capo_quicksight.types.sheet_image_source

    out["Source"] = capo_quicksight.types.sheet_image_source.serialize_json(
        value["source"]
    )
    if "scaling" in value:
        import capo_quicksight.types.sheet_image_scaling_configuration

        out["Scaling"] = (
            capo_quicksight.types.sheet_image_scaling_configuration.serialize_json(
                value["scaling"]
            )
        )
    if "tooltip" in value:
        import capo_quicksight.types.sheet_image_tooltip_configuration

        out["Tooltip"] = (
            capo_quicksight.types.sheet_image_tooltip_configuration.serialize_json(
                value["tooltip"]
            )
        )
    if "image_content_alt_text" in value:
        out["ImageContentAltText"] = value["image_content_alt_text"]
    if "interactions" in value:
        import capo_quicksight.types.image_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.image_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    if "actions" in value:
        import capo_quicksight.types.image_custom_action_list

        out["Actions"] = capo_quicksight.types.image_custom_action_list.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> SheetImage:
    out: SheetImage = {}  # type: ignore[typeddict-item]
    if data.get("SheetImageId") is not None:
        out["sheet_image_id"] = data["SheetImageId"]
    else:
        out["sheet_image_id"] = ""
    if data.get("Source") is not None:
        import capo_quicksight.types.sheet_image_source

        out["source"] = capo_quicksight.types.sheet_image_source.deserialize_json(
            data["Source"]
        )
    else:
        raise DeserializationError("SheetImage.source required")
    if data.get("Scaling") is not None:
        import capo_quicksight.types.sheet_image_scaling_configuration

        out["scaling"] = (
            capo_quicksight.types.sheet_image_scaling_configuration.deserialize_json(
                data["Scaling"]
            )
        )
    if data.get("Tooltip") is not None:
        import capo_quicksight.types.sheet_image_tooltip_configuration

        out["tooltip"] = (
            capo_quicksight.types.sheet_image_tooltip_configuration.deserialize_json(
                data["Tooltip"]
            )
        )
    if data.get("ImageContentAltText") is not None:
        out["image_content_alt_text"] = data["ImageContentAltText"]
    if data.get("Interactions") is not None:
        import capo_quicksight.types.image_interaction_options

        out["interactions"] = (
            capo_quicksight.types.image_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    if data.get("Actions") is not None:
        import capo_quicksight.types.image_custom_action_list

        out["actions"] = (
            capo_quicksight.types.image_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    return out


def redact_sensitive(value: SheetImage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_quicksight.types.image_custom_action_list

        out["actions"] = (
            capo_quicksight.types.image_custom_action_list.redact_sensitive(
                value["actions"]
            )
        )
    return out

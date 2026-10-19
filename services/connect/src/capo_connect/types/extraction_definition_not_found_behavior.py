"""Generated from Smithy shape ``com.amazonaws.connect#ExtractionDefinitionNotFoundBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.not_found_behavior_type
    import capo_connect.types.not_found_default_value


class ExtractionDefinitionNotFoundBehavior(TypedDict, closed=True):
    behavior: "capo_connect.types.not_found_behavior_type.NotFoundBehaviorType"
    """<p>The behavior type. <code>USE_DEFAULT_VALUE</code> returns the specified default value. <code>OMIT</code> excludes the field from the output.</p>"""
    default_value: NotRequired[
        "capo_connect.types.not_found_default_value.NotFoundDefaultValue"
    ]
    """<p>The default value to use when the behavior is <code>USE_DEFAULT_VALUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionDefinitionNotFoundBehavior) -> dict:
    out: dict = {}
    import capo_connect.types.not_found_behavior_type

    out["Behavior"] = capo_connect.types.not_found_behavior_type.serialize_json(
        value["behavior"]
    )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> ExtractionDefinitionNotFoundBehavior:
    out: ExtractionDefinitionNotFoundBehavior = {}  # type: ignore[typeddict-item]
    if data.get("Behavior") is not None:
        import capo_connect.types.not_found_behavior_type

        out["behavior"] = capo_connect.types.not_found_behavior_type.deserialize_json(
            data["Behavior"]
        )
    else:
        import typing

        out["behavior"] = typing.cast(
            "capo_connect.types.not_found_behavior_type.NotFoundBehaviorType", ""
        )
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    return out

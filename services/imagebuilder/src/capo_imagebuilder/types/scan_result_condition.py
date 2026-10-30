"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ScanResultCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.maximum_severity_label
    import capo_imagebuilder.types.nullable_boolean


class ScanResultCondition(TypedDict, closed=True):
    maximum_severity_label: (
        "capo_imagebuilder.types.maximum_severity_label.MaximumSeverityLabel"
    )
    """<p>The maximum severity allowed for findings on the output AMI. A finding above this severity fails the image, unless <code>fixAvailable</code> excludes it. Valid values are <code>INFORMATIONAL</code>, <code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>. A <code>CRITICAL</code> finding that counts always fails the image.</p>"""
    fix_available: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether only findings that have a fix available count toward <code>maximumSeverityLabel</code>. When <code>false</code>, Image Builder counts every finding. The default is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultCondition) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.maximum_severity_label

    out["maximumSeverityLabel"] = (
        capo_imagebuilder.types.maximum_severity_label.serialize_json(
            value["maximum_severity_label"]
        )
    )
    if "fix_available" in value:
        out["fixAvailable"] = value["fix_available"]
    return out


def deserialize_json(data: dict) -> ScanResultCondition:
    out: ScanResultCondition = {}  # type: ignore[typeddict-item]
    if data.get("maximumSeverityLabel") is not None:
        import capo_imagebuilder.types.maximum_severity_label

        out["maximum_severity_label"] = (
            capo_imagebuilder.types.maximum_severity_label.deserialize_json(
                data["maximumSeverityLabel"]
            )
        )
    else:
        import typing

        out["maximum_severity_label"] = typing.cast(
            "capo_imagebuilder.types.maximum_severity_label.MaximumSeverityLabel", ""
        )
    if data.get("fixAvailable") is not None:
        out["fix_available"] = data["fixAvailable"]
    return out

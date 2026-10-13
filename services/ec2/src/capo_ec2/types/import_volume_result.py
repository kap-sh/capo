"""Generated from Smithy shape ``com.amazonaws.ec2#ImportVolumeResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.conversion_task


class ImportVolumeResult(TypedDict, closed=True):
    conversion_task: NotRequired["capo_ec2.types.conversion_task.ConversionTask"]
    """<p>Information about the conversion task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportVolumeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "conversion_task" in value:
        import capo_ec2.types.conversion_task

        capo_ec2.types.conversion_task.serialize_ec2_query(
            value["conversion_task"], pairs, f"{key_prefix}ConversionTask"
        )


def deserialize_ec2_query(el: Element) -> ImportVolumeResult:
    out: ImportVolumeResult = {}  # type: ignore[typeddict-item]
    child_conversion_task = el.find("conversionTask")
    if child_conversion_task is not None:
        import capo_ec2.types.conversion_task

        out["conversion_task"] = capo_ec2.types.conversion_task.deserialize_ec2_query(
            child_conversion_task
        )
    return out


def redact_sensitive(value: ImportVolumeResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conversion_task" in value:
        import capo_ec2.types.conversion_task

        out["conversion_task"] = capo_ec2.types.conversion_task.redact_sensitive(
            value["conversion_task"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.glue#DecimalNumber``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.blob
    import capo_glue.types.integer


class DecimalNumber(TypedDict, closed=True):
    unscaled_value: "capo_glue.types.blob.Blob"
    """<p>The unscaled numeric value.</p>"""
    scale: "capo_glue.types.integer.Integer"
    """<p>The scale that determines where the decimal point falls in the unscaled value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecimalNumber) -> dict:
    out: dict = {}
    import capo_glue.types.blob

    out["UnscaledValue"] = capo_glue.types.blob.serialize_aws_json_1_1(
        value["unscaled_value"]
    )
    out["Scale"] = value.get("scale", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DecimalNumber:
    out: DecimalNumber = {}  # type: ignore[typeddict-item]
    if data.get("UnscaledValue") is not None:
        import capo_glue.types.blob

        out["unscaled_value"] = capo_glue.types.blob.deserialize_aws_json_1_1(
            data["UnscaledValue"]
        )
    else:
        out["unscaled_value"] = b""
    if data.get("Scale") is not None:
        out["scale"] = data["Scale"]
    else:
        out["scale"] = 0
    return out

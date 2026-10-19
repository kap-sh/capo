"""Generated from Smithy shape ``com.amazonaws.b2bi#WrapOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.line_length
    import capo_b2bi.types.line_terminator
    import capo_b2bi.types.wrap_format


class WrapOptions(TypedDict, closed=True):
    wrap_by: "capo_b2bi.types.wrap_format.WrapFormat"
    """<p>Specifies the method used for wrapping lines in the EDI output. Valid values:</p> <ul> <li> <p> <code>SEGMENT</code>: Wraps by segment.</p> </li> <li> <p> <code>ONE_LINE</code>: Indicates that the entire content is on a single line.</p> <note> <p>When you specify <code>ONE_LINE</code>, do not provide either the line length nor the line terminator value.</p> </note> </li> <li> <p> <code>LINE_LENGTH</code>: Wraps by character count, as specified by <code>lineLength</code> value.</p> </li> </ul>"""
    line_terminator: NotRequired["capo_b2bi.types.line_terminator.LineTerminator"]
    """<p>Specifies the character sequence used to terminate lines when wrapping. Valid values:</p> <ul> <li> <p> <code>CRLF</code>: carriage return and line feed</p> </li> <li> <p> <code>LF</code>: line feed)</p> </li> <li> <p> <code>CR</code>: carriage return</p> </li> </ul>"""
    line_length: NotRequired["capo_b2bi.types.line_length.LineLength"]
    """<p>Specifies the maximum length of a line before wrapping occurs. This value is used when <code>wrapBy</code> is set to <code>LINE_LENGTH</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WrapOptions) -> dict:
    out: dict = {}
    import capo_b2bi.types.wrap_format

    out["wrapBy"] = capo_b2bi.types.wrap_format.serialize_aws_json_1_0(value["wrap_by"])
    if "line_terminator" in value:
        import capo_b2bi.types.line_terminator

        out["lineTerminator"] = capo_b2bi.types.line_terminator.serialize_aws_json_1_0(
            value["line_terminator"]
        )
    if "line_length" in value:
        out["lineLength"] = value["line_length"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WrapOptions:
    out: WrapOptions = {}  # type: ignore[typeddict-item]
    if data.get("wrapBy") is not None:
        import capo_b2bi.types.wrap_format

        out["wrap_by"] = capo_b2bi.types.wrap_format.deserialize_aws_json_1_0(
            data["wrapBy"]
        )
    else:
        import typing

        out["wrap_by"] = typing.cast("capo_b2bi.types.wrap_format.WrapFormat", "")
    if data.get("lineTerminator") is not None:
        import capo_b2bi.types.line_terminator

        out["line_terminator"] = (
            capo_b2bi.types.line_terminator.deserialize_aws_json_1_0(
                data["lineTerminator"]
            )
        )
    if data.get("lineLength") is not None:
        out["line_length"] = data["lineLength"]
    return out

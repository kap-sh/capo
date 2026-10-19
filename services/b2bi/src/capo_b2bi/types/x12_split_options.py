"""Generated from Smithy shape ``com.amazonaws.b2bi#X12SplitOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.x12_split_by


class X12SplitOptions(TypedDict, closed=True):
    split_by: "capo_b2bi.types.x12_split_by.X12SplitBy"
    """<p>Specifies the method used to split X12 EDI files. Valid values include <code>TRANSACTION</code> (split by individual transaction sets), or <code>NONE</code> (no splitting).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12SplitOptions) -> dict:
    out: dict = {}
    import capo_b2bi.types.x12_split_by

    out["splitBy"] = capo_b2bi.types.x12_split_by.serialize_aws_json_1_0(
        value["split_by"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12SplitOptions:
    out: X12SplitOptions = {}  # type: ignore[typeddict-item]
    if data.get("splitBy") is not None:
        import capo_b2bi.types.x12_split_by

        out["split_by"] = capo_b2bi.types.x12_split_by.deserialize_aws_json_1_0(
            data["splitBy"]
        )
    else:
        import typing

        out["split_by"] = typing.cast("capo_b2bi.types.x12_split_by.X12SplitBy", "")
    return out

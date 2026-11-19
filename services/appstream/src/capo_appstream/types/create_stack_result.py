"""Generated from Smithy shape ``com.amazonaws.appstream#CreateStackResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.stack


class CreateStackResult(TypedDict, closed=True):
    stack: NotRequired["capo_appstream.types.stack.Stack"]
    """<p>Information about the stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStackResult) -> dict:
    out: dict = {}
    if "stack" in value:
        import capo_appstream.types.stack

        out["Stack"] = capo_appstream.types.stack.serialize_aws_json_1_1(value["stack"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStackResult:
    out: CreateStackResult = {}  # type: ignore[typeddict-item]
    if data.get("Stack") is not None:
        import capo_appstream.types.stack

        out["stack"] = capo_appstream.types.stack.deserialize_aws_json_1_1(
            data["Stack"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateStackResult) -> dict:
    out: dict = {}
    if "stack" in value:
        import capo_appstream.types.stack

        out["Stack"] = capo_appstream.types.stack.serialize_cbor(value["stack"])
    return out


def deserialize_cbor(data: dict) -> CreateStackResult:
    out: CreateStackResult = {}  # type: ignore[typeddict-item]
    if data.get("Stack") is not None:
        import capo_appstream.types.stack

        out["stack"] = capo_appstream.types.stack.deserialize_cbor(data["Stack"])
    return out

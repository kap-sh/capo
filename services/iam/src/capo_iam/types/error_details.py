"""Generated from Smithy shape ``com.amazonaws.iam#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.string_type


class ErrorDetails(TypedDict, closed=True):
    message: "capo_iam.types.string_type.stringType"
    """<p>Detailed information about the reason that the operation failed.</p>"""
    code: "capo_iam.types.string_type.stringType"
    """<p>The error code associated with the operation failure.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ErrorDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Message", str(value["message"])))
    pairs.append((f"{key_prefix}Code", str(value["code"])))


def deserialize_query(el: Element) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        out["message"] = ""
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    else:
        out["code"] = ""
    return out

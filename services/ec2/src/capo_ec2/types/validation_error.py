"""Generated from Smithy shape ``com.amazonaws.ec2#ValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ValidationError(TypedDict, closed=True):
    code: NotRequired["capo_ec2.types.string.String"]
    """<p>The error code that indicates why the parameter or parameter combination is not valid. For more information about error codes, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html">Error codes</a>.</p>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>The error message that describes why the parameter or parameter combination is not valid. For more information about error messages, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html">Error codes</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ValidationError, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        pairs.append((f"{key_prefix}Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> ValidationError:
    out: ValidationError = {}  # type: ignore[typeddict-item]
    child_code = el.find("code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out

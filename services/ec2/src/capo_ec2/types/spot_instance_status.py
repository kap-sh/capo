"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string


class SpotInstanceStatus(TypedDict, closed=True):
    code: NotRequired["capo_ec2.types.string.String"]
    """<p>The status code. For a list of status codes, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html#spot-instance-request-status-understand">Spot request status codes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>The description for the status code.</p>"""
    update_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time of the most recent status update, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotInstanceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        pairs.append((f"{key_prefix}Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))
    if "update_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["update_time"], pairs, f"{key_prefix}UpdateTime"
        )


def deserialize_ec2_query(el: Element) -> SpotInstanceStatus:
    out: SpotInstanceStatus = {}  # type: ignore[typeddict-item]
    child_code = el.find("code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_update_time = el.find("updateTime")
    if child_update_time is not None:
        import capo_ec2.types.date_time

        out["update_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_update_time
        )
    return out

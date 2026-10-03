"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorSessionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.traffic_mirror_session


class CreateTrafficMirrorSessionResult(TypedDict, closed=True):
    traffic_mirror_session: NotRequired[
        "capo_ec2.types.traffic_mirror_session.TrafficMirrorSession"
    ]
    """<p>Information about the Traffic Mirror session.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">How to ensure idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTrafficMirrorSessionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_session" in value:
        import capo_ec2.types.traffic_mirror_session

        capo_ec2.types.traffic_mirror_session.serialize_ec2_query(
            value["traffic_mirror_session"], pairs, f"{key_prefix}TrafficMirrorSession"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateTrafficMirrorSessionResult:
    out: CreateTrafficMirrorSessionResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_session = el.find("trafficMirrorSession")
    if child_traffic_mirror_session is not None:
        import capo_ec2.types.traffic_mirror_session

        out["traffic_mirror_session"] = (
            capo_ec2.types.traffic_mirror_session.deserialize_ec2_query(
                child_traffic_mirror_session
            )
        )
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out

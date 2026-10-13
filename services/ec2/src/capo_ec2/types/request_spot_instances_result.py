"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotInstancesResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_instance_request_list


class RequestSpotInstancesResult(TypedDict, closed=True):
    spot_instance_requests: NotRequired[
        "capo_ec2.types.spot_instance_request_list.SpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "spot_instance_requests" in value:
        import capo_ec2.types.spot_instance_request_list

        capo_ec2.types.spot_instance_request_list.serialize_ec2_query(
            value["spot_instance_requests"],
            pairs,
            f"{key_prefix}SpotInstanceRequestSet",
        )


def deserialize_ec2_query(el: Element) -> RequestSpotInstancesResult:
    out: RequestSpotInstancesResult = {}  # type: ignore[typeddict-item]
    child_spot_instance_requests = el.find("spotInstanceRequestSet")
    if child_spot_instance_requests is not None:
        import capo_ec2.types.spot_instance_request_list

        out["spot_instance_requests"] = (
            capo_ec2.types.spot_instance_request_list.deserialize_ec2_query(
                child_spot_instance_requests
            )
        )
    return out


def redact_sensitive(value: RequestSpotInstancesResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spot_instance_requests" in value:
        import capo_ec2.types.spot_instance_request_list

        out["spot_instance_requests"] = (
            capo_ec2.types.spot_instance_request_list.redact_sensitive(
                value["spot_instance_requests"]
            )
        )
    return out

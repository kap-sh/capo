"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceAccessDetailsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_access_details


class GetInstanceAccessDetailsResult(TypedDict, closed=True):
    access_details: NotRequired[
        "capo_lightsail.types.instance_access_details.InstanceAccessDetails"
    ]
    """<p>An array of key-value pairs containing information about a get instance access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceAccessDetailsResult) -> dict:
    out: dict = {}
    if "access_details" in value:
        import capo_lightsail.types.instance_access_details

        out["accessDetails"] = (
            capo_lightsail.types.instance_access_details.serialize_aws_json_1_1(
                value["access_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceAccessDetailsResult:
    out: GetInstanceAccessDetailsResult = {}  # type: ignore[typeddict-item]
    if data.get("accessDetails") is not None:
        import capo_lightsail.types.instance_access_details

        out["access_details"] = (
            capo_lightsail.types.instance_access_details.deserialize_aws_json_1_1(
                data["accessDetails"]
            )
        )
    return out


def redact_sensitive(value: GetInstanceAccessDetailsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_details" in value:
        import capo_lightsail.types.instance_access_details

        out["access_details"] = (
            capo_lightsail.types.instance_access_details.redact_sensitive(
                value["access_details"]
            )
        )
    return out
